'use strict';

const shell = require('shelljs');

const gulp = require('gulp');


gulp.task('flake8', function(done) {
  const watcher = gulp.watch([ '/app/**/*.py' ], { usePolling: true });
  watcher.on('change', function(dir, stats) {
    shell.exec(`/usr/local/bin/flake8 --config /app/setup.cfg ${dir}`);
    shell.echo('-----------------------');
  });
  done();
});

gulp.task('default', function(done) {
  gulp.series('flake8')();
  done();
});
