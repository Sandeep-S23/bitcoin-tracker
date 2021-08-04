BITCOIN TRACKER

1. install all required packages from included requirements.txt
pip install -r requirements.txt

2. Authentication used - Token Authentication
JWT Authentication

3. Bitnoin price 
https://github.com/man-c/pycoingecko - to get actual price of Bitcoin in USD

4. Database used
Default db.sqlite3 - as it is demo project and not much data or load. 

5. Database Model
Alert model create for Alerts created by users 

6. Auth URLs 
	- api/auth/register - for new user registration
	- api/auth/login - for existig user login and get token for authorization, obtained token can be used as (Bearer <Token>) in header to get 					  authorized while making further requests

7. Alert URLs
	- api/alerts/ - to get list of all alerts [GET]
	- api/alerts/create - to list and create new alert [GET, POST]
	- api/alerts/triggered - to get list of triggered alerts [GET]
	- api/alerts/delete/<int:id> - to delete a particular alert created by user based on id [GET, DELETE] 			

