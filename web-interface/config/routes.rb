Rails.application.routes.draw do
  devise_for :users
  get 'bookings/index'

  get 'bookings/new'

  get 'bookings/create'

  get 'bookings/delete'

  get 'fingerprints/', to: 'fingerprints#index'
  root to: 'home#index'
  mount ActionCable.server => '/cable'
end
