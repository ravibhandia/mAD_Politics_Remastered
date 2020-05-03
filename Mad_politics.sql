DROP DATABASE IF EXISTS MAD_POLITICS;

CREATE DATABASE MAD_POLITICS;
USE MAD_POLITICS;

DROP TABLE IF EXISTS `State`;
CREATE TABLE `State` (
  `State_id` int(11) NOT NULL,
  `State_name` varchar(20) NOT NULL,
  `State_abbreviation` varchar(20) NOT NULL,
  `Population` int(11) NOT NULL,
  `Delegates` int(11) NOT NULL,
  `Median_income` int(111) NOT NULL,
  `Median Age` DECIMAL NOT NULL,
  PRIMARY KEY  (`State_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
Insert into `State` VALUES (1	,'California'	,'CA'	,39510000	,415	,75277	,36.7),
                           (2	,'New York'	,'NY'	,19450000	,81	,64894	,38.2),
                           (3	,'Washington'	,'WA'	,7615000	,89	,74073	,38.3),
                           (4	,'Arizona'	,'AZ'	,7290000	,78	,59246	,38),
                           (5	,'Pennsylvania'	,'PA'	,12800000	,153	,60905	,40.8),
                           (6	,'Vermont'	,'VT'	,623989	,11	,57513	,42.7),
                           (7	,'Massachusetts'	,'MA'	,6893000	,91	,77385	,39.5),
                           (8	,'Indiana'	,'IN'	,6732000	,89	,54181	,37.4);


DROP TABLE IF EXISTS `CANDIDATE`;
CREATE TABLE `CANDIDATE` (
  `Candidate_id` int(11) NOT NULL,
  `First_name` varchar(30) NOT NULL,
  `Last_name` varchar(30) NOT NULL,
  `Birthday` DATE NOT NULL,
  `State_id` int(11) NOT NULL,
  `Election_year` YEAR NOT NULL,
  `Party` varchar(30) NOT NULL,
  PRIMARY KEY  (`Candidate_id`),
  CONSTRAINT `fk_candidate_state`
    FOREIGN KEY (State_id) REFERENCES State (State_id)
    ON DELETE CASCADE
    ON UPDATE RESTRICT

                         ) ENGINE=MyISAM DEFAULT CHARSET=latin1;

Insert into `CANDIDATE` VALUES (1, 'Joseph','Biden',	11/20/42,	5,	2020,	'Democrat'),
                               (2	,'Donald'	,'Trump'	,14/06/1946	,2	,2020,	'Republican'),
                               (3, 'Bernie',	'Sanders'	,9/8/41,	6	,2020,	'Democrat'),
                               (4, 'Elizabeth'	,'Warren'	,5/22/49	,7	,2020	,'Democrat'),
                               (5, 'Micheal'	,'Bloomberg',	2/14/42,	2,	2020,	'Independent'),
                               (6,'Pete',	'Buttigieg',	1/19/82,	8,	2020,	'Democrat');

DROP TABLE IF EXISTS `Affiliated_groups`;
CREATE TABLE `Affiliated_groups` (
  `Group_id` int(11) NOT NULL,
  `Group_name` varchar(100) NOT NULL,
  `Candidate_id` int(11) NOT NULL,
  PRIMARY KEY  (`Group_id`),
  KEY (`Candidate_id`),
  CONSTRAINT `fk_affiliated_candidate`
    FOREIGN KEY (Candidate_id) REFERENCES CANDIDATE (Candidate_id)
    ON DELETE CASCADE
    ON UPDATE RESTRICT
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
INSERT into `Affiliated_groups` Values (1	,'Mike Bloomberg 2020 Inc'	,5),

(2	,'TRUMP MAKE AMERICA GREAT AGAIN COMMITTEE'	,2),
(3	,'BERNIE 2020'	,3),
(4	,'WARREN FOR PRESIDENT INC'	,4),
(5	,'PETE FOR AMERICA'	,6);









DROP TABLE IF EXISTS `Ad_platform`;
CREATE TABLE `Ad_platform` (
  `Platform_id` int(11) NOT NULL,
  `Platform_name` varchar(30) NOT NULL,
  `Platform_type` varchar(100) NOT NULL,
  PRIMARY KEY  (`Platform_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

Insert into `Ad_platform` VALUES (1,'Facebook',	'Digital'),
                                 (2	,'Google',	'Digital'),
                                 (3,'Hulu','TV');

DROP TABLE IF EXISTS `Advertisement`;
CREATE TABLE `Advertisement` (
  `Ad_id` bigint NOT NULL,
  `Platform_id` int(11) NOT NULL,
  `Candidate_id` int(11) NOT NULL,
  `State_id` int(11) NOT NULL,
  `Group_id` int(11) NOT NULL,
  `Ad_title` varchar(100) default NULL,
  `Ad_content` varchar(100) default NULL,
  `Created_time` DATE default Null,
  `End_time` DATE default NULL,
  `Cost` DECIMAL default NULL,
  `Impression` int(11) default NULL,
  PRIMARY KEY  (`Ad_id`),
  KEY (`Platform_id`),
  KEY (`Candidate_id`),
  KEY(`State_id`),
  KEY(`Group_id`),
  CONSTRAINT `fk_ad_candidate`
    FOREIGN KEY (Candidate_id) REFERENCES CANDIDATE (Candidate_id)
    ON DELETE CASCADE
    ON UPDATE RESTRICT,
CONSTRAINT `fk_ad_platform`
    FOREIGN KEY (Platform_id) REFERENCES Ad_platform (Platform_id)
    ON DELETE CASCADE
    ON UPDATE RESTRICT
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

Insert into `Advertisement`VALUES (6756153498,1	,5	,1	,1	,'Mike Bloomberg',	'GO Mike Bloomberg'	,'2020/04/29 0:00:00',	'2020/04/29 0:00:00'	,45, 17124),
                                  (6756153418, 1, 2, 1, 2, 'Trump',	'MAKE AMERICA GREAT AGAIN'	,'2020/04/25 0:00:00',	'2020/04/25 0:00:00',	45	,17928),
                                  (6756153398,1, 3, 1, 3	,'Bernie'	,'GO BERNIE'	,'2020/04/23 0:00:00'	,'2020/04/23 0:00:00'	,45	,18247),
                                  (6756152498,1,	4,	1,	4,	'Elizabeth Warren'	,'WARREN FOR PRESIDENT'	,'2020/04/21 0:00:00'	,'2020/04/21 0:00:00'	,45	,17924),
                                  (6756133498	,1	,1	,1	,6	,'Joe Biden'	,'BIDEN FOR PRESIDENT'	,'2020/04/19 0:00:00'	,'2020/04/19 0:00:00',	45	,17824),
                                  (6756193498	,1	,6	,1	,5	,'Pete Buttigieg'	,'PETE FOR AMERICA'	,'2020/04/15 0:00:00'	,'2020/04/15 0:00:00'	,45	,19824);




DROP TABLE IF EXISTS `Polling`;
CREATE TABLE `Polling` (
  `Poll_id` int(11) NOT NULL,
  `State_id` int(11) NOT NULL,
  `Candidate_id` int(11) NOT NULL,
  `Check_date` DATE NOT NULL,
  `Polling_percent` decimal(5,2) NOT NULL,
  PRIMARY KEY  (`Poll_id`),
  CONSTRAINT `fk_polling_state`
    FOREIGN KEY (State_id) REFERENCES State (State_id)
    ON DELETE CASCADE
    ON UPDATE RESTRICT,
CONSTRAINT `fk_polling_candidate`
    FOREIGN KEY (Candidate_id) REFERENCES CANDIDATE (Candidate_id)
    ON DELETE CASCADE
    ON UPDATE RESTRICT
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
Insert into `Polling` VALUES (1	,1	,6	,3/1/20	,8.242897),
                             (2	,1	,5	,3/1/20	,13.06435),
                             (3 ,1	,4	,3/1/20	,14.01564),
                             (4	,1	,3	,3/1/20	,33.06242),
                             (5	,1	,1	,3/1/20	,15.072956),
                             (6 ,2	,5	,2/29/20	,23.97167),
                             (7 ,2	,4	,2/29/20	,10.975128),
                             (8 ,2	,3	,2/29/20	,26.630459),
                             (9 ,2	,1	,2/29/20	,15.06949),
                             (10	,2	,6	,2/28/20	,8.800144),
                             (11	,3	,5	,2/28/20	,16.27527),
                             (12	,3	,4	,2/28/20	,13.16813),
                             (13	,3	,3	,2/28/20	,30.53929),
                             (14	,3	,1	,2/28/20	,10.37702),
                             (15	,3	,6	,2/27/20	,10.1617);


