#!/usr/bin/env python
# -*- coding: utf-8 -*-

#import os

from twilio.rest import Client

ACCOUNT_SID = 'AC2de11e8363a8777757f25ec28a033ecb'
AUTH_TOKEN = '2a86cf17409682554a141fdc60f554cd'
client = Client(ACCOUNT_SID, AUTH_TOKEN)

msj_1 = "Existe un peligro de inundación del 95% en la zona donde se encuentra. Diríjase con sus bienes mas preciados al centro de refugio lo más rápido posible."

message11 = client.messages.create(
    to="+5491134246401", 
    from_="+12018318124",
    body=msj_1 )
#    body="Se viene la inundacion. Deje lo que este haciendo y venga con los pibes. SMS enviado desde python! :)")

message12 = client.messages.create(
#    to="+5491160190584", #cami
    to="+5491168006756", #chris
    from_="+12018318124",
    body=msj_1 )

message13 = client.messages.create(
    to="+5491141648522", #sampa
    from_="+12018318124",
    body=msj_1 )


print(message11.sid)
print(message12.sid)
print(message13.sid)

