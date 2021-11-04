import mysql.connector
import bcrypt


class InvalidCredentialsError(Exception):
    pass


class NoUserFoundError(Exception):
    pass


class UserExistError(Exception):
    pass


class UsernameExistError(Exception):
    pass


class DatabaseFilm:
    def __init__(self):
        self._mydb = mysql.connector.connect(host='103.82.242.16', port='5555', user='karel', passwd='32373')
        self._cursor = self._mydb.cursor(buffered=True)
        self._cursor.execute('use karel_bondan')
        self._current_user = None

    def getCurrentUser(self):
        return self._current_user

    def getTable(self):
        self._cursor.execute('show tables;')
        return self._cursor

    def getAllMovie(self, sort_by: str):
        if sort_by == 'Name':
            self._cursor.execute('select * from Movies order by movieName')
        elif sort_by == 'Ratings (Worst-Best)':
            self._cursor.execute('select * from Movies order by ratings')
        else:
            self._cursor.execute('select * from Movies order by ratings desc')
        return self._cursor

    def getMovie(self, movie_name: str, synopsis: str, year: int):
        self._cursor.execute(
            f"select * from Movies where (movieName='{movie_name}' and synopsis='{synopsis}' and year='{year}')")
        return self._cursor

    def getPoster(self, movie_name: str, synopsis: str):
        self._cursor.execute(f"select posterUrl from Movies where movieName='{movie_name}' and synopsis='{synopsis}'")
        return self._cursor

    def getReview(self, movie_id: int):
        self._cursor.execute(f"select * from Review where movieID='{movie_id}'")
        return list(self._cursor)

    def getIndividualReview(self, user_id: int):
        self._cursor.execute(f"select * from Review where userID={user_id}")
        return list(self._cursor)

    def getUser(self, user_id: int):
        self._cursor.execute(f"select userName from Users where userID={user_id}")
        return list(self._cursor)

    def publishRatings(self, movieID: int, userID: int, movieName: str, reviewDesc: str, ratings: int):
        try:
            self._cursor.execute(f"insert into Review(movieID, userID, movieName, dateReviewed, reviewDesc, ratings)"
                                 f"values ({movieID}, {userID}, '{movieName}', CURDATE(), '{reviewDesc}', {ratings})")
            self._mydb.commit()
            self._cursor.execute(f"call get_ratings({movieID})")
            self._mydb.commit()
            return True
        except:
            return False

    # temp
    def updatePassword(self, hashed_password):
        self._cursor.execute(f"update Users set password='{hashed_password}' where userID=9")
        self._mydb.commit()

    def getPassword(self, useremail: str):
        self._cursor.execute(f"select password from Users where userName='{useremail}' or email='{useremail}'")
        return self._cursor

    def register(self, username: str, email: str, firstname: str, lastname: str, password: str):
        self._cursor.execute(f"select * from Users where email='{email}'")
        if len(list(self._cursor)) == 0:
            self._cursor.execute(f"select * from Users where userName='{username.lower()}'")
            if len(list(self._cursor)) == 0:
                hashed_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode('utf-8')
                self._cursor.execute(
                    f"insert into Users(userName, email, firstName, lastName, dateRegistered, password)"
                    f"values ('{username}', '{email}', '{firstname}', '{lastname}', CURDATE(), '{hashed_pw}')")
                self._mydb.commit()
                return True
            else:
                raise UsernameExistError()
        else:
            raise UserExistError()

    def login(self, useremail: str, password: str):
        self._cursor.execute(f"select * from Users where userName='{useremail}' or email='{useremail}'")
        user_exist = list(self._cursor)
        if len(user_exist) == 0:
            raise NoUserFoundError()
        else:
            if bcrypt.checkpw(password.encode(), list(user_exist)[0][-1].encode()):
                self._current_user = user_exist
                return user_exist
            else:
                raise InvalidCredentialsError()

    def logout(self):
        self._current_user = None
        return True

    def deleteAccount(self):
        self._cursor.execute(f"delete from Users where userID={self._current_user[0]}")
        return True

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

# a = DatabaseFilm()
# a.publishRatings(4, 6, 'httyd', 'this movie is amazing and spectacular', 9)

# password = b'rawr2021'
# aa = bcrypt.gensalt()
# hashed = bcrypt.hashpw(password, aa)
#
# print(hashed.decode('utf-8'))
# a.updatePassword(hashed.decode('utf-8'))

# try:
#     b = a.login('daixiez1', 'thisispassword')
#     print("logged in!")
# except InvalidCredentialsError:
#     print('please check your credentails')
# except NoUserFoundError:
#     print('no user found. please register first')

# passwords:
# xiez = thisispassword
# daiko = password123
# boris = iamboris2021
# drazeros = rawr2021
# karelbondan = amazing1
