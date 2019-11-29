<template>
  <div>
    <p>
      <router-link :to="{name: 'TopicModel', params: {topic_model_id: tm.id}}">{{ tm.id }}</router-link>
    </p>
    <b-row align-h="between">
      <b-col>
        <small># topics: {{ tm.n_topics }}</small>
      </b-col>
      <b-col>
        <small>Chunksize: {{ tm.chunksize }}</small>
      </b-col>
      <b-col>
        <small># passes: {{ tm.passes }}</small>
      </b-col>
    </b-row>
    <b-row align-h="between">
      <b-col>
        <small># iterations: {{ tm.iterations }}</small>
      </b-col>
      <b-col>
        <small>Min. count: {{ tm.min_count }}</small>
      </b-col>
      <b-col>
        <small>None above: {{ tm.no_above * 100}}%</small>
      </b-col>
    </b-row>
  </div>
</template>

<script>
export default {
  name: "TopicModelCard",
  props: {
    tm: Object
  }
};
</script>