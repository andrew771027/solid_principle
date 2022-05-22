from src.solid.dip.correspond.lib.ilogger import ILogger


class Logger(ILogger):

    def Log(self, message: str):
        print(f'Write to console: {message}')
