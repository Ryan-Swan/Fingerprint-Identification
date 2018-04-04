class BookingsController < ApplicationController
	before_action :authenticate_user!
  def index
  	@bookings = (0..6).map {|i| Date.today.at_beginning_of_week + i }
  	@bookings = @bookings.map {|datetime| Booking.where(start: datetime.all_day, end: datetime.all_day)}


  end

  def new
  end

  def create
  	date_format = "%m/%d/%Y %l:%M %p"
  	start_time = DateTime.strptime(params["start"], date_format)
  	end_date = DateTime.strptime(params["end"], date_format)
  	permissions = params["permissions"]
  	user_group = params["user-group"]
  	Booking.create!({
  		start: start_time,
  		end: end_date,
  		permissions: permissions,
  		user_group_id: user_group
  	})
  end

  def delete
  end
end
