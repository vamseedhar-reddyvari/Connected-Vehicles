L.mapbox.accessToken = 'pk.eyJ1IjoiaGl2YW1zZWUiLCJhIjoiY2lraGFyMHRiMDFjeXYwa21mdWYxb2t0NiJ9.DaVAaeEszhOTuPzxZyCFwA';
var map = L.mapbox.map('map', 'mapbox.streets').setView([42.288138, -83.69706], 13);

var geojson;

$.getJSON('../data/vehicle-locations.json', function(response){
       geojson= response;
      //  L.geoJson(geojson, { style:L.mapbox.simplestyle.style }).addTo(map);

       var myLayer = L.mapbox.featureLayer().addTo(map);
       myLayer.setGeoJSON(geojson);
});

$.getJSON('../data/rse-data-locations.json', function(response){
       geojson= response;
      //  L.geoJson(geojson, { style:L.mapbox.simplestyle.style }).addTo(map);

       var myLayer = L.mapbox.featureLayer().addTo(map);
       myLayer.setGeoJSON(geojson);
});
