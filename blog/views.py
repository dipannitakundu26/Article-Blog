from blog.models import Category, Post
from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .forms import Post, Postform
from django.urls import reverse_lazy
#def home(request):
    #return render(request,'home.html')
# Create your views here.
class HomeView(ListView):
    model = Post
    template_name='home.html'
    ordering = ['-id']

    def get_context_data(self, *args, **kwargs):
       cat_menu=Category.objects.all()
       context = super(HomeView,self).get_context_data(*args,**kwargs)
       context["cat_menu"] =cat_menu
       return context
   

def CategoryView(request,cats):
    category_posts = Post.objects.filter(category=cats)
    return render(request,'categories.html',{'cats':cats.title(), 'category_posts':category_posts})

class AddCategoryView(CreateView):
    model = Category
    template_name='add_categories.html'
    fields= '__all__'


class ArticledetailView(DetailView):
    model = Post
    template_name='articles_detail.html'

    def get_context_data(self, *args, **kwargs):
       cat_menu=Category.objects.all()
       context = super(ArticledetailView,self).get_context_data(*args,**kwargs)
       context["cat_menu"] =cat_menu
       return context

class AddPostView(CreateView):
    model = Post
    form_class=Postform
    template_name='add_posts.html'
    #fields= '__all__'
    def get_context_data(self, *args, **kwargs):
       cat_menu=Category.objects.all()
       context = super(AddPostView,self).get_context_data(*args,**kwargs)
       context["cat_menu"] =cat_menu
       return context

class UpdatePostView(UpdateView):
    model = Post
    form_class=Postform
    template_name='edit_post.html'
    #fields= ['title','body']
class DeletePostView(DeleteView):
    model = Post
    template_name='delete_post.html'
    success_url=reverse_lazy('homeview')

    