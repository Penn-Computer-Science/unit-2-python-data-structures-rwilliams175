#LISTS
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[0])
print(nums[-1])
print(len(nums)/2)
nums[2] = 99
print(nums)
even_list = []
for number in nums:
    if number % 2 == 0:
        even_list.append(number)
print(even_list)
#DICTIORNARIES
countries = {'India':'New Delhi', 'China':'Beijing','United States':'Washington DC','Indonesia':'Jakarta','Pakistan':'Islamabad'}
print(countries['India'])
print(countries['China'])
countries['Nigeria'] = 'Abuja'
countries['Brazil'] = 'Brasilia'
countries['United States'] = 'Indianapolis'
print(countries)
#SETS
fruits = {'apple', 'mango', 'banana', 'watermelon', 'orange'}
other_fruits = {'pear', 'grapes'}
fruits.update(other_fruits)
friend_fruits = {'pineapple', 'banana', 'dragonfruit', 'watermelon', 'apple', 'cherry', 'kiwi'}
print (fruits & friend_fruits)
print(fruits - friend_fruits)
print(fruits | friend_fruits)
#TUPLES
colors = ('red', 'green', 'blue', 'yellow', 'purple')
print(colors[0] + " " + colors[-1])
print(colors)
colors[0] = 'pink'
