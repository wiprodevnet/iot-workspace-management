import json
from datetime import datetime
from flask import Flask, render_template, request
from flaskext.mysql import MySQL
timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

#app = Flask(__name__)
from angular_flask import app
mysql = MySQL()

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Rajeev@123'
app.config['MYSQL_DATABASE_DB'] = 'TrackWorkSpace'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql.init_app(app)

# First, let's create the MySQL connection:
conn = mysql.connect()
# create cursur
cursor = conn.cursor()
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/building_data', methods=['GET'])
def get_building_data():
    """
        To get building data
    """
    sql_select_Query = "select * from building"
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    return json.dumps(records)

@app.route('/floor_data', methods=['GET'])
def get_floor_data():
    """
		To get building data
	"""
    building_idn = request.args.get("building_id", type=int)
    sql_select_Query = """select * from floor where building_idn = %s"""
    cursor.execute(sql_select_Query, (building_idn,))
    records = cursor.fetchall()
    return json.dumps(records)

@app.route('/cubicle_data', methods=['GET'])
def get_cubicle_data():
    """
       To get building data
    """
    floor_idn = request.args.get("floor_id", type=int)
    sql_select_Query = """select * from cubicle where floor_idn = %s"""
    cursor.execute(sql_select_Query, (floor_idn,))
    records = cursor.fetchall()
    return json.dumps(records)

@app.route('/save_sensor_data', methods=["POST"])
def save_sensor_data():
    """
    Save sensor data into database
    """
    msg = ''
    sensor_data = request.get_json().get('params')
    sensor_serial_no = sensor_data['sensor_serial_no']
    cubicle_idn = sensor_data['cubicle_idn']
    sensor_type = 'positional'
    registered_sensor_list = get_registered_sensor_data()
    if sensor_serial_no not in registered_sensor_list:
        sql_select_Query = """INSERT INTO sensor_details (serial_number, sensor_type, cubicle_idn)
                              VALUES (%s, %s, %s)
                           """
        cursor.execute(sql_select_Query, (sensor_serial_no, sensor_type, cubicle_idn))
        conn.commit()
        msg = 'Sensor data added successfully'
    else:
        msg = 'Sensor Serial Number already registered'
    return json.dumps({'message': msg})

@app.route('/work_space', methods=["GET"])
def render_work_space_data():
    """
       To get workspace data
    """
    sql_select_Query = """SELECT SERIAL_NUMBER,
	                              SENSOR_STATUS,
	                              CUBICLE_NUMBER,
	                              FLOOR_NUMBER,
	                              BUILDING_NAME
	                        FROM sensor_status AS SS
							INNER JOIN sensor_details AS SD
								ON SS.sensor_idn = SD.sensor_idn
						    INNER JOIN cubicle AS C
								ON C.cubicle_idn = SD.cubicle_idn
							inner join floor as F
								on F.floor_idn = C.floor_idn
							inner join building as B
								on B.building_idn = F.building_idn
                       """
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    return json.dumps(records)

@app.route('/getSensorData/api', methods=["POST"])
def insert_sensor_data():
    """
       Get sensor data from Gateway and insert or update
    """
    message = ''
    sensor_gateway_data = request.json
    print(sensor_gateway_data)
    for each_sensor_data in sensor_gateway_data:
        message = insert_update_sensor_data(each_sensor_data)
    return message

def insert_update_sensor_data(sensor_gateway_data):
    """
       Insert and update sensor data into DB
    """
    message = ''
    registered_sensor_list = get_registered_sensor_data()
    payload_sensor_serial_no = sensor_gateway_data['sensor_serial_num']
    payload_sensor_status = sensor_gateway_data['sensor_status']
    if payload_sensor_serial_no in registered_sensor_list:
        sensor_status_record = get_sensor_status_data(payload_sensor_serial_no)
        if sensor_status_record:
            # update the sensor status
            if payload_sensor_status != sensor_status_record[0][2]:
                sensor_status_idn = sensor_status_record[0][0]
                message = update_sensor_status(payload_sensor_status, sensor_status_idn)
        else:
            message = add_sensor_status(payload_sensor_serial_no, payload_sensor_status)
    else:
        message = "Sensor is not registered"
    print(message)
    return message

def get_registered_sensor_data():
    """
       To get all registered sensor data from DB
    """
    sensor_details_select_Query = """select * from sensor_details"""
    cursor.execute(sensor_details_select_Query)
    registered_sensor_records = cursor.fetchall()
    sensor_serial_no_list = [each[1] for each in registered_sensor_records]
    return sensor_serial_no_list

def get_sensor_status_data(sensor_serial_no):
    """
       To get all sensor status from database
    """
    sensor_status_select_Query = """select * from sensor_status where sensor_serial_no = %s """
    cursor.execute(sensor_status_select_Query, (sensor_serial_no,))
    sensor_status_records = cursor.fetchall()
    return sensor_status_records

def update_sensor_status(sensor_status, sensor_status_idn):
    """
        Update sensor status if any changes recieved vai IOXApp
    """
    update_sensor_query= """
                           UPDATE sensor_status
                           SET sensor_status = %s, upd_dt = %s
                           WHERE sensor_status_idn=%s
                         """
    cursor.execute(update_sensor_query, (sensor_status, timestamp,  sensor_status_idn))
    conn.commit()
    message = "Sensor data updated successfully"
    return message

def add_sensor_status(sensor_serial_no, sensor_status):
    """
        To add sensor data if first time sent
    """
    sensor_details_select_Query = """select * from sensor_details where serial_number = %s"""
    cursor.execute(sensor_details_select_Query,(sensor_serial_no,))
    registered_sensor_records = cursor.fetchall()
    sensor_idn = registered_sensor_records[0][0]
    sql_insert_Query = """INSERT INTO sensor_status (sensor_serial_no, sensor_status, sensor_idn, crt_dt, upd_dt) 
                                  VALUES (%s, %s, %s, %s, %s)
                               """
    cursor.execute(sql_insert_Query, (sensor_serial_no, sensor_status, sensor_idn,  timestamp, timestamp))
    conn.commit()
    message = "Sensor data added successfully"
    return message

if __name__ == '__main__':
    #get_sensor_data_from_gateway()
    app.run(host='0.0.0.0', debug=True, port=9001)
