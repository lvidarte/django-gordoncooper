from django.views.generic.base import TemplateView
from django.shortcuts import get_object_or_404
from gordoncooper.models import Post


class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['title'] = 'Home'
        context['menu'] = 'Home'
        context['posts'] = Post.objects.filter(active=True).order_by('-publish')[:50]
        return context

class PostView(TemplateView):
    template_name = "post.html"

    def get_context_data(self, **kwargs):
        context = super(PostView, self).get_context_data(**kwargs)
        context['title'] = 'Post'
        context['menu'] = None
        context['post'] = get_object_or_404(
            Post.objects.filter(
                publish__year=self.kwargs['year'],
                publish__month=self.kwargs['month'],
                publish__day=self.kwargs['day'],
                slug=self.kwargs['slug']
            )
        )
        return context
