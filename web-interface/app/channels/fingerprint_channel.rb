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
      # if User.all.count > 500 then
      #   #pre process & classify
      #   #send value to pc database
      # else
        # ActionCable.server.broadcast(
        #   'fingerprint_channel', 
        #     message: "Classify"
        #   )
      # end
    end

    if data['message'] == "Scanned fingerprint" then
      ActionCable.server.broadcast(
        'fingerprint_channel', 
        message: "Validate Fingerprint"
      )
    end

  end
end