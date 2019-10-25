"""
This is gateway application to get sensor data and post to
WebServer Application.
"""
import json
from datetime import datetime
import requests
from flask import Flask, request, jsonify

WEB_SERVER_APP_IP = '192.168.93.1:9001'

APP = Flask(__name__)

class CacheSensorsData:
    """
       This class cached the sensor data and filter
       with latest sensors data.
    """
    def __init__(self):
        self.data = None

    def return_data_to_sample_web(self, sencor_rec):
        """
           This method return a latest sensor data.
        """
        filter_result = []
        if not self.data:
            self.data = sencor_rec
            return self.data
        for each in sencor_rec:
            for prv_rec in self.data:
                if prv_rec['sensor_serial_num'] == each['sensor_serial_num']:
                    if prv_rec['sensor_status'] != each['sensor_status']:
                        filter_result.append(each)
        self.data = sencor_rec
        return filter_result or self.data

CLS_OBJ = CacheSensorsData()

@APP.route('/fogapp/api', methods=['POST', 'GET'])
def fog_app():
    """
       This method get data from the sensor device.
    """
    rec = request.json
    upd_sencor_rec = CLS_OBJ.return_data_to_sample_web(rec)
    url = 'http://' + WEB_SERVER_APP_IP + '/getSensorData/api'
    header = {"content-type": "application/json"}
    try:
        requests.post(url, json=upd_sencor_rec, headers=header, verify=False)
    except Exception as exp:
        print('Error: {}'.format(exp.__str__()))
    return json.dumps(upd_sencor_rec)

@APP.route('/time')
def time():
    """
        To test application is running in Gateway
    """
    current_time = datetime.now().isoformat(' ')
    return jsonify({"datetime": current_time, "sensorsData": CLS_OBJ.data})

if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=8000)
