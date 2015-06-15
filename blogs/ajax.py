
from django.shortcuts import render_to_response, render
from django.template.loader import render_to_string
from django.http import HttpResponse
from blogs.models import Blog
import json
import datetime
from django.utils import simplejson
from django.core import serializers
from django.contrib.auth.decorators import login_required
# def ajax_get_tags(request):

#     post_id = request.POST.get("post_id")
#     g_id=request.POST['category']
#     t_id = request.POST['tag']
#     g_id = str(g_id)
#     t_id = str(t_id)
#     blogs_list=[]
#     blog = Blog.objects.all()
#     import pdb;pdb.set_trace()
#     if g_id or t_id:
#       blog = blog.filter(category__id=g_id).filter(tag=t_id) 
    
#     # blog_list = [i for i in blog]
    
#     return HttpResponse(simplejson.dumps({"blogs_list":blog_list}), status=200, mimetype="application/json")
 
#     # if g_id or t_id:
    #   blogs = blog.filter(category__id=g_id).filter(tag=t_id) 

    #   for blg in blogs:
    #       blogs_list.append(blg.title)

    # return HttpResponse(content=json.dumps({"blogs_list":blog_list}), status=200,content_type='application/json')


# def ajax_get_tags(request):
#     if not request.is_ajax():
#         return HttpResponse(content="Invalid Request Method.", status=400)

#     post_id = request.POST.get("post_id")
#     g_id=request.POST['category']
#     t_id = request.POST['tag']
#     g_id = str(g_id)
#     t_id = str(t_id)
#     blogs_list=[]
#     blogs = Blog.objects.all()
#     # import pdb;pdb.set_trace()
#     if g_id or t_id:
#       blogs = blogs.filter(category__id=g_id).filter(tag=t_id) 
#     data = {'blogs':serializers.serialize("json", blogs)}

#     return HttpResponse(json.dumps(data), content_type="text/json")


def ajax_get_tags(request):
    if not request.is_ajax():
        return HttpResponse(content="Invalid Request Method.", status=400)

    post_id = request.POST.get("post_id")
    g_id = request.POST.get('category', None)
    t_id = request.POST.get('tag', None)
    blogs = Blog.objects.all()
    if g_id is not None:
        blogs = blogs.filter(category__id=g_id)

    if t_id is not None:
        blogs = blogs.filter(tag=t_id)

    rendered = render_to_string('blogs/includes/blog_list.html',{"allblogs": blogs})
    return HttpResponse(
            json.dumps({'template': rendered}), content_type="text/json")