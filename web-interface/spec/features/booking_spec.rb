require "rails_helper"

RSpec.feature "Booking", :type => :feature do
	describe "Authentication" do 
		context "not signed in" do
			it "redirects with 403"
		end
		context "signed in as non staff" do
			it "redirects with 403"
		end
		context "signed in as staff" do
			it "lets user through to bookings section"
		end
	end
	describe "Creating booking" do
		context "no current booking" do 
		end
		context "current booking exists" do 
		end
	end
end