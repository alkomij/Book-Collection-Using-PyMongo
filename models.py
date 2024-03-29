from dataclasses import dataclass

@dataclass
class Book:
    ISBN: int
    Title: str
    AuthorID: int
    GenreID: int
    TagID: int
    BookType: str
    Series: str
    BookNumber: int
    Edition: str