from typing import Optional, Union


class Building:

    def __init__(self, height: Union[int, float], width: Union[int, float], lenght):
        
        self.height = height
        self.width = width
        self.lenght = lenght
        self.volume = int(self.lenght) * int(self.height) * int(self.width)

    def __repr__(self):
        return f'Building({self.height, self.width, self.lenght})'

    def __gt__(self, other):
        if other is None or not isinstance(other, Building):
            return False
        return other.volume > self.volume

if __name__ == '__main__' :
    a = Building('10','20',30)  #podskazka gde oshibka
    b = Building(20,30,40)
    print(a,b)
    print(a>b)