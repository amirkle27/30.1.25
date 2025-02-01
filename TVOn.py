from typing import override
from TVInterface import TVInterface


class TVOn(TVInterface):
    def __init__ (self, prev_state: TVInterface):
        self.prev_state = prev_state

    @override
    def turn_on(self):
        print(f'Tv is already on casting the {self}')
        return self
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
        from TVOff import TVOff
        print('TV is off')
        return TVOff(prev_state=self)



