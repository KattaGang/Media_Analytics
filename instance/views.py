from django.shortcuts import render, redirect
from instance.models import Instance, Article
from .forms import InstanceForm, ArticleForm

# Create your views here.


def home(request):
    return render(request, 'instance/home.html')


def instanceList(request):
    insts = Instance.objects.all()
    context = {
        'instances': insts,
    }
    return render(request, 'instance/instance_list.html', context)


def articleList(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'instance/article_list.html', context)


def instanceView(request, pk):
    instance = Instance.objects.get(id=pk)
    articles = instance.articles.all()
    context = {
        'instance': instance,
        'articles': articles,
    }
    return render(request, 'instance/instance.html', context)


def instanceUpdate(request, pk):
    inst = Instance.objects.get(id=pk)
    if request.method == 'POST':
        form = InstanceForm(request.POST, instance=inst)
        inst = form.save(commit=False)
        inst.process()
        inst.save()
        return redirect('instance', inst.id)
    form = InstanceForm(instance=inst)
    context = {
        'form': form,
    }
    return render(request, 'instance/form.html', context)


def instanceCreate(request):
    form = InstanceForm()
    if request.method == 'POST':
        form = InstanceForm(request.POST)
        if form.is_valid():
            inst = form.save(commit=False)
            inst.save()
            inst.download()
            inst.process()
            inst.save()
            return redirect('instance', inst.id)

    context = {
        'form': form,
    }
    return render(request, 'instance/form.html', context)


def articleCreate(request):
    form = ArticleForm()
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.process()
            article.save()
            return redirect('article', article.id)

    context = {
        'form': form,
    }
    return render(request, 'instance/form.html', context)


def articleUpdate(request, pk):
    article = Article.objects.get(id=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        article = form.save(commit=False)
        article.process()
        article.save()
        return redirect('article', article.id)
    form = ArticleForm(instance=article)
    context = {
        'form': form,
    }
    return render(request, 'instance/form.html', context)


def articleView(request, pk):
    article = Article.objects.get(id=pk)
    context = {
        'article': article,
    }
    return render(request, 'instance/article.html', context)


def articleDelete(request, pk):
    article = Article.objects.get(id=pk)
    article.delete()
    return redirect('article-list')


def instanceDelete(request, pk):
    instance = Instance.objects.get(id=pk)
    instance.delete()
    return redirect('instance-list')


def instanceDownload(request, pk):
    instance = Instance.objects.get(id=pk)
    instance.download()
    instance.save()
    return redirect('instance', instance.id)
