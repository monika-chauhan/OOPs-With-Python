class CountNumber:
    count = 0  # Class varibaler we define here 
    def __init__(self):
        CountNumber.count += 1

count_class = CountNumber()
count_class1 = CountNumber()
count_class2 = CountNumber()
count_class3 = CountNumber()
print(count_class.count)
