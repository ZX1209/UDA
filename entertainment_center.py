# -*- coding: utf-8 -*-
"""
Created on Wed May 31 15:52:38 2017

@author: 14049
"""

import media
import fresh_tomatoes

#added by myself
first = media.Movie("ALL SUPERHERO MOVIES 2017 Trailer",
                        "Here are all Superhero Movies 2017 with Trailer",
                        "https://i.ytimg.com/vi/0Szbs34k3-Y/hqdefault.jpg?sqp=-oaymwEXCNACELwBSFryq4qpAwkIARUAAIhCGAE=&rs=AOn4CLDsD2y5S1NCDNV1Urdq0jfy95DUBQ",
                        "https://www.youtube.com/watch?v=0Szbs34k3-Y")

second = media.Movie("Transformers: The Last Knight Official Trailer 1 (2017) - Michael Bay Movie",
                        "Starring: Anthony Hopkins, Mark Wahlberg, and Laura Haddock",
                        "https://i.ytimg.com/vi/AntcyqJ6brc/hqdefault.jpg?custom=true&w=336&h=188&stc=true&jpg444=true&jpgq=90&sp=68&sigh=lsOcWEpy6b9YrMupSljBlDk3sdk",
                        "https://www.youtube.com/watch?v=AntcyqJ6brc")

third = media.Movie("Justice League Official Comic-Con Trailer (2017) - Ben Affleck Movie",
                        "Get Tickets - http://www.fandango.com/justiceleague...READ BELOW FOR EASTER EGGS & HIDDEN REFERENCESStarring: Gal Gadot, Jared Leto, Henry Cavill",
                        "https://i.ytimg.com/vi/fIHH5-HVS9o/hqdefault.jpg?sqp=-oaymwEXCNACELwBSFryq4qpAwkIARUAAIhCGAE=&rs=AOn4CLD_opPS-nvPO1hS12f--A5R4H_KEQ",
                        "https://www.youtube.com/watch?v=fIHH5-HVS9o")

fourth = media.Movie("Dhoom 4 Salman Khan movies trailer",
                        "A标准YouTube许可",
                        "https://i.ytimg.com/vi/62qR2B18gCs/hqdefault.jpg?sqp=-oaymwEXCNACELwBSFryq4qpAwkIARUAAIhCGAE=&rs=AOn4CLBrVwsMYuV91DWI0ASQf4dwb1YTqw",
                        "https://www.youtube.com/watch?v=62qR2B18gCs")


fifth = media.Movie("Wonder (2017 Movie) Official Trailer – #ChooseKind – Julia Roberts, Owen Wilson",
                        "Wonder – In theaters November 17. Starring Julia Roberts, Owen Wilson, Jacob Tremblay, Mandy Patinkin, and Daveed Diggs. Based on the best-selling novel by RJ Palacio.",
                        "https://i.ytimg.com/vi/ngiK1gQKgK8/hqdefault.jpg?sqp=-oaymwEXCNACELwBSFryq4qpAwkIARUAAIhCGAE=&rs=AOn4CLCpr4Wbwjxt6dkxalXn9vKphfAZhQ",
                        "https://www.youtube.com/watch?v=ngiK1gQKgK8")


sixth = media.Movie("The Hitman’s Bodyguard (2017) Official F*cking Trailer – Ryan Reynolds, Samuel L. Jackson",
                        "The Hitman’s Bodyguard – In theaters August 18. Starring Ryan Reynolds, Samuel L. Jackson, Gary Oldman, and Salma Hayek, Elodie Yung, Joaquim De Almeida, Kirsty Mitchell, with Richard E. Grant.",
                        "https://i.ytimg.com/vi/IpKmt4MpctM/hqdefault.jpg?sqp=-oaymwEXCNACELwBSFryq4qpAwkIARUAAIhCGAE=&rs=AOn4CLDwp9fWP_QGETF9eutFfpBoUbRwdw",
                        "https://www.youtube.com/watch?v=IpKmt4MpctM")



#print(toy_story.storyline)

#toy_story.show_trailer()

movies = [first,second,third,fourth,fifth,sixth]
fresh_tomatoes.open_movies_page(movies)


