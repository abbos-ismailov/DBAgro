class plants():
    def __init__(self, dbc):
        self.dbc = dbc
    
    def get_all(self):
        plants = self.dbc.plants.get().exec()
        return plants
    
    def get_plant(self, id):
        plant = self.dbc.plants.get(id = id).exec()
        if not plant:
            return None
        return plant[0]
    
    def add_plant(self, name, content):
        self.dbc.plants.add(name = name, content = content).exec()
    
    def delete_plant(self, id):
        print(id)
        self.dbc.plants.delete(id = id).exec()
    
    def add(self, **data):
        self.dbc.plants.add(**data).exec()
    
    def is_id_valid(self, id):
        if not id.isdigit():
            return False
        plant = self.dbc.plants.get(id = int(id)).exec()
        if not plant:
            return False
        return True