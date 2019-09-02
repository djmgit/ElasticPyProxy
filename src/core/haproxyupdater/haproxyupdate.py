import os

class HaproxyUpdate(object):
    def __init__(self, **kwargs):

        '''
            Get desired params
        '''
        self.haproxy_config_file = kwargs.get("haproxy_config_file")
        self.template_file = kwargs.get("template_file")
        self.backend_port = kwargs.get("backend_port")
        self.node_list = kwargs.get("node_list")
        self.haproxy_binary = kwargs.get("haproxy_binary")
        self.init_file = kwargs.get("init_file")
        self.start_by = kwargs.get("start_by")

        self.valid_start_by = [
            "binary",
            "systemd",
            "init"
        ]

    def __sanitise(self):

        '''
            Validate all the paths
        '''
        if not os.path.isfile(self.haproxy_config_file):
            return False

        if not os.path.isfile(self.template_file):
            return False

        if self.backend_port < 0 or self.backend_port > 65536:
            return False

        if self.haproxy_binary and not os.path.isfile(self.haproxy_binary):
            return False

        if self.init_file and not os.path.isfile(self.init_file):
            return False

    def update_haproxy(self):
        pass

    def reload_haproxy(self):
        pass
