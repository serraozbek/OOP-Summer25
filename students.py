students =[
    {
        "first_name" : "Serra",
        "last_name" : "Ozbek",
        "index_number" : 35248,
        "nationality" : "Turkey",
        "starting_date" : "03.10.2024",
        "courses" : ["math", "computer science", "english"]

    },
    {  
        "first_name" : "Berke",
        "last_name" : "Haliloglu",
        "index_number" : 35274,
        "nationality" : "Turkey",
        "starting_date" : "03.10.2024",
        "courses" : ["math", "computer science", "management"]

    },
    {  
        "first_name" : "Sırrı",
        "last_name" : "Cataloglu",
        "index_number" : 34854,
        "nationality" : "Turkey",
        "starting_date" : "03.10.2024",
        "courses" : ["math", "computer science", "economy"]

    }
]

for student in students:
    print(f"Name: {student['first_name']} {student['last_name']}, Index: {student['index_number']}") 