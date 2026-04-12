from beet import Context, DataPack
from beet.contrib.vanilla import Vanilla
from beet.contrib.worldgen import WorldgenConfiguredFeature


def beet_default(ctx: Context):
    source = get_source(ctx.inject(Vanilla), ctx.meta["base_version"])
    apply_patch(ctx.data, source, nested_radius=True)

    for directory, version in ctx.meta["overlay_versions"].items():
        overlay = ctx.data.overlays[directory]
        source = get_source(ctx.inject(Vanilla), version)
        apply_patch(overlay, source, nested_radius=False)


def get_source(vanilla: Vanilla, version: str):
    return vanilla.releases[version].mount("data").data[WorldgenConfiguredFeature]


def apply_patch(pack: DataPack, source, nested_radius: bool):
    patched = source["minecraft:disk_sand"].copy()
    config = patched.data["config"]

    # Half of the height of this disk. Value between 0 and 4 (inclusive).
    config["half_height"] = 0 # defaults to 2

    # The radius of this disk. Value between 0 and 8 (inclusive).
    radius = config["radius"]["value"] if nested_radius else config["radius"]
    radius["min_inclusive"] = 0 # defaults to 2
    radius["max_inclusive"] = 0 # defaults to 6

    pack[WorldgenConfiguredFeature]["minecraft:disk_sand"] = patched
