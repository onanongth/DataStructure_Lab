mid = input('Input Midterm Score : ')
mid = int(mid)
fin = input('Input Final Score : ')
fin = int(fin)
score = mid + fin

if score > 100 or score < 0 :
    grade = 'Score error'
elif score >= 80 :
    grade = 'A'
elif score >= 70 :
    grade = 'B'
elif score >= 60 :
    grade = 'C'
elif score >= 50 :
    grade = 'D'
else :
    grade = 'F'

print('Your Grade : ',grade)