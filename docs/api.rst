API Setup
=========

.. _ucl-api-oauth-setup:

UCL API OAuth Credentials
-------------------------

Create a new app at: https://uclapi.com/dashboard/.

Then fill in the OAuth Callback URL to be the remote url of your server, followed by ``/auth/callback``. If using a localtunnel development server, this will be something like:

.. code-block:: none

  https://abcdefghij.localtunnel.me/auth/callback

Test you've setup your credentials correctly by attempting to log in by visiting ``/auth``.

.. _gmaps-api-setup:

Google Maps API Key
-------------------

A Google Maps API key is necessary for displaying the maps on event pages.

To get your key:

#. Visit https://console.developers.google.com/cloud-resource-manager and sign in
#. Click "Create a Project"
#. Give your project a name, perhaps "SSIG site dev"
#. Click "Create"
#. Click on your newly created project
#. Visit https://console.developers.google.com/apis/api/maps-backend.googleapis.com/overview
#. Click "Enable", wait for the API to be enabled for your project
#. Visit https://console.developers.google.com/apis/credentials/wizard?api=maps-backend.googleapis.com
#. Click "What credentials do I need?"
#. Your API key will be displayed
#. Click "Restrict key" to restrict with what sites and APIs the key can be used (recommended in production)
