# Open file
def get_tabel(file_name):
    tabel = []
    with open(file_name, "r") as file:
        for line in file:
            columns = line.split('\t')
            columns_names = {
                "title": columns[0],
                "copies": columns[1],
                "year": columns[2],
                "genre": columns[3],
                "publisher": columns[4]
            }
            tabel.append(columns_names)
    return tabel


# How many games are in the file
def count_games(file_name):
    return len(get_tabel(file_name))


# Is there a game from a given year?
def decide(file_name, year):
    for row in get_tabel(file_name):
        if int(row["year"]) == year:
            return True
    return False


# Which was the latest game?
def get_latest(file_name):
    max_year = get_tabel(file_name)[0]["year"]
    latest_title = None
    for row in get_tabel(file_name):
        actual_year = row["year"]
        if actual_year > max_year:
            max_year = actual_year
            latest_title = row["title"]
    return latest_title

def count_by_genre(file_name, genre):
    counter = 0
    for row in get_tabel(file_name):
        if row["genre"] == genre:
            counter += 1
    return counter


def get_line_number_by_title(file_name, title):
    counter = 0
    for row in get_tabel(file_name):
        counter += 1
    if row['title'] == title:
        return counter
    raise ValueError("No such game!")

# Bonus Function
def sort_abc(file_name):
    tabel = get_tabel(file_name)
    for row in tabel:
        for i in range(len(tabel - 1)


