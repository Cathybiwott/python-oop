
class Drum:
    def __init__(self, material, size):
        self.material = material
        self.size = size
    def make_sound(self):
        print(f"{self.__class__.__name__} {self.sound}")
class Djembe(Drum):
    sound = "Wide variety of tones"
djembe = Djembe("hides", "small")
djembe.make_sound()

class TalkingDrum(Drum):
    sound = "Mimics human sound"
talking = TalkingDrum("leather", "medium")
talking.make_sound()


class Bougarabou(Drum):
    sound = "rich deep bass"
bougarabou = Bougarabou("plastic", "big")
bougarabou.make_sound()





   



