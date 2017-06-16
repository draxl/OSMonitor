from yapsy.IPlugin import IPlugin

class PluginListing(IPlugin):
    def print_name(self):
        print "This is plugin for showing a list of connected RaspBerry PI"