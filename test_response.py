from unittest import TestCase

from data import find
from script import response


class TestClagi ssify(TestCase):
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

    def test_3(self):
        term = "tin tưởng"
        response(term)
        emotion = find(term)
        levels = ["tán thành", "tin tưởng", "ngưỡng mộ"]
        self.assertEqual(emotion.levels, levels)
        self.assertIsNotNone(emotion.levels)
