---
contributors:
- korikuzma
- jsstevenson
- ahwagner
- OHSU-MachineUser
distribution: https://pypi.org/project/gene-normalizer/
docs: https://gene-normalizer.readthedocs.io/
languages:
- Python
- Shell
latest_commits:
- author: korikuzma
  commit: 'build: properly pin pydantic v2 major version (#290)'
  url: https://github.com/cancervariants/gene-normalization/commit/cae10d77548cb24ee3003407e08910438c2fb58a
- author: jsstevenson
  commit: 'build: define build system (#288)'
  url: https://github.com/cancervariants/gene-normalization/commit/1c18396067cc7655bbce1c8ff223ccae42e160c5
- author: korikuzma
  commit: 'docs: update VRS compliance (#287)'
  url: https://github.com/cancervariants/gene-normalization/commit/ada4432fbf7905e190787f52dbec59c083c856ef
- author: korikuzma
  commit: 'cicd: update release.yaml (publish python distribution to pypi) (#283)
    (#284)'
  url: https://github.com/cancervariants/gene-normalization/commit/8bea8253c029b2edc4c301f4bbb735e6d2d0fb12
- author: jsstevenson
  commit: 'refactor: remove unused error handling (#280)'
  url: https://github.com/cancervariants/gene-normalization/commit/656db1b78699f70fcc1c63f0b2a641e708edc386
latest_release:
  url: https://github.com/cancervariants/gene-normalization/releases/tag/0.3.0-dev1
  version: 0.3.0-dev1
latest_version: 0.3.0-dev1
layout: software
live: https://normalize.cancervariants.org/gene
name: Gene Normalizer
projects:
- Knowledgebase Integration
source: https://github.com/cancervariants/gene-normalization/
---
The Gene Normalizer provides tools for resolving ambiguous human gene references to consistently-structured, normalized terms. For gene concepts extracted from [NCBI Gene](https://www.ncbi.nlm.nih.gov/gene/), [Ensembl](https://useast.ensembl.org/index.html), and [HGNC](https://www.genenames.org/), it designates a [CURIE](https://en.wikipedia.org/wiki/CURIE), and provides additional metadata like current and previously-used symbols, aliases, database cross-references and associations, and coordinates.

