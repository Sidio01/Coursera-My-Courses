import csv
import os


class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = float(carrying)

    def get_photo_file_ext(self):
        ext = os.path.splitext(self.photo_file_name)
        list_of_ext = ['.jpg', '.jpeg', '.png', '.gif']
        if ext[1] in list_of_ext:
            return ext[1]
        else:
            return ''


class Car(CarBase):
    car_type = 'car'

    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.passenger_seats_count = int(passenger_seats_count)


class Truck(CarBase):
    car_type = 'truck'

    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        self.body_whl = body_whl
        if len(body_whl.split('x')) == 3:
            try:
                self.body_length = float(body_whl.split('x')[0])
                self.body_width = float(body_whl.split('x')[1])
                self.body_height = float(body_whl.split('x')[2])
            except ValueError:
                self.body_length = float(0)
                self.body_width = float(0)
                self.body_height = float(0)
        else:
            self.body_length = float(0)
            self.body_width = float(0)
            self.body_height = float(0)

    def get_body_volume(self):
        try:
            return self.body_length * self.body_width * self.body_height
        except TypeError:
            return 0


class SpecMachine(CarBase):
    car_type = 'spec_machine'

    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.extra = extra


def get_car_list(csv_filename):
    car_list = []
    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)
        for row in reader:
            try:
                if row[0] == 'car':
                    try:
                        new_car = Car(row[1], row[3], row[5], row[2])
                        if new_car.get_photo_file_ext() != '' and row[1] != '':
                            car_list.append(new_car)
                    except ValueError:
                        pass
                elif row[0] == 'truck':
                    try:
                        new_car = Truck(row[1], row[3], row[5], row[4])
                        if new_car.get_photo_file_ext() != '' and row[1] != '':
                            car_list.append(new_car)
                    except ValueError:
                        pass
                elif row[0] == 'spec_machine':
                    try:
                        new_car = SpecMachine(row[1], row[3], row[5], row[6])
                        if new_car.get_photo_file_ext() != '' and row[1] != '' and row[6] != '':
                            car_list.append(new_car)
                    except ValueError:
                        pass
            except IndexError:
                pass
    return car_list
