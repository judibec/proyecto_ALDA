import random
from faker import Faker
from unidecode import unidecode

"""
    Complejidad O(1)
"""


def gender():
    sex = random.choice(["M", "F"])
    return sex


"""
    Complejidad O(1)
"""


def firstName(sex):
    fake = Faker("es_Co")
    return (
        fake.first_name_male() + " " + fake.first_name_male()
        if sex == "M"
        else fake.first_name_female() + " " + fake.first_name_female()
    )


"""
    Complejidad O(1)
"""


def lastName():
    fake = Faker("es_Co")
    return fake.last_name() + " " + fake.last_name()


"""
    Complejidad O(n)
"""


def phoneNumber():
    start = [
        "300",
        "301",
        "302",
        "303",
        "304",
        "324",
        "305",
        "310",
        "311",
        "312",
        "313",
        "314",
        "320",
        "321",
        "322",
        "323",
        "315",
        "316",
        "317",
        "318",
        "319",
        "350",
        "351",
        "302",
        "323",
        "324",
        "333",
    ]
    number = random.choice(start)
    for i in range(7):
        number += str(random.randint(0, 9))
    return number


"""
    Complejidad O(n)
"""


def addressCityAndPostalCode():
    fake = Faker("es_Co")
    return fake.address().split("\n")


"""
    Complejidad O(1)
"""


def address(list):
    return list[0]


"""
    Complejidad O(n)
"""


def department(list):
    return list[-1].split(",")[1] if len(list[-1].split(",")) > 1 else list[-1].split(",")[0]


"""
    Complejidad O(n)
"""


def municipality(list):
    return list[-1].split(",")[0]


"""
    Complejidad O(1)
"""


def PostalCode(list):
    return list[-2]


"""
    Complejidad O(1)
"""


def hasChild():
    return random.choice([True, False])


"""
    Complejidad O(1)
"""


def children(flag):
    amount = [1, 2, 3, 4, 5]
    return random.choices(amount, weights=(40, 40, 20, 10, 5))[0] if flag else 0


"""
    Complejidad O(1)
"""


def hasDeadChild():
    return random.choice([True, False])


"""
    Complejidad O(1)
"""


def birthday():
    faker = Faker("es_Co")
    return faker.date_of_birth(minimum_age=18, maximum_age=80)


"""
    Complejidad O(1)
"""


def job(study):
    faker = Faker("es_Co")
    return faker.job() if study != "N/A" else "N/A"


"""
    Complejidad O(1)
"""


def educationLevel():
    edLevel = ["N/A", "Bachiller", "Pregrado", "Tecnologo", "Tecnico", "Posgrado", "Maestria", "Doctorado"]
    return random.choices(edLevel, weights=(45, 50, 30, 30, 30, 20, 10, 7))[0]


"""
    Complejidad O(1)
"""


def typeOfStudy(study):
    return random.choice(["Rural", "Urbana", "Particular"]) if study != "N/A" else "N/A"


"""
    Complejidad O(n)
"""


def email(name, lastName):
    name = name.split(" ")[0]
    lastName = lastName.split(" ")[0]
    res = ""
    domains = ["@gmail.com", "@hotmail.com", "@outlook.com", "@yahoo.com"]
    sizeName = random.randint(1, len(name))
    res += name[:sizeName]
    res += random.choice(["-", "_", ".", ""])
    sizeLastName = random.randint(1, len(lastName))
    res += lastName[:sizeLastName]
    random.randint(0, 4)
    randomNumbers = random.SystemRandom().sample([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], random.randint(0, 4))
    for i in randomNumbers:
        res += str(i)
    res += random.choice(domains)
    return unidecode(res).lower()


"""
    Complejidad O(1)
"""


def rh():
    group = ["A", "O", "B", "AB"]
    type = ["+", "-"]
    return random.choice(group) + random.choice(type)


"""
    Complejidad O(1)
"""


def status():
    civilStatus = ["Solter@", "Casad@", "Union Libre", "Viud@", "Separad@", "Divorciad@"]
    return random.choice(civilStatus)


"""
    Complejidad O(1)
"""


def stratum():
    socialStratum = [1, 2, 3, 4, 5, 6]
    return random.choices(socialStratum, weights=(21, 28, 23, 12, 9, 7))[0]


"""
    Complejidad O(1)
"""


def hasVehicle(stratum):
    return random.choice([True, False]) if stratum >= 3 else False


"""
    Complejidad O(1)
"""


def amountVehicle(flag):
    return random.choice([1, 2, 3]) if flag else 0


"""
    Complejidad O(1)
"""


def typeOfVehicle(flag, amount):
    if flag and (amount > 1):
        return random.choice(["carro", "moto", "otro", "varios"])
    elif flag:
        return random.choice(["carro", "moto", "otro"])
    else:
        return "N/A"


"""
    Complejidad O(1)
"""


def id():
    return random.randint(1000000, 1200000000)


"""
    Complejidad O(1)
"""


def typeId():
    types = ["CC", "PaP", "CE"]
    return random.choices(types, weights=(50, 10, 10))[0]


"""
    Complejidad O(1)
"""


def ownership():
    types = ["Propia", "Arriendo", "Familiar", "N/A"]
    return random.choice(types)


"""
    Complejidad O(1)
"""


def livingPlace(type):
    types = ["Apartamento", "Casa"]
    return (
        random.choice(types)
        if type != "N/A"
        else random.choice(
            ["Inquilinato", "Campamento", "Residencia Estudiantil", "Ancianato", "internado", "Orden Religiosa"]
        )
    )


"""
    Complejidad O(1)
"""


def livingPlaceStatus():
    types = ["Contruida", "Contruccion Activa", "Construccion Paralizada", "En Ruina", "Abandono", "Otro"]
    return random.choice(types)


"""
    Complejidad O(1)
"""


def hasDrinkingWater():
    return random.choice([True, False])


"""
    Complejidad O(1)
"""


def sharedHousing():
    return random.choice([True, False])


"""
    Complejidad O(1)
"""


def amountOfRooms():
    room = ["1", "2", "3", "4", "otro"]
    return random.choice(room)


"""
    Complejidad O(1)
"""


def hasEPS():
    return random.choice([True, False])


"""
    Complejidad O(1)
"""


def EPS(flag):
    entities = ["Compensar", "Sanitas", "Comfenalco", "Salud Total", "Famisanar", "EPS Sura", "Salud Vida"]
    return random.choice(entities) if flag else "SISBEN"


"""
    Complejidad O(1)
"""


def religion():
    options = ["Catolica", "N/A", "Cristiana", "Testigo de Jehova", "Musulman", "Maradoniano", "Budista", "Satanista"]
    return random.choice(options)


"""
    Complejidad O(1)
"""


def ethnicity():
    options = [
        "Negro",
        "Mulato",
        "Afrocolombiano",
        "Afroamericano",
        "Indigena",
        "Raizal",
        "Gitano",
        "Palenquero",
        "N/A",
    ]
    return random.choices(options, weights=(20, 20, 20, 20, 7, 7, 7, 7, 50))[0]


"""
    Complejidad O(1)
"""


def age(date):
    year = str(date).split("-")
    age = year[0]
    return 2023 - int(age)


"""
    Complejidad O(1)
"""


def work(age):
    options = ["Empleado", "Desempleado", "Independiente"]
    return random.choice(options) if age < 60 else "Pensionado"


"""
    Complejidad O(1)
"""


def disability():
    return random.choice([True, False])


"""
    Complejidad O(1)
"""


def typeOfDisability(flag):
    return random.choice(["Fisicas", "Sensorial", "Psiquicas"]) if flag else "N/A"


"""
    Complejidad O(1)
"""


def hasPet():
    return random.choice([True, False])


"""
    Complejidad O(1)
"""


def pet(flag):
    pets = ["Perro", "Gato", "Roedor", "Pez", "Pajaros", "Lagarto", "Anfibio", "Otro", "Varios"]
    return random.choice(pets) if flag else "N/A"


"""
    Complejidad O(1)
"""


def amountOfPets(flag):
    return random.randint(1, 5) if flag else 0


"""
    Complejidad O(1)
"""


def militaryCard(gender):
    return random.choice([True, False]) if gender == "M" else "N/A"


"""
    Complejidad O(1)
"""


def countryOfBirth():
    countries = ["España", "Colombia", "Argentina", "Venezuela", "Ecuador", "Peru", "Mexico"]
    return random.choices(countries, weights=(10, 50, 10, 10, 10, 10, 10))[0]


"""
    Complejidad O(1)
"""


def allergies():
    comAllergies = [
        "N/A",
        "Polen",
        "Cosmeticos",
        "Polvo",
        "Alimentos",
        "Gluten",
        "Medicamentos",
        "Detergentes Ropa",
        "Animales",
        "Moho",
        "Fragancias",
    ]
    return random.choice(comAllergies)


"""
    Complejidad O(1)
"""


def height():
    return "1." + str(random.randint(50, 99))


"""
    Complejidad O(1)
"""


def weight():
    return random.randint(45, 90)


"""
    Complejidad O(1)
"""


def englishLevel():
    letter = ["A", "B", "C", "N/A"]
    number = ["1", "2"]
    res = random.choice(letter)
    return res + random.choice(number) if res != "N/A" else res


"""
    Complejidad O(1)
"""


def languges(english):
    amount = ["2", "3", "4", "mas"]
    return random.choice(amount) if english != "N/A" else "1"


"""
    Complejidad O(1)
"""


def lackOfFood():
    return random.choice([True, False])


"""
    Complejidad O(1)
"""


def reasonOfLackFood(flag):
    types = ["Perdidad de cultivo", "Familia muy grande", "Carencia de trabajo", "Carencia Capital", "Otro"]
    return random.choice(types) if flag else "N/A"
