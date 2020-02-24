# CS362 Assignment 4
# Classroom Manager
#Student class
class Student:
    def __init__(self, id, first_name, last_name):
        self.id = id #Fixed Bug setting id to 0 instead of input
        self.first_name = first_name #Fixed Bug where first name was set equal to last name
        self.last_name = last_name #Fixed bug where last name was set equal to first name
        self.assignments = [] #Fixed bug where assignments was misspeled

    def get_full_name(self):
        return str(self.first_name + " " + self.last_name) #Fixed bug where comma was appended instead of space

    def submit_assignment(self, assignment):
        self.assignments.append(assignment)
        #Fixed bug of extra append

    def get_assignments(self):
        return self.assignments #Fixed Bug where function would only return first assignment in list

    def get_assignment(self, name):
        for a in self.assignments:
            if a.name == name: #Fixed bug where input was not used as name
                return a


    def get_average(self):
        sum_grades = 0
        total_assignments = 0
        average = 0 #Added to create average variable
        for a in self.assignments:
            if a.grade != None:
                sum_grades = sum_grades + a.grade #Fixed Bug where sum was subtracted to instead of added
                total_assignments = total_assignments + 1 #Fixed Bug Where 11 was added instead of one
        if total_assignments != 0 and sum_grades != 0: #Fixed bug that would divided values if they were equal to 0
            average = sum_grades / total_assignments #Fixed bug where dividers were reverse
        return average

    def remove_assignment(self, name):
        for a in self.assignments:
            if a.name == name: #Fixed bug where input was not used as name
                self.assignments.remove(a) #Fixed bug where assignment was not delete
                return


#Assignment Class
class Assignment:
    def __init__(self, name, max_score):
        self.name = name
        self.max_score = max_score
        self.grade = None #Fixed bug where grade was set to -1 instead of None

    def assign_grade(self, grade):
        self.grade = grade #Fixed bug where grade was being compared to input instead of being set to it
        if grade > self.max_score: #Fixed Bug where comparison was greater than and equal to rather than just greater than
            self.grade = None #Fixed bug where grade was not attached to the assignment and it was equal to -1 and not None
