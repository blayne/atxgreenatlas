String.prototype.format = function()
{
   var content = this;
   for (var i=0; i < arguments.length; i++)
   {
        var replacement = '{' + i + '}';
        content = content.replace(replacement, arguments[i]);  
   }
   return content;
};

//attach the leaflet  and modal service to our angular app
var app = angular.module("atxgreenatlas", ['leaflet-directive', 'angularModalService', 'ngSanitize']);

//create our map controller for leaflet with the http service attached
app.controller("map-canvas", [ "$scope","$http","ModalService", function($scope, $http, ModalService) {

    $scope.loading = true;

    $scope.$on('leafletDirectiveMarker.click', function (e, args) {
        if(args.layerName == 'water_quality'){
            ModalService.showModal({
            templateUrl: "modal.html",
            controller: "WQModalController",
            inputs: {
                head: args.model.message,
                data: args.model.data
              }
             }).then(function(modal) {

               //it's a bootstrap element, use 'modal' to show it
               modal.element.modal();
               modal.close.then(function(result) {
                 console.log(result);
             });
          });
        }
        if(args.layerName == 'air_quality'){
            ModalService.showModal({
            templateUrl: "modal.html",
            controller: "AQModalController",
            inputs: {
                head: args.model.message,
                data: args.model.data
              }
             }).then(function(modal) {

               //it's a bootstrap element, use 'modal' to show it
               modal.element.modal();
               modal.close.then(function(result) {
                 console.log(result);
             });
          });
        }
        if(args.layerName == 'greenhouse_gas'){
            ModalService.showModal({
            templateUrl: "modal.html",
            controller: "GGModalController",
            inputs: {
                head: args.model.message,
                data: args.model.data
              }
             }).then(function(modal) {

               //it's a bootstrap element, use 'modal' to show it
               modal.element.modal();
               modal.close.then(function(result) {
                 console.log(result);
             });
          });
        }
    });

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
                    name: 'Water Quality Results',
                    type: 'markercluster',
                    visible: false
                },
                air_quality : {
                    name: 'Air Quality Results',
                    type: 'markercluster',
                    visible: false
                },
                greenhouse_gas : {
                    name: 'Greenhouse Gas Emissions',
                    type: 'markercluster',
                    visible: false
                },
                zips: {
                    name: 'Zip codes',
                    type: 'group',
                    visible: false
                },
                solid_waste: {
                    name: 'Solid Waste Sites',
                    type: 'markercluster',
                    visible: false
                },
                rainGardens : {
                    name: 'Rain Gardens',
                    type: 'markercluster',
                    visible: false
                },
                bicycle : {
                    name: 'B-Cycle stations',
                    type: 'markercluster',
                    visible: false
                }
            }
        },
        markers: {},
        paths: {},
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

    //parsed dataset for the Air Quality Results layer
    $http.get('data/airQualityOut.json') 
       .success(function(data, status){
            angular.forEach(data, function(value, key) {
                $scope.markers[key] = value;
            })
        })
       .then(function(){
            $scope.loading = false;
       });

    //parsed dataset for the Greenhouse Gas Emissions Results layer
    $http.get('data/greenHouseOut.json') 
       .success(function(data, status){
            angular.forEach(data, function(value, key) {
                $scope.markers[key] = value;
            })
        });

    //parsed dataset for the solid wastes (landfills)
    $http.get('data/solidWasteOut.json') 
       .success(function(data, status){
            angular.forEach(data, function(value, key) {
                $scope.markers[key] = value;
            })
        });

    //parsed dataset for the austin rain gardens
    $http.get('data/RainGardenOut.json') 
       .success(function(data, status){
            angular.forEach(data, function(value, key) {
                $scope.markers[key] = value;
            })
        });

    //parsed dataset for the austin B-Cycle Stations
    $http.get('data/bikesOut.json') 
       .success(function(data, status){
            angular.forEach(data, function(value, key) {
                $scope.markers[key] = value;
            })
        });

    //GeoJSON (polygon) for all Austin Area parks.
    //Disabled due to accurate Google Maps parks labels.
    //Use in zip-code search only.
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
    /*
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
    */

    //GeoJSON (polygon) for the zip codes in the greater austin area
    $http.get("data/zipsOut.json")
        .success(function(data, status) {
            angular.forEach(data, function(value, key) {
                $scope.paths[key] = value;
            })
        })
    
}]);

app.controller('AQModalController', function($scope, head, data, close) {
    var htmlTableData = '<table class="table table-striped"><thead><tr><th>Site</th><th>Facility Type</th><th>Measurment</th><th>Value</th><th>Units</th></tr></thead><tbody>';

    angular.forEach(data, function(value) {
        htmlTableData += "<tr><td>{0}</td><td>{1}</td><td>{2}</td><td>{3}</td><td>{4}</td></tr>".format(value.facility_site_name, value.facility_source_description, value.description, value.total_emissions,value.uom);
    });

    htmlTableData += '</tbody></table>';


    $scope.head = head;
    $scope.data = htmlTableData;
    $scope.close = function() {
        close("modal closed", 500); // close, but give 500ms for bootstrap to animate
    };

});

app.controller('WQModalController', function($scope, head, data, close) {
    var htmlTableData = '<table class="table table-striped"><thead><tr><th>Date</th><th>Site</th><th>Medium</th><th>Measurment</th><th>Parameter</th><th>Value</th><th>Units</th></tr></thead><tbody>';

    angular.forEach(data, function(value) {
        htmlTableData += "<tr><td>{0}</td><td>{1}</td><td>{2}</td><td>{3}</td><td>{4}</td><td>{5}</td><td>{6}</td></tr>".format(value[9], value[11], value[12], value[13],value[14], value[16], value[17]);
    });

    htmlTableData += '</tbody></table>';


    $scope.head = head;
    $scope.data = htmlTableData;
    $scope.close = function() {
        close("modal closed", 500); // close, but give 500ms for bootstrap to animate
    };

});

app.controller('GGModalController', function($scope, head, data, close) {
    var htmlTableData = '<table class="table table-striped"><thead><tr><th>Annual GHG per Household</th><th>Annual GHG per Acre</th><th>Units</th></tr></thead><tbody>';

    angular.forEach(data, function(value) {
        htmlTableData += "<tr><td>{0}</td><td>{1}</td><td>Tonnes</td></tr>".format(value.co2_per_hh_local, value.co2_per_acre_local);
    });

    htmlTableData += '</tbody></table>';


    $scope.head = head;
    $scope.data = htmlTableData;
    $scope.close = function() {
        close("modal closed", 500); // close, but give 500ms for bootstrap to animate
    };

});
