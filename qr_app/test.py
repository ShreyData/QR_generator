students = []
for _ in range(int(input())):
    student = []
    name = input()
    score = float(input())
    student.append(name)
    student.append(score)
    students.append(student)

print(students)
def second_lowest(s_list):
    s_list.sort(key=lambda x: x[1])
    if s_list[1][1] == s_list[2][1]:
        return f"{s_list[1][0]}\n{s_list[2][0]}"
    else:
        return s_list[1][0]

print(second_lowest(students))

"""5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39"""