from website import create_app, db, models
from website.models import Location, Venue


def seed_data():
    app = create_app()

    with app.app_context():
        all_data = []

        # Create locations
        camberville = Location(name="Somerville/Cambridge")
        allbright = Location(name="Allston/Brighton")
        downtown = Location(name="Downtown")
        elsewhere = Location(name="Elsewhere")

        all_data.append(camberville)
        all_data.append(allbright)
        all_data.append(downtown)
        all_data.append(elsewhere)

        # Create venues

        # Add to the session and commit
        db.session.add_all(all_data)
        db.session.commit()


if __name__ == "__main__":
    seed_data()
