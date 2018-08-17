import math
class Vectors:
	import math
	def vector_add(v,w):
		"""adds corresponding elements"""
		return [v_i + w_i for v_i, w_i in zip(v,w)]

	def vector_subtract(self,v,w):
		"""subtracts corresponding elements"""
		return [v_i - w_i for v_i,w_i in zip(v,w)]

	def vector_sum(vectors):
		"""sums all corresponding elements"""
		result = vectors[0]
		for vector in vectors[1:]:
			result = vector_add(result, vector)
		return result

	def scalar_multiply(c,v):
		"""c is a number, v is a vector"""
		return [c*v_i for v_i in v]

	def vector_mean(vectors):
		"""compute the vector whose ith element is the mean of the
		ith elements of the input vectors"""
		n = len(vectors)
		return scalar_multiply(1/n,vector_sum(vectors))

	def dot(self,v,w):
		"""v_1 * w_1 + ... v_n * w_n"""
		return sum(v_i * w_i for v_i,w_i in zip(v,w))

	def sum_of_squares(self,v):
		"""v_1 * v_1 + ... + v_n * v_n"""
		return self.dot(v,v)

	def magnitude(self,v):
		"""magnitude(length) of vector v"""
		return math.sqrt(self.sum_of_squares(v))

	def squared_distance(self, v,w):
		"""((v_1 - w_1)^2) + ... ((v_n - w_n)^2)"""
		return self.sum_of_squares(self.vector_subtract(v,w))

	def distance(self, v,w):
		"""distance between vectors 1 and 2"""
		return math.sqrt(self.squared_distance(v,w))

class Matrices:
	def shape(A):
		num_rows = len(A)
		num_cols = len(A[0]) if A else 0
		return num_rows,num_cols

	def get_row(A,i):
		return A[i]

	def get_column(A,j):
		return [A_i[j] for A_i in A]

	def make_matrix(num_rows, num_cols, entry_fn):
		"""return a num_rows x num_cols matrix
		whose (i,j)th entry is entry_fn(i,j)"""
		return [[entry_fn(i,j)
				for  j in range(num_cols)]
				for i in range(num_rows)]

	def is_diagonal(i,j):
		"""1s on the diagonal, 0s everywhere else"""
		return 1 if i==j else 0