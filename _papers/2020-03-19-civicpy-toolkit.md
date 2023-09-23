---
# still tentative. unsure how to handle citation/names
# name file as YYYY-MM-DD-some-identifying-words.md
layout: paper

name: "CIViCpy: A Python Software Development and Analysis Toolkit for the CIViC Knowledgebase"
date: 2020-03-19
authors: "Alex H. Wagner, Susanna Kiwala, Adam C. Coffman, Joshua F. McMichael, Kelsy C. Cotto, Thomas B. Mooney, Erica K. Barnell, Kilannin Krysiak, Arpad M. Danos, Jason Walker, Obi L. Griffith, and Malachi Griffith"
journal_cite: "JCO Clinical Cancer Informatics 2020 :4, 245-253"
doi: https://doi.org/10.1200/cci.19.00127
pmid: 32191543
publisher_url: https://ascopubs.org/doi/10.1200/CCI.19.00127?url_ver=Z39.88-2003
github: https://github.com/griffithlab/civicpy

thumbnail: civicpy-toolkit-preview.jpeg
---

### Purpose

Precision oncology depends on the matching of tumor variants to relevant knowledge describing the clinical significance of those variants. We recently developed the Clinical Interpretations for Variants in Cancer (CIViC; civicdb.org) crowd-sourced, expert-moderated, and open-access knowledgebase. CIViC provides a structured framework for evaluating genomic variants of various types (eg, fusions, single-nucleotide variants) for their therapeutic, prognostic, predisposing, diagnostic, or functional utility. CIViC has a documented application programming interface for accessing CIViC records: assertions, evidence, variants, and genes. Third-party tools that analyze or access the contents of this knowledgebase programmatically must leverage this application programming interface, often reimplementing redundant functionality in the pursuit of common analysis tasks that are beyond the scope of the CIViC Web application.

### Methods

To address this limitation, we developed CIViCpy (civicpy.org), a software development kit for extracting and analyzing the contents of the CIViC knowledgebase. CIViCpy enables users to query CIViC content as dynamic objects in Python. We assess the viability of CIViCpy as a tool for advancing individualized patient care by using it to systematically match CIViC evidence to observed variants in patient cancer samples.

### Results
We used CIViCpy to evaluate variants from 59,437 sequenced tumors of the American Association for Cancer Research Project GENIE data set. We demonstrate that CIViCpy enables annotation of > 1,200 variants per second, resulting in precise variant matches to CIViC level A (professional guideline) or B (clinical trial) evidence for 38.6% of tumors.

### Conclusion

The clinical interpretation of genomic variants in cancers requires high-throughput tools for interoperability and analysis of variant interpretation knowledge. These needs are met by CIViCpy, a software development kit for downstream applications and rapid analysis. CIViCpy is fully documented, open-source, and available free online.
