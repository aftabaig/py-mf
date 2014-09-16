mf.controller("DealController", ['$scope', '$rootScope', 'DealService', 'deals', function($scope, $rootScope, DealService, deals) {

  $rootScope.activeMenu = "Deals";

  $scope.promise = null;
  $scope.message = "Updating ...";

  $scope.alert = {
    "show": false,
    "title": "",
    "message": ""
  }

  $scope.selectedIndex = -1;

  $scope.deals = deals;
  $scope.getLeases = function() {
    LeaseService.all().then(function(data) {
        $scope.leases = data;
    });
  };

  $scope.add = function() {
    var newDeal = {
        "name": "New Lease",
        "isNew": true
    }
    $scope.deals.push(newDeal);
  };

  $scope.cancelAdd = function(index) {
    $scope.deals.splice(index, 1);
  }

  $scope.save = function(index) {

    $scope.message = "Adding ...";

    $scope.promise = DealService.add($scope.deals[index]).then(function(data) {
        $scope.deals[index].isNew = false;
        $scope.deals[index].editing = false;
    });
  }

  $scope.editInline = function(index) {
    $scope.deals[index].editing = true;
  };

  $scope.cancelEditing = function(index) {
    $scope.deals[index].editing = false;
  };

  $scope.update = function(index) {

    $scope.message = "Updating";

    $scope.promise = DealService.update($scope.leases[index]).then(function(data) {
        $scope.deals[index].editing = false;
    });
  };

  $scope.confirmDelete = function(index) {
    $scope.selectedIndex = index;
    $scope.alert.title = "Delete " + $scope.deals[index].name;
    $scope.alert.message = "Are you sure to delete this deal?";
    $scope.alert.show = true;
  }

  $scope.delete = function() {

    $scope.message = "Deleting ...";

    $scope.promise = DealService.delete($scope.leases[$scope.selectedIndex].id).then(function(data) {
        $scope.deals.splice($scope.selectedIndex, 1);
        $scope.alert.show = false;
    });
  }

  $scope.hideAlert = function() {
    $scope.alert.show = false;
  }

}]);

