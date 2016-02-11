L.mapbox.accessToken = 'pk.eyJ1IjoiaGl2YW1zZWUiLCJhIjoiY2lraGFyMHRiMDFjeXYwa21mdWYxb2t0NiJ9.DaVAaeEszhOTuPzxZyCFwA';
var map = L.mapbox.map('map', 'mapbox.streets')
    .setView([42.268138, -83.79706], 13);

var geojson;

$.getJSON('../data/rse-geo.json', function(response){
       geojson= response;
       L.geoJson(geojson, { style: L.mapbox.simplestyle.style }).addTo(map);
});

$.getJSON('../data/center-point.json', function(response){
       geojson= response;
       L.geoJson(geojson, { style: L.mapbox.simplestyle.style }).addTo(map);
});
