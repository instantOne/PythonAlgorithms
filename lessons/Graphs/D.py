def digit_sum(n):
    return sum(map(int, str(n)))

costs = [(0, 0)]
def min_digit_sum(K):
    N = K * 2
    min_sum = digit_sum(N)
    iteration_limit = 10**2
    for _ in range(iteration_limit):
        cur_sum = digit_sum(N)
        if min_sum >= cur_sum:
            min_sum = cur_sum
        prev = digit_sum(N - K)
        cur = digit_sum(N)
        costs.append((costs[_][0] + cur - prev, N))

        N += K
    print(costs)
    return min_sum

def main():
    K = int(input())
    print(min_digit_sum(K))
if __name__ == "__main__":
    main()