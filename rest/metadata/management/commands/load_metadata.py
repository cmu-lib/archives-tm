from django.core.management.base import BaseCommand
from metadata import models
from physical.models import Document
from tqdm import tqdm
from glob import glob
import re
import os
import csv


class Command(BaseCommand):
    help = "Attach document metadata"

    def add_arguments(self, parser):
        parser.add_argument("metadata_path", nargs="+", type=str)
        parser.add_argument(
            "--wipe",
            action="store_true",
            help="Wipe all existing metadata entries first",
        )

    def handle(self, *args, **options):
        models.DocumentRecord.objects.all().delete()

        def extract_num(s, n):
            return int(re.match(r".+(\d{" + str(n) + r"})$", s).groups()[0])

        with open(options["metadata_path"][0]) as csvfile:
            csv_reader = csv.DictReader(csvfile, delimiter=",")
            for row in csv_reader:
                collection = models.Collection.objects.get_or_create(
                    label=row["browse1"]
                )[0]
                doc_path = row["image_path"].split("\\")
                try:
                    print(doc_path)
                    doc_seq = extract_num(doc_path[12], 4)
                    bundle_seq = extract_num(doc_path[11], 4)
                    folder_seq = extract_num(doc_path[10], 5)
                    box_seq = extract_num(doc_path[9], 5)
                    print(doc_seq)
                    print(bundle_seq)
                    print(folder_seq)
                    print(box_seq)
                    document = Document.objects.get(
                        sequence=doc_seq,
                        bundle__sequence=bundle_seq,
                        bundle__folder__sequence=folder_seq,
                        bundle__folder__box__sequence=box_seq,
                    )
                except:
                    print(f"Skipping {doc_path}")
                    continue
                docsubject = models.DocumentSubject.objects.get_or_create(
                    label=row["browse3"]
                )[0]
                docformat = models.DocumentFormat.objects.get_or_create(
                    label=row["format"]
                )[0]
                series = models.Series.objects.get_or_create(
                    collection=collection, label=row["browse3"]
                )[0]
                document.label = row["title"]
                document.save()
                folder = document.bundle.folder
                folder.label = row["browse4"]
                folder.save()
                record_title = row["title"].split("(")[0]
                models.DocumentRecord.objects.create(
                    document=document,
                    label=record_title,
                    document_format=docformat,
                    document_subject=docsubject,
                    created_date_text=row["created_date"],
                    coverage_text=row["field14"],
                )

