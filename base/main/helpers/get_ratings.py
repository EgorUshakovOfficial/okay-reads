from book.models import Review

def get_ratings(books):
    # Ratings
    ratings = []

    # Calculates average review rating of each book
    for book in books:
        # Review of each specified book
        reviews = Review.objects.filter(book=book.book_id)

        # Book has not been reviewed
        if len(reviews) == 0:
            ratings.append(None)

        else:
            # Initialize average review rating for the book
            avg_review_rating = 0

            # Calculates the average review rating
            for review in reviews:
                avg_review_rating += review.rating / len(reviews)


            # Appends the rating to the list of ratings
            ratings.append(f'{avg_review_rating:.1f}')

    return ratings