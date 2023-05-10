class Musician:
    def __init__(self, name):
        self.name = name


class Guitarist(Musician):
    def __str__(self):
        return f"My name is {self.name} and I play guitar"

    def __repr__(self):
        return f"Guitarist instance. Name = {self.name}"

    def get_instrument(self):
        return "guitar"

    def play_solo(self):
        return "face melting guitar solo"


class Bassist(Musician):
    def __str__(self):
        return f"My name is {self.name} and I play bass"

    def __repr__(self):
        return f"Bassist instance. Name = {self.name}"

    def get_instrument(self):
        return "bass"

    def play_solo(self):
        return "bom bom buh bom"


class Drummer(Musician):
    def __str__(self):
        return f"My name is {self.name} and I play drums"

    def __repr__(self):
        return f"Drummer instance. Name = {self.name}"

    def get_instrument(self):
        return "drums"

    def play_solo(self):
        return "rattle boom crash"


class Band:
    instances = []

    def __init__(self, name, members):
        self.name = name
        self.members = members
        self.__class__.instances.append(self)

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Band instance. Name = {self.name}"

    def play_solos(self):
        return [member.play_solo() for member in self.members]

    @classmethod
    def to_list(cls):
        return cls.instances

    def add_member(self, member):
        self.members.append(member)


if __name__ == "__main__":
    joan = Guitarist("Joan Jett")
    sheila = Drummer("Sheila E.")
    meshell = Bassist("Meshell Ndegeocello")

    print(str(joan))
    print(repr(joan))
    print(str(sheila))
    print(repr(sheila))
    print(str(meshell))
    print(repr(meshell))

    print(joan.get_instrument())
    print(sheila.get_instrument())
    print(meshell.get_instrument())

    print(joan.play_solo())
    print(sheila.play_solo())
    print(meshell.play_solo())

    nirvana = Band("Nirvana", [])
    
    jimi = Guitarist("Jimi Hendrix")
    flea = Bassist("Flea")
    ginger = Drummer("Ginger Baker")
   
    nirvana.add_member(jimi)
    nirvana.add_member(flea)
    nirvana.add_member(ginger)

    print(nirvana.name)  
    print(nirvana.members)  

    
