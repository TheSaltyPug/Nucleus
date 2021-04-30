"""
Nucleus by Gnottero
Forked  by TSP
"""

# Import all the required libraries
import os
import json
import requests
from Datapack import Datapack

def try_mkdir(path):
    """Attempt to create a directory"""
    try:
        os.makedirs(path)
    except FileExistsError:
        pass

def gen_pack_mcmeta(dp_path,dp_name,dev_name):
    """Generate datapack metadata file"""
    pack = {"pack": {"pack_format": 5,"description": f"{dp_name} by {dev_name}"}}
    with open(f'{dp_path}/{dp_name}/pack.mcmeta', 'w') as fout:
        fout.write(json.dumps(pack, indent=5, sort_keys=True))

def global_advancements(g_adv_path,namespace,dev_name,skull_value):
    """Create the global advancements"""
    root = {
            "display":
            {
                "title": "Installed Datapacks",
                "description": "",
                "icon":
                {
                    "item": "minecraft:knowledge_book"
                    },
                "background": "minecraft:textures/block/gray_concrete.png",
                "show_toast": False,
                "announce_to_chat": False
                },
            "criteria":
            {
                "trigger":
                {
                    "trigger":
                    "minecraft:tick"
                    }
                }
            }
    dev = {"display": {"title": f"{dev_name}","description": "","icon": {"item": "minecraft:player_head","nbt": f"{{SkullOwner:{{Name: \"{dev_name}\", Properties: {{textures: [{{Value: \"{skull_value}\"}}]}}}}}}"},"show_toast": False,"announce_to_chat": False},"parent": "global:root","criteria": {"trigger": {"trigger": "minecraft:tick"}}}

    with open(f'{g_adv_path}/root.json', 'w') as fout:
        fout.write(json.dumps(root, indent=5, sort_keys=True))
    with open(f'{g_adv_path}/{namespace}.json', 'w') as fout:
        fout.write(json.dumps(dev, indent=5, sort_keys=True))

def dp_advancement(dp_adv_path,project_name,dp_name,dp_desc,dp_item,namespace):
    """Create the datapack advancement"""
    dp_adv = {"display": {"title": f"{dp_name.title()}","description": f"{dp_desc}","icon": {"item": f"minecraft:{dp_item}"},"announce_to_chat": False,"show_toast": False},"parent": f"global:{namespace}","criteria": {"trigger": {"trigger": "minecraft:tick"}}}
    with open(f'{dp_adv_path}/{project_name}.json', 'w') as fout:
        fout.write(json.dumps(dp_adv, indent=5, sort_keys=True))

def mc_tags(mc_tags_path,namespace,project_name):
    """Create the tick and load files inside minecraft:%"""
    mc_load = {"values": [f"#{namespace}:{project_name}/load"]}
    mc_tick = {"values": [f"#{namespace}:{project_name}/loop"]}

    with open(f'{mc_tags_path}/load.json', 'w') as fout:
        fout.write(json.dumps(mc_load, indent=5, sort_keys=True))
    with open(f'{mc_tags_path}/tick.json', 'w') as fout:
        fout.write(json.dumps(mc_tick, indent=5, sort_keys=True))

def dp_tags(dp_tags_path,namespace,main_name,load_name,project_name):
    """Create the tick and load files inside namespace:project/%"""
    ns_load = {"values": [f"{namespace}:{project_name}/{load_name}"]}
    ns_loop = {"values": [f"{namespace}:{project_name}/{main_name}"]}

    with open(f'{dp_tags_path}/load.json', 'w') as fout:
        fout.write(json.dumps(ns_load, indent=5, sort_keys=True))
    with open(f'{dp_tags_path}/loop.json', 'w') as fout:
        fout.write(json.dumps(ns_loop, indent=5, sort_keys=True))

def dp_fun(dp_fun_path,main_name,load_name,dp_name, namespace, project_name):
    """Fill the generated function files with neat stuff"""
    with open(f'{dp_fun_path}/{main_name}.mcfunction', 'w') as fout:
        fout.write(f"""#> {namespace}:{project_name}/{main_name}
                # This function will run every tick""")
    with open(f'{dp_fun_path}/{load_name}.mcfunction', 'w') as fout:
        fout.write(f"""#> {namespace}:{project_name}/{load_name}
                # This function will run on datapack loading""")
    with open(f'{dp_fun_path}/uninstall.mcfunction', 'w') as fout:
        fout.write(f"""#> {namespace}:{project_name}/uninstall
                This is the uninstall function\n datapack disable "file/{dp_name}" """)

def main():
    """The main function"""

    #> Setupping the variables <#
    dev_name = input('Please insert your name (Minecraft Username): ')
    dp_name = input('Please insert your datapack name: ')
    namespace = input('(Optional) Please insert the name of the namespace: ').replace(" ", "_").lower()
    project_name = input('(Optional) Please insert the project name: ').replace(" ", "_").lower()
    dp_item = input('(Optional) Please insert the id of the item that will be displayed in the advancement: ')
    dp_desc = input('(Optional) Please insert the description of the datapack: ')
    main_name = input('(Optional) Please insert the name of the main function: ').replace(" ", "_").lower()
    load_name = input('(Optional) Please insert the name of the load function: ').replace(" ", "_").lower()
    dp_path = input('(Optional) Please insert the path where you want to generate the datapack: ')

    datapack = Datapack(project_name, namespace, dp_item, dp_desc, main_name, load_name, dp_path, dp_name, dev_name)
    datapack.set_defaults()

    #> Requesting player data from the Mojang API <#
    # XXX do network check; if network proceeed, else default to no nbt and just the Username
    uuid_rq = requests.get(f'https://api.mojang.com/users/profiles/minecraft/{dev_name}')
    player_uuid = uuid_rq.json()['id']
    skull_value_rq = requests.get(f'https://sessionserver.mojang.com/session/minecraft/profile/{player_uuid}')
    skull_value = skull_value_rq.json()['properties'][0]['value']

    #> Starting the generation phase <#

    #> Generating all the needed folder <#
    g_adv_path = f"{dp_path}/{dp_name}/data/global/advancements"
    dp_adv_path = f"{dp_path}/{dp_name}/data/{namespace}/advancements/{project_name}"
    mc_tags_path = f"{dp_path}/{dp_name}/data/minecraft/tags/functions"
    dp_tags_path = f"{dp_path}/{dp_name}/data/{namespace}/tags/functions/{project_name}"
    dp_fun_path = f"{dp_path}/{dp_name}/data/{namespace}/functions/{project_name}"

    try_mkdir(g_adv_path)
    try_mkdir(dp_adv_path)
    try_mkdir(mc_tags_path)
    try_mkdir(dp_tags_path)
    try_mkdir(dp_fun_path)

    gen_pack_mcmeta(dp_path,dp_name,dev_name)
    global_advancements(g_adv_path,namespace,dev_name,skull_value)
    dp_advancement(dp_adv_path,project_name,dp_name,dp_desc,dp_item,namespace)
    mc_tags(mc_tags_path,namespace,project_name)
    dp_tags(dp_tags_path,namespace,main_name,load_name,project_name)
    dp_fun(dp_fun_path,main_name,load_name,dp_name, namespace, project_name)

    print(
        f'''Template generated successfully with the following info:

        Datapack developer: {dev_name}
        Datapack name: {dp_name}
        Datapack namespace: {namespace}
        Datapack item: minecraft:{dp_item}
        Datapack description: {dp_desc}

    '''
    )


if __name__ == "__main__":
    main()
