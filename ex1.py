import statistics
def average_score(scores):
    return sum(scores) / len(scores)
def average_score(scores: list[int]) -> float:
     if len(scores)!= 3:
        raise ValueError("Expected exactly three scores")
     #return (sum(scores)/len(scores))
     return float(statistics.mean(scores))
print(average_score([50,67,70]))
print(average_score([80, 90, 70]))
print(average_score([100, 100, 100]))
print(average_score([80, 90, 70, 60]))