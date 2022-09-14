# Weather Forecast App
The purpose of this project is to get what the weather is going to be for the next 1-10 days. I used [Weather API](https://www.weatherapi.com/) to get the weather forecast data. django-rest-framework was used to create the api.

# Running the Application Locally
- clone the repo into a location of your choice i.e 
```
git clone https://github.com/michael-basweti/weather.git
```

- In your terminal, move into the project folder called **weather**
- while in the project folder, create a python virtual environment (Assuming at this point you have python and python3-venv installed in your machine). To create a virtual environment, run the commands below.
```
# windows platform
python -m venv venv

# unix based platforms

python3 -m venv venv

# next we activate the python environment through
# windows platform
source venv/Scripts/activate
# unix based platforms
source venv/bin/activate
```

- Now that we are in the virtual environment, let's install the requiremts. Make sure you're in the root folder of the project when running the command below.
```
pip install -r requirements.txt

or

pip3 install -r requirements.txt
```

- while still in the root folder, we can now start the server through the command below.
```
python manage.py runserver
```

- Now that the app is running, we can test it and get to see the different responses we get according to the parameters we add. Personally, I used Insomnia as my API Client to test the API (One can use Postman too).

In your API Client of choice, hit the url http://127.0.0.1:8000/api/location/ with parameter **city** and days i.e http://127.0.0.1:8000/api/location/?city=london&days=2

Below is a screenshots for a successful query.

Below is a failed query because no such city exits

- To run tests, execute the following command in the root folder of the project.
```
python manage.py test
```

