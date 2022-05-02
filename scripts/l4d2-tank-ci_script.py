##################################################################
# Game   : L4D2
# Map    : Tanks Playground
# File   : Continuous Integration Script 
# Lang   : Python 2
# Author : obez
##################################################################
import hashlib
import subprocess
import shutil
import datetime
import os
import sys

fastcompile = False

for arg in sys.argv:
  if arg == '-fast':
    fastcompile = True

maps = [
  'l4d2_tanksplayground',
  'l4d2_tanksplayground_night',
  'l4d2_tanksplayground_surv_2_8'
]

TODAY = datetime.datetime.now().strftime('%Y-%m-%d_%H%M')
WORK_PATH = '' # Working directory, typically this repository (ex: c:\\dev\\maps\\l4d2-tanks-playground\\)
TMP_PATH = WORK_PATH + 'tmp'
SRC_PATH = WORK_PATH + 'src\\'
SCRIPT_PATH = WORK_PATH + 'scripts\\'
VPK_NAME = 'l4d2_tanksplayground'
VPK_PATH = SRC_PATH + 'vpk\\' + VPK_NAME + '\\'
VMF_PATH = SRC_PATH + 'vmf\\'
L4D2_DIR = '' # Path to the Steam L4D2 installation directory (ex: c:\\steam\\steamapps\\common\\left 4 dead 2\\)
GAME_DIR = L4D2_DIR + 'left4dead2\\'
GAME_BIN_DIR = L4D2_DIR + 'bin\\'
GAME_ADDONS_DIR = GAME_DIR + 'addons\\'
GAME_MAPS_DIR = GAME_DIR + 'maps\\'
GAME_EXE = L4D2_DIR + 'left4dead2.exe'
FTP_DIR = WORK_PATH + 'ftp\\'
ARCH_DIR = FTP_DIR + 'archives\\'
RAR_BIN = '' # Path to WinRAR binary/exe (ex: c:\\Program Files\\WinRAR\\Rar.exe)

# FUNCTIONS -------------------------------------------------------------------
def get_vmf_path(mapname):
  return VMF_PATH + mapname + '.vmf'

def get_bsp_path(mapname):
  return VMF_PATH + mapname + '.bsp'

def get_md5_path(mapname):
  return VMF_PATH + mapname + '.md5'

def ftp_log(msg):
  flog = open(FTP_DIR + 'compile.log', 'a')
  flog.write(TODAY + ' - ' + msg)
  flog.close()

def map_has_changed(mapname):
  m = hashlib.new('md5')
  f = open(get_vmf_path(mapname), 'rb')
  m.update(f.read())
  f.close()
  newmd5 = m.hexdigest()

  if os.path.exists(get_md5_path(mapname)):
    fmd5 = open(get_md5_path(mapname), 'r')
    oldmd5 = fmd5.read()
    fmd5.close()

    if oldmd5 == newmd5:
      ftp_log("Map " + mapname + " hasn't changed\n")
      return False

  fmd5 = open(get_md5_path(mapname), 'w')
  fmd5.write(newmd5)
  fmd5.close()
  return True

def compile_map(mapname, fast):
  visoptions = [GAME_BIN_DIR + 'vvis.exe']
  radoptions = [GAME_BIN_DIR + 'vrad.exe']

  if fast:
    visoptions.append('-fast')
    radoptions.append('-fast')
  else:
    radoptions.append('-both')
    radoptions.append('-final')

  visoptions.append('-game')
  visoptions.append(GAME_DIR)
  visoptions.append(get_bsp_path(mapname))

  radoptions.append('-StaticPropPolys')
  radoptions.append('-TextureShadows')
  radoptions.append('-game')
  radoptions.append(GAME_DIR)
  radoptions.append(get_bsp_path(mapname))

  subprocess.call([GAME_BIN_DIR + 'vbsp.exe', '-game', GAME_DIR, get_vmf_path(mapname)])
  subprocess.call(visoptions)
  subprocess.call(radoptions)

  ftp_log("New compile " + mapname + " OK\n")

def copy_to_vpk(mapname):
  shutil.copy(get_bsp_path(mapname), VPK_PATH + '\\maps\\')
  
def build_dictionary_and_cubemaps(mapname):
  if os.path.exists(GAME_ADDONS_DIR + VPK_NAME + '.vpk'):
    os.remove(GAME_ADDONS_DIR + VPK_NAME + '.vpk')

  shutil.copy(get_bsp_path(mapname), GAME_MAPS_DIR)
  subprocess.call([GAME_EXE, '-novid', '-buildcubemaps', '+map ' + mapname])
  shutil.move(GAME_MAPS_DIR + mapname + '.bsp', get_bsp_path(mapname))

# MAIN ------------------------------------------------------------------------
one_map_has_changed = False

for mapname in maps:
  if map_has_changed(mapname):
    one_map_has_changed = True
    compile_map(mapname, fastcompile)
    build_dictionary_and_cubemaps(mapname)
    copy_to_vpk(mapname)

if one_map_has_changed:
  # Archive old VPK version
  for oldf in os.listdir(FTP_DIR):
    if oldf.startswith(VPK_NAME):
      shutil.move(os.path.join(FTP_DIR, oldf), ARCH_DIR)

  # Build VPK
  subprocess.call([GAME_BIN_DIR + 'vpk.exe', VPK_PATH])
  os.rename(VPK_PATH + '.vpk', VPK_PATH + VPK_NAME + '.vpk')

  # Compress VPK to RAR
  # a=add, -df=delete file, -m5=best compression, -ep=no directories
  subprocess.call([RAR_BIN, 'a', '-df', '-m5', '-ep', FTP_DIR + VPK_NAME + '-' + TODAY + '.rar', VPK_PATH + VPK_NAME + '.vpk'])

exit()
