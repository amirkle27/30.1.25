from typing import override
from TVInterface import TVInterface


class TVSports(TVInterface):

    def __str__(self):
        return f"Sports Channel"

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
        print('TV is already casting the Sports Channel')
        return self

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



