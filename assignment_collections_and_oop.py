# Task 1
class Car:
    brand: str
    model_name: str
    construction_year: int

    def __init__(self, brand, model, year) -> None:
        self.brand = brand
        self.model_name = model
        self.construction_year = year

    # Task 3
    def __repr__(self) -> str:
        return f"Car(brand={self.brand}, model={self.model_name}, year={self.construction_year})"


# Task 2
car1 = Car("porsche", "cayenne", 2019)

# Using the repr function to print out the attributes
print(car1)
