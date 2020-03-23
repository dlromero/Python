

class Swan:

    def __init__(self, is_turned_on):
        self._is_week_up = True

    def grans_on(self):
        self._is_grans = True
        self._is_week_up = self._is_grans

    def grans_off(self):
        self._is_grans = False
        self._is_week_up = self._is_grans

    def dead_on(self):
        self._is_dead = False
        self._is_week_up = self._is_dead

    def dead_off(self):
        self._is_dead = True
        self._is_week_up = self._is_dead

