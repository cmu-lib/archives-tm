<template>
  <div>
    <b-row>
      <b-col cols="9">
        <router-link :to="{name: 'TopicModel', params: {topic_model_id: tm.id}}">{{ tm.id }}</router-link>
        <span v-show="tm.is_calculated">READY</span>
      </b-col>
      <b-col cols="1">
        <b-button-group>
          <b-button size="sm" variant="danger" @click="$emit('delete', tm.id)">X</b-button>
          <b-button size="sm" variant="primary" @click="$emit('run', tm.id)">O</b-button>
        </b-button-group>
      </b-col>
    </b-row>
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