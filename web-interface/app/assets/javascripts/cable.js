// Action Cable provides the framework to deal with WebSockets in Rails.
// You can generate new channels where WebSocket features live using the `rails generate channel` command.
//
//= require action_cable
//= require_self
//= require_tree ./channels

(function() {
  this.App || (this.App = {});

  App.cable = ActionCable.createConsumer();


}).call(this);

setTimeout(() => {
	App.subscriptions = {}
  keys = App.cable.subscriptions.subscriptions.map((x) =>
  	JSON.parse(x.identifier).channel
  ).map( (key, index) => {
  	App.subscriptions[key] = App.cable.subscriptions.subscriptions[index]
  })
},2000)