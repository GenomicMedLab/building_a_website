---
authors: Matthew Cannon, James Stevenson, Kori Kuzma, Susanna Kiwala, Jeremy L Warner, Obi L Griffith, Malachi Griffith, Alex H Wagner
date: 2023-11-08
doi: https://doi.org/10.1101/2023.07.27.23293245
issue: 4
journal: JAMIA Open
layout: paper
name: Normalization of Drug and Therapeutic Concepts with TheraPy
preprint: https://www.medrxiv.org/content/10.1101/2023.07.27.23293245v1
projects:
- Knowledgebase Integration
publisher_url: https://academic.oup.com/jamiaopen/article/6/4/ooad093/7388192
thumbnail: therapy_paper_preview.png
volume: 6
---
### Objective

The diversity of nomenclature and naming strategies makes therapeutic terminology difficult to manage and harmonize. As the number and complexity of available therapeutic ontologies continues to increase, the need for harmonized cross-resource mappings is becoming increasingly apparent. This study creates harmonized concept mappings that enable the linking together of like-concepts despite source-dependent differences in data structure or semantic representation.

### Materials and Methods

For this study, we created Thera-Py, a Python package and web API that constructs searchable concepts for drugs and therapeutic terminologies using 9 public resources and thesauri. By using a directed graph approach, Thera-Py captures commonly used aliases, trade names, annotations, and associations for any given therapeutic and combines them under a single concept record.

### Results

We highlight the creation of 16 069 unique merged therapeutic concepts from 9 distinct sources using Thera-Py and observe an increase in overlap of therapeutic concepts in 2 or more knowledge bases after harmonization using Thera-Py (9.8%-41.8%).

### Conclusion

We observe that Thera-Py tends to normalize therapeutic concepts to their underlying active ingredients (excluding nondrug therapeutics, eg, radiation therapy, biologics), and unifies all available descriptors regardless of ontological origin.

