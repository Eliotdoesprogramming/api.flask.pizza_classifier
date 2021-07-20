from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from service.api_service import Service
from controller.sample_controller import SampleController
#single db instance


#init flask application
app = Flask(__name__)

#sqlalchemy database config, dialect://user:pass@url:port/dbname




service = Service(app)

sample_controller = SampleController(app,service)

if(__name__=='__main__'):
    
    app.run(debug=True)
