# Initialize logger
import logging
from logging.handlers import TimedRotatingFileHandler
from flask import Flask, abort, request
import json
import sys

def create_empty_text(path):
    """
    This will create an empty txt file
    Inputs:
        path (str): path to create the file
    """
    with open(path, 'w') as f:
        pass

# def define_logger(path, when, interval):
#     """
#     Creates a logger object, which will take post requests and append them into txt file.
#     When the given interval is passed from the creation time of the most recent txt file, then a new
#     txt file will be created. This is more efficient then creating files every e.g. 5 minutes if there is no POST request.
#     But it will ensure that POST request within a file only includes the requests that are received within that interval.

#     Inputs:
#         path (str): path for logging file
#         when (str): time component like 's' for seconds, 'm' for minutes
#         interval (int): interval to check and when to renew the file
#     Outputs:
#         logger (obj): logger object to use for appending files
#     """
#     logger = logging.getLogger("Rotating Log")
#     logger.setLevel(logging.INFO)
#     handler = TimedRotatingFileHandler(path, when=when, interval=interval)
#     logger.addHandler(handler)

#     return logger

# main functions
prefix = sys.argv[1]
#prefix = 'prefix'
# create empty Raw.txt
raw_path = '/srv/runme/' + prefix + '/Raw.txt'
create_empty_text(raw_path)
# create empty proc.txt
proc_path = '/srv/runme/' + prefix + '/proc.txt'
create_empty_text(proc_path)

logger = logging.getLogger("Rotating Log")
logger.setLevel(logging.INFO)
handler = TimedRotatingFileHandler(raw_path, when='m', interval=2)
logger.addHandler(handler)


app = Flask(__name__)
@app.route('/', methods=['POST'])
def main():
    """
    Flask app which will listen to JSON POST requests at port 8080
    """
    if not request.json:
        print('Not a JSON file')
        return abort(400)
    else:
        # append request to log files
        text = json.dumps(request.json)
        with open(raw_path, 'a') as f:
            logger.info(text)
        # process incoming request
        try:
            # if valid
            d = request.json
            name = d['name']
            age = d['prop']['age']
            with open(proc_path, 'a') as f:
                f.write(name + '\t' + str(age) + '\n')
        except:
            print("Not a 'valid' JSON blob: {}".format(text))
        return 'OK'

# @app.route('/', methods=['GET'])
# def index():
#     return "This is the homepage, you can POST your single line JSON files at localhost:8080/process_json/"


# main functions
# prefix = sys.argv[1]
# #prefix = 'prefix'
# # create empty Raw.txt
# raw_path = '/srv/runme/' + prefix + '/Raw.txt'
# create_empty_text(raw_path)
# # create empty proc.txt
# proc_path = '/srv/runme/' + prefix + '/proc.txt'
# create_empty_text(proc_path)
# # get logger
# logger = define_logger(raw_path, 'm', 2)
# run flask app
app.run(host='0.0.0.0', port=8080)