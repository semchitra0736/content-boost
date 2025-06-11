# Create your views here.
#/veo3 – VEO3 Prompt Generator
#/youtube-tags – YouTube Tag Generator
#/tiktok-tags – TikTok Hashtag Generator
#/facebook-reels – Facebook Reels Hashtag Generator
# generator/views.py

from django.shortcuts import render
from .models import PromptRecord
import random
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import redirect


def home(request):
    return render(request, "home.html")

def generate_veo3_prompt(user_input):
    # Simple local logic using templates
    templates = [
        f"Create a VEO3 video about '{user_input}' with a high-energy intro and strong call to action.",
        f"Make a short-form video exploring '{user_input}' in a fun, educational tone.",
        f"Engage viewers with a visual breakdown of '{user_input}' and end with a question.",
        f"Record a trending-style reel on '{user_input}', including a reaction and tips.",
        f"Present '{user_input}' using step-by-step storytelling in under 60 seconds.",
    ]
    return random.choice(templates)

# def veo3(request):
#     result = None
#     if request.method == "POST":
#         user_input = request.POST.get("input")
#         result = f"Generated VEO3 prompt for: {user_input}"  # Mock result
#     return render(request, "veo3.html", {"result": result})
def veo3_prompt_view(request):
    prompts = []
    if request.method == 'POST':
        # Collect form data
        character = request.POST.get('character', '')
        action = request.POST.get('action', '')
        # ...get all other fields similarly...

        # Mock prompt generation for example
        prompts = [
            {
                'title': 'Quantum Physics Basics',
                'category': 'Informative',
                'tone': 'Casual',
                'language': 'English',
                'description': 'A comprehensive guide to understanding the basics of quantum physics...',
            },
            {
                'title': 'Build Your Own Robot',
                'category': 'Tutorial',
                'tone': 'Casual',
                'language': 'English',
                'description': 'A step-by-step tutorial on how to build a simple robot...',
            },
        ]
    return render(request, 'veo3.html', {'prompts': prompts})


def veo3(request):
    result = None
    prompts = None
    if request.method == "POST":
        user_input = request.POST.get("input", "").strip()

        # Mock prompt generation for example
        prompts = [
            {
                'title': 'Quantum Physics Basics',
                'category': 'Informative',
                'tone': 'Casual',
                'language': 'English',
                'description': 'A comprehensive guide to understanding the basics of quantum physics...',
            },
            {
                'title': 'Build Your Own Robot',
                'category': 'Tutorial',
                'tone': 'Casual',
                'language': 'English',
                'description': 'A step-by-step tutorial on how to build a simple robot...',
            },
        ]
        if user_input:
            result = generate_veo3_prompt(user_input)

            if request.user.is_authenticated:
                PromptRecord.objects.create(
                    user=request.user,
                    prompt_type="veo3",
                    user_input=user_input,
                    result=result,
                )
    return render(request, "veo3.html", {"result": result, "prompts": prompts})



def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = UserCreationForm()
    return render(request, "auth/register.html", {"form": form})

def youtube_tags(request):
    return render(request, "youtube_tags.html")

def tiktok_tags(request):
    return render(request, "tiktok_tags.html")

def facebook_reels(request):
    return render(request, "facebook_reels.html")

