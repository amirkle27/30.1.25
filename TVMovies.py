from typing import override
from TVInterface import TVInterface


class TVMovies(TVInterface):

    def __str__(self):
        return f"Movies Channel"

    @override
    def turn_on(self):
        print(f'Tv is already on and casting the {self}')
        return self

    @override
    def news_channel(self):
        from TVNews import TVNews
        print('TV has switched to the News Channel')
        return TVNews()

    @override
    def sports_channel(self):
        from TVSports import TVSports
        print('TV TV has switched to the Sports Channel')
        return TVSports()

    @override
    def movies_channel(self):
        print('TV is already casting the Movies Channel')
        return self

    @override
    def turn_off(self):
        from TVOff import TVOff
        print('TV is off')
        return TVOff(prev_state=self)
