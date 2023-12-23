from compounds import *
import random as r

def gen(compounds, message):
	all = len(compounds)
	print(message, end="")
	results = [0, 0]
	while True:
		if len(compounds) > 0:
			part = r.randint(0, 1)
			if part == 0: # write the formula
				compound = compounds[r.randint(0, len(compounds) - 1)]
				print(f"Write the formula of the following compound: {compound['name']}")
				response = input("Your answer: ")
				if response.replace("^", "").casefold() == compound['formula'].replace("^", "").casefold(): # syntax of responses (still can be frustrating though)
					print("Bravo! *&^&^&^*\n") # 🎉
					results[0] += 1
				elif response == ":q!":
					break
				else:
					print(f"Wrong. The correct answer is: {compound['formula']}\n")
					results[1] += 1

			if part == 1: # write the name
				compound = compounds[r.randint(0, len(compounds) - 1)]
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

			compounds.remove(compound)
		else:
			print(f"That's all {all} compounds in this mode.")
			break

	print(f"Your stats: {results[0]} correct answers || {results[1]} were wrong.\n")


def main():
	while True:
		print("\nWelcome! Let's do some chemistry training.\nSelect the mode: g - general, a - acids, o - organic (to be released).\n# You can always exit typing :q!\n")
		mode = input("You choose: ")
		if mode == ":q!":
			print("\nOK, see you around. Winter is coming -- good luck on the exam)\n")
			exit()
		elif mode == "g":
			gen(general, "Great! In this regeme you can get a random name or formula of a compound.\n\nFor example: ")
		elif mode == "a":
			gen(acids, "Great! In this regeme you can get a random name or formula of an acid or its anion.\n\nFor example: ")
		elif mode == "o":
			print("I'm absolutely interested in creating this part, so it'll be released soon...\nThe general mode, however, has more than 200 compounds at the moment - maybe check it out?\n")

if __name__ == "__main__":
	main()