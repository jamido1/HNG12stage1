
from .utils import *
import requests as r
from django.http import JsonResponse as jr


def classify_number(request):
    #this Api classifies a number and returns its properties.
    num = request.GET.get('number')

    # input vaqlidation for number
    if not num or not num.lstrip("-").isdigit():
        return jr({"number": "alphabet", "error": True}, status=400)

    # Converts it to integer
    n = int(num)

    # Determines the properties
    digit_sum = sum(int(digit) for digit in str(abs(n)))  # sum of digits
    prime_status = is_prime(n)
    perfect_status = is_perfect(n)
    armstrong_status = is_armstrong(n)
    parity = "odd" if n % 2 != 0 else "even"

    # this defines the properties array
    properties = [parity]
    if armstrong_status:
        properties.insert(0, "armstrong")

    # Fetch fun fact from Numbers API
    try:
        url=f"http://numbersapi.com/{n}/math?json"
        response = r.get(url, timeout=5)
        fun_fact = response.json().get("text", "No fact available.")
    except r.RequestException:
        fun_fact = "unable to fetch a fun fact. kindly try again."

    
    data = {
        "number": n,
        "is_prime": prime_status,
        "is_perfect": perfect_status,
        "properties": properties,
        "digit_sum": digit_sum,
        "fun_fact": fun_fact
    }

    return jr(data, json_dumps_params={'indent': 2}) 
