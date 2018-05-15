class CardChannel < ApplicationCable::Channel
  def subscribed
    stream_from "card_channel"
  end

  def unsubscribed
    # Any cleanup needed when channel is unsubscribed
  end

  def scan(data)
  	# ActionCable.server.broadcast(
   #    'face_channel', 
   #    message: data['message']
   #  )
  end
end
