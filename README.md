# OCR for Low-Resource Indian Languages 

Contributed as a part of [Samanantar](https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00452/109468). 
Please note that this repo is not being managed actively. 
# Directory Structure 

This pipeline has 4 parts: 
- Crawler (includes files for crawling, matching articles, extracting metadata, yield estimation for sources)
- Preprocessing (Cleaning, Lang detection, Punctuation normalizer, tokenization, sentence splitting)
- OCR (Tesseract based OCR, Direct pipeline for sourcing urls and extracting data.)
- Alignment (Alignment with BleuAlign, HunAlign, LaBSE)
```
├── OCR
│   ├── pdf_ocr_reader.py
│   ├── url_pdf_ocr.ipynb
│   └── url_to_ocr.ipynb
├── README.md
├── aligner
│   ├── LaBSEAligner.ipynb
│   └── LaBSE_PDF_aligner.py
├── crawler
│   ├── PDFCrawler.ipynb
│   ├── PDFSourceNameScraper.ipynb
│   ├── PDFSourceNameScraper_Interleaved.ipynb
│   ├── PDFSourceNameScraper_Parallel.ipynb
│   ├── act_aligner.py
│   ├── act_matcher.py
│   ├── crawler.py
│   ├── sm_concatenate_files.py
│   ├── url_crawler.py
│   ├── visionocr.py
│   ├── visionocr_jsontotxt.py
│   └── yield_comparison.ipynb
└── preprocessing
    ├── SentenceSplitter.ipynb
    ├── SentenceSplittingPreprocessedDocuments.ipynb
    ├── indicpostprocessing.py
    ├── json_to_text.ipynb
    ├── postprocessing.py
    └── summary_generator.ipynb
```