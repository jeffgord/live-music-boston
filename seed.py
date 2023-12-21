from website import create_app, db
from website.models import Location, Venue


def seed_data():
    app = create_app()

    with app.app_context():
        # Create locations
        allbright = Location(name="Allston/Brighton", ordinal=1)
        camberville = Location(name="Somerville/Cambridge", ordinal=2)
        downtown = Location(name="Downtown", ordinal=3)
        elsewhere = Location(name="Elsewhere", ordinal=4)

        db.session.add_all([camberville, allbright, downtown, elsewhere])
        db.session.commit()

        all_venues = []

        # Create venues
        obriens = Venue(
            name="Obrien's Pub",
            link="https://obrienspubboston.com/",
            location_id=allbright.id,
            frequency="Music every night",
            genre="Local acts",
        )
        bmh = Venue(
            name="Brighton Music Hall",
            link="https://crossroadspresents.com/pages/brighton-music-hall",
            location_id=allbright.id,
            frequency="Music most nights",
            genre="Touring indie acts",
        )
        notch = Venue(
            name="Notch Brewing",
            link="https://www.notchbrewing.com/notchbrighton#brightonevents",
            location_id=allbright.id,
            frequency="Music most Thursdays",
            genre="Local acts",
        )
        armory = Venue(
            name="Arts at the Armory",
            link="https://artsatthearmory.org/events/music/",
            location_id=camberville.id,
            frequency="Music some nights",
            genre="Local variety",
        )
        jungle = Venue(
            name="The Jungle",
            link="https://www.thejunglemusicclub.com/events-calendar",
            location_id=camberville.id,
            frequency="Music every night",
            genre="Local variety",
        )
        burren = Venue(
            name="The Burren",
            link="https://www.burren.com/music.html",
            location_id=camberville.id,
            frequency="Music every night",
            genre="Local folk/rock",
        )
        passim = Venue(
            name="Club Passim",
            link="https://www.passim.org/live-music/",
            location_id=camberville.id,
            frequency="Music every night",
            genre="Local folk",
        )
        lilypad = Venue(
            name="Lilypad",
            link="https://www.lilypadinman.com/calendar",
            location_id=camberville.id,
            frequency="Music every night",
            genre="Jazz/variety",
        )
        cantab = Venue(
            name="The Cantab Lounge",
            link="https://www.thecantablounge.com/",
            location_id=camberville.id,
            frequency="Music every night",
            genre="Local bands",
        )
        middle_east = Venue(
            name="The Middle East",
            link="https://www.mideastoffers.com/all-shows/",
            location_id=camberville.id,
            frequency="Music most nights",
            genre="Local bands & dance",
        )
        rockwell = Venue(
            name="The Rockwell",
            link="https://do617.com/venues/the-rockwell-davis-square-theatre",
            location_id=camberville.id,
            frequency="Music occasionally",
            genre="Local and small touring acts",
        )
        sinclair = Venue(
            name="The Sinclair",
            link="https://do617.com/venues/the-rockwell-davis-square-theatre",
            location_id=camberville.id,
            frequency="Music most nights",
            genre="Touring indie acts",
        )
        crystal_ballrom = Venue(
            name="Crystal Ballroom",
            link="https://www.crystalballroomboston.com/events/",
            location_id=camberville.id,
            frequency="Music occassionaly",
            genre="Touring indie acts",
        )
        state_park = Venue(
            name="State Park Bar",
            link="https://www.statepark.is/music-stuff/live-music",
            location_id=camberville.id,
            frequency="Music on sundays",
            genre="Local acts",
        )
        union_tavern = Venue(
            name="Union Tavern",
            link="https://www.instagram.com/uniontavernsomerville/",
            location_id=camberville.id,
            frequency="Music occasionally",
            genre="Local acts",
        )
        aeronaut_somerville = Venue(
            name="Aeronaut Brewery",
            link="https://www.aeronautbrewing.com/visit/somerville/#events",
            location_id=camberville.id,
            frequency="Music Thursdays, Saturdays, and Sundays",
            genre="Local acts",
        )
        lizard_lounge = Venue(
            name="Lizard Lounge",
            link="https://lizardloungeclub.com/calendar/",
            location_id=camberville.id,
            frequency="Music most nights",
            genre="Local rock/folk",
        )
        plough_and_stars = Venue(
            name="The Plough & Stars",
            link="https://calendar.ploughandstars.com/events/calendar",
            location_id=camberville.id,
            frequency="Music most nights",
            genre="Local blues/rock",
        )
        sally_obriens = Venue(
            name="Sally O'brien's",
            link="https://www.sallyobriensbar.com/music/",
            location_id=camberville.id,
            frequency="Music most nights",
            genre="Local blues/rock",
        )
        red_room = Venue(
            name="The Red Room at Cafe939",
            link="https://www.berklee.edu/red-room-cafe-939/calendar",
            location_id=downtown.id,
            frequency="Music some nights",
            genre="Berklee bands & Small indie acts",
        )
        roadrunneer = Venue(
            name="Roadrunner",
            link="https://roadrunnerboston.com/calendar/",
            location_id=downtown.id,
            frequency="Music some nights",
            genre="Touring indie acts",
        )
        house_of_blues = Venue(
            name="House of Blues Boston",
            link="https://www.houseofblues.com/boston/concert-events",
            location_id=downtown.id,
            frequency="Music some nights",
            genre="Touring acts",
        )
        paradise_rock_club = Venue(
            name="Paradis Rock Club",
            link="https://crossroadspresents.com/pages/paradise-rock-club",
            location_id=downtown.id,
            frequency="Music some nights",
            genre="Touring indie acts",
        )
        royale = Venue(
            name="Royale",
            link="https://royaleboston.com/events/month/",
            location_id=downtown.id,
            frequency="Music some nights",
            genre="Touring acts",
        )
        bpc = Venue(
            name="Berklee Performance Center",
            link="https://www.berklee.edu/BPC",
            location_id=downtown.id,
            frequency="Music occasionally",
            genre="Berklee bands & Variety",
        )
        bills_bar = Venue(
            name="Bill's Bar",
            link="https://www.billsbarboston.com/event/breaking-sound/",
            location_id=downtown.id,
            frequency="Music Tuesdays",
            genre="Local bands",
        )
        all_venues.append(obriens)
        all_venues.append(bmh)
        all_venues.append(notch)
        all_venues.append(armory)
        all_venues.append(jungle)
        all_venues.append(burren)
        all_venues.append(passim)
        all_venues.append(lilypad)
        all_venues.append(cantab)
        all_venues.append(middle_east)
        all_venues.append(rockwell)
        all_venues.append(sinclair)
        all_venues.append(crystal_ballrom)
        all_venues.append(state_park)
        all_venues.append(aeronaut_somerville)
        all_venues.append(union_tavern)
        all_venues.append(lizard_lounge)
        all_venues.append(plough_and_stars)
        all_venues.append(sally_obriens)
        all_venues.append(red_room)
        all_venues.append(roadrunneer)
        all_venues.append(house_of_blues)
        all_venues.append(paradise_rock_club)
        all_venues.append(royale)
        all_venues.append(bpc)
        all_venues.append(bills_bar)

        # Add to the session and commit
        db.session.add_all(all_venues)
        db.session.commit()


if __name__ == "__main__":
    seed_data()
