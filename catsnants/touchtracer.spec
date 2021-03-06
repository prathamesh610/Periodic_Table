# -*- mode: python ; coding: utf-8 -*-
import webbrowser
import time
from kivy_deps import sdl2, glew, gstreamer

block_cipher = None


a = Analysis(['catsnants.py'],
             pathex=['D:\\KivyApp\\Periodic_Table\\catsnants'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='touchtracer',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,  Tree('D:\\KivyApp\\Periodic_Table\\catsnants'),
               a.binaries,
               a.zipfiles,
               a.datas,
               *[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins + gstreamer.dep_bins)],
               strip=False,
               upx=True,
               upx_exclude=[],
               name='touchtracer')
