import random
def count_draws_until_sum_exceeds(limit: int = 42)-> int:
    sum_=0
    count = 0
    while True:
        if sum_ >= limit:
            break
        num_= random.randint(0, 10)
        print(num_)

        sum_ += num_
        count += 1
    print(f"{sum_} exceeded 42 after {count} draws")
    return count
print(count_draws_until_sum_exceeds(42))