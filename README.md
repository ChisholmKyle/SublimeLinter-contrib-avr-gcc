SublimeLinter-contrib-avr-gcc
================================

[![Build Status](https://travis-ci.org/SublimeLinter/SublimeLinter-contrib-avr-gcc.svg?branch=master)](https://travis-ci.org/SublimeLinter/SublimeLinter-contrib-avr-gcc)

This linter plugin for [SublimeLinter][docs] provides an interface to [avr-gcc](http://www.atmel.com/webdoc/AVRLibcReferenceManual/overview_1overview_gcc.html). It will be used with files that have the “C/C++” syntax. This linter is based on [SublimeLinter-contrib-clang](https://packagecontrol.io/packages/SublimeLinter-contrib-clang).

## Installation
SublimeLinter 3 must be installed in order to use this plugin. If SublimeLinter 3 is not installed, please follow the instructions [here][installation].

### Linter installation

Before using this plugin, you must ensure that `avr-gcc` is installed on your system. To install `avr-gcc`, do the following:

#### Linux

1. Install `avr-gcc` with your distro's package manager. On Ubuntu, for example, type the following in a terminal:

    sudo apt-get install git gcc-avr

#### Mac

1. Install and update [Macports](https://www.macports.org/)
2. Type the following in a terminal:

    sudo port install avr-gcc

#### Windows

1. Download and extract the [Amtel AVR Toolchain for Windows](http://www.atmel.com/tools/atmelavrtoolchainforwindows.aspx).

### Linter configuration
In order for `avr-gcc` to be executed by SublimeLinter, you must ensure that its path is available to SublimeLinter. Before going any further, please read and follow the steps in [“Finding a linter executable”](http://sublimelinter.readthedocs.org/en/latest/troubleshooting.html#finding-a-linter-executable) through “Validating your PATH” in the documentation.

Once you have installed and configured `avr-gcc`, you can proceed to install the SublimeLinter-contrib-avr-gcc plugin if it is not yet installed.

### Plugin installation
Please use [Package Control][pc] to install the linter plugin. This will ensure that the plugin will be updated when new versions are available. If you want to install from source so you can modify the source code, you probably know what you are doing so we won’t cover that here.

To install via Package Control, do the following:

1. Within Sublime Text, bring up the [Command Palette][cmd] and type `install`. Among the commands you should see `Package Control: Install Package`. If that command is not highlighted, use the keyboard or mouse to select it. There will be a pause of a few seconds while Package Control fetches the list of available plugins.

1. When the plugin list appears, type `avr-gcc`. Among the entries you should see `SublimeLinter-contrib-avr-gcc`. If that entry is not highlighted, use the keyboard or mouse to select it.

## Settings
For general information on how SublimeLinter works with settings, please see [Settings][settings]. For information on generic linter settings, please see [Linter Settings][linter-settings].

In addition to the standard SublimeLinter settings, SublimeLinter-contrib-avr-gcc provides its own settings.

|Setting|Description|
|:------|:----------|
|include_dirs|A list of directories to be added to the header search paths (-I is not needed).|
|extra_flags|A string with extra flags to pass to avr-gcc. These should be used carefully, as they may cause linting to fail.|

In project-specific settings, '${project_folder}' can be used to specify a relative path. Here is an example of project settings for development on an Arduino Mini Pro 5V:

```
"SublimeLinter":
{
    "linters":
    {
        "avrgcc": {
            "include_dirs": [
                "${project_folder}/include",
                "/Applications/Arduino.app/Contents/Java/hardware/arduino/avr/cores/arduino"
            ],
            "extra_cflags": "-mmcu=atmega328p -DF_CPU=16000000L"
        }
    }
},
```

## Contributing
If you would like to contribute enhancements or fixes, please do the following:

1. Fork the plugin repository.
1. Hack on a separate topic branch created from the latest `master`.
1. Commit and push the topic branch.
1. Make a pull request.
1. Be patient.  ;-)

Please note that modifications should follow these coding guidelines:

- Indent is 4 spaces.
- Code should pass flake8 and pep257 linters.
- Vertical whitespace helps readability, don’t be afraid to use it.
- Please use descriptive variable names, no abbreviations unless they are very well known.

Thank you for helping out!

[docs]: http://sublimelinter.readthedocs.org
[installation]: http://sublimelinter.readthedocs.org/en/latest/installation.html
[locating-executables]: http://sublimelinter.readthedocs.org/en/latest/usage.html#how-linter-executables-are-located
[pc]: https://sublime.wbond.net/installation
[cmd]: http://docs.sublimetext.info/en/sublime-text-3/extensibility/command_palette.html
[settings]: http://sublimelinter.readthedocs.org/en/latest/settings.html
[linter-settings]: http://sublimelinter.readthedocs.org/en/latest/linter_settings.html
[inline-settings]: http://sublimelinter.readthedocs.org/en/latest/settings.html#inline-settings
