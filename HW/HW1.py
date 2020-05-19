def isPrime(number):
	for i in range (2, number):
		if (number % i) == 0:
			return False

	return True

def findSigmasAndLambdas():
	lowerBound = input("Please enter a number --> ")
	upperBound = input("Please enter a larger number --> ")
	
	primes = []
	sigmaPairs = []
	lambdas = []
	
	for i in range(lowerBound, upperBound + 1):
		if isPrime(i):
			primes.append(i)
	
	if len(primes) > 0:
		print("Sigma pair(s) in the range (" + str(lowerBound) + "..." + str(upperBound) + ")")
		for i in range(0, len(primes) - 1):
			if (primes[i] + primes[i + 1]) % 3 != 0:
				sigmaPairs.append(primes[i])
				sigmaPairs.append(primes[i + 1])
				print(str(primes[i]) + "\t" + str(primes[i + 1]))

		for i in range(0, len(primes)):
			if sigmaPairs.count(primes[i]) > 1:
				lambdas.append(primes[i])
				
		if len(lambdas) > 0:
			print("Lambda prime(s) in the range (" + str(lowerBound) + "..." + str(upperBound) + ")")
			print(lambdas)
		else:
			print("No lambda primes found")
	else:
		print("No primes found")
	
findSigmasAndLambdas()