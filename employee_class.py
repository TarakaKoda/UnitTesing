import requests


class Employee:
    raise_amount = 1.05
    company_name = "youwecan"

    def __init__(self, first_name: str, last_name: str, salary: int | float):
        assert salary > 0, "Salary must be greater than zero  "
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def email(self):
        email = f"{self.first_name.lower()}{self.last_name.lower()}@{self.company_name}.com"
        return email

    def apply_raise(self):
        self.salary = int(self.salary * self.raise_amount)
        return self.salary

    def monthly_schedule(self, month):
        response = requests.get(f"http://{self.company_name}.com/{self.last_name}/{month}")
        if response.ok:
            return response.text
        else:
            return "Bad response"






