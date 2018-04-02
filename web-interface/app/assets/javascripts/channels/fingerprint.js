App.fingerprint = App.cable.subscriptions.create("FingerprintChannel", {
  connected() {},
    // Called when the subscription is ready for use on the server

  disconnected() {},
    // Called when the subscription has been terminated by the server

  received(data) {
    
    if(data['message'] == "Scanned fingerprint") {
    	$(".waiting-for-fingerprint").hide()
    	$(".waiting-for-match").show()
    	$(".waiting").show()
        $(".loader").show()
        document.getElementsByTagName("img")[0].src= ""
    	document.getElementsByTagName("img")[0].src= "/assets/outputimage.png?" + Date.now()
	}        
    else if(data['message'] == "Valid authentication") {
        console.log("Valid!");
        $(".door-locked").hide()
        $(".door-unlocked").show()
        $(".loader").hide()
        $(".waiting").hide()
        window.location = "/fingerprints"
    }
        
    else if(data['message'] == "Invalid authentication") {
        console.log("InValid!");
        $(".door-unlocked").hide()
        $(".door-locked").show()
        $(".waiting").hide()
        $(".loader").hide()
    }
  },

  scan(message) {
    return this.perform('scan', {message});
  }
}
);

function findGetParameter(parameterName) {
    var result = null,
        tmp = [];
    location.search
        .substr(1)
        .split("&")
        .forEach(function (item) {
          tmp = item.split("=");
          if (tmp[0] === parameterName) result = decodeURIComponent(tmp[1]);
        });
    return result;
}
