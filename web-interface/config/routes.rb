Rails.application.routes.draw do
  get 'bookings/index'

  get 'bookings/new'

  get 'bookings/create'

  get 'bookings/delete'

  get 'fingerprints/', to: 'fingerprints#index'
  get 'home/index'
  mount ActionCable.server => '/cable'
end
