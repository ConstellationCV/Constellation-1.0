import sys
sys.path.insert(0, '../src/modules/Arithmetic_Toolkit')
from Linear_Algebra import Vectors
from collections import Counter

class KNN():
	"""docstring for KNN"""

	def raw_majority_vote(self, labels):
		votes = Counter(labels)
		winner, _ = votes.most_common(1)[0]
		return winner

	def majority_vote(self, labels):
		"""assumes that labels are ordered from nearest to farthest"""
		vote_counts = Counter(labels)
		winner, winner_count = vote_counts.most_common(1)[0]
		num_winners = len([count
							for count in vote_counts.values()
							if count == winner_count])
		if num_winners == 1: # unique winner, so return it
			return winner
		else:
			return self.majority_vote(labels[:-1]) # try again with the k-1 nearest

	def knn_classify(self, k, labeled_points, new_point):
		"""each labeled point should be a pair (point, label)"""
		v = Vectors()
		by_distance = sorted(labeled_points, key=lambda (point, _): abs(point-new_point))
		k_nearest_labels = [label for _, label in by_distance[:k]]
		return self.majority_vote(k_nearest_labels)
