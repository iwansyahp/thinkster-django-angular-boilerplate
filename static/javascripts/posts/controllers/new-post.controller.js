(function(){
	'use strict';

	angular
		.module('thinkster.posts.controllers')
		.controller('NewPostController', NewPostController);

	NewPostController.$inject = ['$rootScope', '$scope', 'Authentication', 'Snackbar', 'Posts'];

	function NewPostController($rootScope, $scope, Authentication, Snackbar, Posts){
		var vm = this;

		vm.submit = submit;

		 /**
    * @name submit
    * @desc Create a new Post
    * @memberOf thinkster.posts.controllers.NewPostController
    */
    	function submit(){
    		// optimistic broadcast.
    		/**
    		The fact of the matter is that this call will rarely fail. 
    		There are only two cases where this will reasonably fail: 
    		either the user is not authenticated or the server is down.
    		*/
    		$rootScope.$broadcast('post.created', {
    			content: vm.content,
    			author: {
    				username: Authentication.getAuthenticatedAccount().username
    			}
    		});

    		//This is a method provided by ngDialog
    		$scope.closeThisDialog();

    		Posts.create(vm.content.then(createPostSuccessFn, createPostErrorFn));

    		 /**
      * @name createPostSuccessFn
      * @desc Show snackbar with success message
      */
      		function createPostSuccessFn(data, status, headers, config){
      			Snackbar.show('Success!. Post created.');
      		}

      	 /**
      * @name createPostErrorFn
      * @desc Propogate error event and show snackbar with error message
      */
      		function createPostErrorFn(data, status, headers, config){
      			$rootScope.$broadcast('post.created.error');
      			Snackbar.error(data.error);
      		}
    	}
	}
})();