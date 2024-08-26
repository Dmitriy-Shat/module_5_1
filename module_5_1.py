class House:
    def __init__(self, name, number):
        self.name = name
        self.number_of_floors = number

    def go_to(self, new_floor):
        if self.number_of_floors <= new_floor or new_floor <= 0:
            print('Такoго этажа нет')
        else:
            new_floor_new = 0
            for i in range(0, new_floor):
                new_floor_new += 1
                print(new_floor_new)


Korp1 = House('Волга', 3)
Korp1.go_to(2)
print(Korp1.name, Korp1.number_of_floors)
Korp2 = House('Долг', 7)
Korp2.go_to(6)
print(Korp2.name, Korp2.number_of_floors)
