#srbridge.com
#https://github.com/srbridgecom
#https://www.facebook.com/srbridge
#https://www.linkedin.com/in/r-bridge-3baa332a4/
#Python

#Flask RestAPI #Python
#note you must have flask installed, curcl installed 1st.
# A simple function to calculate the square of a number 
# the number to be squared is sent in the URL when we use GET 

#import what we need
from flask import Flask, jsonify, request

#create the app
app = Flask(__name__)

app.route('/home/<int:num>', methods = ['GET']) 
def disp(num): 
  
    return jsonify({'data': num**2}) 
  
pp.run(host='0.0.0.0')    #It will make the server externally visible. If the IP 
                            #address of the machine is 192.168.X.X then, from the same network you can 
                            # access it in 5000 port. Like, http://192.168.X.X:5000    
  
# driver function 
if __name__ == '__main__': 
  
    app.run(debug = True) 
    
