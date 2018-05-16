App.fingerprint = App.cable.subscriptions.create("FingerprintChannel", {
  connected() {},
    // Called when the subscription is ready for use on the server

  disconnected() {},
    // Called when the subscription has been terminated by the server

  received(data) {
  	valid = false
  	if(window.location.pathname == "/fingerprints" || window.location.pathname == "/fingerprints/")
    switch(data['message']) {
	    case "Scanned fingerprint":
	    	$(".waiting-for-fingerprint").hide()
	    	$(".waiting-for-match").show()
	    	$(".waiting").show()
	        $(".loader").show()
	        document.getElementsByTagName("img")[0].src= ""
	    	document.getElementsByTagName("img")[0].src= "/assets/outputimage.png?" + Date.now()
		 	break
	    case "Valid authentication":
	        console.log("Valid!");
	        valid = true
	        $(".door-locked").hide()
	        $(".door-unlocked").show()
	        $(".loader").hide()
	        $(".waiting").hide()
	        setTimeout( () => {
	        	$(".door-locked").hide()
		        $(".door-unlocked").show()
		        $(".loader").hide()
		        $(".waiting").hide()
	        }, 200)
	        setTimeout( () => window.location = "/?message=Valid!", 1000 )
		    break
	    case "Invalid authentication":
	    	if(!valid) {
		        console.log("InValid!");
		        $(".door-unlocked").hide()
		        $(".door-locked").show()
		        $(".waiting").hide()
		        $(".loader").hide()
		    }
	        break
	    case "Timeout":
	    	 
	    	 setTimeout( () => window.location = "/?message=Invalid", 1200)
	    default:
	    	break
    }
    if(window.location.pathname == "/fingerprints/new") {
    	console.log(data['message'])
	    switch(data['message']) {
		    case "Scanned fingerprint":
		    	$(".waiting-for-fingerprint").hide()
		    	$(".waiting-for-match").show()
		    	$(".waiting").show()
		        $(".loader").show()
		        document.getElementsByTagName("img")[0].src= ""
		    	document.getElementsByTagName("img")[0].src= "/assets/outputimage.png?" + Date.now()
			 	break
		    // case "Valid authentication":
		    //     console.log("Valid!");
		    //     $(".door-locked").hide()
		    //     $(".door-unlocked").show()
		    //     $(".loader").hide()
		    //     $(".waiting").hide()
		        
		    //     window.location = "/"
			   //  break
		    // case "Invalid authentication":
		    //     console.log("InValid!");
		    //     $(".door-unlocked").hide()
		    //     $(".door-locked").show()
		    //     $(".waiting").hide()
		    //     $(".loader").hide()
		    //     break
		    default:
		    	break
	    }
	    if(data['message'].split(":")[0] == "Registered user") {
	    	console.log("Valid!");
	        $(".door-locked").hide()
	        $(".door-unlocked").show()
	        $(".loader").hide()
	        $(".waiting").hide()
	        setTimeout(() => window.location = "/faces/new?card_id=" + cardId, 1000)
	    }
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
