Rails.application.routes.draw do
  get 'user_groups/index'
  post 'user_groups/', to: 'user_groups#create'
  get 'user_groups/new'

  devise_for :users
  get 'bookings/', to: 'bookings#index'
  post 'bookings/', to: 'bookings#create'

  get 'bookings/new'

  get 'bookings/create'

  get 'bookings/delete'

  get 'fingerprints/', to: 'fingerprints#index'
  root to: 'home#index'
  mount ActionCable.server => '/cable'
end
