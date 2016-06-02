//attach the leaflet directive to our angular app
var app = angular.module("atxgreenatlas", ['leaflet-directive']);

//create our map controller for leaflet with the http service attached
app.controller("map-canvas", [ "$scope","$http", function($scope, $http) {
    angular.extend($scope, {
        //map centered on Austin, TX
        austin: {
            lat: 30.2672,
            lng: -97.7431,
            zoom: 12
        },
        layers: {
            //basic underlying layers below any data set
            baselayers: {
            	googleRoadmap: {
                    name: 'Google Streets',
                    layerType: 'ROADMAP',
                    type: 'google'
                },
                googleHybrid: {
                    name: 'Google Hybrid',
                    layerType: 'HYBRID',
                    type: 'google'
                },
                googleTerrain: {
                    name: 'Google Terrain',
                    layerType: 'TERRAIN',
                    type: 'google'
                }
            },
            //data set layers in group or cluster forms
            overlays: {
            	recycling: {
                    name: 'Recycling Centers',
                    type: 'group',
                    visible: false
                },
                storage_tanks: {
                    name: 'Underground Storage Tanks',
                    type: 'markercluster',
                    visible: false
                },
                water_quality: {
                    name: 'Austin Water Quality Results',
                    type: 'markercluster',
                    visible: false
                }
            }
        },
        markers: {},
        controls: {
            fullscreen: {
                position: 'topleft'
            }
        }
    });

    //parsed dataset for the Recycling Centers layer
    $http.get('data/recyclingOut.json') 
       .success(function(data, status){
           	angular.forEach(data, function(value, key) {
                $scope.markers[key] = value;
            })
        });

    //parsed data set for the Underground Storage Tanks layer
    $http.get('data/storageTanksOut.json') 
       .success(function(data, status){
            angular.forEach(data, function(value, key) {
                $scope.markers[key] = value;
            })
        });

    //parsed dataset for the Water Quality Results layer
    $http.get('data/waterQualityOut.json') 
       .success(function(data, status){
            angular.forEach(data, function(value, key) {
                $scope.markers[key] = value;
            })
        });

    //GeoJSON (polygon) for all Austin Area parks.
    //Disabled due to accurate Google Maps parks labels.
    //Use in zip-code search only.
   /* 
   $http.get("data/parks.geojson")
        .success(function(data, status) {
            $scope.layers.overlays['parks'] =   {    
                name: 'Austin City Parks',
                type: 'geoJSONShape',
                data: data,
                visible: false,
                layerOptions: {
                    style: {
                            color: '#000',
                            fillColor: '#9D9',
                            weight: 1.0,
                            opacity: 1.0,
                            fillOpacity: 0.5
                    }
                }
            }
        });
    */

    //GeoJSON (polygon) for all contribution zones to the edwards aquifer
    //parse as boolean in zip code search
    $http.get("data/ea_contribution_zones.geojson")
        .success(function(data, status) {
            $scope.layers.overlays['ea'] =   {    
                name: 'Edwards Aquifer Contribution Zones',
                type: 'geoJSONShape',
                data: data,
                visible: false,
                layerOptions: {
                    style: {
                            color: '#000',
                            fillColor: '#69F',
                            weight: 1.0,
                            opacity: 1.0,
                            fillOpacity: 0.5
                    }
                }
            }
        });

    //GeoJSON (polygon) for all watersheds from area rivers
    //parse as boolean in zip code search
    $http.get("data/watersheds.geojson")
        .success(function(data, status) {
            $scope.layers.overlays['watersheds'] =   {    
                name: 'Greater Austin Area Watersheds',
                type: 'geoJSONShape',
                data: data,
                visible: false,
                layerOptions: {
                    style: {
                            color: '#000',
                            fillColor: '#F96',
                            weight: 1.0,
                            opacity: 1.0,
                            fillOpacity: 0.5
                    }
                }
            }
        });

    //GeoJSON (polygon) for the zip codes in the greater austin area
    $http.get("data/zips.geojson")
        .success(function(data, status) {
            $scope.layers.overlays['zips'] =   {    
                name: 'Greater Austin Area Zipcodes',
                type: 'geoJSONShape',
                data: data,
                visible: false,
                layerOptions: {
                    style: {
                            color: '#000',
                            fillColor: '#F69',
                            weight: 1.0,
                            opacity: 1.0,
                            fillOpacity: 0.5
                    }
                }
            }
        });
}]);