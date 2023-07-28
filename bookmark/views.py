from django.shortcuts import render
from django.views.generic import ListView, DetailView  # 클래스형 제네릭 뷰  사용
from bookmark.models import Bookmark

# Create your views here.
class BookmarkLV(ListView):
    model = Bookmark

class BookmarkDV(DetailView):
    model = Bookmark