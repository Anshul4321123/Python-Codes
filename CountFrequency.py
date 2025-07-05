
def frequency(string):
    count={}
    for char in string:
        if char in count:
            count[char]+=1
        else:
            count[char]=1
    return count


string="countfrequency"
count = frequency(string)
for char in count:
    print(f"{char}: {count[char]}")