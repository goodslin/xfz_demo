from .base import BasePlugin


class NicPlugin(BasePlugin):

    def windows(self):
        output = self.shell_cmd('cccc')
        return output

    def linux(self):
        output = self.shell_cmd('dddd')
        return output
