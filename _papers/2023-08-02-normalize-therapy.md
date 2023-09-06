---
layout: paper

title: Normalization of Drug and Therapeutic Concepts with TheraPy
date: 2023-08-02
authors: "Matthew Cannon, James Stevenson, Kori Kuzma, Susanna Kiwala, Jeremy L Warner, Obi L Griffith, Malachi Griffith, Alex H Wagner"
journal_cite: "medRxiv 2023.07.27.23293245v1"
doi: https://doi.org/10.1101/2023.07.27.23293245
publisher_url:
preprint: https://www.medrxiv.org/content/10.1101/2023.07.27.23293245v1

thumbnail: therapy_paper_preview.png

projects:
---
Working with therapeutic terminology in the field of medicine can be challenging due to both the number of ways terms can be addressed and the ambiguity associated with different naming strategies. A therapeutic concept can be identified across many facets from ontologies and vocabularies of varying focus, including natural product names, chemical structures, development codes, generic names, brand names, product formulations, or treatment regimens. This diversity of nomenclature makes therapeutic terminology difficult to manage and harmonize. As the number and complexity of available therapeutic ontologies continues to increase, the need for harmonized cross-resource mappings is becoming increasingly apparent. Harmonized concept mappings will enable the linking together of like-concepts despite source-dependent differences in data structure or semantic representation. To support these mappings, we introduce TheraPy, a Python package and web API that constructs stable, searchable merged concepts for drugs and therapeutic terminologies using publicly available resources and thesauri. By using a directed graph approach, TheraPy can capture commonly used aliases, trade names, annotations, and associations for any given therapeutic and combine them under a single merged concept record. Using this approach, we found that TheraPy tends to normalize therapeutic concepts to their underlying active ingredients (excluding non-drug therapeutics, e.g. radiation therapy, biologics), and unifies all available descriptors regardless of ontological origin. In this report, we highlight the creation of 16,069 unique merged therapeutic concepts from 9 distinct sources using TheraPy. Further, we analyze rates of normalization for therapeutic terms taken from publicly available vocabularies.