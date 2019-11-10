import reports


def get_text_for_count_games(file_name):
    return str(reports.count_games(file_name))


def get_text_for_decide(file_name):
    input_year = int(input("Enter a year: "))
    return str(reports.decide(file_name, input_year))


def get_text_for_latest_title(file_name):
    return str(reports.get_latest(file_name))   


def get_text_for_count_by_genre(file_name):
    genre = input("Enter a genre: ")
    return str(reports.count_by_genre(file_name, genre))


def get_text_for_line_number_by_title(file_name):
    input_title = input("Enter a title: ")
    try:
        return str(reports.get_line_number_by_title(file_name, input_title))
    except ValueError:
        return "There no such title."


def get_text_for_sorted_titles(file_name):
    return ", ".join(reports.sort_abc(file_name))


def get_text_for_sorted_genre(file_name):
    return ", ".join(reports.get_genres(file_name))


def get_text_for_year_top_sold_FPS(file_name):
    try:
        return str(reports.when_was_top_sold_fps(file_name))
    except ValueError:
        return "No FPS in the data base"


def main():
    source_file_name = "game_stat.txt"
    target_file_name = "game_stat_export.txt"

    with open(target_file_name, "w+") as file:
        file.write(get_text_for_count_games(source_file_name) + "\n")
        file.write(get_text_for_decide(source_file_name) + "\n")
        file.write(get_text_for_latest_title(source_file_name) + "\n")
        file.write(get_text_for_count_by_genre(source_file_name) + "\n")
        file.write(get_text_for_line_number_by_title(source_file_name) + "\n")
        file.write(get_text_for_sorted_titles(source_file_name) + "\n")
        file.write(get_text_for_sorted_genre(source_file_name) + "\n")
        file.write(get_text_for_year_top_sold_FPS(source_file_name) + "\n")


if __name__ == "__main__":
    main()
