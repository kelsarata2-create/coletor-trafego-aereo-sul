class Aircraft:
    def __init__(self, callsign, origin, longitude, latitude, altitude_metros, speed_ms):
        self.callsign = callsign
        self.origin = origin
        self.longitude = longitude
        self.latitude = latitude
        if altitude_metros is not None:
            self.altitude_fl = (altitude_metros * 3.28) / 100
        else:
            self.altitude_fl = None
        if speed_ms is not None:
            self.speed_kt = (speed_ms * 1.94)
        else:
            self.speed_kt = None