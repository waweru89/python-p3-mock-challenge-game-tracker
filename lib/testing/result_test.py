import pytest
from classes.many_to_many import Result, Game, Player

def test_result_is_stored_in_class_attribute():
    """Results are tracked globally in a class attribute"""
    Result.all_results = []  # Reset the class attribute to an empty list
    game = Game("Skribbl.io")
    player = Player("Nick")
    result = Result(player, game, 3000)

    assert result in Result.all_results  # Check the global list
    assert len(Result.all_results) == 1  # Ensure only one result is stored
