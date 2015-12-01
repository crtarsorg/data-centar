# coding=utf-8
from app import mongo
from rashodi_data_feeder import RashodiDataFeed
import re
from bson.regex import Regex

class PrihodiDataFeed():

    def calculate_sum_of_expenditure_types(self, query_params):

        return RashodiDataFeed().calculate_sum_of_expenditure_types(query_params)

    def build_json_response_for_parent_categories(self, query_params):

        # Since we use the same mongo query as in Rashodi to build JSON response
        # we use RashdoiDataFeed function, tipPodataka value prihodi determines the difference of json response
        json_doc = RashodiDataFeed().build_json_response_for_parent_categories(query_params)

        return json_doc

    def retrieve_list_of_municipalities_for_given_class(self, query_params):

        # Since we use the same mongo query as in Rashodi to build JSON response
        # we use RashdoiDataFeed function, tipPodataka value prihodi determines the difference of json response
        return RashodiDataFeed().retrieve_list_of_municipalities_for_given_class(query_params)

