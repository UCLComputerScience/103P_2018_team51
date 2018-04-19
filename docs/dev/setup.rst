Development Setup
=================

The recommended development environment is Docker, but a Vagrant environment is also provided.

Cloning the repository
----------------------

Both environments require you to:

#. Clone the repository: ``git clone https://github.com/UCLComputerScience/103P_2018_team51.git``
#. Enter the cloned repository: ``cd 103P_2018_team51``
#. Copy the *env-dist* file to *.env*: ``cp env-dist .env``

Docker
------

Ensure you've installed Docker Compose by following the instructions here: https://docs.docker.com/compose/install/

Then, build the container with: ``docker-compose build``.

Next, you'll need to run the database migrations, to set up the database. To do this:

#. Open a shell within the docker container: ``docker-compose run web sh``
#. Within the container, run: ``python3 manage.py migrate``

Now, close the container shell with ``exit`` (or open a new terminal window) and run the container with: ``docker-compose up``.

You should now be able to access the site at: http://localhost:8000

Stopping the container
^^^^^^^^^^^^^^^^^^^^^^

To stop the running container, go to the terminal it's running in and hit **Ctrl + C**. Docker will then gracefully bring the container down.

If the container is hanging, hit **Ctrl + C** again to kill it.

Updating the container
^^^^^^^^^^^^^^^^^^^^^^

When pulling in new changes to the ``requirements.txt`` file from git, the container will need to be rebuilt.

To rebuild and bring the container up in one step run: ``docker-compose up --build``.

Tips, tricks and oddities
^^^^^^^^^^^^^^^^^^^^^^^^^

Running Docker as root
""""""""""""""""""""""

If running ``docker-compose`` as root, `as is recommended <https://docs.docker.com/engine/security/security/#docker-daemon-attack-surface>`_, then all files and directories created in the source directory within the container will be owned by root, and git will be unable to properly version control them. Run ``sudo chown -R $USER:$USER .`` outside the container to update their ownership to your user.

Vagrant
-------

Download Vagrant and install it from here: https://www.vagrantup.com/downloads.html

You'll also need to install VirtualBox from here: https://www.virtualbox.org/wiki/Downloads

Bring the machine up with: ``vagrant up``.

After the machine has finished booting, open a shell within it with: ``vagrant ssh``.

Next, you'll want to navigate to the directory holding the project's source code with: ``cd /vagrant``.

Here, run the database migrations to set up the database with ``python3 manage.py migrate``, and bring the server up with ``gulp``.

You should now be able to access the site at: http://localhost:8000

Stopping the machine
^^^^^^^^^^^^^^^^^^^^

To stop the running machine:

#. Kill the server with: **Ctrl + C**
#. Exit from the machine's shell with: ``exit``
#. Stop the machine with: ``vagrant halt``

Updating the machine
^^^^^^^^^^^^^^^^^^^^

When pulling in changes to the ``requirements.txt`` file from git, those new requirements will need to be installed in the machine.

Do this by running ``pip3 install -r requirements.txt`` from the ``/vagrant`` path within the machine.

Tips, tricks and oddities
^^^^^^^^^^^^^^^^^^^^^^^^^

Using Windows as a host
"""""""""""""""""""""""

It seems that on Windows, the ``up.sh`` provisioning script isn't run on every ``vagrant up``. This will usually be apparent if running ``gulp`` produces an error about it not being installed. This can be resolved by running ``./up.sh`` from the ``/vagrant`` path within the machine, every time after you bring it up.

It also seems that the correct database configuration options aren't set. Resolve this by updating your ``.env`` file to include::

  DATABASE_HOST=localhost
  DATABASE_USER=vagrant
  DATABASE_PASSWORD=vagrant

Admin Interface
---------------

Create a superuser to access the admin interface at http://localhost:8000/admin.

Do this by running ``python3 manage.py createsuperuser`` within your development environment.

*UPI* stands for Unique Person Identifier, a unique id given to every member of UCL, set this to your own UPI (found on your UCL ID card) if you want to be able to log into the admin interface through UCL API OAuth.

Authentication
--------------

The project makes use of `UCL API OAuth <https://uclapi.com/>`_ for authentication.

Reverse Proxy
^^^^^^^^^^^^^

UCL API prohibits setting localhost as as callback URL, so you'll need to set up a reverse proxy to access your local development server through a remote url.

One solution is localtunnel, which can be used by following the instructions here: https://localtunnel.github.io/www/.

OAuth Credentials
^^^^^^^^^^^^^^^^^

Create a new app at: https://uclapi.com/dashboard/.

Then fill in the OAuth Callback URL to be the remote url of your development server, followed by ``/auth/callback``. If using localtunnel, this will be something like:

.. code-block:: none

  https://abcdefghij.localtunnel.me/auth/callback

Then update your ``.env`` file to include the *Client ID* and *Client Secret* from the UCL API dashboard, for example:

.. code-block:: none

  UCLAPI_CLIENT_ID=0123456789.0123456789
  UCLAPI_CLIENT_SECRET=0123456789abcdef

Test you've setup your credentials correctly by attempting to log in by visiting ``/auth``.

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

Then update your ``.env`` file to include the API key:

.. code-block:: none

  GOOGLE_MAPS_KEY=0123456789abcdef
