Our web project with Python and Flask will be placed here.

How run webapp.py for testing and presentation purpose in local mode


1. install flask on system by pip3 (python module manager) ex. $pip3 flask

2. download Chart.min.js from https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.3.0/Chart.min.js and put it to Web/static directory

3. copy DatabaseManager.py from Common directory to Web directory

4. create FLASK_APP shell variable pointing to place of our web python script ex. export FLASK_APP=/home/somename/place/where/is/webapp.py

5. $flask run - now on localhost:5000 you should find webpage with nice chart :)
