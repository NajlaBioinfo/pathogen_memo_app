# PathogenMemoApp

![alt text](pathogen_memo/static/img/flaskpython.png "PathogenMemo_icon")
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

* About:
	
	A Flask REST-API displaying some characteristics of serveral Pathogens/Potential Pathogens (demo).


* Some features used /tested

- Responsive table : Displaying data from database.
- REST-SWAGGER(OpenApi:3.0.0) : Rest-API module for somes entries.
- CRUD operations
- Restrict Access( Delete page and Dashboard, as a demo)
- SignUp / Login module. 
>> Login:hello@gmail.com // Pass: helloH9 , if you want to test the app.
- Responsive graphics (Matplotlib.)

* HowTo (Dev)
- You can build your own image for the application

```bash
docker build -t pathogen-memo-pack . 
```

- Then  Run the application with the cmd below:

```bash
docker run -it -p 8080:8080 -p 5432:5432 -p 5000:5000 pathogen-memo-pack:latest
```
- SignUp:
http://yourserver:5000/signup


* Link: Demo (Production)
<a href="https://pathogen-memo.herokuapp.com"> https://pathogen-memo.herokuapp.com </a>

##### - Author
Najlabioinfo

##### -  License
MIT
