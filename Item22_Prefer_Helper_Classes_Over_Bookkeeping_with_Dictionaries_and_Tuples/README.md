# Prefer	Helper	Classes	Over	Bookkeeping	with Dictionaries	and	Tuples



* refactor a complex dictionary in class to a helper class

```
# keep track of the grades of a set of students
class SimpleGradeBook:
    def __init__(self):
        self._grades = {}

    def add_student(self, name):
        self._grades[name] = []

    def report_grade(self, name, score):
        self._grades[name].append(score)

    def average_grade(self, name):
        scores = self._grades[name]
        return sum(scores) / len(scores)
```

when requires become complex
```
# keep a list of grades by subject
# track the weight of each score
# toward the overall grade in the
# class so midterms and finals are
# more important than pop quizzes

No:
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

Yes:
# refactor grade to a namedtuple
# as soon as you find yourself going longer
# than a two-tuple, its time to consider another
# approch
import collections
Grade = collections.namedtuple(‘Grade’,	(‘score’,	‘weight’))
```