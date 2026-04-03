#Number to roman
#1 to 10


def converter(num):
    nums = {'1':'I', '2':'II','3':'III', '4':'IV','5':'V','6':'VI','7':'VII','8':'VIII','9':'IX','10':'X'}
    for num in nums:
        return nums[num]

print('WELCOME\nPLEASE ENTER A NUMBER BETWEEN 1 AND 10')
number = input('Enter the number: ')
roman_num = converter(number)
print(f"The Roman Number for {number} is {roman_num}")