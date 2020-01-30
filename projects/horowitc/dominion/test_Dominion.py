from unittest import TestCase
import testUtility
import Dominion


class TestCard(TestCase):
    def setUp(self):
        self.player_names = ["Ann", "*Ben", "*Carla"]
        self.players = testUtility.GetPlayers(self.player_names)
        self.nV = testUtility.GetVictoryCards(self.player_names)
        self.nC = -10 + 10 * len(self.player_names)
        self.box = testUtility.GetBox(self.nV)
        self.supply_order = testUtility.GetSupplyOrder()
        self.boxlist = testUtility.GetBoxList(self.box)
        self.random10 = self.boxlist[:10]
        self.supply = testUtility.GetSupply(self.box, self.random10, self.player_names, self.nV, self.nC)
        self.trash = []
        self.player = Dominion.Player('Annie')

    def test_init(self):
        self.setUp()

    def test_Action(self):
        # Test Action card intialization number 1
        cost = 1
        actions = 2
        cards = 1
        buys = 1
        coins = 1
        action = Dominion.Action_card(self.player.name, cost, actions, cards, buys, coins)
        self.assertEqual(cost, action.cost)
        self.assertEqual(actions, action.actions)
        self.assertEqual(cards, action.cards)
        self.assertEqual(buys, action.buys)
        self.assertEqual(coins, action.coins)

    def test_react(self):
        pass
