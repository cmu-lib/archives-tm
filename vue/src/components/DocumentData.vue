<template>
  <b-card :header="document.label" class="document-container">
    <p>{{ document.n_pages }} page(s)</p>
    <p>Created: {{ document.record.created_date_text }}</p>
    <p>Coverage: {{ document.record.coverage_text }}</p>
    <hr />
    <p class="document-fulltext">{{ document.fulltext }}</p>
  </b-card>
</template>

<script>
export default {
  name: "DocumentData",
  props: {
    document: Object
  }
};
</script>

<style>
.document-container {
}

p.document-fulltext {
  height: 500px;
  overflow-y: scroll;
}
</style>
