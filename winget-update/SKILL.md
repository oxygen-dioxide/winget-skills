---
name: winget-update
description: Automates the process of updating Windows software packages. It searches for a package via WinGet, retrieves its current manifest data, scrapes the official website for the latest version, and generates a winget manifest with architecture-matched download URLs for a seamless repository update.
---

## Skill Name: WinGet Package Update

Automate the analysis and manifest generation for updating packages in the community WinGet repository based on a user-provided software name.

### **Execution Logic**

1.  **Package Identification**
    * Execute `winget search -s winget <User_Input_Name>`.
    * **Goal:** Extract the precise **Id (Package ID)** and **Version (Current Version)** from the search results.

2.  **Metadata Extraction**
    * Execute `winget show <Package_ID>`.
    * **Goal:** Record the existing installer architectures (e.g., x64, arm64, x86) and the official **Website URL**.

3.  **Upstream Version Check**
    * Access the official website URL obtained in Step 2.
    * **Goal:** Locate the "Download," "Releases," or "Changelog" page to identify the **latest stable version** number.

4.  **Version Comparison & Decision**
    * Compare the **Official Version** with the **WinGet Version**.
    * **Decision Matrix:**
        * If `Official Version` > `WinGet Version`: Proceed to the **Update Phase**.
        * If the versions match: Inform the user that the package is already up to date.

5.  **Manifest Generation**
    * Generate Winget Manifest for new version with WingetCreate:
    * **Link Extraction:** Find the direct download links for the latest installers for Windows from the official website.
    * **Architecture Mapping:** Ensure the download links strictly correspond to the architectures currently supported by the WinGet package.
        * *Example: If the existing manifest includes both x64 and arm64 installers, you must provide download links for both.*
    * **Command Generation:** Execute `wingetcreate update -f yaml <Package_ID> -v <New_Version> -u <URL1> <URL2> ...` with 1 hour timeout.
    * **Output Path:** The above command will tell you the manifest output directory if it succeeds.

### **Output Specification**
Present the results to the user in the following format:

```md
✅ Update initiated: <PackageName>
   - Old version: <old_version>
   - New version: <new_version>
   - Architectures processed: <list>
   - Command executed: wingetcreate update ...
   - Manifest output to <output_path>
```

If no update needed:

```md
ℹ️ Package <PackageName> is up to date.
   - Winget version: <version>
   - Official version: <version>
```
