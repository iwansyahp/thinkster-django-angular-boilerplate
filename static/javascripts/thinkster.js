(function() {
    'use strict';

    angular
        .module('thinkster', [
            'thinkster.config',
            'thinkster.routes',
            'thinkster.authentication',
            'thinkster.utils', // snackbar.
            'thinkster.layout',
            'thinkster.posts',
            'thinkster.profiles'
        ]).run(run);

    run.$inject = ['$http'];

    angular
        .module('thinkster.config', []);
    angular
        .module('thinkster.routes', ['ngRoute']);

    /**
     * @name run
     * @desc Update xsrf $http headers to align with Django's defaults
     */
    function run($http) {
        $http.defaults.xsrfHeaderName = 'X-CSRFToken';
        $http.defaults.xsrfCookieName = 'csrftoken';
    }
})();