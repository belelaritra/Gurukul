from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UploadFiles
from datetime import datetime

# Create your views here.
@login_required(login_url="/login")
def Upload(request):
    if request.method == "POST":
        title = request.POST.get("title")
        author = request.POST.get("author")
        ISBN = request.POST.get("ISBN")
        bookfile = request.FILES["bookfile"]
        filename = bookfile.name
        fileextention = filename.split(".")[-1]
        if fileextention == "pdf":
            name = (
                str(title.replace(" ", "_"))
                + str(datetime.now().strftime("%Y%m%d%H%M%S"))
                + "."
                + fileextention
            )
            bookfile.name = name
        else:
            messages.error(request, "Only PDF files are allowed")
            return redirect("/upload")
        image_url = (
            "https://books.google.com/books/content?vid=isbn"
            + str(ISBN)
            + "&printsec=frontcover&img=1&zoom=0&edge=curl&source=gbs_api"
        )
        timestamp = datetime.now()
        if title and author and ISBN and bookfile and image_url:
            try:
                UploadFiles.objects.create(
                    title=title,
                    author=author,
                    ISBN=ISBN,
                    bookfile=bookfile,
                    image_url=image_url,
                    timestamp=timestamp,
                )
                messages.success(request, "File uploaded successfully")
            except:
                messages.error(request, "Something went wrong")
        else:
            messages.error(request, "Please fill all the fields")
        return redirect("/upload")
    else:
        return render(request, "Library/uploadfiles.html")


@login_required(login_url="/login")
def feed(request):
    books = UploadFiles.objects.all()
    context = {"books": books}
    return render(request, "Library/feed.html", context)
