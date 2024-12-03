class Person:
    def __init__(self, name, age, contact_info):
        self.name = name
        self.age = age
        self.contact_info = contact_info

    def set_details(self, name, age, contact_info):
        self.name = name
        self.age = age
        self.contact_info = contact_info

    def get_details(self):
        return f"Name: {self.name}\nAge: {self.age}\nContact Info: {self.contact_info}"


class Member(Person):
    def __init__(self, name, age, contact_info, member_id, sport):
        super().__init__(name, age, contact_info)
        self.member_id = member_id
        self.sport = sport
        self.performance_scores = []

    def set_member_details(self, member_id, sport):
        self.member_id = member_id
        self.sport = sport

    def add_performance_score(self, score):
        if isinstance(score, (int, float)) and score >= 0:
            self.performance_scores.append(score)

    def calculate_average_score(self):
        return round(sum(self.performance_scores) / len(self.performance_scores), 2) if self.performance_scores else 0

    def get_member_summary(self):
        return (
            f"{self.get_details()}\n"
            f"Member ID: {self.member_id}\nSport: {self.sport}\n"
            f"Average Performance Score: {self.calculate_average_score()}"
        )


class Coach(Person):
    def __init__(self, name, age, contact_info, coach_id, specialty, salary):
        super().__init__(name, age, contact_info)
        self.coach_id = coach_id
        self.specialty = specialty
        self.salary = salary
        self.students = []
        self.mentorship_group = []

    def set_coach_details(self, coach_id, specialty, salary):
        self.coach_id = coach_id
        self.specialty = specialty
        self.salary = salary

    def assign_student(self, member):
        if isinstance(member, Member):
            self.students.append(member)
            return f"Coach {self.name} is now coaching {member.name} in {member.sport}"

    def list_students(self):
        if self.students:
            for student in self.students:
                print(f"Student: {student.name}")
        else:
            print("No students assigned.")

    def increase_salary(self, percentage):
        if percentage > 0:
            self.salary += self.salary * percentage / 100

    def mentor_coach(self, coach):
        if isinstance(coach, Coach):
            self.mentorship_group.append(coach)
            print(f"Coach {self.name} is now mentoring Coach {coach.name} in {self.specialty}")

    def list_mentorship_group(self):
        if self.mentorship_group:
            for coach in self.mentorship_group:
                print(f"Coach: {coach.name} || Specialty: {coach.specialty}")
        else:
            print("No coaches in the mentorship group.")


class Staff(Person):
    def __init__(self, name, age, contact_info, staff_id, position, years_of_service):
        super().__init__(name, age, contact_info)
        self.staff_id = staff_id
        self.position = position
        self.years_of_service = years_of_service

    def set_staff_details(self, staff_id, position, years_of_service):
        self.staff_id = staff_id
        self.position = position
        self.years_of_service = years_of_service

    def increment_years_of_service(self):
        self.years_of_service += 1

    def assist_member(self, member):
        print(f"Staff {self.name} assisted {member.name} in resolving an issue.")

    def get_staff_summary(self):
        return (
            f"{self.get_details()}\n"
            f"Staff ID: {self.staff_id}\n"
            f"Position: {self.position}\n"
            f"Years of Service: {self.years_of_service}"
        )