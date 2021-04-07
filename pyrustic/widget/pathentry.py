import tkinter as tk
from tkinter import filedialog
from pyrustic import widget
from pyrustic.tkmisc import get_cnf
from pyrustic.view import View


ENTRY = "entry"
BUTTON = "button"
DIALOG = "dialog"

class Pathentry(widget.Frame):
    """
    """
    def __init__(self,
                 master=None,
                 browse="file",
                 width=17,
                 title=None,
                 initialdir=None,
                 options=None,
                 extra_options=None):
        """
        - master: widget parent. Example: an instance of tk.Frame

        """
        super().__init__(master=master,
                         class_="Pathentry",
                         cnf=options if options else {},
                         on_build=self.__on_build,
                         on_display=self.__on_display,
                         on_destroy=self.__on_destroy)
        self.__browse = browse
        self.__width = width
        self.__title = title
        self.__initialdir = initialdir
        self.__entry = None
        self.__button = None
        self.__options = options
        self.__extra_options = extra_options
        self.__components = {}
        self.__string_var = tk.StringVar(value="")
        # build
        self.__view = self.build()
    # ==============================================
    #                   PROPERTIES
    # ==============================================
    @property
    def components(self):
        """
        """
        return self.__components

    @property
    def string_var(self):
        return self.__string_var

    @property
    def path(self):
        return self.__path

    @path.setter
    def path(self, val):
        self.__path = val

    def __on_build(self):
        self.__entry = tk.Entry(self, textvariable=self.__string_var,
                                width=self.__width,
                                cnf=get_cnf(ENTRY,
                                              self.__extra_options))
        self.__entry.pack(side=tk.LEFT, pady=0, fill=tk.X, expand=1)
        self.__components["entry"] = self.__entry
        self.__button = tk.Button(self, text="...",
                                  command=self.__on_click_button,
                                  cnf=get_cnf(BUTTON,
                                              self.__extra_options))
        self.__button.pack(side=tk.LEFT, padx=(2, 0), fill=tk.Y)
        self.__components["button"] = self.__button

    def __on_display(self):
        pass

    def __on_destroy(self):
        pass

    def __on_click_button(self):
        if self.__browse == "file":
            try:
                filename = filedialog.askopenfilename(initialdir=self.__initialdir,
                                                      title=self.__title,
                                                      **get_cnf(DIALOG,
                                                                self.__extra_options))
            except Exception as e:
                return
            path = None
            if not filename:
                pass
            elif isinstance(filename, str):
                path = filename
            else:
                path = ";".join(filename)
            if path:
                self.__string_var.set(path)
        else:
            try:
                filename = filedialog.askdirectory(initialdir=self.__initialdir,
                                                   title=self.__title,
                                                   **get_cnf(DIALOG,
                                                             self.__extra_options))
            except Exception as e:
                return
            path = None
            if not filename:
                pass
            elif isinstance(filename, str):
                path = filename
            else:
                path = ";".join(filename)
            if path:
                self.__string_var.set(path)
        self.__entry.icursor("end")


if __name__ == "__main__":
    root = tk.Tk()
    pathentry_test = Pathentry(root, browse="dir",
                               extra_options={"dialog":
                                                  {"initialdir": "/home/alex",
                                                   "title": "Hello"}})
    pathentry_test.pack(fill=tk.BOTH, expand=1)
    root.mainloop()