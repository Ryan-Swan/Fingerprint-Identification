validFace = false
App.face = App.cable.subscriptions.create("FaceChannel", {
  connected() {},
    // Called when the subscription is ready for use on the server

  disconnected() {},
    // Called when the subscription has been terminated by the server

  received(data) {
    switch(data['message']) {
      case "Not recognised":
          console.log("InValid!");
          // $(".door-unlocked").hide()
          $(".door-locked").show()
          $(".waiting").hide()
          $(".loader").hide()
          // setTimeout(() => window.location = "/?message=Valid", 2500)
          break
      default:
        if(data["message"].match("Face: ")) {
          word = data['message'].match("(?<=: ).*$")[0]
          $("#user-name").text(" - " + word)
          $(".door-locked").hide()
          $(".door-unlocked").show()
          console.log("Valid!");
          $(".loader").hide()
          $(".waiting").hide()
          validFace = true
          setTimeout(() =>  window.location = "/?message=Valid", 500)
         
        } else if(data["message"] == "Registered") {
          window.location = "/?message='Registered user'"
        }
        console.log(data["message"])
        break
    }
  },

  scan(message) {
    return this.perform('scan', {message});
  },
  authenticate(message) {
    return this.perform('authenticate', {message});
  }
}
);
