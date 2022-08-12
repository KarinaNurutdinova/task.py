import pytest

from Player import Player


class TestPlayer:

    def test_change_name(self):
        player = Player("Karina")
        player.change_name("Alina")
        assert player.name == "Alina", "Ошибка в имени"

    def test_add_points(self):
        player = Player("Alina")
        player.add_points(4)
        assert player.points == 4, "Ошибка в вычислениях"

    def test_get_points(self):
        player = Player("Alina")
        assert player.get_points() == 0, "Ошибка в вычислениях"


