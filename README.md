# Vim-Template: A Boiler Plate Code Generator

Table of Contents
=================

* [Description](#description)
* [Requirement](#requirement)
* [Installation Guide](#installation-guide)
* [How to use it](#how-to-use-it)
    * [Default Templates](#default-templates)
    * [Custom Templates](#custom-templates)
* [Extra Information](#extra-information)
* [TODO](#todo)

## Description
Vim-Template is my first attempt at writing a vim plugin so it might not be the best one out there. It's written
in python with a VimL Wrapper over the python code.

## Requirement
Python3 support is needed for the plugin to work:
* Almost all vim 8 have python3 unless you are working with the default MacOS vim. I'd suggest to download the latest vim version using homebrew:
```
brew install vim
```
* Neovim requires you to install python3 module. Look up the documentation to install the module:
```
:help provider
```

## Installation Guide
Use your favourite plugin manager for vim i.e. Vundle, vim-plug  then add this to your vimrc/init.vim:
1. Vundle
```
Plugin "saadparwaiz1/Vim-Template"
```
2. vim-plug
```
Plug "saadparwaiz1/Vim-Template"
```

## How to use it
There are two ways to utilise the plugin:
* Default Templates
* Custom Templates

### Default Templates
By default there is boiler plate code for following files:
1. C
2. C++
3. Java
4. HTML

Simply, open the file with correct extension i.e. index.html and then run:
```
:DefaultTemplate
```
That would add the default template for the file.

### Custom Templates
To use a custom template first you need to create it. This can be done as follows:
- Set path for your custom templates in your vimrc/init.vim using:
```
let g:vim_template_custom_directory
```
- If no path is set my custom_templates directory provided with the repo is used
- Create a custom file with customName_template
- For example there are two Makefile templates for C and C++ files as follows in my custom_templates directory:
    - makec_template
    - makecpp_template
- Now to use the custom template run the following code in vim:
```
:CustomTemplate customName
```
So for example to generate Makefile template for a C project we run:
```
:CustomTemplate makec
```

## Extra Information
To use the default templates in a file that doesn't contain the proper extension. For, example if you want to add html boiler plate code to a text file called
test.txt then the following code can be utilised:
```
:CustomTemplate html
```
By default the class name for Java files and title for HTML files is the file name.


## TODO
1. Implement boiler plate source code from header files
2. <s>Allow user to set a path for custom_templates directory</s>
