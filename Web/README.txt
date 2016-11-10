Our web project with Python and Flask will be placed here.

How run webapp.py for testing and presentation purpose in local mode


1. install flask on system by pip3 (python module manager) ex. $pip3 flask

2. download Chart.min.js from https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.3.0/Chart.min.js and put it to Web/static directory

3. download bootstrap and JQuerry and place all needed files to Web/static directory (by default in downloaded folder with bootstrap all files are separated into many folders ex. js, css. EXTRACT this files from this directories and place there to Web/static directory together)

4. copy DatabaseManager.py from Common directory to Web directory

5. create FLASK_APP shell variable pointing to place of our web python script ex. export FLASK_APP=/home/somename/place/where/is/webapp.py

6. $flask run - now on localhost:5000 you should find webpage with nice chart :)
