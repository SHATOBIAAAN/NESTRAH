from django.shortcuts import render

# Create your views here.

def MainPage(request):
    return render(request, 'Base/MainPage.j2')

def story_list(request):
    return render(request, 'Stories/StoryList.j2')

def new_story(request):
    return render(request, 'Stories/NewStory.j2')
