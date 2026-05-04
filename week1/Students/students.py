# def sort_key(x):
#     return x[1]

def get_top_student(data: dict, n: int) -> list:

    # new_grade_list = [  for grade in data.values()]
    new_list = [(name, sum(grade)/ len(grade)) for name, grade in data.items()]
    sorted_list = sorted(new_list, key= lambda x: x[1], reverse = True) #key=sort_key
    return sorted_list[:n]

students = {"Alice" :  [70,90,95] ,
            "Max" : [84, 82, 90] ,
            "Leha" : [100, 90, 85] ,
            "Dima" : [91, 80, 75] ,
            "Grisha": [74, 82, 80] ,
            "Toha": [50, 70, 65]
            }


top_3_students = get_top_student(students, 3)

for i, (name, grade )in enumerate(top_3_students):
    print(f"Student №{i+1}: {name}, total grade: {round(grade, 2)}")
