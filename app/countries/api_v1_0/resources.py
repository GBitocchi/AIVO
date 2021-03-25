from flask import Blueprint, jsonify, make_response
from flask_restful import Api, Resource
import pandas as pd

countries_v1_0_bp = Blueprint('countries_v1_0_bp', __name__)
api = Api(countries_v1_0_bp)

class CountryListResource(Resource):
    def get(self, name_index, value_index):
        iter_csv = pd.read_csv('resources/BLI_28032019144925238.csv', iterator=True)
        countries_retrieved = pd.concat([chunk[(chunk['Indicator'] == name_index) & (chunk['Value'] > value_index)] for chunk in iter_csv])
        if countries_retrieved.empty:
            no_found_response = make_response('No countries matched with the input condition', 404)
            no_found_response.mimetype = "text/plain"
            return no_found_response
        return jsonify(countries = countries_retrieved['Country'].tolist())

api.add_resource(CountryListResource, '/api/v1.0/countries/<string:name_index>/<float:value_index>', endpoint='country_list_resource')