import os
import string
from pathlib import Path
import random
from uuid import uuid4
from dotenv import load_dotenv
from azure.ai.formrecognizer import DocumentAnalysisClient
from azure.core.credentials import AzureKeyCredential

load_dotenv()
env = os.environ

key = env.get('DOC_AI_KEY')
endpoint = env.get('DOC_AI_ENDPOINT')


def rename_id(instance, filename):
    ext = filename.split('.')[-1]
    rand_strings = ''.join(random.choice(string.ascii_lowercase + string.digits
                                         + string.ascii_uppercase)
                           for i in range(5))
    new_name = '{}{}.{}'.format(rand_strings, uuid4().hex, ext)

    BASE_DIR = Path(__file__).resolve(strict=True).parent.parent
    home = f'{BASE_DIR}/media/id_documents'
    new_path = os.path.join(home, new_name)

    return new_path


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
