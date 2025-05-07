class Engine:
    def start(self):
        print("Engine started.")

class Car:
    def __init__(self, engine):
        self.engine = engine  
    def start_car(self):
        print("Starting the car...")
        self.engine.start()  

engine_obj = Engine()

car_obj = Car(engine_obj)

car_obj.start_car()
