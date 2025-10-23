import random
from typing import List


class RockPaperScissors:
    """
    Main class for the game Rock, Paper, Scissors
    """
    def __init__(self):
        self.choices: List[str] = ['rock', 'paper', 'scissors']

    def get_user_choice(self) -> str:
        """Method to get the user's choice.
        
        :return: User's choice as a string
        """

        

        user_choice: str = input("Enter your choice (rock/paper/scissors): ")
        if user_choice in self.choices:
            return user_choice
        else:
            print    
