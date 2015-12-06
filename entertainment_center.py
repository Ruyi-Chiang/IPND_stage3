
import media
import fresh_tomatoes

# 6 movie instances
toy_story = media.Movie("Toy Story", "A story of a boy and his toys that come to life", "https://goo.gl/XU0hRY", "https://www.youtube.com/watch?v=KYz2wyBy3kc", 81)

avatar = media.Movie("Avatar", "A marine on an alien planet", "http://goo.gl/YN3ipr", "https://www.youtube.com/watch?v=qlRriWu1zOI", 162)

the_intern = media.Movie("The Intern", "70-year-old widower Ben Whittaker (Robert De Niro) seizes the opportunity to become a senior intern at an online fashion site.", "http://goo.gl/rhhHEx", "https://www.youtube.com/watch?v=ZU3Xban0Y6A", 121)

bridge_of_spies = media.Movie("Bridge of Spies", "A Russian spy was defended by an American lawyer during the Cold War", "http://goo.gl/xD4711", "https://www.youtube.com/watch?v=mBBuzHrZBro", 141)

the_martian = media.Movie("The Martian", "A astronaut tried to go back to Earth from Mars", "http://goo.gl/hC5pbU", "https://www.youtube.com/watch?v=Ue4PCI0NamI", 144)

minions = media.Movie("Minions", "The begin of Minions", "http://goo.gl/eXSvvu", "https://www.youtube.com/watch?v=SvKmSNxFHyQ", 91)

# the list of names of movie instances
movies = [toy_story, avatar, the_intern, bridge_of_spies, the_martian, minions]

fresh_tomatoes.open_movies_page(movies)
