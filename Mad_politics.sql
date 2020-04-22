DROP DATABASE IF EXISTS MAD_POLITICS;

CREATE DATABASE MAD_POLITICS;
USE MAD_POLITICS;

DROP TABLE IF EXISTS `CANDIDATE`;
--
-- Table structure for table `CANDIDATE`
--

DROP TABLE IF EXISTS `CANDIDATE`;
CREATE TABLE `CANDIDATE` (
  `Candidate_id` int(11) NOT NULL,
  `First_name` varchar(30) NOT NULL,
  `Last_name` varchar(30) NOT NULL,
  `Birthday` DATE NOT NULL,
  `State_id` int(11) NOT NULL,
  `Election_year` YEAR NOT NULL,
  `Party` varchar(30) NOT NULL,
  PRIMARY KEY  (`Candidate_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

DROP TABLE IF EXISTS `Ad_platform`;
CREATE TABLE `Ad_platform` (
  `Platform_id` int(11) NOT NULL,
  `Platform_name` varchar(30) NOT NULL,
  `Platform_type` varchar(100) NOT NULL,
  `Election_year` YEAR NOT NULL,
  PRIMARY KEY  (`Platform_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

DROP TABLE IF EXISTS `Advertisement`;
CREATE TABLE `Advertisement` (
  `Ad_id` int(11) NOT NULL,
  `Platform_id` int(11) NOT NULL,
  `Candidate_id` int(11) NOT NULL,
  `State_id` int(11) NOT NULL,
  'Group_id' int(11) NOT NULL,
  'Ad_title' varchar(100) default NULL,
  'Ad_content' varchar(100) default NULL,
  'Created_time' TIMESTAMP default Null,
  `End_time` TIMESTAMP default NULL,
  PRIMARY KEY  (`Ad_id`),
  KEY (`Platform_id`),
  KEY (`Candidate_id`),
  KEY(`State_id`),
  KEY(`Group_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;


DROP TABLE IF EXISTS `State`;
CREATE TABLE `State` (
  `State_id` int(11) NOT NULL,
  `State_name` varchar(20) NOT NULL,
  `State_abbreviation` varchar(20) NOT NULL,
  `Population` int(11) NOT NULL,
  'Delegates' int(11) NOT NULL,
  'Median_income' int(111) NOT NULL,
  'Demographic' varchar(100) NOT NULL,
  PRIMARY KEY  (`State_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

DROP TABLE IF EXISTS `Polling`;
CREATE TABLE `Polling` (
  `Poll_id` int(11) NOT NULL,
  `State_id` int(11) NOT NULL,
  `Candidate_id` int(11) NOT NULL,
  `Check_date` DATE NOT NULL,
  'Polling_percent' decimal(5,2) NOT NULL,
  PRIMARY KEY  (`Poll_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;


DROP TABLE IF EXISTS `Affiliated_groups`;
CREATE TABLE `Affiliated_groups` (
  `Group_id` int(11) NOT NULL,
  `Group_name` varchar(100) NOT NULL,
  `Candidate_id` int(11) NOT NULL,
  PRIMARY KEY  (`Group_id`),
  KEY (`Candidate_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;







