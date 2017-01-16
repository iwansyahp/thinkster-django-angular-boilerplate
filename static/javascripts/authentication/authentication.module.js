/* Ini adalah super-module dari services, controllers dan routes
 */
(function() {
    'use strict';
    angular
        .module('thinkster.authentication', [
            'thinkster.authentication.controllers',
            'thinkster.authentication.services'
        ]);

    angular
        .module('thinkster.authentication.controllers', []);
    angular
        .module('thinkster.authentication.services', ['ngCookies']);
})();