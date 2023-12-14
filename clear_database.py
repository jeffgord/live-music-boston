from flask import Flask
from website import create_app, db


def clear_database():
    app = create_app()

    with app.app_context():
        db.drop_all()
        db.create_all()


if __name__ == "__main__":
    confirmation = input(
        "Are you sure you want to clear the database? (Type 'y' to confirm): "
    )
    if confirmation.lower() == "y":
        clear_database()
        print("Database cleared!")
    else:
        print("Operation cancelled!")
