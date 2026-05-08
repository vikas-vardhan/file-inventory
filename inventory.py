import os
import sys

def inventory_folder(folder_path):
	if not os.path.isdir(folder_path):
		print(f"Error: '{folder_path}' is not a valid folder.")
		return

	file_count = 0
	folder_count = 0
	total_size = 0
	extensions = {}

	for dirpath, dirnames, filenames in os.walk(folder_path):
		if dirpath != folder_path:
			folder_count += 1
		for filename in filenames:
			full_path = os.path.join(dirpath, filename)
			file_count += 1
			total_size += os.path.getsize(full_path)
			ext = os.path.splitext(filename)[1].lower()
			if ext == "":
				ext = "(no extension)"
			extensions[ext] = extensions.get(ext, 0) + 1

	print(f"\nInventory of: {folder_path} (including subfolders)")
	print(f"Files: {file_count}")
	print(f"Folders: {folder_count}")
	print(f"Total size: {total_size:,} bytes")
	print(f"\nFiles by extension:")
	for ext, count in sorted(extensions.items()):
		print(f" {ext}: {count}")

if __name__ == "__main__":
	if len(sys.argv) < 2:
		print("Usage: python3 inventory.py <folder_path>")
		sys.exit(1)
	inventory_folder(sys.argv[1])
