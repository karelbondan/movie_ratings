import mysql.connector
import bcrypt
import threading
import time


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

    def refresh(self):
        if not self._mydb.is_connected():
            self._mydb = mysql.connector.connect(host='103.82.242.16', port='5555', user='karel', passwd='32373')
            self._cursor = self._mydb.cursor(buffered=True)
            self._cursor.execute('use karel_bondan')

    def getCurrentUser(self):
        return self._current_user

    def getTable(self):
        self.refresh()
        self._cursor.execute('show tables;')
        return self._cursor

    def getAllMovie(self, sort_by: str):
        self.refresh()
        if sort_by == 'Name':
            self._cursor.execute('select * from Movies order by movieName')
        elif sort_by == 'Ratings (Worst-Best)':
            self._cursor.execute('select * from Movies order by ratings')
        else:
            self._cursor.execute('select * from Movies order by ratings desc')
        return self._cursor

    def _getAllMovie(self):
        self.refresh()
        self._cursor.execute('select * from Movies order by movieName')
        return self._cursor

    def getMovie(self, movie_name: str, synopsis: str, year: int):
        self.refresh()
        self._cursor.execute(
            f"select * from Movies where (movieName='{movie_name}' and synopsis='{synopsis}' and year='{year}')")
        return self._cursor

    def getMovieByID(self, movie_id: int):
        self._cursor.execute(f"select * from Movies where movieID={movie_id}")
        return list(self._cursor)

    def getMovieName(self, movie_id: int):
        self._cursor.execute(f"select movieName from Movies where movieID={movie_id}")
        return list(self._cursor)

    def getPoster(self, movie_name: str, synopsis: str):
        self._cursor.execute(f"select posterUrl from Movies where movieName='{movie_name}' and synopsis='{synopsis}'")
        return self._cursor

    def getReview(self, movie_id: int):
        self.refresh()
        self._cursor.execute(f"select * from Review where movieID='{movie_id}'")
        return list(self._cursor)

    def getMyReview(self, user_id: int):
        self.refresh()
        self._cursor.execute(f"select * from Review where userID={user_id}")
        return list(self._cursor)

    def getIndividualReview(self, user_id: int, movie_id: int):
        self.refresh()
        self._cursor.execute(f"select * from Review where userID={user_id} and movieID={movie_id}")
        return list(self._cursor)

    def getUser(self, user_id: int):
        self._cursor.execute(f"select userName from Users where userID={user_id}")
        return list(self._cursor)

    def publishRatings(self, movieID: int, userID: int, reviewDesc: str, ratings: int):
        try:
            print(movieID, userID, reviewDesc, ratings)
            self._cursor.execute(f"insert into Review(movieID, userID, dateReviewed, reviewDesc, ratings)"
                                 f"values ({movieID}, {userID}, curdate(), '{reviewDesc}', {ratings})")
            self._mydb.commit()
            self._updateRatings(movieID)
            self._mydb.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def updateReview(self, movieID: int, userID: int, reviewDesc: str, ratings: int):
        try:
            self._cursor.execute(
                f"update Review set reviewDesc='{reviewDesc}' where movieID={movieID} and userID={userID}")
            self._mydb.commit()
            self._cursor.execute(f"update Review set ratings='{ratings}' where movieID={movieID} and userID={userID}")
            self._mydb.commit()
            self._updateRatings(movieID)
            self._mydb.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def _getRawRating(self):
        self._cursor.execute(f"select movieID, round(avg(ratings), 1), count(ratings) from Review group by movieID")
        self._mydb.commit()
        return list(self._cursor)

    def updateSpecificMovie(self, movie_id: int):
        self._cursor.execute(f"call get_ratings({movie_id})")
        self._mydb.commit()

    def _updateRatings(self, movie_id: int):
        # get ratings is a stored procedure that updates the average ratings on the Movies table. See below
        # for more details
        self._cursor.execute(f"call get_ratings({movie_id})")
        self._mydb.commit()

    def updateRatings(self):
        # movies = list(self._getAllMovie())
        # raw = [list(self._getRawRating())]
        # raw_ids = [id[0] for id in raw]
        # for rating in movies:
        #     if rating[0] in raw_ids and (rating[-3] != raw[]):
        #         try:
        #             self._updateRatings(rating[0])
        #         except mysql.connector.errors.IntegrityError:
        #             pass
        # raw = self._getRawRating()
        # for rating in raw:
        #     movie = self.getMovieByID(rating[0])
        #     if rating[-3] != movie[0][-1]:
        #         try:
        #             self._updateRatings(rating[0])
        #         except mysql.connector.errors.IntegrityError:
        #             pass
        self._cursor.execute(f"call update_ratings()")
        self._mydb.commit()

    def deleteRatings(self, user_id: int, movie_id: int):
        try:
            self._cursor.execute(f"delete from Review where userID={user_id} and movieID={movie_id}")
            self._mydb.commit()
            self._updateRatings(movie_id)
            self._mydb.commit()
            return True
        except:
            return False

    def updatePassword(self, user_id: int, hashed_password: str):
        try:
            self._cursor.execute(f"update Users set password='{hashed_password}' where userID={user_id}")
            self._mydb.commit()
            return True
        except:
            return False

    def getPassword(self, useremail: str):
        self._cursor.execute(f"select password from Users where userName='{useremail}' or email='{useremail}'")
        self._mydb.commit()
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
        self._mydb.commit()
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

    def deleteAccount(self, user_id: int):
        try:
            # self._cursor.execute(f"delete from Users where userID={user_id}")
            # self._mydb.commit()
            self._cursor.execute(f"call delete_account({user_id})")
            self._mydb.commit()
            return True
        except:
            return False

# stored procedure details:
# get_ratings(in movieID int) procedure

# delimiter $$
# create procedure get_ratings(in movieID int)
#       begin
#           update Movies
#               set Movies.ratings = (
#                   select round(avg(ratings), 1)
#                   from Review
#                   where Review.movieID = movieID
#               )
#               where Movies.movieID = movieiD;
#           update Movies
#               set Movies.ratings = (
#                   select count(ratings)
#                   from Review
#                   where Review.movieID = movieID
#               )
#               where Movies.movieID = movieiD;
#       end$$
# delimiter ;

# update_ratings() procedure

# delimiter $$
# create procedure update_ratings()
# begin
# 	declare id int default 0;
# 	declare done int default false;
#     declare movie_IDs cursor for select movieID from Review group by movieID;
#     declare continue handler for not found set done = true;
# 	open movie_IDs;
#     loop_through_rows: loop
# 		fetch movie_IDs into id;
# 		if done then
# 		  leave loop_through_rows;
# 		end if;
#         call get_ratings(id);
# 	end loop;
#     close movie_IDs;
# end$$
# delimiter ;

# delete_account(in userID int) procedure

# delimiter $$
# create procedure delete_account(in userID int)
# begin
# 	delete from Users where Users.userID = userID;
#     call update_ratings();
# end $$
# delimiter ;


# testings (ignore)


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
# print([i[0] for i in a.getPoster('Onward', 'Two elven brothers embark on a quest to bring their father back for one
# day.')][-1])

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
