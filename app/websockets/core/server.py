from aiohttp import web
from app.websockets.core import views


app = web.Application()
app.router.add_get('/ws', views.WebSocketView)
