#!/usr/bin/env python3
import os
import json
import subprocess
from pathlib import Path
from datetime import datetime

PIRATE = "\U0001F3F4\u200d\u2620\ufe0f"
EYE = "\U0001F441\ufe0f"
SHIELD = "\U0001F6E1\ufe0f"
OK = "\u2705"
WARN = "\u26A0\ufe0f"

HOME = Path.home()
ROOT = Path(__file__).resolve().parents[1]
REPORTS = ROOT / "reports"
REPORTS.mkdir(exist_ok=True)

STAMP = datetime.now().strftime("%Y%m%d_%H%M%S")
OUT = REPORTS / f"big_brother_detectors_{STAMP}.txt"

TRUSTED_CLOUD_MOUNTS = {
    "GoogleDrive-design.kejstudio@gmail.com",
    "GoogleDrive-design.jk.marchand@gmail.com",
    "GoogleDrive-designorchard.kyle@gmail.com",
    "GoogleDrive-drjkmarchand@gmail.com",
    "GoogleDrive-Kyle@drmarchandslaboratory.com",
    "Dropbox-Kejstudio",
    "Dropbox-Personal",
    "OneDrive-drmarchands com",
    "OneDrive-drmarchandscom",
    "OneDrive-Personal",
}

SUSPICIOUS_NAMES = [
    ".env",
    "token",
    "secret",
    "service_account.json",
    ".pem",
    ".key",
    "credentials",
    "password",
]

def run(cmd):
    try:
        return subprocess.check_output(cmd, shell=True, text=True, stderr=subprocess.STDOUT).strip()
    except subprocess.CalledProcessError as e:
        return e.output.strip()

def line(msg=""):
    print(msg)

def detector_cloud_mounts():
    line(f"\n{EYE} === CLOUD ACCOUNT DETECTOR ===")
    cloud = HOME / "Library/CloudStorage"
    if not cloud.exists():
        line(f"{WARN} CloudStorage path missing")
        return

    found = [p.name for p in cloud.iterdir() if p.is_dir()]
    for name in sorted(found):
        if name in TRUSTED_CLOUD_MOUNTS:
            line(f"{OK} trusted_mount: {name}")
        else:
            line(f"{PIRATE} unknown_cloud_mount: {name}")

def detector_google_accounts():
    line(f"\n{EYE} === GOOGLE ACCOUNT DETECTOR ===")
    cloud = HOME / "Library/CloudStorage"
    if not cloud.exists():
        return
    for p in sorted(cloud.glob("GoogleDrive-*")):
        name = p.name
        if name in TRUSTED_CLOUD_MOUNTS:
            line(f"{OK} trusted_google_account: {name}")
        else:
            line(f"{PIRATE} unregistered_google_account: {name}")

def detector_secret_filenames():
    line(f"\n{SHIELD} === SECRET FILENAME DETECTOR ===")
    hits = []
    for base in [ROOT, HOME / "Developer", HOME / "Downloads", HOME / "Desktop"]:
        if not base.exists():
            continue
        for p in base.rglob("*"):
            if not p.is_file():
                continue
            s = str(p).lower()
            if any(x.lower() in s for x in SUSPICIOUS_NAMES):
                if "node_modules" not in s and ".git" not in s:
                    hits.append(p)
    if not hits:
        line(f"{OK} no obvious secret filenames found in scanned zones")
    else:
        for p in hits[:100]:
            line(f"{PIRATE} possible_secret_file: {p}")

def detector_git_state():
    line(f"\n{EYE} === GIT DETECTOR ===")
    line(run("git status --short"))
    remotes = run("git remote -v")
    line(remotes if remotes else f"{WARN} no git remote found")

def detector_ssh():
    line(f"\n{SHIELD} === SSH DETECTOR ===")
    ssh = HOME / ".ssh"
    if not ssh.exists():
        line(f"{WARN} no ~/.ssh directory")
        return
    for p in sorted(ssh.iterdir()):
        if p.is_file():
            mode = oct(p.stat().st_mode)[-3:]
            label = f"{p.name} mode={mode}"
            if p.name.endswith(".pub") or p.name in {"known_hosts", "config"}:
                line(f"{OK} ssh_file: {label}")
            else:
                line(f"{PIRATE} sensitive_ssh_file_present: {label}")

def detector_disk_pressure():
    line(f"\n{EYE} === DISK PRESSURE DETECTOR ===")
    out = run('df -h "$HOME" | tail -1')
    line(out)
    parts = out.split()
    if len(parts) >= 5:
        cap = parts[4]
        try:
            pct = int(cap.replace("%", ""))
            if pct >= 95:
                line(f"{PIRATE} disk_pressure_high: {cap}")
            elif pct >= 85:
                line(f"{WARN} disk_pressure_moderate: {cap}")
            else:
                line(f"{OK} disk_pressure_ok: {cap}")
        except ValueError:
            pass

def main():
    with OUT.open("w") as f:
        import sys
        old = sys.stdout
        sys.stdout = f
        line("==================================================")
        line(f"{EYE} BIG BROTHER DETECTOR REPORT {EYE}")
        line(f"Generated: {datetime.now().isoformat()}")
        line(f"Mode: READ ONLY")
        line("==================================================")
        detector_disk_pressure()
        detector_cloud_mounts()
        detector_google_accounts()
        detector_secret_filenames()
        detector_git_state()
        detector_ssh()
        line("\n==================================================")
        line(f"REPORT: {OUT}")
        line("==================================================")
        sys.stdout = old

    print(OUT.read_text())

if __name__ == "__main__":
    main()
