def get_top_student(data: dict, n: int) -> list:

    new_list = [(name, sum(grade) / len(grade)) for name, grade in data.items() ]
    sorted_list = sorted(new_list, key=lambda x: x[1], reverse=True)
    return sorted_list[:n]

students = {"Alice" :  [70,90,95] ,
            "Max" : [84, 82, 90] ,
            "Leha" : [100, 90, 85] ,
            "Dima" : [91, 80, 75] ,
            "Grisha": [74, 82, 80] ,
            "Toha": [50, 70, 65]
            }

top_3 = get_top_student(students, 3)
for i, (name, grade) in enumerate(top_3):
    print(f"{i+1}. {name} - {round(grade, 2)} ")