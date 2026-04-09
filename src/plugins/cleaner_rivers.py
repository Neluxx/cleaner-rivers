from beet import Context, DataPack
from beet.contrib.vanilla import Vanilla
from beet.contrib.worldgen import WorldgenConfiguredFeature

DISK_SAND = "minecraft:disk_sand"
DISK_GRAVEL = "minecraft:disk_gravel"


def beet_default(ctx: Context):
    config = ctx.meta["cleaner_rivers"]
    vanilla = ctx.inject(Vanilla)

    _patch(ctx.data, vanilla, config["base_version"], DISK_SAND)
    _patch(ctx.data, vanilla, config["base_version"], DISK_GRAVEL)

    for directory, version in config["overlay_versions"].items():
        overlay = ctx.data.overlays[directory]
        _patch_overlay(overlay, vanilla, version, DISK_SAND)
        _patch_overlay(overlay, vanilla, version, DISK_GRAVEL)


def _patch(pack: DataPack, vanilla: Vanilla, version: str, feature: str):
    source = vanilla.releases[version].mount("data").data[WorldgenConfiguredFeature][feature]
    patched = source.copy()
    patched.data["config"]["half_height"] = 0
    patched.data["config"]["radius"]["min_inclusive"] = 0
    patched.data["config"]["radius"]["max_inclusive"] = 0
    pack[WorldgenConfiguredFeature][feature] = patched


def _patch_overlay(pack: DataPack, vanilla: Vanilla, version: str, feature: str):
    source = vanilla.releases[version].mount("data").data[WorldgenConfiguredFeature][feature]
    patched = source.copy()
    patched.data["config"]["half_height"] = 0
    patched.data["config"]["radius"]["value"]["min_inclusive"] = 0
    patched.data["config"]["radius"]["value"]["max_inclusive"] = 0
    pack[WorldgenConfiguredFeature][feature] = patched