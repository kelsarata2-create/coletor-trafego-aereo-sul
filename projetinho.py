import requests
import json
from datetime import datetime
from aircraft import Aircraft

opensky = requests.get('https://opensky-network.org/api/states/all?lamin=-34&lomin=-57&lamax=-22&lomax=-48')

if opensky.status_code != 200:
    print('Temos um problema!', opensky.status_code)
    exit()

dados = opensky.json()

frotas = []
nova_frota = []

for lista in dados['states']:
    callsign = lista[1]
    origin = lista[2]
    longitude = lista[5]
    latitude = lista[6]
    altitude_metros = lista[7]
    speed_ms = lista[9]
    aircraft = Aircraft(callsign, origin, longitude, latitude, altitude_metros, speed_ms)
    frotas.append(aircraft)

for avioes in frotas:
    dicionario_frotas = {'Callsign': avioes.callsign, 'Origin': avioes.origin, 'Longitude': avioes.longitude,
                         'Latitude': avioes.latitude}
    try:
        if avioes.altitude_fl > 100:
            dicionario_frotas['Flight level'] = f'FL {int(avioes.altitude_fl)}'
        else:
            fl_para_ft = avioes.altitude_fl * 100
            dicionario_frotas['Altitude'] = f'{int(fl_para_ft)} ft'
    except TypeError:
        dicionario_frotas['Altitude'] = 'Sem dados'
    try:
        dicionario_frotas['Speed'] = f'{int(avioes.speed_kt)} kt'
    except TypeError:
        dicionario_frotas['Speed'] = 'Sem dados'
    nova_frota.append(dicionario_frotas)

with open(f'voos_sul_{datetime.now().strftime("%d-%m-%Y-%H-%M-%S")}.json', 'w', encoding='utf-8') as arquivo:
    json.dump(nova_frota, arquivo, ensure_ascii=False, indent=4)
