mf.controller("ContactController", ['$scope', '$rootScope', 'BranchService', 'ContactService', 'contacts', 'branch', function($scope, $rootScope, BranchService, ContactService, contacts, branch) {

  $rootScope.activeMenu = "Branches";

  $scope.alert = {
    "show": false,
    "title": "",
    "message": ""
  }

  $scope.selectedIndex = -1;

  $scope.contacts = contacts;
  $scope.branch = branch;

  $scope.add = function() {
    var newContact = {
        "lease": $scope.lease.id,
        "sheet": $scope.sheet.id,
        "sub_sheet": $scope.subSheet ? $scope.subSheet.id : null,
        "name": "New Field",
        "data_type": $scope.data_types[0],
        "min_value": "0",
        "max_value": "100",
        "calculate_total": false,
        "calculate_average": false,
        "isNew": true
    }
    if (!$scope.fields) {
        $scope.fields = [];
    }
    $scope.fields.push(newField);
  };

  $scope.cancelAdd = function(index) {
    $scope.fields.splice(index, 1);
  }

  $scope.save = function(index) {
    FieldService.add($scope.fields[index]).then(function(data) {
        $scope.fields[index].isNew = false;
        $scope.fields[index].editing = false;
    });
  }

  $scope.editInline = function(index) {
    $scope.fields[index].editing = true;
  };

  $scope.cancelEditing = function(index) {
    $scope.fields[index].editing = false;
  };

  $scope.update = function(index) {
    FieldService.update($scope.fields[index]).then(function(data) {
        $scope.fields[index].editing = false;
    });
  };

  $scope.confirmDelete = function(index) {
    $scope.selectedIndex = index;
    $scope.alert.title = "Delete " + $scope.fields[index].name;
    $scope.alert.message = "Are you sure to delete this field?";
    $scope.alert.show = true;

  }

  $scope.delete = function() {
    FieldService.delete($scope.fields[$scope.selectedIndex].id).then(function(data) {
        $scope.fields.splice($scope.selectedIndex, 1);
        $scope.alert.show = false;
    });
  }

  $scope.hideAlert = function() {
    $scope.alert.show = false;
  }

}]);