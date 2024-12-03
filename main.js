import { readToken, delay } from "./utils/file.js";
import { createConnection } from "./utils/websocket.js";
import { showBanner } from "./utils/banner.js";

async function start() {
    showBanner()
    const tokens = await readToken("providers.txt");

    // Create connections without proxies
    for (let i = 0; i < tokens.length; i++) {
        const token = tokens[i];

        await createConnection(token);
        await delay(0);
    }
}

start();
