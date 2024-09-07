name = input('type your name: ')
print('Welcome', name , 'to this adventure!')

answer = input('You in a small boat alone and u got caught in a storm, u got 2 options to fight thro the storm or sit in a barrel and pray, what would u do? (fight/sit) ').lower()
if answer == 'fight':
    answer = input('while fight the storm u got a hole in the boat, now u can sit inside a barrel or abort the ship, what would u do? (abort/sit) ').lower()
    if answer == 'sit':
        print('storm got worse by the time and u drowned')
    elif answer == 'abort':
        print('You drowned!')    
    else:
        print('invalid option ,U loose !')
        
elif answer == 'sit':
    answer = input('U found yourself in a island with strangers and u got a chance to talk to them(talk/ignore)? ').lower()
    if answer == 'talk':
        print('they helped you and u got to go to another adventure someday')
    elif answer == 'ignore':
        print("You got lost and u couldn't survive!")    
    else:
        print('invalid option ,U loose !')
else:
    print('invalid option ,U loose !')

print('thanks for going thro this adventure', name)