<template>
  <b-container fluid v-if="document">
    <b-row>
      <b-col cols="3">
        <DocumentData :document="document" />
      </b-col>
      <b-col cols="9">
        <IIIFSequence :id="document_id + 'image'" :info_urls="page_urls" />
      </b-col>
    </b-row>
  </b-container>
</template>

<script>
import { HTTP } from "../main";
import DocumentData from "../components/DocumentData";
import IIIFSequence from "../components/IIIFSequence";
export default {
  name: "Document",
  components: {
    DocumentData,
    IIIFSequence
  },
  props: {
    document_id: String
  },
  asyncComputed: {
    document() {
      return HTTP.get("/documents/" + this.document_id + "/").then(
        results => {
          return results.data;
        },
        error => {
          console.log(error);
        }
      );
    }
  },
  computed: {
    page_urls() {
      return this.document.pages.map(x => x.image.info);
    }
  }
};
</script>
