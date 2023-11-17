grade_to_points_OL = {
    "A": 3,
    "B": 2,
    "C": 1,
}
grade_to_points_AL = {"A": 5, "B": 4, "C": 3, "D": 2, "E": 1}


def get_grade_point(grade, level="AL"):
    if level == "AL":
        return grade_to_points_AL[grade]
    else:
        return grade_to_points_OL[grade]


class Record:
    def __init__(self, record, level="AL"):
        self.name, self.grades = sanitize_record(record)
        self.points = calculate_points(self.grades)
        self.gpa = 5 * self.points / get_grade_point('A', level) / len(self.grades) #Flawed!!! Assumes students passed all subjects they took.
    
    def __repr__(self):
        # return f"{self.name}: {self.points} points -> {self.grades}"
        return f"GPA: {self.gpa:.2f} | {self.points} points -> {self.grades}"
    
    def __str__(self) -> str:
        return self.__repr__()

class GradeDist:
    def __init__(self) -> None:
        self.names = []
        self.count = 0
    
    def add(self, name):
        self.names.append(name)
        self.count += 1
    
    def __str__(self) -> str:
        return f"{self.count}"  
    
    def __repr__(self) -> str:
        return f"{self.count}"

def calculate_points(grades, level = "AL"):
    total_points = 0
    for grade in grades.values():
        total_points += get_grade_point(grade, level)
    return total_points

def sanitize_record(record):
    name, grades_str = record
    grades = {}
    for t_grade in grades_str.split(','):
        if "-" not in t_grade:
            continue
        subject, grade = t_grade.split('-')
        grade = "".join(grade.split("\n"))
        subject = "".join(subject.split("\n"))
        grades[subject.strip()] = grade.strip()

    return name.strip(), grades


def return_first_n_chars_or_fill_with_spaces(text):
    n = 30
    return text[:n] + " " * (n - len(text[:n]))