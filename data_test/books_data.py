from models.books import Book


class BooksData:
    book1 = Book(
        isbn="9781593275846",
        title="Eloquent JavaScript, Second Edition",
        subTitle="A Modern Introduction to Programming",
        author="Marijn Haverbeke",
        publish_date="2014-12-14T00:00:00.000Z",
        publisher="No Starch Press",
        pages=472,
        description="JavaScript lies at the heart of almost every modern web application, from social apps to the newest browser-based games. Though simple for beginners to pick up and play with, JavaScript is a flexible, complex language that you can use to build full-scale ",
        website="http://eloquentjavascript.net/"
    )
    book2 = Book(
        isbn="9781449325862",
        title="Git Pocket Guide",
        subTitle="A Working Introduction",
        author="Richard E. Silverman",
        publish_date="2020-06-04T08:48:39.000Z",
        publisher="O'Reilly Media",
        pages=234,
        description="This pocket guide is the perfect on-the-job companion to Git, the distributed version control system. It provides a compact, readable introduction to Git for new users, as well as a reference to common commands and procedures for those of you with Git experience",
        website="http://chimera.labs.oreilly.com/books/1230000000561/index.html"
    )

    all_books = {book1.isbn: book1,
                 book2.isbn: book2}
