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
  	end_time = DateTime.strptime(params["end"], date_format)
  	permissions = params["permissions"]
  	user_group = params["user-group"]
  	recurring = params["recurring"]
  	frequency_peroid = params["frequency-peroid"]  
  	frequency_number = params["frequency-number"].to_i
  	Booking.where("start > ?", Time.zone.now).each do |booking|
  		if  start_time.between?(booking.start, booking.end) && 
  			end_time.between?(booking.start, booking.end)
  		then
  			raise "Booking exists during this time"
  		end
  	end
  	if recurring == "1" then
  		case frequency_peroid
	  		when "Day"
	  			frequency = 1.day
	  		when "Week"
	  			frequency = 1.week
	  		when "Month"
	  			frequency = 1.month
	  		else
	  			frequency = 1.day
	  	end
  		(0..(frequency_number)).each do |booking_number|
  			Booking.create!({
		  		start: start_time + (booking_number * frequency),
		  		end: end_time + (booking_number * frequency),
		  		permissions: permissions,
		  		user_group_id: user_group
		  	})
  		end
  	else
  		Booking.create!({
	  		start: start_time,
	  		end: end_time,
	  		permissions: permissions,
	  		user_group_id: user_group
	  	})
	end
   	
  end

  def delete
  end
end
