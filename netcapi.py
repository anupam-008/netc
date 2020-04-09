import connexion
from flask import Flask,request
from flask_cors import CORS, cross_origin
from flask_restful import Resource, Api

# Create the application instance
app = connexion.FlaskApp(__name__, specification_dir='./')

# Read the swagger.yml file to configure the endpoints
app.add_api('swagger.yaml')

CORS(app.app)

@app.route('/') 
def index():
    return 'NETC Vehicle Mapping API'

# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5003, debug=True)
