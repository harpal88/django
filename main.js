const { app, BrowserWindow } = require('electron');

function createWindow() {
    const win = new BrowserWindow({
        width: 800,
        height: 600,
        webPreferences: {
            nodeIntegration: true,
        },
    });

    win.loadURL('http://127.0.0.1:8000/'); // Point to Django app
}

app.on('ready', createWindow);
