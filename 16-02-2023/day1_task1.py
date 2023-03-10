# Create a function students which takes three numbers total_students, no.of students from bio, and number of students from Math
# 1. Calculate the number of students without math and bio
# 2. Calculate the number of students with math and bio

def students(total, bio,mathematics):
    no_of_std_without_math_bio = total-(mathematics+bio)
    print("Number of students without Math and Bio : "+ str(no_of_std_without_math_bio))

    no_of_std_with_math_bio = mathematics+bio
    print("Number of students with Math and Bio : "+str(no_of_std_with_math_bio))

students(100,60,30)
