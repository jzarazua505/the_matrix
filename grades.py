calc = int(input("What is the calc grade? "))
chem = int(input("What is the chem grade? "))
econ = int(input("What is the econ grade? "))
sum = calc + chem + econ
print(sum)
avg = sum / 3
print(avg)

if avg < 4:
    print("Failed, work harder!")
if 4 <= avg < 7:
    print("work harder, bro")
if avg >= 7:
    print("Good job")

if avg < 4:
    print("Failed, bruh")
elif avg < 7:
    print("You passed I guess")
else:
    print("Wow dude")
