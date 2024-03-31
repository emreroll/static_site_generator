import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)
    def test_eq1(self):
        node = TextNode('emre','bold')
        node2 = TextNode('emre','bold')
        self.assertEqual(node, node2)

if __name__ == "__main__":
    unittest.main()
