
def get_top_grades(data: dict, n: int)->list:

    # new_list=[(name, max(grades)) for name, grades in data.items()]
    new_list = []
    for name, grades in data.items():
        # new_list.append((name,grades))
        for grade in grades:
            new_list.append((name, grade))


    sorted_list = sorted(new_list, key= lambda x: x[1], reverse= True)

    return sorted_list[:n]


students = {"Alice" :  [70,90,95] ,
            "Max" : [84, 82, 90] ,
            "Leha" : [100, 99, 85] ,
            "Dima" : [91, 80, 75] ,
            "Grisha": [74, 82, 80] ,
            "Toha": [50, 70, 65]
            }


top_3_students = get_top_grades(students, 3)
for name, grades in top_3_students:
    print(f"Name: {name}, grade: {grades}")

