import numpy as np

"""
Hacked ringBuffer.py for 2D data:
- The buffer is a 2D array
- each line represents 512 sensors.
- Don't use np.roll() since it copies values around
"""

#  Objet buffer
# creer un array de donnee avec le nombre de colonne et ligne et le type de nombre 
# format     [[data1],[data2],[data3],[data4]]    print(curent position and size)

class RingBuffer2D(object):
    def __init__(self, rows, cols=512,
                 default_value=0.0, dtype=int):
        """
        initialization
        """
        self.rows = rows # size of buffer = how many events you want to keep for integration for example
        self.cols = cols # data size

        self._data = np.empty((rows, cols), dtype=dtype)
        self._data.fill(default_value)

        self.filled_rows = 0
        self.curr_pos = 0
        self.free_pos = 0

    def append(self, value,ev_num=0,time=0,key=0):
        """
        append a 1D element (row)
        :param value:
        """
        # Assign
        if(key=='addref'):
            self._data[self.curr_pos][0] = ev_num
            self._data[self.curr_pos][1] = time
            self._data[self.curr_pos][2:]= value
        else: self._data[self.curr_pos] = value
        # Go to the next position
        self.curr_pos = (self.curr_pos+1) % self.rows
        # Increment filled_rows if necessary
        if self.filled_rows < self.rows: 
            self.filled_rows+=1

    def get_all(self):
        """
        return a list of elements from the oldest to the newest
        """
        if self.filled_rows < self.rows:
            return np.roll(self._data, -(self.curr_pos + self.rows - self.filled_rows),
                           axis=0)[:self.filled_rows,:]
        else:
            # The buffer has fewer lines in this case
            return np.roll(self._data, -self.curr_pos,
                           axis=0)

    def get_partial(self, at=0):
        # Return last item 
        return self._data[(self.curr_pos-1 + at) % self.rows]
        
    def len(self,affichage=False):    ## donne le nombre de donnees chargees
        Taille=0
        for j,i in enumerate(self._data):
            if(np.all(i==0)==False):
                Taille+=1
        if(affichage==True):
            print(Taille)
        return Taille
            
    def __getitem__(self, key):
        """
        get element
        DEPRECATED
        """
        return self._data[key]

    def __repr__(self):
        """
        return string representation
        """
        s = self._data.__repr__()
        s = s + '\npointer: ' + str(self.curr_pos)
        s = s + '\nsize ({},{})'.format(self.rows, self.cols)
        return s

