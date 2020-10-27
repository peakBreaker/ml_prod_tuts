import logging
import json
import pickle
import os

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    data = json.loads(req.params['data'])
    curr_dir = os.getcwd()
    files_in_dir = os.listdir(os.path.dirname(os.path.realpath(__file__)))
    logging.info(f'got data {data}, curr dir is {curr_dir} - loading model from avail files: {files_in_dir}')
    model_f_path = os.path.dirname(os.path.realpath(__file__))+'/finalized_model.pkl'
    logging.info(f'Got model filepath : {model_f_path}')
    model_f = open(model_f_path, 'rb')
    logging.info(f'Got model file, deserializing..')
    model = pickle.load(model_f)
    logging.info(f'loaded model - getting predictions..')
    predictions = model.predict(data)
    logging.info(f'got predictions {predictions} - returning')
    return func.HttpResponse(json.dumps(predictions.tolist()))
