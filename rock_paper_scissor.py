import random
rock= '''
    ----
---   ----)
      (-----)    
      (-----)
      (----)
---._ _(---) '''
paper='''
    -------
---'   _ _ _ _)_ _ _ _
             _ _ _ _ _ _)
             _ _ _ _ _ _ _)
           _ _ _ _ _ _ _)
---._ _ _ _ _ _ _ _ _ )  
'''
scissor='''
    -------
---'    _ _ _ _)_ _ _ _
              _ _ _ _ _ _)
        _ _ _ _ _ _ _ _ _ _) 
        (_ _ _ _)
----._ _(_ _ _)
'''
game_image=[rock,paper,scissor]
choose=int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissor.\n"))
if choose>=0 and choose<2:
    print(game_image[choose])
computer_choice=random.randint(0,2)
print(f"Computer chose:")
print(game_image[computer_choice])

if choose>=3:
    print("You typed an invalid number, You lose!")
elif computer_choice=="2" and choose=="0":
    print("You win!")
elif computer_choice=="0" and choose=="2":
    print("You lose, Computer wins!")
elif choose>=3:
    print("You typed an invalid number, You lose!")
elif computer_choice>choose:
    print("You lose, Computer wins!")
elif computer_choice<choose:
    print("You win!")
elif choose==computer_choice:
    print("That's a tie!")
elif choose>=3:
    print("You typed an invalid number, You lose!")
