#srbridge.com
#https://github.com/srbridgecom
#https://www.facebook.com/srbridge
#https://www.linkedin.com/in/r-bridge-3baa332a4/
#Python

#Flask RestAPI #Python
#there are two functions: One function to just return or print the data sent
# through GET or POST and
#note you must have flask installed, curcl installed 1st.


#import what we need
from flask import Flask, jsonify, request

#create the app
app = Flask(__name__)

# on the terminal type: curl http://127.0.0.1:5000/ or your IP
# mine was curl http://192.168.0.115:5000
# returns hello world when we use GET. 
# returns the data that we send when we use POST. 
@app.route('/', methods = ['GET', 'POST'])
def home():
        if (request.method == 'GET'):
            data = "hey world"
            return jsonify({'data' : data})
        
app.run(host='0.0.0.0')    #It will make the server externally visible. If the IP 
                            #address of the machine is 192.168.X.X then, from the same network you can 
                            # access it in 5000 port. Like, http://192.168.X.X:5000       
        
#to run the program, outside the dev IDE, open terminal.
#run the python app from terminal
#THIS IS MY TERM OUTPUT
#ryan@ROG:~/Documents/Documents/D.pycharmprojects/pythonProject/build_rest_api$ python3 python_restapi_helloworld.py
# * Serving Flask app 'python_build_restapi' (lazy loading)
# * Environment: production
#   WARNING: This is a development server. Do not use it in a production deployment.
#   Use a production WSGI server instead.
# * Debug mode: off
# * Running on all addresses.
#   WARNING: This is a development server. Do not use it in a production deployment.
# * Running on http://192.168.0.115:5000/ (Press CTRL+C to quit)
#THEN OPEN A NEW TERM WINDOW
#ENTER COMMAND curl http://192.168.0.115:5000/

#OUTPUT WAS curl http://192.168.0.115:5000/
#{"data":"hey world"}
