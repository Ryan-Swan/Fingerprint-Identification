class FaceChannel < ApplicationCable::Channel
  def subscribed
    stream_from "face_channel"
  end

  def unsubscribed
    # Any cleanup needed when channel is unsubscribed
  end

  def scan(data)
    ActionCable.server.broadcast(
      'face_channel', 
      message: "Recieved faceprint"
    )
		File.open('/Users/hassan-alubeidi/keras-face/demo/data/images/new.jpg', 'wb') do|f|
			f.write(Base64.decode64(data['message'].gsub(/data:image\/jpeg;base64,/, "")))
		end
  end

  def authenticate(data)
    ActionCable.server.broadcast(
      'face_channel', 
      message: data['message']
    )
  end
end