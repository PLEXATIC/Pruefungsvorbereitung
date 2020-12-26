class Boye:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return (self.name)
    
boy = Boye("kim")
print(boy)

Boye.be_fucked = lambda s : print(s.name + " is fucked")
boy.be_fucked()