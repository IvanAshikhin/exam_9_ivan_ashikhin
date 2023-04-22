from django.contrib.auth import get_user_model
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from photo.forms import SearchForm, PhotoForm
from photo.models import Photo

User = get_user_model()


class IndexView(ListView):
    template_name = 'index.html'
    model = Photo
    context_object_name = 'photos'
    paginate_by = 6
    paginate_orphans = 1

    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().get(request, *args, **kwargs)

    def get_search_form(self):
        return SearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search']
        return None

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['form'] = self.form
        return context


class AddPhotoView(CreateView):
    model = Photo
    fields = ['signature', 'image']
    template_name = 'add_photo.html'

    def form_valid(self, form):
        photo = form.save(commit=False)
        photo.author = self.request.user
        photo.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('index')


class PhotoUpdateView(UpdateView):
    template_name = 'update.html'
    form_class = PhotoForm
    model = Photo
    context_object_name = 'photo'

    def get_success_url(self):
        return reverse('details', kwargs={'pk': self.object.pk})


class PhotoDetail(DetailView):
    template_name = 'detail.html'
    model = Photo
    context_object_name = 'photo'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class PhotoDeleteView(DeleteView):
    template_name = 'confirm_delete.html'
    context_object_name = 'photo'
    model = Photo
    success_url = reverse_lazy('index')
