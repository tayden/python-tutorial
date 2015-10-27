##  Nesting conditionals

    powerrangers = [
        {color: "Red", zord_rating: 7 },
        {color: "Black", zord_rating: 8 },
        {color: "Pink", zord_rating: 9 },
        {color: "Blue", zord_rating: 2 }
    ]

    for ranger in powerrangers:
        if ranger.zord_rating > 7:
            print ranger.color


    outputs>> "Black"
    outputs>> "Pint"
