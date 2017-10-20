import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys taht comes to life",
                        "https://www.voices.com/blog/wp-content/uploads/old_assets/voiceovertimes/wp-content/uploads/toy_story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
                     "Marine on Alien Planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=cRdxXPV9GNQ")

school_of_rock = media.Movie("School of Rock",
                             "A strict teacher try into rock band",
                             "https://static.rogerebert.com/uploads/movie/movie_poster/school-of-rock-2003/large_cREN222Yw78zvSQ9bg17Y9QZS0c.jpg",
                             "https://www.youtube.com/watch?v=XCwy6lW5Ixc")

ratatouille = media.Movie("Ratatouille",
                          "A rat who can cook makes an unusal alliance",
                          "https://images-na.ssl-images-amazon.com/images/M/MV5BMTMzODU0NTkxMF5BMl5BanBnXkFtZTcwMjQ4MzMzMw@@._V1_UY1200_CR90,0,630,1200_AL_.jpg",
                          "https://www.youtube.com/watch?v=c3sBBRxDAqk")

midnight_in_paris = media.Movie("Midnight in Paris",
                                "While on a trip to Paris, a nostalgic screenwriter finds himself mysteriously going back to 1920s",
                                "http://is5.mzstatic.com/image/thumb/Video/v4/80/5c/8f/805c8f2a-5d93-0621-2f3d-2f23ba60f775/source/1200x630bb.jpg",
                                "https://www.youtube.com/watch?v=BYRWfS2s2v4")

hunger_games = media.Movie("The hunger Games",
                           "A televised competition in which two teenagers are chosen at random to fight to the death",
                           "https://images-na.ssl-images-amazon.com/images/I/91ikvZgoHZL._SL1500_.jpg",
                           "https://www.youtube.com/watch?v=4S9a5V9ODuY")

movies = [toy_story, avatar, school_of_rock, ratatouille, midnight_in_paris,
          hunger_games]

fresh_tomatoes.open_movies_page(movies)
