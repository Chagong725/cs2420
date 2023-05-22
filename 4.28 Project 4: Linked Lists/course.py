class Course:
    def __init__(self, number=0, name="", credit_hour=0.0, grade=0.0):
        if not isinstance(number, int) or not isinstance(name, str) or not isinstance(credit_hour, (int, float)) or not isinstance(grade, (int, float)):
            raise ValueError("Invalid parameter type.")
        if grade < 0.0 or grade > 4.0:
            raise ValueError("Invalid grade value.")
        if number < 0:
            raise ValueError("Invalid course number.")
        if credit_hour < 0.0:
            raise ValueError("Invalid credit hour value.")

        self._number = number
        self._name = name
        self._credit_hour = credit_hour
        self._grade = grade


    def number(self):
        return self._number

    def name(self):
        return self._name

    def credit_hr(self):
        return self._credit_hour

    def grade(self):
        return self._grade

    def __eq__(self, other):
        cnumb = other
        if isinstance(other, Course):
            cnumb = other.number()
        return self.number() == cnumb

    def __lt__(self, other):
        if isinstance(other, Course):
            return self._number < other._number
        return False

    def __le__(self, other):
        if isinstance(other, Course):
            return self._number <= other._number
        return False

    def __str__(self):
        return f"{self._name} {self._number} Grade: {self._grade} Credit Hours: {self._credit_hour}"
