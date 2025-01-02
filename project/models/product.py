class Product:
    def __init__(self, name, price, url, description=None):
        """
        Initializes a product instance.
        
        :param name: Name of the product
        :param price: Price of the product
        :param url: URL to the product listing
        :param description: Optional description of the product
        """
        self.name = name
        self.price = price
        self.url = url
        self.description = description

    def __repr__(self):
        return f"Product(name={self.name}, price={self.price}, url={self.url})"
