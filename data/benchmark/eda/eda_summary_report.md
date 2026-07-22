# Exploratory Data Analysis Summary

## Purpose

This report summarises the exploratory dataset diagnostics performed before prompt construction and model execution. The EDA verifies whether the extracted CodeSearchNet-style records are suitable for controlled function-level code documentation generation.

## Input

- Input file: `data/processed/codesearchnet_balanced_15000.jsonl`

- Original record count: `15000`

- Record count after language filtering: `15000`

- Languages retained: `python, javascript, java`


## Column Mapping

- language: `language`

- code: `code`

- reference_doc: `reference_documentation`

- split: `split_name`


## Diagnostic Thresholds

- Minimum documentation length: `3` words

- Long-code diagnostic threshold: `6000` characters


## Language and Split Distribution

| language   | split   |   record_count |
|:-----------|:--------|---------------:|
| java       | train   |           5000 |
| javascript | train   |           5000 |
| python     | train   |           5000 |


## Length Statistics

| language   |   records |   code_chars_mean |   code_chars_median |   code_chars_p95 |   code_words_mean |   code_lines_mean |   doc_words_mean |   doc_words_median |   doc_words_p95 |   doc_lines_mean |
|:-----------|----------:|------------------:|--------------------:|-----------------:|------------------:|------------------:|-----------------:|-------------------:|----------------:|-----------------:|
| java       |      5000 |           465.636 |                 311 |          1364.5  |            48.277 |                 1 |           22.63  |                 20 |              52 |                1 |
| javascript |      5000 |           505.011 |                 352 |          1445    |            63.884 |                 1 |           19.694 |                 16 |              48 |                1 |
| python     |      5000 |           588.607 |                 452 |          1486.05 |            69.535 |                 1 |           20.419 |                 16 |              52 |                1 |


## Missing and Duplicate Summary

| language   |   records |   missing_code |   missing_doc |   very_short_doc |   duplicate_code |   duplicate_doc |   duplicate_code_doc_pair |
|:-----------|----------:|---------------:|--------------:|-----------------:|-----------------:|----------------:|--------------------------:|
| java       |      5000 |              0 |             0 |              108 |                0 |             271 |                         0 |
| javascript |      5000 |              0 |             0 |              111 |                0 |              39 |                         0 |
| python     |      5000 |              0 |             0 |               41 |                0 |              21 |                         0 |


## Code-Structure Summary

| language   |   records |   avg_parameter_count |   median_parameter_count |   records_with_parameters |   records_with_return |   parameter_record_rate |   return_record_rate |
|:-----------|----------:|----------------------:|-------------------------:|--------------------------:|----------------------:|------------------------:|---------------------:|
| java       |      5000 |                 1.511 |                        1 |                      4101 |                  3579 |                  0.8202 |               0.7158 |
| javascript |      5000 |                 1.183 |                        1 |                      3041 |                  3591 |                  0.6082 |               0.7182 |
| python     |      5000 |                 1.576 |                        1 |                      3855 |                  3703 |                  0.771  |               0.7406 |


## Filtering Diagnostics

| language   |   raw_records |   missing_code_or_doc |   short_documentation |   long_code_records |   duplicate_code_doc_pairs |   diagnostically_retained_records |
|:-----------|--------------:|----------------------:|----------------------:|--------------------:|---------------------------:|----------------------------------:|
| java       |          5000 |                     0 |                   108 |                   0 |                          0 |                              4892 |
| javascript |          5000 |                     0 |                   111 |                   0 |                          0 |                              4889 |
| python     |          5000 |                     0 |                    41 |                   0 |                          0 |                              4959 |


## Sample-Size Feasibility

|   candidate_sample_size_per_language | feasible_for_all_languages   |   java_available_valid_records |   javascript_available_valid_records |   python_available_valid_records |
|-------------------------------------:|:-----------------------------|-------------------------------:|-------------------------------------:|---------------------------------:|
|                                  100 | True                         |                           4892 |                                 4889 |                             4959 |
|                                  200 | True                         |                           4892 |                                 4889 |                             4959 |
|                                  400 | True                         |                           4892 |                                 4889 |                             4959 |
|                                  800 | True                         |                           4892 |                                 4889 |                             4959 |
|                                 1000 | True                         |                           4892 |                                 4889 |                             4959 |
|                                 1200 | True                         |                           4892 |                                 4889 |                             4959 |


## Interpretation

The EDA confirms whether language balancing, documentation filtering, duplicate removal, and prompt-length control are required before constructing the final benchmark. The structure diagnostics also support later code-grounded evaluation because parameter availability and return-statement presence determine whether parameter coverage and return coverage can be meaningfully assessed.
