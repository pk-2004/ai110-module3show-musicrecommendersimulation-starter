from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file.
    Required by src/main.py
    """
    import csv

    songs = []
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            songs.append({
                "id":           int(row["id"]),
                "title":        row["title"],
                "artist":       row["artist"],
                "genre":        row["genre"],
                "mood":         row["mood"],
                "energy":       float(row["energy"]),
                "tempo_bpm":    int(row["tempo_bpm"]),
                "valence":      float(row["valence"]),
                "danceability": float(row["danceability"]),
                "acousticness": float(row["acousticness"]),
            })
    print(f"Loaded {len(songs)} songs from {csv_path}")
    return songs

def score_song(song: Dict, user_prefs: Dict) -> float:
    """
    Scores a single song against a user taste profile.
    Returns a float score (max 4.5 points).
    """
    score = 0.0

    # +2.0 for genre match
    if song["genre"] == user_prefs["genre"]:
        score += 2.0

    # +1.0 for mood match
    if song["mood"] == user_prefs["mood"]:
        score += 1.0

    # 0.0–1.0 based on energy proximity
    energy_diff = abs(song["energy"] - user_prefs["energy"])
    score += (1.0 - energy_diff)

    # 0.0–0.5 based on acousticness proximity
    acoustic_diff = abs(song["acousticness"] - user_prefs["acousticness"])
    score += (0.5 - (acoustic_diff * 0.5))

    return score

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """
    Functional implementation of the recommendation logic.
    Required by src/main.py
    """
    scored = []
    for song in songs:
        score = score_song(song, user_prefs)

        reasons = []
        if song["genre"] == user_prefs["genre"]:
            reasons.append(f"matches your favorite genre ({song['genre']})")
        if song["mood"] == user_prefs["mood"]:
            reasons.append(f"matches your preferred mood ({song['mood']})")
        if abs(song["energy"] - user_prefs["energy"]) <= 0.15:
            reasons.append(f"energy is close to your target ({song['energy']})")
        explanation = "Because it " + ", and ".join(reasons) if reasons else "Broadly similar to your taste"

        scored.append((song, score, explanation))

    return sorted(scored, key=lambda x: x[1], reverse=True)[:k]
