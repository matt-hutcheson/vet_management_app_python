class Treatment():
    def __init__(self, notes, date, patient=None, vet=None, id=None):
        self.notes = notes
        self.patient = patient
        self.vet = vet
        self.id = id
        self.date = date