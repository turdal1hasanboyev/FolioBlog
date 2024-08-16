from django.shortcuts import render, redirect

from folio.models import Blog, Portfolio, Comment, User, Category, GetInTouch


def index(request):
    url = request.META.get('HTTP_REFERER')

    user = User.objects.get(id=1)
    
    blogs = Blog.objects.all()
    portfolios = Portfolio.objects.all()
    categories = Category.objects.all()

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        GetInTouch.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message,
        )

        return redirect(url)
    
    context = {
        'user': user,
        'blogs': blogs.order_by('-id')[:3],
        'portfolios': portfolios.order_by('-id')[:6],
        "categories": categories.order_by('title'),
    }

    return render(request, 'index.html', context)

def single(request, slug):
    blog = Blog.objects.get(slug__exact=slug)

    comments = Comment.objects.filter(blog_id=blog.id)

    if request.method == "POST":   
        name = request.POST.get("name")
        email = request.POST.get("email")
        comment = request.POST.get("comment")
        web_site = request.POST.get("website")

        Comment.objects.create(
            blog_id=blog.id,
            user_id=request.user.id,
            name=name,
            email=email,
            comment=comment,
            web_site=web_site,
        )

        return redirect('single', blog.slug)

    context = {
        "blog": blog,
        "comments": comments,
        }
    
    return render(request, 'blog-single.html', context)

def grid(request):
    blogs = Blog.objects.all()
    
    return render(request, 'blog-grid.html', {'blogs': blogs.order_by('-id')})
