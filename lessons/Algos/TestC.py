count = 0 # initialize count to 0
for i in range(1000000, 10000000): # loop through all 7-digit numbers in base 9
    num = oct(i)[2:] # convert the number to base 9 and remove the '0o' prefix
    if num.count('8') == 1 and num[0] in ['2', '4', '6'] and num[-1] in ['1', '3', '5', '7']:
        # check if the number has exactly one '8', and if it starts with an even digit and ends with an odd digit
        count += 1 # increment the count if the number satisfies the conditions

print("The number of 7-digit numbers in base 9 with exactly one '8', not starting with odd digits and not ending with even digits is:", count)
