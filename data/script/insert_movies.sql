-- use karel_bondan;

-- insert into Movies(movieName, year, genre, synopsis, ratings, posterUrl) 
-- values('Onward', 2020, 'Animation', 'Two elven brothers embark on a quest to bring their father back for one day.', 0.0, 'https://xl.movieposterdb.com/20_01/2020/7146812/xl_7146812_61d71abe.jpg');

-- create table Review(
-- 	reviewID int not null auto_increment,
--     movieID int not null, 
--     movieName varchar(255) not null,
--     dateReviewed date not null,
--     userName varchar(255) not null,
--     reviewDesc text not null,
--     ratings double not null,
--     primary key (reviewID),
--     foreign key (movieID) references Movies (movieID),
--     foreign key (userName) references Users (userName)
--     on update cascade on delete cascade);
--     
-- show engine innodb status;

-- insert into Movies(movieName, year, genre, synopsis, ratings, posterUrl) 
-- values('Onward', 2020, 'Animation', 'Two elven brothers embark on a quest to bring their father back for one day.', 0.0,
--  'https://xl.movieposterdb.com/20_01/2020/7146812/xl_7146812_61d71abe.jpg'),
--  ('How to Train Your Dragon', 2010, 'Animation',
--  'A hapless young Viking who aspires to hunt dragons becomes the unlikely friend of a young dragon himself, and learns there may be more to the creatures than he assumed.',
--  0.0, 'https://posters.movieposterdb.com/10_03/2010/892769/l_892769_59411b04.jpg'),
--  ('How to Train Your Dragon 2',
--  2014, 'Animation',
--  'When Hiccup and Toothless discover an ice cave that is home to hundreds of new wild dragons and the mysterious Dragon Rider, the two friends find themselves at the center of a battle to protect the peace.',
--  0.0, 'https://posters.movieposterdb.com/14_11/2014/1646971/l_1646971_f8a0dc5c.jpg'),
--  ('How to Train Your Dragon: The Hidden World',
--  2019, 'Animation',
--  'When Hiccup discovers Toothless isn\'t the only Night Fury, he must seek "The Hidden World", a secret Dragon Utopia before a hired tyrant named Grimmel finds it first.',
--  0.0, 'https://xl.movieposterdb.com/21_05/2019/2386490/xl_2386490_1cc009ee.jpg')

select * from Movies;