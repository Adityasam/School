var granted = false;

function ask_location_permission() {
  if (navigator.geolocation) {
    navigator.permissions
      .query({ name: "geolocation" })
      .then(function (result) {
        if (result.state === "granted") {
          console.log("Geolocation permission granted.");
          granted = true;
          // Code to retrieve location goes here
        } else if (result.state === "prompt") {
          navigator.geolocation.getCurrentPosition(
            function (position) {
              console.log("Geolocation permission granted.");
              granted = true;
              // Code to retrieve location goes here
            },
            function () {
              console.log("Geolocation permission denied.");
            }
          );
        } else if (result.state === "denied") {
          console.log("Geolocation permission denied.");
        }
      });
  } else {
    console.log("Geolocation is not supported by this browser.");
  }
}

function get_location() {
  if (navigator.geolocation) {
    if (granted == true) {
      navigator.geolocation.getCurrentPosition(function (position) {
        var latitude = position.coords.latitude;
        var longitude = position.coords.longitude;
        console.log("Latitude: " + latitude + " Longitude: " + longitude);
        return latitude + "^" + longitude;
      });
    }else{
        return "NOPERMISSION";
    }
  } else {
    console.log("Geolocation is not supported by this browser.");
    return "NOSUPPORT";
  }
}
