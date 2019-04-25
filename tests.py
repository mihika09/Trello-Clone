import unittest
from app.dbs import Database
from app.boards.queries import BoardQuery
import uuid


class Boards(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        Database().run_query("DROP TABLE card")
        Database().run_query("DROP TABLE list")
        Database().run_query("DROP TABLE board")
        Database().close_connection()

    def test_board(self):

        q = BoardQuery().get_all_boards()
        r = Database().run_query(q)
        self.assertEqual(r, [])

        bid1 = str(uuid.uuid1())
        q = BoardQuery().create_board({'id': bid1, 'title': 'Board#1'})
        Database().run_query(q)

        bid2 = str(uuid.uuid1())
        q = BoardQuery().create_board({'id': bid2, 'title': 'Board#2'})
        Database().run_query(q)

        q = BoardQuery().get_all_boards()
        r = Database().run_query(q)
        self.assertEqual(len(r), 2)

        q = BoardQuery().update_board({'title': 'Board#3'}, bid2)
        Database().run_query(q)
        q = BoardQuery().get_board_by_id(bid2)
        r = Database().run_query(q)
        self.assertEqual(r[0]['id'], bid2)
        self.assertEqual(r[0]['title'], 'Board#3')

        q = BoardQuery().delete_board(bid2)
        Database().run_query(q)
        q = BoardQuery().get_board_by_id(bid2)
        r = Database().run_query(q)
        self.assertEqual(r, [])
        q = BoardQuery().get_all_boards()
        r = Database().run_query(q)
        self.assertEqual(len(r), 1)


if __name__ == '__main__':
    unittest.main(verbosity=2)

