from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

monthly_challenges = {
    "january": "Write a gratitude list.",
    "february": "Eat more veggies.",
    "march": "Declutter your space.",
    "april": "Read before bed.",
    "may": "Try a new recipe.",
    "june": "Walk daily.",
    "july": "Skip sugary drinks.",
    "august": "Learn one new word.",
    "september": "Breathe deeply.",
    "october": "Walk instead of drive.",
    "november": "Say thank you.",
    "december": "Set your goals."
}

def index(request):
    months = list(monthly_challenges.keys())
    list_items = ""
    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"
        
    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        response_data = f"<h1>{challenge_text}</h1>"
        return HttpResponse(response_data)
    except KeyError:
        return HttpResponseNotFound("<h1>This month is not supported!</h1>")

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months) or month < 1:
        return HttpResponseNotFound("Invalid month")
    redirect_month = months[month - 1]
    return_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(return_path)