import book as bk, bookinventory as bi, profile as pf


# -----------------------------
# For performance profiling
# -----------------------------
def find_book_ntimes(inven, name, n):
    for idx in xrange(0, n):
        inven.find(name)
        
def find_bsearch_book_ntimes(inven, name, n):
    for idx in xrange(0, n):
        inven.find_bsearch(name)



if __name__ == '__main__':
    inven = bi.BookInventory()


    for idx in xrange(0,10000):
        book = bk.Book(
            "mybook{:04}".format(idx),
            "myauthor{:04}".format(idx),
            "mypublisher{:04}".format(idx),
            idx + 1000)
    
        inven.add(book)


    #----------------
    # Test
    #----------------
    print "# Test 1"
    book = inven.find("mybook0123")
    book.show()
    print


    print "# Test 2"
    book = inven.find("mybook0123")     # implement Book.set_price()
    book.set_price(9999)
    
    book = inven.find("mybook0123")
    if book:
        book.show()
    else:
        print "Not in the inventory"
    print 


    print "# Test 3"
    inven.remove("mybook0123")          # implement BookInventory.remove()
    book = inven.find("mybook0123")
    if book:
        book.show()
    else:
        print "Not in the inventory"
    print 


    print "# Test 4"
    pf.run('find_book_ntimes(inven, "mybook0000", 10000)')     # performance evaluation of sequential search
    pf.run('find_book_ntimes(inven, "mybook0123", 10000)')     # *this book is not in the inventory
    pf.run('find_book_ntimes(inven, "mybook9999", 10000)')


    print "# Test 4 - bsearch"
    pf.run('find_bsearch_book_ntimes(inven, "mybook0000", 10000)')     # implement BookInventory.find_bsearch()
    pf.run('find_bsearch_book_ntimes(inven, "mybook0123", 10000)')
    pf.run('find_bsearch_book_ntimes(inven, "mybook9999", 10000)')





