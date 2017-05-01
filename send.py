#!/usr/bin/env python
# -*- coding: utf-8 -*-

#import os

from twilio.rest import Client

ACCOUNT_SID = 'AC2de11e8363a8777757f25ec28a033ecb'
AUTH_TOKEN = '2a86cf17409682554a141fdc60f554cd'
client = Client(ACCOUNT_SID, AUTH_TOKEN)

#"Existe un peligro de inundación del 95% en la zona donde se encuentra. Diríjase con sus bienes mas preciados al centro de refugio lo más rápido posible."
msj_1 = """Alerta de evacuación!
Existe un peligro de inundación del 95% para Comodoro Rivadavia y alrededores.
Diríjase cuanto antes al centro de refugio más cercano, que se encuentra en Av. 10 de Noviembre y Polonia.
- Lleve consigo solo lo esencial
- Si tiene tiempo, desconecte el suministro de gas, electricidad y agua
- Desconecte los electrodomésticos para evitar descargas eléctricas cuando se restablezca el suministro eléctrico
- Siga las rutas de evacuación designadas y prepárese ante la posibilidad de que haya mucho tráfico
- No trate de atravesar en automóvil o a pie los riachuelos y las calles inundadas"""

message11 = client.messages.create(
    to="+5491134246401", #joaco
    from_="+12018318124",
    body=msj_1 )

message12 = client.messages.create(
    to="+5491168006756", #chris
    from_="+12018318124",
    body=msj_1 )

message13 = client.messages.create(
    to="+5491141648522", #sampa
    from_="+12018318124",
    body=msj_1 )
    
message14 = client.messages.create(
    to="+5491160190584", #cami
    from_="+12018318124",
    body=msj_1 )

print(message11.sid)
print(message12.sid)
print(message13.sid)
print(message14.sid)

