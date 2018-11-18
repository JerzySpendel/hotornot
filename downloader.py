import asyncio
import pathlib
import typing

import cv2 as cv
import numpy as np
import aiohttp
import tqdm
from aiostream import stream, pipe


async def download_and_save(url: str, path):
    async with aiohttp.ClientSession() as session:
        try:
            response: aiohttp.ClientResponse = await session.get(url)
        except aiohttp.client_exceptions.ClientError:
            return

        if response.status != 200:
            response.close()
            return

        binary = await response.read()
        response.close()
        np_image = cv.imdecode(np.array(bytearray(binary)), cv.IMREAD_COLOR)
        return cv.imwrite(str(path), np_image)


async def download_all(file_name: str):
    dir: pathlib.Path = pathlib.Path(__file__).parent / 'dogs'
    dir.mkdir()

    urls = [url.strip() for url in open(file_name, 'r').readlines()]
    tasks = [asyncio.ensure_future(download_and_save(url, dir / f'{index}.png')) for index, url in enumerate(urls)]

    # for f in tqdm.tqdm(asyncio.as_completed(tasks), total=len(tasks)):
    #     await f

    done, pending = await asyncio.wait(tasks)


loop = asyncio.get_event_loop()
loop.run_until_complete(download_all('dogs.urls'))