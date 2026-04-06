const tt3404 = require('../wasm/tt3404.js');
const fs = require('fs');
const path = require('path');

async function testMetadata() {
    try {
        const wasmPath = path.resolve(__dirname, '../wasm/tt3404.wasm');
        const wasmBinary = fs.readFileSync(wasmPath);

        const module = await tt3404({
            wasmBinary: wasmBinary
        });
        const project = new module.ProjectWasm();

        const description = project.get_description();
        const infoLink = project.get_info_link();
        const repoLink = project.get_repo_link();

        console.log(`METADATA_START`);
        console.log(`DESCRIPTION:${description}`);
        console.log(`INFO_LINK:${infoLink}`);
        console.log(`REPO_LINK:${repoLink}`);
        console.log(`METADATA_END`);

        project.delete();
    } catch (error) {
        console.error('Test failed:', error);
        process.exit(1);
    }
}

testMetadata();
