import os
import sys 
import argparse
from flask.cli import FlaskGroup
from app import create_app, settings

application = create_app()
cli = FlaskGroup(application)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog=f"{sys.argv[0].split(os.sep)[-1]}", description=f"{settings.PROJECT_NAME} {settings.VERSION}", add_help=False)
    parser.version = settings.VERSION
    parser.add_argument('-v', '--version', action='version', version=settings.VERSION)
    parser.add_argument(
        dest='command',
        nargs='*',
        type=str,
        default=None,
        help='command, default:None'
    )
    parser.add_argument(
        '-h',
        '--host',
        dest='host',
        default='0.0.0.0',
        required=False,
        help='host, default: 0.0.0.0'
    )

    parser.add_argument(
        '-p',
        '--port',
        dest='port',
        default=5000,
        required=False,
        help='port, default: 5000'
    )

    args = parser.parse_args(sys.argv[1:])

    if args.command==['runserver']:
        application.run(host=args.host, port=args.port)
    else:
        application.app_context().push()
        cli(args.command)
