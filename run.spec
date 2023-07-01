# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['C:\\Users\\27par\\Desktop\\Github Repos\\Medical-Office-Administration/run.py'],
    pathex=['C:\\Users\\27par\\Desktop\\Github Repos\\Medical-Office-Administration'],
    binaries=[],
    datas=[('C:\\Users\\27par\\Desktop\\Github Repos\\Medical-Office-Administration/backend', 'backend/'), ('C:\\Users\\27par\\Desktop\\Github Repos\\Medical-Office-Administration/frontend', 'frontend/')],
    hiddenimports=['greenlet', 'pyodbc', 'PyQt5', 'PyQt5-Qt5', 'PyQt5-sip', 'SQLAlchemy', 'typing_extensions'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=True,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [('v', None, 'OPTION')],
    exclude_binaries=True,
    name='run',
    debug=True,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='run',
)
