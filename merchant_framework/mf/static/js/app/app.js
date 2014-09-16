
function onError(e) {
  console.log(e);
}

// Create module.
var mf = angular.module('mf', ['ngResource', 'ngRoute', 'ngStorage', 'datePicker', 'ui.bootstrap', 'cgBusy']);

mf.config(function($interpolateProvider) {
  $interpolateProvider.startSymbol('^^');
  $interpolateProvider.endSymbol('^^');
});

mf.config(function($routeProvider) {
    $routeProvider
        .when("/login", {
            templateUrl: "static/js/app/views/login.html",
            controller: "LoginController",
            resolve: {

            }
        })
        .when("/branches", {
            templateUrl: "static/js/app/views/branches.html",
            controller: "BranchController",
            resolve: {
                branches: function (BranchService) {
                    return BranchService.all();
                }
            }
        })
        .when("/branch", {
            templateUrl: "static/js/app/views/branch.html",
            controller: "BranchController",
            resolve: {

            }
        })
        .when("/branches/:id/contacts", {
            templateUrl: "static/js/app/views/contacts.html",
            controller: "ContactController",
            resolve: {
                contacts: function($route, BranchService) {
                    var branchId = $route.current.params.id;
                    return BranchService.contacts(branchId);
                },
                branch: function($route, BranchService) {
                    var branchId= $route.current.params.id;
                    return BranchService.info(branchId);
                }
            }
        })
        .when("/deals", {
            templateUrl: "static/js/app/views/deals.html",
            controller: "DealController",
            resolve: {
                deals: function (DealService) {
                    return DealService.all();
                }
            }
        })
        .when("/deals/:id/branches", {
            templateUrl: "static/js/app/views/deal-branches.html",
            controller: "DealBranchController",
            resolve: {
                branches: function($route, DealService) {
                    var dealId = $route.current.params.id;
                    return DealService.branches(dealId);
                },
                deal: function($route, DealService) {
                    var dealId = $route.current.params.id;
                    return DealService.info(dealId);
                }
            }
        })
})