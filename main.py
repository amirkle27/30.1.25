from TVInterface import TVInterface
from TVMovies import TVMovies
from TVNews import TVNews
from TV_state_pattern import Context
tv_state = Context(TVMovies())

if __name__ == "__main__":

    tv_state.turn_off()

    tv_state.turn_on()

    tv_state.turn_off()

    tv_state.turn_on()

    tv_state.sports_channel()

    tv_state.sports_channel()

    tv_state.turn_off()

    tv_state.turn_on()

    tv_state.movies_channel()

    tv_state.turn_off()

    tv_state.turn_on()

    tv_state.news_channel()

    tv_state.turn_off()

    tv_state.turn_on()