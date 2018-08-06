#!/product/pci/sw/LocalCentOS5_64bit/Python-2.7.2/bin/python
import sys, os, os.path
from Tkinter import *
import logging
import subprocess
import shutil
import math
import platform
import tkFileDialog
import socket
import datetime
#import stitching_outside

global fullPath,dstPath ,dffPath
fullPath = "/users/pci/tom/AMP-ToolKit/"
dstPath = "/users/pci/Desktop/Resistors_Data/"
dffPath = "/pci/tmp/aor/height_calc/depth.pgm"
sys.path.insert(0, fullPath+"Poly_position/")
import Manual_pointer
import angleCheck



# for stand-alone evocation
# go to some location with good AutoTesting
#robot_dir = '/home/leon-m/dev/PCI/RTC-LIFT-AOS-Common/Root/Pci/Application/automatic_test/robot/'
robot_dir = os.getenv("SCRIPT_WORKING_DIR")
print "SCRIPT_WORKING_DIR = " + str(robot_dir)
sys.path.insert(0, robot_dir)

os.chdir(robot_dir)
import AutoTesting
import CosNaming, _GlobalIDL
import time
import run_test_delay
import smtplib

######################################################################
# initialize
autoTest = AutoTesting.AutoTesting()
autoTest.auto_test_connect_to_app()
######################################################################

global logger
# logger settings
logger = logging.getLogger("logging_tryout2")
logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
hdlr = logging.FileHandler(fullPath+"Poly_position/LogFile.log")

# create formatter
formatter = logging.Formatter("%(asctime)s;%(levelname)s;%(message)s")

# add formatter to ch
ch.setFormatter(formatter)
hdlr.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)
logger.addHandler(hdlr)
######################################################################

global year, month, date
date = time.strftime("%x").split('/')
date = date[1]+date[0]+date[2]
month = time.strftime("%B")
year = time.strftime("%Y")

dst = dstPath + year +"/"+month+"/"+date+"/"
material = ''


def depo_func(donorIn, donorOut, dst, material, polygons_path, pitch):
    autoTest.auto_test_set_param_value('droplet_pitch', pitch)
    logger.info("Changed droplet_pitch Parameter to - " + str(pitch))

    autoTest.load_material(material)
    logger.info("Loading Material - " + material)

    autoTest.load_polygons(polygons_path)
    logger.info("Loading Polygons - " + polygons_path)

    logger.info("Start Deposition")
    autoTest.deposit_screen_polygon(donorIn, donorOut,
                                    dst + "/DonorHoles" + "/R" + "_DonorHoles")
    logger.info("Deposition Done!")



polygons_path = fullPath + "Polygons/Auto_position_polygons/Line/Line_polygon_to_RePosition_output_LineDepoSeed"
donorIn = True
donorOut = True
for r in range (1,4):
    for i in range (2,8,2):
        x = 25*i
        y = 25*r
        autoTest.move_relative(x,y)
        print (autoTest.get_optical_head_position())
        depo_func(donorIn, donorOut, dst, material, polygons_path,i)
