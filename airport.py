class Airplane:
    def __init__(self, name, count_of_passangers):
        self.name = name
        self.count_of_passangers = count_of_passangers

    def getName(self):
        return self.name

    def getPassengers(self):
        return self.count_of_passangers


class Airport:
    def __init__(self, name, list_of_landed_airplanes):
        self.name = name
        self.list_of_landed_airplanes = list_of_landed_airplanes

    def land(self, airplane):
        self.list_of_landed_airplanes.append(airplane)

    def printAllLandedAirplanes(self):
        for airplane in self.list_of_landed_airplanes:
            print(airplane.name)

    def getStats(self):
        total = 0
        for airplane in self.list_of_landed_airplanes:
            total += airplane.getPassengers()
        return total



# Here are more commands to code

wien_airport = Airport('Wien', [])

boeing = Airplane('boeing 7576', 40)
air_bus = Airplane('air bus 399', 38)

print(boeing.getName())
print(boeing.getPassengers())

wien_airport.land(boeing)
wien_airport.land(air_bus)

wien_airport.printAllLandedAirplanes()

print(wien_airport.getStats())