import pytest
from classes.many_to_many import Player, Game, Result


class TestPlayer:
    """Test cases for Player class"""

    def test_has_username(self):
        """Player is initialized with a username"""
        player = Player("Sam")
        assert player.username == "Sam"

    def test_username_is_mutable_string(self):
        """Username is mutable and must be a string"""
        player = Player("Sam")
        assert isinstance(player.username, str)

        player.username = "NewName"
        assert player.username == "NewName"

        with pytest.raises(TypeError):
            player.username = 123

    def test_player_has_many_results(self):
        """Player has many results"""
        game = Game("Skribbl.io")
        player = Player("Sam")
        result_1 = Result(player, game, 2000)
        result_2 = Result(player, game, 3500)

        assert len(player.results()) == 2
        assert result_1 in player.results()
        assert result_2 in player.results()

    def test_player_has_many_games(self):
        """Player has many games"""
        game_1 = Game("Skribbl.io")
        game_2 = Game("Codenames")
        player = Player("Nick")
        Result(player, game_1, 5000)
        Result(player, game_2, 2000)

        assert game_1 in player.games_played()
        assert game_2 in player.games_played()

    def test_player_game_count(self):
        """Player knows how many times a game has been played"""
        game = Game("Skribbl.io")
        player = Player("Nick")
        Result(player, game, 5000)
        Result(player, game, 2000)

        assert player.num_times_played(game) == 2
