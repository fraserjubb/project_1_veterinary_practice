class Pet:

    def __init__(self, name, date_of_birth, type_of_animal, id = None):
        self.name = name
        self.date_of_birth = date_of_birth
        self.type_of_animal = type_of_animal
        self.id = id
        self.medical_history = []