import os
import subprocess
from pathlib import Path

def compileLatex():
    tex_extension = ["*.tex"]
    for extension in tex_extension:
       for filename in Path(path).rglob(extension):
           subprocess.run(["pdflatex", "-interaction", "nonstopmode", filename])
def compileSage():
    sage_extension = ["*.sagetex.sage"]
    for extension in sage_extension:
        for filename in Path(path).rglob(extension):
            subprocess.run(["sage", filename])
    

print("""
Choose your directory:

[1]: LatexSageMath
[2]: LatexMath
""")

includesSage = int(input("Enter your choice: "))
if includesSage == 1:
    os.chdir(r"LatexSageMath")
    path = os.getcwd()
    genAllFiles = input("Would you like to generate ALL files [Y]/[N]?: ")
    
    if genAllFiles == "Y":
        compileLatex()
        compileSage()
        compileLatex()
    else:
        genMultipleCopies = input("Would you like to generate multiple copies of a file? [Y] / [N]?: ")

        if genMultipleCopies == "Y":
            filename = input("Enter the filename: ")
            copies = input("Enter the number of copies: ")
            copy = 1
            while copy <= int(copies):
                subprocess.run(["pdflatex",  "-interaction", "nonstopmode",filename+".tex"])
                subprocess.run(["sage", filename+".sagetex.sage"])
                subprocess.run(["pdflatex", "-interaction", "nonstopmode",filename+".tex"])
                subprocess.run(["mv", filename+".pdf", filename+"-"+str(copy)+".pdf"])
                copy += 1
        else:
            pass 
elif includesSage == 2:
    os.chdir(r"LatexMath")
    path = os.getcwd()
    
    genAllFiles = input("Would you like to generate ALL files [Y]/[N]?: ")

    if genAllFiles == "Y":
        compileLatex()
    else:
        genMultipleCopies = input("Would you like to generate multiple copies of a file? [Y] / [N]?: ")

        if genMultipleCopies == "Y":
            filename = input("Enter the filename: ")
            copies = input("Enter the number of copies: ")
            copy = 1
            while copy <= int(copies):
                subprocess.run(["pdflatex",  "-interaction", "nonstopmode", filename+".tex"])
                subprocess.run(["mv", filename+".pdf", filename+"-"+str(copy)+".pdf"])
                copy += 1
        else:
            pass
else:
    pass


# =-= FILES BY EXTENSION
del_extensions = ["*.aux", "*.lb", "*.fdb_latexmk", "*.snm", "*.fls", "*.mw", "*.toc", "*.lb","*.nav", "*.synctex.gz", "*.vrb", "*.out", "*.log", "*.pytxcode", "*.sagetex.sage", "*.sagetex.sage.py", "*.sagetex.sout", "*.synctex.gz", "*.sagetex.scmd", "*.synctex(busy)"]
for del_extension in del_extensions:
    for filename in Path(path).rglob(del_extension):
        subprocess.run(["rm", filename])

# =-= DIRECTORIES TO BE RECURSIVELY DELETED
dir_patterns = ["pythontex-files-*","sage-plots-for*"]
for dir_pattern in dir_patterns:
    for dir_name in Path(path).rglob(dir_pattern):
       subprocess.run(["rm", "-r", dir_name])