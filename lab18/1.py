class Human():
    def __innit__(self,f_name,m_name):
        self.f_name = f_name
        self.m_name = m_name
class Student(Human):
    def __innit__(self,grade):
        self.grade = grade
class Worker(Human):
    def __init__(self,wage,work_hrs):
        self.wage = wage
        self.work_hrs = work_hrs
    def calc_wage_1hr(self):
        res = self.wage/self.work_hrs
        return res

students = {
    'Peter Stoyanov': 5.4,
    'Boiko Bogdanov': 5.1,
    'Maria Terezova': 5.0
}
students_grades = list()
for k,v in students.items():
    f = Student()
    students_grades.append(k + ' ' + str(v))
print(students_grades)

workers = {
    'Peter Stoyanov': [16,65],
    'Brian Bogdanov': [29,35],
    'Maria Terezova': [33,55] 
}
workers_1hr_wage = list()
for k,v in workers.items():
    s = Worker(v[0],v[1])
    One_hour_wage = Worker.calc_wage_1hr(s)
    workers_1hr_wage.append(k + ' ' + str(One_hour_wage))
print(workers_1hr_wage)