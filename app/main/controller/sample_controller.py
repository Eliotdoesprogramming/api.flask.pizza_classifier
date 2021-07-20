from flask import Flask, request, jsonify

from service.api_service import Service
class SampleController(object):
    def __init__(self,app:Flask,service:Service) -> None:
        self.app=app
        self.service=service
        self.add_routes(app)
    def add_routes(self,app:Flask):
       
        app.add_url_rule('/evaluate',methods=['POST'],view_func=self.evaluate)
    def evaluate(self):
        # get the request body and put it into a variable named img
        img = request.json['img']
        # call the evaluate method on the service
        # and put the result into a variable named result
        result = self.service.evaluate_image(img)
        # return the result as json
        
        return jsonify(result)                    
