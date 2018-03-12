SublimeLinter-contrib-avr-gcc
================================

[![Build Status](https://travis-ci.org/ChisholmKyle/SublimeLinter-contrib-avr-gcc.svg?branch=master)](https://travis-ci.org/ChisholmKyle/SublimeLinter-contrib-avr-gcc)

This linter plugin for [SublimeLinter](https://github.com/SublimeLinter/SublimeLinter) provides an interface to [avr-gcc](http://www.atmel.com/webdoc/AVRLibcReferenceManual/overview_1overview_gcc.html). It will be used with files that have the “C/C++” syntax. This linter is based on [SublimeLinter-contrib-clang](https://packagecontrol.io/packages/SublimeLinter-contrib-clang).

## Note: Breaking change in 2.0.0

Since version 2.0.0, the `${project_folder}` expansion variable will NOT be expanded in the settings. To fix this, replace with `${project_path}`. All expansion variables supported by SublimeLinter settings are described [here](http://sublimelinter.readthedocs.io/en/latest/settings.html#settings-expansion).

## Installation

SublimeLinter must be installed in order to use this plugin.

Please use [Package Control](https://packagecontrol.io) to install the linter plugin.

### Install `avr-gcc`

Before using this plugin, you must ensure that `avr-gcc` is installed on your system. To install `avr-gcc`, do can do the following:

#### Linux

1. Install `avr-gcc` with your distro's package manager. On Ubuntu, for example, type the following in a terminal:

    sudo apt-get install git gcc-avr

#### Mac

1. Install and update [Macports](https://www.macports.org/)
2. Type the following in a terminal:

    sudo port install avr-gcc

#### Windows

1. Download and extract the [Amtel AVR Toolchain for Windows](http://www.atmel.com/tools/atmelavrtoolchainforwindows.aspx).

### Configure PATH

In order for `avr-gcc` to be executed by SublimeLinter, you must ensure that its path is available to SublimeLinter. The docs cover [troubleshooting PATH configuration](http://sublimelinter.readthedocs.io/en/latest/troubleshooting.html#finding-a-linter-executable).

## Settings
- SublimeLinter settings: http://sublimelinter.readthedocs.org/en/latest/settings.html
- Linter settings: http://sublimelinter.readthedocs.org/en/latest/linter_settings.html

Additional SublimeLinter-contrib-avr-gcc settings:

|Setting|Description|
|:------|:----------|
|include_dirs|A list of directories to be added to the header search paths (-I is not needed).|
|extra_flags|A string with extra flags to pass to avr-gcc. These should be used carefully, as they may cause linting to fail.|
|extra_cflags|Extra flags to pass to avr-gcc when linting C syntax code.|
|extra_cxxflags|Extra flags to pass to avr-gcc when linting C++ syntax code.|

In project-specific settings, note that SublimeLinter allows [expansion variables](http://sublimelinter.readthedocs.io/en/latest/settings.html#settings-expansion). For example the variable '${project_path}' can be used to specify a path relative to the project folder for the `include_dirs` or `extra_flags` options. Here is an example of project settings for development targeting an Arduino Mini Pro 5V with the Wire library:

```
"SublimeLinter":
{
    "linters":
    {
        "avrgcc": {
            "include_dirs": [
                "${project_path}/include",
                "/Applications/Arduino.app/Contents/Java/hardware/arduino/avr/cores/arduino",
                "/Applications/Arduino.app/Contents/Java/hardware/arduino/avr/variants/eightanaloginputs",
                "/Applications/Arduino.app/Contents/Java/hardware/arduino/avr/libraries/Wire/src",
                "/Applications/Arduino.app/Contents/Java/hardware/arduino/avr/libraries/Wire/src/utility"
            ],
            "extra_flags": "-mmcu=atmega328p -DF_CPU=16000000L -DARDUINO_ARCH_AVR -DARDUINO_AVR_PRO",
            "extra_cflags": "-std=gnu99",
            "extra_cxxflags": "-std=gnu++14"
        }
    }
}
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
