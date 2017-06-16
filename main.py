from Tkinter import *
from yapsy.PluginManager import PluginManager


def main():
    # Load the plugins from the plugin directory.
    manager = PluginManager()
    manager.setPluginPlaces(["plugins"])
    manager.collectPlugins()

    # Loop round the plugins and print their names.
    for plugin in manager.getAllPlugins():
        plugin.plugin_object.print_name()

if __name__ == "__main__":
    main()


root=Tk()

theLabel = Label(root, text="RaspPi Monitor")
theLabel.pack()

theLabel2 = Label(root, text="Second Label")
theLabel2.pack(fill=X)

topFrame = Frame(root)
topFrame.pack()

bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

button1 = Button(topFrame,text="Button 1", fg="red")
button2 = Button(topFrame,text="Button 2", fg="blue")
button3 = Button(topFrame,text="Button 3", fg="pink")
button4 = Button(bottomFrame,text="Button 4", fg="green")

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=LEFT)

root.mainloop()