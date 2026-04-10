from beet import Context, DataPack
from beet.contrib.vanilla import Vanilla
from beet.contrib.worldgen import WorldgenConfiguredFeature

FEATURES = [
    "minecraft:disk_sand",
    "minecraft:disk_gravel",
]


def beet_default(ctx: Context):
    base_version = ctx.meta["base_version"]
    overlay_versions = ctx.meta["overlay_versions"]
    vanilla = ctx.inject(Vanilla)

    for feature in FEATURES:
        source = get_source(vanilla, base_version)
        apply_patch(ctx.data, source, feature, nested_radius=True)

    for directory, version in overlay_versions.items():
        overlay = ctx.data.overlays[directory]
        source = get_source(vanilla, version)
        for feature in FEATURES:
            apply_patch(overlay, source, feature, nested_radius=False)


def get_source(vanilla: Vanilla, version: str):
    return vanilla.releases[version].mount("data").data[WorldgenConfiguredFeature]


def apply_patch(pack: DataPack, source, feature: str, nested_radius: bool):
    patched = source[feature].copy()
    config = patched.data["config"]
    config["half_height"] = 0
    radius = config["radius"]["value"] if nested_radius else config["radius"]
    radius["min_inclusive"] = 0
    radius["max_inclusive"] = 0
    pack[WorldgenConfiguredFeature][feature] = patched
