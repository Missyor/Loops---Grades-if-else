while True:
    try:
        grade = int(input("Enter your grade: "))
        break
    except ValueError:
        print("\nThis is not a number. Try again...")
      
while grade <1 or grade >100:
  print("Enter a grade between 1 and 100")
  grade = int(input("Enter your grade: "))
   

if grade >=90:
   print("H1")
elif grade >=80:
   print("H2")
elif grade >=70:
   print("H3")
elif grade >=60:
   print("H4")
elif grade >=50:
   print("H5")
elif grade >=40:
   print("H6")
elif grade >=30:
   print("H7")
else:
  print("H8")