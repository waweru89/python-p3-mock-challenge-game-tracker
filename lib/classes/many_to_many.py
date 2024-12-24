class Game:
    def __init__(self, title):
        if not isinstance(title, str) or not title:
            raise ValueError("Title must be a non-empty string.")
        self._title = title
        self._results = []

    @property
    def title(self):
        return self._title

    def results(self):
        """Return all results associated with this game."""
        return self._results

    def players(self):
        """Return a list of unique players associated with this game."""
        return list({result.player for result in self._results})

    def average_score(self, player):
        """Calculate the average score of a player for this game."""
        scores = [result.score for result in self._results if result.player == player]
        return sum(scores) / len(scores) if scores else 0


class Player:
    def __init__(self, username):
        if not isinstance(username, str) or not (2 <= len(username) <= 16):
            raise ValueError("Username must be a string of length 2-16.")
        self._username = username
        self._results = []

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, new_username):
        if not isinstance(new_username, str):
            raise TypeError("Username must be a string.")
        if not (2 <= len(new_username) <= 16):
            raise ValueError("Username must be a string of length 2-16.")
        self._username = new_username

    def results(self):
        """Return all results associated with this player."""
        return self._results

    def games_played(self):
        """Return a list of unique games played by this player."""
        return list({result.game for result in self._results})

    def num_times_played(self, game):
        """Return the number of times this player has played the given game."""
        return len([result for result in self._results if result.game == game])


class Result:
    all_results = []  # Renamed to avoid conflict with method name

    def __init__(self, player, game, score):
        if not isinstance(score, int) or not (1 <= score <= 5000):
            raise ValueError("Score must be an integer between 1 and 5000 inclusive.")
        self.player = player
        self.game = game
        self.score = score

        # Link result to player and game
        player._results.append(self)
        game._results.append(self)
        Result.all_results.append(self)  # Append to the global list

    @classmethod
    def get_all(cls):
        """Return all result instances."""
        return cls.all_results
