"""
This will act as clinet to send sensor Data to gateway app.
"""

import time
import requests
from sencors_data import PAYLOAD, FOG_APP_IP


class RequestSensor:
    """
    This class written for post sensor data to the fog app.
    """
    def main(self):
        """
            This method send a sensors data to the fog app.
        """
        header = {"content-type": "application/json"}
        URL = 'http://' + FOG_APP_IP + '/fogapp/api'
        while True:
            for each_payload in PAYLOAD:
                try:
                    resp = requests.post(URL, json=each_payload, headers=header, verify=False)
                except Exception as error:
                    print('Error: {}'.format(error.__str__()))
                else:
                    print("Post status code:"+ str(resp.status_code))
                time.sleep(15)

if __name__ == '__main__':
    OBJ_REQ = RequestSensor()
    OBJ_REQ.main()
