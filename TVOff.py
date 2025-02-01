from typing import override
from TVInterface import TVInterface

from typing import override
from TVInterface import TVInterface


class TVOff(TVInterface):

    @override
    def __init__(self, prev_state:TVInterface = None):
            self.prev_state = prev_state

    @override
    def turn_on(self):
        from TVOn import TVOn
        print(f'Tv is on and casting the {self.prev_state}')
        return self.prev_state

    @override
    def news_channel(self):
        from TVNews import TVNews
        print('TV has switched to the News Channel')
        return TVNews()

    @override
    def sports_channel(self):
        from TVSports import TVSports
        print('TV has switched to the Sports Channel')
        return TVSports()

    @override
    def movies_channel(self):
        from TVMovies import TVMovies
        print('TV has switched to the Movies Channel')
        return TVMovies()

    @override
    def turn_off(self):
        print('TV is already off')
        return self



