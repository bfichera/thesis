#!/bin/bash

pdflatex fichera-bfichera-phd-physics-2024-source.tex
bibtex bibliography
pdflatex fichera-bfichera-phd-physics-2024-source.tex
pdflatex fichera-bfichera-phd-physics-2024-source.tex
mv fichera-bfichera-phd-physics-2024-source.pdf fichera-bfichera-phd-physics-2024-thesis.pdf
