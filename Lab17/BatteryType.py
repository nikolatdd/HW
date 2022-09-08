from enum import Enum

BatteryType = {
	'LiIon':1,
	'NiMH':2,
	'NiCd':3
}

class BatteryType(Enum):
	LiIon=1
	NiMH=2
	NiCd=3

class Battery:
    def __init__(self,type):
        self.battery_type = type
battery1=Battery(BatteryType['NiMH'])
print(battery1)