class Employee:
    def __init__(self, first_name, last_name, age, position):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.position = position

    def to_dict(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age,
            "position": self.position,
        }

    def from_dict(data):
        return Employee(
            data["first_name"], data["last_name"], data["age"], data["position"]
        )

    def __str__(self):
        return f"{self.first_name} {self.last_name}, Age: {self.age}, Position: {self.position}"
