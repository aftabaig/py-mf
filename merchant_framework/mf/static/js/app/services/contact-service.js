mf.factory("ContactService", function($http, $q) {
    var api_url = "/api/contacts/";
    return {
        info: function(contactId) {
            var url = api_url + contactId + "/info";
            var defer = $q.defer();
            $http({
                method: 'GET',
                url: url
            }).success(function(data, status, header, config) {
                defer.resolve(data);
            }).error(function(data, status, header, config) {
                defer.reject(status);
            });
            return defer.promise;
        },
        add: function(contact) {
            var defer = $q.defer();
            $http({
                method: 'POST',
                url: api_url,
                data: contact
            }).success(function(data, status, header, config) {
                defer.resolve(data);
            }).error(function(data, status, header, config) {
                console.dir(data);
                defer.reject(field);
            });
            return defer.promise;
        },
        update: function(contact) {
            var url = api_url + contact.id + "/";
            var defer = $q.defer();
            $http({
                method: 'PUT',
                url: url,
                data: contact
            }).success(function(data, status, header, config) {
                defer.resolve(data);
            }).error(function(data, status, header, config) {
                defer.reject(status);
            });
            return defer.promise;
        },
        delete: function(contact_id) {
            var url = api_url + contact_id + "/";
            var defer = $q.defer();
            $http({
                method: 'DELETE',
                url: url
            }).success(function(data, status, header, config) {
                defer.resolve(data);
            }).error(function(data, status, header, config) {
                defer.reject(status);
            });
            return defer.promise;
        },
    }
});