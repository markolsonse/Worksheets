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
				<img src="https://img.shields.io/badge/sagetex-orange.svg" />
</p>

Worksheets is a LaTeX project used to create randomly generated single-sided worksheets that can be easily reproduced.  Both the questions and answers on a given worksheet are generated using SageMath and typeset using LaTeX. It is the `sagetex.sty` package that provides latex the access to SageMath to perform calculations and reference stored values. This worksheets project has been designed to easily run on CoCalc, but it can also be made to work on a local MacOs/Linux machine with some care and attention to ensuring all the dependencies are satisfied.  If you are using >= MacOS 10.15, then getting SageMath to install locally in my experience has been a massive headache, which is why I prefer to just run anything using SageMath on CoCalc. 


## Style Files

This project comes with 3 style files that can either be placed in the folder where your foo.tex file are stored or in your local _texmf_ folder:

1. markolsonworksheet.sty [Required]
1. markolsoncolorsthlm.sty [Required]
1. markolsonmath.sty [Optional]

You must also have a working `sagetex.sty` style file either in your latex path or project directory that corresponds to the SageMath release installed on your computer.  CoCalc ensures the correct file is in the correct place, so nothing required by the user here.  Note that if you are using CoCalc, then your local _texmf_ can be found in your home directory:
`~/texmf/tex/latex/`.  Your sagetex.sty should already be included in this path if you are using CoCalc.

Each worksheet is built using the latex article document class layout. It is further styled using the markolsonworksheet.sty file. The colors used for the worksheet are being referenced from the `markolsoncolorsthlm.sty` file.  Of course, you could modify the existing color definintions in the `markolsoncolorsthlm.sty` file or define your own directly in the `markolsonworksheet.sty` to fulfill your color choice preferences.

The `markolsonmath.sty` file is not required.  It is simply a collection of commands that I use to typeset my latex documents. By default, you should not need to include this package in your preamble.  

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

The preamble starts by defining the document class as article with options of a4paper and 11 point font.  Notice that both the `markolsonworksheet` and `markolsoncolorsthlm` packages are being called while the line used to call the `markolsonmath` package is commented out.  

For some worksheets, you might want to include a package to help format your content.  For example, you might be creating a worksheet with with questions that involve column addition that could be easily typeset using the xlop package.  All you need to do is append the `\usepackage{xlop}` to your preamble.

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

\maketitle % Print the title 
```
Of course, you could choose to design your custom title from the style file or manually create your own title by replacing the `\maketitle` command with your own custom title.


#### Worksheets Questions & Answers

While the `sagesilent` environment is written before the latex code used to typeset the worksheet questions and answers, we should first consider what it is we want to be expressed on the worksheet.  First, we would like to create an enumerated environment and populate it with items that represent the questions.  

```latex
begin{enumerate}
 \item Question 1
 \item Question 2
 \item Question 3
 .
 .
 .
 \item Question n
\end{enumerate}

The number of questions on a given worksheet will vary, so we are going to have sage generate the latex code necessary to generate each `\item` line of the enumerated environment.  Sage is now in charge of writing some latex code and we can forget about having to write each `\item` line of enumerated environment for each unique worksheet.  Good eh?

Sage will be used to assign all `\item` lines to a variable called `qoutput` of type raw string and we can access that variable in our latex code using a `\sagestr{}` command.  I choose the variable qoutput for _question output_, but you could easily change this to something more to your liking.  Now, our enumerated environment is simplified to one line of code and can generate a `\item` line for each question within our enumerated environment:

```latex
\begin{enumerate}
	\sagestr{qoutput}
\end{enumerate}
```
In fact a similar process will be used to generate the answers using the variable `aoutput`:

```latex
\begin{enumerate}
\sagestr{aoutput}
\end{enumerate}
```
Now we have a goal to have sage generate two variables `qoutput` and `aoutput`.


#### SageSilent Environment

The SageSilent environment is where all the magic happens as it is within this environment where you will write the majority of your Sage code.  In general, 



The majority of the worksheets we create have both questions and an answers section.
For the majority of the worksheets that are generate, we are interested in generating two variables that I initialise as empty strings.

1. `qoutput` 
1. `aoutput` 

The `qoutput` variable represents a raw string that 

```python
# Set the random seed

t=ZZ.random_element(999999)
set_random_seed(t)

# SOME CODE GOES HERE 
# to generate an array of questions and an array of answers.

qoutput = ""
aoutput = ""

question = [ SomeArray of questions]
answer = [ SomeArray of answers]

for i in range(numberOfQuestions):
  qoutput += r"\item ${}$".format(question[i])
  aoutput += r"\item \cRed{{${}$}}".format(answer[i])
``
