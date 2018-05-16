class AdminController < ApplicationController
	# skip_before_filter :verify_authenticity_token 
	skip_before_action :verify_authenticity_token
  def index
  end

  def settings
  end

  def log
  end

  def create_card
  	begin
	  	User.create!({
	  		username: params["name"],
	  		email: "#{params["name"]}@#{params["name"]}.com",
	  		card_id: params["name"],
	  		password: "password"
	  	})
	rescue 
	end
  	redirect_to "/"
  end
end
