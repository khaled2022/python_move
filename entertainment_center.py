import fresh_tomatoes
import media
toy_story = media.Movie("toy Story",
                        "A story of a boy and his toys that come to life",
                        "90969854_223288249036116_7253380046960721920_o.jpg",
                        "https://www.youtube.com/watch?v=wmiIUN-7qhE")
avatar = media.Movie("Avatar",
                     "A marine on alien planet",
                     "avatar.jpg",
                     "https://www.youtube.com/watch?v=yUXd-enstO8")
movie_1917 = media.Movie("1917",
                         "Movieclips Trailers",
                         "1917.jpg",
                         "https://www.youtube.com/watch?v=TOkun-ZityQ")
spider_man = media.Movie("Spider Man",
                         "In Cinemas Dec 23, 2016",
                         "spider man.jpg",
                         "https://www.youtube.com/watch?v=x_7YlGv9u1g")
Bella_Ciao = media.Movie("Bella Ciao",
                         " Free Guy Trailer starring Ryan Reynolds!",
                         "bella.jpg",
                         "https://www.youtube.com/watch?v=2niQA2aYFVw")
captain_america = media.Movie("Captain_America",
                         "MARVEL'S THE FALCON AND THE WINTER SOLDIER Teaser Trailer ",
                         "captin.jpg",
                         "https://www.youtube.com/watch?v=aOOBA4vIeNk")
movies = [toy_story , avatar, movie_1917, spider_man,Bella_Ciao, captain_america]
fresh_tomatoes.open_movies_page(movies)
