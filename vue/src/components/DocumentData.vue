<template>
  <b-card>
    <h2>{{ document.label }}</h2>
    <p>{{ document.n_pages }} page(s)</p>
    <p>Created: {{ document.date_created_text }}</p>
    <p>Coverage: {{ document.coverage_text }}</p>
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
p.document-fulltext {
  height: 500px;
  overflow-y: scroll;
}
</style>
