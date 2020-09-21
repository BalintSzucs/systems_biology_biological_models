# Mining NCBI Databases

## Description

This script mines NCBI databases and creates a network of genes that are connected based on being mentioned in the same PubMed article. 

The script requires a Taxonomy ID to begin and creates and output in a Graphml file. A network representation can be created using a third-hand software (e.g. Cytoscape, Gephi).

The weight of an edge is determined by the number of articles linking **two genes.** As an example if GeneID_1 and GeneID_2 are both mentioned in 5 different PubMed articles the weight is proportionally going to be thicker. 

The script aims to discern (1) important networks, (2) uninteresting or virgin territorries in research, (3) small volume of research articles (low edge weight/potential research interests).

**Examples:**

**TaxID: 9606**
**NCBI release: Homo sapiens Annotation Release 109**

**Set of 25 genes connected by PubMed articles:**

![Set of 25 genes connected by PubMed articles:](https://github.com/BalintSzucs/systems_biology_biological_models/blob/Mining_NCBI_Databases/Mining_NCBI_databases/sample_dataset1.png)


**Set of 25 genes connected by PubMed articles:**

![Set of 100 genes connected by PubMed articles:](https://github.com/BalintSzucs/systems_biology_biological_models/blob/Mining_NCBI_Databases/Mining_NCBI_databases/sample_network_100_genes.png)