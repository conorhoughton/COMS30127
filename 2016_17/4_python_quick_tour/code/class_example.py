class Counter:

    def __init__(self,value):
        self.value=value

    def add(self,increment):
        self.value+=increment

counter=Counter(5)

print counter.value

counter.add(7)

print counter.value

counter.value+=3

print counter.value
