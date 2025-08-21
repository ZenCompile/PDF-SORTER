import os
import shutil
from datetime import datetime

# THIS IS THE PARENT FOLDERPATH FOR EACH CLIENT, WHICH CHANGES BASED OFF EACH CLIENT
ROOT_FOLDER = r"C:/example/path"

# CLIENTS TO ITERATE THROUGH 
CLIENTS = ["CLIENT1Dir", "CLIENT2Dir", "CLIENT3Dir", "CLIENT4Dir", "CLIENT5Dir"]

# WHICH DIRECTORY TO MOVE FILES TO BASED ON THE KEYWORD IT CONTAINS
# Example: a file containing "invoice" in the name goes to the "Invoices" folder.
DEST_RULES = {
    "invoice": "invoices",
    "report": "reports",
    "contract": "contracts",
    "receipt": "receipts"
}

class ClientSorter:
    def __init__(self, client_name, base_path, rules):
        self.client_name = client_name
        self.base_path = base_path
        self.rules = rules
        self.source_folder = base_path

    # MAIN HANDLER TO SORT FILES
    def sort_pdfs(self):
        if not os.path.exists(self.source_folder):
            print(f"[WARNING] Skipped {self.client_name}: folder not found at {self.source_folder}")
            return
        
        date_folder = datetime.now().strftime("%m-%d-%y")
        date_folder_path = os.path.join(self.base_path, date_folder)
        os.makedirs(date_folder_path, exist_ok=True)

        for file in os.listdir(self.source_folder):
            if file.lower().endswith(".pdf"):
                # Backup copy to date folder
                shutil.copy2(
                    os.path.join(self.source_folder, file),
                    os.path.join(date_folder_path, file)
                )

                # Move file to sorted folder
                dest_folder = self.get_destination(file)
                os.makedirs(dest_folder, exist_ok=True)
                shutil.move(
                    os.path.join(self.source_folder, file),
                    os.path.join(dest_folder, file)
                )
                print(f"[OK] {self.client_name}: '{file}' moved to '{os.path.basename(dest_folder)}'")

    # IF THERE'S NO DEST_RULE KEY, IT MOVES THE FILE INTO "MISC"
    def get_destination(self, filename):
        for keyword, folder in self.rules.items():
            if keyword.lower() in filename.lower():
                return os.path.join(self.base_path, folder)
        print(f"[INFO] {self.client_name}: '{filename}' did not match any rule, moved to 'MISC'")
        return os.path.join(self.base_path, "MISC")
    
for client in CLIENTS:
    client_path = os.path.join(ROOT_FOLDER, client)
    sorter = ClientSorter(client, client_path, DEST_RULES)
    sorter.sort_pdfs()