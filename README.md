
# Weather temperature API

A brief description of what this project does and who it's for


## API Reference

#### Get weather items for a spefic city for number of days

```http
  GET /api/locations/{city}/?days={number_of_days}
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `city` | `string` | **Required**. City NAME |
| `days` | `int` | **Required**. Days |



## Badges




## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`DEBUG`

`SECRET_KEY`

To access the weather API,Add the WEATHER_API_KEY below
`WEATHER_API_KEY= df882f0b551a4463a8064542221809`


 


## Run Locally

Clone the project

```bash
  git clone https://link-to-project
```

Go to the project directory

```bash
  cd weather
```

Create virtual environment and activate

```bash
  python3 -m venv venv
  source venv/bin/activate
```

Install Depedencies

```bash
  pip install r requirements.txt
```
Run Server

```bash
  python manage.py runserver
```

## Running Tests

To run tests, run the following command

```bash
   coverage run manage.py test
```
## View Coverage in HTML

To view code coverage, run the following command

```bash
   ccoverage html
```


## Appendix

Any additional information goes here

