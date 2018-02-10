var gulp = require('gulp')
var { spawn } = require('child_process')

gulp.task('django:runserver', () => {
  spawn('python3', ['manage.py', 'runserver', '0.0.0.0:8000'], {
    stdio: 'inherit'
  })
})

gulp.task('default', () => {
  gulp.start('django:runserver')
})
