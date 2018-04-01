Rails.application.routes.draw do
  get 'fingerprints/', to: 'fingerprints#index'
  get 'home/index'
  mount ActionCable.server => '/cable'
end
