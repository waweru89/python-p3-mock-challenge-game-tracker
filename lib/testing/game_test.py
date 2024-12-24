import pytest
from classes.many_to_many import Game, Player, Result


class TestGame:
    """Test cases for Game class"""

    def test_has_title(self):
        """Game is initialized with a title"""
        game_1 = Game("Skribbl.io")
        game_2 = Game("Jenga")

        assert game_1.title == "Skribbl.io"
        assert game_2.title == "Jenga"

    def test_title_is_immutable_string(self):
        """Title is an immutable string"""
        game = Game("Skribbl.io")
        assert isinstance(game.title, str)

        with pytest.raises(AttributeError):
            game.title = "New Title"

    def test_title_length(self):
        """Title is greater than 0 characters"""
        game = Game("Skribbl.io")
        assert len(game.title) > 0

        with pytest.raises(ValueError):
            Game("")

    def test_game_has_many_results(self):
        """Game has many results"""
        game = Game("Skribbl.io")
        player = Player("Sam")
        result_1 = Result(player, game, 2000)
        result_2 = Result(player, game, 3500)

        assert len(game.results()) == 2
        assert result_1 in game.results()
        assert result_2 in game.results()

    def test_game_has_many_players(self):
        """Game has many unique players"""
        game = Game("Skribbl.io")
        player_1 = Player("Nick")
        player_2 = Player("Ari")
        Result(player_1, game, 5000)
        Result(player_2, game, 4500)

        assert len(game.players()) == 2
        assert player_1 in game.players()
        assert player_2 in game.players()

    def test_game_average_score(self):
        """Game calculates average score of a player"""
        game = Game("Skribbl.io")
        player = Player("Nick")
        Result(player, game, 2000)
        Result(player, game, 4000)

        assert game.average_score(player) == 3000
