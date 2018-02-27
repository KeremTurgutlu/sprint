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

# run flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)