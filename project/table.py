import pandas as pd
from project import functions as f


def createTable(rows):
    table = pd.DataFrame()
    firstName = []
    lastName = []
    gender = []
    phoneNumber = []
    address = []
    department = []
    municipality = []
    PostalCode = []
    hasChild = []
    children = []
    hasDeadChild = []
    birthday = []
    job = []
    educationLevel = []
    typeOfStudy = []
    email = []
    rh = []
    status = []
    stratum = []
    hasVehicle = []
    amountVehicle = []
    typeOfVehicle = []
    id = []
    typeId = []
    ownership = []
    livingPlace = []
    livingPlaceStatus = []
    hasDrinkingWater = []
    sharedHousing = []
    amountOfRooms = []
    hasEPS = []
    EPS = []
    religion = []
    ethnicity = []
    age = []
    work = []
    disability = []
    typeOfDisability = []
    hasPet = []
    pet = []
    amountOfPets = []
    militaryCard = []
    countryOfBirth = []
    allergies = []
    height = []
    weight = []
    englishLevel = []
    languges = []
    lackOfFood = []
    reasonOfLackFood = []
    addressCityAndPostalCode = []
    for i in range(rows):
        gender += [f.gender()]
        firstName += [f.firstName(gender[i])]
        lastName += [f.lastName()]
        phoneNumber += [f.phoneNumber()]
        id += [f.id()]
        typeId += [f.typeId()]
        addressCityAndPostalCode += [f.addressCityAndPostalCode()]
        address += [f.address(addressCityAndPostalCode[i])]
        department += [f.department(addressCityAndPostalCode[i])]
        municipality += [f.municipality(addressCityAndPostalCode[i])]
        PostalCode += [f.PostalCode(addressCityAndPostalCode[i])]
        hasChild += [f.hasChild()]
        children += [f.children(hasChild[i])]
        hasDeadChild += [f.hasDeadChild()]
        birthday += [f.birthday()]
        age += [f.age(birthday[i])]
        countryOfBirth += [f.countryOfBirth()]
        educationLevel += [f.educationLevel()]
        job += [f.job(educationLevel[i])]
        typeOfStudy += [f.typeOfStudy(educationLevel[i])]
        email += [f.email(firstName[i],lastName[i])]
        rh += [f.rh()]
        status += [f.status()]
        stratum += [f.stratum()]
        hasVehicle += [f.hasVehicle(stratum[i])]
        amountVehicle += [f.amountVehicle(hasVehicle[i])]
        typeOfVehicle += [f.typeOfVehicle(hasVehicle[i], amountVehicle[i])]
        ownership += [f.ownership()]
        livingPlace += [f.livingPlace(ownership[i])]
        livingPlaceStatus += [f.livingPlaceStatus()]
        hasDrinkingWater += [f.hasDrinkingWater()]
        sharedHousing += [f.sharedHousing()]
        amountOfRooms += [f.amountOfRooms()]
        hasEPS += [f.hasEPS()]
        EPS += [f.EPS(hasEPS[i])]
        religion += [f.religion()]
        ethnicity += [f.ethnicity()]
        work += [f.work(age[i])]
        disability += [f.disability()]
        typeOfDisability += [f.typeOfDisability(disability[i])]
        hasPet += [f.hasPet()]
        pet += [f.pet(hasPet[i])]
        amountOfPets += [f.amountOfPets(hasPet[i])]
        militaryCard += [f.militaryCard(gender[i])]
        allergies += [f.allergies()]
        height += [f.height()]
        weight += [f.weight()]
        englishLevel += [f.englishLevel()]
        languges += [f.languges(englishLevel[i])]
        lackOfFood += [f.lackOfFood()]
        reasonOfLackFood += [f.reasonOfLackFood(lackOfFood[i])]
    table["Nombres"] = firstName
    table["Apellidos"] = lastName
    table["id"] = id
    table["Tipo de id"] = typeId
    table["Genero"] = gender
    table["Telfono"] = phoneNumber
    table["Correo"] = email
    table["Tipo de sangre"] = rh
    table["Edad"] = age
    table["Fecha Nacimiento"] = birthday
    table["Pais de Nacimiento"] = countryOfBirth
    table["Direccion de Residencia"] = address
    table["Departamento de Residencia"] = department
    table["Municipio de Residencia"] = municipality
    table["Codigo Postal"] = PostalCode
    table["Altura"] = height
    table["Peso"] = weight
    table["Tien Hijos"] = hasChild
    table["Cantidad de Hijos"] = children
    table["Ha tenido hijos no nacidos"] = hasDeadChild
    table["Nivel de educacion"] = educationLevel
    table["Profesion"] = job
    table["Tipo de estudio"] = typeOfStudy
    table["Nivel de ingles"] = englishLevel
    table["# Idiomas que domina"] = languges
    table["Estado Civil"] = status
    table["Estrato Social"] = stratum
    table["Tiene Vehiculos"] = hasVehicle
    table["Cantidad de Vehiculos"] = amountVehicle
    table["Tipo de Vehiculo"] = typeOfVehicle
    table["Propiedad de vivienda"] = ownership
    table["Tipo de Vivienda"] = livingPlace
    table["Estado de la vivienda"] = livingPlaceStatus
    table["Tiene agua potable"] = hasDrinkingWater
    table["Vivienda compartida"] = sharedHousing
    table["Cantidad de Habitaciones"] = amountOfRooms
    table["Tiene EPS"] = hasEPS
    table["Tipo de EPS"] = EPS
    table["Religion"] = religion
    table["Grupo etnico"] = ethnicity
    table["Estado Laboral"] = work
    table["Tiene discapacidades"] = disability
    table["Tipo de discapacidad"] = typeOfDisability
    table["Tiene Mascotas"] = hasPet
    table["Tipo de mascota"] = pet
    table["Cantidad de mascotas"] = amountOfPets
    table["Tiene libreta militar"] = militaryCard
    table["Tipo de alergias"] = allergies
    table["Ha sufrido de escasez de alimentos"] = lackOfFood
    table["Razon de la escasez de alimentos"] = reasonOfLackFood
    table.to_csv("table.csv")
    table.to_excel("table.xlsx", index=False)