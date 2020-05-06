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
LOAD DATA LOCAL INFILE '/Users/seanc/Documents/data/state_entity.csv'
INTO TABLE `State`
FIELDS TERMINATED BY ',';


DROP TABLE IF EXISTS `CANDIDATE`;
CREATE TABLE `CANDIDATE` (
  `Candidate_id` int(11) NOT NULL,
  `First_name` varchar(30) NOT NULL,
  `Last_name` varchar(30) NOT NULL,
  `Birthday` DATE,
  `State_id` int(11) NOT NULL,
  `Election_year` YEAR NOT NULL,
  `Party` varchar(30) NOT NULL,
  PRIMARY KEY  (`Candidate_id`),
  CONSTRAINT `fk_candidate_state`
    FOREIGN KEY (State_id) REFERENCES State (State_id)
    ON DELETE CASCADE
    ON UPDATE RESTRICT
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
LOAD DATA LOCAL INFILE '/Users/seanc/Documents/data/candidate_entity.csv'
INTO TABLE `CANDIDATE`
FIELDS TERMINATED BY ','
(`Candidate_id`, `First_name`,`Last_name`, @DATE_STR, `State_id`, `Election_year`, `Party`)
SET `Birthday` = STR_TO_DATE(@DATE_STR, '%c/%e/%y');



DROP TABLE IF EXISTS `Affiliates`;
 CREATE TABLE `Affiliates` (
   `Affiliate_id` int(11) NOT NULL,
   `Affiliate_name` varchar(100) NOT NULL,
   `Candidate_id` int(11) NOT NULL,
   PRIMARY KEY  (`Affiliate_id`),
   KEY (`Candidate_id`),
   CONSTRAINT `fk_affiliated_candidate`
     FOREIGN KEY (Candidate_id) REFERENCES CANDIDATE (Candidate_id)
     ON DELETE CASCADE
     ON UPDATE RESTRICT
 ) ENGINE=MyISAM DEFAULT CHARSET=latin1;
LOAD DATA LOCAL INFILE '/Users/seanc/Documents/data/affiliate_entity.csv'
INTO TABLE `Affiliates`
FIELDS TERMINATED BY ',';


DROP TABLE IF EXISTS `Ad_platform`;
 CREATE TABLE `Ad_platform` (
   `Platform_id` int(11) NOT NULL,
   `Platform_name` varchar(30) NOT NULL,
   `Platform_type` varchar(100) NOT NULL,
   PRIMARY KEY  (`Platform_id`)
 ) ENGINE=MyISAM DEFAULT CHARSET=latin1;
LOAD DATA LOCAL INFILE '/Users/seanc/Documents/data/platform_entity.csv'
INTO TABLE `Ad_platform`
FIELDS TERMINATED BY ',';

DROP TABLE IF EXISTS `Advertisement`;
 CREATE TABLE `Advertisement` (
   `Ad_id` bigint NOT NULL,
   `Platform_id` int(11) NOT NULL,
   `State_id` int(11) NOT NULL,
   `Group_id` int(11) NOT NULL,
   `Ad_title` varchar(100) default NULL,
   `Created_time` DATE default Null,
   `End_time` DATE default NULL,
   `Cost` DECIMAL default NULL,
   `Impression` int(11) default NULL,
   PRIMARY KEY  (`Ad_id`),
   KEY (`Platform_id`),
   KEY(`State_id`),
   KEY(`Group_id`),
   CONSTRAINT `fk_ad_platform`
     FOREIGN KEY (Platform_id) REFERENCES Ad_platform (Platform_id)
     ON DELETE CASCADE
     ON UPDATE RESTRICT
 ) ENGINE=MyISAM DEFAULT CHARSET=latin1;
LOAD DATA LOCAL INFILE '/Users/seanc/Documents/data/ad_entity.csv'
INTO TABLE `Advertisement`
FIELDS TERMINATED BY ','
(`Ad_id`,`Platform_id`,`State_id`,`Group_id`,`Ad_title`,@DATE_STR, @DATE_STR,`Cost`,`Impression`)
SET
    `Created_time` = STR_TO_DATE(@DATE_STR, '%c/%e/%y'),
    `End_time` = STR_TO_DATE(@DATE_STR, '%c/%e/%y');

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
LOAD DATA LOCAL INFILE '/Users/seanc/Documents/data/poll_entity.csv'
INTO TABLE `Polling`
FIELDS TERMINATED BY ','
( `Poll_id`,`State_id`,`Candidate_id`,@DATE_STR,`Polling_percent`)
SET `Check_date` = STR_TO_DATE(@DATE_STR, '%c/%e/%y');
