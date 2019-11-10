import reports


def ask_integer(message):
    result = None
    while True:
        try:
            result = int(input(message))
            return result
        except ValueError:
            print("Write a number")
            continue


def print_count_games(file_name):
    number_of_games = reports.count_games(file_name)
    print(f"How many games are in the file? {number_of_games}")


def print_decide(file_name):
    input_year = ask_integer("Enter a year: ")
    is_game_from_year = reports.decide(file_name, input_year)
    print(f"Is there a game from a given year {input_year}? {is_game_from_year}")


def print_latest_title(file_name):
    latest_title = reports.get_latest(file_name)
    print(f"Which was the latest game? {latest_title}")


def print_count_by_genre(file_name):
    genre = input("Enter a genre: ")
    number_of_games_by_genre = reports.count_by_genre(file_name, genre)
    print(f"How many games do we have by genre? {number_of_games_by_genre}")


def print_line_number_by_title(file_name):
    while True:
        input_title = input("Enter a title: ")
        try:
            line_number = reports.get_line_number_by_title(file_name, input_title)
            break
        except ValueError:
            print("There no such title")
            continue
    print(f"What is the line number of the given game (by title)? {line_number}")


def print_sorted_titles(file_name):
    sorted_titles = "\n".join(reports.sort_abc(file_name))
    print(f"What is the alphabetical ordered list of the titles?\n{sorted_titles}")


def print_sorted_genre(file_name):
    sorted_genre = "\n".join(reports.get_genres(file_name))
    print(f"What are the genres?\n{sorted_genre}")

def print_year_top_sold_FPS(file_name):
    try:
        year_of_top_sold_fps = reports.when_was_top_sold_fps(file_name)
    except ValueError:
        year_of_top_sold_fps = "No FPS in the data base"
    print(f'What is the release date of the top sold "First-person shooter" game? {year_of_top_sold_fps}')


def main():
    while True:
        file_name = input("File source: ")  # game_stat.txt
        try:
            print_count_games(file_name)
            print_decide(file_name)
            print_latest_title(file_name)
            print_count_by_genre(file_name)
            print_line_number_by_title(file_name)
            print_sorted_titles(file_name)
            print_sorted_genre(file_name)
            print_year_top_sold_FPS(file_name)
            break
        except FileNotFoundError:
            print("No file found")
            continue


if __name__ == "__main__":
    main()