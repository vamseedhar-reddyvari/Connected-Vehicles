L.mapbox.accessToken = 'pk.eyJ1IjoiaGl2YW1zZWUiLCJhIjoiY2lraGFyMHRiMDFjeXYwa21mdWYxb2t0NiJ9.DaVAaeEszhOTuPzxZyCFwA';
var map = L.mapbox.map('map', 'mapbox.streets')
    .setView([42.288138, -83.69706], 13);

var geojson;

$.getJSON('../data/rse-geo.json', function(response){
       geojson= response;
       L.geoJson(geojson, { style: L.mapbox.simplestyle.style }).addTo(map);
});

//$.getJSON('../data/center-point.json', function(response){
//       geojson= response;
//       L.geoJson(geojson, { style: L.mapbox.simplestyle.style }).addTo(map);
//});
$.getJSON('../data/rse-data-locations.json', function(response){
       geojson= response;
       L.geoJson(geojson, {
         style:L.mapbox.simplestyle.style }).addTo(map);
});
// icon: L.mapbox.marker.icon({'marker-symbol': 'post', 'marker-color': '0044FF'}
// style: L.mapbox.simplestyle.style
var myIcon = L.icon({
	iconUrl: 'my-icon.png',
	iconRetinaUrl: 'my-icon@2x.png',
	iconSize: [38, 95],
	iconAnchor: [22, 94],
	popupAnchor: [-3, -76],
	shadowUrl: 'my-icon-shadow.png',
	shadowRetinaUrl: 'my-icon-shadow@2x.png',
	shadowSize: [68, 95],
	shadowAnchor: [22, 94]
});

L.marker([50.505, 30.57], {icon: myIcon}).addTo(map);
