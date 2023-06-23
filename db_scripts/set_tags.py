"""
Script for poulate db with tags for
testing and development purposes.
"""

def tags():
    from tags.models import Tags
    tags = [
            "Alternative",
            "Punk",
            "Metalhead",
            "Bohemian",
            "Tattoos",
            "Piercings",
            "Indie",
            "Hipster",
            "Skater",
            "Retro",
            "Rocker",
            "Electronic",
            "Art",
            "Eco-friendly",
            "Veganism",
            "Activism",
            "LGBTQ+",
            "Geek Culture",
            "Freak",
            "Traveler",
            "Gastronomy",
            "Reader",
            "Photography",
            "Artist",
            "Festivalgoer",
            "Concerts",
            "Electronic Music",
            "Hip-hop",
            "Alternative Fashion",
            "Underground",
            "Nature Lover",
            "Adventurer",
            "Fitness Enthusiast",
            'Adventurous',
            'Animal Lover',
            'Artist',
            'Athlete',
            'Beach Lover',
            'Dancer',
            'Spiritual',
            'Photography Lover',
            'Intellectual',
            'Football Fan',
            'Fashion Lover',
            'Theater Lover',
            'Wine Enthusiast',
            'Car Lover',
            'Empathetic',
            'Writer',
            'Basketball Fan',
            'Free Spirit',
            'Aspiring Musician',
            'Human Rights Advocate',
            'Technology Enthusiast'
    ]

    clean_list = list(set(tags))

    for item in clean_list:
        Tags.objects.create(tag_name=item)
