# author CJP 9/29/ 2021

magic_strength = int(input("What is your magic strength level? "))

shield_charged = int(input("What is your shield charged to? "))

if not ((magic_strength >= 90) and (shield_charged >= 75)): 
    print("The dragon burns you to a crisp.")
else:
    print("You defeated the dragon! But the princess is in another castle.")
