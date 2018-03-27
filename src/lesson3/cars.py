import os
import csv


class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        self.carrying = float(carrying)
        self.photo_file_name = photo_file_name

    def get_photo_file_ext(self):
        return os.path.splitext(self.photo_file_name)[1]


class Car(CarBase):
    car_type = 'car'

    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.passenger_seats_count = int(passenger_seats_count)


class Truck(CarBase):
    car_type = 'truck'

    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        try:
            params = body_whl.split('x')
            self.body_width = float(params[0])
            self.body_height = float(params[1])
            self.body_length = float(params[2])
        except ValueError:
            self.body_width = 0.0
            self.body_height = 0.0
            self.body_length = 0.0

    def get_body_volume(self):
        return self.body_width * self.body_height * self.body_length


class SpecMachine(CarBase):
    car_type = 'spec_machine'

    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.extra = extra


def get_car_list(csv_filename):
    list = []

    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)
        for row in reader:
            try:
                type = row[0]
                if type == '':
                    continue

                del row[0]
                if type == 'car':
                    del row[-1]
                    list.append(Car(row[0], row[2], row[-1], row[1]))
                elif type == 'truck':
                    del row[-1]
                    list.append(Truck(row[0], row[2], row[-1], row[3]))
                elif type == 'spec_machine':
                    list.append(SpecMachine(row[0], row[2], row[4], row[5]))

            except IndexError as e:
                continue

    return list

# print(get_car_list('./cars.csv'))
