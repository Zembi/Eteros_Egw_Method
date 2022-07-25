#Pythagoras mathematic method
import sys

#Create a class/object through which it will find the amicable numbers
class EterosEgw:
	def __init__(self, numberToStopSearch):
		self.numberToStopSearch = numberToStopSearch
		self.countOfFriendMainNumber = 0;
		self.countOfFriendSecNumber = 0;

	def searchForFriendsNumbers(self):

		#Function that is getting as an input, a number and returns the possible new amicable number of it
		def giveNumberAndGetTheNewOne(number):
			c = 0
			for y in range(1, number):
				z = number % y
				if z == 0:
					c += y

			return c

		for x in range(1, self.numberToStopSearch):
			self.countOfFriendMainNumber = 0;
			self.countOfFriendSecNumber = 0;

			#Find first the other number
			self.countOfFriendSecNumber = giveNumberAndGetTheNewOne(x)

			#Then check the new number you found if they are amicable with the starting one (current x value)
			self.countOfFriendMainNumber = giveNumberAndGetTheNewOne(self.countOfFriendSecNumber)

			#Finally make sure if there in any occassion are the same two numbers, but that they are unequal
			if self.countOfFriendMainNumber == x and self.countOfFriendMainNumber != self.countOfFriendSecNumber:
				print(self.countOfFriendMainNumber, " ", self.countOfFriendSecNumber)


	#Explain the Έτερος Εγώ method
	def explainMethod(self):
		print("\nExplanation")
		print("Either of a pair of numbers each of which equals the sum of the different exact divisors of the other excluding the number itself.")

#Ask input from the user
text = input("Write a number-STOP, to stop searching for amicable numbers -> ")
text = int(text)

#Create the object(class EterosEgw) where are all the functions are and call those which needed
obj = EterosEgw(text)
obj.searchForFriendsNumbers()
obj.explainMethod()