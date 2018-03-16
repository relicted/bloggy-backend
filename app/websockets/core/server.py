# from aiohttp import web
# from app.websockets.core import views
#
#
# app = web.Application()
# app.router.add_get('/ws', views.WebSocketView)


import asyncio

from aiohttp import web

from app.websockets.core import settings
from app.websockets.core.routes import routes

async def create_app(loop):
    """ Prepare application """
    # init application
    app = web.Application(loop=loop)

    app.wslist = {}

    for route in routes:
        app.router.add_route(**route)



    handler = app.make_handler()
    serv_generator = loop.create_server(handler, settings.HOST, settings.PORT)
    return serv_generator, handler, app


async def shutdown(server, app, handler):
    """ Safe close server """
    for room in app.wslist.values():
        for peer in room.values():
            peer.send_json({'text': 'Server shutdown'})
    server.close()
    await server.wait_closed()

    await app.cleanup()


if __name__ == '__main__':

    loop = asyncio.get_event_loop()
    serv_generator, handler, app = loop.run_until_complete(create_app(loop))
    server = loop.run_until_complete(serv_generator)

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    finally:

        loop.run_until_complete(shutdown(server, app, handler))
        loop.close()
