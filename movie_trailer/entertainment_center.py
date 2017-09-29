from SmrutiMohantyRepo.FullStackWeb.movies_trailer import media , fresh_tomatoes


"""
Toy Story Movie Details
"""
ts_title="Toy Story"
ts_storyline="A cowboy doll is profoundly threatened " \
             "and jealous when a new spaceman figure supplants him as top toy in a boy's room."
ts_poster_image_url="https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg"
ts_trailer_youtube_url="https://youtu.be/KYz2wyBy3kc?t=5s"

toy_story = media.Movie(ts_title,ts_storyline,ts_poster_image_url,ts_trailer_youtube_url)

"""
Avatar Movie
"""

a_title="Avatar"
a_storyline="A paraplegic marine dispatched to the moon Pandora on a " \
            "unique mission becomes torn between following his orders " \
            "and protecting the world he feels is his home"
a_poster_image_url = "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg"
a_trailer_youtube_url="https://youtu.be/d1_JBMrrYw8?t=4s"

avatar = media.Movie(a_title,a_storyline,a_poster_image_url,a_trailer_youtube_url)

"""
The Boss Baby
"""

b_title="The Boss Baby"
b_storyline="A suit-wearing, briefcase-carrying baby pairs up with his 7-year old" \
            " brother to stop the dastardly plot of the CEO of Puppy Co."
b_poster_image_url="https://upload.wikimedia.org/wikipedia/en/0/0e/The_Boss_Baby_poster.jpg"
b_trailer_youtube_url="https://youtu.be/k397HRbTtWI?t=1s"

bossBaby = media.Movie(b_title,b_storyline,b_poster_image_url,b_trailer_youtube_url)


"""
Mother!
"""

m_title="Mother !"
m_storyline="A couple's relationship is tested when uninvited guests arrive at their home, disrupting their tranquil existence."
m_poster_image_url="https://upload.wikimedia.org/wikipedia/en/9/94/Mother%212017.jpg"
m_trailer_youtube_url="https://youtu.be/XpICoc65uh0?t=7s"

mother = media.Movie(m_title,m_storyline,m_poster_image_url,m_trailer_youtube_url)


"""
M.S. Dhoni: The Untold Story

"""

dhoni_title="M.S. Dhoni: The Untold Story"
dhoni_storyline="The untold story of Mahendra Singh Dhoni's journey from ticket " \
                "collector to trophy collector - the world-cup-winning captain of the Indian Cricket Team."
dhoni_poster_image_url="https://upload.wikimedia.org/wikipedia/en/3/33/M.S._Dhoni_-_The_Untold_Story_poster.jpg"
dhoni_trailer_youtube_url="https://youtu.be/6L6XqWoS8tw"

dhoni = media.Movie(dhoni_title,dhoni_storyline,dhoni_poster_image_url,dhoni_trailer_youtube_url)


"""
Dangal
"""

Dangal_title="Dangal"
Dangal_storyline="Former wrestler Mahavir Singh Phogat " \
                 "and his two wrestler daughters struggle towards glory at " \
                 "the Commonwealth Games in the face of societal oppression."
Dangal_poster_image_url="https://upload.wikimedia.org/wikipedia/en/9/99/Dangal_Poster.jpg"
Dangal_trailer_youtube_url="https://youtu.be/x_7YlGv9u1g"

Dangal = media.Movie(Dangal_title,Dangal_storyline,Dangal_poster_image_url,Dangal_trailer_youtube_url)

#Creating List of Movies.
movies=[toy_story,avatar,bossBaby,mother,dhoni,Dangal]

#Launch the WebSite
fresh_tomatoes.open_movies_page(movies)