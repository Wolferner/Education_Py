
class Buildings(object):
    def __init__(self, stages):
        self.stages = stages

    def house_stages(self):
        print(self.stages)


class Hospital(Buildings):
    def __init__(self, free_places, stages):
        super().__init__(stages)
        self.free_places = free_places

    def free_places_in(self):
        print(self.free_places)


class Restauran(Buildings):
    def __init__(self, tables, stages):
        super().__init__(stages)
        self.tables = tables

    def free_tables(self):
        print(self.tables)


if __name__ == '__main__':

    hos_1 = Hospital(200, 5)
    res_1 = Restauran(100, 2)

    hos_1.free_places_in()
    hos_1.house_stages()
    res_1.free_tables()
    res_1.house_stages()
