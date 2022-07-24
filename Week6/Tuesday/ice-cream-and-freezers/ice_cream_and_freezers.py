class IceCream:

    def __init__(self, freeze_time, name):
        self.name = name
        self.start_time = 0
        self.status = None
        self.freeze_time = freeze_time

    def get_status(self, time):
        if time >= 0 and time < self.freeze_time//5:
            self.status = 'watery'
        elif time >= self.freeze_time//5 and time < self.freeze_time:
            self.status = 'almost_ready'
        elif time == self.freeze_time:
            self.status = 'ready'
        else:
            self.status = 'freezer_burned'
        return self.status

class Freezer:

    def __init__(self) -> None:
        self.inventory = []
        self.time = 0

    def add_inventory(self, ice_cream_batch):
        ice_cream_batch.start_time = self.time
        self.inventory.append(ice_cream_batch)
        return self.inventory

    def remove_inventory(self, ice_cream_batch):
        self.inventory.remove(ice_cream_batch)
        return self.inventory
        
    def time_warp(self, time_jump):
        self.time += time_jump
        return self.time

    def check_inventory(self):
        status = []
        for batch in self.inventory:
            status.append([batch.name, batch.get_status(self.time)])
        return status

    def check_batch(self, ice_cream_batch):
        batch_pos = self.inventory.index(ice_cream_batch)
        status = self.inventory[batch_pos].get_status(self.time)
        return status
        



