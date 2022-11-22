from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Post, Comment, User, Education, Job, Skill, Project, Category, Contactme, Socialaccount
from .forms import CommentForm, ContactForm

# Frontend
def home(request):
    bios = User.objects.all()
    studies = Education.objects.all()
    jobs = Job.objects.all()
    skills = Skill.objects.all()
    projects = Project.objects.all()

    linkedin = Socialaccount.objects.filter(social_name='linkedin')
    dribble = Socialaccount.objects.filter(social_name='dribbble')

    if request.method == 'POST':
        fullname = request.POST["full_name"]
        email = request.POST["email"]
        subject= request.POST["subject"]
        message = request.POST["message"]
        dict = {
            'fullname': fullname,
            'email': email,
            'subject': subject,
            'message': message,
        }
        contact = Contactme(full_name=fullname, email=email, subject=subject, message=message)
        contact.save()
        return HttpResponseRedirect('/thanks/') 

    context = {
        'bios': bios,
        'jobs': jobs,
        'skills': skills,
        'studies': studies,
        'projects': projects,
        'page': 'home',
        'linkedin': linkedin,
        'dribble': dribble,
    }
    return render(request, "home.html", context)

def portfolio(request):
    projects = Project.objects.filter(is_published=True)
    linkedin = Socialaccount.objects.filter(social_name='linkedin')
    dribble = Socialaccount.objects.filter(social_name='dribbble')

    context = {
        'projects': projects,
        'page': 'portfolio',
        'linkedin': linkedin,
        'dribble': dribble,
    }
    return render(request, "portfolio.html", context)

def blog(request):
    categories = Category.objects.all()
    posts = Post.objects.all().order_by('-created_at')

    linkedin = Socialaccount.objects.filter(social_name='linkedin')
    dribble = Socialaccount.objects.filter(social_name='dribbble')

    context = {
        "posts": posts,
        "categories": categories,
        'page': 'blog',
        'linkedin': linkedin,
        'dribble': dribble,
    }
    return render(request, "blog.html", context)

def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    linkedin = Socialaccount.objects.filter(social_name='linkedin')
    dribble = Socialaccount.objects.filter(social_name='dribbble')

    context = {
        'header': 'project',
        'project': project,
        'linkedin': linkedin,
        'dribble': dribble,
    }
    return render(request, "project_detail.html", context)

def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)

    linkedin = Socialaccount.objects.filter(social_name='linkedin')
    dribble = Socialaccount.objects.filter(social_name='dribbble')


    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment_body = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post
            )
            comment_body.save()
            #return HttpResponseRedirect('')
            form = CommentForm()
    else:
        form = CommentForm()
    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
        'header': 'project',
        'form': form,
        'linkedin': linkedin,
        'dribble': dribble,
    }
    return render(request, "blog_detail.html", context)

def blog_category(request, category):
    posts = Post.objects.filter(
        categories__name__contains=category
    ).order_by(
        '-created_at'
    )

    linkedin = Socialaccount.objects.filter(social_name='linkedin')
    dribble = Socialaccount.objects.filter(social_name='dribbble')

    context = {
        "category": category,
        "posts": posts,
        'linkedin': linkedin,
        'dribble': dribble,
    }
    return render(request, "blog_category.html", context)

def thankyou(request):
    linkedin = Socialaccount.objects.filter(social_name='linkedin')
    dribble = Socialaccount.objects.filter(social_name='dribbble')

    context = {
        'linkedin': linkedin,
        'dribble': dribble,
    }    
    return render(request, "thanks.html", context)