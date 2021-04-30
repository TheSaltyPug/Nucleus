# Pug's Nucleus
A simple datapack template generator written in Python3.

Generated datapacks follow select conventions from the 'Minecraft Datapacks' Discord server. You can learn more about these conventions [here](https://mc-datapacks.github.io/en/) or by [joining the Discord server](https://discord.gg/whFfamE).

This version has several goals:
- Clean up the source code
- Automatically create Git repositories
- Automatically create test worlds

More features might be added in the future upon request or necessity .

## Features
- Creates datapacks based on CLI input
- Created files follow [Arcensoth's IMP-Doc](https://github.com/Arcensoth/imp-spec/blob/master/docs/imp_doc.mdhttps://github.com/Arcensoth/imp-spec/blob/master/docs/imp_doc.md)
- Follows the following conventions from the Minecraft Datapacks Discord:
    - Datapack advancement
        - Creates the `global:root`, `global:<namespace>`, and `<namespace>:<project>` advancements
    - Datapack uninstallation
        - Creates a function that disables the datapack
    - Namespace convention
        - Created project files are organized by `<namespace>:<project>`
    - Reloading message
        - A reloading message is not generated

## Installation
Clone this repository or copy the file `nucleus.py` into the directory where you want to create a new datapack.

Nucleus requres the 'requests' module to work. You can install it by running `pip install requests` on UNIX systems.

## How to Use
Simply run the python file named Nucleus.

## TODO
- Better input/variable names
- refactor
    - functions
- Variables for use in other options
    - Minecraft directory
    - Template world name
    - git username
- Command line options
    - t, copy a template world, move datapack there
    - g, initialize a git repository
        - h, link with github
    - y, generate yellow shulker box
    - p, path

### Low Priority
- Create a make file to install nucleus in the user's $PATH

## Credit
The original version of Nucleus was created by Gnottero. You can find him here:

  - PlanetMinecraft page: https://www.planetminecraft.com/member/gnottero/
  - Github page: https://github.com/Gnottero
