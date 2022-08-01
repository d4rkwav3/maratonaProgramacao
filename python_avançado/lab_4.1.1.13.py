'''
Objectives

    improving the student's skills in creating classes representing candies;
    improving the student's skills in operating with deepcopy() and copy.

Scenario

The previous task was a very easy one. Now let's rework the code a bit:

    introduce the Delicacy class to represent a generic delicacy. The objects of this class will replace the old school dictionaries. Suggested attribute names: name, price, weight;
    your class should implement the __str__() method to represent each object state;
    experiment with the copy.copy() and deepcopy.copy() methods to see the difference in how each method copies objects .
'''
import copy as c

class Candy:
    def __init__(self, name, price, weight) -> None:
        self.name = name
        self.price = price
        self.weight = weight

    def __str__(self) -> str:
        return f'{self.name}\tPrice: {self.price}\tWeight: {self.weight}'

choco = Candy("Chocolate", 2.0, 0.6)
choco_bar = choco 
choco_bar.name = "Chocolate Bar"
choco_bar.price = 1.0
choco_bar.weight = 0.2

print(choco, choco_bar, sep="\n")

lemon_pie = Candy("Lemon Pie", 20.0, 1.5)
lemon_pie_piece = c.copy(lemon_pie) # Why is working just like deepcopy??
lemon_pie_piece.name = "Lemon Pie Piece"
lemon_pie_piece.price = 2.0
lemon_pie_piece.weight = 0.350

print(lemon_pie, lemon_pie_piece, sep="\n")

ice_cream = Candy("Vanilla Ice Cream", 5.0, 10.0)
gelato = c.deepcopy(choco)
gelato.name = "Red Velvet Gelato"
gelato.price = 7.0
gelato.weight = 0.25

print(ice_cream, gelato, sep="\n")