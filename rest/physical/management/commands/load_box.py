from django.core.management.base import BaseCommand
from physical import models
from metadata.models import Collection
from tqdm import tqdm
from glob import glob
import re
import os


class Command(BaseCommand):
    help = "Load a box into the database"

    def add_arguments(self, parser):
        parser.add_argument("box_path", nargs="+", type=str)

    def handle(self, *args, **options):
        models.Box.objects.all().delete()
        collection = Collection.objects.get_or_create(
            label="Herbert A. Simon Collection -- (1909, 1924) 1929-1998"
        )[0]
        box_path = options["box_path"][0]
        box_sequence = int(re.match(r".+/box(\d{5})", box_path).groups()[0])
        box = models.Box.objects.create(
            label=box_path, sequence=box_sequence, collection=collection
        )
        folders = os.listdir(box_path)
        for folder_path in folders:
            print(folder_path)
            folder_sequence = int(re.match(r"fld(\d{5})", folder_path).groups()[0])
            folder = models.Folder.objects.create(
                label=folder_path, sequence=folder_sequence, box=box
            )
            bundles = os.listdir(box_path + "/" + folder_path)
            for bundle_path in bundles:
                print(bundle_path)
                bundle_sequence = int(re.match(r"bdl(\d{4})", bundle_path).groups()[0])
                bundle = models.Bundle.objects.create(
                    label=bundle_path, sequence=bundle_sequence, folder=folder
                )
                documents = os.listdir(box_path + "/" + folder_path + "/" + bundle_path)
                for document_path in documents:
                    print(document_path)
                    document_sequence = int(
                        re.match(r"doc(\d{4})", document_path).groups()[0]
                    )
                    dir_base = (
                        box_path
                        + "/"
                        + folder_path
                        + "/"
                        + bundle_path
                        + "/"
                        + document_path
                        + "/"
                    )
                    try:  # skip empty document folders
                        document_pdf_path = glob(dir_base + "*.pdf")[0]
                    except:
                        continue
                    document_fulltext_path = glob(dir_base + "*.txt")[0]
                    document_fulltext = open(document_fulltext_path, "r").read()
                    document = models.Document.objects.create(
                        label=document_path,
                        sequence=document_sequence,
                        pdf=document_pdf_path,
                        fulltext=document_fulltext,
                        bundle=bundle,
                    )
                    pages = glob(dir_base + "*.tiff")
                    for page_path in pages:
                        print(page_path)
                        page_sequence = int(
                            re.match(r".+/(\d+)\.tiff", page_path).groups()[0]
                        )
                        page = models.Page.objects.create(
                            label=page_path,
                            sequence=page_sequence,
                            tiff=page_path,
                            document=document,
                        )
