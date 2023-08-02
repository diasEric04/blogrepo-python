from django.shortcuts import render
from django.core.paginator import Paginator
from blog.models import Post, Page, Category, Tag
from django.db.models import Q
from django.http import Http404
from django.contrib.auth.models import User

PER_PAGE = 9


def index(request):
    posts = Post.objects \
        .order_by('-pk') \
        .filter(is_published=True)
    paginator = Paginator(posts, PER_PAGE)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'site_title': 'Home - ',
        'page_obj': page_obj
    }
    return render(
        request,
        'blog/pages/index.html',
        context
    )


def post(request, slug):
    post = (
        Post.objects.get_published()
        .filter(slug=slug)
        .first()
    )

    if post is None:
        raise Http404()

    post_title = post.title

    context = {
        'site_title': f'Post {post_title} - ',
        'post': post
    }
    return render(
        request,
        'blog/pages/post.html',
        context
    )


def page(request, slug):
    page = (
        Page.objects.get_published()
        .filter(slug=slug)
        .first()
    )

    if page is None:
        raise Http404()

    page_title = page.title

    context = {
        'site_title': f'Page {page_title} - ',
        'page': page
    }
    return render(
        request,
        'blog/pages/page.html',
        context
    )


def created_by(request, author_pk):
    posts = Post.objects.get_published()\
        .filter(created_by__pk=author_pk)

    paginator = Paginator(posts, PER_PAGE)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    users = User.objects.filter(pk=author_pk).first()

    if users is None:
        raise Http404()

    author_name = users.username

    if users.first_name and users.last_name:
        author_name = f'{users.first_name} {users.last_name}'

    context = {
        'site_title': f'Author {author_name} - ',
        'page_obj': page_obj
    }
    return render(
        request,
        'blog/pages/index.html',
        context
    )


def category(request, slug):
    posts = Post.objects.get_published()\
        .filter(category__slug=slug)
    paginator = Paginator(posts, PER_PAGE)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    categories = Category.objects.filter(slug=slug).first()

    if categories is None:
        raise Http404()

    category_name = categories.name

    context = {
        'site_title': f'Category {category_name} - ',
        'page_obj': page_obj
    }
    return render(
        request,
        'blog/pages/index.html',
        context
    )


def tag(request, slug):
    posts = Post.objects.get_published()\
        .filter(tags__slug=slug)
    paginator = Paginator(posts, PER_PAGE)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    tags = Tag.objects.filter(slug=slug).first()

    if tags is None:
        raise Http404()

    tag_name = tags.name

    context = {
        'site_title': f'Tag {tag_name} - ',
        'page_obj': page_obj
    }
    return render(
        request,
        'blog/pages/index.html',
        context
    )


def search(request):
    search_value = request.GET.get('q', '').strip()
    posts = (
        Post.objects.get_published()
        .filter(
            # titulo contem search_value ou
            # excerpt contem search_value ou
            # conteudo contem search_value
            Q(title__icontains=search_value) |
            Q(excerpt__icontains=search_value) |
            Q(content__icontains=search_value)
        )[0:PER_PAGE]
    )

    context = {
        'site_title': f'Search {search_value} - ',
        'page_obj': posts,
        'search_value': search_value
    }
    return render(
        request,
        'blog/pages/index.html',
        context
    )
