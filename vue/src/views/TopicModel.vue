<template>
  <b-container fluid>
    <b-row>
      <b-col cols="6">
        <b-card title="Topics" no-body>
          <b-list-group flush>
            <b-list-group-item
              button
              v-for="topic in topics"
              :key="topic.id"
              :selected="topic.id==selected_topic_id"
              @click="selected_topic_id=topic.id"
            >
              <p>{{ topic.id }}</p>
              <p>{{ terms_format(topic.terms) }}</p>
            </b-list-group-item>
          </b-list-group>
        </b-card>
      </b-col>
      <b-col cols="6">
        <b-card title="Documents">
          <b-list-group flush>
            <b-list-group-item
              v-for="rel in documents"
              :key="rel.document.id"
              :selected="rel.document.id==selected_document_id"
              @click="selected_document_id=rel.document.id"
            >
              <b-media>
                <template v-slot:aside v-if="rel.document.first_page">
                  <b-img
                    :src="rel.document.first_page.image.thumbnail"
                    width="100"
                    alt="first document page"
                  ></b-img>
                </template>
                <router-link
                  :to="'/boxes/' + rel.document.box + '/documents/' + rel.document.id"
                >{{ rel.document.label }}</router-link>
              </b-media>
            </b-list-group-item>
          </b-list-group>
        </b-card>
      </b-col>
    </b-row>
  </b-container>
</template>

<script>
import { HTTP } from "../main";
export default {
  name: "TopicModel",
  props: {
    topic_model_id: String
  },
  data() {
    return {
      selected_topic_id: null,
      selected_document_id: null
    };
  },
  computed: {
    topics_filter_params() {
      var base = { params: { topic_model: this.topic_model_id } };
      return base;
    },
    documents_filter_params() {
      var base = { params: { topic_model: this.topic_model_id, limit: 10 } };
      if (!!this.selected_topic_id) {
        base.params.topic = this.selected_topic_id;
      }
      return base;
    }
  },
  asyncComputed: {
    topic_model() {
      return HTTP.get("/topic_models/" + this.topic_model_id + "/").then(
        results => {
          return results.data;
        },
        error => {
          console.log(error);
        }
      );
    },
    topics() {
      return HTTP.get("/topics/", this.topics_filter_params).then(
        results => {
          return results.data.results;
        },
        error => {
          console.log(error);
        }
      );
    },
    documents() {
      if (!!this.selected_topic_id) {
        return HTTP.get(
          "/document_topic_relations/",
          this.documents_filter_params
        ).then(
          results => {
            return results.data.results;
          },
          error => {
            console.log(error);
          }
        );
      } else {
        return [];
      }
    }
  },
  methods: {
    terms_format: function(terms) {
      return terms.join(", ");
    }
  }
};
</script>

<style lang="css">
.selected {
  color: lightskyblue;
}
</style>