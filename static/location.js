var lat;
var lon;

if (navigator.geolocation) {
  navigator.geolocation.getCurrentPosition(Start);
}

function Start(location) {
  lat = location.coords.latitude;
  lon = location.coords.longitude;
}

function ProximityRedirect(opinion) {
  window.location = "/?lat=" + lat + "&lon=" + lon;
}