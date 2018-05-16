# Create face encodings for images directory
from scipy import misc
import tensorflow as tf
import numpy as np
import sys
import os
import copy
import facenet
import align.detect_face

from os import listdir
from os.path import isfile, join

with tf.Graph().as_default():
    gpu_options = tf.GPUOptions(per_process_gpu_memory_fraction=1.0)
    alignSess = tf.Session(config=tf.ConfigProto(gpu_options=gpu_options, log_device_placement=False))
    with alignSess.as_default():
        pnet, rnet, onet = align.detect_face.create_mtcnn(alignSess, None)

def load_and_align_data(image_paths, image_size, margin, gpu_memory_fraction):
    minsize = 20 # minimum size of face
    threshold = [ 0.6, 0.7, 0.7 ]  # three steps's threshold
    factor = 0.709 # scale factor
    
    print('Creating networks and loading parameters')
    
  
    tmp_image_paths=copy.copy(image_paths)
    img_list = []
    for image in tmp_image_paths:
        img = misc.imread(os.path.expanduser(image), mode='RGB')
        img_size = np.asarray(img.shape)[0:2]
        bounding_boxes, _ = align.detect_face.detect_face(img, minsize, pnet, rnet, onet, threshold, factor)
        if len(bounding_boxes) < 1:
          image_paths.remove(image)
          print("can't detect face, remove ", image)
          continue
        det = np.squeeze(bounding_boxes[0,0:4])
        bb = np.zeros(4, dtype=np.int32)
        bb[0] = np.maximum(det[0]-margin/2, 0)
        bb[1] = np.maximum(det[1]-margin/2, 0)
        bb[2] = np.minimum(det[2]+margin/2, img_size[1])
        bb[3] = np.minimum(det[3]+margin/2, img_size[0])
        cropped = img[bb[1]:bb[3],bb[0]:bb[2],:]
        aligned = misc.imresize(cropped, (image_size, image_size), interp='bilinear')
        prewhitened = facenet.prewhiten(aligned)
        img_list.append(prewhitened)
    images = np.stack(img_list)
    return images

def create_encoding(sess, image_path):
    image = load_and_align_data([image_path], 160, 44, 1.0)
    feed_dict = { images_placeholder: image, phase_train_placeholder:False }
    emb = sess.run(embeddings, feed_dict=feed_dict)
    return emb[0]

def who_is_it(sess, database, image_path):
	new_face = create_encoding(sess, image_path)
	score = 2
	min_score = 2
	user = None
	for username in database:
		face = database[username]
		score = np.linalg.norm(new_face - face)
		if score < min_score:
			min_score = score
			if score < 0.9:
				user = username
	print(min_score)
	return user




image_dir_path = "./data/images/"
model_path = "./models/facenet"
image_file_names = [ (image_dir_path + f) for f in listdir(image_dir_path) if isfile(join(image_dir_path, f)) and f != ".DS_Store"]
image_size = 160
margin = 44
gpu_memory_fraction = 1.0
images = load_and_align_data(image_file_names, image_size, margin, gpu_memory_fraction)

graph = tf.Graph()
dgraph = graph.as_default()
dgraph.__enter__()
sess = tf.InteractiveSession()
  
# Load the model
facenet.load_model(model_path)

# Get input and output tensors
images_placeholder = tf.get_default_graph().get_tensor_by_name("input:0")
embeddings = tf.get_default_graph().get_tensor_by_name("embeddings:0")
phase_train_placeholder = tf.get_default_graph().get_tensor_by_name("phase_train:0")

# Run forward pass to calculate embeddings
feed_dict = { images_placeholder: images, phase_train_placeholder:False }

def retrain():
    global embeddings
    global feed_dict
    global image_file_names
    global image_dir_path
    global model_path
    global images
    images = load_and_align_data(image_file_names, image_size, margin, gpu_memory_fraction)

    image_file_names = [ (image_dir_path + f) for f in listdir(image_dir_path) if isfile(join(image_dir_path, f)) and f != ".DS_Store"]
    feed_dict = { images_placeholder: images, phase_train_placeholder:False }

    emb = sess.run(embeddings, feed_dict=feed_dict)

    nrof_images = len(image_file_names)

    print('Images:')
    for i in range(nrof_images):
        print('%1d: %s' % (i, image_file_names[i]))
    print('')

    print('Creating database dictionary')
    database = dict()
    image_file_names = list(filter(lambda x: x != "./data/images/new.jpg", image_file_names))
    for i,v in enumerate(image_file_names):
        filename, file_extension = os.path.splitext(v)
        filename = filename.split("/")[3]
        if(file_extension == ".jpg" and filename != "new" and filename != "newAligned"):
            print(filename, i)
            database[filename] = emb[i]
    return database


# MIT License
# 
# Copyright (c) 2016 David Sandberg. Modified by Hassan Al-ubeidi (under MIT license).
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
