from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView



from .models import New
from comments.models import Comment
from .filters import NewFilter
from .forms import NewsForm
from comments.forms import CommentForm


# Create your views here.
class NewsListView(ListView):
    model = New
    template_name = "news/news_list.html"
    paginate_by = 3

    # def get_queryset(self):
    #     return New.objects.filter(status__exact='public').order_by('is_due')


def get_search_data(self, **kwargs):
    news = New.objects.all()
    newsfilter = NewFilter(request.Get, queryset=news)
    news = news.qs
    context.update({
        'newsfilter':newsFilter
        })
    return context



class NewsDetailView(LoginRequiredMixin, DetailView):
    model = New
    template_name = "news/news_details.html"
    form_class = CommentForm

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            new = self.get_object()
            form.instance.user = self.request.user
            form.instance.new = new
            form.save()
            return redirect(reverse("news:news-details", kwargs={'pk': new.id}))

    def get_context_data(self, **kwargs):
        news_comment_counts = Comment.objects.all().filter(
            new=self.object.id).count()
        news_comments = Comment.objects.all().filter(new=self.object.id)
        context = super().get_context_data(**kwargs)
        context["form"] = self.form_class
        context.update({
            'form': self.form_class,
            'news_comments': news_comments,
            'news_comment_counts': news_comment_counts
        })
        return context



class NewsCreateView(LoginRequiredMixin, CreateView):
    model = New
    form_class = NewsForm
    template_name = "news/create_news.html"
    success_url = reverse_lazy('news:home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.save()
        return super().form_valid(form)


