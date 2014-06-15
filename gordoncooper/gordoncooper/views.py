from django.views.generic.base import TemplateView
from django.shortcuts import get_object_or_404
from gordoncooper.models import Post


class ListView(TemplateView):
    template_name = "list.html"

    def get_context_data(self, **kwargs):
        context = super(ListView, self).get_context_data(**kwargs)
        type = kwargs['type']
        context['menu'] = type or 'home'
        context['title'] = 'Home'

        posts = Post.objects.filter(active=True).order_by('-publish')
        if type is None:
            context['posts'] = posts[:50]
        else:
            context['posts'] = posts.filter(type=type)[:50]
        return context

class PostView(TemplateView):
    template_name = "post.html"

    def get_context_data(self, **kwargs):
        context = super(PostView, self).get_context_data(**kwargs)
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
