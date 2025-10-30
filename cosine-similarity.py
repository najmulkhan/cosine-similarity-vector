import math

def cosine_similarity(v1, v2):
    """
    Calculates the cosine similarity between two vectors.
    """
    dot_product = sum(x * y for x, y in zip(v1, v2))
    magnitude_v1 = math.sqrt(sum(x**2 for x in v1))
    magnitude_v2 = math.sqrt(sum(y**2 for y in v2))

    if magnitude_v1 == 0 or magnitude_v2 == 0:
        return 0  # Handle cases where one or both vectors are zero vectors

    return dot_product / (magnitude_v1 * magnitude_v2)

# Example usage
vector1 = [3, 45, 7, 2]
vector2 = [2, 54, 13, 15]
similarity = cosine_similarity(vector1, vector2)
print(f"Cosine Similarity: {similarity}")