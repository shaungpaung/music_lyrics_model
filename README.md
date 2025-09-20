music_lyrics_model

A music lyrics recommendation API using FastAPI, TF-IDF, and Qdrant for vector search.

Features:
- Recommend songs based on input lyrics
- Stores song vectors in Qdrant (cloud or local)
- FastAPI REST API with Swagger UI

How to Run (Local with Docker):

1. Build Docker image:
   docker build -t music-api .

2. Run Docker container:
   docker run -d -p 8000:8000 music-api

3. Access API docs:
   http://localhost:8000/docs
   Endpoint: /recommend (POST)

Example request:
{
  "lyric": "your song lyrics here"
}

Example response:
{
  {
    "recommendations": [
        {
        "artist": "nancy sinatra",
        "track": "so long, babe",
        "genre": "pop",
        "release_date": 1966,
        "score": 0.87605774,
        "ly": "know leavin babe goodbye long someday somebody listen song bright light spell true maybe change scene best long babe long babe long babe long babe long babe know leavin babe goodbye long pick piece belong give give nothin babe nothin long babe long babe long babe long babe long babe long babe long babe know leavin babe goodbye long babe wonder go wrong understand songs walk away leave come long babe long babe yeah long babe long babe long babe long babe long babe long babe long babe long babe long babe"
        },
        {
        "artist": "nancy sinatra",
        "track": "it ain't me babe",
        "genre": "pop",
        "release_date": 1966,
        "score": 0.82365507,
        "ly": "window leave choose speed want babe need lookin weak strong protect defend right wrong open door babe babe lookin babe lightly ledge babe lightly grind want babe lookin promise close eye close heart babe babe lookin babe"
        },
        {
        "artist": "belinda carlisle",
        "track": "world without you",
        "genre": "pop",
        "release_date": 1987,
        "score": 0.8117496,
        "ly": "learn live rain darling trade pleasure pain live food money wouldn hard star fell baby world babe babe couldn breathe babe couldn breathe babe world babe babe couldn breathe babe couldn breathe babe wouldn music reason laugh reason smile couldn live live worthwhile know worthless weren world hand wouldn thing cause world babe babe couldn breathe babe couldn breathe babe world babe babe couldn breathe couldn breathe world baby worthless weren world hand wouldn thing world babe babe couldn breathe babe couldn breathe babe world babe babe couldn breathe babe couldn breathe babe world babe babe couldn breathe babe couldn breathe babe world babe"
        },
        {
        "artist": "fat joe",
        "track": "what's luv? (feat. ja-rule & ashanti)",
        "genre": "pop",
        "release_date": 2001,
        "score": 0.76459366,
        "ly": "fuckin crack gotti ashanti terror terror squad trust babe trust babe babe trust babe yeah yeah slow baby know gate lady wanna chick hips lick lips office type like strip girl arouse look talk ruinin high wanna lose feelin cause roof chillin lookin good gettin rider hoodie linen provider jewelry women livin squad stay fillin truck chicks willin triz gotta gotta little menage partay slide come babe trust babe babe trust babe yeah yeah mami know issue gotta need understand somethin frame little tattoo chest middle hater crush shake booty want stop need come little closer come little closer arm like suppose believe leave freakin night like need trust jump little hard mahal babe trust babe babe trust babe yeah stroll club style steppin fault cause chain whip know party bullshit mami body motion nigga open come heart cheat need sing song ladies come look eye stoppin want crack uhhuh want stack break yeah gonna slack cause like come yeah yeah yeah yeah girl girl babe trust babe babe trust babe babe trust babe babe trust babe"
        },
        {
        "artist": "roxy music",
        "track": "over you",
        "genre": "pop",
        "release_date": 1980,
        "score": 0.59931266,
        "ly": "baby wish sweet lips tell romance baby cry long strangers look lose come babe babe moment"
        }
    ]
    }
}

Using Qdrant Cloud:

1. Upload song vectors using upload_vectors.py.
2. Connect FastAPI to Qdrant Cloud:
   from qdrant_client import QdrantClient
   client = QdrantClient(
       url="YOUR_QDRANT_CLOUD_URL",
       api_key="YOUR_QDRANT_API_KEY"
   )
3. Run FastAPI:
   uvicorn app:app --reload

Dependencies:

- Python 3.11+
- FastAPI
- qdrant-client
- scikit-learn
- pandas
- pydantic
- uvicorn

Install from requirements.txt:
   pip install -r requirements.txt

Notes:

- Ensure vectorizer.pkl and your dataset are available for vectorization.
- For Docker, the container must expose port 8000.
- If using Qdrant Cloud, upload all vectors before testing the /recommend endpoint.
