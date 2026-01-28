from django.shortcuts import render
from .forms import BookForm
from .models import Book
# Create your views here.
def home(request):
    return render(request, 'home.html')

def addbook(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'addbook.html', {'form': BookForm(), 'msg': 'Book added successfully!'})
    else:
        form = BookForm()
    return render(request, 'addbook.html', {'form': form})

def viewbooks(request):
    bookdata = Book.objects.all()
    return render(request, 'viewbooks.html', {'bookdata': bookdata})

def deletebook(request, id):
    book = Book.objects.get(id=id)
    book.delete()
    bookdata = Book.objects.all()
    return render(request, 'viewbooks.html', {'bookdata': bookdata, 'msg': 'Book deleted successfully!'})


def searchbook(request):
    if request.method == "POST":
        id = request.POST.get('id')
        book = Book.objects.get(id=id)
        return render(request, 'searchbook.html', {'book': book})
    
    return render(request, 'searchbook.html')