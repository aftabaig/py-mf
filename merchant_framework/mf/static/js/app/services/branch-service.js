mf.factory("BranchService", function($http, $q, $localStorage) {
    var api_url = "/api/branches/";
    return {
        info: function(branchId) {
            var url = api_url + branchId + "/info";
            var defer = $q.defer();
            $http({
                headers: {
                    'Authorization': 'Token ' + $localStorage.token
                },
                method: 'GET',
                url: url
            }).success(function(data, status, header, config) {
                defer.resolve(data);
            }).error(function(data, status, header, config) {
                defer.reject(status);
            });
            return defer.promise;
        },
        all: function() {
            var defer = $q.defer();
            $http({
                headers: {
                    'Authorization': 'Token ' + $localStorage.token
                },
                method: 'GET',
                url: api_url
            }).success(function(data, status, header, config) {
                defer.resolve(data);
            }).error(function(data, status, header, config) {
                defer.reject(status);
            });
            return defer.promise;
        },
        add: function(branch) {
            var defer = $q.defer();
            $http({
                headers: {
                    'Authorization': 'Token ' + $localStorage.token
                },
                method: 'POST',
                url: api_url,
                data: branch
            }).success(function(data, status, header, config) {
                defer.resolve(data);
            }).error(function(data, status, header, config) {
                defer.reject(data);
            });
            return defer.promise;
        },
        update: function(branch) {
            var url = api_url + branch.id + "/";
            var defer = $q.defer();
            $http({
                headers: {
                    'Authorization': 'Token ' + $localStorage.token
                },
                method: 'PUT',
                url: url,
                data: branch
            }).success(function(data, status, header, config) {
                defer.resolve(data);
            }).error(function(data, status, header, config) {
                defer.reject(status);
            });
            return defer.promise;
        },
        delete: function(branch_id) {
            var url = api_url + branch_id + "/";
            var defer = $q.defer();
            $http({
                headers: {
                    'Authorization': 'Token ' + $localStorage.token
                },
                method: 'DELETE',
                url: url
            }).success(function(data, status, header, config) {
                defer.resolve(data);
            }).error(function(data, status, header, config) {
                defer.reject(status);
            });
            return defer.promise;
        },

        contacts: function(branch_id) {
            var url = api_url + branch_id + "/contacts/";
            var defer = $q.defer();
            $http({
                headers: {
                    'Authorization': 'Token ' + $localStorage.token
                },
                method: 'GET',
                url: url
            }).success(function(data, status, header, config) {
                defer.resolve(data);
            }).error(function(data, status, header, config) {
                defer.reject(status);
            });
            return defer.promise;
        }
    }
});