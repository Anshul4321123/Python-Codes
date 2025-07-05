def max_frequency(lst):
    count = {}
    for char in lst:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
        max_freq = max(count.values())
        max_freq_char = [k for k, v in count.items() if v == max_freq]
    print(f"{max_freq},{max_freq_char}")


string = "maxFrequencyyyy"
max_frequency(string)
