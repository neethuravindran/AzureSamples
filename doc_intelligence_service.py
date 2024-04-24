"""
FILE: doc_intelligence_service.py
 
DESCRIPTION:
    This example shows how to analyse general documents using Azure Form Recognizer
 
USAGE: python doc_intelligence_service.py
 Input PDF / DOCX document required
 Pretrained document-analysis models used for analyse document
 create  `DocumentAnalysisClient` instance and `AzureKeyCredential` variable
 
EXAMPLE OUTPUT:
   Extracted written or printed table cells, pages, lines, and words.
   To test any of the document, select the pretrained document-analysis models and use the sample documents to analyze. 
"""


import os
from azure.ai.formrecognizer import DocumentAnalysisClient
from azure.core.credentials import AzureKeyCredential
  
#Replace docUrl with the path from blob storage
docUrl = "https://raw.githubusercontent.com/Azure-Samples/cognitive-services-REST-api-samples/master/curl/form-recognizer/sample-layout.pdf"
endpoint = "https://<xxxxxx>.cognitiveservices.azure.com/"
key = "yyyyyyyyy"
 

def doc_intelligence_service():  
 
     document_analysis_client = DocumentAnalysisClient(endpoint=endpoint, credential=AzureKeyCredential(key))
 
     poller = document_analysis_client.begin_analyze_document_from_url(
            "prebuilt-document", docUrl)
     result = poller.result()
   
     for table_idx, table in enumerate(result.tables):
        print(
            "Table # {} has {} rows and {} columns".format(
                table_idx, table.row_count, table.column_count
            )
        )
        
     for cell in table.cells:
        print(
            "...Cell[{}][{}] has content '{}'".format(
                cell.row_index,
                cell.column_index,
                cell.content,
            )
        )          
            
     for page in result.pages:
        print("----Analyzing document from page #{}----".format(page.page_number))
        print(
            "Page has width: {} and height: {}, measured with unit: {}".format(
                page.width, page.height, page.unit
            )
        )

     for line_idx, line in enumerate(page.lines):
        print(
            "...Line # {} has text content '{}'".format(
                line_idx,
                line.content
            )
        )
     for word in page.words:
        print(word.content)
   
 
if __name__ == "__main__":
    doc_intelligence_service()