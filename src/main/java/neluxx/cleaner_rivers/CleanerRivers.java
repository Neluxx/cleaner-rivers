package neluxx.cleaner_rivers;

import net.fabricmc.api.ModInitializer;
import net.fabricmc.fabric.api.resource.ResourceManagerHelper;
import net.fabricmc.fabric.api.resource.ResourcePackActivationType;
import net.fabricmc.loader.api.FabricLoader;
import net.minecraft.util.Identifier;

public class CleanerRivers implements ModInitializer {
	public static final String MOD_ID = "cleaner-rivers";

	@Override
	public void onInitialize() {
        // Register the datapack
        ResourceManagerHelper.registerBuiltinResourcePack(
                Identifier.of(MOD_ID, "datapack"),
                FabricLoader.getInstance().getModContainer(MOD_ID).orElseThrow(),
                ResourcePackActivationType.ALWAYS_ENABLED
        );
	}
}