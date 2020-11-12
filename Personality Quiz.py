print("Hello! Welcome To Johanssen Personality Quiz!")

#variables
a_answer = 0
b_answer = 0
c_answer = 0

#Questions 1-10
q1 = input("1) How would you describe yourself? \na)Brave\nb)Laugh\nc)Smart")
if q1.lower () == 'a':
    a_answer += 1
elif q1.lower () == 'b':
    b_answer += 1
elif q1.lower() == 'c' :
    c_answer += 1
else:
    print ("Sorry, I didn't understand that input")

q2 = input("2) Which hand is your dominate had? \na)Right\nb)Left\nc)Both")
if q2.lower () == 'a':
    a_answer += 1
elif q2.lower () == 'b':
    b_answer += 1
elif q2.lower() == 'c' :
    c_answer += 1
else:
    print ("Sorry, I didn't understand that input")

q3 =input("3) How do you sleep? \na)Stomach\nb)Back\nc)Side")
if q3.lower () == 'a':
    a_answer += 1
elif q3.lower () == 'b':
    b_answer += 1
elif q3.lower() == 'c' :
    c_answer += 1
else:
    print ("Sorry, I didn't understand that input")

q4 =input("4) What is your most common dream? \na)Falling\nb)Dying\nc)Other")
if q4.lower () == 'a':
    a_answer += 1
elif q4.lower () == 'b':
    b_answer += 1
elif q4.lower() == 'c' :
    c_answer += 1
else:
    print ("Sorry, I didn't understand that input")

q5 = input("5) You're waiting in a long line.\na)You chat with the person next to you\nb)You keep your eyes on your phone\nc)Other")
if q5.lower () == 'a':
    a_answer += 1
elif q5.lower () == 'b':
    b_answer += 1
elif q5.lower() == 'c' :
    c_answer += 1
else:
    print ("Sorry, I didn't understand that input")

q6 = input("6) Roomates:\na)It is great to have someone there when you get home.\nb)You’d much rather live by yourself.\nc)Other")
if q6.lower () == 'a':
    a_answer += 1
elif q6.lower () == 'b':
    b_answer += 1
elif q6.lower() == 'c' :
    c_answer += 1
else:
    print ("Sorry, I didn't understand that input")

q7 = input("7) If you had to choose, you'd rather be: \na)enginner\nb)designer\nc)teacher")
if q7.lower () == 'a':
    a_answer += 1
elif q7.lower () == 'b':
    b_answer += 1
elif q7.lower() == 'c' :
    c_answer += 1
else:
    print ("Sorry, I didn't understand that input")

q8 = input("8) Your friends would describe you as: \na)a very open person\nb)in middle\nc)a very private person")
if q8.lower () == 'a':
    a_answer += 1
elif q8.lower () == 'b':
    b_answer += 1
elif q8.lower() == 'c' :
    c_answer += 1
else:
    print ("Sorry, I didn't understand that input")

q9 = input("9) Choose the word that describes you better: \na)logical\nb)emotional\nc)strategic")
if q9.lower () == 'a':
    a_answer += 1
elif q9.lower () == 'b':
    b_answer += 1
elif q9.lower() == 'c' :
    c_answer += 1
else:
    print ("Sorry, I didn't understand that input")



q10 =input("10) Are your feeling easily hurt:\na)Yes\nb)Maybe\nc)No")
if q10.lower () == 'a':
    a_answer += 1
elif q10.lower () == 'b':
    b_answer += 1
elif q10.lower() == 'c' :
    c_answer += 1
else:
    print ("Sorry, I didn't understand that input")

if a_answer > b_answer and a_answer > c_answer:
    print(" You have a average personality! \n its a common personality \n tending to be more sociable, assertive,pessimistic,and over-sensitive\n tending to be more routine based and less open to attraction\n tend to seek attention but are not overly intellectually curious")
elif c_answer > a_answer and b_answer > c_answer:
    print(" You have a roles model personality! \n tending to exhibit qualities that evoke respect and admired leadership\n tending to be more confident and brave, taking calculated risks\n Dependable and open to new ideas\n Strong leaders")
elif c_answer > a_answer and c_answer > b_answer:
    print(" You have a reserved personality! \n tending to be more trusting,sensitive,well-liked,and reliable\n tending to stay on the course with confidence\n Emotionally stable \nSomewhat extraverted,but not overly so ")
else:
    print("Amazing you personality is a combination of Role Model, Average, and Reserved!")