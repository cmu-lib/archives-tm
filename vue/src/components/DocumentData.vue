<template>
  <b-card>
    <h2>{{ document.label }}</h2>
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