---
contributors:
- korikuzma
- jsstevenson
- ahwagner
- OHSU-MachineUser
description: a <b>sdfflkj</b> c
distribution: https://pypi.org/project/gene-normalizer/
docs: https://gene-normalizer.readthedocs.io/en/latest/
languages:
- Python
- Shell
latest_commits:
- author: jsstevenson
  commit: 'feat!: use wags-tails for data acquisition (#303)'
  url: https://github.com/cancervariants/gene-normalization/commit/c747340a4f41e1464a63a88195611bcbee288fdd
- author: jsstevenson
  commit: 'test: suppress noisy boto logs by default (#300)'
  url: https://github.com/cancervariants/gene-normalization/commit/5f678bc9a467b000655d1cfada74cb95d17b4130
- author: jsstevenson
  commit: 'cicd: use ruff for autoformatting (#292)'
  url: https://github.com/cancervariants/gene-normalization/commit/98294edceb433ad3d4060fa771105bdd2e1c6605
- author: korikuzma
  commit: 'build: properly pin pydantic v2 major version (#290)'
  url: https://github.com/cancervariants/gene-normalization/commit/cae10d77548cb24ee3003407e08910438c2fb58a
- author: jsstevenson
  commit: 'build: define build system (#288)'
  url: https://github.com/cancervariants/gene-normalization/commit/1c18396067cc7655bbce1c8ff223ccae42e160c5
latest_release:
  url: https://github.com/cancervariants/gene-normalization/releases/tag/0.3.0-dev1
  version: 0.3.0-dev1
layout: software
live: https://normalize.cancervariants.org/gene
name: Gene Normalizer
projects:
- Knowledgebase Integration
source: https://github.com/cancervariants/gene-normalization/
---
The Gene Normalizer provides tools for resolving ambiguous human gene references to consistently-structured, normalized terms. For gene concepts extracted from [NCBI Gene](https://www.ncbi.nlm.nih.gov/gene/), [Ensembl](https://useast.ensembl.org/index.html), and [HGNC](https://www.genenames.org/), it designates a [CURIE](https://en.wikipedia.org/wiki/CURIE), and provides additional metadata like current and previously-used symbols, aliases, database cross-references and associations, and coordinates.

