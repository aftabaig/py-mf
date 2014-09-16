mf.factory("AuthService", function($http, $q) {
    var api_url = "/api/users/";
    return {
        authenticate: function(username, password) {
            var url = api_url + "authenticate/";
            var defer = $q.defer();
            $http({
                method: 'POST',
                url: url,
                data: {
                    "username": username,
                    "password": password
                }
            }).success(function(data, status, header, config) {
                defer.resolve(data);
            }).error(function(data, status, header, config) {
                defer.reject(data, status);
            });
            return defer.promise;
        }
    }
});