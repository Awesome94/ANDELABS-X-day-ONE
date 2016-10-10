class Car(object):
    def __init__(self,name='General', model='GM', num_of_wheels=4, vehicle_type='saloon',num_of_doors= 4, speed=0):
        self.name = name
        self.model = model
        self.vehicle_type = vehicle_type
        if name == 'Porsche' or name =='Koenigsegg':
            self.num_of_doors = 2
        else:
            self.num_of_doors = num_of_doors
        if vehicle_type == 'trailer':
            self.num_of_wheels = 8
        else:
            self.num_of_wheels = num_of_wheels
    def is_saloon(self):
        if self.vehicle_type = 'saloon':
            return True
        else:
            return False
    def car_speed(self, car_speed = 0 ):
        if self.vehicle_type == 'trailer':
            self.speed = 77
        else:
            self.speed = speed