def max_boring_prefix(n, a):
    counts = {}
    freqs = {}
    left = 0
    max_len = 0

    for right in range(n):
        x = a[right]
        counts[x] = counts.get(x, 0) + 1

        count_x = counts[x]
        freqs[count_x] = freqs.get(count_x, 0) + 1
        freqs[count_x - 1] = freqs.get(count_x - 1, 0) - 1

        while freqs and freqs[min(freqs)] == 0:
            del freqs[min(freqs)]
        max_freq = max(freqs)
        min_freq = min(freqs)

        if max_freq == 1 or (max_freq == min_freq + 1 and freqs[max_freq] == 1):
            max_len = max(max_len, right - left + 1)
        else:
            counts[a[left]] -= 1
            if counts[a[left]] == 0:
                del counts[a[left]]
            freqs[counts.get(a[left], 0)] -= 1
            freqs[counts.get(a[left], 0) + 1] += 1
            left += 1

    return max_len

max_boring_prefix(int(input()), list(map(int, input().split())))