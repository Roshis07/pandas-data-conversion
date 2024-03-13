# pandas-data-conversion
Pandas Data Conversion is your friendly assistant for managing data types effortlessly. Powered by Django on the backend and React on the frontend, this web app simplifies the process of inferring and converting data types in CSV and Excel files.


To run this application in your device we need to install some packages in the backend or frontend for the first time which is listed below:



## Backend: We need to go on backend directery (same as manage.py directery) in the any terminal and needs to install

# make sure you type python 3 for mac and python only for windows

1) Install python
2) Install django (pip install django)
3) Install djangorestframework (pip install djangorestframework)
4) make migration to djangorestframework( python manage.py makemigrations)
5) migrate model in backend( python manage.py migrate)
6) Install crossheaders (pip install django-cors-headers) which allows to connect with frontend address
7) install pandas (pip install pandas)
8) To run the program (python manage.py runserver)
## make sure to run the program properly we have to run the both server in same time, maybe you can use two terminal at the time 
## most of these which needs to install are stored in the requirements.txt in the project file for the references




## for the frontend ( we need to go on the frontend directory which is dataconversion-frontend)
1) go to project directory and install dependencies (npm install)
2) run the frontend(npm start)




## Additional notes

This project utilises the python script in the backend and craete views based on this and after this connected to url endpoint based on the 
views function, backend url is 
## http://127.0.0.1:8000/data/infer/
then frontend uses this url endpoint and connected through the post request and return and map data in the frontend which
is done in FileUpload.js, later this component is render in the App.js in the react 
