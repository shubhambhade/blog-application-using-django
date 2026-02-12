from django.shortcuts import render, redirect, get_list_or_404
from django.http import HttpResponse

from . models import Blog, Category
# Create your views here.

def posts_by_category(request, category_id):
    # fetch the post that belongs to category with the category_id
    posts = Blog.objects.filter(status='Published', category = category_id)
    # use try/except when we want to do some custome actions if the category does not exists

    # try:
    #     category =  Category.objects.get(pk=category_id)
    # except:
    #     # redirect user to home page
    #     return redirect('home')
    
    # Use get_object_or_404 when you want to show 404 error page if category does not exists
    category =  get_list_or_404(Category,pk=category_id)

    context = {
        'posts':posts,
        'category':category,
    }
    return render(request,'post_by_category.html', context)
