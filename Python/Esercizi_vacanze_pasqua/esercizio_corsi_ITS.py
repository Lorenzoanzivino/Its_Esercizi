class Room:
    def __init__(self, id: str, floor: int, seats: int):
        self.id = id
        self.floor = floor
        self.seats = seats
        self.area = seats * 2

    def get_id(self):
        return self.id

    def get_floor(self):
        return self.floor

    def get_seats(self):
        return self.seats

    def get_area(self):
        return self.area

class Building:
    def __init__(self, name: str, address: str, floors: int):
        self.name = name
        self.address = address
        self.floors = floors
        self.rooms = []

    def get_floors(self):
        return self.floors

    def get_rooms(self):
        return self.rooms

    def add_room(self, room):
        if room.get_floor() >= 1 and room.get_floor() <= self.floors:
            if room.get_id() not in [room.get_id() for room in self.rooms]:
                self.rooms.append(room)

    def area(self):
        total_area = 0
        for room in self.rooms:
            total_area += room.get_area()
        return total_area

class Person:
    def __init__(self, cf:str, name:str, surname:str, age:int):
        self.cf = cf
        self.name = name
        self.surname = surname
        self.age = age

class Student(Person):
    def __init__(self, cf:str, name:str, surname:str, age:int):
        super().__init__(cf, name, surname, age)
        self.group = None

    def set_group(self, group):
        self.group = group

class Lecturer(Person):
    def __init__(self, cf, name, surname, age):
        super().__init__(cf, name, surname, age)

class Group:
    def __init__(self, name, limit):
        self.name = name
        self.limit = limit
        self.students = []
        self.lecturers = []

    def get_name(self):
        return self.name

    def get_limit(self):
        return self.limit

    def get_students(self):
        return self.students

    def get_limit_lecturers(self):
        number_of_students = len(self.students)
        limit = number_of_students // 10
        return 1 if limit < 1 else limit

    def add_student(self, student):
        if len(self.students) < self.limit:
            self.students.append(student)
            student.set_group(self)

    def add_lecturer(self, lecturer):
        if len(self.lecturers) < self.get_limit_lecturers():
            self.lecturers.append(lecturer)

class Course:
    def __init__(self, name: str, room=None, group=None, lecturer=None):
        self.name = name
        self.room = room
        self.group = group
        self.lecturer = lecturer
        self.groups = []
        self.students = []

    def add_group(self, group):
        if group not in self.groups:
            self.groups.append(group)

    def get_name(self):
        return self.name

    def get_room(self):
        return self.room

    def get_group(self):
        return self.group

    def get_lecturer(self):
        return self.lecturer

    def describe(self):
        return (
            f"Course: {self.name}\n"
            f"Room: {self.room.get_id()} (Floor {self.room.get_floor()})\n"
            f"Group: {self.group.get_name()} with {len(self.group.get_students())} students\n"
            f"Lecturer: {self.lecturer.name} {self.lecturer.surname}"
        )

    def register(self, student):
        for group in self.groups:
            if len(group.get_students()) < group.get_limit():
                group.add_student(student)
                self.students.append(student)
                break
