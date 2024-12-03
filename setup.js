import { readToken, delay } from "./utils/file.js";
import { showBanner } from "./utils/banner.js";
import { loginFromFile } from "./utils/login.js";
import { createProviders } from "./utils/providers.js";
import { logger } from "./utils/logger.js";

async function setup() {
    showBanner();
    const isLogin = await loginFromFile('accounts.txt');
    if (!isLogin) {
        logger("No accounts were successfully logged in. Exiting...", "", "error");
        return; 
    }

    const numProv = 100; // Arbitrarily chosen maximum
    logger(`Creating ${numProv} Providers...`);
    await createProviders(numProv);
}

setup();
