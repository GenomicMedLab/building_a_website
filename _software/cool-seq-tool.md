---
contributors:
- korikuzma
- jsstevenson
- jarbesfeld
- ahwagner
- katiestahl
description: <p>The <strong>CoolSeqTool</strong> provides:</p><ul><li>A Pythonic API
  on top of sequence data of interest to tertiary analysis tools, including mappings
  between gene names and transcripts, <a href="https://www.ncbi.nlm.nih.gov/refseq/MANE/">MANE
  transcript</a> descriptions, and the <a href="https://github.com/biocommons/uta">Universal
  Transcript Archive</a></li><li>Augmented access to the <a href="https://github.com/biocommons/biocommons.seqrepo">SeqRepo</a>
  database, including multiple additional methods and tools</li><li>Mapping tools
  that combine the above to support translation between references sequences, annotation
  layers, and MANE transcripts</li></ul>
distribution: https://pypi.org/project/cool-seq-tool/
docs: https://coolseqtool.readthedocs.io
languages:
- Python
latest_commits:
- author: jarbesfeld
  commit: Ensure proper gene symbol comparison (#373)
  url: https://github.com/GenomicMedLab/cool-seq-tool/commit/e9a917e32b07a705231fa17f69d9844c4bb01a6c
- author: katiestahl
  commit: 'fix: make gene optional param for converting genomic coords'
  url: https://github.com/GenomicMedLab/cool-seq-tool/commit/6fa7efbdc2fa5547d9b9ca42dbab845e24476115
- author: jarbesfeld
  commit: Do not require gene when genomic accession and transcript are provided to
    genomic_to_tx_segment (#369)
  url: https://github.com/GenomicMedLab/cool-seq-tool/commit/14443469efd510a9fe7cfe34252b53ba32b7c401
- author: korikuzma
  commit: 'refactor: remove duplicate `genomic_ac` check (#365)'
  url: https://github.com/GenomicMedLab/cool-seq-tool/commit/0f7fc9a23d9f440a5d9a3966a4ac40157d7c617b
- author: korikuzma
  commit: 'refactor: rename `_get_alt_ac_start_and_end` + flatten output (#360)'
  url: https://github.com/GenomicMedLab/cool-seq-tool/commit/aa0ab3755a4588513566499a878be907b3fecbd8
latest_release:
  url: https://github.com/GenomicMedLab/cool-seq-tool/releases/tag/0.7.1
  version: 0.7.1
layout: software
name: Cool-Seq-Tool
source: https://github.com/GenomicMedLab/cool-seq-tool/
---

