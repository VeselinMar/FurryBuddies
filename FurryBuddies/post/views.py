from django.shortcuts import render, redirect, get_object_or_404

from FurryBuddies.author.models import Author
from FurryBuddies.post.forms import CreatePostForm, EditPostForm, DeletePostForm
from FurryBuddies.post.models import Post


# Create your views here.


def index(request):
    author_id = request.session.get('author_id')
    author = Author.objects.filter(id=author_id).first() if author_id else None

    context = {
        'author': author,
    }

    return render(request, 'index.html', context=context)


def dashboard(request):
    posts = Post.objects.all()
    author = Author.objects.filter(id=request.session.get('author_id')).first()

    context = {
        'posts': posts,
        'author': author
    }

    return render(request, 'dashboard.html', context=context)


def post_details(request, pk):
    post = get_object_or_404(Post, id=pk)
    author = Author.objects.filter(id=request.session.get('author_id')).first()

    context= {
        'author': author,
        'post': post,
    }

    return render(request, 'details-post.html', context=context)


def create_post(request):
    author = Author.objects.filter(id=request.session.get('author_id')).first()
    if request.method == 'POST':
        form = CreatePostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = author
            post.save()
            return redirect('dashboard')
    else:
        form = CreatePostForm()

    context = {
        'form': form,
        'author': author,
    }

    return render(request, 'create-post.html', context=context)


def edit_post(request, pk):
    post = get_object_or_404(Post, id=pk)
    author = Author.objects.filter(id=request.session.get('author_id')).first()

    if request.method == 'POST':
        form = EditPostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    else:
        form = EditPostForm(instance=post)

    context = {
        'author': author,
        'form': form,
    }

    return render(request, 'edit-post.html', context=context)


def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        post.delete()
        return redirect('dashboard')

    form = DeletePostForm(instance=post)
    author = Author.objects.filter(id=request.session.get('author_id')).first()

    context = {
        'author': author,
        'form': form,
        'post': post,
    }

    return render(request, 'delete-post.html', context=context)