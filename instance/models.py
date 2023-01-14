from django.db import models
from django.contrib.auth.models import User
from utils import risk_analysis, data_api
from django.utils import timezone

# Create your models here.
DEFAULT_THRESHOLD = 5


class Article(models.Model):
    link = models.URLField(max_length=500)
    title = models.TextField(null=True)
    description = models.TextField(null=True)
    date = models.DateTimeField(null=True)
    threshold = models.IntegerField(default=DEFAULT_THRESHOLD)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    company_name = models.CharField(max_length=200, default='exxon-mobile')

    number_risk_statements = models.IntegerField(default=0)
    score = models.IntegerField(default=0)

    def process(self):
        self.score = risk_analysis.get_score_text(
            self.description, self.company_name)
        self.number_risk_statements = risk_analysis.get_risky_lines_article(
            self.description, self.threshold, self.company_name)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        name = self.title + '\n' + "Number of risk statements : " + \
            str(self.number_risk_statements) + \
            '\n' + "Score : " + str(self.score)
        return name


class Instance(models.Model):
    company_name = models.CharField(max_length=200, default='exxon-mobile')
    description = models.TextField(null=True, blank=True)
    from_date = models.DateTimeField(
        default=timezone.now() - timezone.timedelta(days=100))
    to_date = models.DateTimeField(default=timezone.now())
    threshold = models.IntegerField(default=DEFAULT_THRESHOLD)
    number_risk_articles = models.IntegerField(default=0)
    phrases = models.TextField(default="")

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    articles = models.ManyToManyField(Article)

    class Meta:
        ordering = ['-updated', '-created']

    def process(self):
        for article in self.articles.all():
            article.threshold = self.threshold
            article.company_name = self.company_name
            article.process()
            article.save()

    def download(self):
        arts = data_api.getData(self.company_name)
        for art in arts:
            article = Article(company_name=self.company_name,
                              threshold=self.threshold, date=art['date'], title=art['title'], description=art['description'], link=art['url'])
            article.save()
            self.articles.add(article)
