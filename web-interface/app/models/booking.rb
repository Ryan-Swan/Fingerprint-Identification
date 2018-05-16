class Booking < ApplicationRecord
	belongs_to :user_group
	def self.current_booking
		Booking.all.each do |booking|
			if booking.start < Time.zone.now && booking.end > Time.zone.now
				return booking
			end
		end
		return nil
	end
end
