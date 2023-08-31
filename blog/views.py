from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from pytils.translit import slugify
from blog.models import Blog


class BlogCreateView(CreateView):
    model = Blog
    fields = ('title', 'text', 'blog_img', 'is_published', 'date_of_creation')
    success_url = reverse_lazy('weblog:list')

    def form_valid(self, form):
        if form.is_valid():
            new_weblog = form.save()
            new_weblog.slug = slugify(new_weblog.title)
            new_weblog.save()

        return super().form_valid(form)


class BlogListView(ListView):
    model = Blog

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class BlogDetailView(DetailView):
    model = Blog

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(pk=self.kwargs.get('pk', None))
        return queryset

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.count_of_views += 1
        self.object.save()
        return self.object


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('title', 'text', 'blog_img', 'date_of_creation')

    def form_valid(self, form):
        if form.is_valid():
            new_weblog = form.save()
            new_weblog.slug = slugify(new_weblog.title)
            new_weblog.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('weblog:view', args=[self.kwargs.get('pk')])


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('weblog:list')
