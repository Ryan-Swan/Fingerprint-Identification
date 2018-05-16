class FingerprintsController < ApplicationController
  def index
  end
  def new
  	@user = User.find_by(card_id: params["card_id"])
  end
end
