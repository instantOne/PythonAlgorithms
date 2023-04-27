def max_boring_prefix_length(n, a):
    counts = {}
    freqs = {}
    left = 0
    max_len = 0

    for right in range(n):
        num = a[right]

        # Увеличиваем количество вхождений элемента num
        counts[num] = counts.get(num, 0) + 1

        # Увеличиваем частоту этого количества вхождений
        count_freq = counts[num]
        freqs[count_freq] = freqs.get(count_freq, 0) + 1

        # Если можно удалить один элемент из текущего префикса
        # чтобы получить скучный префикс, сдвигаем left вправо на 1
        while freqs[max(freqs)] > 1 and left <= right:
            count_freq_left = counts[a[left]]
            freqs[count_freq_left] -= 1
            if freqs[count_freq_left] == 0:
                del freqs[count_freq_left]
            counts[a[left]] -= 1
            left += 1

        # Проверяем, является ли текущий префикс скучным
        if len(freqs