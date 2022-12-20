class Pet:

    def __init__(self, name, date_of_birth, type_of_animal, owner, id = None):
        self.name = name
        self.date_of_birth = date_of_birth
        self.type_of_animal = type_of_animal
        self.owner = owner 
        self.id = id
        self.vet = []
        self.medical_history = []

    def add_vet_to_pet(self, vet):
        self.vet.append(vet)

    def add_notes_to_history(self, note):
        self.medical_history.append(note)