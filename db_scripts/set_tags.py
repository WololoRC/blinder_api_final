"""
Script for poulate db with tags for
testing and development purposes.
"""

def db_tags():
    from tags.models import Tags
    tags = [
            "Alternative",
            "Gothic",
            "Punk",
            "Metalhead",
            "Hippie",
            "Bohemian",
            "Tattoos",
            "Piercings",
            "Rockabilly",
            "Indie",
            "Hipster",
            "Skater",
            "Retro",
            "Rocker",
            "Electronic",
            "Art",
            "Experimental",
            "Eco-friendly",
            "Veganism",
            "Vegetarian",
            "Activism",
            "LGBTQ+",
            "Geek Culture",
            "Freak",
            "Traveler",
            "Minimalist",
            "Vintage",
            "Handmade",
            "Gastronomy",
            "Filmmaker",
            "Reader",
            "Photography",
            "Artist",
            "Designer",
            "Festivalgoer",
            "Concerts",
            "Electronic Music",
            "Classic Rock",
            "Hip-hop",
            "Reggae",
            "Ska",
            "Folk",
            "Psychedelic",
            "Grunge",
            "Alternative Pop",
            "Alternative Fashion",
            "Underground",
            "Cyberpunk",
            "Alternative Architecture",
            "Nature Lover",
            "Adventurer",
            "Fitness Enthusiast",
            "Sustainable Living"
        ]


    for item in tags:
        Tags.objects.create(tag_name=item)
