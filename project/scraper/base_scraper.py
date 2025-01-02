from abc import ABC , abstractmethod

class Base(ABC):
    
    @abstractmethod
    def fetch_data(self,product_name):
        # to fetch product data same structure for all scrapers
        pass