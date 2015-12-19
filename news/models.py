# -*- coding: utf-8 -*-


from django.db import models
from django.db.models.query_utils import Q


class NewsModel(models.Model):
    news_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=64)
    image_url = models.CharField(max_length=128, null=True)
    author = models.CharField(max_length=32)
    date_time = models.DateTimeField()
    keywords = models.CharField(max_length=128, null=True)
    original_link = models.CharField(max_length=128)
    source = models.CharField(max_length=16)
    content = models.TextField()
    reading_number = models.IntegerField(default=0)
    agree_number = models.IntegerField(default=0)
    disagree_number = models.IntegerField(default=0)
    category = models.IntegerField()

    class Meta:
        db_table = 'news'

    def detail(self):
        return {
            'news_id': self.news_id,
            'title': self.title,
            'author': self.author,
            'content': self.content,
            'keywords': [keyword for keyword in self.keywords.strip(",")],
            'category': self.category,
            'reading_number': self.reading_number,
            'agree_number': self.agree_number,
            'disagree_number': self.disagree_number,
            'source': self.source,
            'image_url': self.image_url,
            'original_link': self.original_link,
            'date_time': self.date_time
        }


class DoNewsModel(object):
    @classmethod
    def get_by_id(cls, news_id):
        try:
            news = NewsModel.objects.get(news_id=news_id)
        except NewsModel.DoesNotExist:
            return None
        return news.detail()

    @classmethod
    def get_news(cls, page_num, page_size, category):
        condition = Q()
        if category:
            condition &= Q(category=category)
        news = NewsModel.objects.filter(category=category). \
            order_by('-date_time')[page_num * page_size:(page_num + 1) * page_size]
        return [news.detail() for news in news]

    @classmethod
    def add(cls, param):
        NewsModel.objects.create(**param)
        return {'news_id':param['news_id']}

    @classmethod
    def delete_by_id(cls, news_id):
        try:
            news = NewsModel.objects.get(news_id=news_id)
        except NewsModel.DoesNotExist:
            return NewsModel.DoesNotExist
        news.delete()

    @classmethod
    def delete_by_ids(cls, news_ids):
        NewsModel.objects.filter(news_id__in=news_ids).delete()

