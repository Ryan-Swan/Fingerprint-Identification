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

App.fingerprint = App.cable.subscriptions.create("FingerprintChannel", {
  connected() {},
    // Called when the subscription is ready for use on the server

  disconnected() {},
    // Called when the subscription has been terminated by the server

  received(data) {
    
    if(data['message'] == "Scanned fingerprint")
    	if(findGetParameter("scanned") != "true") {
        	window.location = "/fingerprints?scanned=true&loading=true";
    	}
        else 
        	document.getElementsByTagName("img")[0].src= "/assets/outputimage.png?" + Date.now()
	        
    else if(data['message'] == "Valid authentication")
        console.log("Valid!");
        
    else if(data['message'] == "Invalid authentication")
        console.log("InValid!");
  },

  scan(message) {
    return this.perform('scan', {message});
  }
}
);
