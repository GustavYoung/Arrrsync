#!/bin/env python3
import os
import sys

from command_parser.parser import parser
from command_parser.client_parser import client_parser
from client.ssh import connectSSH


def clientConsole(client):
    stdin, stdout, stderr = client.exec_command('cd .')
    current_path = stdout.readline().rstrip('\n')
    running = True
    while running:
        # Catching user input
        # CTRL-C jumps to a blank input
        # CTLR-D exits the program
        try:
            command = input('>>: ')
        except KeyboardInterrupt:
            print('')
            continue
        except EOFError:
            print('Shutting down.')
            client.close()
            sys.exit(1)

        # Parsing input, getting actual command name and arguments
        program, args = parser(command)
        if program == 'ls':
            # Compile options for ls
            ls_args = ['ls']
            if args['a']:
                ls_args.append('-a')
            if args['l']:
                ls_args.append('-l')

            # Get absolute path from current position to target
            targetPath = os.path.join(current_path, args['path'])
            ls_args.append(targetPath)

            # Send command to server
            stdin, stdout, stderr = client.exec_command(' '.join(ls_args))

            # Print response
            for line in stdout.readlines():
                print(line.rstrip('\n'))

        elif program == 'cd':
            cd_args = ['cd']
            # Get absolute path from current position to target
            targetPath = os.path.join(current_path, args['path'])

            cd_args.append(targetPath)
            stdin, stdout, stderr = client.exec_command(' '.join(cd_args))

            errors = stderr.readline().rstrip('\n')
            if not len(errors) > 1:
                # Save current position
                current_path = stdout.readline().rstrip('\n')
            else:
                # Print response
                print(errors)

        elif program == 'exit':
            running = False

    client.close()
    sys.exit(0)


def main():
    args = vars(client_parser.parse_args())

    client = connectSSH(args)

    try:
        clientConsole(client)
    except KeyboardInterrupt:
        print('Keyboard interrupt. Shutting down')
        client.close()
        sys.exit(1)
