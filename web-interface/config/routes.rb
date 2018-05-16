Rails.application.routes.draw do
  get 'admin/', to: 'admin#index'

  get 'admin/settings'
  post 'admin/create_card'

  get 'admin/log'

  get 'cards/index'

  get 'cards/register_fingerprint'

  get 'faces/new'

  post 'faces/', to: "faces#create"

  get 'faces/', to: 'faces#index'

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
  get 'fingerprints/new', to: 'fingerprints#new'

  root to: 'home#index'
  mount ActionCable.server => '/cable'
end
