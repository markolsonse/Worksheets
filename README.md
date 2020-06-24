<p align="center">
    <img src="GitHub-Worksheets.png" width="400" max-width="90%" alt="Publish" />
</p>

<p align="center">
    <a href = "https://www.sagemath.org">
        <img src="https://img.shields.io/badge/SageMath-9.1-blue.svg" />
    </a>
    <a href = "https://www.cocalc.com">
        <img src="https://img.shields.io/badge/CoCalc-orange.svg" />
    </a>
        <img src="https://img.shields.io/badge/LaTeX-orange.svg" />
</p>

Worksheet is a LaTeX project used to create randomly generated worksheets that can be easily reproduced.  Both the questions and answers on a given worksheet are generated using SageMath and typeset using LaTeX.   This project has been designed to easily run on CoCalc, but it can also be made to work on a local MacOs/Linux install with some care and attention given to ensuring all the dependencies are correctly installed.  If you are using >= MacOS 10.15, then getting SageMath to install locally in my experience has been a real pain, which is why I prefer to just run this project on CoCalc.

## Style Files

This project comes with 3 style files that can either be placed in your project folder or stored in your local _texmf_ folder:

1. markolsonworksheet.sty [Required]
1. markolsoncolorsthlm.sty [Required]
1. markolsonmath.sty [Optional]

If you are using CoCalc, then your local _texmf_ can be found in your home directory:
_~/texmf/tex/latex/_

Each worksheet is built using the latex article document class layout. It is further styled using the markolsonworksheet.sty file. The colors used for the worksheet are being referenced from the markolsoncolorsthlm.sty file.  Of course, you could either define your own colors directly in the markolsonworksheet.sty file or update markolsoncolorsthml.sty to fulfill your color choices.

The markolsonmath.sty file is not required.  It is a collection of commands that I use to typeset my latex documents. By default, you should not need to install this package (include this style file in your preamble).  



