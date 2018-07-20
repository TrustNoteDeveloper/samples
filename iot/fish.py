#!/usr/bin/python

# -*- coding: UTF-8 -*-

import RPi.GPIO as GPIO

import time

import requests

import json

GPIO.setmode(GPIO.BOARD)

#GPIO.setmode(GPIO.BCM)

pin=12

GPIO.setup(pin,GPIO.OUT)

#GPIO.output(pin,GPIO.HIGH)

#GPIO.output(pin,GPIO.LOW)

min=-1

while(True):

    r=requests.get("http://127.0.0.1/api/balance/VOXKRZWYYUP6JSSY7FZRKCQT3FAPWCFJ")

    #print r.text

    j=json.loads(r.text)

    amount=j['result']['objBalance']['kPI5sZc1e7vG/nik67qDP4N8sjAnnhYRsUTUB/YvsTY=']

    print "{0}:{1}".format(min,amount)

    if min==-1:

        min=amount

    else:

       if amount>min :

         GPIO.output(pin,GPIO.HIGH)

         min=amount

         time.sleep(10)

       else:

         GPIO.output(pin,GPIO.LOW)

    time.sleep(2)
