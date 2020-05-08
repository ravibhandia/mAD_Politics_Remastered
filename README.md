# mAD_Politics ! 
####### INFO 257 Final Project #######

### Prerequisites
---
* **Dockerfile** : Use this file to set up Docker container. Be sure to direct to webapp folder
* **Mad_politics.sql** : The SQL file to build up our database. Be sure to direct the file location to data folders in `LOAD DATA LOCAL INFILE'(path to .csv)' ` 


### Deliverables
---
* **Presentation_mAD_Politics.pdf** : Final presentation slides
* **.pdf** : Final report

### data
---

##### Sources

Political Advertisements from Facebook
https://www.propublica.org/datastore/dataset/political-advertisements-from-facebook
Facebook Ads Report
https://www.facebook.com/ads/library/report/
Independent Political Ad Spending (2004-2016)
https://www.kaggle.com/fec/independent-political-ad-spending
Tracking Every Presidential Candidate’s TV Ad Buys
https://projects.fivethirtyeight.com/2020-campaign-ads/
Political advertising on Google
https://transparencyreport.google.com/political-ads/home?hl=en

Data collected from the above sources is manipulated for this project. We dropped
some information we deemed irrelevant for this project. We also manipulated it in order
to make it easier and also for demonstration purposes. You can take a look at ```clean_data.ipynb```.
The data is processed in clean_data and is exported to csv file. The output is then bulkloaded
into the database using queries in Mad_politics.sql




### webapp
---
*
