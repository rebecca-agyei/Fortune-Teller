from django.shortcuts import render
import random

# Create your views here.

fortuneList = [
   "You have a bright future",
   "Be content with what you have",
   "Knowledge is power",
   "Happy yourself",
   "You can do it"
]
def fortune(request):
    fortune = random.choice(fortuneList)
    context = {
        'fortune': fortune
    }
    return render(request, "randomfortune/fortune.html", context)
