from django.shortcuts import render

def book_list(request):
    books = [
        {'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald', 'genre': 'Fiction', 'publish_date': '1925', 'description': 'A portrait of the Jazz Age in all of its decadence and excess.'},
        {'title': 'To Kill a Mockingbird', 'author': 'Harper Lee', 'genre': 'Fiction', 'publish_date': '1960', 'description': 'A novel about the serious issues of rape and racial inequality.'},
        {'title': '1984', 'author': 'George Orwell', 'genre': 'Dystopian', 'publish_date': '1949', 'description': 'A dystopian novel about the consequences of government over-reach, totalitarianism, and mass surveillance.'},
        {'title': 'Pride and Prejudice', 'author': 'Jane Austen', 'genre': 'Classic', 'publish_date': '1813', 'description': 'A romantic novel of manners.'},
        {'title': 'The Hobbit', 'author': 'J.R.R. Tolkien', 'genre': 'Fantasy', 'publish_date': '1937', 'description': 'A children\'s fantasy novel and prelude to The Lord of the Rings.'},
    ]
    return render(request, 'myapp/book_list.html', {'books': books})
