from apple_tree import AppleTree

tree = AppleTree()

while tree.any_apples() == False:
    tree.age_tree()

print(f"My apple tree is producing apples at age {tree.age} and is {tree.height} feet tall")

while tree.is_dead() == False: 
    apple_basket = []

    while tree.any_apples(): 
        apple_basket.append(tree.pick_an_apple())
    check = []
    for apple in apple_basket:
        check.append(apple.diameter)
    avg_diameter = round((sum(check) / len(check)), 2)

    print(f"Year {tree.age} Report")
    print(f"Tree height: {tree.height} feet")
    print(f"Harvest: {len(apple_basket)} apples with an average diameter of {avg_diameter} inches")

    # Age the tree another year
    tree.age_tree()

print(f"The tree is now dead at age {tree.age}! Time to plant a new one!")
