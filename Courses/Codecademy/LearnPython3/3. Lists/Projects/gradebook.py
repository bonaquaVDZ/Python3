# You are a student and you are trying to organize your subjects and grades using Python. 
# Let’s explore what we’ve learned about lists to organize your subjects and scores.

last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Your code below: 
subjects = ['physics', 'calculus', 'poetry', 'history']
grades = [98, 97, 85, 88]

gradebook = [[subjects[0], grades[0]], [subjects[1], grades[1]],[subjects[2], grades[2]],[subjects[3], grades[3]]]

gradebook.append(['computer science', 100])
gradebook.append(['visual arts', 93])
gradebook[5][1] = 98
gradebook[2].remove(85)
gradebook[2].append('Pass')

full_gradebook = last_semester_gradebook + gradebook
print(full_gradebook)




