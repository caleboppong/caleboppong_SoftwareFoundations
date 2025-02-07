#----Software Foundations Assessment
#--Generated  : 27.12.2024 - Caleb Oppong
#--Modified : 07/02/2025 - Caleb Oppong
#--Description : Python file v005

#This functions determine the grade input of students based on their average score
def calculate_average(scores):
    return sum(scores) / len(scores)

def assign_grade(average):
    if average >= 95:
        return 'A'
    elif average >= 85:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'

#-----End Funtions---------------

# importing csv file
import csv



# starting the students list
students = []

# reading csv file
#with open('Students_input.csv','r') as file:
with open('Students_input.csv','r') as file:
        # creating a csv reader object
        reader = csv.reader(file)

        # Read the header (first row)
        header = next(reader) 
        
        # extracting field names through first row
        for row in reader:
            #this derterming the first row  which is student name and subject or data collected from the student input.
            name, geography, history, maths = row
            #this will calculate the average of or three subject.
            average = calculate_average([int(geography), int(history), int(maths)])
            m_grade = assign_grade(int(geography))
            s_grade = assign_grade(int(history))
            e_grade = assign_grade(int(maths))
            # Determine if the student passed or failed
            pass_fail = "Congratulations, you passed!" if average >= 60 else "Fail"
            #This will print the student result grade, average, the condition of pass or fail in the output.
            students.append([name, geography, m_grade, history, s_grade, maths, e_grade, average, pass_fail])

with open('Students_output.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Geography', 'Geography_Grade','History','History_Grade', 'Maths', 'Maths_Grade','Average', 'Pass_Fail'])
        writer.writerows(students)

print('Results saved to Student_output.csv')