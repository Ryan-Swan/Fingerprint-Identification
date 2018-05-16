require 'rails_helper'

RSpec.describe AdminController, type: :controller do

  describe "GET #index" do
    it "returns http success" do
      get :index
      expect(response).to have_http_status(:success)
    end
  end

  describe "GET #bookings" do
    it "returns http success" do
      get :bookings
      expect(response).to have_http_status(:success)
    end
  end

  describe "GET #log" do
    it "returns http success" do
      get :log
      expect(response).to have_http_status(:success)
    end
  end

end
