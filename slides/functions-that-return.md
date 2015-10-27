##  Functions that return
Reusable functions typically return a value so it can then be used as the input to another function

    # add two numbers and print the result
    def add(a, b):
        return a+b

    # call function
    result = add(1, 1)
    result = add(1, result)
    print result

    output>> 3
