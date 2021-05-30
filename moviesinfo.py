import imdb
z = imdb.IMDb()
movie_name = input("Enter the name of the movie:-")
movies =z.search_movie(str(movie_name))
index = movies[0].getID()
movie = z.get_movie(index)
movie_title = movie['title']
movie_year = movie['year']
movie_cast = movie['cast']
list_of_cast = ','.join(map(str, movie_cast))
print("Title of movie is:-",movie_title)
print("Year of release of movie is:-",movie_year)
print("cast of movie is:=",movie_cast)
