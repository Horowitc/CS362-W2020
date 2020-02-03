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

    def test_action_init(self):
        cost = 2
        actions = 3
        cards = 5
        buys = 2
        coins = 3
        action = Dominion.Action_card(self.player.name, cost, actions, cards, buys, coins)
        self.assertEqual(cost, action.cost)
        self.assertEqual(actions, action.actions)
        self.assertEqual(cards, action.cards)
        self.assertEqual(buys, action.buys)
        self.assertEqual(coins, action.coins)
        # Test Action card intialization number 2
        cost = 1
        actions = 1
        cards = 1
        buys = 1
        coins = 1
        action = Dominion.Action_card(self.player.name, cost, actions, cards, buys, coins)
        self.assertEqual(cost, action.cost)
        self.assertEqual(actions, action.actions)
        self.assertEqual(cards, action.cards)
        self.assertEqual(buys, action.buys)
        self.assertEqual(coins, action.coins)

    def test_use(self):
        action = Dominion.Action_card(self.player.name, 1, 1, 1, 1, 1)
        self.player.hand = [action] * 1
        # Test Action card use
        action.use(self.player, self.trash)
        self.assertIn(action, self.player.played)
        self.assertNotIn(action, self.player.hand)

    def test_augment(self):
        action = Dominion.Action_card(self.player.name, 1, 1, 1, 1, 1)
        self.player.hand = [action] * 1
        # Test Action card augment
        action.augment(self.player)
        self.assertEqual(2, self.player.actions)
        self.assertEqual(2, self.player.buys)
        self.assertEqual(2, self.player.purse)



    def test_action_balance(self):
        #Test Player action balance function 1
        self.player.deck = [Dominion.Militia()]*2
        balance = self.player.action_balance()
        self.assertEqual(-20, balance)

        # Test Player action balance function 2
        self.player.deck = [Dominion.Festival()] * 2
        balance = self.player.action_balance()
        self.assertEqual(20, balance)

    def test_calcpoints(self):
        #Test Player calculate points function 1
        self.player.deck = [Dominion.Duchy()] * 1
        self.player.hand = [Dominion.Copper()] * 1
        tally = self.player.calcpoints()
        self.assertEqual(3, tally)

        # Test Player calculate points function 2
        self.player.deck = [Dominion.Duchy()] * 2 + [Dominion.Gardens()]*1
        self.player.hand = [Dominion.Copper()] * 2
        tally = self.player.calcpoints()
        self.assertEqual(6, tally)

    def test_draw(self):
        #Test Player draw function 1
        self.player.hand = [Dominion.Duchy()]*1
        self.player.deck = [Dominion.Cellar()]*1
        newcard = self.player.draw()
        self.assertNotIn(newcard, self.player.deck)
        self.assertIn(newcard, self.player.hand)
        self.assertEqual(newcard, self.player.hand[1])

        # Test Player draw function 2
        self.player.hand = [Dominion.Estate()] * 1
        self.player.deck = [Dominion.Militia()] * 1
        newcard = self.player.draw()
        self.assertNotIn(newcard, self.player.deck)
        self.assertIn(newcard, self.player.hand)
        self.assertEqual(newcard, self.player.hand[1])

        # Test Player draw function 3
        self.player.hand = [Dominion.Estate()] * 1
        self.player.deck = []
        newcard = self.player.draw()
        self.assertNotIn(newcard, self.player.deck)


    def test_card_summary(self):
        # Test Player card summary function 1
        self.player.deck = [Dominion.Duchy()]*1
        self.player.hand = [Dominion.Copper()]*2
        summary = self.player.cardsummary()
        self.assertEqual(1, summary['Duchy'])
        self.assertEqual(2, summary['Copper'])
        self.assertEqual(3, summary['VICTORY POINTS'])

        # Test Player card summary function 2
        self.player.deck = [Dominion.Estate()] * 2
        self.player.hand = [Dominion.Silver()] * 1
        summary = self.player.cardsummary()
        self.assertEqual(2, summary['Estate'])
        self.assertEqual(1, summary['Silver'])
        self.assertEqual(2, summary['VICTORY POINTS'])

    def test_game_over(self):
        #Test game over function 1
        self.supply["Province"] = [Dominion.Province()] * 1
        gover =Dominion.gameover(self.supply)
        self.assertEqual(gover, False)

        # Test game over function 2
        self.supply["Province"] = [Dominion.Province()] * 0
        gover = Dominion.gameover(self.supply)
        self.assertEqual(gover, True)

        # Test gameover function 3
        self.supply["Province"] = [Dominion.Province()] * 1
        self.supply["Copper"] = [Dominion.Copper()] * 0
        self.supply["Silver"] = [Dominion.Silver()] * 0
        self.supply["Gold"] = [Dominion.Gold()] * 0
        gover = Dominion.gameover(self.supply)
        self.assertEqual(gover, True)




    def test_react(self):
        pass
