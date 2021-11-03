import mysql.connector


class DatabaseFilm:
    # constructor
    def __init__(self):
        self._mydb = mysql.connector.connect(host='103.82.242.16', port='5555', user='karel', passwd='32373')
        self._cursor = self._mydb.cursor()
        self._cursor.execute('use karel_bondan')

    def getTable(self):
        self._cursor.execute('show tables;')
        return self._cursor

    def getMovie(self, sortBy):
        if sortBy == 'Name':
            self._cursor.execute('select * from Movies order by movieName')
        elif sortBy == 'Ratings (Worst-Best)':
            self._cursor.execute('select * from Movies order by ratings')
        else:
            self._cursor.execute('select * from Movies order by ratings desc')
        return self._cursor

    def getPoster(self, movie_name: str, synopsis: str):
        self._cursor.execute(f"select posterUrl from Movies where movieName='{movie_name}' and synopsis='{synopsis}'")
        return self._cursor

# a = DatabaseFilm()
# b = user.User('lizard', 'lizard@email.com', 'lizardo', 'milos', '2021-10-31')
# print(b.username)
#
# for i in a.getMovie():
#     print(i)
#
# for i in a.getPoster('Onward', 'Two elven brothers embark on a quest to bring their father back for one day.'):
#     print(i)
#
# print([i[0] for i in a.getPoster('Onward', 'Two elven brothers embark on a quest to bring their father back for one day.')][-1])

