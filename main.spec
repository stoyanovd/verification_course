# -*- mode: python -*-

block_cipher = None

a = Analysis(['src/main.py'],
             pathex=['/home/dima/work/verification_course/python'],
             binaries=[
                 # ('ltl2ba/ltl2ba', 'ltl2ba/ltl2ba')
                 # , ('dot', 'dot')
             ],
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
          name='verifier',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True)
