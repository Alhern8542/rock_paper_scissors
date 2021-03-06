#!/usr/bin/env python3
import random

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def learn(self, my_move, their_move):
        pass


class RockPlayer(Player):
    def move(self):
        return 'rock'


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


def valid_input(string, options):
    while True:
        word = input(string).lower()
        if word in options:
            return word
        else:
            print("Invalid choice, try again")


class HumanPlayer(Player):
    def move(self):
        return valid_input("choose rock, paper, or "
                           "scissors:\n", ["rock", "paper", "scissors"])


def beats(one, two):  # players choices are compared for player one win
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class ReflectPlayer(Player):
    def __init__(self):
        self.new_move = "rock"

    def move(self):
        return self.new_move

    def learn(self, my_move, their_move):
        self.new_move = their_move


class CyclePlayer(ReflectPlayer):
    def learn(self, my_move, their_move):
        if my_move == "rock":
            self.new_move = "paper"
        elif my_move == "paper":
            self.new_move = "scissors"
        else:
            self.new_move = "rock"


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.score1 = 0
        self.score2 = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        player1_wins = beats(move1, move2)
        if move1 == move2:
            print("It is a tie!\n")
        elif player1_wins:
            self.score1 += 1
            print("Player 1 wins round, score: "
                  f"{self.score1} - {self.score2} \n")
        else:
            self.score2 += 1
            print("Player 2 wins round, score: "
                  f"{self.score1} - {self.score2} \n")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self, num_rounds):
        print("Game start!")
        for round in range(num_rounds):
            print(f"Round {round+1}...")   # rounds start from 1
            self.play_round()
        if self.score1 == self.score2:
            print("The game is a tie!")
        elif self.score1 > self.score2:
            print("Player 1 wins the game!")
        else:
            print("Player 2 wins the game!")
        print(f"Final score: {self.score1} - {self.score2}\nGame over!")


def choose_opponent():
    opponent = {
        "1": RockPlayer(),
        "2": RandomPlayer(),
        "3": CyclePlayer(),
        "4": ReflectPlayer()}
    key = valid_input("Select opponent type:\n"
                      "1- Rock Player\n2- Random Player\n"
                      "3- Cycle Player\n"
                      "4- Reflect Player\n", ["1", "2", "3", "4"])
    return Game(HumanPlayer(), opponent[key])


def play():
    game = choose_opponent()
    rounds = int(valid_input("Choose number of rounds(1-7)"
                             ": ", ["1", "2", "3", "4", "5", "6", "7"]))
    game.play_game(rounds)  # choose number of rounds


if __name__ == '__main__':
    play()
