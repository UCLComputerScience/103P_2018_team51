Azure Deployment Manual
=======================

PostgreSQL server
-----------------

#. Create a new PostgreSQL server: https://portal.azure.com/#create/Microsoft.PostgreSQLServer
#. Open the configuration page for the PostgreSQL server you've created
#. Navigate to "Connection Security" under "Settings" in the sidebar
#. Toggle "Allow access to Azure services" to "On"
#. Click "Add My IP"
#. Click "Save"

Create Web App
--------------

#. Create a new Web App in the same resource group as your PostgreSQL server: https://portal.azure.com/#create/Microsoft.WebSite
#. Open the configuration page for the Web App you've created
#. Navigate to "Extensions" under "Development Tools in" the sidebar
#. Click "Add", and install "Python 3.6.4 x86"

Configure Web App
----------------

Now we need to provide the Web App with some settings to run:

#. Navigate to "Application settings" under "Settings" on the sidebar.
#. Scroll down to "Application settings" and click "Add new setting" for each of the following:

.. list-table::
   :header-rows: 1

   * - Name
     - Value
   * - DATABASE_NAME
     - postgresql
   * - DATABASE_USER
     - *enter the postgresql username you previously created*
   * - DATABASE_PASSWORD
     - *enter the postgresql password you previously created*
   * - DATABASE_HOST
     - *enter the domain of the postgresql server you previously created*
   * - SECRET_KEY
     - *randomly generate a string and enter it here*
   * - ALLOWED_HOSTS
     - *enter the domain of the web app you've created*
   * - UCLAPI_CLIENT_ID
     - *create* :ref:`ucl-api-oauth-setup` *and enter the client id here*
   * - UCLAPI_CLIENT_SECRET
     - *create* :ref:`ucl-api-oauth-setup` *and enter the client secret here*
   * - GOOGLE_MAPS_KEY
     - *create a* :ref:`gmaps-api-setup` *and enter it here*

Finally click "Save".

Create Deployment User
----------------------

Follow the documentation here: https://docs.microsoft.com/en-gb/azure/app-service/app-service-deployment-credentials

Deploy Web App
--------------

#. Clone the repository: ``git clone https://github.com/UCLComputerScience/103P_2018_team51.git``
#. Enter the cloned repository: ``cd 103P_2018_team51``
#. Navigate to your Web App's overview page
#. Create a new remote from the "Git clone url" on the Web App Overview page: ``git remote add azure <paste "Git clone url" here>``
#. Deploy the app to azure with: ``git push azure master``
#. Enter the previously created deployment credentials when prompted

Create superuser
----------------

Run the ``python3 manage.py createsuperuser`` command locally by setting the database settings on the command line:

.. code-block:: none

  DATABASE_NAME=postgresql DATABASE_USER=<enter value> DATABASE_PASSWORD=<enter value> DATABASE_HOST=<enter value> python3 manage.py createsuperuser

*UPI* stands for Unique Person Identifier, a unique id given to every member of UCL, set this to your own UPI (found on your UCL ID card) if you want to be able to log into the admin interface through UCL API OAuth.

You can now log into the admin interface at: https://your-domain/admin/login
