from django.shortcuts import render_to_response, redirect, render
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required

# from django.template.context import RequestContext
from forms import AddCategoryForm,ArticleForm,CommentForm,ImageForm
from blogs.models import AddCategory,Blog,Image
from django.http import  HttpResponseRedirect,HttpResponse
import json
from django.shortcuts import render, get_object_or_404
import datetime
from django.contrib import messages
from django.contrib.comments.models import Comment
from django.conf import settings
from django.contrib import comments
# from django_cron import CronJobBase, Schedule
# from ajaxuploader.views import AjaxFileUploader

def login(request):
    return render(request, 'blogs/login.html',{})

@login_required(login_url='/')
def home_page(request):
    '''this method help to show all category ''' 

    c_user = request.user
    blogs = Blog.objects.filter(user=c_user)
    ctx = {
        'blogs':blogs,
            }
	
    return render(request,'blogs/home.html',ctx)


def logout(request):
    auth_logout(request)
    return redirect('/')

@login_required(login_url='/')
def profile(request):
    """show all category"""

    return render(request,'blogs/login.html',{})

@login_required(login_url='/')
def addcategory(request):
    """To Add New AddCategory"""
    form = AddCategoryForm()
    if request.method == 'POST':
        tname = request.POST.get('tnm', '')
        slug = request.POST.get('slug', '')
        post_obj = AddCategory(title=tname,slug=slug)
        post_obj.save()
        return HttpResponseRedirect('/home/')
    ctx ={
    
    'form':form,

    }
    return render(request,'blogs/addcategory.html',ctx)

@login_required(login_url='/')
def newblog(request):
    """To create New Post"""

    form = ArticleForm()
    file_list = request.FILES.getlist('img')
    try:
        if request.method == 'POST':
            form = ArticleForm(request.POST, request.FILES)
            if form.is_valid:
                post = form.save(commit=False)
                post.user = request.user
                post.save()
                for i in file_list:
                    img = Image(image=i)
                    img.blog_id = post.id 
                    img.save()
                return HttpResponseRedirect('/home/')
    except:
        form.errors
    ctx = {
            'form':form,
          }
    return render(request,'blogs/newblog.html', ctx)


def detail(request,category_id):
    """show complete detail of perticular post"""

    article_list = Blog.objects.filter(category__pk=category_id)
    data={
        'categories': AddCategory.objects.all(),
        'posts': article_list,
        'category_id':category_id,
        # 'articles' : articles,
        }
    return render(request,'blogs/post_detail.html', data)


def single(request,post_id):
    """A single article"""

    cat=Blog.objects.get(pk=post_id)
    article = get_object_or_404(Blog,title=cat)
    images = Image.objects.filter(blog__id=post_id)
    posts = Blog.objects.get(pk=post_id)

    return render(
        request,
        "blogs/single.html",
        {
            "article" : article,
            # "blog_dates" : blog_dates,
            "posts" : posts,
            "images":images,
        }
    )

@login_required(login_url='/')
def edit_blog(request,post_id):
    instance = get_object_or_404(Blog, id=post_id)
    file_list = request.FILES.getlist('img')
    form = ArticleForm(request.POST or None,request.FILES or None, instance=instance)
    try:
        if form.is_valid():
            form.save()
            for i in file_list:
                img = Image(image=i)
                img.blog_id = post_id 
                img.save()
            return HttpResponseRedirect('/')
    except:
        form.errors
    ctx = {
            'form':form,
          }
    return render(request,'blogs/edit_blog.html', ctx)


@login_required(login_url='/')
def delete_blog(request,post_id):
    blog = Blog.objects.all()
    if post_id:
        try:
            blog = Blog.objects.get(id=post_id).delete()
        except:
            messages.warning(request, 'unable to delete.')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))


@login_required(login_url='/')
def show_salesimage(request, sales_id=None):
    sale = Image.objects.filter(blog__id=sales_id)[0]
    image = sale.image
    return HttpResponse(image.read())


@login_required(login_url='/')
def delete_own_comment(request, message_id):
    """The delete Posted Comment"""
    comment = Comment.objects.get(pk=message_id)
    if comment.user_email == request.user.email:
        comment.is_removed = True
        comment.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))


@login_required(login_url='/')
def edit_own_comment(request, message_id, slug):
    """The Edit Posted Comment"""
    try:
        comment = Comment.objects.get(id=message_id)
    except:
        pass
    if request.method == "POST":
        form = CommentForm(request.POST,instance = comment)
        if form.is_valid():
            post = form.save(commit=False)
            post.site_id=1
            post.save()
            return HttpResponseRedirect('/blogs/single/%s'%slug)
    else:
        form = CommentForm(instance = comment)
    return render(request, "blogs/update_comment.html", {'form':form})


def allblog(request):

    allblogs = Blog.objects.all()
    category = AddCategory.objects.all()
    print ("hiii")
    # import pdb; pdb.set_trace()
    tags = [j for j in allblogs]
    ctx= {
    'all_blogs' : tags,
    'categories':category,
    'allblogs':allblogs,
    }
    return render(request,"blogs/allblog.html",ctx)

def delete_image(request, id):
    image = Image.objects.get(pk=id).delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))

# @login_required(login_url='/')
# def delete_blog(request,post_id):
#     blog = Blog.objects.all()
#     if post_id:
#         try:
#             blog = Blog.objects.get(id=post_id).delete()
#         except:
#             messages.warning(request, 'unable to delete.')
#     return render(request,'blogs/home.html',{'blog':blog,'messages':messages})