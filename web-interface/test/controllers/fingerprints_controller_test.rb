require 'test_helper'

class FingerprintsControllerTest < ActionDispatch::IntegrationTest
  test "should get index" do
    get fingerprints_index_url
    assert_response :success
  end

end
