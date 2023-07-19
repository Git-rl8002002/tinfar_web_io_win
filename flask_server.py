#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# Author   : JasonHung
# Date     : 20230330
# Function : web io cloud platform

from argparse import Namespace
from dataclasses import dataclass
from distutils.log import debug
from email import charset
from hashlib import md5
from tabnanny import check
import hashlib , random , minimalmodbus , json , time , logging , sys , os
from flask import Flask,render_template,request,session,url_for,redirect,escape
from flask_socketio import SocketIO , emit 
#import socketio
from control.web_cloud_dao import web_cloud_dao 

db = web_cloud_dao()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret' 
socketio = SocketIO(app)  


########
# log
########
log_format = "%(asctime)s %(message)s"
logging.basicConfig(format=log_format , level=logging.INFO , datefmt="%Y-%m-%d %H:%M:%S")

##############
# variables
##############
title  = web_cloud_dao.param['title']


##########
# /sd
##########
@app.route("/sd")
def sd():
        
    ### record time
    r_time  = time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime())

    ### port 
    jnc_sd = minimalmodbus.Instrument(port='COM3' , slaveaddress=1 , mode=minimalmodbus.MODE_RTU)
    jnc_sd.serial.baudrate = 9600
    jnc_sd.serial.timeout = 1
    jnc_sd.clear_buffers_before_each_transaction = True
    jnc_sd.close_port_after_each_call = True
    jnc_sd.debug = False

    try:
        ###  show SD read register val
        sd_val1 = jnc_sd.read_register(int('0x0000',16),functioncode=int(4))
        
        ### json format
        json_format = {"date":r_time , "sd-co2" : sd_val1}
        json_val = json.dumps(json_format)
        #json_val = json.dumps({'date':r_time , 'sd-co2':sd_val1} , sort_keys=True , indent=4 , separators=(',',': '))
        #json_val = demjson.encode(json_format)
        
        return render_template('sd.html' , res=json_val)

    except Exception as e:
        logging.info('< Error > monitor sd : ' + str(e))
    finally:
        jnc_sd.serial.close()

        
    


################################################################################################################################################
#
# start
#
################################################################################################################################################
if __name__ == "__main__":
    ### Flask
    #app.run(host="0.0.0.0" , port=8080 , debug=True)
    
    ### Flask-SocketIO
    socketio.run(app , host="0.0.0.0" , port=8095 , debug=True)
