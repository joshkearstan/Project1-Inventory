"""CSCI 204 Project phase 1
Author: Joshua Kearstan
Project 1
Inventory code
"""
# Phase 1: Inventory Class Implementation

# --- Item Classes ---

class Item:
    """Base class for all items."""

    def __init__(self, name, price, quantity):
        """Initialize common attributes."""
        self.name = name
        self.price = float(price)  # Convert price to float
        self.quantity = int(quantity)  # Convert quantity to integer

    def __str__(self):
        """Return a formatted string representation."""
        return f"{self.name} - Price: ${self.price:.2f}, Quantity: {self.quantity}"

class Book(Item):
    """Class for book items."""

    def __init__(self, name, price, quantity, author, publisher, isbn, date):
        """Initialize book-specific attributes."""
        super().__init__(name, price, quantity)
        self.author = author
        self.publisher = publisher
        self.isbn = isbn
        self.date = date

    def __str__(self):
        """Return a formatted string representation."""
        return f"{super().__str__()}, Author: {self.author}, Publisher: {self.publisher}, ISBN: {self.isbn}, Date: {self.date}"

class CDVinyl(Item):
    """Class for CD and Vinyl items."""

    def __init__(self, name, price, quantity, artist, label, asin, date):
        """Initialize CD/Vinyl-specific attributes."""
        super().__init__(name, price, quantity)
        self.artist = artist
        self.label = label
        self.asin = asin
        self.date = date

    def __str__(self):
        """Return a formatted string representation."""
        return f"{super().__str__()}, Artist: {self.artist}, Label: {self.label}, ASIN: {self.asin}, Date: {self.date}"

class Collectible(Item):
    """Class for collectible items."""

    def __init__(self, name, price, quantity, owner, date):
        """Initialize collectible-specific attributes."""
        super().__init__(name, price, quantity)
        self.owner = owner
        self.date = date

    def __str__(self):
        """Return a formatted string representation."""
        return f"{super().__str__()}, Owner: {self.owner}, Date: {self.date}"

class Electronic(Item):
    """Base class for electronic items."""

    def __init__(self, name, price, quantity, manufacturer, date):
        """Initialize electronic-specific attributes."""
        super().__init__(name, price, quantity)
        self.manufacturer = manufacturer
        self.date = date

    def __str__(self):
        """Return a formatted string representation."""
        return f"{super().__str__()}, Manufacturer: {self.manufacturer}, Date: {self.date}"

class Electronics(Electronic):
    """Class for electronics items."""
    pass  # No additional attributes needed

class Fashion(Electronic):
    """Class for fashion items."""
    pass  # No additional attributes needed

class HomeGarden(Electronic):
    """Class for home and garden items."""
    pass  # No additional attributes needed

# --- Inventory Class ---

import csv

class Inventory:
    """Class to manage the inventory."""

    def __init__(self):
        """Initialize the inventory."""
        self.items = []
        self.read_data()

    def read_data(self):
        """Read data from CSV files and create item objects."""
        files = {
            "book.csv": Book,
            "cd-vinyl.csv": CDVinyl,
            "collectible.csv": Collectible,
            "electronics.csv": Electronics,
            "fashion.csv": Fashion,
            "home_garden.csv": HomeGarden,
        }

        for filename, item_class in files.items():
            self._read_csv_data(filename, item_class)

    def _read_csv_data(self, filename, item_class):
        """Read data from a CSV file and create item objects."""
        try:
            with open(filename, 'r') as file:
                reader = csv.reader(file)
                header = next(reader)  # Get the header row

                for row in reader:
                    data = dict(zip(header, row))

                    # Handle missing/invalid data ("########")
                    for key, value in data.items():
                        if value == "########":
                            data[key] = None

                    # Create item object based on item_class
                    try:
                        if item_class == Book:
                            item = item_class(data["Title"], data["Price"], data["Quantity"], data["Author"], data["Publisher"], data["ISBN"], data["Date"])
                        elif item_class == CDVinyl:
                            item = item_class(data["Title"], data["Price"], data["Quantity"], data["Artist"], data["Label"], data["ASIN"], data["Date"])
                        elif item_class == Collectible:
                            item = item_class(data["Name"], data["Price"], data["Quantity"], data["Owner"], data["Date"])
                        elif item_class == Electronics:
                            item = item_class(data["Name"], data["Price"], data["Quantity"], data["Manufacturer"], data["Date"])
                        elif item_class == Fashion:
                            item = item_class(data["Name"], data["Price"], data["Quantity"], data["Manufacturer"], data["Date"])
                        elif item_class == HomeGarden:
                            item = item_class(data["Name"], data["Price"], data["Quantity"], data["Manufacturer"], data["Date"])
                        self.items.append(item)
                    except KeyError as e:
                        print(f"Error creating item from {filename}: Missing key {e}")

        except FileNotFoundError:
            print(f"File not found: {filename}")
        except Exception as e:
            print(f"Error reading {filename}: {e}")

    def check_type(self, item):
        """Determine the type of an item."""
        return type(item).__name__

    def compute_inventory(self):
        """Compute the total value of the inventory."""
        total_value = 0
        for item in self.items:
            total_value += item.price * item.quantity
        return total_value

    def print_inventory(self):
        """Print the inventory."""
        for item in self.items:
            print(item)

    def print_category(self, category):
        """Print items of a specific category."""
        for item in self.items:
            if isinstance(item, eval(category)):  # Use eval() to get the class from string
                print(item)

    def search_item(self, pattern):
        """Search for items matching a pattern."""
        for item in self.items:
            if pattern.lower() in item.name.lower():
                print(item)

