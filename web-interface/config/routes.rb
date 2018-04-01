Rails.application.routes.draw do
  get 'home/index'
  mount ActionCable.server => '/cable'
end
