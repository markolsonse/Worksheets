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

Worksheet is a LaTeX project used to create randomly generated single sided worksheets that can be easily reproduced.  Both the questions and answers on a given worksheet are generated using SageMath and typeset using LaTeX.   This project has been designed to easily run on CoCalc, but it can also be made to work on a local MacOs/Linux install with some care and attention given to ensuring all the dependencies are correctly installed.  If you are using >= MacOS 10.15, then getting SageMath to install locally in my experience has been a real pain, which is why I prefer to just run this project on CoCalc.

## Style Files

This project comes with 3 style files that can either be placed in your project folder or stored in your local _texmf_ folder:

1. markolsonworksheet.sty [Required]
1. markolsoncolorsthlm.sty [Required]
1. markolsonmath.sty [Optional]

If you are using CoCalc, then your local _texmf_ can be found in your home directory:
`~/texmf/tex/latex/`

Each worksheet is built using the latex article document class layout. It is further styled using the markolsonworksheet.sty file. The colors used for the worksheet are being referenced from the markolsoncolorsthlm.sty file.  Of course, you could either define your own colors directly in the `markolsonworksheet.sty file or update markolsoncolorsthml.sty to fulfill your color choices.

The markolsonmath.sty file is not required.  It is a collection of commands that I use to typeset my latex documents. By default, you should not need to install this package (include this style file in your preamble).  

## Document Structure

### Preamble

``` tex
%-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
%	DOCUMENT CLASS & PACKAGES
%-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

\documentclass[a4paper, 11pt]{article}
\usepackage{markolsonworksheet}
\usepackage{markolsoncolorsthlm}
%\usepackage{markolsonmath}
```

Here we can see that we are using the **article** document class with the options of a4paper and 11 point being passed to it.  Notice that both the `markolsonworksheet` and `markolsoncolorsthlm` packages are being called while the line used to call the _markolsonmath_ package is commented out.  For some worksheets, you might want to include a package to help format your content.  

For example, you might be creating a worksheet with with questions that involve column addition that could be easily typeset using xlop package.  All you need to do is append the `\usepackage{xlop}` to your preamble.

``` tex
%-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
%	DOCUMENT CLASS & PACKAGES
%-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

\documentclass[a4paper, 11pt]{article}
\usepackage{markolsonworksheet}
\usepackage{markolsoncolorsthlm}
%\usepackage{markolsonmath}

\usepackage{xlop}
```

### The Document

#### The Header Title

Each worksheet has the same title _Worksheet_.  The worksheet header title is globally defined in the `markolsonworksheet.sty` file and included on the worksheet using the `\maketitle` command.  

``` tex
%-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
%	DOCUMENT CLASS & PACKAGES
%-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

\begin{document}

\maketitle % Print the title section
```
Of course, you could choose to design your custom title from the style file or manually create your own title by replacing the `\maketitle` command with your own.

#### SageSilent Environement

The SageSilent environment is where all the magic happens as it is within this environment where you will write the majority of your sage code to generate your document. 

To under

For the majority of the worksheets that I generate, I am interested in generating two variables.

1. `qoutput` : a raw string of latex code to generate each question
1. `aoutput` : a raw string of latex code to generate each answer 



```python
# Set the random seed

t=ZZ.random_element(999999)
set_random_seed(t)

#SOME CODE GOES HERE 
# to generate an array of questions and an array of answers.

qoutput = ""
aoutput = ""

question = [ SomeArray of questions]
answer = [ SomeArray of answers]

for i in range(numberOfQuestions):
  qoutput += r"\item ${}$".format(question[i])
  aoutput += r"\item \cRed{{${}$}}".format(answer[i])
``
