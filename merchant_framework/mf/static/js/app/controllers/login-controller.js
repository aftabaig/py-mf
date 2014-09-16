mf.controller("LoginController", ['$scope', '$rootScope', '$localStorage', 'AuthService', function($scope, $rootScope, $localStorage, AuthService) {

    $scope.login = function() {

        AuthService.authenticate($scope.username, $scope.password)
        .then(function(data) {
            $localStorage.token = data.token;
        }, function(error, status) {
            delete $scope.storage.token;
        });

    };

}]);

