import pytest

from bookstore.book import Book
from bookstore.book_repository import InMemoryBookRepository
from bookstore.services.book_filtering_service import BookFilterService
from bookstore.services.bookstore_service import BookStoreService


# TODO: Create a fixture that returns a BookService instance
@pytest.fixture
def create_book_service():
    """
    INSTRUCTIONS:
    - Create and return a BookService instance
    - Use InMemoryBookRepository for storage
    - Use default BookFilterService
    
    HINTS:
    repository = ...
    book_filter_service = ...
    return BookService(repository, book_filter_service)
    """
    repository = InMemoryBookRepository()
    book_filter_service = BookFilterService()
    return BookStoreService(repository, book_filter_service)

@pytest.fixture
# TODO: Create a fixture that returns a sample book for testing
def create_sample_book():
    """
    INSTRUCTIONS:
    - Create a Book instance with sample data
    - Use realistic values for title, author, genre, and price

    REQUIREMENTS:
    - Book should have valid, testable attributes
    """
    book = Book(title="The Great Gatsby", author="F. Scott Fitzgerald", genre="Classic", price=10.99)
    return book


# INFO: For the following tests, use only the BookService instance created by the fixture
def test_add_book(create_book_service, create_sample_book):
    """
    TESTING OBJECTIVES:
    1. Create a book service using the fixture
    2. Create a sample book using the fixture
    3. Add the book to the service
    4. Verify:
       - Book has a non-None ID
       - Book attributes match the original book
    
    HINTS:
    - Use assertions to check book details
    - Verify ID is automatically assigned
    """
    # Your implementation here
    
    book_service = create_book_service
    sample_book = create_sample_book
    added_book = book_service.add_book(sample_book)
    
    assert added_book.id is not None, "Book ID should be assigned"
    assert added_book.title == sample_book.title, "Book title should match"
    assert added_book.author == sample_book.author, "Book author should match"
    assert added_book.price == sample_book.price, "Book price should match"


def test_add_book_validation(create_book_service):
    """
    TESTING OBJECTIVES:
    1. Attempt to add a book with invalid data
    2. Verify appropriate exception is raised
    
    REQUIREMENTS:
    - Test scenarios like:
      * Book with empty title
      * Book with empty author
    
    HINTS:
    - Use pytest.raises() to check for exceptions
    """
    # Your implementation here
    
    service = create_book_service
    
    # Test empty title
    with pytest.raises(ValueError, match="Book must have a title and author"):
        bad_book = Book(title="", author="Valid Author", genre="Tech", price=10.0)
        service.add_book(bad_book)
        
    # Test empty author
    with pytest.raises(ValueError, match="Book must have a title and author"):
        bad_book = Book(title="Valid Title", author="", genre="Tech", price=10.0)
        service.add_book(bad_book)



# INFO: Here you should use @pytest.mark.parametrize to test multiple genres

@pytest.mark.parametrize("search_genre, expected_count", [
    ("Fantasy", 2),    # Should find Hobbit and Harry Potter
    ("fantasy", 2),    # Case-insensitive check
    ("Sci-Fi", 1),     # Should find Dune
    ("History", 0),    # Genre that doesn't exist in our list
    (None, 3)          # No filter should return all books
])

def test_get_books_by_genre(create_book_service, search_genre, expected_count):
    """
    TESTING OBJECTIVES:
    1. Add multiple books with different genres
    2. Filter books by specific genres
    3. Verify:
       - Only books of the specified genre are returned
       - Filtering is case-insensitive
    
    REQUIREMENTS:
    - Add books across multiple genres
    - Test filtering with different genre inputs
    
    HINTS:
    - Use service's get_books() method with genre parameter
    - Check length and genre of returned books
    """
    # Your implementation here
    
    service = create_book_service
    books_to_add = [
        Book("The Hobbit", "J.R.R. Tolkien", "Fantasy", 25.0),
        Book("Harry Potter", "J.K. Rowling", "Fantasy", 20.0),
        Book("Dune", "Frank Herbert", "Sci-Fi", 30.0),
    ]
    
    for b in books_to_add:
        service.add_book(b)
        
    results = service.get_books(genre=search_genre)
    
    assert len(results) == expected_count
    if search_genre:
        for book in results:
            assert book.genre.lower() == search_genre.lower()

@pytest.mark.parametrize("min_price, max_price, expected_count", [
    (15.0, None, 3),   # Books priced at $15 or above
    (None, 25.0, 2),   # Books priced at $25 or below
    (15.0, 25.0, 1),   # Books priced between $15 and $25
])
# INFO: Here you should use @pytest.mark.parametrize to test multiple price ranges
def test_price_range_filtering(create_book_service, min_price, max_price, expected_count):
    """
    TESTING OBJECTIVES:
    1. Add books at different price points
    2. Test filtering by:
       - Minimum price
       - Maximum price
       - Combined price range
    
    REQUIREMENTS:
    - Verify correct number of books returned
    - Ensure only books within price range are included
    
    HINTS:
    - Add books with varied prices
    - Use get_books() with min_price and max_price
    - Test edge cases and different price combinations
    """
    # Your implementation here
    service = create_book_service
    books_to_add = [
        Book("Book A", "Author A", "Genre A", 10.0),
        Book("Book B", "Author B", "Genre B", 20.0),
        Book("Book C", "Author C", "Genre C", 30.0),
        Book("Book D", "Author D", "Genre D", 40.0),
    ]
    
    for b in books_to_add:
        service.add_book(b)
        
    results = service.get_books(min_price=min_price, max_price=max_price)
    
    assert len(results) == expected_count
    
    for book in results:
        if min_price is not None:
            assert book.price >= min_price, f"Book price {book.price} should be >= {min_price}"
        if max_price is not None:
            assert book.price <= max_price, f"Book price {book.price} should be <= {max_price}"


def test_update_book(create_book_service, create_sample_book):
    """
    TESTING OBJECTIVES:
    1. Add a book to the service
    2. Update the book's details
    3. Verify:
       - Specific attributes can be updated
       - Updated values are correct
       - Other attributes remain unchanged
    
    REQUIREMENTS:
    - Test updating multiple attributes
    - Ensure update works for different book properties
    
    HINTS:
    - Use update_book() method
    - Compare book before and after update
    """
    book_service = create_book_service
    sample_book = create_sample_book
    
    added_book = book_service.add_book(sample_book)
    original_author = added_book.author
    original_genre = added_book.genre
    
    updated_book = book_service.update_book(added_book.id, title="The Great Gatsby - Updated", price=12.99)
    
    assert updated_book is not None, "Updated book should not be None"
    assert updated_book.title == "The Great Gatsby - Updated", "Book title should be updated"
    assert updated_book.price == 12.99, "Book price should be updated"
    
    assert updated_book.author == original_author, "Author should not have changed"
    assert updated_book.genre == original_genre, "Genre should not have changed"
    assert updated_book.id == added_book.id, "ID should never change"
    


def test_remove_book(create_book_service, create_sample_book):
    """
    TESTING OBJECTIVES:
    1. Add a book to the service
    2. Remove the book
    3. Verify:
       - Book is successfully removed
       - Attempting to retrieve the book returns None
    
    REQUIREMENTS:
    - Test successful book removal
    - Test removing a non-existent book
    
    HINTS:
    - Use remove_book() method
    - Check return value of remove operation
    - Verify book is no longer in the service
    """
    # Your implementation here
    service = create_book_service
    sample_book = create_sample_book
    added_book = service.add_book(sample_book)
    
    removed = service.remove_book(added_book.id)
    
    assert removed, "Book should be successfully removed"
    retrieved_book = service.get_book_by_id(added_book.id)
    assert retrieved_book is None, "Removed book should not be retrievable"
    
    assert service.get_book_by_id(999) is None, "Non-existent book should return None"
    pass
