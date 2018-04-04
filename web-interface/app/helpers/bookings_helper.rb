module BookingsHelper
	def booking_colour(booking)
		if booking.permissions == "default"
			return ""
		elsif booking.permissions == "non-anonymous"
			return "blue"
		elsif booking.permissions == "exam-style"
			return "red"
		elsif booking.permissions == "staff-only"
			return "orange"
		end
	end
end
