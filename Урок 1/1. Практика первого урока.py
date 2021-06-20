class StandartUser:
    user_type = 'None'

    def __init__(self, name, surname, special_type, special):
        self.name, self.surname, self.special = name, surname, special
        self.special_type = special_type

    def __str__(self):
        return f'{self.name} {self.surname} - {self.user_type}'

    def __repr__(self):
        return f'{self.__class__.__name__}("{self.name}", "{self.surname}", "{self.user_type}")'


class Parents(StandartUser):
    user_type = 'Родитель'
    security_level = 0


class Pupil(StandartUser):
    user_type = 'Ученик'
    security_level = 1


class Teacher(StandartUser):
    user_type = 'Учитель'
    security_level = 2


class BossOfTheGym(StandartUser):
    user_type = 'Директор'
    security_level = 3


class StandartRoom:
    def __init__(self, number, room_name):
        self.number = number
        self.room_name = room_name

    room_type = 'None'
    security_level = 0

    def enter_attempt(self, user):
        print(
            f'{user.user_type} {user.name} {user.surname} пытается войти в {self.room_name}({self.number}):',
            end='')
        if user.security_level >= self.security_level:
            print(' успех.')
        else:
            print(' неудача.')

    def __str__(self):
        return f'{self.room_type} - {self.number}'

    def __repr__(self):
        return f'{self.__class__.__name__}("{self.room_type}", {self.number})'


class ActovyZal(StandartRoom):
    room_type = "Актовый зал"


class Classroom(StandartRoom):
    room_type = "Кабинет для занятий"
    security_level = 1


class TeacherRoom(StandartRoom):
    room_type = "Учительская"
    security_level = 2


class BossRoom(StandartRoom):
    room_type = "Директорская"
    security_level = 3


Vova = Pupil('Владимир', 'Путин', 'favourite game', 'Civilization 6')
Mother = Parents('Миринда', 'Цветных', 'favourite film', 'Начало (2010)')
Nikitos = Teacher('Никита', 'Попов', 'favourite joke', 'Шутка про хохла')
Braga = Teacher('Брага', 'Пиво', 'favourite joke', 'Шутка про бар')
Darkholme = BossOfTheGym('Van', 'Darkholme', 'award amount', '100')
people = [Vova, Mother, Nikitos, Braga, Darkholme]
print(people)
print(*people, sep='\n')
print()
scene = ActovyZal(110, 'Актовый зал')
english = Classroom(69420, 'Кабинет английского языка лол')
ukraine = Classroom(666, 'Кабинет украинского языка')
teachersroom = TeacherRoom(10, 'Учительская')
endgame = BossRoom(5, 'Кабинет директора')
classes = [scene, english, ukraine, teachersroom, endgame]
print(classes)
print(*classes, sep='\n')
print()
scene.enter_attempt(Mother)
english.enter_attempt(Mother)
ukraine.enter_attempt(Mother)
teachersroom.enter_attempt(Mother)
endgame.enter_attempt(Mother)
print()
scene.enter_attempt(Vova)
scene.enter_attempt(Mother)
scene.enter_attempt(Nikitos)
scene.enter_attempt(Braga)
scene.enter_attempt(Darkholme)
print()
endgame.enter_attempt(Vova)