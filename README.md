##### Project Title

#!mAD Politics - Campaign Advertising

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

```
Python 3.7
DataGrip 2019.3.2
Docker Desktop 2.2.0.5
```

### Installing

1. Clone or download this Github repository for all the necessary materials. 
	
```
[Instruction Link of Cloning Github Repository] (https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository)
```

2. Build and Run the Flask Container through Docker. 

```
[Instruction Link of Docker Container Creation and Running] (https://github.com/munners17/python-flask-app)
* **Dockerfile** : Use this file to set up Docker container. Be sure to direct to webapp folder
```

3. Run Mad_politics.sql in MariabDB to create the database.

```
All data files in the folder of "Data"
* **Mad_politics.sql** : The SQL file to build up our database. Be sure to direct the file location to data folders in `LOAD DATA LOCAL INFILE'(path to .csv)' `
```

4. Open the web browser, navigate to http://127.0.0.1:5000/ to check if webpage is up!

```

```


### Deliverables
---
* **Presentation_mAD_Politics.pdf** : Final presentation slides
* **.pdf** : Final report

### Data
---

##### Sources

1. Political Advertisements from Facebook
https://www.propublica.org/datastore/dataset/political-advertisements-from-facebook
2. Facebook Ads Report
https://www.facebook.com/ads/library/report/
3. Independent Political Ad Spending (2004-2016)
https://www.kaggle.com/fec/independent-political-ad-spending
4. Tracking Every Presidential Candidate’s TV Ad Buys
https://projects.fivethirtyeight.com/2020-campaign-ads/
5. Political advertising on Google
https://transparencyreport.google.com/political-ads/home?hl=en

Data collected from the above sources is manipulated for this project. We dropped
some information we deemed irrelevant for this project. We also manipulated it in order
to make it easier and also for demonstration purposes. You can take a look at ```clean_data.ipynb```.
The data is processed in clean_data and is exported to csv file. The output is then bulkloaded
into the database using queries in Mad_politics.sql

### webapp
---

## Acknowledgments

* https://github.com/munners17/INFO257-Sp2020
* Luis Aguilar
* Eric Zan

