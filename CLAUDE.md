# File Inventory Project

## What this is
A simple Python script that inventories the contents of a folder — counts files, folders, total size, and breaks down files by extension.

## How to use it

```
source venv/bin/activate
python3 inventory.py <folder_path>
```

## Current capabilities
- Counts files and folders in the given directory
- Reports total size in bytes
- Groups files by extension
- [Add the feature you implemented in Day 7]

## Conventions
- Python 3, virtual environment in `venv/`
- Standard library only (no external packages yet)
- Code style: simple and readable, no clever tricks

## Things to know if extending this
- Currently only inspects the top level, not recursive [or update if you did Option A]
- No error handling for permission-denied folders yet
- Could be a future home for a small CLI tool with more commands

