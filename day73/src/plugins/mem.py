from .base import BasePlugin


class MemPlugin(BasePlugin):

    def windows(self):
        output = self.shell_cmd('aaaa')
        return output

    def linux(self):
        output = self.shell_cmd('bbbb')
        return output