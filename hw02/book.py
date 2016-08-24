class Book:
    def __init__(self, name, author, publisher, price):
        self.name = name
        self.author = author
        self.publisher = publisher
        self.price = price

    def get_name(self):
        return self.name

    def get_author(self):
        return self.author

    def get_publisher(self):
        return self.publisher

    def get_price(self):
        return self.price

    def show(self):
        print "Name: {}".format(self.name)
        print "Author: {}".format(self.author)
        print "Publisher: {}".format(self.publisher)
        print "Pirce: {}".format(self.price)



