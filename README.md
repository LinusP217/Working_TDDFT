# Working TD-DFT Project

```bash
 
   _   _                            _____  ______ _______ 
  | | (_)                          |  __ \|  ____|__   __|
  | |_ _  ___ _ __ ___  _ __   ___ | |  | | |__     | |   
  | __| |/ _ \ '_ ` _ \| '_ \ / _ \| |  | |  __|    | |   
  | |_| |  __/ | | | | | |_) | (_) | |__| | |       | |   
   \__|_|\___|_| |_| |_| .__/ \___/|_____/|_|       |_|   
                       | |                                
                       |_|                                
 
 An OER for learning time-dependent density-functional theory.
```

[![Python 3.10](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

> Density functional theory is one of the greatest free lunches ever. It’s a mysterious way to bypass solving the Schrödinger equation directly, making it relatively inexpensive to solve electronic structure problems, but requiring an uncontrolled approximation.
>
> \- [**Kieron Burke**](https://www.chemistryviews.org/details/ezine/10661444/Speeding_Up_DFT_Calculations_with_Machine_Learning/), UCI

---

## To do 
 - [x] Start boilerplate repo
 - [ ] Develop GUI widget tools with 1D PIB (Jacob)
 - [ ] Code up coupling matrix for ^^ (Jacob)
 - [ ] SymPy implementation + testing (Dayana)
 - [ ] Runge-Gross Theorem explanation (Evan)
 - [ ] conceptual description of Casida's eq'n (Evan)

## 🪟 Overview

This repository contains learning material on time-dependent density-functional theory (TDDFT)  accessible through the Google Colaboratory (Colab). TDDFT is a widely used method in quantum chemistry, but, like its ground state counterpart, is often a black box to the users of commercial software packages, e.g., VASP and Gaussian. This work helps to fix that. Intended for both researchers and students who want to develop a deeper understanding, we present a collection of Colab tutorials that progressively explains the fundamental concepts, from the Runge-Gross theorem to XC kernels to Casida's equation. Our approach relies on a one-dimensional particle-in-a-box model system that&mdash;in contrast to the complexity present in plane-wave and molecular codes&mdash;allows for simplified integrals and matrix operations. Basic knowledge of quantum mechanics and ground state DFT is assumed throughout. Feel free to explore the content through the links below.

This is a project in active development by the [Zuehlsdorff Group](https://timzuehlsdorff.com/) at Oregon State University 🌳 and is an extension of previous efforts with [pedagogic DFT content](https://github.com/tjz21/DFT_PIB_Code).

## 🗒️ Computational Notebooks

### Table of Contents

| Notebook | Description | Colab Link |
| -------- | ----------- | ---------- |
| 1&mdash;🏗️ TD-DFT Foundations  | Brief outline of the history and mathematical justification of TD-DFT.| [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/LinusP217/Working_TDDFT/blob/main/notebooks/Notebook1.ipynb)       |
| 2&mdash;🍳 Ingredients of TD-DFT | Essential components of TD-DFT presented through a 1D PIB system. | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/LinusP217/Working_TDDFT/blob/main/notebooks/Notebook2.ipynb)       |
| 3&mdash;👨 Casida's Approach | Delves into the machinery of linear-response TD-DFT, used in quantum chemistry codes. | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/LinusP217/Working_TDDFT/blob/main/notebooks/Notebook3.ipynb)       |
| 4&mdash;⌛ Real-time  | Alternative nonperturbative approach using time propagation. | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/LinusP217/Working_TDDFT/blob/main/notebooks/Notebook4.ipynb)       |
| 5&mdash;📈 Making Spectra | Taking the energies and oscillator strengths to generate spectra. | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/LinusP217/Working_TDDFT/blob/main/notebooks/Notebook5.ipynb)       |

### Interactivity

Content blocks with GUI widgets contain interactive visualization tools. They become active after the cell is executed:

<div style="text-align:center;">
  <img src="https://github.com/BashirovaD/DFT_code/blob/main/figures/wavefunction_anim.gif" width="700" height="398">
</div>

## Links
 - [Further Resources List]()
 - [Changelog]()
 - [Contributing](https://github.com/LinusP217/Working_TDDFT/blob/main/CONTRIBUTING.md)
 - [Authors](https://github.com/LinusP217/Working_TDDFT/blob/main/AUTHORS)

---

### Citation
If you would like cite this work, please refer to the following publication:
>
>
>

