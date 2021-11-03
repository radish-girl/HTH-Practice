##Creating dictionary from given table
food_price = {
    "Chicken":1.59, 
    "Beef":1.99, 
    "Cheese":1.00, 
    "Milk":2.50
    }
print(food_price) ##check dictionary content, order is arbitrary in dictionaries

##Create new dictionary
shoe_type = {
    "errands":"sneakers",
    "lifting":"converse",
    "party":"heels",
    "home":"none",
}

errand_shoes = shoe_type["errands"]
lift_shoes = shoe_type["lifting"]
party_shoes = shoe_type["party"]
home_shoes = shoe_type["home"]

print(errand_shoes)
print(lift_shoes)
print(party_shoes)
print(home_shoes)


##Access food price and store in variable
chicken_price = food_price["Chicken"]
beef_price = food_price["Beef"]
cheese_price = food_price["Cheese"]
milk_price = food_price["Milk"]

print(chicken_price)
print(beef_price)
print(cheese_price)
print(milk_price)

##Shoe name and inventory counts
shoe_inv = {
    "Jordan 13":1,
    "Yeezy":8,
    "Foamposite":10,
    "Air Max":5,
    "SB Dunk": 20
}

##subtract 2 pairs sb dunks
shoe_inv["SB Dunk"] -= 2
##add 1 pair yeezys
shoe_inv["Yeezy"] += 1
##all increase by 7
shoe_inv["Jordan 13"]+=7
shoe_inv["Yeezy"]+=7
shoe_inv["Foamposite"]+=7
shoe_inv["Air Max"]+=7
shoe_inv["SB Dunk"]+=7

##all decrease by 3
shoe_inv["Jordan 13"]-=3
shoe_inv["Yeezy"]-=3
shoe_inv["Foamposite"]-=3
shoe_inv["Air Max"]-=3
shoe_inv["SB Dunk"]-=3

print(shoe_inv)

##Adding key:value pairs to existing dictionaries
##notation dict_name[key] = value
##just adding one to each dictionary I have
food_price["Tomato"] = 1.00
shoe_type["going through it"] = "flip flops"
shoe_inv["Chuck Taylors"] = 0

print(food_price)
print(shoe_type)
print(shoe_inv)

##Deleting items in dictionary
##notation del dict_name[key]
del food_price["Tomato"] 
del shoe_type["going through it"] 
del shoe_inv["Chuck Taylors"] 

print(food_price)
print(shoe_type)
print(shoe_inv)

