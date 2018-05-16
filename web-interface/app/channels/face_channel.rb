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
      message: "Recieved faceprint: " + data['message'].gsub(/data:image\/jpeg;base64,/, "")
    )
  end

  def authenticate(data)
    ActionCable.server.broadcast(
      'face_channel', 
      message: data['message']
    )
    AuthenticationLog.create({user_id: user.find_by(data['message']).id})
  end

  def register(data)
    ActionCable.server.broadcast(
      'face_channel', 
      message: data['message']
    )
  end
end