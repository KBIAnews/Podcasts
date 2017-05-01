module.exports = function(grunt) {
	grunt.loadNpmTasks('grunt-contrib-uglify');
	grunt.loadNpmTasks('grunt-contrib-compass');
	grunt.loadNpmTasks('grunt-contrib-watch');

	grunt.initConfig({
		uglify: {
			my_target:{
				files: {
					'components-build/js/player.js': ['components/js/player.js']
				}
			}
		},
		compass: {
			dev: {
				options: {
					config: 'config.rb'
				}
			}
		},
		watch: {
			scripts: {
				files: ['components/js/*.js'],
				tasks: ['uglify']
			},
			sass: {
				files: ['components/sass/*.scss'],
				tasks: ['compass:dev']
			}
		}
	});

	grunt.registerTask('default', 'watch');
}