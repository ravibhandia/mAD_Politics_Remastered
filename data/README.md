# Data

This directory contains sample csv data for each entity we have in our DB Schema.
Feel free to manipulate the data however you want. Just make sure to keep the
integrity of the data.

Some attributes such as Dates may not be in appropriate sql format. We have written
set of commands in Mad_politics.sql script that handles the conversion to appropriate
format when bulk loading the data into DB.

### state_entity

```
(
  `State_id` int(11) NOT NULL,
  `State_name` varchar(20) NOT NULL,
  `State_abbreviation` varchar(20) NOT NULL,
  `Population` int(11) NOT NULL,
  `Delegates` int(11) NOT NULL,
  `Median_income` int(111) NOT NULL,
  `Median Age` DECIMAL NOT NULL,
   PRIMARY KEY  (`State_id`)
)

```

### candidate_entity

```
(
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
)
```

### affiliate_entity

```
(
   `Affiliate_id` int(11) NOT NULL,
   `Affiliate_name` varchar(100) NOT NULL,
   `Candidate_id` int(11) NOT NULL,
   PRIMARY KEY  (`Affiliate_id`),
   KEY (`Candidate_id`),
   CONSTRAINT `fk_affiliated_candidate`
     FOREIGN KEY (Candidate_id) REFERENCES CANDIDATE (Candidate_id)
     ON DELETE CASCADE
     ON UPDATE RESTRICT
 )
```

### ad_platform_entity
```
(
   `Platform_id` int(11) NOT NULL,
   `Platform_name` varchar(30) NOT NULL,
   `Platform_type` varchar(100) NOT NULL,
   PRIMARY KEY  (`Platform_id`)
)
```

### ad_entity

```
(
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
 )
```

### poll_entity
```
(
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
 )
```
