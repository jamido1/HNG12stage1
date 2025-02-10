# Number Classification API

## Project Description
My Number Classification API is a Django framework API that classifies numbers based on their properties. It determines whether a number is prime, perfect, Armstrong odd, or even. Additionally, it fetches fun facts about numbers from the Numbers API.

## Features
- Classifies numbers (Prime, Perfect, Armstrong, Odd/Even)
- Fetches fun facts about numbers using the Numbers API
- Returns JSON responses
- CORS enabled for cross-origin requests

## Tech Stack
- **Backend:** python, Django
- **Deployment:** Ralway
- **External API Integration:** Numbers API

  ## Setup Instructions

Prerequisites
Ensure you have the following installed:
- Python (>= 3.8)
- Git

Installation Steps
```bash
# Clone the repository
git clone https://github.com/jamido1/HNG12stage1.git
cd hngxii1

# Create a virtual environment and activate it
 pipenv shell

# Install dependencies
pip install -r requirements.txt

# Apply database migrations
python manage.py migrate

# Run the development server
python manage.py runserver
```

### Environment Variables
Create a `.env` file and add the following:
```
SECRET_KEY=your_secret_key
DEBUG=True
```

## API Usage

### Base URL
```

```

### Endpoints
#### **Classify a Number**
**GET** `/classify/<number>/`
- **Example Request:**
  ```bash
  curl -X GET https://hng12stage1-production-d636.up.railway.app/api/classify-number?number=40
  ```
- **Example Response:**
  ```json
{
  "number": 40,
  "is_prime": false,
  "is_perfect": false,
  "properties": [
    "even"
  ],
  "digit_sum": 4,
  "fun_fact": "40 is the only number whose letters are in alphabetical order."
}
  ```

## Deployment
The API is deployed on **Railway**.

### Procfile for Deployment
```
web: gunicorn core.wsgi:application --preload
```

## Known Issues
- The API works with `curl` but has connection issues with the Postman desktop app. Possible solutions include disabling SSL verification in Postman settings.

## Contributing
1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Make changes and commit (`git commit -m 'Add feature'`)
4. Push to your branch (`git push origin feature-branch`)
5. Open a Pull Request


## Acknowledgments
- Django Framework documentation
- Numbers API for number facts
- Railway for deployment

