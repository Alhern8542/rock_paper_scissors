#!/usr/bin/env python3
import random

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass

class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)

class HumanPlayer(Player):
    def move(self):
        while True:
            word = input("choose rock, paper, or scissors:\n").lower()
            if word in ["rock", "paper", "scissors"]:
                return word
            else:
                print("Invalid choice, try again")


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class ReflectPlayer(Player):
    def __init__(self):
        self.reflect_move = "rock"

    def move(self):
        return self.reflect_move 
        
    def learn(self, my_move, their_move):
        self.reflect_move = their_move


#class CyclePlayer(Player):
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
            print(f"Player 1 wins round, score: {self.score1} - {self.score2} \n")
        else:
            self.score2 += 1
            print(f"Player 2 wins round, score: {self.score1} - {self.score2} \n")
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


if __name__ == '__main__':
    game = Game(HumanPlayer(), RandomPlayer())
    rounds = int(input("Choose number of rounds: "))
    game.play_game(rounds)  # choose number of rounds
