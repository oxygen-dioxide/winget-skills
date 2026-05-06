import os
import sys
import pathlib

#find path like manifests\*\*\*\* in the current directory
def find_manifest():
    current_dir = pathlib.Path(".")
    manifest_path = None

    for path in current_dir.rglob('manifests/*/*/*/*/*.yaml'):
        if path.is_file():
            manifest_path = path.parent
            break

    return manifest_path

if __name__ == "__main__":
    manifest_path = find_manifest()
    github_token = sys.argv[1]
    if manifest_path:
        print(f"Found manifest: {manifest_path}")
        os.system(f"wingetcreate submit {manifest_path} -t {github_token}")
    else:
        print("No manifest found.")