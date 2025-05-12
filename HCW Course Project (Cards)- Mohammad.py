deck=set()

#You are not allowed to modify this function.
def createDeck():
    for each in ['clubs','diamonds','hearts','spades']:
        for item in ['2','3','4','5','6','7','8','9','10','J','Q','K','A']:
            deck.add(item+' of '+each)
    '''Puts the card ranks and suites together and adds it to the set called deck, allowing it to be a set of 52 'cards'.
        This allows the set that is called 'deck' to have each of it's 'values' look similar to: 6 of Hearts''' 

# You need to modify/complete this function.
# Make sure to comment appropriately.
# The strip() method from Topic 7 (Files & Exceptions) may help you
# isnumeric() may also help you
def determineWinnerOfRound(player, CPU):
    
    cardRank = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13}
    # a dictionary to match the string values to their numeric values
    CPU_rank = cardRank[CPU.strip()]
    Player_rank = cardRank[player.strip()]
    #Will strip any space if the string is a single character/number
    if CPU_rank < Player_rank:
        return('PLAYER')
    elif CPU_rank > Player_rank:
        return('CPU')
    else:
        return('TIE')
    #determines who is the winner of the round or if there is a tie instead

# You need to modify/complete this function.
# Make sure to comment appropriately.
# Format specifier from Topic 2 (Numbers & Strings) may help you.
def printTheDeck():
    pDeck = list(deck)
    rows = (len(pDeck) // 4) + (1 if len(pDeck) % 4 != 0 else 0)
    '''turns the set called deck into a list so a for statement will work,
    additionally it sets how long row will be while adapting to the decreasing size of the deck.
    So even if there are not 52 cards, it will still print the cards in 4 different columns''' 
    for row in range(rows):
        for col in range(4):
            index = row * 4 + col
            if index < len(pDeck):
                print(f'{pDeck[index]:<15s}', end='')
    #A nested for statement to iterate through the cards and print them in columns
        print()
    print(f'There are {len(deck)} remaining.')
    

# You are not allowed to modify this function.
# Make sure to comment appropriately.
def pullCard():
    for card in deck:
        return card
    '''returns a random card value, this is due to deck being a set and sets are unordered'''
    
# You need to modify/complete this function.
# Make sure to comment appropriately.
def removeCard(card):
    deck.discard(card)
    '''deletes the card/value from the set that is called deck'''

#This function should print out if the winner is player, CPU
def chooseFinalWinnerOfGame(player,CPU,ties):
    if ties==2:
        print('\nTwo rounds had a tie, so the game was ended.')
    if player>CPU:
        print('\nPLAYER is the winner!!')
    elif player==CPU:
        print('\nThere is a Tie.')
    else: print('\nCPU is the winner!!')
    print(f'\nThe final rounds score is PLAYER:{player} and CPU:{CPU} and Tied:{ties}')
    '''This function simply compares the values it receives like player wins, CPU wins, and ties. If there were two ties during the game it will let the user know.
    If player wins are greater than CPU then the player wins. If it is the opposite then the CPU wins.'''
# You need to modify/complete this function.
# Make sure to comment appropriately.
def instructions():
    print('--------------------------------------------!!!WELCOME TO HIGH CARD WINS!!!--------------------------------------------')
    print('In this game, the goal is to beat the dealer\'s card.\nYou will pull a card and the dealer will pull a card.\nWhomever has the higher card wins both card.')
    print('\nThe player with highest number of card after 15 rounds and/or 2 ties is the winner.')
    print('\nIf both players pull the same value (for example, 5 of diamonds and 5 of clubs), those cards are tossed out and no one receives them. Ties do not count as a completed round.')
    print('\nFrom highest to lowest, the card values are: K Q J 10 9 8 7 6 5 4 3 2 A')
     #This function simply prints the instructions in this order. This helps the user know the rules of the game and grasp an understanding of the game before playing.

    
# You need to modify/complete this function.
# Make sure to comment appropriately.
def playerChoice(pTotal,cpuTotal,tieTotal):
    pChoice = input('\nType DECK to show remaining cards, SCORE to show round totals, or press Enter to continue: ')

    while pChoice != '':
        if pChoice == 'DECK': 
            printTheDeck()
        elif pChoice == 'SCORE':
            theScore(pTotal,cpuTotal,tieTotal)
        else:
            print('Invalid Option, please enter a valid input.')
        pChoice = input('\nType DECK to show remaining cards, SCORE to show round totals, or press Enter to continue: ')

        '''If the input that the user inputs is not the 'ENTER' key then this function will check if they typed DECK or SCORE instead.
        If they did then it will call upon the respective functions so it can give the user what they requested. If the input is not valid it will inform the user.
        The function will also not proceed with the round even after printing the deck or the score and will only proceed when the ENTER key is inputted.'''

        
# You are NOT allowed to modify this function.
# Make sure to comment appropriately.
def theScore(player,CPU,ties):   
    print(f'\nThe rounds score is player:{player} and CPU:{CPU} and Tied:{ties}.')
    print()
    '''It displays the score when called by the playerChoice function'''

# YOU ARE NOT ALLOWED TO MODIFY main().
def main():
    instructions()
    print()
    createDeck()
    turns=1
    pTotal=0
    cpuTotal=0
    tieTotal=0
    while turns<=15 and tieTotal<2:
        print()
        playerChoice(pTotal,cpuTotal,tieTotal)
        player=pullCard()
        removeCard(player)      
        CPU=pullCard()
        removeCard(CPU)
        print('-'*30+'Round '+str(turns)+'-'*30)
        print("Player card is",player)
        print("CPU card is",CPU)
        roundWinner=determineWinnerOfRound(player[0:2],CPU[0:2])
        print(f"{roundWinner} wins Round {turns}.")
        if roundWinner=='PLAYER':          
            pTotal=pTotal+1
            turns=turns+1       
        elif roundWinner=='CPU':
            cpuTotal=cpuTotal+1
            turns=turns+1           
        else:
            print(f"No one wins a tie. We should replay Round {turns}.")
            tieTotal=tieTotal+1
 
        
    chooseFinalWinnerOfGame(pTotal,cpuTotal,tieTotal)
        
main()
