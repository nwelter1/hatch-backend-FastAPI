from fastapi import FastAPI
from calls import Call
import requests
from typing import Optional

app = FastAPI()

@app.get('/api/ping')
async def ping():
    ping = requests.get('https://api.hatchways.io/assessment/blog/posts?tag=tech').status_code
    print(ping)
    if ping == 200:
        return {'success': True}
    return {'failure': False}, 500


@app.get('/api/posts')
async def posts(tags: str, sortBy: Optional[str] = None, direction: Optional[str] = None):
    if not tags:
        return {'error':'Tags parameter is required'}, 400
    call = Call(tags, sortBy, direction)
    if not call.checkSortField():
        return {'error':'sortBy parameter is invalid'}, 400
    if not call.checkSortDirection():
        return {'error':'Sorting direction parameter is invalid'}, 400
    return call.getAllPosts()
