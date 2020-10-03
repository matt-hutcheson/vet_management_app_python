class Patient():
    def __init__(self, name, dob, type, breed, gender, status, check_in_date=None, check_out_date=None, id=None, vet_id=None, client_id=None):
        self.name = name
        self.dob = dob
        self.type = type
        self.breed = breed
        self.gender = gender
        self.status = status
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date
        self.id =id
        self.vet_id = vet_id
        self.client_id = client_id