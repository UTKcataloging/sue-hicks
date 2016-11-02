# Sue Hicks Metadata

---

## About

This repository includes all metadata from the Sue Hicks Collection for the "[Of Monkeys and Men: Public and Private Views of the Scopes Trial](https://digital.lib.utk.edu/collections/scopescollection)" digital collection.

## Repository Structure

```
|-- cleaned_data
    |-- modsxml
        |-- 0012_000416_000001.xml 
        |-- 0012_000416_000002.xml
        |-- 0012_000416_000003.xml
        |-- 0012_000416_000004.xml
        |-- 0012_000416_000005.xml
        |-- 0012_000416_000006.xml
        |-- etc. etc.
    |-- remediation_files
        |-- final_cleaned.csv
        |-- SueHicks-FinalEdit.openrefine.tar.gz
        |-- SueHicks_MODS_collection.xml
        |-- sue-hicks-test.xml
        |-- short-example.xml
|-- original_data
    |-- Sue_Hicks.csv

```

## XSL File
An xsl stylesheet to convert a modsCollection to a series of individual MODS records.
* drops elements with 'null' text nodes
* (_attempts_ at) processing `name/namePart` elements that contain the valueURI for the `name`
* splits the modsCollection on each mods child (this could be genericized a bit more).
* the `short-example.xml` is for quick tests and can be ignored.
