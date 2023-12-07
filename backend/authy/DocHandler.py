import os
import random
import string
from pathlib import Path
from uuid import uuid4
from dotenv import load_dotenv
from azure.ai.formrecognizer import DocumentAnalysisClient
from azure.core.credentials import AzureKeyCredential
import fitz
import io
from PIL import Image

load_dotenv()
env = os.environ

key = env.get('DOC_AI_KEY')
endpoint = env.get('DOC_AI_ENDPOINT')


def analyse_ID(fileURL):
    document_analysis_client = DocumentAnalysisClient(
        endpoint=endpoint, credential=AzureKeyCredential(key)
    )

    poller = document_analysis_client.begin_analyze_document_from_url(
        "prebuilt-idDocument", fileURL
    )
    id_documents = poller.result()

    for idx, id_document in enumerate(id_documents.documents):
        first_name = id_document.fields.get("FirstName")
        f_name = ''
        if first_name:
            f_name = first_name.value

        last_name = id_document.fields.get("LastName")
        l_name = ''
        if last_name:
            l_name = last_name.value

        document_number = id_document.fields.get("DocumentNumber")
        doc_num = ''
        if document_number:
            doc_num = document_number.value

        dob = id_document.fields.get("DateOfBirth")
        d_o_b = ''
        if dob:
            d_o_b = str(dob.value)

        doe = id_document.fields.get("DateOfExpiration")
        d_o_e = ''
        if doe:
            d_o_e = str(doe.value)

        sex = id_document.fields.get("Sex")
        sex_ = ''
        if sex:
            sex_ = sex.value

        address = id_document.fields.get("Address")
        address_ = ''
        if address:
            address_ = str(address.value)

        country_region = id_document.fields.get("CountryRegion")
        country = ''
        if country_region:
            country = str(country_region.value)

        region = id_document.fields.get("Region")
        region_ = ''
        if region:
            region_ = str(region.value)

        send = {
            'first_name': f_name,
            'last_name': l_name,
            'document_number': doc_num,
            'DOB': d_o_b,
            'DOE': d_o_e,
            'sex': sex_,
            'address': address_,
            'country': country,
            'region': region_
        }
        return send


def PDFtoImage(pdfPath):
    # open the file
    pdf_file = fitz.open(pdfPath)
    print(pdf_file)

    # iterate over PDF pages
    path = ''
    for page_index in range(len(pdf_file)):
        # get the page itself
        page = pdf_file[page_index]
        image_list = page.get_images()

        # printing number of images found in this page
        if image_list:
            print(f"[+] Found a total of {len(image_list)} images in page "
                  f"{page_index}")
        else:
            print("[!] No images found on page", page_index)
        for image_index, img in enumerate(page.get_images(), start=1):
            # get the XREF of the image
            xref = img[0]
            # extract the image bytes
            base_image = pdf_file.extract_image(xref)
            image_bytes = base_image["image"]
            # get the image extension
            image_ext = base_image["ext"]
            # load it to PIL
            image = Image.open(io.BytesIO(image_bytes))
            # save it to local disk
            rand_strings = ''.join(random.choice(string.ascii_lowercase
                                                 + string.digits
                                                 + string.ascii_uppercase)
                                   for i in range(5))
            file_name = f"{rand_strings}{uuid4().hex}.{image_ext}"
            BASE_DIR = Path(__file__).resolve(strict=True).parent.parent
            path = f'{BASE_DIR}/media/pdf_images/{file_name}'
            image.save(open(path, "wb"))

    return path
