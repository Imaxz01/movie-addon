from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# This tells your computer it is safe for Stremio to talk to this code
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# This is your add-on's identity card
MANIFEST = {
    "id": "com.personal.movieapp",
    "version": "1.0.0",
    "name": "My Custom Scraper",
    "description": "My personal movie add-on.",
    "resources": ["stream"],
    "types": ["movie"],
    "catalogs": [],
    "idPrefixes": ["tt"] 
}

@app.get("/manifest.json")
def get_manifest():
    return MANIFEST

# This is what runs when you click a movie in Stremio
@app.get("/stream/{type}/{id}.json")
def get_stream(type: str, id: str):
    # We will add your real movie website searcher here later. 
    # For now, it sends a safe, open-source test video to make sure the connection works.
    streams = []
    if type == "movie":
        streams.append({
            "title": "Test Video (Working!)",
            "url": "http://distribution.bbb3d.renderfarming.net/video/mp4/bbb_sunflower_1080p_30fps_normal.mp4"
        })
    return {"streams": streams}