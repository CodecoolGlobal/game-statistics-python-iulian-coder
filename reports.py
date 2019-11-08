# Open file
def get_tabel(file_name):
    tabel = []
    with open(file_name, "r") as file:
        for line in file:
            colums = line.split('\t')
            tabel.append(colums)
    return tabel


# How many games are in the file
def count_games(file_name):
    return len(get_tabel(file_name))


# Is there a game from a given year?
def decide(file_name, year):
    for row in get_tabel(file_name):
        if int(row[2]) == year:
            return True
    return False

def get_latest(file_name):
    max_year = get_latest(file_name)[0][2]
    







