import unittest
import advent7

f = advent7.File('test_file', 100)
d1 = advent7.Directory('test_directory')
d1.objects.append(f)

d2 = advent7.Directory('test')
d2.objects.append(d1)
d2.objects.append(f)


class FileTest(unittest.TestCase):

    def test_names(self):
        self.assertIsInstance(f.name, str)  # add assertion here

    def test_size(self):
        self.assertEqual(f.get_size(), 100)


class DirectoryTest(unittest.TestCase):

    def test_size(self):
        self.assertEqual(f.get_size(), d1.get_size())
        self.assertEqual(f.get_size() * 2, d2.get_size())


if __name__ == '__main__':
    unittest.main()
