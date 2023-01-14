from django.forms import ModelForm
from .models import Instance, Article

class InstanceForm(ModelForm):
    class Meta:
        model = Instance
        fields = '__all__'
        exclude = ['number_risk_articles', 'articles', 'created', 'updated']

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
        exclude = ['number_risk_statements', 'score']