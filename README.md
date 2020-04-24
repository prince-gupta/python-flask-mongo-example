# python-flask-mongo-example

Project to showcase integration of Python, Flask,Angular,Marshmallow and PyMongo

Flask : Full Stack Framework for Python
Marshmallow: ORM Tool for Python
PyMongo : Tool to access Mongo and Dealing with all operations of saving, updating, retrieving and deleting collections.

Project is using Okta as SSO Server with its SDK.

### To Run the project one need to follow below steps : 
  #### To Run frontend : 
  1. go to app/http/web-app
  2. run npm install
  3. run ng serve
  
  #### To Run backend : 
  1. go to project folder
  2. FLASK_APP=$PWD/app/http/api/endpoints.py FLASK_ENV=development pipenv run python -m flask run --port 4433
  
 