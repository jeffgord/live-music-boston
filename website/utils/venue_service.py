import pandas as pd
import requests as rs
from io import StringIO
from ..models import Venue


def get_venues(location=None):
    request = rs.get(
        "https://docs.google.com/spreadsheets/d/e/2PACX-1vSsaDGmK4B0luksDiBe_qD3tcoOxpWNvETtIUcPMnBrW80_7Y8613rTSGXm61eRYV6TlD7ZgjItoIuu/pub?output=csv"
    )
    csv = StringIO(request.content.decode("utf-8"))
    df = pd.read_csv(csv)
    venues = []

    for index, row in df.iterrows():
        if location and row["LOCATION"] != location:
            continue

        venues.append(
            Venue(
                row["NAME"],
                row["LOCATION"],
                row["FREQUENCY"],
                row["GENRE"],
                row["LINK"],
            )
        )

    return venues
