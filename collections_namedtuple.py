from collections import namedtuple


n = int(input())
a = input()
total = 0
Student = namedtuple('Student', a)
print(Student)

for _ in range(n):
    student = Student(*input().split())
    total += int(student.MARKS)
    print(student)
print('{:.2f}'.format(total/n))
