from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, UpdateView, DeleteView

from FurryBuddies.author.forms import AuthorEditForm, AuthorCreateForm, DeleteAuthorForm
from FurryBuddies.author.models import Author


# Create your views here.


def create_author_profile(request):
    if request.method == "POST":
        form = AuthorCreateForm(request.POST)
        if form.is_valid():
            author = form.save()
            request.session['author_id'] = author.id
            return redirect('dashboard')
    else:
        form = AuthorCreateForm()

    author = Author.objects.filter(id=request.session.get('author_id')).first()
    context = {
        'form': form,
        'author': author,
    }

    return render(request, 'create-author.html', context=context)


class AuthorDetailView(DetailView):
    model = Author
    template_name = 'details-author.html'

    def get_object(self, queryset=None):
        return get_object_or_404(Author)


class AuthorEditView(UpdateView):
    model = Author
    form_class = AuthorEditForm
    template_name = 'edit-author.html'

    def get_object(self, queryset=None):
        return Author.objects.first()

    def get_success_url(self):
        return reverse('author-details')


class AuthorDeleteView(DeleteView):
    model = Author
    form_class = DeleteAuthorForm
    template_name = 'delete-author.html'
    success_url = reverse_lazy('index')

    def get_object(self, queryset=None):
        return get_object_or_404(Author)

    def post(self, request, *args, **kwargs):
        author = self.get_object()
        author.delete()
        return redirect(self.success_url)

