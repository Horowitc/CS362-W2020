from unittest import TestCase
import classroom_manager
class TestStudent(TestCase):
    def testProp(self):
        id = 2
        first_name = "Jeff"
        last_name = "Maname"
        assignments = []
        student = classroom_manager.Student(id, first_name, last_name)
        self.assertEqual(id, student.id)
        self.assertEqual(first_name, student.first_name)
        self.assertEqual(last_name, student.last_name)
        self.assertEqual(assignments, student.assignments)

    def test_get_full_name(self):
        student = classroom_manager.Student(5, "Jeff", "Maname")
        fullname = classroom_manager.Student.get_full_name(student)
        self.assertEqual("Jeff Maname", fullname)

    def test_get_assignments(self):
        assigment = classroom_manager.Assignment("Extra Credit", 100)
        assignments = [assigment, assigment, assigment]
        student = classroom_manager.Student(5, "Jeff", "Maname")
        student.assignments = [assigment, assigment, assigment]
        geta = classroom_manager.Student.get_assignments(student)
        self.assertEqual(assignments, geta)


    def test_get_assignment(self):
        assigment = classroom_manager.Assignment("Extra Credit", 100)
        assigment2 = classroom_manager.Assignment("Something Else", 80)
        assigment3 = classroom_manager.Assignment("Another One", 60)
        student = classroom_manager.Student(5, "Jeff", "Maname")
        student.assignments = [assigment, assigment2, assigment3]
        getname = classroom_manager.Student.get_assignment(student, "Extra Credit")
        self.assertEqual(assigment, getname)
        student.assignments = [assigment2]
        getname = classroom_manager.Student.get_assignment(student, "uishaiuasgd")
        self.assertEqual(None, getname)


    def test_get_average(self):
        assigment = classroom_manager.Assignment("Extra Credit", 100)
        assigment2 = classroom_manager.Assignment("Something Else", 80)
        assigment3 = classroom_manager.Assignment("Another One", 60)
        student = classroom_manager.Student(5, "Jeff", "Maname")
        student.assignments = [assigment, assigment2, assigment3]
        getav = classroom_manager.Student.get_average(student)
        self.assertEqual(0, getav)
        classroom_manager.Assignment.assign_grade(assigment, 100)
        classroom_manager.Assignment.assign_grade(assigment2, 80)
        classroom_manager.Assignment.assign_grade(assigment3, 60)
        student.assignments = [assigment, assigment2, assigment3]
        getav = classroom_manager.Student.get_average(student)
        self.assertEqual(80, getav)

    def test_submit_assignment(self):
        assigment = classroom_manager.Assignment("Extra Credit", 100)
        assigments = [assigment]
        assigment2 = classroom_manager.Assignment("Something Else", 80)
        assigment3 = classroom_manager.Assignment("Another One", 60)
        student = classroom_manager.Student(5, "Jeff", "Maname")
        classroom_manager.Student.submit_assignment(student, assigment)
        getsub = classroom_manager.Student.get_assignments(student)
        self.assertEqual(assigments, getsub)
        assigments = [assigment, assigment2]
        classroom_manager.Student.submit_assignment(student, assigment2)
        getsub = classroom_manager.Student.get_assignments(student)
        getfirst = classroom_manager.Student.get_assignment(student, "Extra Credit")
        self.assertEqual(assigments, getsub)
        self.assertEqual(assigment, getfirst)

    def test_remove_assignment(self):
        assigment = classroom_manager.Assignment("Extra Credit", 100)
        assigment2 = classroom_manager.Assignment("Something Else", 80)
        assigment3 = classroom_manager.Assignment("Another One", 60)
        student = classroom_manager.Student(5, "Jeff", "Maname")
        classroom_manager.Student.submit_assignment(student, assigment)
        classroom_manager.Student.remove_assignment(student, "Extra Credit")
        geta = classroom_manager.Student.get_assignments(student)
        assignments = []
        self.assertEqual(assignments, geta)
        student.assignments = [assigment, assigment2, assigment3]
        classroom_manager.Student.remove_assignment(student, "Something Else")
        assignments = [assigment, assigment3]
        geta = classroom_manager.Student.get_assignments(student)
        self.assertEqual(assignments, geta)
        classroom_manager.Student.remove_assignment(student, "Something Else")
        geta = classroom_manager.Student.get_assignments(student)
        self.assertEqual(assignments, geta)







class TestAssignments(TestCase):
    def testConstructor(self):
        name = "Homework"
        max_score = 100
        grade = None
        assigment = classroom_manager.Assignment(name, max_score)
        self.assertEqual(name, assigment.name)
        self.assertEqual(max_score, assigment.max_score)
        self.assertEqual(grade, assigment.grade)

    def test_assign_grade(self):
        grade = 80
        assigment = classroom_manager.Assignment("Extra Credit", 100)
        agrade = classroom_manager.Assignment.assign_grade(assigment, grade)
        self.assertEqual(grade, assigment.grade)
        grade = 110
        agrade2 = classroom_manager.Assignment.assign_grade(assigment, grade)
        self.assertEqual(None, assigment.grade)
        grade = 100
        classroom_manager.Assignment.assign_grade(assigment, grade)
        self.assertEqual(grade, assigment.grade)

def test_react(self):
    pass
