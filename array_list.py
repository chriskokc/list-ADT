# List ADT
# Fixed-size array implementation


class List:
    def __init__(self, size):
        self.size = size
        self.length = 0
        self.items = [None for i in range(size)]

    def is_empty(self):
        return self.length == 0

    def insert_back(self, x):
        # Dynamic array implementation
        # double the size of the array when it is full
        if self.length == self.size:
            self.items += [None for i in range(self.size)]
            self.size *= 2
        self.items[self.length] = x
        self.length += 1

    def insert_front(self, x):
        map = {}
        if self.length < self.size:
            for i in range(0, self.size):
                map[i+1] = self.items[i]
            self.items[0] = x
            for i in range(1, self.size):
                self.items[i] = map[i]
            self.length += 1
        else:
            print("The array is full")

    def insert_at(self, x, pos):
        map = {}
        if self.length < self.size:
            if pos <= self.length:
                for i in range(pos, self.size):
                    map[i+1] = self.items[i]
                self.items[pos] = x
                for i in range(pos+1, self.size):
                    self.items[i] = map[i]
                self.length += 1
            else:
                print(f"You only have {self.length} items so far")
        else:
            print("The array is full")

    def remove_at(self, pos):
        map = {}
        if not self.is_empty():
            for i in range(pos+1, self.size):
                map[i-1] = self.items[i]
            for i in range(pos, self.size-1):
                self.items[i] = map[i]
            self.items[self.size-1] = None
            self.length -= 1
        else:
            print("The array is empty")

    def get_item(self, index):
        return self.items[index]

    def update_item(self, index, x):
        self.items[index] = x

    def search(self, x):
        return x in self.items


