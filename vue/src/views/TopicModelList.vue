<template>
  <b-list-group>
    <b-list-group-item v-for="tm in topic_models" :key="tm.id">
      <router-link :to="{name: 'TopicModel', params: {topic_model_id: tm.id}}">{{ tm.id }}</router-link>
    </b-list-group-item>
  </b-list-group>
</template>

<script>
import { HTTP } from "../main";
export default {
  name: "TopicModelList",
  asyncComputed: {
    topic_models() {
      return HTTP.get("/topic_models/").then(
        results => {
          return results.data.results;
        },
        error => {
          console.log(error);
        }
      );
    }
  }
};
</script>
