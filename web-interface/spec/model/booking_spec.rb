require "rails_helper"

RSpec.describe Booking, :type => :model do
	describe "#current_bookings when" do
		context "booking exists at current time" do
			it "returns the current booking"
		end
		context "booking doesn't exist currently" do
			it "returns nil"
		end
	end
end