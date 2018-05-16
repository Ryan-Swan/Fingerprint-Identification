class FacesController < ApplicationController
  def index
  end
  def new
  	@user = User.find_by(card_id: params["card_id"])
  end
  def create
  	@user = User.find_by(card_id: params["card_id"])
  	base_64_image = params["imageData"].gsub(/data:image\/jpeg;base64,/, "")
  	ActionCable.server.broadcast(
      'face_channel', 
      message: "Register face: " + @user.username + " | " + base_64_image
    )
    redirect_to root_path
  end
end
