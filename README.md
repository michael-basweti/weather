# Weather Forecast App
The purpose of this project is to get what the weather is going to be for the next 1-10 days. I used [Weather API](https://www.weatherapi.com/) to get the weather forecast data. Django-rest-framework was used to create the api.

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

- Create a .env file in the root folder as shown below:
```
touch .env

#In the file, paste in the values as shown below.

source venv/Scripts/activate
export SECRET_VALUE="xxxxxxxxxxxxxxxxxxxxxx"
export WEATHER_API_BASE_URL="http://api.weatherapi.com/v1/forecast.json?"
export WEATHER_API_KEY="--your-key"


```
A .env file will be shared when submitting this project. Kindly copy it to the root folder before running this application

- while still in the root folder, we can now start the server through the command below.
```
python manage.py runserver
```

- Now that the app is running, we can test it and get to see the different responses we get according to the parameters we add. Personally, I used Insomnia as my API Client to test the API (One can use Postman too).

In your API Client of choice, hit the url http://127.0.0.1:8000/api/location/ with parameter **city** and days i.e http://127.0.0.1:8000/api/location/?city=london&days=2

Below is a screenshots for a successful query.
![successful](https://user-images.githubusercontent.com/23398223/190058464-7296a465-f690-4925-9fc8-38d315fa1bbf.png)

Below is a failed query because no such city exists
![failed](https://user-images.githubusercontent.com/23398223/190058641-bf54d793-969b-4165-b4c7-8439ced3e05e.png)


- To run tests, execute the following command in the root folder of the project.
```
python manage.py test
```

