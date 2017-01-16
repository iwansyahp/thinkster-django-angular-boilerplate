(function() {
    'use strict';

    angular
        .module('thinkster.config')
        .config(config);

    config.$inject = ['$locationProvider'];

    /**
     * @name config
     * @desc Enable HTML5 routing
     */
    function config($locationProvider) {
        $locationProvider.html5Mode(true);
        // kegunaan hash routing adalah untuk membentuk url cantik seperti ini: www.google.com /#/search
        $locationProvider.hashPrefix('!');
    }
})();