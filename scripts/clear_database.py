from flask import Flask
from website import create_app, db


def clear_database():
    confirmation = input(
        "Are you sure you want to clear the database? (Type 'y' to confirm): "
    )
    if confirmation.lower() == "y":
        print("Database cleared!")
    else:
        print("Operation cancelled!")
    app = create_app()

    with app.app_context():
        db.drop_all()
        db.create_all()


if __name__ == "__main__":
    clear_database()
