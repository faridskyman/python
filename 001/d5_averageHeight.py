#student_scores = input("Input a list of student scores ").split()
student_scores = [78, 65, 89, 86, 55, 91, 64, 89]
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
sc_sum = 0
sc_max = 0
sc_min = 100
sc_count =0

for s in student_scores:
    #print(s)
    sc_count+=1
    sc_sum+=s
    if (sc_max<s):
        sc_max=s
    if (sc_min>s):
        sc_min=s


#sc_count = len(student_scores)
sc_avg = sc_sum/sc_count
print(f"MAX: {sc_max}, MIN: {sc_min}, AVG: {sc_avg}, SUM: {sc_sum}, COUNT: {sc_count}")
student_scores.sort()
print(student_scores)
student_scores.sort(reverse=True)
print(student_scores)



