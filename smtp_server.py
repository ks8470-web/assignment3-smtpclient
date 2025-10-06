#!/usr/bin/env python3
"""
Simple SMTP Server for Testing
Run this first, then run smtp_client.py in another terminal
"""
import asyncio
from aiosmtpd.controller import Controller


class MessageHandler:
    async def handle_DATA(self, server, session, envelope):
        print('\n' + '='*60)
        print('MESSAGE RECEIVED!')
        print('='*60)
        print(f'From: {envelope.mail_from}')
        print(f'To: {envelope.rcpt_tos}')
        print(f'Data length: {len(envelope.content)} bytes')
        print('-'*60)
        print('Message Content:')
        print(envelope.content.decode('utf8', errors='replace'))
        print('='*60 + '\n')
        return '250 Message accepted for delivery'


async def main():
    handler = MessageHandler()
    controller = Controller(handler, hostname='localhost', port=1025)
    controller.start()
    print('SMTP Server running on localhost:1025')
    print('Waiting for messages... (Press Ctrl+C to stop)\n')

    try:
        # Keep server running
        while True:
            await asyncio.sleep(1)
    except KeyboardInterrupt:
        print('\nShutting down server...')
        controller.stop()


if __name__ == '__main__':
    asyncio.run(main())
