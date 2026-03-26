marks = {}

for i in range(5):
    subject = input("Enter subject name: ")
    score = int(input("Enter marks for " + subject + ": "))
    marks[subject] = score

total = sum(marks.values())
print("Total marks:", total)

average = total / len(marks)
print("Average marks:", average)

highest = max(marks.values())
print("Highest mark:", highest)

top_subject = max(marks, key=marks.get)
print("Subject with highest mark:", top_subject)