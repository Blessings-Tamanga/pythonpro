name = input("Enter your name: ")
age = int(input("Enter your age "))


if age > 18:
	print("you are old enough to vote")
elif age > 66:
	print("you are old you cannot vote")
elif age < 15:
	print("okay")
else:
	print("You are a person")