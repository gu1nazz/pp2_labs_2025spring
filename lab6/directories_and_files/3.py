import os

def check_path(path):
    if os.path.exists(path):
        print("\n✅ Path exists!")
        print("📄 File name:", os.path.basename(path))
        print("📁 Directory name:", os.path.dirname(path))
    else:
        print("\n❌ Path does not exist.")

# 🔹 Пайдаланушыдан жол сұраймыз
user_path = input("📥 Enter the full path: ")
check_path(user_path)

#/Users/kassymgulnaz/Documents/attachment.pdf