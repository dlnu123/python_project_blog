import asyncio
from aiohttp import web
import logging
logging.basicConfig(level=logging.INFO)


def index(request):
    return web.Response(body=b'<h1>Awesome</h1>', content_type="text/html")


async def init():
    # 创建 Application 对象，并指定处理的地址、函数
    app = web.Application()
    app.add_routes([web.get("/", index)])

    # 根据 Application 对象，创建 AppRunner 对象，并启动
    runner = web.AppRunner(app)
    await runner.setup()

    # 指定监听的地址和端口
    site = web.TCPSite(runner, "127.0.0.1", 9000)
    await site.start()
    logging.info("server started at http://127.0.0.1:9000...")

    # app = web.Application(loop=loop)
    # app.router.add_route("GET", "/", index)
    # server = await loop.create_server(app.make_handler(), "127.0.0.1", 9000)
    # logging.info("server started at http://127.0.0.1:9000...")
    # return server


loop = asyncio.get_event_loop()
loop.run_until_complete(init())
loop.run_forever()
