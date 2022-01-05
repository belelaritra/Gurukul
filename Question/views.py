from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import Question, Answer
from django.contrib import messages
from .templatetags import get_dict
from django.contrib.auth.decorators import login_required
from .models import Question, Answer

# Create your views here.
@login_required(login_url="/login")
def feed(request):
    allposts = (
        Question.objects.all()
    )  # .objects --> Get all the objects from the database
    # print(allposts)

    context = {"allposts": allposts}
    return render(request, "Question/feed.html", context)


@login_required(login_url="/login")
def question(request, slug):
    post = Question.objects.filter(slug=slug).first()  # .filter --> Filter the objects

    # Comments Corresponding to post
    comments = Answer.objects.filter(
        post=post, parent=None
    )  # .objects --> Get all the objects from the database
    replies = Answer.objects.filter(post=post).exclude(
        parent=None
    )  # .objects --> Get all the objects from the database
    # print(post)
    # print(comments, replies)
    reply_count = {}
    for comment in comments:
        reply_count[comment.serial_no] = Answer.objects.filter(parent=comment).count()

    # Key = Comment_Id (Serial_No) & Value = List of Replies (whose parent is the comment.serial_no)
    reply_Dict = {}
    for reply in replies:
        # Initial
        if reply.parent.serial_no not in reply_Dict.keys():
            reply_Dict[reply.parent.serial_no] = [reply]
        # Append
        else:
            reply_Dict[reply.parent.serial_no].append(reply)

    print(reply_Dict)
    context = {
        "post": post,
        "comments": comments,
        "user": request.user,
        "reply_Dict": reply_Dict,
        "reply_count": reply_count,
    }
    return render(request, "Question/question.html", context)
    # return HttpResponse(f'Blog Post : {slug}')


@login_required(login_url="/login")
def comment(request):
    if request.method == "POST":
        comment = request.POST.get("comment")
        user = request.user

        post_serial_no = request.POST.get("post_serial_no")
        parent_serial_no = request.POST.get("parent_serial_no")

        post = Question.objects.filter(serial_no=post_serial_no).first()

        if parent_serial_no == "":
            comment = Answer(comment=comment, user=user, post=post)
            comment.save()
            messages.success(request, "Your comment has been posted successfully.")

        else:
            parent = Answer.objects.get(serial_no=parent_serial_no)
            comment = Answer(comment=comment, user=user, post=post, parent=parent)
            comment.save()
            messages.success(request, "Your reply has been posted successfully.")

    return redirect(f"/question/{post.slug}")
