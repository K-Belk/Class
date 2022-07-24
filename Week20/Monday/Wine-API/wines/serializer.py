from builtins import object

class WineSerializer(object):
    def __init__(self, body) -> None:
        self.body = body

    def all_wines(self):
        output = {'wines': []}

        for wine in self.body:
            wine_details = {
                'id': wine.id,
                'wine_name' : wine.wine_name,
                'price' : wine.price,
                'varietal' : wine.varietal,
                'description' : wine.description
            }
            output['wines'].append(wine_details)
        return output

    def wine_detail(self):
        wine_details = {
            'id' : self.body.id,
            'wine_name' : self.body.wine_name,
            'price' : self.body.price,
            'varietal' : self.body.varietal,
            'description' : self.body.description
        }
        return wine_details