import tensorflow as tf

def cosine_similarity(v1, v2):
    v1_norm = tf.nn.l2_normalize(v1, axis=-1)
    v2_norm = tf.nn.l2_normalize(v2, axis=-1)
    return tf.reduce_sum(tf.multiply(v1_norm, v2_norm), axis=-1)

def enhanced_similarity(features, user_input, ratings, sentiments, alpha=0.4, beta=0.6):
    # Calculate cosine similarity between user input and feature vectors
    sim_scores = cosine_similarity(features, user_input)
    ratings_scaled = (ratings - tf.reduce_min(ratings)) / (tf.reduce_max(ratings) - tf.reduce_min(ratings))
    sentiments_scaled = (sentiments - tf.reduce_min(sentiments)) / (tf.reduce_max(sentiments) - tf.reduce_min(sentiments))
    final_scores = alpha * sim_scores + beta * (0.4 * ratings_scaled + 0.6 * sentiments_scaled)
    return final_scores

def weather_decider(m):
    if 4 <= m <= 9:  #kemarau == 1
        return 1
    else:
        return 0