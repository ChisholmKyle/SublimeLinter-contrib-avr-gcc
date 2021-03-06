SublimeLinter-contrib-avr-gcc
================================

[![Build Status](https://travis-ci.org/ChisholmKyle/SublimeLinter-contrib-avr-gcc.svg?branch=master)](https://travis-ci.org/ChisholmKyle/SublimeLinter-contrib-avr-gcc)

This linter plugin for [SublimeLinter](https://github.com/SublimeLinter/SublimeLinter) provides an interface to [avr-gcc](http://www.atmel.com/webdoc/AVRLibcReferenceManual/overview_1overview_gcc.html). This linter will be used with files that have the “C/C++” syntax.

### Tip for usage with Arduino

If you are new to `avr-gcc` or microprocessors in general and want to get started using the [Arduino](https://www.arduino.cc/) library with C/C++ source files and great linting, this plugin can help (but does require some manual setup). See the example in [Settings](#settings) for using it with an Arduino Pro 5V and Wire library. If you set your Arduino IDE to show verbose output when compiling (enable in Arduino preferences), you can easily extract the required compiler flags for linting with `avr-gcc`.

## Installation

SublimeLinter must be installed in order to use this plugin.

Please use [Package Control](https://packagecontrol.io) to install the linter plugin.

### Install `avr-gcc`

Before using this plugin, you must ensure that `avr-gcc` is installed on your system. To install `avr-gcc`, do can do the following:

#### Linux

1. Install `avr-gcc` with your distro's package manager. On Ubuntu, for example, type the following in a terminal:
```
    sudo apt-get install git gcc-avr
```

#### Mac

Xcode and command line tools are required.

1. Install and update [Macports](https://www.macports.org/)
2. Type the following in a terminal:
```
    sudo port install avr-gcc
```

Alternatively, use Homebrew:

1. Install [Homebrew](https://brew.sh/)
2. Run the following commands:
```
    brew tap osx-cross/avr
    brew install avr-libc
```

#### Windows

1. Download and extract the [Microchip AVR Toolchain for Windows](https://www.microchip.com/mplab/avr-support/avr-and-arm-toolchains-c-compilers).

### Configure PATH

In order for `avr-gcc` to be executed by SublimeLinter, you must ensure that its path is available to SublimeLinter. The docs cover [troubleshooting PATH configuration](http://sublimelinter.readthedocs.io/en/latest/troubleshooting.html#finding-a-linter-executable).

## Settings
- SublimeLinter settings: [http://sublimelinter.readthedocs.org/en/latest/settings.html](http://sublimelinter.readthedocs.org/en/latest/settings.html)
- Linter settings: [http://sublimelinter.readthedocs.org/en/latest/linter_settings.html](http://sublimelinter.readthedocs.org/en/latest/linter_settings.html)

Additional SublimeLinter-contrib-avr-gcc settings:

|Setting|Description|
|:------|:----------|
|include_dirs|A list of directories to be added to the header search paths (-I is not needed).|
|extra_flags|A string with extra flags to pass to avr-gcc. These should be used carefully, as they may cause linting to fail.|
|extra_cflags|Extra flags to pass to avr-gcc when linting C syntax code.|
|extra_cxxflags|Extra flags to pass to avr-gcc when linting C++ syntax code.|

In project-specific settings, note that SublimeLinter allows [expansion variables](http://sublimelinter.readthedocs.io/en/latest/settings.html#settings-expansion). For example the variable '${project_path}' can be used to specify a path relative to the project folder in your settings. Here is an example of project settings for development targeting an Arduino Mini Pro 5V with the Wire library:
```json
"settings": {
    "SublimeLinter.linters.avrgcc.executable": "C:/tools/avr8-gnu-toolchain-win32_x86/bin/avr-gcc.exe",
    "SublimeLinter.linters.avrgcc.extra_cflags": "-std=gnu99",
    "SublimeLinter.linters.avrgcc.extra_cxxflags": "-std=gnu++14",
    "SublimeLinter.linters.avrgcc.extra_flags": "-mmcu=atmega328p -DF_CPU=16000000L -DARDUINO_ARCH_AVR -DARDUINO_AVR_PRO",
    "SublimeLinter.linters.avrgcc.include_dirs": [
        "${project_path}/include",
        "C:/Program Files (x86)/Arduino/hardware/arduino/avr/cores/arduino",
        "C:/Program Files (x86)/Arduino/hardware/arduino/avr/variants/eightanaloginputs",
        "C:/Program Files (x86)/Arduino/hardware/arduino/avr/libraries/Wire/src",
        "C:/Program Files (x86)/Arduino/hardware/arduino/avr/libraries/Wire/src/utility"
    ]
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
