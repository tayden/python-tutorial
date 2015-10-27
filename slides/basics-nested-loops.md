## Nested loops

You can do anthing you want in the [Do something] part of the loop, including call more loops

    quads = [
      [1,2,3,4],
      [5,6,7,8]
    ]

    for item in quads:
        # item is [1,2,4,8], then [1,3,9,27].
        for n in item:
            print n*2, # trailing comma makes print not add a newline
            print ", ",

        print # print a newline


    output>> 2, 4, 6, 8,
    output>> 10, 12, 14, 16,
