# coding: utf-8

import bookinventory.book as book
import bookinventory.bookinventory as inventory

import sys, unittest



class TestInventory(unittest.TestCase):
    """
    Inventoryクラスに関わるユニットテストを実装。
    """
    def setUp(self):
        self.inven = inventory.BookInventory()

    def tearDown(self):
        pass


    def testAddBookIntoInventory(self):
        """
        新しいBookオブジェクトを生成してInventoryへ格納するadd()関数をテストする。
        正しく保存されたかを確認するため、生成したonebookオブジェクトとInventory
        に保存されたオブジェクトの比較を行う。
        """
        # 新しい書籍オブジェクトの生成
        onebook = book.Book(
            "mybook",
            "myauthor",
            "mypublisher",
            1000)

        # 在庫目録へ追加
        self.inven.add(onebook)

        # 正しく追加されたかテスト
        found = self.inven.find("mybook")
        self.assertItemsEqual(
            found.__dict__, 
            onebook.__dict__,
            msg = "Added book is not equal to the original book!"
        )


    def testRemoveBookFromInventory(self):
        """
        在庫目録(self.inven)からタイトルが「mybook1234」の書籍
        を削除し、正しく削除されたのかをチェックするテストを行う。
        """
        for idx in xrange(0,10000):
            onebook = book.Book(
                "mybook{:04}".format(idx),
                "myauthor{:04}".format(idx),
                "mypublisher{:04}".format(idx),
                idx + 1000)
            self.inven.add(onebook)

        # TODO: テストコードをここへ追加
        # self.asssetTrueは適切なものに変更してください。
        # ...
        # ...
        self.assertTrue(False)

    def testFindBookThatExistsInTheInventory(self):
        """
        ある書籍(例、「mybook1234」)が在庫目録に存在するのかを
        チェックするテストを行う。
        """
        for idx in xrange(0,10000):
            onebook = book.Book(
                "mybook{:04}".format(idx),
                "myauthor{:04}".format(idx),
                "mypublisher{:04}".format(idx),
                idx + 1000)
            self.inven.add(onebook)

        # TODO: テストコードをここへ追加
        # self.asssetTrueは適切なものに変更してください。
        # ...
        # ...
        self.assertTrue(False)
       

    def testFindBookThatDoesNotExistInTheInventory(self):
        """
        在庫目録に存在しない書籍(例、「not_in_my_inven」)を検索すると
        正しい(None)を返すのかをテスト。
        """
        for idx in xrange(0,10000):
            onebook = book.Book(
                "mybook{:04}".format(idx),
                "myauthor{:04}".format(idx),
                "mypublisher{:04}".format(idx),
                idx + 1000)
            self.inven.add(onebook)
        
        # TODO: テストコードをここへ追加
        # self.asssetTrueは適切なものに変更してください。
        # ...
        # ...
        self.assertTrue(False)


    def testFindAndFindBSearchResults(self):
        """
        新しく実装したfind_bsearch()関数がもともとのfind()関数と同じく動作
        するのかをテスト。
        """
        for idx in xrange(0,10000):
            onebook = book.Book(
                "mybook{:04}".format(idx),
                "myauthor{:04}".format(idx),
                "mypublisher{:04}".format(idx),
                idx + 1000)
            self.inven.add(onebook)

        # TODO: テストコードをここへ追加
        # self.asssetTrueは適切なものに変更してください。
        # ...
        # ...
        self.assertTrue(False)


    def testRemoveBookFromInventoryWithDuplicateBooks(self):
        """
        在庫目録(self.inven)からタイトルが「mybook1234」の書籍
        を削除し、正しく削除されたのかをチェックするテストを行う。
        ただし、在庫目録には与えられた名前の書籍が複数存在する。
        """
        indices = [0, 1, 2, 2, 2, 3]
        for idx in indices:
            onebook = book.Book(
                "mybook{:04}".format(idx),
                "myauthor{:04}".format(idx),
                "mypublisher{:04}".format(idx),
                idx + 1000)
            self.inven.add(onebook)

        # TODO: テストコードをここへ追加
        # self.asssetTrueは適切なものに変更してください。
        # ...
        # ...
        self.assertTrue(False)


if __name__ == '__main__':
    unittest.main()
    sys.exit(0)


