from django.shortcuts import render
from .utils import length_factors, weight_factors, speed_factors

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request,'about.html')

def document(request):
    return render(request,'documentation.html')


def length_converter(request):
    result = None
    to_unit = None

    if request.method == 'POST':
        from_unit = request.POST.get('from_unit')
        to_unit = request.POST.get('to_unit')
        value = request.POST.get('value')

        try:
            value = float(value)
            if value < 0:
                result = "Value cannot be negative"
            else:
                value_in_meters = value * length_factors[from_unit]
                result = value_in_meters / length_factors[to_unit]
        except (ValueError, TypeError, KeyError):
            result = "Invalid input"

    return render(request, 'length.html', {'result': result, 'to_unit': to_unit})


def temperature_converter(request):
    result = None
    to_unit = None

    if request.method == 'POST':
        from_unit = request.POST.get('from_unit')
        to_unit = request.POST.get('to_unit')
        value = request.POST.get('value')

        try:
            value = float(value)

            if from_unit == 'Celsius' and to_unit == 'Fahrenheit':
                result = (value * 9/5) + 32
            elif from_unit == 'Fahrenheit' and to_unit == 'Celsius':
                result = (value - 32) * 5/9
            elif from_unit == 'Celsius' and to_unit == 'Kelvin':
                result = value + 273.15
            elif from_unit == 'Kelvin' and to_unit == 'Celsius':
                result = value - 273.15
            elif from_unit == 'Fahrenheit' and to_unit == 'Kelvin':
                result = (value - 32) * 5/9 + 273.15
            elif from_unit == 'Kelvin' and to_unit == 'Fahrenheit':
                result = (value - 273.15) * 9/5 + 32
            else:
                result = value  # Same unit

        except (ValueError, TypeError):
            result = "Invalid input"

    return render(request, 'temperature.html', {'result': result, 'to_unit': to_unit})


def weight_converter(request):
    result = None
    to_unit = None

    if request.method == 'POST':
        from_unit = request.POST.get('from_unit')
        to_unit = request.POST.get('to_unit')
        value = request.POST.get('value')

        try:
            value = float(value)
            if value < 0:
                result="Value cannot be negative"
            else:
                value_in_kg = value * weight_factors[from_unit]
                result = value_in_kg / weight_factors[to_unit]
            
        except (ValueError, TypeError, KeyError):
            result = "Invalid input"

    return render(request, 'weight.html', {'result': result, 'to_unit': to_unit})


def speed_converter(request):
    result = None
    to_unit = None

    if request.method == 'POST':
        from_unit = request.POST.get('from_unit')
        to_unit = request.POST.get('to_unit')
        value = request.POST.get('value')

        try:
            value = float(value)
            if value < 0:
                result = "Value cannot be negative"
            else:
                value_in_mps = value * speed_factors[from_unit]
                result = value_in_mps / speed_factors[to_unit]
        except (ValueError, TypeError, KeyError):
            result = "Invalid input"

    return render(request, 'speed.html', {'result': result, 'to_unit': to_unit})
