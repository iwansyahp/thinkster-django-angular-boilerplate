/**
* Posts
* @namespace thinkster.posts.directives
*/
(function(){
    'use strict';
    
    angular
        .module('thinkster.posts.directives')
        .directive('posts'. posts);
    
    /**
  * @namespace Posts
  */
  function posts(){
      /**
    * @name directive
    * @desc The directive to be returned
    * @memberOf thinkster.posts.directives.Posts
    */
    var directive = {
        controller: 'PostsController',
        controllerAs: 'vm',
        restrict: 'E', // E for html element
        scope: {
            posts: '='
            // The second line, posts: '=' simply means 
            // that we want to set $scope.posts
        },
        templateUrl: '/static/templates/posts/posts.html'
    };
    return directive;
  }
})();