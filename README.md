# PDF File Sorter

This script helps keep things tidy by automatically organizing PDF files into the right folders for each client. It also creates a dated backup of everything and moves any files that don’t match a rule into a “MISC” folder.

---

## Features
- Sorts PDF files into client-specific folders.  
- Creates a date-stamped backup of every PDF.  
- Uses keyword rules to decide which folder a file goes into.  
- Unmatched files are placed into a `MISC` folder automatically.  
- Easy to customize for your own clients and rules.  
- Uses only Python’s standard library (no installs needed).  

---

## How It Works
1. Define your **parent folder** (`ROOT_FOLDER`).  
2. Add the **client folder names** to the `CLIENTS` list.  
3. Set up **sorting rules** in `DEST_RULES` (`keyword -> destination folder`).  
4. Run the script. PDFs are copied into a backup folder (with today’s date) and then sorted into the correct folders.  

---

## Example Rules
```python
DEST_RULES = {
    "invoice": "invoices",
    "report": "reports",
    "contract": "contracts",
    "receipt": "receipts"
}
