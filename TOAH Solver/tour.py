"""
functions to run TOAH tours.
"""


# Copyright 2013, 2014, 2017 Gary Baumgartner, Danny Heap, Dustin Wehr,
# Bogdan Simion, Jacqueline Smith, Dan Zingaro
# Distributed under the terms of the GNU General Public License.
#
# This file is part of Assignment 1, CSC148, Winter 2018.
#
# This is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This file is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this file.  If not, see <http://www.gnu.org/licenses/>.
# Copyright 2013, 2014 Gary Baumgartner, Danny Heap, Dustin Wehr


# you may want to use time.sleep(delay_between_moves) in your
# solution for 'if __name__ == "__main__":'

import time
from toah_model import TOAHModel


def get_i(dic):
    x =0
    for key in dic:
        x = key
    return key

def get_min_dict(dic):
    m = 1000000
    for key in dic:
        if dic[key] < m:
            m = dic[key]
    return m

def get_min_pair(dic):
    m = get_min_dict(dic)
    r = {}
    for key in dic:
        if dic[key] == m:
            r[key] = dic[key]
            return r

def best_i(n):
    best = 1
    if n == 1:
        #print("base case reached")
        return {1:1}
    choices = {}
    for i in range(1, n):
        choice = 2*get_min_dict(best_i(n-i)) + (2**i-1)
        choices[i] = choice
    lil = get_min_pair(choices)
    #print(n)
    return lil

def shift(peg):
    if peg == 0:
        return 1
    if peg == 1:
        return 2
    if peg == 2:
        return 3
    if peg == 3:
        return 1
    
def availability(desin, orig, model):
    base = [0,1,2,3]
    #print(base)
    base.pop(base.index(desin))
    #print(base)
    base.pop(base.index(orig))
    if type(model.get_top_cheese(base[0])) == type(None):
        return base[0]
    if type(model.get_top_cheese(base[1])) == type(None):
        return base[1]    
    return desin
    
                    
        

        
def move_stool(model,n,  i, ori, des, animate, tm):
    tim = tm
    o = ori
    d = des
    if n == 1:
        model.move(o, d)
        try:
            if animate == True:
                time.sleep(tim)
                print(model)
                
                
        except TypeError:
            print("dangit")
    else:
            top = n-i
            bottom = i
            inter = availability(d, o, model)
            move_stool(model, top, get_i(best_i(top)), o, inter, animate, tim)
            
        
            move_stool(model, bottom, get_i(best_i(bottom)), o, d, animate, tim)         
                   
            move_stool(model, top, get_i(best_i(top)), inter, d, animate, tim) 
                


    
def tour_of_four_stools(model, delay_btw_moves=0.5, animate=True):
    """Move a tower of cheeses from the first stool in model to the fourth.

    @type model: TOAHModel
        TOAHModel with tower of cheese on first stool and three empty
        stools
    @type delay_btw_moves: float
        time delay between moves if console_animate is True
    @type animate: bool
        animate the tour or not
    @rtype: None
    """
    move_stool(model, model.get_number_of_cheeses(), get_i(best_i(model.get_number_of_cheeses())), 0, 3, animate, delay_btw_moves )
    
    
    
    #while len(model.stools[-1]) != model.get_number_of_cheeses():
        
        


if __name__ == '__main__':
    num_cheeses = 5
    delay_between_moves = 0.3
    console_animate = True

    # DO NOT MODIFY THE CODE BELOW.
    four_stools = TOAHModel(4)
    four_stools.fill_first_stool(num_cheeses)

    tour_of_four_stools(four_stools,
                        animate=console_animate,
                        delay_btw_moves=delay_between_moves)

    print(four_stools.number_of_moves())
