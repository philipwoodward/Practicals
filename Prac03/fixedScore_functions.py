"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

def main():
	score = float(input("Enter score between 1 and 100: "))
	score_result = score_status(score)
	if score_result == 6:
		print ("Invalid score")
	elif score_result == 5:
		print ("Bad")
	elif score_result == 4:
		print ("Passable")
	#else print ("Excellent")	
	
	
def score_status(score):
	print ("The score is " + str(score))
	if score < 0 or score > 100:
		score_result= 6
		print ("The score_result is " + str(score_result))
		return (score_result)
	elif score < 50:
		score_result = 5
		print ("The score_result is " + str(score_result))
		return (score_result)
	elif score < 90:
		score_result = 4
		print ("The score_result is " + str(score_result))
		return (score_result)
	else:
		score_result = 3
		print ("The score_result is " + str(score_result))
		return (score_result)

main()
