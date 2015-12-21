# -*- coding: utf-8 -*-

import unittest
# noinspection PyUnresolvedReferences
from datetime import datetime, timedelta

from models import DoNewsModel, News


class NewsModelTest(unittest.TestCase):
    def setUp(self):
        News.objects.create(
            title=u'新闻',
            image_url='pyorc/aa.jpg',
            author=u'新闻',
            date_time=datetime.today() + timedelta(minutes=5),
            keywords=u"苹果,科技",
            original_link='http://www.baidu.com',
            source=u'腾讯',
            content=u'新闻',
            reading_number=10,
            agree_number=1,
            disagree_number=2,
            category=1,
            news_id=1
        )

    def test_get_by_id(self):
        news = DoNewsModel.get_by_id(1)
        self.assertIsNotNone(news)

    def test_get_news(self):
        news = DoNewsModel.get_news(0, 10, 1)
        self.assertEqual(len(news), 1)

    def test_delete(self):
        News.objects.create(
            title='新闻',
            image_url='pyorc/aa.jpg',
            author=u'小白',
            date_time=datetime.today() + timedelta(minutes=5),
            keywords=u"哈哈",
            original_link='http://www.baidu.com',
            source=u'百度',
            content=u'很好',
            reading_number=10,
            agree_number=1,
            disagree_number=2,
            category=1,
            news_id=10
        )

        flag = DoNewsModel.delete_by_id(10)
        self.assertIsNone(flag)

    def test_add(self):
        data = {
            'title': '新闻',
            'image_url': 'pyorc/aa.jpg',
            'author': u'小白',
            'date_time': datetime.today() + timedelta(minutes=5),
            'keywords': u"哈哈",
            'original_link': 'http://www.baidu.com',
            'source': u'百度',
            'content': u'很好',
            'reading_number': 10,
            'agree_number': 1,
            'disagree_number': 2,
            'category': 1,
            'news_id': 8
        }
        news = DoNewsModel.add(data)
        self.assertIsNotNone(news)
        self.assertEqual(news['news_id'], 8)

    def test_delete(self):
        News.objects.create(
            title='新闻',
            image_url='pyorc/aa.jpg',
            author=u'小白',
            date_time=datetime.today() + timedelta(minutes=5),
            keywords=u"哈哈",
            original_link='http://www.baidu.com',
            source=u'百度',
            content=u'很好',
            reading_number=10,
            agree_number=1,
            disagree_number=2,
            category=1,
            news_id=20
        )

        flag = DoNewsModel.delete_by_ids([20, 1])
        self.assertIsNone(flag)

    def tearDown(self):
        News.objects.all().delete()
