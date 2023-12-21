from scripts import clear_database as cd, create_admin_user as cau, seed


def main():
    cd.clear_database()
    cau.create_admin_user()
    seed.seed_data()


if __name__ == "__main__":
    main()
