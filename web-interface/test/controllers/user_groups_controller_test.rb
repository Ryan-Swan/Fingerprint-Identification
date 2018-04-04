require 'test_helper'

class UserGroupsControllerTest < ActionDispatch::IntegrationTest
  test "should get index" do
    get user_groups_index_url
    assert_response :success
  end

  test "should get new" do
    get user_groups_new_url
    assert_response :success
  end

end
