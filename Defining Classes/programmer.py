class Programmer:
    def __init__(self, name: str, language: str, skills: int):
        self.name = name
        self.language = language
        self.skills = skills

    def watch_course(self, course_name: str, language: str, skills_earned: int):
        if language == self.language:
            self.skills += skills_earned
            return f"{self.name} watched {course_name}"
        else:
            return f"{self.name} does not know {language}"

    def change_language(self, new_language, skills_required):
        if self.skills >= skills_required and new_language is not self.language:
            old_language = self.language
            self.language = new_language
            return f"{self.name} switched from {old_language} to {self.language}"
        elif self.skills >= skills_required and new_language == self.language:
            return f"{self.name} already knows {new_language}"
        else:
            return f"{self.name} needs {skills_required - self.skills} more skills"


# UNCOMMENT FOR TESTING PURPOSES
# programmer = Programmer("John", "Java", 50)
# print(programmer.watch_course("Python Masterclass", "Python", 84))
# print(programmer.change_language("Java", 30))
# print(programmer.change_language("Python", 100))
# print(programmer.watch_course("Java: zero to hero", "Java", 50))
# print(programmer.change_language("Python", 100))
# print(programmer.watch_course("Python Masterclass", "Python", 84))