class FingerprintChannel < ApplicationCable::Channel
  def subscribed
    stream_from "fingerprint_channel"
  end

  def unsubscribed
    # Any cleanup needed when channel is unsubscribed
  end

  def scan(data)
  	ActionCable.server.broadcast(
  		'fingerprint_channel', 
  		message: data['message']
  	)
    if data['message'].match(/Base 64 Image: /) then
      File.open('./app/assets/images/outputimage.png', 'wb') do|f|
        f.write(Base64.decode64(data['message'].gsub(/Base 64 Image: /, "")))
      end
    end
    
  end
end