require "rails_helper"

RSpec.feature "Fingerprints", :type => :feature do
    describe "scanning" do
    	context "fingerprint scanned correctly" do
    		it "sets state to validating"
    	end
    end
  
    describe "validating" do
    	context "fingerprint is valid" do
    		it "sends unlock signal"
    		it "updates page to show user is authenticated"
    		it "resets to scanning"
    	end
    	context "fingerprint is invalid" do
    		it "dosen't send unlock signal"
    		it "resets to scanning"
    	end
    end
end