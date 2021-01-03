def latest(scores):
    return scores[len(scores)-1]


def personal_best(scores):
    return max(scores)


def personal_top_three(scores):
    top_scores_count = 3
    top_three = []
    top_scores_count = top_scores_count if len(scores) > top_scores_count else len(scores)

    for i in range(top_scores_count):
        max_score = max(scores)
        top_three.append(max_score)
        scores.remove(max_score)
    return top_three