# binary search algo

# init values
data_list = [0.1, 0.4, 0.5, 1.9, 2.0, 3.7, 7.4]
value = 2.0
low_idx = 0
high_idx = len(data_list) - 1

# loop
while low_idx <= high_idx: # correct algorithm
    print(f'low is {low_idx} and high is {high_idx}')

    mid_idx = int((low_idx + high_idx) / 2)
    guess_value = data_list[mid_idx]

    # compare guess to value
    if guess_value == value:
        print(f"you found it! at {mid_idx}")
        break
    # check higher numbers
    elif value > guess_value:
        low_idx = mid_idx + 1
    # check lower numbers
    else:
        high_idx = mid_idx - 1

# print(f'{value} was found at position {mid_idx}')
