mf.controller("BranchController", ['$scope', '$rootScope', '$window', 'BranchService', 'branches', function($scope, $rootScope, $window, BranchService, branches) {

  $rootScope.activeMenu = "Branches";

  $scope.promise = null;
  $scope.message = "Updating ...";

  $scope.alert = {
    "show": false,
    "title": "",
    "message": ""
  }

  $scope.selectedIndex = -1;

  $scope.branches = branches;

  $scope.add = function() {
    $window.location.href = "/#/branch";
    //var newBranch = {
    //    "name": "New Branch",
    //    "isNew": true
    //}
    //$scope.branches.push(newBranch);
  };

  $scope.cancelAdd = function(index) {
    $scope.branches.splice(index, 1);
  }

  $scope.save = function(index) {

    $scope.message = "Adding ...";

    $scope.promise = BranchService.add($scope.branches[index]).then(function(data) {
        $scope.branches[index].isNew = false;
        $scope.branches[index].editing = false;
    }, function(error) {
        console.dir(error);
    });
  }

  $scope.editInline = function(index) {
    $scope.branches[index].editing = true;
  };

  $scope.cancelEditing = function(index) {
    $scope.branches[index].editing = false;
  };

  $scope.update = function(index) {

    $scope.message = "Updating";

    $scope.promise = BranchService.update($scope.branches[index]).then(function(data) {
        $scope.branches[index].editing = false;
    });
  };

  $scope.confirmDelete = function(index) {
    $scope.selectedIndex = index;
    $scope.alert.title = "Delete " + $scope.branches[index].name;
    $scope.alert.message = "Are you sure to delete this branch?";
    $scope.alert.show = true;
  }

  $scope.delete = function() {

    $scope.message = "Deleting ...";

    $scope.promise = BranchService.delete($scope.branches[$scope.selectedIndex].id).then(function(data) {
        $scope.branches.splice($scope.selectedIndex, 1);
        $scope.alert.show = false;
    });
  }

  $scope.hideAlert = function() {
    $scope.alert.show = false;
  }

}]);

