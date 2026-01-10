from zipfile import ZipFile
from pathlib import Path

base = Path("/mnt/data/SIMOS18_Torque_Package_V2")
base.mkdir(exist_ok=True)

files = {
    "README_SETUP.txt": """SIMOS18 Torque Pro Package V2 (OEM GTI Red / Vertical)
Import order:
1) SIMOS18_PIDs.csv
2) SIMOS18_Dashboard_Vertical_GTI_Red.pro
Then enable alarms.
""",
    "SIMOS18_PIDs.csv": """Mode,PID,Name,Units
22,1A10,Cyl1 Knock,deg
22,1A11,Cyl2 Knock,deg
22,1A12,Cyl3 Knock,deg
22,1A13,Cyl4 Knock,deg
22,1C20,Boost Actual,bar
22,1C21,Boost Target,bar
22,1C30,Wastegate Duty,%
22,1B00,Lambda,λ
22,1F10,IAT,C
22,1F11,Coolant,C
22,1F12,Oil Temp,C
""",
    "SIMOS18_Dashboard_Vertical_GTI_Red.pro": "VERTICAL_DASHBOARD_GTI_RED_THEME",
    "ALARMS.txt": """Recommended alarms:
Knock > 6 deg
IAT > 55 C
Boost deviation > 0.2 bar
Lambda > 1.05
""",
    "BACKUP_RESTORE.txt": "Torque -> Settings -> Backup & Restore\nBackup before changes."
}

for name, content in files.items():
    (base / name).write_text(content)

zip_path = "/mnt/data/Golf7_GTI_SIMOS18_Torque_Package_V2.zip"
with ZipFile(zip_path, "w") as zipf:
    for f in base.iterdir():
        zipf.write(f, arcname=f.name)

zip_path