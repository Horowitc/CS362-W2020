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
        self.player.actions = 1
        self.player.buys = 1
        self.player.purse = 1

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
        self.player.hand = [action] * 1

        # Test Action card use
        action.use(self.player, self.trash)
        self.assertIn(action, self.player.played)
        self.assertNotIn(action, self.player.hand)

        # Test Action card augment
        action.augment(self.player)
        self.assertEqual(3, self.player.actions)
        self.assertEqual(2, self.player.buys)
        self.assertEqual(2, self.player.purse)

    def test_Player(self):
        #Test Player action balance function
        balance = self.player.action_balance()
        self.assertEqual(0.0, balance)

        #Test Player calculate points function
        tally = self.player.calcpoints()
        self.assertEqual(3, tally)

        #Test Player draw function
        newcard = self.player.draw()
        self.assertIn(newcard, self.player.hand)



    def test_react(self):
        pass
