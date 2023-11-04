import os
from dotenv import load_dotenv
from azure.ai.formrecognizer import DocumentAnalysisClient
from azure.core.credentials import AzureKeyCredential

load_dotenv()
env = os.environ

key = env.get('DOC_AI_KEY')
endpoint = env.get('DOC_AI_ENDPOINT')


def analyse_passport():
    identityUrl = ("https://cs210032002b1ac1664.blob.core.windows.net/"
                   "user-ids/Current Passport.pdf")

    document_analysis_client = DocumentAnalysisClient(
        endpoint=endpoint, credential=AzureKeyCredential(key)
    )

    poller = document_analysis_client.begin_analyze_document_from_url(
        "prebuilt-idDocument", identityUrl
    )
    id_documents = poller.result()

    for idx, id_document in enumerate(id_documents.documents):
        first_name = id_document.fields.get("FirstName")
        f_name = {}
        if first_name:
            f_name = {
                'value': first_name.value,
                'score': first_name.confidence
            }

        last_name = id_document.fields.get("LastName")
        l_name = {}
        if last_name:
            l_name = {
                'value': last_name.value,
                'score': last_name.confidence
            }

        document_number = id_document.fields.get("DocumentNumber")
        doc_num = {}
        if document_number:
            doc_num = {
                'value': document_number.value,
                'score': document_number.confidence
            }

        dob = id_document.fields.get("DateOfBirth")
        d_o_b = {}
        if dob:
            d_o_b = {
                'value': dob.value,
                'score': dob.confidence
            }

        doe = id_document.fields.get("DateOfExpiration")
        d_o_e = {}
        if doe:
            d_o_e = {
                'value': doe.value,
                'score': doe.confidence
            }

        sex = id_document.fields.get("Sex")
        sex_ = {}
        if sex:
            sex_ = {
                'value': sex.value,
                'score': sex.confidence
            }

        address = id_document.fields.get("Address")
        address_ = {}
        if address:
            address_ = {
                'value': address.value,
                'score': address.confidence
            }

        country_region = id_document.fields.get("CountryRegion")
        country = {}
        if country_region:
            country = {
                'value': country_region.value,
                'score': country_region.confidence
            }

        region = id_document.fields.get("Region")
        region_ = {}
        if region:
            region_ = {
                'value': region.value,
                'score': region.confidence
            }

        send = {
            'First_Name': f_name,
            'Last_Name': l_name,
            'Document_Number': doc_num,
            'DOB': d_o_b,
            'DOE': d_o_e,
            'Sex': sex_,
            'Address': address_,
            'Country': country,
            'Region': region_
        }
        # return send
        print(send)


analyse_passport()
