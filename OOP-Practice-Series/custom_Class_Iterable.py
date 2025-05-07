class Countdown:
    def __init__(self, start):
        self.current = start  # Countdown ka current number set karte hain

    def __iter__(self):
        return self  # Iterable object return karte hain (usually self)

    def __next__(self):
        if self.current < 0:
            raise StopIteration  # Jab 0 se neeche aa jaaye, to loop stop kar dete hain
        else:
            value = self.current  # Current value ko save karte hain
            self.current -= 1     # Current ko 1 se decrease karte hain
            return value          # Current value return karte hain
# Object banaya jisme countdown 5 se start hoga
count = Countdown(5)

# Countdown object ko for loop mein use kiya
for num in count:
    print(num)
