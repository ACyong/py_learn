import asyncio
import logging
import signal
import socket

from asyncio import AbstractEventLoop
from typing import List


async def echo(connection: socket, loop: AbstractEventLoop) -> None:
    try:
        # 无限循环等待来自客户端连接的数据
        while data := await loop.sock_recv(connection, 1024):
            print(f"I got some data: {data}")
            if data == b"boom\r\n":
                raise Exception("Unexpected network error!")
            # 一旦得到数据, 将其发送回客户端
            await loop.sock_sendall(connection, data)
    except Exception as e:
        logging.exception(e)
    finally:
        # 关闭连接
        connection.close()


async def close_echo_tasks(echo_tasks: List[asyncio.Task]):
    waiters = [asyncio.wait_for(task, timeout=2) for task in echo_tasks]
    for task in waiters:
        try:
            await task
        except asyncio.exceptions.TimeoutError:
            # 处理超时任务
            pass


echo_tasks: List[asyncio.Task] = []


async def connection_listener(server_socket: socket, loop: AbstractEventLoop):
    while True:
        connection, address = await loop.sock_accept(server_socket)
        connection.setblocking(False)
        print(f"I got a connection from {address}!")

        # 每当获得连接时, 创建一个回显任务来监听客户端数据
        echo_task = asyncio.create_task(echo(connection, loop))
        echo_tasks.append(echo_task)


class GracefulExit(SystemExit):
    pass


def shutdown():
    raise GracefulExit()


async def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    server_address = ("127.0.0.1", 8000)
    server_socket.setblocking(False)
    server_socket.bind(server_address)
    server_socket.listen()

    for sig_name in {'SIGINT', 'SIGTERM'}:
        loop.add_signal_handler(getattr(signal, sig_name), shutdown)

    # 启动协程以监听连接
    await connection_listener(server_socket, loop)


loop = asyncio.new_event_loop()

try:
    loop.run_until_complete(main())
except GracefulExit:
    loop.run_until_complete(close_echo_tasks(echo_tasks))
finally:
    loop.close()
