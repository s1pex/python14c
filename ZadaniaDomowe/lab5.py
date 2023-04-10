import smtplib

students = {}

with open("students.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        data = line.strip().split(",")
        email = data[0]
        name = data[1]
        surname = data[2]
        points = int(data[3])
        totalPoint = float(data[4]) if data[4] else None
        mailStatus = data[5]
        students[email] = {'name': name, 'surname': surname, 'points': points, 'grade': totalPoint, 'status': mailStatus}

def saveDtudentsData():
    with open("students.txt", "w") as f:
        for email, data in students.items():
            line = f"{email},{data['name']},{data['surname']},{data['points']},{data['grade'] or ''},{data['status']}\n"
            f.write(line)

def addStudent():
    email = input("Enter email: ")
    if email in students:
        print("Student already exists!")
        return
    name = input("Enter name: ")
    surname = input("Enter surname: ")
    totalPoint = int(input("Enter points: "))
    grade = None
    mailStatus = ''
    students[email] = {'name': name, 'surname': surname, 'points': totalPoint, 'grade': grade, 'status': mailStatus}
    saveDtudentsData()

def removeStudent():
    email = input("Enter email: ")
    if email not in students:
        print("Student not found!")
        return
    del students[email]
    saveDtudentsData()

def assignGrades():
    for email, data in students.items():
        if data['status'] not in ['GRADED', 'MAILED']:
            if data['points'] >= 90:
                data['grade'] = 5
            elif data['points'] >= 75:
                data['grade'] = 4
            elif data['points'] >= 60:
                data['grade'] = 3
            else:
                data['grade'] = 2
            data['status'] = 'GRADED'
    saveDtudentsData()

def sendEmail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    sender_email = input("Enter your email: ")
    sender_password = input("Enter your password: ")
    server.login(sender_email, sender_password)
    message = ("Your grade has been posted!")
    message['Subject'] = "Grade Notification"
    for email, data in students.items():
        if data['status'] != 'MAILED':
            message['To'] = email
            server.sendmail(sender_email, email, message.as_string())
            data['status'] = 'MAILED'
    server.quit()
    saveDtudentsData()

while True:
    print("\nMenu:")
    print("1. Add student")
    print("2. Remove student")
    print("3. Assign grades")
    print("4. Send email")
    print("5. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        addStudent()
    elif choice == '2':
        removeStudent()
    elif choice == '3':
        assignGrades()
        saveDtudentsData()
    elif choice == '4':
        sendEmail()
        saveDtudentsData()
    elif choice == '5':
        break
    else:
        print("Invalid choice, try again!")
