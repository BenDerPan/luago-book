class LuaStack:
    MAX_STACK_SIZE = 1000

    def __init__(self):
        self.slots = []

    def top(self):
        return len(self.slots)

    def check(self, n):
        return len(self.slots) + n <= LuaStack.MAX_STACK_SIZE

    def push(self, val):
        if len(self.slots) > LuaStack.MAX_STACK_SIZE:
            raise Exception('Stack Over Flow')
        self.slots.append(val)

    def pop(self):
        ret = self.slots[-1]
        self.slots.pop()
        return ret

    def abs_index(self, idx):
        if idx >= 0:
            return idx
        return idx + len(self.slots) + 1

    def is_valid(self, idx):
        idx = self.abs_index(idx)
        return (idx > 0) and (idx <= len(self.slots))

    def get(self, idx):
        if not self.is_valid(idx):
            return None
        return self.slots[self.abs_index(idx)-1]

    def set(self, idx, val):
        if not self.is_valid(idx):
            raise Exception('Invalid Index')
        self.slots[self.abs_index(idx)-1] = val

    def reverse(self, begin, end):
        while begin < end:
            self.slots[begin], self.slots[end] = self.slots[end], self.slots[begin]
            begin += 1
            end -= 1
