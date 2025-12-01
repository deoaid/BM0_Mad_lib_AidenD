person = input("Enter a person:")
place = input("Enter a place:")
thing = input("Enter a thing:")
import random



if random.randint(1,2) == 2:
		print(f"{person} is walking in the airport as they just landed in {place} but they forgot their {thing}.")
else:
	print(f"Many people hate on {person} due to their love of {thing}, people from their hometown {place} still support them.")
