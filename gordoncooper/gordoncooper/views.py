from django.views.generic.base import TemplateView
from gordoncooper.models import Post


class Home(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        context['title'] = 'Home'
        context['posts'] = Post.objects.all()[:50]
        return context
