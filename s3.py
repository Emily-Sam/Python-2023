temperature = input("What will be the temperature today:")

if temperature < "6":
    print("Wear a pair of gloves")
elif temperature < "8":
    print("Wear a hat")
elif temperature < "10":
    print("Wear a scarf")
elif temperature < "12":
    print("Wear a jacket")
elif temperature > "25":
    print("Wear sunglasses")
else:
    print("No recommendation")

rain = input("What is the probability of rain (from 0-100):")

if rain >= "50":
    print("Use an umbrella")
else:
    print("No umbrella needed")
