class Hand:
    def __init__(self,cards,bid):
        self.cards = cards
        self.bid = bid
        self.type = 0
        self.score = 0
        self.order = 'AKQJT98765432'

    def determineType(self):
        occurs = [0] * len(self.order)

        for c in self.cards:
            n = self.order.find(c)
            occurs[n] = occurs[n] + 1
        
        #AAAAA
        if 5 in occurs:
            self.type = 6
            return
        
        #AAAAK
        if 4 in occurs:
            self.type = 5
            return
        
        if 3 in occurs:
            #AAAKK
            if 2 in occurs:
                self.type = 4
                return
            #AAAKQ
            else:
                self.type = 3
                return
        #AAKKQ
        if occurs.count(2) == 2:
            self.type = 2
            return
        
        #AAKQT
        if occurs.count(2) == 1:
            self.type = 1
            return
    
    def calculateScore(self):
        base = len(self.order)

        self.score = self.score + (base**5) * self.type
        self.score = self.score + (base**4) * self.order[::-1].find(self.cards[0])
        self.score = self.score + (base**3) * self.order[::-1].find(self.cards[1])
        self.score = self.score + (base**2) * self.order[::-1].find(self.cards[2])
        self.score = self.score + (base**1) * self.order[::-1].find(self.cards[3])
        self.score = self.score + (base**0) * self.order[::-1].find(self.cards[4])


def main():
    f = open("day07/data.input", "r")
    Lines = f.readlines()

    hands = []

    for line in Lines:
        line = line.split(" ")
        hands.append(Hand(line[0], int(line[1])))

        hands[-1].determineType()
        hands[-1].calculateScore()


    Scores = [0] * len(hands)
    Bids = [0] * len(hands)

    for i in range(len(hands)):
        Scores[i] = hands[i].score
        Bids[i] = hands[i].bid


    zipped_lists = zip(Scores, Bids)

    sorted_pairs = sorted(zipped_lists)

    res = [[i for i, j in sorted_pairs],
       [j for i, j in sorted_pairs]]

    Bids = res[1]

    out = 0
    for i in range(len(Bids)):
        out = out + (i+1)*Bids[i]

    print(out)

if __name__ == '__main__':
    main()
