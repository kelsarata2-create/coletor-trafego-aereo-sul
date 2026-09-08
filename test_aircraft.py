from aircraft import Aircraft


def test_conversao_altitude():
    aircraft = Aircraft(
        callsign='Teste',
        origin='Brasil',
        longitude=49.0,
        latitude=45.0,
        altitude_metros=500,
        speed_ms= 200
    )
    resultado_esperado = (500 * 3.28) / 100
    assert aircraft.altitude_fl == resultado_esperado

def test_conversao_speed():
    aircraft = Aircraft(
        callsign='Teste',
        origin='Brasil',
        longitude=49.0,
        latitude=45.0,
        altitude_metros=500,
        speed_ms= 200
    )
    resultado_esperado = 200 * 1.94
    assert aircraft.speed_kt == resultado_esperado

def test_none():
    aircraft = Aircraft(
        callsign='Teste',
        origin='Brasil',
        longitude=49.0,
        latitude=45.0,
        altitude_metros=None,
        speed_ms= None
    )
    assert aircraft.altitude_fl is None
    assert aircraft.speed_kt is None

