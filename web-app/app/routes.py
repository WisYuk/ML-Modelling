from flask import request, jsonify
from flask_restful import Resource
import pandas as pd
import tensorflow as tf
from .model import enhanced_similarity, weather_decider
import asyncio

class Recommendation(Resource):
    async def post(self):
        data = request.get_json()  # This should not be awaited as it is a synchronous method
        tgl = data['date'].split('_')
        l = []
        if weather_decider(int(tgl[1])):
            l = [0,1]
        else:
            l = [1,0]
        print(data['user_input'] + l)
        user_input = tf.constant(data['user_input'] + l, tf.float32)

        # Load your dummy CSV file
        kk = pd.read_csv('data_final.csv')
        features = tf.constant(kk.iloc[:, :8].to_numpy(), tf.float32)
        ratings = tf.constant(kk.iloc[:, 9].to_numpy(), tf.float32)
        # print(ratings)
        sentiments = tf.constant(kk.iloc[:, 8].to_numpy(), tf.float32)

        recommendations = enhanced_similarity(features, user_input, ratings, sentiments)
        sorted_indices = tf.argsort(recommendations, direction='DESCENDING')
        N = data.get('N', 10)
        top_N_indices = (sorted_indices[:N].numpy()+1).tolist()

        return jsonify({"top_N_indices": top_N_indices})

# Helper function to run the async method
def async_route(app, route, method):
    async def run_async_method(*args, **kwargs):
        return await method(*args, **kwargs)
    app.add_url_rule(route, view_func=run_async_method, methods=['POST'])

# Add the route to the Flask app
def add_routes(app):
    async_route(app, '/recommend', Recommendation().post)
