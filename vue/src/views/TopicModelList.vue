<template>
  <b-row>
    <b-col cols="3">
      <b-list-group>
        <b-list-group-item v-for="tm in topic_models" :key="tm.id">
          <TopicModelCard :tm="tm" />
        </b-list-group-item>
      </b-list-group>
    </b-col>
    <b-col cols="9">
      <b-card title="Register a topic model">
        <b-row>
          <SubjectMenu v-model="document_subject" />
          <FormatMenu v-model="document_format" />
          <p>Documents: {{ document_count }}</p>
        </b-row>
        <b-row>
          <b-form-group
            id="n_topics_group"
            label-for="n_topics_input"
            label="# of topics"
            :description="String(n_topics)"
          >
            <b-input type="range" v-model="n_topics" min="5" max="20" number />
          </b-form-group>
          <b-form-group
            id="chunksize_group"
            label-for="chunksize_input"
            label="Chunk size"
            :description="String(chunksize)"
          >
            <b-input type="range" v-model="chunksize" min="100" max="3000" step="100" number />
          </b-form-group>
          <b-form-group
            id="n_passes_group"
            label-for="n_passes_input"
            label="# of passes"
            :description="String(n_passes)"
          >
            <b-input type="range" v-model="n_passes" min="10" max="200" step="10" number />
          </b-form-group>
          <b-form-group
            id="iterations_group"
            label-for="iterations_input"
            label="# of iterations"
            :description="String(iterations)"
          >
            <b-input type="range" v-model="iterations" min="10" max="200" step="10" number />
          </b-form-group>
          <b-form-group
            id="min_count_group"
            label-for="min_count_input"
            label="Only terms appearing more than n times"
            :description="String(min_count)"
          >
            <b-input type="range" v-model="min_count" min="0" max="50" step="1" number />
          </b-form-group>
          <b-form-group
            id="no_above_group"
            label-for="no_above_input"
            label="Terms not in more than"
            :description="String(no_above * 100) + '% of documents'"
          >
            <b-input type="range" v-model="no_above" min="0" max="1" step="0.1" number />
          </b-form-group>
        </b-row>
        <b-button variant="success" @click="register_model">Submit</b-button>
      </b-card>
    </b-col>
  </b-row>
</template>

<script>
import { HTTP } from "../main";
import SubjectMenu from "../components/SubjectMenu";
import FormatMenu from "../components/FormatMenu";
import TopicModelCard from "../components/TopicModelCard";
export default {
  name: "TopicModelList",
  components: {
    SubjectMenu,
    FormatMenu,
    TopicModelCard
  },
  data() {
    return {
      document_subject: "",
      document_format: "",
      n_topics: 10,
      chunksize: 2000,
      n_passes: 20,
      iterations: 40,
      min_count: 10,
      no_above: 0.5,
      submitted_model: {},
      topic_models: []
    };
  },
  asyncComputed: {
    documents() {
      const payload = {
        params: {
          document_subject: this.document_subject,
          document_format: this.document_format
        }
      };
      return HTTP.get("/documents/", payload).then(
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
    document_count() {
      if (!!this.documents) {
        return this.documents.count;
      } else {
        return null;
      }
    }
  },
  methods: {
    refresh_topic_models() {
      HTTP.get("/topic_models/").then(
        results => {
          this.topic_models = results.data.results;
        },
        error => {
          console.log(error);
        }
      );
    },
    create_model() {
      const payload = {
        n_topics: this.n_topics,
        chunksize: this.chunksize,
        passes: this.passes,
        iterations: this.iterations,
        min_count: this.min_count,
        no_above: this.no_above
      };
      return HTTP.post("/topic_models/", payload).then(
        response => {
          return response.data;
        },
        error => {
          console.log(error);
        }
      );
    },
    load_model() {
      const docs = {
        params: {
          document_subject: this.document_subject,
          document_format: this.document_format
        }
      };
      this.create_model().then(tm => {
        HTTP.post("/topic_models/" + tm.id + "/load_model/", docs).then(
          response => {
            console.log(response);
          },
          error => {
            console.log(error);
          }
        );
      });
    },
    register_model() {
      this.load_model();
    }
  },
  created() {
    this.refresh_topic_models();
  }
};
</script>
