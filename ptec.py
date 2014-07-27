from PythonCard.components import button, textfield, statictext, gauge, checkbox, combobox
from wx import ICON_QUESTION, ICON_INFORMATION, ICON_ERROR
from PythonCard import model, dialog, timer
import wx, os, urllib, sys, pickle, time, shutil, webbrowser, subprocess
# To make it easier for me:
if sys.platform=="win32":
    rsrc={'application':{'type':'Application',
          'name':'Template',
    'backgrounds': [
    {'type':'Background',
          'name':'PTEC 2.0',
          'title':u'PTEC 2.0',
          'size':(600, 425),
          'statusBar':1,
          'icon':'iconv2.ico',

        'menubar': {'type':'MenuBar',
         'menus': [
             {'type':'Menu',
             'name':'menuFile',
             'label':'&File',
             'items': [
                  {'type':'MenuItem',
                   'name':'menuFileNew',
                   'label':u'&New\tCtrl+N',
                   'command':'new',
                  },
                  {'type':'MenuItem',
                   'name':'menuFileOpen',
                   'label':u'&Open...\tCtrl+O',
                   'command':'open',
                  },
                  {'type':'MenuItem',
                   'name':'menuFileSave',
                   'label':u'&Save\tCtrl+S',
                   'command':'save',
                  },
                  {'type':'MenuItem',
                   'name':'menuFileSaveas',
                   'label':u'Save &as...\tCtrl+Shift+S',
                   'command':'saveas',
                  },
                  {'type':'MenuItem',
                   'name':'Dash3',
                   'label':u'-',
                  },
                  {'type':'MenuItem',
                   'name':'menuFileExit',
                   'label':u'E&xit\tAlt+F4',
                   'command':'exit',
                  },
              ]
             },
             {'type':'Menu',
             'name':'menuConvert',
             'label':u'&Convert',
             'items': [
                  {'type':'MenuItem',
                   'name':'menuConvertConvert',
                   'label':u'&Convert!\tCtrl+T',
                   'command':'cmdconvert',
                  },
              ]
             },
             {'type':'Menu',
             'name':'menuHelpandUpdates',
             'label':u'&Help and Updates',
             'items': [
                  {'type':'MenuItem',
                   'name':'menuHelpandUpdatesHelp',
                   'label':u'&Help\tCtrl+H',
                   'command':'cmdh',
                  },
                  {'type':'MenuItem',
                   'name':'menuHelpandUpdatesinfo',
                   'label':u'&Version Info\tCtrl+E',
                   'command':'info',
                  },
                  {'type':'MenuItem',
                   'name':'menuHelpandUpdatesLicense',
                   'label':u'&License\tCtrl+L',
                   'command':'license',
                  },
                  {'type':'MenuItem',
                   'name':'Dash2',
                   'label':u'-',
                  },
                  {'type':'MenuItem',
                   'name':'menuHelpandUpdatesCheckforupadates',
                   'label':u'Check for &Updates\tCtrl+U',
                   'command':'cfu',
                  },
              ]
             },
         ]
     },
         'components': [

{'type':'TextField',
    'name':'pybox',
    'position':(181, 8),
    'size':(323, -1),
    },

{'type':'Button',
    'name':'pyexebrowse',
    'position':(510, 35),
    'command':u'pyexebrowse',
    'label':u'Browse...',
    },

{'type':'TextField',
    'name':'pyexedrop',
    'position':(168, 35),
    'size':(335, -1),
    'command':u'pyexebrowse',
    'text':u'C:\Python27\python.exe',
    },

{'type':'Button',
    'name':'exebrowse',
    'position':(510, 62),
    'command':u'cmdexe',
    'label':u'Browse...',
    },

{'type':'TextField',
    'name':'exebox',
    'position':(256, 62),
    'size':(248, -1),
    },

{'type':'StaticText',
    'name':'exestatic',
    'position':(10, 65),
    'text':u'Location you want to save the converted program:',
    },

{'type':'Gauge',
    'name':'loadconvert',
    'position':(7, 306),
    'size':(571, 32),
    'layout':'horizontal',
    'max':100,
    'value':0,
    },

{'type':'StaticText',
    'name':'pyexestatic',
    'position':(10, 38),
    'text':u'Python version you want to use:',
    },

{'type':'Button',
    'name':'pybrowse',
    'position':(510, 7),
    'command':u'choosepyfile',
    'label':u'Browse...',
    },


{'type':'StaticText',
    'name':'pystatic',
    'position':(10, 10),
    'text':u'Python script you want to convert:',
    },

{'type':'CheckBox',
    'name':'cmdcheck',
    'position':(9, 113),
    'label':u'Hide CMD window. (Default: Show CMD window)',
    },

{'type':'TextField',
    'name':'iconbox',
    'position':(95, 90),
    'size':(409, 18),
    'enabled':False,
    },

{'type':'Button',
    'name':'iconbrowse',
    'position':(510, 88),
    'command':u'cmdicon',
    'enabled':False,
    'label':u'Browse...',
    },

{'type':'Button',
    'name':'convert',
    'position':(6, 132),
    'size':(573, 168),
    'command':'cmdconvert',
    'font':{'faceName': u'MS Shell Dlg 2', 'family': 'sansSerif', 'size': 40},
    'label':u'Convert!',
    },

{'type':'CheckBox',
    'name':'iconcheck',
    'position':(9, 88),
    'size':(85, 20),
    'label':u' Custom Icon:',
    },

] # end components
} # end background
] # end backgrounds
} }
else:
    rsrc={'application':{'type':'Application',
          'name':'Template',
    'backgrounds': [
    {'type':'Background',
          'name':'PTEC 2.0',
          'title':u'PTEC 2.0',
          'size':(769, 370),
          'statusBar':1,
          'icon':'iconv2.ico',

        'menubar': {'type':'MenuBar',
         'menus': [
             {'type':'Menu',
             'name':'menuFile',
             'label':'&File',
             'items': [
                  {'type':'MenuItem',
                   'name':'menuFileNew',
                   'label':u'&New\tCtrl+N',
                   'command':'new',
                  },
                  {'type':'MenuItem',
                   'name':'menuFileOpen',
                   'label':u'&Open...\tCtrl+O',
                   'command':'open',
                  },
                  {'type':'MenuItem',
                   'name':'menuFileSave',
                   'label':u'&Save\tCtrl+S',
                   'command':'save',
                  },
                  {'type':'MenuItem',
                   'name':'menuFileSaveas',
                   'label':u'Save &as...\tCtrl+Shift+S',
                   'command':'saveas',
                  },
                  {'type':'MenuItem',
                   'name':'Dash3',
                   'label':u'-',
                  },
                  {'type':'MenuItem',
                   'name':'menuFileExit',
                   'label':u'E&xit\tAlt+F4',
                   'command':'exit',
                  },
              ]
             },
             {'type':'Menu',
             'name':'menuConvert',
             'label':u'&Convert',
             'items': [
                  {'type':'MenuItem',
                   'name':'menuConvertConvert',
                   'label':u'&Convert!\tCtrl+T',
                   'command':'cmdconvert',
                  },
              ]
             },
             {'type':'Menu',
             'name':'menuHelpandUpdates',
             'label':u'&Help and Updates',
             'items': [
                  {'type':'MenuItem',
                   'name':'menuHelpandUpdatesHelp',
                   'label':u'&Help\tCtrl+H',
                   'command':'cmdh',
                  },
                  {'type':'MenuItem',
                   'name':'menuHelpandUpdatesinfo',
                   'label':u'&Version Info\tCtrl+E',
                   'command':'info',
                  },
                  {'type':'MenuItem',
                   'name':'menuHelpandUpdatesLicense',
                   'label':u'&License\tCtrl+L',
                   'command':'license',
                  },
                  {'type':'MenuItem',
                   'name':'Dash2',
                   'label':u'-',
                  },
                  {'type':'MenuItem',
                   'name':'menuHelpandUpdatesCheckforupadates',
                   'label':u'Check for &Updates\tCtrl+U',
                   'command':'cfu',
                  },
              ]
             },
         ]
     },
         'components': [


{'type':'TextField',
    'name':'pybox',
    'position':(239, 6),
    'size':(439, -1),
    },

{'type':'Button',
    'name':'pyexebrowse',
    'position':(680, 35),
    'command':u'pyexebrowse',
    'label':u'Browse...',
    },

{'type':'TextField',
    'name':'pyexedrop',
    'position':(329, 35),
    'size':(349, -1),
    'command':u'pyexebrowse',
    'text':u'/usr/bin/python2.7',
    },

{'type':'Button',
    'name':'exebrowse',
    'position':(680, 65),
    'command':u'cmdexe',
    'label':u'Browse...',
    },

{'type':'TextField',
    'name':'exebox',
    'position':(347, 66),
    'size':(331, -1),
    },

{'type':'StaticText',
    'name':'exestatic',
    'position':(10, 70),
    'backgroundColor':(242, 241, 240, 255),
    'text':u'Location you want to save the converted program:',
    },

{'type':'Gauge',
    'name':'loadconvert',
    'position':(11, 311),
    'size':(754, 32),
    'backgroundColor':(229, 227, 225, 255),
    'layout':'horizontal',
    'max':100,
    'value':0,
    },

{'type':'StaticText',
    'name':'pyexestatic',
    'position':(10, 40),
    'size':(317, -1),
    'backgroundColor':(242, 241, 240, 255),
    'text':u'Python version you want to use (Python 2.4-2.7):',
    },

{'type':'Button',
    'name':'pybrowse',
    'position':(680, 5),
    'command':u'choosepyfile',
    'label':u'Browse...',
    },

{'type':'StaticText',
    'name':'pystatic',
    'position':(10, 10),
    'backgroundColor':(242, 241, 240, 255),
    'text':u'Python script you want to convert:',
    },

{'type':'Button',
    'name':'convert',
    'position':(10, 100),
    'size':(755, 207),
    'command':'cmdconvert',
    'font':{'faceName': u'MS Shell Dlg 2', 'family': 'sansSerif', 'size': 40},
    'label':u'Convert!',
    },

] # end components
} # end background
] # end backgrounds
} }
def see(self):
    self.components.pyexedrop.enabled=True
    self.components.exebrowse.enabled=True
    self.components.pyexebrowse.enabled=True
    self.components.exestatic.enabled=True
    self.components.pyexestatic.enabled=True
    self.components.pybrowse.enabled=True
    self.components.exebox.enabled=True
    self.components.pybox.enabled=True
    self.components.pystatic.enabled=True
    self.components.convert.enabled=True
    if sys.platform=="win32":
        self.components.cmdcheck.enabled=True
        self.components.iconbox.checked=True
        self.components.iconcheck.enabled=True
        if self.components.iconcheck.checked==True:
            self.components.iconbox.enabled=True
            self.components.iconbrowse.enabled=True
        else:
            self.components.iconbox.enabled=False
            self.components.iconbrowse.enabled=False
def nosee(self):
    self.components.pyexedrop.enabled=False
    self.components.pyexebrowse.enabled=False
    self.components.exebrowse.enabled=False
    self.components.exestatic.enabled=False
    self.components.pyexestatic.enabled=False
    self.components.pybrowse.enabled=False
    self.components.pybox.enabled=False
    self.components.exebox.enabled=False
    self.components.pystatic.enabled=False
    self.components.convert.enabled=False
    if sys.platform=="win32":
        self.components.cmdcheck.enabled=False
        self.components.iconbox.checked=False
    
        self.components.iconcheck.enabled=False
        self.components.iconbox.enabled=False
        self.components.iconbrowse.enabled=False
# and here is the end....

class MainWindow(model.Background):
    #Start-up
    def on_initialize(self, event):
        self.current="2.0"
        #Timer for "Converting..."
        self.myTimer=timer.Timer(self.components.convert, -1)
        self.myTimer.Start(4000)
        #gets the whole taskbar thing going
        self.startTitle=self.title
        self.currentpath=None
        self.name=""
        if len(sys.argv)>1:
            pkl=open(sys.argv[1], "r")
            fileopen=pickle.load(pkl)
            self.components.pybox.text=fileopen[0]
            self.components.pyexedrop.text=fileopen[1]
            self.components.exebox.text=fileopen[2]
            if sys.platform=="win32":
                self.components.iconcheck.checked=fileopen[3]
                self.components.iconbox.text=fileopen[4]
                self.components.cmdcheck.checked=fileopen[5]
            pkl.close()
            self.currentpath=sys.argv[1]
            self.name=os.path.basename(sys.argv[1])
            self.title=self.name+" - "+self.startTitle
        else:
            self.on_new_command(None)
        self.tick=False
        self.statusBar.text="(C) 2011-2012 PTEC Productions"
        see(self)
        self.os=sys.platform
        internet =1
        try:
            x=urllib.urlopen("http://ptecproductions.webs.com/stable.txt")
        except IOError:
            internet=0
        if internet ==1:
            y=x.read()
            y=y.strip()
            stable=y
            if self.current<stable:
                x=dialog.messageDialog(self, "New update available! PTEC %s is now out.\nWould you like to download it now?" % stable, "Auto-Updater", wx.ICON_INFORMATION|wx.YES_NO)
                if x.accepted == True:
                    webbrowser.open('http://ptecproductions.webs.com/ptec')
    #Convert button moving.
    def on_convert_timer(self, event):
        if self.tick==True:
            self.components.convert.label="Converting"
            time.sleep(1)
            self.components.convert.label="Converting."
            time.sleep(1)
            self.components.convert.label="Converting.."
            time.sleep(1)
            self.components.convert.label="Converting..."
        else:
            self.components.convert.label="Convert!"
            self.statusBar.text="(C) 2011-2012 PTEC Productions"
    if sys.platform=="win32":
        # if click in icon check box makes browse and txt box useable also no ever from menu. turns on icon switch.
        def on_iconcheck_mouseClick(self, event):
            see(self)
        #Browse button for icon. if the check box isnt checked, error. prints results from fileopenbox.
        def on_cmdicon_command(self, event):
            if self.components.iconcheck.checked==True:
               wildcard = "Icon files (*.ico)|*.ico"
               x=dialog.openFileDialog(wildcard=wildcard)
               x.paths=x.paths.pop()
               self.components.iconbox.text=str(x.paths)
            else:
                dialog.messageDialog(self, '"Custom Icon:" checkbox not selected.', "Error!", wx.ICON_ERROR)
    #Browse for py file and prints it in box.
    def on_choosepyfile_command(self, event):
        wildcard = "Python script (*.py;*.pyw)|*.py;*.pyw"
        x=dialog.openFileDialog(wildcard=wildcard)
        x.paths=x.paths.pop()
        self.components.pybox.text=str(x.paths)
    def on_pyexebrowse_command(self, event):
        if sys.platform=="win32":
            wildcard = "Python (python.exe)|python.exe"
        else:
            wildcard = "Python (python2*)|python2*"
        x=dialog.openFileDialog(wildcard=wildcard)
        x.paths=x.paths.pop()
        self.components.pyexedrop.text=str(x.paths)
    #Choose save loction for exe and prints it in box.
    def on_cmdexe_command(self, event):
        if sys.platform=="win32":
            wildcard = "Executable file (*.exe)|*.exe"
        else:
            wildcard = "Executable (*)|*"    
        x=dialog.saveFileDialog(wildcard=wildcard)
        x.paths=x.paths.pop()
        self.components.exebox.text=str(x.paths)
    #Checks for Updates.
    def on_cfu_command(self, event):
        try:
            x=urllib.urlopen("http://ptecproductions.webs.com/stable.txt")
        except IOError:
            dialog.messageDialog(self, "No internet access.", "No Internet", wx.ICON_INFORMATION)
        y=x.read()
        y=y.strip()
        stable=y
        if self.current==stable:
            dialog.messageDialog(self, "No new updates available.", "Check for Updates", wx.ICON_INFORMATION)
        elif self.current<stable:
            x=dialog.messageDialog(self, "New update available! PTEC %s is now out.\nWould you like to download it now?" % stable, "Check for Updates", wx.ICON_INFORMATION|wx.YES_NO)
            if x.accepted == True:
                webbrowser.open('http://ptecproductions.webs.com/ptec')
        else:
                dialog.messageDialog(self, "You seem to have a version of PTEC that hasn't come out yet...", "Check for Updates", wx.ICON_INFORMATION)
    #Help. PTEC email.
    def on_cmdh_command(self, event):
        msg="""Help:
    OS: Windows and Linux (Ubuntu)
    Python versions: 2.4.x-2.7.x
    Computer architectures: 32-bit, 64-bit
    fill everything in correctly, it'll be ok!

Bugs, comments, suggestions, etc:
    email: ptecproductions@gmail.com
    site: http://ptecproductions.webs.com"""
        dialog.scrolledMessageDialog(self, msg, "Help")
    #Info
    def on_info_command(self, event):
        msg="""Version 2.0
    added Ubuntu x32 and x64 support
    fixed my english in regards to understanding what the program wants, etc
    bug fixes
    updated help
    pywin32 218 support
    'subprocess' instead os 'os.system', which apparently is better
    now uses the new ptecproductions.webs.com website!
    [WINDOWS] changed choosing Python Directory to python.exe
Version 1.9.1
    fix links in installed version
    fixed a pywin32 bug
    fixed major bug "space in python dir error"
    updated pywin32 messages
    minor bug fixes
    removed "notice" whenever you click the convert button
    added auto-updater
    added save-on-close
Version 1.9
    updated pyinstaller to dev code (no choice)
    discontinued support for Python 2.3
    updated updater
    updated help
    updated intaller
    other various fixes
Version 1.8
    fixed spelling mistakes
    created abilty to choose python directory
    removed a few menus (unnecessary)
    fixed icon
    better way to detect and install pywin32
    fixed help
Version 1.7
    updated for pyinstaller 2.0
    removed support for Python 2.2 (in GUI)
    general code cleanup
    removed the taskbar icon (it was annoying)
Version 1.6.1.1
    few spelling changes
    made a few unnoticeable changes
    updated help
    fixed no intenet bug (only fixed for "check for updates")
Version 1.6.1:
    updated to pywin32 build 217
    copyright changed to 2011-2012
Version 1.6.0:
    works!                          not yet
    updated to: PyInstaller 1.5.1   yes
    multi-OS                        not yet
    fixed "tick" bug                yes
    icon on/off                     ????
    64-bit support                  not yet
    update help                     not yet
    disable icon in menu            yes no test
    multiple icon support           not yet
Version 1.5.0:
    Check for Updates choice that download new updates
    visible/invisble problems fixed
    icon on taskbar!
    much, much smaller (14.8 MB)
    got a license and copyright for PTEC (Which is why you cant get old versions of this program)
    fixed all (or most) spelling mistakes
Version 1.2.6 & 1.2.7:
    Took out Downloads menu because it didn't work.
    Locations were messed up but now fixed
    Added the would e-mail list
    100% sure it works this time around (kind of)
    mistake at the end of the conversion where for some reason the icon menu goes back to normal is fixed (kind of)
    says "Converting..." on the status menu
Version 1.2.0:
    support for Python 3.2
    "Downloads" menu
    Checking for updates through the internet
    PTEC Productions e-mail
    Downloads though the internet
Version 1.1.0 and before:
    didn't even work."""
        dialog.scrolledMessageDialog(self, msg, "Version Info")
    # License:
    def on_license_command(self, event):
        msg="""PTEC: An easy way to convert python files to standalone executables.
Copyright (C) 2011-2012 PTEC Productions

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>."""
        dialog.scrolledMessageDialog(self, msg, "License")
    #File >> open
    def on_open_command(self, event):
        wildcard = "PTEC files (*.ptec)|*.ptec"
        x=dialog.openFileDialog(wildcard=wildcard)
        x=str(x.paths.pop())
        pkl=open(x, "r")
        fileopen=pickle.load(pkl)
        self.components.pybox.text=fileopen[0]
        self.components.pyexedrop.text=fileopen[1]
        self.components.exebox.text=fileopen[2]
        if sys.platform=='win32':
            self.components.iconcheck.checked=fileopen[3]
            self.components.iconbox.text=fileopen[4]
            self.components.cmdcheck.checked=fileopen[5]
        pkl.close()
        if sys.platform=='win32':
            if self.components.iconcheck.checked==True:
                self.components.iconbox.enabled=True
                self.components.iconbrowse.enabled=True
            else:
                self.components.iconbox.enabled=False
                self.components.iconbrowse.enabled=False
        self.name=os.path.basename(x)
        self.title=self.name+" - "+self.startTitle
        self.currentpath=x
    #File >> save as
    def on_saveas_command(self, event):
        wildcard = "PTEC files (*.ptec)|*.ptec"
        x=dialog.saveFileDialog(wildcard=wildcard)
        x=str(x.paths.pop())
        pkl=open(x, "w")
        if sys.platform=='win32':
            filesave=[self.components.pybox.text, self.components.pyexedrop.text, self.components.exebox.text, \
                  self.components.iconcheck.checked, self.components.iconbox.text, self.components.cmdcheck.checked]
        else:
            filesave=[self.components.pybox.text, self.components.pyexedrop.text, self.components.exebox.text, \
                  "False", "", "False"]
        pickle.dump(filesave, pkl)
        pkl.close()
        self.name=os.path.basename(x)
        self.title=self.name+" - "+self.startTitle
        self.currentpath=x
    # File >> Save
    def on_save_command(self, event):
        title=self.title
        if self.currentpath==None:
            self.on_saveas_command(None)
        else:
            x=self.currentpath
            pkl=open(x, "w")
            if sys.platform=='win32':
                filesave=[self.components.pybox.text, self.components.pyexedrop.text, self.components.exebox.text, \
                  self.components.iconcheck.checked, self.components.iconbox.text, self.components.cmdcheck.checked]
            else:
                filesave=[self.components.pybox.text, self.components.pyexedrop.text, self.components.exebox.text, \
                  "False", "", "False"]
            pickle.dump(filesave, pkl)
            pkl.close()
            self.name=os.path.basename(x)
            self.title=self.name+" - "+self.startTitle
    # File >> new
    def on_new_command(self, event):
        self.components.pybox.text=""
        if sys.platform=='win32':
            self.components.pyexedrop.text="C:\Python27\python.exe"
            self.components.iconcheck.checked=False
            self.components.iconbox.text=""
            self.components.cmdcheck.checked=False
        else:
            self.components.pyexedrop.text="/usr/bin/python2.7"
        self.components.exebox.text=""
        self.title="Untitled - "+self.startTitle
        self.currentpath=None
        self.name=""
    #Converter
    def on_cmdconvert_command(self, event):
        # Get tick moving:
        self.tick=True
        self.statusBar.text="Converting..."
        nosee(self)
        # Check if input is correct:
        x=self.components.pybox.text
        y=self.components.exebox.text
        l=self.components.pyexedrop.text
        if sys.platform=='win32':
            z=self.components.iconbox.text
            if self.components.pybox.text=='':
                self.statusBar.text="(C) 2011-2012 PTEC Productions"
                self.tick=False
                dialog.messageDialog(self, 'Nothing in "Python Script" textbox.', "Error!", wx.ICON_ERROR)
                see(self)
                a=0
            elif os.path.isfile(x)==False or (x.endswith(".py")==False and x.endswith(".pyw")==False)==True:
                self.statusBar.text="(C) 2011-2012 PTEC Productions"
                self.tick=False
                dialog.messageDialog(self, 'Invalid file in "Python Script" textbox.', "Error!", wx.ICON_ERROR)
                see(self)
                a=0
            else:
                a=1
            if self.components.exebox.text=='':
                self.statusBar.text="(C) 2011-2012 PTEC Productions"
                self.tick=False
                dialog.messageDialog(self, 'Nothing in "Executable File" textbox.', "Error!", wx.ICON_ERROR)
                see(self)
                b=0
            elif y.endswith(".exe")==False:
                self.statusBar.text="(C) 2011-2012 PTEC Productions"
                self.tick=False
                dialog.messageDialog(self, 'Invalid extention in "Executable File" textbox.', "Error!", wx.ICON_ERROR)
                see(self)
                b=0
            else:
                b=1
            if self.components.iconbox.text=='' and self.components.iconcheck.checked==True:
                self.statusBar.text="(C) 2011-2012 PTEC Productions"
                self.tick=False
                dialog.messageDialog(self, 'Nothing in "Icon" textbox.', "Error!", wx.ICON_ERROR)
                see(self)
                c=0
            elif self.components.iconcheck.checked==True and z.endswith(".ico")==False:
                self.statusBar.text="(C) 2011-2012 PTEC Productions"
                self.tick=False
                dialog.messageDialog(self, 'Invalid extention in "Icon" textbox.', "Error!", wx.ICON_ERROR)
                see(self)
                c=0
            else:
                c=1
            if self.components.pyexedrop.text=='':
                self.statusBar.text="(C) 2011-2012 PTEC Productions"
                self.tick=False
                dialog.messageDialog(self, 'Nothing in "Python" textbox.', "Error!", wx.ICON_ERROR)
                see(self)
                d=0
            elif os.path.isfile(l)==False or os.path.basename(l)!="python.exe":
                self.statusBar.text="(C) 2011-2012 PTEC Productions"
                self.tick=False
                dialog.messageDialog(self, 'Invalid file in "Python" textbox.', "Error!", wx.ICON_ERROR)
                see(self)
                d=0
            else:
                d=1
            py=os.path.dirname(self.components.pyexedrop.text)
            py=py+"\\"
            path=py+"Doc"
            files=os.listdir(path)
            files=files.pop()
            files=files.replace(' ', '')[:-5].upper()
            if files.endswith("6")==True or files.endswith("7")==True or files.endswith("6")==True or files.endswith("5")==True or files.endswith("4")==True:
                e=1
            else:
                self.statusBar.text="(C) 2011-2012 PTEC Productions"
                self.tick=False
                dialog.messageDialog(self, 'Invalid Python version in "Python" textbox.', "Error!", wx.ICON_ERROR)
                see(self)
                e=0
        else:
            if self.components.pybox.text=='':
                self.statusBar.text="(C) 2011-2012 PTEC Productions"
                self.tick=False
                dialog.messageDialog(self, 'Nothing in "Python Script" textbox.', "Error!", wx.ICON_ERROR)
                see(self)
                a=0
            elif os.path.isfile(x)==False or (x.endswith(".py")==False and x.endswith(".pyw")==False)==True:
                self.statusBar.text="(C) 2011-2012 PTEC Productions"
                self.tick=False
                dialog.messageDialog(self, 'Invalid file in "Python Script" textbox.', "Error!", wx.ICON_ERROR)
                see(self)
                a=0
            else:
                a=1
            if self.components.exebox.text=='':
                self.statusBar.text="(C) 2011-2012 PTEC Productions"
                self.tick=False
                dialog.messageDialog(self, 'Nothing in "Executable" textbox.', "Error!", wx.ICON_ERROR)
                see(self)
                b=0
            else:
                b=1
            c=1
            if self.components.pyexedrop.text=='':
                self.statusBar.text="(C) 2011-2012 PTEC Productions"
                self.tick=False
                dialog.messageDialog(self, 'Nothing in "Python" textbox.', "Error!", wx.ICON_ERROR)
                see(self)
                d=0
            elif os.path.isfile(l)==False or os.path.basename(l).startswith("python2")==False:
                self.statusBar.text="(C) 2011-2012 PTEC Productions"
                self.tick=False
                dialog.messageDialog(self, 'Invalid file in "Python" textbox.', "Error!", wx.ICON_ERROR)
                see(self)
                d=0
            else:
                d=1
            py=self.components.pyexedrop.text
            files=py
            files=files[-3:]
            if (files) > 2.3:
                e=1
            else:
                self.statusBar.text="(C) 2011-2012 PTEC Productions"
                self.tick=False
                dialog.messageDialog(self, 'Invalid Python version in "Python Directory" textbox.', "Error!", wx.ICON_ERROR)
                see(self)
                e=0
        # If everything is good:
        if a==1 and b==1 and c==1 and d==1 and e==1:
            pla=1
            if sys.platform=='win32':
                pla=0
                # Check if you need to install pywin32
                if os.path.isfile(self.components.exebox.text):
                    os.remove(self.components.exebox.text)
                self.components.loadconvert.value=12
                py=py+"\\"
                path=py+"Doc"
                files=os.listdir(path)
                files=files.pop()
                files=files.replace(' ', '')[:-5].upper()
                if files.endswith("6")==True or files.endswith("7")==True:
                    xer = True
                else:
                    xer=False
                # Start of check
                if os.path.isfile(py+"Lib/site-packages/pythoncom.py")==False and xer==True:
                    dia=dialog.messageDialog(self, 'The following needs to be installed:\npywin32\n\nIt needs to be installed in order for PTEC to run.\nWould you like to be sent to the pywin32 website to download it now?\nNote: internet connection required.', "Notice!", wx.ICON_INFORMATION|wx.YES_NO|wx.YES_DEFAULT)
                    if dia.accepted==True:
                        webbrowser.open('http://sourceforge.net/projects/pywin32/files/pywin32/Build 218/')
                        dialog.messageDialog(self, "When the installation is complete, click Convert to begin converting.", "Installer Info", wx.OK)
                        pla=1
                pla=1
            if pla == 1:
                # Configuring...
                self.components.loadconvert.value=25
                onefile="--onefile"
                if sys.platform=='win32':
                    if self.components.cmdcheck.checked==True:
                        cmd="--windowed"
                    else:
                        cmd=""
                    if self.components.iconcheck.checked==True:
                        shutil.copy(self.components.iconbox.text, "icon.ico")
                        icon='--icon=icon.ico'
                    else:
                        icon=""
                name="--name=spec"
                self.components.loadconvert.value=50
                shutil.copy(self.components.pybox.text, "py.py")
    #           building...
                if sys.platform=='win32':
                    com=["%spython.exe" % py, "pyinstaller\pyinstaller.py", onefile,cmd,icon,name, "py.py"]
                    if com[4]=="":
                        com.pop(4)
                    if com[3]=="":
                        com.pop(3)
                    proc=subprocess.Popen(com, shell=False)
                else:
                    com=["%s" % py, "pyinstaller/pyinstaller.py",onefile,name,"py.py"]
                    proc=subprocess.Popen(com, shell=False)
                proc.wait()
                self.components.loadconvert.value=75
                if sys.platform=='win32':
                    os.renames("dist\spec.exe", self.components.exebox.text)
                else:
                    os.renames("dist/spec", self.components.exebox.text)
                # Done!
                self.components.loadconvert.value=100
                self.statusBar.text="(C) 2011-2012 PTEC Productions"
                self.tick=False
                dialog.messageDialog(self, "Conversion Sucessful.", "Completed.", wx.OK)
                self.components.loadconvert.value=0
                see(self)
        see(self)
        self.statusBar.text="(C) 2011-2012 PTEC Productions"
        self.tick=False
        self.components.loadconvert.value=0
    def on_close(self, event):
        if self.name!="":
            pkl=open(self.currentpath, "r")
            fileopen=pickle.load(pkl)
            if sys.platform=='win32':
                filesave=[self.components.pybox.text, self.components.pyexedrop.text, self.components.exebox.text, \
                      self.components.iconcheck.checked, self.components.iconbox.text, self.components.cmdcheck.checked]
            else:
                filesave=[self.components.pybox.text, self.components.pyexedrop.text, self.components.exebox.text, \
                      "False", "", "False"]
            if fileopen != filesave:
                final=dialog.messageDialog(self, 'Would you like to save changes to "%s"?"' % self.name, "PTEC %s" % self.current, wx.YES_NO|wx.CANCEL|wx.YES_DEFAULT)
                if final.returnedString=="Yes":
                    title=self.title
                    if self.currentpath==None:
                        self.on_saveas_command(None)
                    else:
                        x=self.currentpath
                        pkl=open(x, "w")
                        pickle.dump(filesave, pkl)
                        pkl.close()
                        self.name=os.path.basename(x)
                        self.title=self.name+" - "+self.startTitle
                        sys.exit(0)
                elif final.returnedString=="No":
                    sys.exit(0)
                elif final.returnedString=="Cancel":
                    pass
                else:
                    sys.exit(0)
            else:
                sys.exit(0)
        else:
            sys.exit(0)
app=model.Application(MainWindow, None, rsrc)
app.MainLoop()
