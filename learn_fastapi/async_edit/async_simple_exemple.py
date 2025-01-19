from async_edit.synchronius_simple_exemple import url
import asyncio
import aiohttp
import time

async def make_reauest(session, req_n):
    print(f'making request {req_n}')
    async with session.get(url) as resp:
        if resp.status == 200:
            await resp.text()

async def main():
    request_count = 10
    async with aiohttp.ClientSession() as sesssion:
        await asyncio.gather(
            *[make_reauest(sesssion, i) for i in range(request_count)]
        )

loop = asyncio.get_event_loop()
start = time.time()
loop.run_until_complete(main())
end = time.time()
print('Time elapsed: ', end-start)


