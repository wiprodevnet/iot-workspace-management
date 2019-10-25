//
var trackWorkSpaceApp = angular.module('trackWorkSpaceApp',[]);

trackWorkSpaceApp.controller('getWorkSpacedataController',['$scope', '$http', '$interval', 'dataService',
  function($scope, $http, $interval, dataService)
    { 
        $scope.showWorkSpace = false;
        $scope.showSensorReg = false;

        $scope.counter = 0;
        var increaseCounter = function () {
                $scope.getWorkSpacedata()
                $scope.counter = $scope.counter + 1;
                console.log($scope.counter);
        };

        $scope.showWorkSpaceDiv = function(){
          $scope.showWorkSpace = true;
          $scope.showSensorReg = false;
          $scope.getWorkSpacedata()
          $interval(increaseCounter, 10000); 

        };

        $scope.showSensorRegPage = function(){
          $scope.showWorkSpace = false;
          $scope.showSensorReg = true;

        };

        $scope.getWorkSpacedata = function() {
            dataService.getWorkSpaceDetails().then(function(dataResponse) {
            $scope.workSpaceData = dataResponse.data;
            });
        }; 

        $scope.getBuildingData = function () {

            $scope.data = null;
            dataService.getBuildingData().then(function(dataResponse) {
            $scope.buildingData = dataResponse.data;
            });
        };
        //Calling the function to load the data on pageload
        $scope.getBuildingData();

        $scope.getFloordata = function (buildingIdn) {
            $scope.data = null;
            dataService.getFloordata(buildingIdn).then(function(dataResponse) {
            $scope.floorData = dataResponse.data;
            });
        };

        $scope.getCubicleData = function (floorIdn) {
            $scope.data = null;
            dataService.getCubiclerdata(floorIdn).then(function(dataResponse) {
            $scope.cubicleData = dataResponse.data;
            });
        };

        $scope.saveSensorDetails = function(){
          var sensorDataSet = {'sensor_serial_no': $scope.sensorSerialNo,
                                'cubicle_idn': $scope.selectedCubicleNo[0]
                              };
            dataService.saveSensordata(sensorDataSet).then(function(dataResponse) {
                $scope.addSensorDetails = {};
                $scope.responseMsg = dataResponse.data;
            });

        }

}]); 

trackWorkSpaceApp.service('dataService', function($http) {
    this.getWorkSpaceDetails = function() {
        // $http() returns a $promise that we can add handlers with .then()
        return $http.get('/work_space')
     },

     this.getBuildingData = function() {
        // $http() returns a $promise that we can add handlers with .then()
        return $http.get('/building_data')
     },

     this.getFloordata = function(buildingIdn) {
        // $http() returns a $promise that we can add handlers with .then()
        return $http.get('/floor_data',{params: { building_id: buildingIdn[0] }})
     },

     this.getCubiclerdata = function(floorIdn) {
        // $http() returns a $promise that we can add handlers with .then()
        return $http.get('/cubicle_data',{params: { floor_id: floorIdn[0] }})
     },

     this.saveSensordata = function(sensorDataSet) {
        // $http() returns a $promise that we can add handlers with .then()
        return $http.post('/save_sensor_data',{params: sensorDataSet})
     }


});
    