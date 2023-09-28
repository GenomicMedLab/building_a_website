---
layout: paper

name: "Prioritization of retinal disease genes: an integrative approach"
date: 2013-06-01
authors: "Alex H. Wagner, Kyle R. Taylor, Adam P. DeLuca, Thomas L. Casavant, Robert F. Mullins, Edwin M. Stone, Todd E. Scheetz, Terry A. Braun"
journal: Human Mutation
volume: 34
pages: "853-859"
doi: https://doi.org/10.1002/humu.22317
pmid: 23508994
publisher_url: https://onlinelibrary.wiley.com/doi/10.1002/humu.22317

thumbnail: retinal-gene-prioritization.jpg
---
The discovery of novel disease-associated variations in genes is often a daunting task in highly heterogeneous disease classes. We seek a generalizable algorithm that integrates multiple publicly available genomic data sources in a machine-learning model for the prioritization of candidates identified in patients with retinal disease. To approach this problem, we generate a set of feature vectors from publicly available microarray, RNA-seq, and ChIP-seq datasets of biological relevance to retinal disease, to observe patterns in gene expression specificity among tissues of the body and the eye, in addition to photoreceptor-specific signals by the CRX transcription factor. Using these features, we describe a novel algorithm, positive and unlabeled learning for prioritization (PULP). This article compares several popular supervised learning techniques as the regression function for PULP. The results demonstrate a highly significant enrichment for previously characterized disease genes using a logistic regression method. Finally, a comparison of PULP with the popular gene prioritization tool ENDEAVOUR shows superior prioritization of retinal disease genes from previous studies. The java source code, compiled binary, assembled feature vectors, and instructions are available online at (https://github.com/ahwagner/PULP)[https://github.com/ahwagner/PULP].
