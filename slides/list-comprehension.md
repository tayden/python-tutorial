##  List comprehension
A compact for loop for working with lists/tuples

    numbers = [1,2,3,4,5,6,7,8,9,10]

    odds = [n for n in numbers if n%2 == 1]
    print odds

    output>> [1,3,5,7,9]
