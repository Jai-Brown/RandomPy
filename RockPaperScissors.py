#! /usr/bin/env python
from random import randint, seed
from sys import exit, version_info

# Python 2 and 3 compatibility.
input = raw_input if version_info == 2 else input

__version__ = '0.1'
__author__ = 'JaINTP - Jai Brown'
__maintainer__ = 'JaINTP - Jai Brown'
__status__ = 'Development'


class RockPaperScissors(object):
    """Basic class that handles a Rock, Paper, Scissors game."""

    __slots__ = [
        '__choices'
    ]

    def __init__(self):
        """Constructor.
        Initialises member variables.
        """
        self.__choices = ['Rock', 'Paper', 'Scissors']

    def game_loop(self):
        """Main method that handles the game logic."""
        # Seed the random number generator.
        seed()

        # Enter main loop.
        while True:
            # Get user input.
            player_turn = self.get_input()
            # Get bot input.
            bot_turn = randint(0, 2)
            result = self.get_result(player_turn, bot_turn)

            # Output choices.
            print('You chose: {}\nBot chose: {}'.format(
                self.__choices[player_turn],
                self.__choices[bot_turn]))

            # Check and declare results!
            if not result[0] and not result[1]:
                print('Tie!\n')
            else:
                print('{} win{}!\n'.format('Bot' if result[1] else 'You',
                                           's' if result[1] else ''))

    @staticmethod
    def get_input():
        """ Retrieves the user's input with a menu style prompt.

        @rtype:  int
        @return: The user's input, minus one.
        """
        choice = None
        while True:
            try:
                print('Rock - 1\nPaper - 2\nScissors - 3\nExit - 4')
                choice = int(input('Choice: '))

                if choice not in (1, 2, 3, 4):
                    raise ValueError()
                else:
                    break
            except (ValueError, SyntaxError):
                print('Invalid input!')

        if choice == 4:
            exit()
        return choice - 1

    def get_result(self, player_choice, bot_choice):
        """Calculates the results of both the player's and the bot's turns.

        @type player_choice:  int
        @param player_choice: The player's selection.

        @type bot_choice:  int
        @param bot_choice: The bot's selection.

        @rtype:  tuple
        @return: A tuple containing two booleans.
                 Whether the player's turn won and whether the bot's turn won.
        """
        # player_choice - 1 should equal the bot's choice to win.
        # Yes I know PEP8 says not to assign lambdas, but YOLO!
        algo = lambda a, b, c: c[b] == c[a - (1 if a == 0 else 1)]

        player_wins = algo(player_choice, bot_choice, self.__choices)
        bot_wins = algo(bot_choice, player_choice, self.__choices)

        return player_wins, bot_wins


if __name__ == '__main__':
    game = RockPaperScissors()
    game.game_loop()
