from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

monthly_challenges = {
    "january": "Eat no meat for the entire month",
    "february": "Walk for atleat 20 minutes every day",
    "march": "Learn django for 20 minutes everyday",
    "april": "Eat no meat for the entire month",
    "may": "Walk for atleat 20 minutes every day",
    "june": "Learn django for 20 minutes everyday",
    "july": "Eat no meat for the entire month",
    "august": "Walk for atleat 20 minutes every day",
    "september": "Learn django for 20 minutes everyday",
    "october": "Eat no meat for the entire month",
    "november": "Walk for atleat 20 minutes every day",
    "december": None,
}


# Create your views here.

def index(request):
    months = list(monthly_challenges.keys())

    context={
        "months":months
    }
    return render(request,'challenges/index.html',context)


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("<h1>Invalid Month!</h1>")
    redirect_month = months[month-1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        context={
            "text":challenge_text,
            "month_name":month
        }
        return render(request,'challenges/challenge.html',context)
    except:
        raise Http404()
