class Flower:

    def __init__(self, name, freshness, color, length, lifetime, price):
        self.name = name
        self. freshness = freshness
        self.color = color
        self.length = length
        self.lifetime = lifetime
        self.price = price

    def __str__(self):
        return (f'{self.color} {self.name}, {self.length} cm, freshness: {self.freshness}, '
                f'lifetime: {self.lifetime} days, price: {self.price} rub')

    def __repr__(self):
        return self.__str__()


class Tulip(Flower):

    def __init__(self, freshness, color, length):
        super().__init__('tulip', freshness, color, length, 3, 70)


class Peony(Flower):

    def __init__(self, freshness, color, length):
        super().__init__('peony', freshness, color, length, 4, 150)


class Carnation(Flower):

    def __init__(self, freshness, color, length):
        super().__init__('carnation', freshness, color, length, 15, 90)


class Bouquet:

    def __init__(self, flowers):
        self.flowers = flowers

    def total_price(self):
        return sum(flower.price for flower in self.flowers)

    def total_lifetime(self):
        return round(sum(flower.lifetime for flower in self.flowers) / len(self.flowers), 2)

    def show(self):
        for flower in self.flowers:
            print(flower)
        print('Total lifetime:', self.total_lifetime(), 'days')
        print('Total price:', self.total_price(), 'rub')

    def sort_by(self, param):
        self.flowers.sort(key=lambda x: getattr(x, param))
        for flower in self.flowers:
            print(flower)

    def search(self, param, value):
        for flower in self.flowers:
            if getattr(flower, param, None) == value:
                print(flower)


tulip1 = Tulip(10, 'white', 25)
tulip2 = Tulip(7, 'pink', 25)
peony1 = Peony(8, 'white', 30)
peony2 = Peony(9, 'pink', 30)
carnation1 = Carnation(5, 'pink', 30)
carnation2 = Carnation(7, 'white', 35)

bouquet = Bouquet([tulip1, tulip2, peony1, peony2, carnation1, carnation2])

bouquet.show()
bouquet.sort_by('freshness')
bouquet.sort_by('color')
bouquet.sort_by('length')
bouquet.sort_by('price')
bouquet.search('length', 25)
bouquet.search('color', 'white')
bouquet.search('price', 70)
bouquet.search('freshness', 8)
