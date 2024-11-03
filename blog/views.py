from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
from .forms import ArticleForm
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.db.models import Q
from django.shortcuts import render
from .models import Article, Comment

def home(request):
    return render(request, 'home.html')


@login_required
def submit_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            send_mail(
                'Article soumis',
                'Votre article a été soumis pour examen.',
                'from@example.com',
                [request.user.email]
            )
            return redirect('success')
    else:
        form = ArticleForm()
    return render(request, 'submit_article.html', {'form': form})

@login_required
def approve_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    if request.method == 'POST':
        article.is_approved = True
        article.save()
        send_mail(
            'Article approuvé',
            'Votre article a été approuvé et publié.',
            'from@example.com',
            [article.author.email]
        )
        return redirect('dashboard')
    return render(request, 'approve_article.html', {'article': article})

def success(request):
    return render(request, 'success.html')

@login_required
def submit_comment(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.author = request.user.username
            comment.save()
            send_mail(
                'Commentaire soumis',
                'Votre commentaire a été soumis pour examen.',
                'from@example.com',
                [request.user.email]
            )
            return redirect('article_detail', article_id=article.id)
    else:
        form = CommentForm()
    return render(request, 'submit_comment.html', {'form': form, 'article': article})

@login_required
def approve_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.method == 'POST':
        comment.is_approved = True
        comment.save()
        send_mail(
            'Commentaire approuvé',
            'Votre commentaire a été approuvé et publié.',
            'from@example.com',
            [comment.author]
        )
        return redirect('dashboard')
    return render(request, 'approve_comment.html', {'comment': comment})

@staff_member_required
def dashboard(request):
    pending_articles = Article.objects.filter(is_approved=False)
    pending_comments = Comment.objects.filter(is_approved=False)
    return render(request, 'dashboard.html', {'pending_articles': pending_articles, 'pending_comments': pending_comments})

def search(request):
    query = request.GET.get('q')
    results = Article.objects.filter(
        Q(title__icontains=query) | Q(content__icontains=query),
        is_approved=True
    )
    return render(request, 'search_results.html', {'query': query, 'results': results})

def get_recommendations(article):
    similar_articles = Article.objects.filter(
        category=article.category,
        tags__in=article.tags.all()
    ).exclude(id=article.id).distinct()[:5]
    return similar_articles

def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    recommendations = get_recommendations(article)
    return render(request, 'article_detail.html', {'article': article, 'recommendations': recommendations})
