import random

def __main__():
    def pickRandom() -> str:
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        return f'The {random.choice(ranks)} of {random.choice(suits)}'
    
    print(pickRandom())
    
if __name__ == '__main__':
    __main__()