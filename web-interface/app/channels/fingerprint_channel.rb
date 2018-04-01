class FingerprintChannel < ApplicationCable::Channel
  def subscribed
    stream_from "fingerprint_channel"
  end

  def unsubscribed
    # Any cleanup needed when channel is unsubscribed
  end

  def scan(data)
  	ActionCable.server.broadcast('messages',
      message: render_message(data['message']))
  end
end
