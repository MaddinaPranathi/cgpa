# Function to convert grades to grade points
def grade_to_points(grade):
    grade_dict = {'O': 10,'A+': 9,'A': 8,'B+': 7,'B': 6,'C': 5,'U': 0 }
    # U means the student has failed in that subject
    return grade_dict.get(grade)

# Module for credit-based GPA calculation
def calculate_gpa(credits, grades):
    total_points = 0#total points obtained by the student
    total_credits = 0#total credits of that particular semester
    for i in range(len(credits)):
        total_points += credits[i] * grade_to_points(grades[i])
        total_credits += credits[i]
    return total_points / total_credits

# Function for each semester
def calculate_sem_gpa(sem_credits, sem_subjects):
    sem_grades = []
    for i in range(len(sem_subjects)):
        grade = input(f"Enter your grade for {sem_subjects[i]} (O, A+, A, B+, B, C, U): ")
        if grade == 'U':
            print(f"You have failed in {sem_subjects[i]}. CGPA cannot be calculated.")
            return None
        sem_grades.append(grade)
    return calculate_gpa(sem_credits, sem_grades)

# Main function to calculate CGPA
def calculate_cgpa():
    num_semesters = int(input("Enter the number of semesters you want to calculate CGPA for: "))
    sem_gpas = []
    if(0<num_semesters<=8):
        for sem in range(num_semesters):
            print(f"\n--- Semester {sem+1} ---")
            # Predefined subjects and credits for each semester
            if sem == 0:
                sem_subjects = ('Communicative English','Engineering Chemistry','Matrices and calculus', 'Engineering Physics', 'Problem solving and python programming','Heritage of tamil','Physics and Chemistry Laboratory',
'Problem Solving and Python Programming Laboratory','Communicative English Laboratory')
                sem_credits = (3,3,4,3,3,1,2,2,1)
            elif sem == 1:
                sem_subjects = ('Technical English','Statistics and Numerical Methods','Physics for Computer Science Engineers','Engineering Graphics','Programming in C','Tamils and Technology','Environmental Sciences and Sustainability','Technical English Laboratory','Programming in C Laboratory','Engineering Practices Laboratory')
                sem_credits = (3,4,3,4,3,1,2,1,2,2)
            elif sem==2:
                sem_subjects = ('Digital Principles and Computer Organization','Foundations of Data Science','Data Structures','Object Oriented Programming','Operating Systems','Data Structures Laboratory','Object Oriented Programming Laboratory','Data Science Laboratory','Quantitative Aptitude & Verbal Reasoning')
                sem_credits = (4,3,3,3,4,2,2,2,1)
            elif sem==3:
                sem_subjects = ('Software Engineering','Design and Analysis of Algorithms','Discrete Mathematics','Database Management Systems','Java Programming','Database Management Systems Laboratory','Java Programming Laboratory','Quantitative Aptitude & Behavioural Skills')
                sem_credits = (3,4,4,3,3,2,2,1)
            elif sem==4:
                sem_subjects = ('Compiler Design','Open Elective-I','Computer Networks','Full Stack Programming','Professional Elective-I','Professional Elective-II','Quantitative Aptitude & Communication Skills')
                sem_credits = (4,3,4,4,3,3,1)
            elif sem==5:
                sem_subjects = ('Mobile Computing',' Open Elective-II','Cryptography and Cyber Security','Artificial Intelligence and Machine Learning','Professional Elective-III','Professional Elective-IV','Mobile Application Development Lab','Quantitative Aptitude & Soft Skills',' Mini Project')
                sem_credits = (3,3,4,4,3,3,2,1,2)
            elif sem==6 :
                sem_subjects = ('Human Values and Ethics','Elective - Management','Open Elective - III','Professional Elective - V','Professional Elective - VI','Internship')
                sem_credits = (2,3,3,3,3,1)
            elif sem==7:
                sem_subjects =('project')
                sem_credits =(10)
            # Add more semesters as needed
        
            sem_gpa = calculate_sem_gpa(sem_credits, sem_subjects)
            if sem_gpa is None:
                return
            sem_gpas.append(sem_gpa)
            print(f"Semester {sem+1} GPA: {sem_gpa:.2f}")

        cgpa = sum(sem_gpas) / num_semesters
        print(f"\nYour CGPA after {num_semesters} semesters is: {cgpa:.2f}")
    else:
        print("enter a valid semester number ")

# Run the CGPA calculation
calculate_cgpa()
