class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")

class Instructor(User):
    def __init__(self, name, email, subject):
        super().__init__(name, email)
        self.subject = subject

    def upload_content(self):
        print(f"Content uploaded for {self.subject}")

    def display_info(self):
        super().display_info()
        print(f"Subject Expertise: {self.subject}")

class CourseCreator(Instructor):
    def __init__(self, name, email, subject, course_name):
        super().__init__(name, email, subject)
        self.course_name = course_name

    def create_course(self):
        print(f"Course '{self.course_name}' created with modules.")

    def display_info(self):
        super().display_info()
        print(f"Course: {self.course_name}")

if __name__ == "__main__":
    creator = CourseCreator("Dr. Smith", "smith@example.com", "AI", "AI Foundations")
    creator.display_info()
    creator.upload_content()
    creator.create_course()
