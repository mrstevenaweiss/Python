!/usr/bin/python3

my_list= [4, 1, 5, 0, 1, 6, 5, 1, 5, 3]

def count_keys_equal(numbers, constraint):
    length = len(numbers)
    equal = [0] * constraint
    
    for number in numbers:
        equal[number] += 1
    return equal
    
    
def count_keys_less(equal_numbers, constraint):
    
    less = [0] * constraint
    for index in range(1, len(equal_numbers)):
        less[index] = less[index - 1] + equal_numbers[index -1]
        
    return less

# A. Set key to AŒi.
# B. Set index to nextŒkey.
# C. Set BŒindex to AŒi.
# D. Increment nextŒkey.
# 4. Return the B array.

def rearrange(less_numbers, length_of_original_list, original_list):
    print([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 'indexes')
    # print(original_list, 'original list')
    # print([5, 1, 6, 0, 2, 9, 7, 3, 8, 4], 'index pattern')
    # print('\n')
    print(less_numbers, ' less numbers')
    # print([0, 1, 1, 1, 3, 4, 5, 5, 5, 6], 'desired')
    
    counted_sorted = []
    rearrange = []
    length_of_less = len(less_numbers)
    
    # for less_number in less_numbers:
    #     rearrange.append(less_number + 1)
    # # print(rearrange)
    # for index in range(length_of_original_list):
    number = less_numbers[5]
    print(number)
    print(original_list[number])
    
    # counted_sorted.append(original_list[less_numbers[5]])
        # print(original_list[index], less_numbers[index])
        
