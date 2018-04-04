class UserGroupsController < ApplicationController
  before_action :authenticate_user!
  def index
  end

  def new
  end
  def create
  	group_name = params["name"]
  	users = params["users"].split(",")
  	UserGroup.create(name: group_name, users: users.map {|id|User.find(id)})
  end
end
