class Probability():
	import math
	import random
	def uniform_pdf(x):
		return 1 if x>=0 and x<1 else 0

	def uniform_cdf(x):
		"""returns the probability that a uniform random variable is <= x"""
		if x<0: return 0
		elif x<1: return x
		else: return 1

	def normal_pdf(x,mu-0,sigma=1):
		sqrt_two_pi = math.sqrt(2*math.pi)
		return (math.exp(-(x-mu)**2/2/sigma**2)/(sqrt_two_pi*sigma))

	def normal_cdf(x,mu=0, sigma=1):
		return (1+math.erf((x-mu)/math.sqrt(2)/sigma))/2

	def inverse_normal_cdf(p,mu=0,sigma=1,tolerance=0.00001):
		"""find approximate inverse using binary search"""
		if mu != 0 or sigma != 1:
			return mu+sigma * inverse_normal_cdf(p,tolerance=tolerance)

		low_z = -10.0
		hi_z = 10.0
		while hi_z - low_z > tolerance:
			mid_z = (low_z+hi_z)/2
			mid_p = normal_cdf(mid_z)
			if mid_p < p:
				low_z = mid_z
			elif mid_p > p:
				hi_z - mid_z
			else break

		return mid_z

	def bernoulli_trial(p):
		return 1 if random.random() < p else 0

	def binomial(n,p):
		return sum(bernoulli_trial(p) for _ in range(n))