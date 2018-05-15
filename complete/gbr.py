#!/usr/bin/env python3
import glob
import matplotlib.pyplot as plt
import numpy as np
from optparse import OptionParser
import scipy.misc as misc
import scipy.ndimage as ndimage

import utils2
from os import listdir
from os.path import isfile, join
import os

parser = OptionParser(usage="%prog [options] sourceimage [destinationimage]")

parser.add_option("-i", dest="images", default=0, action="count",
        help="Show intermediate images.")

parser.add_option("-s", "--subdivide", dest="subdivide",
        default=False, action="store_true",
        help="Iterate the image by subdividing areas.")

parser.add_option("-d", "--dry-run", dest="dryrun", default=False, action="store_true",
        help="Do not save the result.")

parser.add_option("-b", "--no-binarization", dest="binarize", default=True, action="store_false",
        help="Use this option to disable the final binarization step")

options, args = parser.parse_args()


def gaborKernel(size, angle, frequency):
    """
    Create a Gabor kernel given a size, angle and frequency.
    Code is taken from https://github.com/rtshadow/biometrics.git
    """

    angle += np.pi * 0.5
    cos = np.cos(angle)
    sin = -np.sin(angle)

    yangle = lambda x, y: x * cos + y * sin
    xangle = lambda x, y: -x * sin + y * cos

    xsigma = ysigma = 4

    return utils2.kernelFromFunction(size, lambda x, y:
            np.exp(-(
                (xangle(x, y) ** 2) / (xsigma ** 2) +
                (yangle(x, y) ** 2) / (ysigma ** 2)) / 2) *
            np.cos(2 * np.pi * frequency * xangle(x, y)))

def gaborFilter(image, orientations, frequencies, w=32):
    result = np.empty(image.shape)

    height, width = image.shape
    for y in range(0, height - w, w):
        for x in range(0, width - w, w):
            orientation = orientations[y+w//2, x+w//2]
            frequency = utils2.averageFrequency(frequencies[y:y+w, x:x+w])

            if frequency < 0.0:
                result[y:y+w, x:x+w] = image[y:y+w, x:x+w]
                continue

            kernel = gaborKernel(16, orientation, frequency)
            result[y:y+w, x:x+w] = utils2.convolve(image, kernel, (y, x), (w, w))

    return utils2.normalize(result)


def gaborFilterSubdivide(image, orientations, frequencies, rect=None):
    if rect:
        y, x, h, w = rect
    else:
        y, x = 0, 0
        h, w = image.shape

    result = np.empty((h, w))

    orientation, deviation = utils2.averageOrientation(
            orientations[y:y+h, x:x+w], deviation=True)

    if (deviation < 0.2 and h < 50 and w < 50) or h < 6 or w < 6:
        #print(deviation)
        #print(rect)

        frequency = utils2.averageFrequency(frequencies[y:y+h, x:x+w])

        if frequency < 0.0:
            result = image[y:y+h, x:x+w]
        else:
            kernel = gaborKernel(16, orientation, frequency)
            result = utils2.convolve(image, kernel, (y, x), (h, w))

    else:
        if h > w:
            hh = h // 2

            result[0:hh, 0:w] = \
                    gaborFilterSubdivide(image, orientations, frequencies, (y, x, hh, w))

            result[hh:h, 0:w] = \
                    gaborFilterSubdivide(image, orientations, frequencies, (y + hh, x, h - hh, w))
        else:
            hw = w // 2

            result[0:h, 0:hw] = \
                    gaborFilterSubdivide(image, orientations, frequencies, (y, x, h, hw))

            result[0:h, hw:w] = \
                    gaborFilterSubdivide(image, orientations, frequencies, (y, x + hw, h, w - hw))



    if w > 20 and h > 20:
        result = utils2.normalize(result)

    return result


if __name__ == '__main__':
    np.set_printoptions(
            threshold=np.inf,
            precision=4,
            suppress=True)

    print("Reading image")
    image_dir_path = "./new/"
    image_file_names = [f for f in listdir("./new") if isfile(join(image_dir_path, f)) and f != ".DS_Store"]
    for img in image_file_names:
        destinationImage = image_dir_path + img
        image = ndimage.imread(image_dir_path + img, mode="L").astype("float64")
        if options.images > 0:
            utils2.showImage(image, "original", vmax=255.0)

        print("Normalizing")
        image = utils2.normalize(image)
        if options.images > 1:
            utils2.showImage(image, "normalized")

        print("Finding mask")
        mask = utils2.findMask(image)
        if options.images > 1:
            utils2.showImage(mask, "mask")

        print("Applying local normalization")
        image = np.where(mask == 1.0, utils2.localNormalize(image), image)
        if options.images > 1:
            utils2.showImage(image, "locally normalized")

        print("Estimating orientations")
        orientations = np.where(mask == 1.0, utils2.estimateOrientations(image), -1.0)
        if options.images > 0:
            utils2.showOrientations(image, orientations, "orientations", 8)

        print("Estimating frequencies")
        frequencies = np.where(mask == 1.0, utils2.estimateFrequencies(image, orientations), -1.0)
        if options.images > 1:
            utils2.showImage(utils2.normalize(frequencies), "frequencies")

        print("Filtering")
        if options.subdivide:
            image = utils2.normalize(gaborFilterSubdivide(image, orientations, frequencies))
        else:
            image = gaborFilter(image, orientations, frequencies)
        image = np.where(mask == 1.0, image, 1.0)
        if options.images > 0:
            utils2.showImage(image, "gabor")

        if options.binarize:
            print("Binarizing")
            image = np.where(mask == 1.0, utils2.binarize(image), 1.0)
            if options.images > 0:
                utils.showImage(image, "binarized")

        if options.images > 0:
            plt.show()

        if not options.dryrun:
            misc.imsave(destinationImage, image)