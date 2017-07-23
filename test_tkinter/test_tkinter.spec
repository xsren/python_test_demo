# -*- mode: python -*-

block_cipher = None


a = Analysis(['test_tkinter.py'],
             pathex=['/Users/xsren/my_projects/python_test_demo/test_tkinter'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='test_tkinter',
          debug=False,
          strip=False,
          upx=True,
          console=True )
