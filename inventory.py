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
	
	for entry in os.listdir(folder_path):
		full_path = os.path.join(folder_path, entry)
		if os.path.isfile(full_path):
			file_count += 1
			total_size += os.path.getsize(full_path)
			ext = os.path.splitext(entry)[1].lower()
			if ext == "":
				ext = "(no extension)"
			extensions[ext] = extensions.get(ext, 0) + 1
		elif os.path.isdir(full_path):
			folder_count += 1

	print(f"\nInventory of: {folder_path}")
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
