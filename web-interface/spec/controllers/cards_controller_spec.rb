require 'rails_helper'

RSpec.describe CardsController, type: :controller do

  describe "GET #index" do
    it "returns http success" do
      get :index
      expect(response).to have_http_status(:success)
    end
  end

  describe "GET #register_fingerprint" do
    it "returns http success" do
      get :register_fingerprint
      expect(response).to have_http_status(:success)
    end
  end

  describe "GET #register_face" do
    it "returns http success" do
      get :register_face
      expect(response).to have_http_status(:success)
    end
  end

end
