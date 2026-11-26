from dataclasses import dataclass

from beet import Context

from beet_datapack_utils import FEATURE, get_config, set_uniform, versioned_packs


@dataclass(frozen=True)
class Disk:
    # Half of the height of the disk. Value between 0 and 4 (inclusive).
    half_height: int
    # The radius of the disk. Values between 0 and 8 (inclusive).
    min_radius: int
    max_radius: int


# Vanilla default for all three: half_height 1, radius 2..3.
DISKS: dict[str, Disk] = {
    "minecraft:disk_clay": Disk(half_height=2, min_radius=2, max_radius=5),
    "minecraft:disk_sand": Disk(half_height=0, min_radius=0, max_radius=0),
    "minecraft:disk_gravel": Disk(half_height=0, min_radius=0, max_radius=0),
}


def beet_default(ctx: Context):
    for pack in versioned_packs(ctx):
        for name, disk in DISKS.items():
            with pack.edit(FEATURE, name) as feature:
                config = get_config(feature)
                config["half_height"] = disk.half_height
                set_uniform(config, "radius", disk.min_radius, disk.max_radius)