from angular_flask import app

def runserver():
    app.run(host='0.0.0.0', debug=True, port=9001)

if __name__ == '__main__':
    runserver()