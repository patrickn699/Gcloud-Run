import pandas as pd
from google.cloud import storage



def convert_to_xls(file_name,bukcet_name_d, bukcet_name_u):
    """
    Converts the file to excel format
    """
   
    download_blob(bukcet_name_d, file_name, file_name)
    
    df = pd.read_csv(file_name)
    df.to_excel(file_name[:-4]+ '.xls', index=False)
    upload_blob(bukcet_name_u, file_name[:-4]+ '.xls', 'converted'+file_name[:-4]+'.xls')
    return "Converted to excel"


def convert_to_csv(file_name,bukcet_name_d,bukcet_name_u):
    """
    Converts the file to csv format
    """
    filn = file_name[:-4] if file_name[-4:] == '.xls' else file_name[:-5]
    download_blob(bukcet_name_d, file_name, file_name)
    df = pd.read_excel(file_name)
    df.to_csv(filn+'.csv', index=False)
    upload_blob(bukcet_name_u, filn+ '.csv', 'converted'+ filn +'.csv')
    return "Converted to csv"

def upload_blob(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to the bucket."""
    # The ID of your GCS bucket
    # bucket_name = "your-bucket-name"
    # The path to your file to upload
    # source_file_name = "local/path/to/file"
    # The ID of your GCS object
    # destination_blob_name = "storage-object-name"

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

    print(
        "File {} uploaded to {}.".format(
            source_file_name, destination_blob_name
        )
    )


def download_blob(bucket_name, source_blob_name, destination_file_name):
    """Downloads a blob from the bucket."""
    # The ID of your GCS bucket
    # bucket_name = "your-bucket-name"

    # The ID of your GCS object
    # source_blob_name = "storage-object-name"

    # The path to which the file should be downloaded
    # destination_file_name = "local/path/to/file"

    storage_client = storage.Client()

    bucket = storage_client.bucket(bucket_name)

    # Construct a client side representation of a blob.
    # Note `Bucket.blob` differs from `Bucket.get_blob` as it doesn't retrieve
    # any content from Google Cloud Storage. As we don't need additional data,
    # using `Bucket.blob` is preferred here.
    blob = bucket.blob(source_blob_name)
    blob.download_to_filename(destination_file_name)

    print(
        "Downloaded storage object {} from bucket {} to local file {}.".format(
            source_blob_name, bucket_name, destination_file_name
        )
    )



def upload_blob_from_memory(bucket_name, contents, destination_blob_name):
    """Uploads a file to the bucket."""

    # The ID of your GCS bucket
    # bucket_name = "your-bucket-name"

    # The contents to upload to the file
    # contents = "these are my contents"

    # The ID of your GCS object
    # destination_blob_name = "storage-object-name"

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_string(contents)

    print(
        "{} with contents {} uploaded to {}.".format(
            destination_blob_name, contents, bucket_name
        )
    )


def create_bucket(bucket_name):
    """Creates a new bucket."""
    # bucket_name = "your-bucket-name"

    storage_client = storage.Client()
    bucket = storage_client.create_bucket(bucket_name)

    print("Bucket {} created.".format(bucket.name))
