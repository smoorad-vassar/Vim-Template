# Vim-Template: A Boiler Plate Code Generator

## Description
Vim-Template is my first attempt at writing a vim plugin so it might not be the best one out there. It's written
in python with a VimL Wrapper over the python code.

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
- Go to the plugin directory
- Then go to the custom_templates directory
- Create a custom file with customName_template
- For example there are two Makefile templates for C and C++ files as follows:
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
