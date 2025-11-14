# Complete Guide: Publishing Your Systematic Review to GitHub

## 📝 Table of Contents

1. [Repository Description](#repository-description)
2. [Pre-Publication Preparation](#pre-publication-preparation)
3. [Creating the GitHub Repository](#creating-the-github-repository)
4. [Uploading Files](#uploading-files)
5. [Post-Publication Configuration](#post-publication-configuration)
6. [Final Verification](#final-verification)

---

## 📖 Repository Description

### Repository Name

```
cubesat-antenna-systematic-review
```

Alternatives:
```
systematic-review-cubesat-antennas
microstrip-antenna-cubesat-review
```

**Recommendation**: Use descriptive but concise names, lowercase, with hyphens.

### Short Description (for GitHub)

```
Systematic review (PRISMA 2020) of microstrip antenna design workflows for CubeSat platforms.
Analysis of 79 studies covering electromagnetic simulation, experimental validation, feeding
integration, and fabrication processes. Complete dataset with transparency and reproducibility.
```

**Characters**: ~280 (GitHub recommends <350)

### Detailed Description (for README and About)

```markdown
# Systematic Review: Microstrip Antenna Design for CubeSat Platforms

**Complete dataset** from a systematic review examining empirical workflow configurations
in antenna design for small satellites.

## 🔬 Scope

- **Protocol**: PRISMA 2020
- **Records processed**: 551 (4 databases)
- **Studies included**: 79 articles
- **Period**: 2000-2025 (25 years)
- **Areas**: EM simulation, experimental validation, integration, fabrication

## 📊 Key Findings

- 85% simulation-measurement agreement (±1.5 dB)
- Critical gaps: 71% feeding-system integration, 86% thermal validation
- Dominant workflow configurations identified
- Inductive analysis of 4 specific objectives

## 🎯 Transparency & Reproducibility

All search data, PRISMA screening, analyses, and 79 PDFs included.
CC BY 4.0 license. Zenodo-ready.
```

### Tags/Topics for GitHub

```
systematic-review
cubesat
antenna-design
microstrip-antenna
prisma-2020
research-data
electromagnetic-simulation
nanosatellites
small-satellites
open-science
reproducible-research
hfss
cst-microwave-studio
antenna-engineering
aerospace
```

**Recommendation**: GitHub allows ~20 topics. Use the most relevant ones.

---

## 🔧 Pre-Publication Preparation

### Step 1: Complete Personal Information

#### A. Edit `.zenodo.json`

```json
{
  "creators": [
    {
      "name": "LastName, FirstName",
      "affiliation": "Your University",
      "orcid": "0000-0002-1234-5678"
    }
  ]
}
```

#### B. Edit `CITATION.cff`

```yaml
authors:
  - given-names: 'Your First Name'
    family-names: 'Your Last Name'
    email: 'your.email@university.edu'
    affiliation: 'Your University'
    orcid: 'https://orcid.org/0000-0002-1234-5678'
```

#### C. Edit `LICENSE`

Replace:
```
Copyright (c) 2025 [Authors Names]
```

With:
```
Copyright (c) 2025 FirstName LastName, FirstName2 LastName2
```

### Step 2: Clean Temporary Files

```powershell
# In PowerShell, from project folder:

# Check for temporary files
Get-ChildItem -Recurse -Include ~$* | Select-Object FullName

# Remove Excel temporary files
Get-ChildItem -Recurse -Include ~$* | Remove-Item -Force

# Verify they were removed
Get-ChildItem -Recurse -Include ~$*
```

### Step 3: Verify Repository Size

```powershell
# Get total size
Get-ChildItem -Recurse | Measure-Object -Property Length -Sum |
    Select-Object @{Name="Size(MB)";Expression={[math]::Round($_.Sum/1MB,2)}}
```

**GitHub Limits**:
- ⚠️ Individual files: Max 100 MB (warning at 50 MB)
- ⚠️ Total repository: Recommended <1 GB

**If you exceed**:
- Consider Git LFS for large PDFs
- Or publish them only on Zenodo

### Step 4: Decision About PDFs

The 79 PDFs in `articulosPDF/` are copyrighted by publishers.

**Option A: Include them** (Fair Use for research)
```bash
# Keep complete folder
git add articulosPDF/
```

**Option B: Don't include them** (Safer)
```bash
# Add to .gitignore
echo "articulosPDF/" >> .gitignore
```

**Option C: Only Open Access**
```bash
# Create list of which are OA first
# Then include only those
```

---

## 🚀 Creating the GitHub Repository

### Method 1: From the Web (Recommended for beginners)

#### Step 1: Go to GitHub

1. Go to https://github.com/
2. Sign in (or create account if you don't have one)
3. Click **"+" button** (top right) → **"New repository"**

#### Step 2: Configure Repository

**Basic information**:

```
Repository name: cubesat-antenna-systematic-review

Description: Systematic review (PRISMA 2020) of microstrip antenna
design workflows for CubeSat platforms. Complete dataset with 79
studies, covering EM simulation, experimental validation, and
fabrication processes.

Public ✅ (for free Zenodo)

[ ] Add a README file (DON'T check - we already have one)
[ ] Add .gitignore (DON'T check - we already have one)
[ ] Choose a license (DON'T check - we already have LICENSE)
```

#### Step 3: Create Repository

Click **"Create repository"**

You'll see a page with instructions. **Save this URL**:
```
https://github.com/[your-username]/cubesat-antenna-systematic-review
```

---

## 📤 Uploading Files

### Option A: Using GitHub Desktop (Easiest)

#### 1. Download GitHub Desktop

- Go to https://desktop.github.com/
- Download and install

#### 2. Configure

1. Open GitHub Desktop
2. Sign in with your GitHub account
3. File → Options → Git
   - Name: Your Name
   - Email: your@email.com

#### 3. Add Local Repository

1. File → **Add local repository**
2. Click **Choose** and navigate to: `G:\RevSisOrd\RevSisCubesatNov25`
3. Click **Add repository**

If it says "not a git repository":
1. Click **"create a repository"**
2. Leave everything as default
3. Click **Create repository**

#### 4. Make First Commit

1. You'll see list of files in "Changes"
2. In the field below:
   - Summary: `Initial commit: Complete systematic review dataset`
   - Description:
     ```
     - PRISMA 2020 protocol implementation
     - 79 studies included from 551 initial records
     - Complete data extraction and analysis
     - All documentation and metadata files
     - Ready for Zenodo publication
     ```
3. Click **Commit to main**

#### 5. Publish to GitHub

1. Click **Publish repository**
2. Verify:
   - Name: cubesat-antenna-systematic-review
   - Description: (should be there)
   - [ ] Keep this code private (DON'T check)
3. Click **Publish repository**

#### 6. Verify

Visit: `https://github.com/[your-username]/cubesat-antenna-systematic-review`

You should see all your files!

### Option B: Using Git Command Line

#### 1. Install Git

- Windows: https://git-scm.com/download/win
- During installation: select "Use Git from Windows Command Prompt"

#### 2. Configure Git

```bash
# Open PowerShell or Git Bash
cd "G:\RevSisOrd\RevSisCubesatNov25"

# Configure identity
git config --global user.name "Your Name"
git config --global user.email "your@email.com"
```

#### 3. Initialize Repository

```bash
# Initialize Git
git init

# Check status
git status
```

#### 4. Add Files

```bash
# Add all files
git add .

# Verify what was added
git status
```

If you want to **exclude** PDFs:
```bash
# First add to .gitignore
echo "articulosPDF/" >> .gitignore

# Then add everything
git add .
```

#### 5. Make the Commit

```bash
git commit -m "Initial commit: Complete systematic review dataset

- PRISMA 2020 protocol implementation
- 79 studies included from 551 initial records
- Complete data extraction and analysis
- All documentation and metadata files
- Ready for Zenodo publication"
```

#### 6. Connect with GitHub

```bash
# Change branch name to main (if necessary)
git branch -M main

# Connect with GitHub (replace [your-username])
git remote add origin https://github.com/[your-username]/cubesat-antenna-systematic-review.git

# Verify
git remote -v
```

#### 7. Upload to GitHub

```bash
# First time (with -u to set upstream)
git push -u origin main
```

It will ask for authentication:
- **Username**: your GitHub username
- **Password**: use **Personal Access Token** (not your password)

**Create Token**:
1. GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Generate new token
3. Select: `repo` (all)
4. Generate token
5. **Copy the token** (only shown once)

#### 8. Verify

```bash
# View history
git log --oneline

# View remote
git remote -v
```

Visit your repository on GitHub!

---

## ⚙️ Post-Publication Configuration

### 1. Configure Repository "About"

1. Go to your repository on GitHub
2. Click **⚙️ (gear icon)** next to "About"
3. Complete:

```
Description:
Systematic review (PRISMA 2020) of microstrip antenna design
workflows for CubeSat platforms. Analysis of 79 studies covering
electromagnetic simulation, experimental validation, feeding
integration, and fabrication processes.

Website: [URL of your institution or profile]

Topics:
systematic-review, cubesat, antenna-design, microstrip-antenna,
prisma-2020, research-data, electromagnetic-simulation,
nanosatellites, open-science, reproducible-research
```

4. Check:
   - ✅ Releases
   - ✅ Packages
   - ⬜ Deployments

5. Click **Save changes**

### 2. Enable Discussions (Optional but recommended)

1. Settings → General
2. Scroll to "Features"
3. ✅ Discussions
4. Click **Set up discussions**
5. Create categories:
   - 💬 General
   - 💡 Ideas
   - 🙏 Q&A
   - 🐛 Data Issues

### 3. Configure Issue Templates

1. Settings → General → Features
2. Issues → **Set up templates**
3. Add:
   - 🐛 Bug report (for data errors)
   - ✨ Feature request (for new analyses)
   - 📚 Study suggestion (for additional studies)

### 4. Create First Release (v1.0)

1. Code → Releases → **Create a new release**

2. Complete:

```
Tag version: v1.0
Release title: v1.0 - Complete Systematic Review Dataset

Description:
## 📊 First Release: Complete Systematic Review

This release contains the complete dataset and analysis from our
systematic review on microstrip antenna design workflows for
CubeSat platforms.

### 📈 Dataset Overview
- **551 records** processed (PRISMA 2020)
- **79 studies** included
- **4 specific objectives** analyzed
- **25 years** covered (2000-2025)

### 📁 Contents
- Complete PRISMA screening data
- Extracted data for all 79 studies
- Analysis by objective (OE1-OE4)
- Inductive cross-study analysis
- 79 included articles (PDF)
- Full documentation and metadata

### 🔑 Key Findings
- 85% simulation-measurement agreement (±1.5 dB)
- Critical integration gaps identified:
  - 71% feeding-system integration deficit
  - 86% thermal validation deficiency
  - 79% mechanical integration inadequacy

### 📖 Citation
See CITATION.cff for proper citation format.

### 📄 License
CC BY 4.0 - See LICENSE file

### 🚀 Zenodo
This release will be automatically archived in Zenodo with a DOI.

---
🤖 Generated with systematic methodology
📋 PRISMA 2020 compliant
```

3. **Attach files** (optional):
   - If you want separate ZIP from repo

4. Click **Publish release**

**IMPORTANT**: If you connected Zenodo, this will automatically create the deposit in Zenodo!

---

## 🔗 Connect with Zenodo (Optional but Recommended)

### Why connect:

- ✅ Automatic DOI for each release
- ✅ Permanent archive
- ✅ No additional effort
- ✅ Better for citations

### Steps:

1. Go to https://zenodo.org/
2. Log in (or Sign up)
3. Settings → GitHub → **Connect**
4. Authorize Zenodo
5. In the list, find your repository
6. **Toggle ON** the switch
7. Return to GitHub
8. Create/recreate release v1.0
9. Zenodo automatically creates the deposit!
10. Copy the DOI badge from Zenodo

### Add DOI Badge to README

Once you have the DOI:

```markdown
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.XXXXXXX.svg)](https://doi.org/10.5281/zenodo.XXXXXXX)
```

Edit README.md and replace:
```markdown
[![DOI](https://img.shields.io/badge/DOI-pending-blue)]()
```

With your actual Zenodo badge.

---

## ✅ Final Verification

### Publication Checklist

#### On GitHub:

- [ ] README.md displays correctly
- [ ] PRISMA image shows
- [ ] LICENSE visible
- [ ] CITATION.cff detected by GitHub
- [ ] Topics/tags added
- [ ] About complete
- [ ] Release v1.0 created
- [ ] All files present

#### Navigate files:

- [ ] `recoleccion/` has all CSVs
- [ ] `screening/` has PRISMA files
- [ ] `OE1/` - `OE4/` have analyses
- [ ] `objetive-dataDriven/` complete
- [ ] `articulosPDF/` (if you decided to include them)

#### Documentation:

- [ ] README clear and complete
- [ ] PRISMA_METADATA accessible
- [ ] ZENODO_GUIDE available
- [ ] CONTRIBUTING visible

#### Metadata:

- [ ] .zenodo.json with your info
- [ ] CITATION.cff with your info
- [ ] LICENSE with real names

### External User Test

Ask a colleague to:

1. Visit the repository
2. Read the README
3. Download a CSV file
4. Try to cite using CITATION.cff
5. Search for specific data

Could they do it easily? ✅

---

## 🎓 Best Practices

### 1. Clear Commit Messages

```bash
# Good ✅
git commit -m "Fix: Correct data in OE2/grupoA.csv line 45"
git commit -m "Docs: Update README with new finding"
git commit -m "Data: Add 3 validated studies to screening"

# Bad ❌
git commit -m "fix"
git commit -m "update"
git commit -m "changes"
```

### 2. Branches for Large Changes

```bash
# Create branch for update
git checkout -b update/add-new-studies

# Make changes
# ...

# Commit
git commit -m "Add 3 new validated studies"

# Push branch
git push -u origin update/add-new-studies

# Create Pull Request on GitHub
# Merge when ready
```

### 3. Protect Main Branch

GitHub Settings → Branches → Add rule:
- Branch name pattern: `main`
- ✅ Require pull request before merging
- ✅ Require approvals: 1

### 4. Maintain CHANGELOG

Create `CHANGELOG.md`:

```markdown
# Changelog

## [1.0.0] - 2025-11-13

### Added
- Initial release with complete systematic review dataset
- 79 studies included from 551 records
- Complete PRISMA screening data
- Analysis for 4 specific objectives

### Documentation
- Complete README with visual organization
- PRISMA 2020 metadata
- Zenodo publication guide
- Citation formats
```

---

## 🔄 Update Workflow

### For Future Updates:

```bash
# 1. Make changes to local files

# 2. Verify changes
git status
git diff

# 3. Add changes
git add modified-file.csv

# 4. Commit
git commit -m "Update: Add validation data for study XYZ"

# 5. Push
git push origin main

# 6. For new major version:
git tag -a v1.1 -m "Version 1.1: Added 5 new studies"
git push origin v1.1

# Zenodo will create new version automatically
```

---

## ❓ Troubleshooting

### Problem: File too large

```
Error: File size exceeds 100 MB
```

**Solution**:
```bash
# View large files
Get-ChildItem -Recurse | Where-Object {$_.Length -gt 50MB} |
    Select-Object FullName, @{Name="Size(MB)";Expression={[math]::Round($_.Length/1MB,2)}}

# Options:
# 1. Use Git LFS
git lfs install
git lfs track "*.pdf"
git add .gitattributes

# 2. Exclude from repository
echo "large-files/" >> .gitignore
```

### Problem: Authentication error

```
Authentication failed
```

**Solution**: Use Personal Access Token, not password
- GitHub → Settings → Developer settings → Tokens
- Generate new token
- Use that token as password

### Problem: Can't see PRISMA image

**Solution**: Verify path in README.md
```markdown
![PRISMA Diagram](prismaRevSisCubesat.png)
```

Must be relative to README.

### Problem: CITATION.cff not detected

GitHub takes a few minutes. Wait and refresh.

---

## 📚 Additional Resources

### Tutorials:
- GitHub Guides: https://guides.github.com/
- Git Handbook: https://guides.github.com/introduction/git-handbook/
- GitHub Desktop: https://docs.github.com/en/desktop

### Tools:
- GitHub Desktop: https://desktop.github.com/
- Git for Windows: https://git-scm.com/download/win
- Visual Studio Code: https://code.visualstudio.com/

### Community:
- GitHub Community: https://github.community/
- Stack Overflow: https://stackoverflow.com/questions/tagged/github

---

## 📧 Need Help?

If you have problems:

1. **Review** this guide completely
2. **Search** for the error on Google/Stack Overflow
3. **Ask** in GitHub Community
4. **Contact** GitHub support

---

## 🎉 Congratulations!

Once completed, you'll have:

✅ Public repository on GitHub
✅ Permanent DOI from Zenodo (if connected)
✅ Easy citation
✅ Complete transparency
✅ Guaranteed reproducibility
✅ Contributions enabled
✅ Maximum visibility

**Your systematic review will be accessible to the entire world with complete transparency! 🌍**

---

**Last updated**: 2025-11-13
**Version**: 1.0
**Author**: Setup guide for CubeSat systematic review
