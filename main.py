import os
import shutil

# List of folders/files to clean
folders_to_clean = [
    r"%TEMP%",
    r"%APPDATA%\Local\Temp",
    r"C:\Windows\Temp",
    r"C:\Windows\SoftwareDistribution\Download",
    r"C:\Windows\Prefetch",
    r"C:\Windows\Logs",
    r"C:\Windows\Memory.dmp"  # <- esse é arquivo, não pasta
]

# Expand environment variables
folders_to_clean = [os.path.expandvars(path) for path in folders_to_clean]

for path in folders_to_clean:
    if os.path.exists(path):
        if os.path.isdir(path):
            # Se for pasta, limpa conteúdo
            for filename in os.listdir(path):
                filepath = os.path.join(path, filename)
                try:
                    if os.path.isdir(filepath):
                        shutil.rmtree(filepath)
                    else:
                        os.remove(filepath)
                except PermissionError:
                    print(f"Unable to delete {filepath} (in use).")
            print(f"{path} was cleaned.")
        else:
            # Se for arquivo, tenta remover direto
            try:
                os.remove(path)
                print(f"File {path} was deleted.")
            except PermissionError:
                print(f"Unable to delete file {path} (in use).")
    else:
        print(f"{path} does not exist.")

print("Done!")
