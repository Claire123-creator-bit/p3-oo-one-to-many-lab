class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        self.name = name
        
        # Validate pet_type
        if pet_type not in self.PET_TYPES:
            raise Exception(f"Invalid pet type: {pet_type}. Must be one of {self.PET_TYPES}")
        self.pet_type = pet_type
        
        self.owner = owner
        Pet.all.append(self)

class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        """Return a list of pets that belong to this owner."""
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        """Assign this owner to a pet if it is a valid Pet instance."""
        if not isinstance(pet, Pet):
            raise Exception("Must pass a Pet instance")
        pet.owner = self

    def get_sorted_pets(self):
        """Return a sorted list of the owner's pets by name."""
        return sorted(self.pets(), key=lambda pet: pet.name)
