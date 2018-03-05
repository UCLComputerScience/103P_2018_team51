#!/usr/bin/env bash

export STATIC_ROOT="$DEPLOYMENT_TARGET/static"

NPM_VERSION=$(cat "/d/Program Files (x86)/nodejs/$WEBSITE_NODE_DEFAULT_VERSION/npm.txt")

function npm () {
  node "/d/Program Files (x86)/npm/$NPM_VERSION/node_modules/npm/bin/npm-cli.js" "$@"
}

function python () {
  "/d/home/python364x86/python.exe" "$@"
}

echo "Installing node dependencies"

npm install -q

echo "Installing gulp-cli"

npm install -g gulp-cli -q

echo "Cleaning up sass files"

rm -r static/css

echo "Building sass files"

gulp sass:build

echo "Collecting static files"

python manage.py collectstatic --noinput --clear

echo "Installing pip dependencies"

python -m pip install -r requirements.txt -q

echo "Running migrations"

python manage.py migrate

echo "Cleaning up deployment target"

rm -r $DEPLOYMENT_TARGET/ssig_site

echo "Copying files to deployment target"

cp -R ssig_site $DEPLOYMENT_TARGET/
cp web.config $DEPLOYMENT_TARGET/
