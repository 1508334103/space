import collections

# namedtuple是collections模块中的工厂函数，用于生成类似于元组的对象。
# 用于构建只有少数属性但是没有方法的对象
# print()会调用命名元素的默认字符串表示方法，输出格式为Card(rank="x", suit= "xxx")
Card = collections.namedtuple("Card", ["rank", "suit"])


class FrenchDeck(object):
    ranks = [str(n) for n in range(2, 11)] + list("JQKA")
    suits = "spades diamonds clubs hearts".split()
    suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

    # list.index(x) 将会返回x在列表中第一次出现位置的索引
    def spades_high(self, card):
        rank_value = FrenchDeck.ranks.index(card.rank)
        return rank_value * len(self.suit_values) + self.suit_values[card.suit]

    def __init__(self):
        self._cards = [Card(rank, suit) for rank in self.ranks for suit in self.suits]

    def __len__(self):
        return len(self._cards)

    # 使之变成可迭代对象
    def __getitem__(self, position):
        return self._cards[position]


def main():
    deck = FrenchDeck()
    for card in sorted(deck, key=deck.spades_high):
        print(card)


if __name__ == "__main__":
    main()
