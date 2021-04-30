class Datapack():
    """A datapack class"""
    def __init__(self, project_name, namespace, dp_item, dp_desc, main_name, load_name, dp_path, dp_name, dev_name):
        """Constructor"""
        self.project_name = project_name
        self.namespace    = namespace
        self.item      = dp_item
        self.desc      = dp_desc
        self.main    = main_name
        self.load    = load_name
        self.path      = dp_path
        self.dp_name      = dp_name
        self.developer     = dev_name

    def set_defaults(self):
        """Set defaults for variables"""
        #> Adding default values if the description or the item or the main fun name or the load fun name are not defined <#
        if len(self.project_name) == 0:
            self.project_name = self.dp_name.replace(" ", "_").lower()
        if len(self.namespace) == 0:
            self.namespace = self.developer.lower()
        if len(self.item) == 0:
            self.item = 'name_tag'
        if len(self.desc) == 0:
            self.desc = 'This is the pack description'
        if len(self.main) == 0:
            self.main = 'main'
        if len(self.load) == 0:
            self.load = 'setup'
        if len(self.path) == 0:
            self.path = '.'

