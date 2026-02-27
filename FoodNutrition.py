foods = {
"apple":{"calories":52,"protein":0.3,"carbs":14,"fiber":2.4},
"banana":{"calories":96,"protein":1.3,"carbs":27,"fiber":2.6},
"orange":{"calories":43,"protein":1,"carbs":9,"fiber":2.2},
"grapes":{"calories":69,"protein":0.7,"carbs":18,"fiber":0.9},
"papaya":{"calories":43,"protein":0.5,"carbs":11,"fiber":1.7},
"mango":{"calories":60,"protein":0.8,"carbs":15,"fiber":1.6},
"watermelon":{"calories":30,"protein":0.6,"carbs":8,"fiber":0.4},
"pineapple":{"calories":50,"protein":0.5,"carbs":13,"fiber":1.4},
"pear":{"calories":57,"protein":0.4,"carbs":15,"fiber":3.1},
"kiwi":{"calories":61,"protein":1.1,"carbs":15,"fiber":3},

"oats":{"calories":389,"protein":17,"carbs":66,"fiber":11},
"brown rice":{"calories":123,"protein":2.7,"carbs":25,"fiber":1.8},
"white rice":{"calories":130,"protein":2.7,"carbs":28,"fiber":0.4},
"quinoa":{"calories":120,"protein":4.4,"carbs":21,"fiber":2.8},
"chapati":{"calories":104,"protein":3,"carbs":18,"fiber":3},
"pasta":{"calories":131,"protein":5,"carbs":25,"fiber":1.3},
"sweet potato":{"calories":86,"protein":1.6,"carbs":20,"fiber":3},
"corn":{"calories":96,"protein":3.4,"carbs":21,"fiber":2.4},
"barley":{"calories":354,"protein":12,"carbs":73,"fiber":17},

"egg":{"calories":155,"protein":13,"carbs":1.1,"fiber":0},
"egg white":{"calories":52,"protein":11,"carbs":0.7,"fiber":0},
"chicken":{"calories":239,"protein":27,"carbs":0,"fiber":0},
"fish":{"calories":206,"protein":22,"carbs":0,"fiber":0},
"tuna":{"calories":132,"protein":28,"carbs":0,"fiber":0},
"salmon":{"calories":208,"protein":20,"carbs":0,"fiber":0},
"paneer":{"calories":265,"protein":18,"carbs":1.2,"fiber":0},
"tofu":{"calories":76,"protein":8,"carbs":2,"fiber":0.3},
"soybean":{"calories":446,"protein":36,"carbs":30,"fiber":9},
"dal":{"calories":116,"protein":9,"carbs":20,"fiber":8},
"chickpeas":{"calories":164,"protein":9,"carbs":27,"fiber":7.6},
"kidney beans":{"calories":127,"protein":9,"carbs":23,"fiber":6.4},
"black beans":{"calories":132,"protein":9,"carbs":24,"fiber":8.7},

"milk":{"calories":42,"protein":3.4,"carbs":5,"fiber":0},
"curd":{"calories":98,"protein":11,"carbs":4,"fiber":0},
"buttermilk":{"calories":40,"protein":3,"carbs":5,"fiber":0},
"cheese":{"calories":402,"protein":25,"carbs":1.3,"fiber":0},

"almonds":{"calories":579,"protein":21,"carbs":22,"fiber":12},
"walnuts":{"calories":654,"protein":15,"carbs":14,"fiber":7},
"peanuts":{"calories":567,"protein":26,"carbs":16,"fiber":8.5},
"cashews":{"calories":553,"protein":18,"carbs":30,"fiber":3.3},
"chia seeds":{"calories":486,"protein":17,"carbs":42,"fiber":34},
"flax seeds":{"calories":534,"protein":18,"carbs":29,"fiber":27},
"pumpkin seeds":{"calories":559,"protein":30,"carbs":11,"fiber":6},

"broccoli":{"calories":55,"protein":3.7,"carbs":11,"fiber":3.3},
"spinach":{"calories":23,"protein":2.9,"carbs":3.6,"fiber":2.2},
"carrot":{"calories":41,"protein":0.9,"carbs":10,"fiber":2.8},
"tomato":{"calories":18,"protein":0.9,"carbs":3.9,"fiber":1.2},
"cucumber":{"calories":16,"protein":0.8,"carbs":4,"fiber":0.5},
"capsicum":{"calories":31,"protein":1,"carbs":6,"fiber":2.1},
"onion":{"calories":40,"protein":1.1,"carbs":9,"fiber":1.7},
"beetroot":{"calories":43,"protein":1.6,"carbs":10,"fiber":2.8},
"cabbage":{"calories":25,"protein":1.3,"carbs":6,"fiber":2.5},
"cauliflower":{"calories":25,"protein":1.9,"carbs":5,"fiber":2},

"green tea":{"calories":0,"protein":0,"carbs":0,"fiber":0},
"black coffee":{"calories":2,"protein":0,"carbs":0,"fiber":0},
"lemon water":{"calories":5,"protein":0,"carbs":1,"fiber":0},

"protein shake":{"calories":120,"protein":24,"carbs":5,"fiber":1},
"peanut butter":{"calories":588,"protein":25,"carbs":20,"fiber":6},
"veg salad":{"calories":80,"protein":3,"carbs":10,"fiber":4},
"fruit salad":{"calories":120,"protein":2,"carbs":30,"fiber":5},
"chicken salad":{"calories":220,"protein":25,"carbs":6,"fiber":3},
"paneer salad":{"calories":250,"protein":18,"carbs":8,"fiber":3},
"smoothie":{"calories":180,"protein":8,"carbs":35,"fiber":5},
"sprouts":{"calories":80,"protein":7,"carbs":12,"fiber":4}
}

print("Food Macros Calculator developed by Monty")
print("Type exit to quit")

while True:
    food = input("Enter food name: ").lower()
    if food == "exit":
        break
    if food in foods:
        grams = float(input("Enter quantity in grams: "))
        f = foods[food]
        factor = grams / 100
        print("Calories:", round(f["calories"]*factor,2), "kcal")
        print("Protein:", round(f["protein"]*factor,2), "g")
        print("Carbs:", round(f["carbs"]*factor,2), "g")
        print("Fiber:", round(f["fiber"]*factor,2), "g")
        print("------------------")
    else:
        print("Food not found")
        print("------------------")
