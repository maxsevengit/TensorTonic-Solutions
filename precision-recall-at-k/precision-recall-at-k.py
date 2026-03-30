def precision_recall_at_k(recommended, relevant, k):
    """
    Compute precision@k and recall@k for a recommendation list.
    """
    # Take top-k recommendations
    recommended_k = recommended[:k]

    # Convert relevant to set for fast lookup
    relevant_set = set(relevant)

    # Count relevant items in top-k
    relevant_in_k = sum(1 for item in recommended_k if item in relevant_set)

    # Precision@k
    precision = relevant_in_k / k if k > 0 else 0

    # Recall@k
    recall = relevant_in_k / len(relevant_set) if len(relevant_set) > 0 else 0

    return [precision, recall]   # ✅ FIXED