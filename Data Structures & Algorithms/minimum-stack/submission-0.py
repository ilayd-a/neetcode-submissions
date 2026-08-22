class MinStack:

    def __init__(self):
        self.data = []
        self.mins = []

        self.n = 0

    def push(self, val: int) -> None:
        self.data.append(val)
        if len(self.mins)==0 or self.mins[-1]>=val:
            self.mins.append(val)

        self.n+=1

    def pop(self) -> None:
        if self.mins[-1]==self.data[-1]:
            self.mins.pop()
        self.data.pop()

        self.n-=1

    def top(self) -> int:
        return self.data[-1]

    def getMin(self) -> int:
        return self.mins[-1]
