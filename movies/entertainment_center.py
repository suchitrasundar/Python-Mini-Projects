import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "Toy Story is a 1995 American computer-animated buddy comedy adventure film produced by Pixar Animation Studios",
                        "https://en.wikipedia.org/wiki/File:Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
print(toy_story.storyline)

avatar=media.Movie("Avatar",
                   "It is directed by James Cameron",
                   "https://en.wikipedia.org/wiki/File:Avatar-Teaser-Poster.jpg",
                   "https://www.youtube.com/watch?v=cRdxXPV9GNQ")
print(avatar.storyline)
avatar.show_trailer()

movies = [toy_story,avatar]
fresh_tomatoes.open_movies_page(movies)
print(media.Movie.VALID_RATINGS)
