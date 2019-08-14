from django.contrib.auth.decorators import login_required 
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, get_object_or_404
from django.http import Http404

# Create your views here.
from .forms import BlogPostModelForm
from .models import BlogPost

# def blog_post_detail_page(request, slug):
#   print("Django says.....", request.method, request.path, request.user)
  # query_set = BlogPost.objects.filter(slug=slug)
  # if query_set.count() == 0:
  #   raise Http404
  # obj = query_set.first() 
  # obj = get_object_or_404(BlogPost, slug=slug)
  # template_name = 'blog_post_detail.html'
  # context = {"object": obj}
  # return render(request, template_name, context)

# @login_required
@staff_member_required
def blog_post_list_view(request):
  # qs = BlogPost.objects.filter(title__icontains='world')
  qs = BlogPost.objects.all()
  template_name = 'blog/list.html'
  context = {'object_list': qs}
  return render(request, template_name, context)

@staff_member_required
def blog_post_create_view(request):

  form = BlogPostModelForm(request.POST or None)
  if form.is_valid():
    # obj =BlogPost.objects.create(**form.cleaned_data)
    obj = form.save(commit=False)
    # obj.title = form.cleaned_data.get('title') + "0"
    obj.user = request.user
    obj.save()
    form = BlogPostModelForm()
  template_name = 'form.html'
  context = {'form': form}
  return render(request, template_name, context)

def blog_post_detail_view(request, slug):
  obj = get_object_or_404(BlogPost, slug=slug)
  template_name = 'blog/detail.html'
  context = {'object': obj}
  return render(request, template_name, context)
  
def blog_post_update_view(request):
  obj = get_object_or_404(BlogPost, slug=slug)
  form = BlogPostModelForm(request.POST or None, instance=obj)
  template_name = 'form.html'
  context = {'form': form, "title": f"Update {obj.title}"}
  return render(request, template_name, context)

def blog_post_delete_view(request):
  obj = get_object_or_404(BlogPost, slug=slug)
  template_name = 'blog/delete.html'
  context = {'object': obj}
  return render(request, template_name, context)