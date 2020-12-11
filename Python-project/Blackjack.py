from random import shuffle

SUITS = ("Kier", "Karo", "Pik", "Trefl")
RANKS = (
    "Dwójka",
    "Trójka",
    "Czwórka",
    "Piątka",
    "Szóstka",
    "Siódemka",
    "Ósemka",
    "Dziewiątka",
    "Dziesiątka",
    "Jopek",
    "Dama",
    "Król",
    "As",
)
VALUES = {
    "Dwójka": 2,
    "Trójka": 3,
    "Czwórka": 4,
    "Piątka": 5,
    "Szóstka": 6,
    "Siódemka": 7,
    "Ósemka": 8,
    "Dziewiątka": 9,
    "Dziesiątka": 10,
    "Jopek": 10,
    "Dama": 10,
    "Król": 10,
    "As": 11,
}


class BrakKart(Exception): pass


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        name = " ".join((self.rank, self.suit))
        return "|{0:^18}|".format(name)


class Deck:

    def __init__(self):
        self.deck = []
        for suit in SUITS:
            for rank in RANKS:
                self.deck.append(Card(suit, rank))

    def shuffle(self):
        if len(self.deck) > 1:
            shuffle(self.deck)

    def deal_card(self):
        if len(self.deck) > 1:
            return self.deck.pop()
        else:
            raise BrakKart


class Competitor:

    def __init__(self, dealer=False):
        self.dealer = dealer
        self.cards = []
        self.value = 0

    def add_card(self, card):
        self.cards.append(card)

    def throw_cards(self):
        self.cards.clear()

    def calculate_value(self):
        self.value = 0
        has_ace = False
        for card in self.cards:
            self.value += int(VALUES.get(card.rank))
            if VALUES.get(card.rank) == 11:
                has_ace = True

        if has_ace and self.value > 21:
            self.value -= 10

    def get_value(self):
        self.calculate_value()
        return self.value

    def display(self, endgame=False):
        if self.dealer and not endgame:
            print("Ręka krupiera:")
            print("|{0:^18}|".format("Ukryta Karta"))
            print(self.cards[1])
            print()
        elif endgame:
            print("Ręka krupiera:")
            for card in self.cards:
                print(card)
            print("Wynik:", self.get_value())
            print()
        else:
            print("Twoja ręka:")
            for card in self.cards:
                print(card)
            print("Wynik:", self.get_value())
            print()


class Game:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()

        self.player = Competitor()
        self.dealer = Competitor(dealer=True)

    def player_is_over(self):
        return self.player.get_value() >= 21

    def give_card(self, dealer=False):
        try:
            if dealer:
                self.dealer.add_card(self.deck.deal_card())
            else:
                self.player.add_card(self.deck.deal_card())
        except BrakKart:
            self.deck = Deck()
            if dealer:
                self.dealer.add_card(self.deck.deal_card())
            else:
                self.player.add_card(self.deck.deal_card())

    def play(self):
        playing = True
        print("--- Witaj w kasynie! ---")
        while playing:
            for i in range(2):
                self.give_card()
                self.give_card(True)

            self.player.display()
            print()
            self.dealer.display()

            if not self.player_is_over():
                choice = input("Wybierz co robisz [Dobieram / Pasuje] ").lower()
                while choice not in ["d", "p", "dobieram", "pasuje"]:
                    choice = input("Wpisz 'dobieram' lub 'pasuje' (albo D/P) ").lower()
                while choice in ['dobieram', 'd']:
                    self.give_card()
                    self.player.display()
                    if self.player_is_over():
                        choice = "p"
                    else:
                        choice = input("Wpisz 'dobieram' lub 'pasuje' (albo D/P) ").lower()
                        while choice not in ["d", "p", "dobieram", "pasuje"]:
                            choice = input("Wpisz 'dobieram' lub 'pasuje' (albo D/P) ").lower()

            player_hand_value = self.player.get_value()
            dealer_hand_value = self.dealer.get_value()

            print("---Wyniki Końcowe---")
            print()
            self.player.display()
            self.dealer.display(True)

            if 22 > player_hand_value > dealer_hand_value:
                print("Wygrywasz!")
                print("-----------------------------------")
            elif player_hand_value == dealer_hand_value:
                print("Remis!")
                print("-----------------------------------")
            else:
                print("Krupier Wygrywa!")
                print("-----------------------------------")

            self.dealer.throw_cards()
            self.player.throw_cards()

            again = input("Czy chcesz zagrać ponownie? [T/N] ")
            while again.lower() not in ["t", "n"]:
                again = input("Wybierz T lub N ")
            if again.lower() == "n":
                print("--- Kasyno dziękuje za wizytę! ---")
                playing = False


if __name__ == "__main__":
    game = Game()
    game.play()
