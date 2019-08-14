from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template

from .forms import ContactForm
from blog.models import BlogPost

def home_page(request):
  my_title = "Hello there...."
  qs = BlogPost.objects.all()[:5]
  context = {'title': "Welcome", 'blog_list': qs}
  # if request.user.is_authenticated:
  #   context = {"title": my_title, "my_list": [1,2,3,4,5,6]}
  # template_name = "title.txt"
  # template_obj = get_template(template_name)
  # rendered_string = template_obj.render(context)
  # doc = "<h1>{title}</h1>".format(title=title)
  # django_rendered_doc = "<h1>{{title}</h1>".format(title=title)
  return render(request, "home.html", context)

def about_page(request):
  return render(request, "about.html", {"title": "Aboout us"})

def contact_page(request):
  print("+++++++", request.POST)
  form = ContactForm(request.POST or None)
  if form.is_valid():
    print(form.cleaned_data)
    form = ContactForm()
  context = {
      "title": "Contact us",
      "form": form,
    }
  return render(request, "form.html", context)

def example_page(request):
  context = {"title": "Example"}
  template_name = "hello_world.html"
  template_obj = get_template(template_name)
  rendered_item = template_obj.render(context)
  return HttpResponse(rendered_item)