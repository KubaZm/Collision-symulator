import random
import math
import settings

class AtomBlue:
    atoms_list = []

    def __init__(self):
        self.v_x, self.v_y = random.randint(-settings.max_v, settings.max_v), random.randint(-settings.max_v, settings.max_v)
        while True:
            test = True
            x = random.randint(0 + settings.radius, settings.length - settings.radius)
            y = random.randint(0 + settings.radius, settings.height - settings.radius)
            for i in range(len(AtomBlue.atoms_list)):
                if math.sqrt((AtomBlue.atoms_list[i].x - x) ** 2 + (
                        AtomBlue.atoms_list[i].y - y) ** 2) < 2 * settings.radius:
                    test = False
            if test:
                self.x = x
                self.y = y
                break
        AtomBlue.atoms_list.append(self)