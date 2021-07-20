from django.core import paginator
from django.shortcuts import redirect, render, get_object_or_404
from .models import *
from django.utils import timezone
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    diary = Diary.objects.all()
    paginator = Paginator(diary, 3)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(request, 'home.html', {'diary':page})

def detail(request, id):
    diary = get_object_or_404(Diary, pk = id)
    return render(request, 'detail.html', {'diary':diary})

def make_post(request):
    if request.method == "POST":
        new_diary = Diary()
        new_diary.title = request.POST['title']
        new_diary.pub_date = timezone.now()
        new_diary.weather = request.POST['weather']
        new_diary.photo = request.FILES['photo']
        new_diary.body = request.POST['body']
        new_diary.save()
        return redirect('home')
    else:
        return render(request, 'new.html')

def delete(request, id):
    delete_diary = Diary.objects.get(id = id)
    delete_diary.delete()
    return redirect('home')
