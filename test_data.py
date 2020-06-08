from unittest import TestCase

from data import Emotions
from chat import response


class TestData(TestCase):
    def test_1(self):
        response("buồn bã")

    def test_2(self):
        response("ngạc nhiên")
        response("buồn")
        response("vui")
        response("hạnh phúc")
        response("bất ngờ")
        response("giận dữ")
        response("kinh tởm")
        response("sợ hãi")

    def test_level_1(self):
        term = "hậm hực"
        emotion = Emotions.find(term)
        print(emotion)
        levels = ['tức giận', 'điên tiết', 'hậm hực']
        self.assertEqual(emotion.levels, levels)

    def test_level_2(self):
        term = "tin tưởng"
        response(term)
        emotion = Emotions.find(term)
        levels = ["tán thành", "ngưỡng mộ"]
        self.assertEqual(emotion.levels, levels)
        self.assertIsNotNone(emotion.levels)

    def test_find_1(self):
        term = "buồn"
        emotion = Emotions.find(term)
        self.assertEqual(emotion.name, term)

    def test_find_2(self):
        term = "giận"
        emotion = Emotions.find(term)
        self.assertEqual(emotion.name, "giận dữ")
        term = "cáu"
        emotion = Emotions.find(term)
        self.assertEqual(emotion.name, "giận dữ")

    def test_attr_1(self):
        term = "giận"
        emotion = Emotions.find(term)
        synonym_terms = {'cáu', 'hậm hực', 'tức giận', 'điên tiết', 'giận'}
        self.assertEqual(emotion.synonym, synonym_terms)