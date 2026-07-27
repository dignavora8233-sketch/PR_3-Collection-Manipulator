#Collection Manipulator

students = []

print("*"*60)
print("Welcome to the student Data Organizer!!")
print("*"*60)

print("Select an Option:")

while True:
    print("\n1.Add Student")
    print("2.Display All Students")
    print("3.Update student Information")
    print("4.Delate Student")
    print("5.Display Subject Offered")
    print("6.Exit")


    choice = input("Enter your choice: ")

    #-----ADD STUDENT-----#

    if choice == "1":

       std_id = input("Enter Student ID: ")
       
       found = False

       for student in students:
           if student["ID"] == std_id:
            print("Student id already exists.")
            found = True
            break

       if not found:
          name = input("Enter Name: ")
          age = int(input("Enter Age: "))
          grade = input("Enter Grade:")
          dob = input("Enter DOB (DD MM YYYY): ").split()
          dob = tuple(dob)
          subjects = set(input("Enter Subjects using comma: ").split(","))

          student = {
               "ID": std_id,
               "Name": name,
               "Age": age,
               "Grade" : grade,
               "DOB": dob,
               "Subjects": subjects
               }
          
          students.append(student)
          print("Student Added Successfully.")

          print(students)

    #----------DISPLAY----------#
    
    elif choice == "2":

        print("\n---Display All Students---")
        
        if len(students) == 0:
            print("No students found!!")
            
        else:
            for student in students:
                
                print(f"""
                      Student ID   :  {student['ID']}
                      Name         :  {student['Name']}
                      Age          :  {student['Age']}
                      Grade        :  {student['Grade']}
                      DOB          :  {student['DOB']}
                      Subjects     :  {student['Subjects']}
                      """)

    #----------UPDATE----------#

    elif choice == "3":

      serach_id = input("\nEnter Student ID to Update:")

      for student in students:
            if student ["ID"] == serach_id:
               student ["Name"] = input("Enter New Name:")
               student ["Grade"] = input("Enter New Grade:")
               student ["DOB"] = input("Enter New DOB:")
               
               print("Update Successfuly!!")
               
               break

            else:
                print("student not found!!")

    #----------DELETE----------#

    elif choice == "4":

        serach_id = input ("\nEnter ID to delete:")

        for student in students:
            if student ["ID"] == serach_id:
                students.remove(student)

                print("Delete Successfuly!")

                break

            else:
                print("Student not found!")

    #----------SUBJECTS----------#
    elif choice == "5":

        print("\n--- Display Subjects Offered ---")

        all_subjects = set()

        for student in students:

            for subject in student["Subjects"]:

                all_subjects.add(subject)

        print("Subjects offered:" , ", ".join(all_subjects))

    #----------EXIT-----------#
    
    elif choice == "6":
        
        print("Thsnk you for using Student Data Organizer.")

        print("Goodbye!!")
        break

    #----------INVALID----------#
    
    else:

        print("Invalid Choice! Please enter a number between 1 and 6.")
            
    
        






    
