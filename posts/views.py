from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from django.shortcuts import render

from .forms import CreationForm
from .models import Post, Group

User = get_user_model()

def index(request):
        post_list = Post.objects.order_by('-pub_date').all()
        paginator = Paginator(post_list, 10)  # показывать по 10 записей на странице.

        page_number = request.GET.get('page')  # переменная в URL с номером запрошенной страницы
        page = paginator.get_page(page_number)  # получить записи с нужным смещением
        return render(
            request,
            'index.html',
            {'page': page, 'paginator': paginator}
       )


def group_posts(request, slug):
    # функция get_object_or_404 получает по заданным критериям объект из базы данных
    # или возвращает сообщение об ошибке, если объект не найден
    group = get_object_or_404(Group, slug=slug)

    # Метод .filter позволяет ограничить поиск по критериям. Это аналог добавления
    # условия WHERE group_id = {group_id}
    posts = group.posts.all()[:12]
    paginator = Paginator(group.objects.all(), 10)
    context = {"group": group,  "paginatro":paginator}
    return render(request, "group.html", context)


def new_post(request):
    """Добавить новую запись, если пользователь известен."""
    form = CreationForm(request.POST)
    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.save()
        return HttpResponseRedirect(redirect_to='/')
    return render(request, 'new_post.html', {'form': form})

@login_required
def profile(request, username):
    user = User.objects.get(username=username)
    posts = Post.objects.filter(author=user.id)

    paginator = Paginator(posts, 5)
    page_number = request.GET.get('page')  # переменная в URL с номером запрошенной страницы
    page = paginator.get_page(page_number)

    context = {'userprofile': user, 'page': page, 'paginator': paginator, 'posts': posts}

    return render(request, 'profile_posts.html', context)

@login_required
def post_view(request, username, post_id):
    # тут тело функции
    userprofile = User.objects.get(username=username)
    posts = Post.objects.filter(author=userprofile.id)

    context = {'post': posts.get(id=post_id), 'userprofile': userprofile, 'posts': posts}

    return render(request, 'post_alone.html', context)
#
#
# def post_edit(request, username, post_id):
#     # тут тело функции. Не забудьте проверить,
#     # что текущий пользователь — это автор записи.
#     # В качестве шаблона страницы редактирования укажите шаблон создания новой записи
#     # который вы создали раньше (вы могли назвать шаблон иначе)
#     return render(request, 'post_new.html', {})