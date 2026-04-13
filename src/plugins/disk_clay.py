from beet import Context
from beet.contrib.vanilla import Vanilla
from beet.contrib.worldgen import WorldgenConfiguredFeature

from src.plugins.utils import iterate_versions, field_accessor


def beet_default(ctx: Context):
    vanilla = ctx.inject(Vanilla)

    for pack, version in iterate_versions(ctx):
        source = vanilla.releases[version].mount("data").data[WorldgenConfiguredFeature]
        patched = source["minecraft:disk_clay"].copy()
        config = patched.data["config"]
        field = field_accessor(config, version)

        # Half of the height of this disk. Value between 0 and 4 (inclusive).
        config["half_height"] = 2 # defaults to 1

        # The radius of this disk. Value between 0 and 8 (inclusive).
        field("radius")["min_inclusive"] = 2 # defaults to 2
        field("radius")["max_inclusive"] = 5 # defaults to 3

        pack[WorldgenConfiguredFeature]["minecraft:disk_clay"] = patched
