from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Book
from .forms import BookForm

@login_required
def book_list(request):
    books = Book.objects.filter(user=request.user)
    read_count = books.filter(is_read=True).count()
    unread_count = books.filter(is_read=False).count()
    return render(request, 'books/book_list.html', {
        'books': books,
        'read_count': read_count,
        'unread_count': unread_count,
    })

@login_required
def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk, user=request.user)
    return render(request, 'books/book_detail.html', {'book': book})

@login_required
def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.user = request.user
            book.save()
            messages.success(request, f'"{book.title}" added to your library!')
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'books/book_form.html', {'form': form, 'action': 'Add'})

@login_required
def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk, user=request.user)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, f'"{book.title}" updated!')
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'books/book_form.html', {'form': form, 'action': 'Edit', 'book': book})

@login_required
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk, user=request.user)
    if request.method == 'POST':
        title = book.title
        book.delete()
        messages.success(request, f'"{title}" removed from your library.')
        return redirect('book_list')
    return render(request, 'books/book_confirm_delete.html', {'book': book})
