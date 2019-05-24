MODE = "Agent"  # SSH, Salt

PLUGINS = {
    'disk': 'src.plugins.disk.DiskPlugin',
    'men': 'src.plugins.mem.MenPlugin',
    'nic': 'src.plugins.nic.NicPlugin',
}
