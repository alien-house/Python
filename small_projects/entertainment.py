import media

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://lumiere-a.akamaihd.net/v1/images/open-uri20150422-12561-wt2it4_fbf729c8.jpeg",
                        "https://www.youtube.com/watch?v=NBepTulmSMw"
                        )

print(toy_story.storyline)

avatar = media.Movie("Avatar",
                       "A story of a avator",
                       "http://www.ohmygore.com/dvds/fox/avatar/01.jpg",
                       "https://www.youtube.com/watch?v=cX0R3mXaod8"
                       )
avatar.show_trailer()


betterwatch = media.Movie("Better Watch Out",
                       "A story of a Better Watch Out",
                       "",
                       "https://www.youtube.com/watch?v=cX0R3mXaod8"
                       )


badbatch = media.Movie("The Bad Batch",
                       "A story of The Bad Batch",
                       "http://www.ohmygore.com/dvds/fox/avatar/01.jpg",
                       "https://www.youtube.com/watch?v=OUqfP1S-9ok"
                       )

print(media.Movie.__doc__)
