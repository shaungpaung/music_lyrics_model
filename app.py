from fastapi import FastAPI
from pydantic import BaseModel
from qdrant_client import QdrantClient
import pickle

# Load trained TF-IDF vectorizer
with open("vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

# Connect to Qdrant Cloud
client = QdrantClient(
    url="https://c4603001-de6c-43f7-8500-fb653c005461.us-east-1-1.aws.cloud.qdrant.io",
    api_key="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3MiOiJtIn0.te976z5fjuyFmMv-zHQpLz-BHrI8Uo9g5DGkKkvQo6U"
)

collection_name = "songs"

# Optional: check if collection exists
if not client.collection_exists(collection_name):
    print(f"Collection '{collection_name}' does not exist. Please upload vectors first.")

app = FastAPI(title="Music Recommendation API")

class LyricQuery(BaseModel):
    lyric: str

@app.post("/recommend")
def recommend_song(query: LyricQuery):
    # Transform lyric into vector
    query_vector = vectorizer.transform([query.lyric]).toarray()[0].tolist()

    # Search Qdrant Cloud
    results = client.search(
        collection_name=collection_name,
        query_vector=query_vector,
        limit=5
    )

    return {
        "recommendations": [
            {
                "artist": r.payload["artist"],
                "track": r.payload["track"],
                "genre": r.payload.get("genre"),
                "release_date": r.payload.get("release_date"),
                "score": r.score,
                "ly": r.payload['lyrics']
            }
            for r in results
        ]
    }