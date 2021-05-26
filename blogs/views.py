from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, CreateView, DetailView, ListView, DeleteView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from blogs.forms import PostForm, CommentForm
from blogs.models import Post, Comment
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy,reverse

# Create your views here.

class AboutView(TemplateView):
    template_name = 'blogs/about.html'


class CreateNewPost(LoginRequiredMixin, CreateView):
    form_class = PostForm
    model = Post


class CreateNewComment(LoginRequiredMixin, CreateView):
    form_class = CommentForm
    model = Comment
    success_url = reverse_lazy('blogs:post_list')
    url = None

    def form_valid(self, form, *args, **kwargs):
        cur_form = form.save(commit=False)
        cur_form.post = Post.objects.filter(id = self.kwargs['pk'])[0]
        cur_form.save()
        return HttpResponseRedirect(reverse_lazy('blogs:post_detail', kwargs = self.kwargs))


class PostDetail(DetailView):
    model = Post


class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.all()


class PostDelete(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy("blogs:post_list")

    def post(self, request, *args, **kwargs):
        if "confirm" in request.POST:
            return super(PostDelete, self).post(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(reverse('blogs:post_detail', kwargs = kwargs))


@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('blogs:post_detail', pk=pk)
