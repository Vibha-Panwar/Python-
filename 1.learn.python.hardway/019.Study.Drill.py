def cheese_and_crackers_and_fanta(cheese_amount , box_of_crackers , bottles_of_fanta):
    print(f"You have {cheese_amount} cheeses.")
    print(f"You have {box_of_crackers} boxes of crackers.")
    print(f"you have {bottles_of_fanta} bottles of fanta.")
    print("Girls!! that's more than enough.")

cheese_and_crackers_and_fanta(10,20,25)

print("OR,We can use variable just to give amount.")
cheese_amount = 15
box_of_crackers = 25
bottles_of_fanta = 30
cheese_and_crackers_and_fanta(cheese_amount,box_of_crackers,bottles_of_fanta)

print("We can do math inside too :")
cheese_and_crackers_and_fanta(2*12 , 13*2 , 900/5)

print("We can combine two variable togathe here.")
cheese_and_crackers_and_fanta(cheese_amount+20 , box_of_crackers-5 , bottles_of_fanta +20)
cheese_and_crackers_and_fanta(cheese_amount+box_of_crackers , box_of_crackers+bottles_of_fanta , bottles_of_fanta+cheese_amount)
