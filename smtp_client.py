#!/usr/bin/env python3
"""
SMTP Client - Educational/Testing Purposes Only
Demonstrates raw SMTP protocol implementation
"""
from socket import *

# Configuration
mailserver = 'localhost'
port = 1025  # Use 1025 for testing (aiosmtpd default)

# Email content
sender = 'alice@example.com'
recipient = 'bob@example.com'
subject = 'Test Email from Raw SMTP Client'
body = 'Hello! This is a test message sent using raw SMTP commands.\n\nBest regards,\nAlice'

# Construct message with headers
msg = f"Subject: {subject}\r\n"
msg += f"From: {sender}\r\n"
msg += f"To: {recipient}\r\n"
msg += "\r\n"  # Blank line separates headers from body
msg += body

endmsg = "\r\n.\r\n"  # SMTP end-of-message indicator

print('='*60)
print('SMTP Client Starting...')
print('='*60)

try:
    # Section 1: Create Socket Connection
    print(f'\n[1] Connecting to {mailserver}:{port}...')
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((mailserver, port))
    recv = clientSocket.recv(1024).decode()
    print(f'    Server: {recv.strip()}')

    # Section 2: HELO Command (introduce ourselves)
    print('\n[2] Sending HELO...')
    heloCommand = 'HELO client\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    print(f'    Server: {recv1.strip()}')

    # Section 3: MAIL FROM Command
    print(f'\n[3] Sending MAIL FROM: <{sender}>...')
    mailFromCommand = f'MAIL FROM: <{sender}>\r\n'
    clientSocket.send(mailFromCommand.encode())
    recv2 = clientSocket.recv(1024).decode()
    print(f'    Server: {recv2.strip()}')

    # Section 4: RCPT TO Command
    print(f'\n[4] Sending RCPT TO: <{recipient}>...')
    rcptToCommand = f'RCPT TO: <{recipient}>\r\n'
    clientSocket.send(rcptToCommand.encode())
    recv3 = clientSocket.recv(1024).decode()
    print(f'    Server: {recv3.strip()}')

    # Section 5: DATA Command
    print('\n[5] Sending DATA command...')
    dataCommand = 'DATA\r\n'
    clientSocket.send(dataCommand.encode())
    recv4 = clientSocket.recv(1024).decode()
    print(f'    Server: {recv4.strip()}')

    # Section 6: Send Message
    print('\n[6] Sending message content...')
    clientSocket.send(msg.encode())
    print(f'    Message length: {len(msg)} bytes')

    # Section 7: End Message
    print('\n[7] Sending end-of-message indicator...')
    clientSocket.send(endmsg.encode())
    recv5 = clientSocket.recv(1024).decode()
    print(f'    Server: {recv5.strip()}')

    # Section 8: QUIT Command
    print('\n[8] Sending QUIT...')
    quitCommand = 'QUIT\r\n'
    clientSocket.send(quitCommand.encode())
    recv6 = clientSocket.recv(1024).decode()
    print(f'    Server: {recv6.strip()}')
    clientSocket.close()

    print('\n' + '='*60)
    print('[SUCCESS] Email sent successfully!')
    print('='*60)

except ConnectionRefusedError:
    print('\n[ERROR] Could not connect to SMTP server')
    print(f'   Make sure smtp_server.py is running on {mailserver}:{port}')
except Exception as e:
    print(f'\n[ERROR] {e}')
finally:
    try:
        clientSocket.close()
    except:
        pass
