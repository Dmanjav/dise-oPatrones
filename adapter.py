# Diego Manjarrez Viveros
# Tarea:Escribe un adaptador para el Speedometer de forma  que trabaje con la clase CarDisplay
import random


class MphSpeedometer:
    """Estamos pretendiendo que esta es una clase exerna que no podemos cambiar"""

    def __init__(self):
        pass

    def get_speed(self):
        """Regresa la velocidad en MPH (Millas por hora)"""
        speed = random.randint(0, 100)
        print("Speed in MPH: {}".format(speed))
        return speed


class MphToKphSpeedometerAdapter(MphSpeedometer):
    
    def __init__(self, mph_speedometer):
        self.mph_speedometer = mph_speedometer
        
    def get_speed(self):
        mph_speed = self.mph_speedometer.get_speed()
        kph_speed = mph_speed * 1.60934
        print(f"Speed in KPH: {kph_speed}")
        return kph_speed


class CarDisplay:
    def __init__(self, speedometer):
        self.speedometer = speedometer

    def show_speed(self):
        # Mostrar la velocidad utilizando el método get_speed del adaptador
        speed = self.speedometer.get_speed()
        print(f"Speed: {speed}")

if __name__ == "__main__":
    """TAREA: listo"""
    speedometer = MphSpeedometer()
    kms = MphToKphSpeedometerAdapter(speedometer)
    car_display = CarDisplay(kms)
    car_display.show_speed()