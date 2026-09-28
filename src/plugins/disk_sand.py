from beet import Context
from beet.contrib.vanilla import Vanilla

from src.plugins.utils import iterate_versions, field_accessor, feature_registry, worldgen_config


def beet_default(ctx: Context):
    vanilla = ctx.inject(Vanilla)

    for pack, version in iterate_versions(ctx):
        registry = feature_registry(version)
        source = vanilla.releases[version].mount("data").data[registry]
        patched = source["minecraft:disk_sand"].copy()
        config = worldgen_config(patched.data)
        field = field_accessor(config, version)

        # Half of the height of this disk. Value between 0 and 4 (inclusive).
        config["half_height"] = 0 # defaults to 2

        # The radius of this disk. Value between 0 and 8 (inclusive).
        field("radius")["min_inclusive"] = 0 # defaults to 2
        field("radius")["max_inclusive"] = 0 # defaults to 6

        pack[registry]["minecraft:disk_sand"] = patched
