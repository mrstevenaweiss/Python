def rock_paper_scissor(shape1, shape2):
    
    if shape1 == 'rock':
        print(moves[rock])
    
    if shape1 == shape2: 
        return 'It is a draw'
    else: 
        if shape1 == 'rock':
            if shape2 == 'scissor':
                return 'rock wins, scissor loses'
            elif shape2 == 'paper': 
                return 'paper wins, rock loses'
                
        if shape1 == 'scissor':
            if shape2 == 'rock':
                return 'rock wins, scissor loses'
            elif shape2 == 'paper': 
                return 'paper wins, scissor loses'
        
        if shape1 == 'paper':
            if shape2 == 'rock':
                return 'paper wins, rock loses'
            elif shape2 == 'scissor': 
                return 'scissor wins, paper lose'        
        

player1 = 'rock'
player2 = 'rock'

print(rock_paper_scissor(player1, player2))

:wq

