


# keep track of the grades of a set of students

class SimpleGradeBook:
    def __init__(self):
        self._grades = {}

    def add_student(self, name):
        self._grades[name] = []

    def report_grade(self, name, score):
        self._grades[name].append(score)

    def average_grade(self, name):
        print(self._grades)
        grades = self._grades[name]
        return sum(grades) / len(grades)

book =SimpleGradeBook()
book.add_student('Isaac Newton')
book.report_grade('Isaac Newton',	90)
print(book.average_grade('Isaac Newton'))

print('Isaac Newton')
print('Isaac Newton')
print('Isaac	Newton')


# keep a list of grades by subject
# track the weight of each score
# toward the overall grade in the
# class so midterms and finals are
# more important than pop quizzes
class weightGradeBook:
    def __init__(self):
        self._grades = {}

    def add_student(self, name):
        self._grades[name] = {}

    def report_grade(self, name, subject, score, weight):
        by_subject = self._grades[name]
        grade_list = by_subject.setdefault(subject, [])
        grade_list.append((score, weight))

    def average_grade(self, name):
        by_subject = self._grades[name]
        score_sum, score_count = 0, 0
        for subject, scores, in by_subject.items():
            subject_avg, total_weight = 0, 0
            for score, weight in scores:
                # ...
                pass

        return score_sum / score_count

class BySubjectGradeBook(object):
    def __init__(self):
        self._grades = {}
    def add_student(self, name):
        self._grades[name] = {}

    def report_grade(self, name, subject, grade):
        by_subject = self._grades[name]
        #return key value if given key aviable in dictionary
        #if not, return default value and set key to default value
        grade_list = by_subject.setdefault(subject, [])
        grade_list.append(grade)

    def average_grade(self, name):
        by_subject = self._grades[name]
        total, count = 0, 0
        for grades in by_subject.values():
            total += sum(grades)
            count += len(grades)
        return total / count


a = {}
a['a'] = 1
print(a)
c = a.setdefault('a', 'ccc')
#c = a.setdefault(11, 'f')
print(c)

book	=	BySubjectGradeBook()
book.add_student('Albert	Einstein')
book.report_grade('Albert	Einstein',	'Math',	75)
book.report_grade('Albert	Einstein',	'Math',	65)
book.report_grade('Albert	Einstein',	'Gym',	90)
book.report_grade('Albert	Einstein',	'Gym',	95)


import	collections
Grade	=	collections.namedtuple('Grade',	('score',	'weight'))

class Subject:
    def __init__(self):
        self._grades = []

    #every exam a student have taken
    def report_grade(self, score, weight):
        self._grades.append(Grade(score, weight))

    def average_grade(self):
        total, total_weight = 0, 0
        for grade in self._grades:
            total += grade.score * grade.weight
            total_weight += grade.weight
        return total / total_weight


class Student:
    def __init__(self):
        self._subjects = {}

    #subject studied by the student
    def subject(self, name):
        if name not in self._subjects:
            self._subjects[name] = Subject()
        return self._subjects[name]

    def average_grade(self):
        total, count = 0, 0
        for subject in self._subjects.values():
            total += subject.average_grade()
            count += 1
        return total / count

class GradeBook:
    def __init__(self):
        self._students = {}

    def student(self, name):
        if name not in self._students:
            self._students[name] = Student()
        return self._students[name]

book	= GradeBook()
albert	=	book.student('xiao ming')
math	=	albert.subject('math')
math.report_grade(80,	0.10)

print(albert.average_grade())


print(type(Grade('ff', ['3', 'ff'])))

a = lambda x : len(x)
print(a('jjjjjjjjj'))


class Test:
    pass
c = Test()
print(type(Test))
print(type(Test()))
print(c)
print(Test)