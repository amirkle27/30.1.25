from typing import override
from TVInterface import TVInterface


class TVNews(TVInterface):

    def __str__(self):
        return f"News Channel"

    @override
    def turn_on(self):

        print(f'Tv is already on and casting the {self}')
        return self

    @override
    def news_channel(self):
        print('TV is already casting the News Channel')
        return self

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



