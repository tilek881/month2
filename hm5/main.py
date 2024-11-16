from game_pack.logic import play_game
from decouple import config


def main():
        min_number = config("min_number", cast=int)
        max_number = config("max_number", cast=int)
        attempts = config("attempts", cast=int)
        start_capital = config("start_capital", cast=int)

        play_game(min_number, max_number, attempts, start_capital)


if __name__ == "__main__":
    main()
