insert into Movies(movieName, year, genre, synopsis, posterUrl) 
values
('Luca', 2021, 'Animation', 'Luca', 'poster');

insert into Users(userName, email, firstName, lastName, dateRegistered)
values
('daiko', 'daiko@email.com', 'Daimonikos', 'Kaikohuru', CURDATE()),
('boris', 'boris@email.com', 'Christopher', 'Boris', CURDATE()),
('drazeros', 'drazeros@email.com', 'Delainore', 'Zakeros', CURDATE());

delete from Movies where movieID=7;

update Users set lastName='Zekaros' where userID=9;

select * from Movies;

select * from Users;

select * from Review;

insert into Review(movieId, userID, movieName, dateReviewed, reviewDesc, ratings)
values
(4, 6, 'httyd', CURDATE(), 'this movie is amazing and awesome and spectacular', 9),
(4, 7, 'httyd', CURDATE(), 'meh, this is just a generic animation, lack of plot, not recommended to watch', 1),
(4, 8, 'httyd', CURDATE(), 'not good but not bad, just ok', 5),
(4, 9, 'httyd', CURDATE(), 'the character backgrounds are reach and the plot is amazing too, definitely worth the time to watch this awesome movie', 8);

call get_ratings(4, @avgRatings);
update Movies set ratings=@avgRatings where movieID=4;

update Movies set Movies.ratings = (select avg(ratings) from Review where Review.movieID = 4) where Movies.movieID = 4;

select * from Movies;

delimiter $$
drop procedure if exists get_ratings$$
create procedure get_ratings(in movieID int)
begin
	update Movies 
		set Movies.ratings = (
			select avg(ratings) 
            from Review 
            where Review.movieID = movieID
		) 
        where Movies.movieID = movieID;
	update Movies
        set Movies.ratingsCount = (
			select count(ratings) 
            from Review 
            where Review.movieID = movieID
        ) 
        where Movies.movieID = movieID;
end$$
delimiter ;

alter table Users add password varchar(255) not null;

select * from Users;

update Users set password="b'$2b$12$BEZMCKW4XnQuydQkd3SLwux.GVhWxvaa35R8Uos.iV1h.0.pHmgF2'" where userID=6;

update Users set password='' where userID=6;

select * from Users where userName='daixiez' or email='daixiez@gmail.com';

select * from Movies;

alter table Movies add ratingsCount int not null;

select movieID, count(ratings) from Review group by movieID;

select count(ratings) 
            from Review 
            where Review.movieID = 4;

insert into Review(movieID, userID, movieName, dateReviewed, reviewDesc, ratings)
values
(5, 9, 'httyd 2', CURDATE(), 'spectacular!', 10);

show index from Review;

alter table Review add foreign key (userID) references Users(userID) on update cascade on delete cascade;

select * from Review;

call get_ratings(4);

select * from Movies;

delete from Review where reviewDesc='this movie is amazing and spectacular';
