const { app, BrowserWindow } = require('electron');

let mainWindow;

function createWindow() {
    mainWindow = new BrowserWindow({
        frame: true, // No default OS frame
        resizable: false, // Prevent user resizing
        alwaysOnTop: true, // Keeps the assistant window on top
        webPreferences: {
            nodeIntegration: true,
            contextIsolation: false,
        },
    });

    // Load the assistant's HTML file
    mainWindow.loadFile('index.html');

    // Resize to fit content after the page has loaded
    mainWindow.webContents.once('did-finish-load', () => {
        mainWindow.setSize(400, 500); // Set size to match your content
    });

    mainWindow.on('closed', () => {
        mainWindow = null;
    });
}

// Electron lifecycle hooks
app.on('ready', createWindow);
app.on('window-all-closed', () => {
    if (process.platform !== 'darwin') {
        app.quit();
    }
});
app.on('activate', () => {
    if (BrowserWindow.getAllWindows().length === 0) {
        createWindow();
    }
});
