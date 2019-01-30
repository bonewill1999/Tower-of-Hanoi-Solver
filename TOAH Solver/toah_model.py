

def IsLegalMove(model, origin, destination):
    if origin <= model.stools.len() and destination <= moedl.stools.len():
        if model.get_top_cheese(origin) != None:
            if model.get_top_cheese(origin).size < model.get_top_cheese(origin).size:
                return True
    return False

class TOAHModel:
    """ Model a game of Tour Of Anne Hoy.

    Model stools holding stacks of cheese, enforcing the constraint
    that a larger cheese may not be placed on a smaller one.
    """

    def __init__(self, number_of_stools):
        """ Create new TOAHModel with empty stools
        to hold stools of cheese.

        @param TOAHModel self:
        @param int number_of_stools:
        @rtype: None

        >>> M = TOAHModel(4)
        >>> M.fill_first_stool(5)
        >>> (M.get_number_of_stools(), M.number_of_moves()) == (4,0)
        True
        >>> M.get_number_of_cheeses()
        5
        """
        #pass
        # you must have _move_seq as well as any other attributes you choose
        self._move_seq = MoveSequence([])
        self.number_of_stool = number_of_stools
        self.moves = 0
        self.stools = []
        for i in range(number_of_stools):
            self.stools.append([])

    def get_move_seq(self):
        """ Return the move sequence

        @type self: TOAHModel
        @rtype: MoveSequence

        >>> toah = TOAHModel(2)
        >>> toah.get_move_seq() == MoveSequence([])
        True
        """
        return self._move_seq

    def __eq__(self, other):
        """ Return whether TOAHModel self is equivalent to other.

        Two TOAHModels are equivalent if their current
        configurations of cheeses on stools look the same.
        More precisely, for all h,s, the h-th cheese on the s-th
        stool of self should be equivalent to the h-th cheese on the s-th
        stool of other

        @type self: TOAHModel
        @type other: TOAHModel
        @rtype: bool

        >>> m1 = TOAHModel(4)
        >>> m1.fill_first_stool(7)
        >>> m1.move(0, 1)
        >>> m1.move(0, 2)
        >>> m1.move(1, 2)
        >>> m2 = TOAHModel(4)
        >>> m2.fill_first_stool(7)
        >>> m2.move(0, 3)
        >>> m2.move(0, 2)
        >>> m2.move(3, 2)
        >>> m1 == m2
        True
        """
        if self.stools == other.stools:
            return True
        return False

    def _cheese_at(self, stool_index, stool_height):
        # """ Return (stool_height)th from stool_index stool, if possible.
        #
        # @type self: TOAHModel
        # @type stool_index: int
        # @type stool_height: int
        # @rtype: Cheese | None
        #
        # >>> M = TOAHModel(4)
        # >>> M.fill_first_stool(5)
        # >>> M._cheese_at(0,3).size
        # 2
        # >>> M._cheese_at(0,0).size
        # 5
        # """
        if 0 <= stool_height < len(self.stools[stool_index]):
            return self.stools[stool_index][stool_height]
        else:
            return None

    def __str__(self):
        """
        Depicts only the current state of the stools and cheese.

        @param TOAHModel self:
        @rtype: str
        """
        all_cheeses = []
        for height in range(self.get_number_of_cheeses()):
            for stool in range(self.get_number_of_stools()):
                if self._cheese_at(stool, height) is not None:
                    all_cheeses.append(self._cheese_at(stool, height))
        max_cheese_size = max([c.size for c in all_cheeses]) \
            if len(all_cheeses) > 0 else 0
        stool_str = "=" * (2 * max_cheese_size + 1)
        stool_spacing = "  "
        stools_str = (stool_str + stool_spacing) * self.get_number_of_stools()

        def _cheese_str(size):
            # helper for string representation of cheese
            if size == 0:
                return " " * len(stool_str)
            cheese_part = "-" + "--" * (size - 1)
            space_filler = " " * int((len(stool_str) - len(cheese_part)) / 2)
            return space_filler + cheese_part + space_filler

        lines = ""
        for height in range(self.get_number_of_cheeses() - 1, -1, -1):
            line = ""
            for stool in range(self.get_number_of_stools()):
                c = self._cheese_at(stool, height)
                if isinstance(c, Cheese):
                    s = _cheese_str(int(c.size))
                else:
                    s = _cheese_str(0)
                line += s + stool_spacing
            lines += line + "\n"
        lines += stools_str

        return lines
    
    def fill_first_stool(self, num_cheese):
        for c in range(num_cheese, 0, -1):
            new_cheese = Cheese(c)
            self.stools[0].append(new_cheese)
            
        
    def move(self, origin, destination):
        if origin == destination:
            raise IllegalInputError()
        if self.stools[origin] != []:
            if self.IsLegalMove(origin, destination) == True:
                x = self.stools[origin].pop()
                self.stools[destination].append(x)
                self.moves += 1
                self._move_seq.add_move(origin, destination)
            else:
                raise IllegalInputError()
            
        
        
    
    def get_number_of_cheeses(self):
        count = 0
        for stool in range(len(self.stools)):
            for plates in self.stools[stool]:
                count += 1
        return count
    
    def get_number_of_stools(self):
        count = 0
        for stool in self.stools:
            count += 1
        return count
    
    
    def number_of_moves(self):
        return self.moves
    
    def get_cheese_location(self, cheese):
        for stool in range(len(self.stools)):
            for plate in self.stools[stool]:
                if plate == cheese:
                    return stool
    
    def get_top_cheese(self, stool_index):
        if self.stools[stool_index] == []:
            return None
        return self.stools[stool_index][-1]
        
    
    def add(self, c, destination):
        if destination <= len(self.stools):
            if self.get_top_cheese(destination) == None:
                self.stools[destination].append(c)
            elif c.size <= self.get_top_cheese(destination).size:
                self.stools[destination].append(c)
        else:
            raise IllegalInputError
        
    
    
    
    
    ##
    
    def IsLegalMove(self, origin, destination):
        
        if origin <= len(self.stools) and destination <= len(self.stools):
            if self.get_top_cheese(origin) != None:
                if self.get_top_cheese(destination) == None:
                    return True                
                if self.get_top_cheese(origin).size < self.get_top_cheese(destination).size:
                    return True
                
        return False    
    

class Cheese:
    """ A cheese for stacking in a TOAHModel

    === Attributes ===
    @param int size: width of cheese
    """

    def __init__(self, size):
        """ Initialize a Cheese to diameter size.

        @param Cheese self:
        @param int size:
        @rtype: None

        >>> c = Cheese(3)
        >>> isinstance(c, Cheese)
        True
        >>> c.size
        3
        """
        self.size = size

    def __eq__(self, other):
        """ Is self equivalent to other?

        We say they are if they're the same
        size.

        @param Cheese self:
        @param Cheese|Any other:
        @rtype: bool
        """
        if type(other) == type(None):
            return False
        return self.size == other.size
    def __repr__(self):
        return str(self.size)

class IllegalInputError(Exception):
    """ Exception indicating move that violates TOAHModel
    """
    pass

class FalseMoveError(Exception):
    """ if a false move is made
    """
    pass

class MoveSequence:
    """ Sequence of moves in TOAH game
    """

    def __init__(self, moves):
        """ Create a new MoveSequence self.

        @param MoveSequence self:
        @param list[tuple[int]] moves:
        @rtype: None
        """
        # moves - a list of integer pairs, e.g. [(0,1),(0,2),(1,2)]
        self._moves = moves

    def __eq__(self, other):
        """ Return whether MoveSequence self is equivalent to other.

        @param MoveSequence self:
        @param MoveSequence|Any other:
        @rtype: bool
        """
        return type(self) == type(other) and self._moves == other._moves
        
    def get_move(self, i):
        """ Return the move at position i in self

        @param MoveSequence self:
        @param int i:
        @rtype: tuple[int]

        >>> ms = MoveSequence([(1, 2)])
        >>> ms.get_move(0) == (1, 2)
        True
        """
        # Exception if not (0 <= i < self.length)
        return self._moves[i]

    def add_move(self, src_stool, dest_stool):
        """ Add move from src_stool to dest_stool to MoveSequence self.

        @param MoveSequence self:
        @param int src_stool:
        @param int dest_stool:
        @rtype: None
        """
        self._moves.append((src_stool, dest_stool))

    def length(self):
        """ Return number of moves in self.

        @param MoveSequence self:
        @rtype: int

        >>> ms = MoveSequence([(1, 2)])
        >>> ms.length()
        1
        """
        return len(self._moves)

    def generate_toah_model(self, number_of_stools, number_of_cheeses):
        """ Construct TOAHModel from number_of_stools and number_of_cheeses
         after moves in self.

        Takes the two parameters for
        the game (number_of_cheeses, number_of_stools), initializes the game
        in the standard way with TOAHModel.fill_first_stool(number_of_cheeses),
        and then applies each of the moves in this move sequence.

        @param MoveSequence self:
        @param int number_of_stools:
        @param int number_of_cheeses:
        @rtype: TOAHModel

        >>> ms = MoveSequence([])
        >>> toah = TOAHModel(2)
        >>> toah.fill_first_stool(2)
        >>> toah == ms.generate_toah_model(2, 2)
        True
        """
        model = TOAHModel(number_of_stools)
        model.fill_first_stool(number_of_cheeses)
        for move in self._moves:
            model.move(move[0], move[1])
        return model

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


        
def move_stool(model,n,  i, ori, des):
    if n == 1:
        model.move(ori, des)
    else:
            top = n-i
            bottom = i
            inter = availability(ori, des, model)
            move_stool(model, top, get_i(best_i(top)), ori, inter)
        
        
            move_stool(model, bottom, get_i(best_i(bottom)), ori, des)         
        
            move_stool(model, top, get_i(best_i(top)), inter, des)

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
