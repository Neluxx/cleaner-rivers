from beet import Context

from datapack_utils import FEATURE, Targets, provider, set_range, worldgen_config


def beet_default(ctx: Context):
    for target in ctx.inject(Targets):
        with target.patch(FEATURE, "minecraft:disk_clay") as disk:
            config = worldgen_config(disk)

            # Half of the height of this disk. Value between 0 and 4 (inclusive).
            config["half_height"] = 2  # defaults to 1

            # The radius of this disk. Value between 0 and 8 (inclusive).
            set_range(provider(config, "radius"), 2, 5)  # defaults to 2..3