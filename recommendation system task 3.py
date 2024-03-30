import numpy as np
class CollaborativeFiltering:
    def __init__(self, num_users, num_items, ratings):
        self.num_users = num_users
        self.num_items = num_items
        self.ratings = ratings
        self.similarity_matrix = np.zeros((num_items, num_items))
        self.predictions = np.zeros((num_users, num_items))

    def calculate_similarity(self):
        for i in range(self.num_items):
            for j in range(self.num_items):
                if i != j:
                    mask = np.logical_and(self.ratings[:, i] != 0, self.ratings[:, j] != 0)
                    if np.any(mask):
                        self.similarity_matrix[i, j] = np.corrcoef(self.ratings[mask, i], self.ratings[mask, j])[0, 1]
                    else:
                        self.similarity_matrix[i, j] = 0
        self.similarity_matrix[np.isnan(self.similarity_matrix)] = 0

    def predict_ratings(self):
        for user in range(self.num_users):
            for item in range(self.num_items):
                if self.ratings[user, item] == 0:
                    numerator = 0
                    denominator = 0
                    for j in range(self.num_items):
                        if self.ratings[user, j] != 0:
                            numerator += self.similarity_matrix[item, j] * self.ratings[user, j]
                            denominator += np.abs(self.similarity_matrix[item, j])
                    if denominator != 0:
                        self.predictions[user, item] = numerator / denominator

    def recommend_items(self, user_id, top_n=5):
        user_predictions = self.predictions[user_id]
        top_indices = np.argsort(user_predictions)[::-1][:top_n]
        return top_indices

# Example usage
num_users = 5
num_items = 10
ratings = np.array([
    [5, 0, 0, 0, 4, 0, 0, 0, 0, 1],
    [0, 4, 0, 0, 0, 0, 0, 2, 0, 0],
    [0, 0, 3, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 2, 0, 0, 0, 0, 3, 0],
    [0, 0, 0, 0, 0, 4, 5, 0, 0, 0]
])

cf = CollaborativeFiltering(num_users, num_items, ratings)
cf.calculate_similarity()
cf.predict_ratings()

user_id = 0
recommendations = cf.recommend_items(user_id)
print("Recommendations for user", user_id, ": ", recommendations)

