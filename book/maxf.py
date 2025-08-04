def max_frequency(s):
    freq = {}  # dictionary to store frequency of each character
    
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    
    max_freq = max(freq.values())  # get the highest frequency
    return max_freq

# Example usage:
input_str = "hello world"
print("Maximum frequency:", max_frequency(input_str))
