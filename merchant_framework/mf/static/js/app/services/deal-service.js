mf.factory("DealService", function($http, $q, $localStorage) {
    var api_url = "/api/deals/";
    return {
        info: function(dealId) {
            var url = api_url + dealId + "/info";
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
        add: function(deal) {
            var defer = $q.defer();
            $http({
                headers: {
                    'Authorization': 'Token ' + $localStorage.token
                },
                method: 'POST',
                url: api_url,
                data: deal
            }).success(function(data, status, header, config) {
                defer.resolve(data);
            }).error(function(data, status, header, config) {
                defer.reject(status);
            });
            return defer.promise;
        },
        update: function(deal) {
            var url = api_url + deal.id + "/";
            var defer = $q.defer();
            $http({
                headers: {
                    'Authorization': 'Token ' + $localStorage.token
                },
                method: 'PUT',
                url: url,
                data: deal
            }).success(function(data, status, header, config) {
                defer.resolve(data);
            }).error(function(data, status, header, config) {
                defer.reject(status);
            });
            return defer.promise;
        },
        delete: function(deal_id) {
            var url = api_url + deal_id + "/";
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

        branches: function(deal_id) {
            var url = api_url + deal_id + "/branches/";
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