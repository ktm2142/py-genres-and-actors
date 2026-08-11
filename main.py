import init_django_orm  # noqa: F401
from django.db.models import QuerySet
from db.models import Genre, Actor


def main() -> QuerySet:
    genres_names = [
        "Western",
        "Action",
        "Dramma"
    ]
    for name in genres_names:
        Genre.objects.create(name=name)

    actor_names = [
        {"first_name": "George", "last_name": "Klooney"},
        {"first_name": "Kianu", "last_name": "Reaves"},
        {"first_name": "Scarlett", "last_name": "Keegan"},
        {"first_name": "Will", "last_name": "Smith"},
        {"first_name": "Jaden", "last_name": "Smith"},
        {"first_name": "Scarlett", "last_name": "Johansson"}
    ]
    for actor in actor_names:
        Actor.objects.create(
            first_name=actor["first_name"],
            last_name=actor["last_name"]
        )

    Genre.objects.filter(name="Dramma").update(name="Drama")
    Actor.objects.filter(first_name="George").update(last_name="Clooney")
    Actor.objects.filter(first_name="Kianu").update(
        first_name="Keanu",
        last_name="Reeves"
    )
    Genre.objects.get(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    return Actor.objects.filter(last_name="Smith").order_by("first_name")
