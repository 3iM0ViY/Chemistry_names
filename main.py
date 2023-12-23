from compounds import *
import random as r

def gen():
	all = len(general)
	print("Great! In this regeme you can get a random name or formula of a compound.\n\nFor example: ", end="")
	results = [0, 0]
	while True:
		if len(general) > 0:
			part = r.randint(0, 1)
			if part == 0:
				compound = general[r.randint(0, len(general) - 1)]
				print(f"Write the formula of the following compound: {compound['name']}")
				response = input("Your answer: ")
				if response.casefold() == compound['formula'].casefold():
					print("Bravo! *&^&^&^*\n")
					results[0] += 1
				elif response == ":q!":
					break
				else:
					print(f"Wrong. The correct answer is: {compound['formula']}\n")
					results[1] += 1
			if part == 1:
				compound = general[r.randint(0, len(general) - 1)]
				print(f"Write the name of the following compound: {compound['formula']}")
				response = input("Your answer: ")
				if response.casefold() == compound['name'].casefold():
					print("Bravo! *&^&^&^*\n")
					results[0] += 1
				elif response == ":q!":
					break
				else:
					print(f"Wrong. The correct answer is: {compound['name']}\n")
					results[1] += 1
			general.remove(compound)
		else:
			print(f"That's all {all} compounds in this mode.")
			break
	print(f"Your stats: {results[0]} correct answers, {results[1]} were wrong.\n")


def main():
	while True:
		print("\nWelcome! Let's do some chemistry training.\nSelect the mode: g - general, a - acids, an - just the anions.\n# You can always exit typing :q!\n")
		mode = input("You choose: ")
		if mode == "g":
			gen()



if __name__ == "__main__":
	main()