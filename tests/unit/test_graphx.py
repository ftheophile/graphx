import unittest

from graphx import Graphx


class TestGraphx(unittest.TestCase):

    def setUp(self):
        self.g = Graphx()

    def tearDown(self):
        del self.g

    def test_empty_graph(self):
        self.assertEqual(len(self.g.get_nodes()), 0, "should be 0")
        self.assertEqual(len(self.g.get_edges()), 0, "should be 0")

    def test_add_node_to_empty_graph(self):
        a = 7
        self.g.add_node(a)
        self.assertEqual(len(self.g.get_nodes()), 1, "should be 1")
        self.assertEqual(self.g.get_nodes()[0], a, f"should be {a}")
        self.assertEqual(len(self.g.get_edges()), 0, "should be 0")

    def test_multiple_nodes_to_empty_graph(self):
        self.g.add_nodes([1, 2])
        result = len(self.g.get_nodes())
        result1 = len(self.g.get_edges())
        self.assertEqual(result, 2, "should be 2")
        self.assertEqual(result1, 0, "should be 0")

    def test_add_edge_to_empty_graph(self):
        self.g.add_edge((1, 2))
        result = len(self.g.get_nodes())
        result1 = len(self.g.get_edges())
        self.assertEqual(result, 2, "should be 2")
        self.assertEqual(result1, 1, "should be 1")

    def test_add_multiple_edges_to_empty_graph(self):
        self.g.add_edges([(1, 2), (2, 3)])
        result = len(self.g.get_nodes())
        result1 = len(self.g.get_edges())
        self.assertEqual(result, 3, "should be 3")
        self.assertEqual(result1, 2, "should be 2")

    def test_add_multiple_nodes_and_then_edges_to_empty_graph(self):
        self.g.add_nodes([1, 2, 4])
        self.g.add_edges([(1, 2), (2, 3)])
        result = len(self.g.get_nodes())
        result1 = len(self.g.get_edges())
        self.assertEqual(result, 4, "should be 4")
        self.assertEqual(result1, 2, "should be 2")

    def test_add_multiple_edges_and_then_distinct_nodes_to_empty_graph(self):
        self.g.add_edges([(1, 2), (2, 3)])
        self.g.add_nodes([5, 4])
        result = len(self.g.get_nodes())
        result1 = len(self.g.get_edges())
        self.assertEqual(result, 5, "should be 5")
        self.assertEqual(result1, 2, "should be 2")

    def test_add_multiple_edges_and_then_existing_nodes_to_graph_fails(self):
        self.g.add_edges([(1, 2), (2, 3)])
        self.assertRaises(Exception, self.g.add_node, 2)
        self.assertRaises(Exception, self.g.add_nodes, [1, 2, 4])

    def test_add_multiple_edges_and_then_existing_nodes_to_graph_succeeds(self):
        self.g.add_edges([(1, 2), (2, 3)])
        self.g.add_nodes([1, 2], False)
        result = len(self.g.get_nodes())
        self.assertEqual(result, 3, "should be 3")
        self.assertEqual(len(self.g.get_edges()), 2, "should be 2")

    def test_add_new_edge_to_connected_graph(self):
        self.g.add_edges([(1, 2), (1, 3), (2, 3)])
        self.g.add_edge((1, 4))
        result = len(self.g.get_nodes())
        result1 = len(self.g.get_edges())
        self.assertEqual(result, 4, "should be 4")
        self.assertEqual(result1, 4, "should be 4")

    def test_add_existing_edge_to_connected_graph_default(self):
        self.g.add_edges([(1, 2), (1, 3), (2, 3)])
        self.g.add_edge((1, 2))
        result = len(self.g.get_nodes())
        result1 = len(self.g.get_edges())

        self.assertEqual(result, 3, "should be 3")
        self.assertEqual(result1, 3, "should be 3")

    def test_add_edge_with_new_node_to_graph_fails(self):
        self.g.add_edges([(1, 2), (1, 3)])
        self.assertRaises(Exception, self.g.add_edge, (1, 4), False, False)
        self.assertRaises(Exception, self.g.add_edges, [(1, 2), (1, 5)], False, False)

    def test_add_existing_edge_to_graph_fails(self):
        self.g.add_edges([(1, 2), (1, 3), (2, 4)])
        self.assertRaises(Exception, self.g.add_edge, (1, 2), True)
        self.assertRaises(Exception, self.g.add_edges, [(1, 3), (1, 5)], True)

    # def test_add_edge_to_disconnected_graph(self):
    #     self.gd.add_edge((1,2))
    #     result = len(self.gd.get_nodes())
    #     result1 = len(self.gd.get_edges())
    #     self.assertEqual(result, 3, "should be 3")
    #     self.assertEqual(result1, 1, "should be 1")
    #
    #
    # def test_multiple_edges_to_connected_graph(self):
    #     self.gc.add_edges([(4, 5), (3, 4)])
    #     result = len(self.gc.get_nodes())
    #     result1 = len(self.gc.get_edges())
    #     self.assertEqual(result, 5, "should be 5")
    #     self.assertEqual(result1, 5, "should be 5")
    #
    # def test_multiple_edges_to_disconnected_graph(self):
    #
    #     self.g.add_edges([(1, 2), (2, 3), (4, 5), (3, 4)])
    #     result = len(self.gd.get_nodes())
    #     result1 = len(self.gd.get_edges())
    #     self.assertEqual(result, 5, "should be 5")
    #     self.assertEqual(result1, 4, "should be 4")

    # def test_connected_graph(self):
    #     gc = Graphx([1, 2, 3], [(1, 2), (1, 3), (2, 3)])
    #     result = len(gc.get_nodes())
    #     result1 = len(gc.get_edges())
    #     self.assertEqual(result, 3, "should be 3")
    #     self.assertEqual(result1, 3, "should be 3")
    #
    # def test_disconnected_graph(self):
    #     gd = Graphx([1, 2, 3])
    #     result = len(gd.get_nodes())
    #     result1 = len(gd.get_edges())
    #     self.assertEqual(result, 3, "should be 3")
    #     self.assertEqual(result1, 0, "should be 0")

    # def test_add_node_to_connected_graph(self):
    #     self.gc.add_node([5])
    #     result = len(self.gc.get_nodes())
    #     result1 = len(self.gc.get_edges())
    #     self.assertEqual(result, 4, "should be 4")
    #     self.assertEqual(result1, 3, "should be 3")
    #
    # def test_add_node_to_disconnected_graph(self):
    #     self.gd.add_node([5])
    #     result = len(self.gd.get_nodes())
    #     result1 = len(self.gd.get_edges())
    #     self.assertEqual(result, 4, "should be 4")
    #     self.assertEqual(result1, 0, "should be 0")
    #

    # def test_multiple_nodes_to_connected_graph(self):
    #     self.gc.add_nodes([4, 5])
    #     result = len(self.gc.get_nodes())
    #     result1 = len(self.gc.get_edges())
    #     self.assertEqual(result, 5, "should be 5")
    #     self.assertEqual(result1, 3, "should be 3")
    #
    # def test_multiple_nodes_to_disconnected_graph(self):
    #     self.gd.add_nodes([4, 5])
    #     result = len(self.gd.get_nodes())
    #     result1 = len(self.gd.get_edges())
    #     self.assertEqual(result, 5, "should be 5")
    #     self.assertEqual(result1, 0, "should be 0")


if __name__ == '__main__':
    unittest.main()
