class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books= {}

    def get_email(self):
        return self.email


    def change_email(self, new_email):
        self.email = new_email
        print ("The user {} email has been updated to {}".format(self.name, self.email))

    def __repr__(self):
        return ("The user {}, with email: {} has read {} books".format(self.name, self.email, len(self.books.keys())))

    def __eq__(self, another):
        if self.name == another.name and self.email == another.email:
            return True
        else:
            return False

    def read_book(self, book, rating=None):
        self.books[book]= rating

    def get_average_rating(self):
        rating_accum = 0
        for value in self.books.values():
            if value != None:
                rating_accum += value
        return rating_accum / len(self.books)
                



    
class Book(object):
    def __init__(self,title,isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []
   
    def __hash__(self):
        return hash((self.title, self.isbn))


    def get_title(self):
        return self.tile

    def get_isbn(self):
        return self.isbn
    
    def set_isbn(self, new_isbn):
        self.isbn = new_isbn
        print ("The isbn has been updated from {} to {}". format(self.isbn, new_isbn))

    def add_rating(self, rating):
        if rating:
            if rating > 0 and rating < 5:
                self.ratings.append(rating)
            else:
                print("Invalid Rating")

    def __eq__(self, another_book):
        if self.title == another_book.title and self.isbn == another_book.isbn:
            return True
        else:
            return False
  
    def __repr__(self):
        return self.title

    def get_average_rating(self):
        rtg_summ = 0
        for rtg in self.ratings:
            rtg_summ += rtg
        if len(self.ratings) > 0:
            avg_rtg = rtg_summ / len(self.ratings)
        else:
            avg_rtg = 0
        return avg_rtg

    
    
class Fiction(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author

    def get_author(self, title):
        return self.author

    def __repr__(self):
        return "{title} by {author}".format(title=self.title, author=self.author)

class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn):
         super().__init__(title, isbn)
         self.subject = subject
         self.level = level

    def get_subject(self, title):
        return self.author

    def get_level(self, title):
        return self.level

    def __repr__(self):
        return "{title}, a level {level} manual on {subject}".format(title=self.title, level=self.level, subject=self.subject)


class TomeRater(object):
    def __init__(self):
        self.users = {}
        self.books = {}
    
    def create_book(self,title, isbn):
        new_book = Book (title, isbn)
        return new_book
        

    def create_novel(self, title, author, isbn):
        new_novel = Fiction(title, author, isbn)
        return new_novel

    def create_non_fiction(self, title, subject, level, isbn):
        new_non_fiction = Non_Fiction(title, subject, level, isbn)
        return new_non_fiction

    def add_book_to_user(self, book, email, rating = None):
        if not self.users[email]:
            print("No user with email {email}!".format(email=email))
        else:
            self.users[email].read_book(book, rating)
            if book in self.books:
                self.books[book] += 1
            else:
                self.books[book] = 1
            

    def add_user(self, name, email, user_books= None):       
            try:
                self.users[email]
                print("This User already exists in the system")
                exit
            except KeyError:
                domains = [".com", ".org", ".edu"]
                if not any (char in email for char in domains):
                    print ("Invalid domain in email, please re-enter")
                    return None
                elif not "@" in email:
                    print ("Invalid email, please re-enter")
                    return None
                new_user = User(name, email)
                self.users[email] = new_user    
            if user_books:
                for book in user_books:
                    self.add_book_to_user(book, email)

    def print_catalog(self):
        for item in self.books:
            print (item)           

    def print_users(self):
        for user in self.users.values():
            print (user)

    

    def most_read_book(self):
        most_read_book = None
        total_reads = 0
        for book, reads in self.books.items():
            if reads > total_reads:
                total_reads = reads
                most_read_book = book
        return most_read_book
	   
    def highest_rated_book(self):
        top_avrating = 0
        top_title = None
        for book in self.books:
            toprate = book.get_average_rating()
            if toprate > top_avrating:
                top_avrating = toprate
                top_title = book
            return book

    def most_positive_user(self):
        top_ur = 0
        top_user = None
        for user in self.users.values():
            top_usename = user.get_average_rating()
            if top_usename > top_ur:
                top_ur = top_usename
                top_user = user
        return top_user

    def isbn_audit(self, isbn):
        isbn_list = [book.get_isbn()for book in self.books.keys()]
        if isbn in isbn_list:
                return "Duplicate Found"
        else:
                return "Unique ISBN"
        return (isbn in isbn_list)




