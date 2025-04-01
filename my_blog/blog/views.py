from django.shortcuts import render
from datetime import date

all_posts = [
    {
        "slug": "sking-in-snow",  # Corrected spelling mistake in slug
        "image": "self.JPG",
        "author": "SaiKumar",
        "date": date(2025, 4, 1),
        "title": "Misawa, Japan",
        "excert": "Enjoy breathtaking views after an adventurous ski run in Misawa's snowy landscape.",
        "content": """
            Skiing in the snow-covered landscapes of Misawa is an exhilarating experience. 
            The crisp mountain air, the stunning white slopes, and the thrill of skiing down 
            perfectly groomed trails make it a must-visit destination for winter sports lovers. 
            Whether you're a beginner or an experienced skier, Misawa offers slopes for all skill levels. 
        """
    },
    {
        "slug": "hiking-in-misawa",
        "image": "sking.jpg",
        "author": "SaiKumar",
        "date": date(2025, 3, 28),
        "title": "Hiking in Misawa",
        "excert": "A thrilling hike through forests and valleys, leading to breathtaking panoramic views.",
        "content": """
            Hiking in Misawa is an adventure like no other. The trails lead through dense forests, 
            picturesque valleys, and up to stunning peaks with panoramic views. The journey is rewarding, 
            with fresh mountain air, the sound of rustling leaves, and the occasional sighting of local wildlife. 
            Whether hiking in the spring or autumn, Misawa’s trails offer an unforgettable experience. 
        """
    },
    {
        "slug": "japan-cherry-blossom",
        "image": "self.JPG",
        "author": "SaiKumar",
        "date": date(2025, 3, 20),
        "title": "Cherry Blossom in Japan",
        "excert":  "Immerse yourself in Japan’s mesmerizing sakura season, a true spectacle of nature.",
        "content": """
            Springtime in Japan is synonymous with cherry blossoms, or 'sakura'. 
            The delicate pink and white petals create breathtaking landscapes, drawing visitors from around the world. 
            Hanami, the tradition of flower viewing, is a time of joy and celebration, where families and friends 
            gather under the blooming trees for picnics. Cities like Tokyo, Kyoto, and Osaka offer some of the 
            most picturesque cherry blossom spots. 
        """
    }
]

def get_date(post):
    return post['date']

def starting_page(request):
    sorted_post = sorted(all_posts, key = get_date)
    latest_post = sorted_post[-2:]
    return render(request, "blog/index.html", {
        "posts": latest_post
    })


def posts(request):
    return render(request, "blog/all-posts.html", {
        "all_posts": all_posts
    })


def blog_post_complete_detail(request, slug):
    identified_post = next(post for post in all_posts if post["slug"] == slug)
    return render(request, "blog/post-detail.html", {
        "post": identified_post
    })