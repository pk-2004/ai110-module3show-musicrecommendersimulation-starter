"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from src.recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv")

    high_energy_pop = {
        "genre":        "pop",
        "mood":         "happy",
        "energy":       0.88,
        "acousticness": 0.10,
    }

    chill_lofi = {
        "genre":        "lofi",
        "mood":         "chill",
        "energy":       0.40,
        "acousticness": 0.75,
    }

    deep_intense_rock = {
        "genre":        "rock",
        "mood":         "intense",
        "energy":       0.91,
        "acousticness": 0.08,
    }

    users = {
        "High-Energy Pop":   high_energy_pop,
        "Chill Lofi":        chill_lofi,
        "Deep Intense Rock": deep_intense_rock,
    }

    for profile_name, user_prefs in users.items():
        print(f"\n=== {profile_name} ===")
        recommendations = recommend_songs(user_prefs, songs, k=5)
        for song, score, explanation in recommendations:
            print(f"{song['title']} - Score: {score:.2f}")
            print(f"Because: {explanation}")
            print()


if __name__ == "__main__":
    main()
