# setup data structure
student_records = []
stats = {}
unique_scores = set()

# collect data for 6 students
print("Enter student data:")
for i in range(6):
    name = input(f"Student {i+1} Name: ")
    score = int(input(f"Student {i+1} Score: "))
    
    # store as tuple
    student_records.append((name, score))

# claculate statistics
all_scores = []
for record in student_records:
    all_scores.append(record[1])

stats['highest'] = max(all_scores)
stats['lowest'] = min(all_scores)
stats['average'] = sum(all_scores) / len(all_scores)

# find unique score
unique_scores = set(all_scores)

# count grade distribution 
grade_distribution = {}
for score in all_scores:
    count = grade_distribution.get(score, 0)
    grade_distribution[score] = count + 1

# print report 
print("\n=== STUDENT RECORDS ===")
for record in student_records:
    print(f"{record[0]}: {record[1]}")

print("\n=== CLASS STATISTICS ===")
print(f"Highest Score: {stats['highest']}")
print(f"Lowest Score: {stats['lowest']}")
print(f"Average Score: {stats['average']:.2f}")

print("\n=== UNIQUE SCORES ===")
print(unique_scores)
print(f"Total unique scores: {len(unique_scores)}")

print("\n=== GRADE DISTRIBUTION ===")
for score, count in grade_distribution.items():
    print(f"Score {score}: {count} students")