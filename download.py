import subprocess
import sys
# Check for flag --export
EXPORT_FLAG=False
if "--export" in sys.argv:
    EXPORT_FLAG=True
url=sys.argv[1]
tdf=f"npx dl-librescore@latest -i {url} -t midi -o C:\\Users\\river\\USACOTESTS\\tmp"
subprocess.run(tdf, shell=True)
# store name of midi (in tmp folder)
import os
tfiles=os.listdir("C:\\Users\\river\\USACOTESTS\\tmp")
midi_file=str(tfiles[0])
import shutil
shutil.copy(f"C:\\Users\\river\\USACOTESTS\\tmp\\{midi_file}", f"C:\\Users\\river\\USACOTESTS\\midis\\{midi_file}")
os.remove(f"C:\\Users\\river\\USACOTESTS\\tmp\\{midi_file}")
# launch new process with this (nushell syntax)
# `C:\Downloads\Pianoteq 9\Pianoteq 9.exe` --preset "NY Steinway Model D" --midi MIDI_PATH --play
cmdp=[r"C:\Downloads\Pianoteq 9\Pianoteq 9.exe", "--preset", "NY Steinway Model D", "--midi", f"C:\\Users\\river\\USACOTESTS\\midis\\{midi_file}"]
if not EXPORT_FLAG:
    cmdp.append("--headless")
    cmdp.append("--play-and-quit")
else:
    cmdp.append("--play")
subprocess.run(cmdp)
