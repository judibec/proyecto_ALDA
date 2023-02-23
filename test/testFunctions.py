import datetime
import unittest
import project.functions as f

amountOfTest = 50
rhGroup = ["A+", "A-", "O+", "O-", "B+", "B-", "AB+", "AB-"]
typeId = ["CC", "PaP", "CE"]
typeOfliving = ["Propia", "Arriendo", "Familiar", "N/A"]
typeOfLivingPlace = ["Inquilinato", "Campamento", "Residencia Estudiantil", "Ancianato", "internado", "Orden Religiosa",
                     "Apartamento", "Casa"]
typePlaceStatus = ["Contruida", "Contruccion Activa", "Construccion Paralizada", "En Ruina", "Abandono", "Otro"]
eps = ["Compensar", "Sanitas", "Comfenalco", "Salud Total", "Famisanar", "EPS Sura", "Salud Vida"]
typeReligion = ["Catolica", "N/A", "Cristiana", "Testigo de Jehova", "Musulman", "Maradoniano", "Budista", "Satanista"]
ethnicity = ["Negro", "Mulato", "Afrocolombiano", "Afroamericano", "Indigena", "Raizal", "Gitano", "Palenquero", "N/A"]
typeOfPet = ["Perro", "Gato", "Roedor", "Pez", "Pajaros", "Lagarto", "Anfibio", "Otro", "Varios"]
birthCountries = ["España", "Colombia", "Argentina", "Venezuela", "Ecuador", "Peru", "Mexico"]
comAllergies = ["N/A", "Polen", "Cosmeticos", "Polvo", "Alimentos", "Gluten", "Medicamentos", "Detergentes Ropa",
                "Animales", "Moho", "Fragancias"]
englishLevel = ["A1", "A2", "B1", "B2", "C1", "C2", "N/A"]
reasonLackFood = ["N/A", "Perdidad de cultivo", "Familia muy grande", "Carencia de trabajo", "Carencia Capital", "Otro"]


class testFunctions(unittest.TestCase):
    def test_get_genders(self):
        res = set()
        for i in range(amountOfTest):
            res.add(f.gender())
        self.assertEqual(2, len(res))

    def test_get_phone_numbers(self):
        for i in range(amountOfTest):
            if len(f.phoneNumber()) != 10:
                self.fail()

    def test_get_postal_code(self):
        res = []
        flag = True
        for i in range(amountOfTest):
            if len(f.PostalCode(f.addressCityAndPostalCode())) != 6:
                self.fail()

    def test_get_has_child(self):
        res = set()
        for i in range(amountOfTest):
            res.add(f.hasChild())
        self.assertEqual(2, len(res))

    def test_get_children(self):
        for i in range(amountOfTest):
            if f.children(f.hasChild()) > 5:
                self.fail()

    def test_get_birthday(self):
        for i in range(amountOfTest):
            if datetime.date(2023, 12, 31) < f.birthday() < datetime.date(1942, 12, 31):
                self.fail()

    def test_get_job(self):
        for i in range(amountOfTest):
            flag = f.educationLevel()
            if flag != "N/A":
                if f.job(flag) == "N/A":
                    self.fail()
            else:
                if f.job(flag) != "N/A":
                    self.fail()

    def test_get_education_level(self):
        res = set()
        for i in range(amountOfTest):
            res.add(f.educationLevel())
        if len(res) > 8:
            self.fail()

    def test_get_type_study(self):
        for i in range(amountOfTest):
            flag = f.educationLevel()
            if flag != "N/A":
                if f.typeOfStudy(flag) == "N/A":
                    self.fail()
            else:
                if f.typeOfStudy(flag) != "N/A":
                    self.fail()

    def test_get_email(self):
        for i in range(amountOfTest):
            mail = f.email(f.firstName(f.gender()), f.lastName())
            domain = mail.split("@")
            if "@" not in mail:
                self.fail()
            elif ".com" not in domain[1]:
                self.fail()

    def test_get_rh(self):
        for i in range(amountOfTest):
            if f.rh() not in rhGroup:
                self.fail()

    def test_get_status(self):
        res = set()
        for i in range(amountOfTest):
            res.add(f.status())
        if len(res) > 6:
            self.fail()

    def test_get_stratum(self):
        for i in range(amountOfTest):
            if 0 > f.stratum() > 6:
                self.fail()

    def test_get_has_vehicle(self):
        res = set()
        for i in range(amountOfTest):
            stratum = f.stratum()
            if stratum < 3:
                if f.hasVehicle(stratum):
                    self.fail()
            else:
                res.add(f.hasVehicle(stratum))
        self.assertEqual(2, len(res))

    def test_get_amount_vehicle(self):
        for i in range(amountOfTest):
            if f.amountVehicle(f.hasVehicle(f.stratum())) > 3:
                self.fail()

    def test_get_type_vehicle_more_than_1(self):
        res = set()
        for i in range(amountOfTest):
            flag = f.hasVehicle(f.stratum())
            amount = f.amountVehicle(flag)
            if flag and amount > 1:
                res.add(f.typeOfVehicle(flag, amount))
        if len(res) > 4:
            self.fail()

    def test_get_type_one_vehicle(self):
        res = set()
        for i in range(amountOfTest):
            flag = f.hasVehicle(f.stratum())
            amount = f.amountVehicle(flag)
            if flag and amount == 1:
                res.add(f.typeOfVehicle(flag, amount))
        if len(res) > 3:
            self.fail()

    def test_get_type_vehicle_less_than_1(self):
        for i in range(amountOfTest):
            flag = f.hasVehicle(f.stratum())
            amount = f.amountVehicle(flag)
            if not flag:
                if f.typeOfVehicle(flag, amount) != "N/A":
                    self.fail()

    def test_get_id(self):
        for i in range(amountOfTest):
            if not (7 <= len(str(f.id())) <= 10):
                self.fail()

    def test_get_type_id(self):
        for i in range(amountOfTest):
            if f.typeId() not in typeId:
                self.fail()

    def test_get_ownership(self):
        for i in range(amountOfTest):
            if f.ownership() not in typeOfliving:
                self.fail()

    def test_get_living_place(self):
        for i in range(amountOfTest):
            if f.livingPlace(f.ownership()) not in typeOfLivingPlace:
                self.fail()

    def test_get_living_place_status(self):
        for i in range(amountOfTest):
            if f.livingPlaceStatus() not in typePlaceStatus:
                self.fail()

    def test_get_amount_of_room(self):
        res = set()
        for i in range(amountOfTest):
            res.add(f.amountOfRooms())
        self.assertEqual(5, len(res))

    def test_get_type_eps(self):
        for i in range(amountOfTest):
            if f.EPS(True) not in eps:
                self.fail()

    def test_get_not_eps(self):
        for i in range(amountOfTest):
            if f.EPS(False) != "SISBEN":
                self.fail()

    def test_get_religion(self):
        for i in range(amountOfTest):
            if f.religion() not in typeReligion:
                self.fail()

    def test_get_ethnicity(self):
        for i in range(amountOfTest):
            if f.ethnicity() not in ethnicity:
                self.fail()

    def test_get_age(self):
        for i in range(amountOfTest):
            if not (17 <= f.age(f.birthday()) <= 81):
                self.fail()

    def test_get_work_not_pensioner(self):
        res = set()
        for i in range(amountOfTest):
            age = f.age(f.birthday())
            if age < 60:
                res.add(f.work(age))
        self.assertEqual(3, len(res))

    def test_get_work_pensioner(self):
        for i in range(amountOfTest):
            age = f.age(f.birthday())
            if age >= 60:
                if f.work(age) != "Pensionado":
                    self.fail()

    def test_get_type_has_disability(self):
        res = set()
        for i in range(amountOfTest):
            res.add(f.typeOfDisability(True))
        self.assertEqual(3, len(res))

    def test_get_type_not_disability(self):
        for i in range(amountOfTest):
            if f.typeOfDisability(False) != "N/A":
                self.fail()

    def test_get_type_pet(self):
        for i in range(amountOfTest):
            if f.pet(True) not in typeOfPet:
                self.fail()

    def test_get_not_pet(self):
        for i in range(amountOfTest):
            if f.pet(False) != "N/A":
                self.fail()

    def test_get_amount_pets(self):
        for i in range(amountOfTest):
            if not (0 <= f.amountOfPets(f.hasPet()) <= 5):
                self.fail()

    def test_get_military_card_for_men(self):
        res = set()
        for i in range(amountOfTest):
            res.add(f.militaryCard("M"))
        self.assertEqual(2, len(res))

    def test_get_military_card_for_women(self):
        for i in range(amountOfTest):
            if f.militaryCard("F") != "N/A":
                self.fail()

    def test_get_countries_birth(self):
        for i in range(amountOfTest):
            if f.countryOfBirth() not in birthCountries:
                self.fail()

    def test_get_allergies(self):
        for i in range(amountOfTest):
            if f.allergies() not in comAllergies:
                self.fail()

    def test_get_height(self):
        for i in range(amountOfTest):
            if not (1.50 <= float(f.height()) <= 1.99):
                self.fail()

    def test_get_weight(self):
        for i in range(amountOfTest):
            if not (45 <= int(f.weight()) <= 90):
                self.fail()

    def test_get_english_level(self):
        for i in range(amountOfTest):
            if f.englishLevel() not in englishLevel:
                self.fail()

    def test_get_languages(self):
        res = set()
        for i in range(amountOfTest):
            res.add(f.languges(f.englishLevel()))
        self.assertEqual(5, len(res))

    def test_get_reason_of_lack_food(self):
        for i in range(amountOfTest):
            if f.reasonOfLackFood(f.lackOfFood()) not in reasonLackFood:
                self.fail()

    def test_get_has_dead_child(self):
        res = set()
        for i in range(amountOfTest):
            res.add(f.hasDeadChild())
        self.assertEqual(2, len(res))

    def test_get_has_drinking_water(self):
        res = set()
        for i in range(amountOfTest):
            res.add(f.hasDrinkingWater())
        self.assertEqual(2, len(res))

    def test_get_has_eps(self):
        res = set()
        for i in range(amountOfTest):
            res.add(f.hasEPS())
        self.assertEqual(2, len(res))

    def test_get_shared_house(self):
        res = set()
        for i in range(amountOfTest):
            res.add(f.sharedHousing())
        self.assertEqual(2, len(res))

    def test_get_disability(self):
        res = set()
        for i in range(amountOfTest):
            res.add(f.disability())
        self.assertEqual(2, len(res))


if __name__ == '__main__':
    unittest.main()
