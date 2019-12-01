<template>
  <b-container>
    <h1>Simon TM</h1>
    <p>A prototype application for document clustering in the context of archival collections.</p>
    <b-card title="Boxes">
      <b-list-group v-if="boxes">
        <b-list-group-item v-for="box in boxes" :key="box.id">
          <router-link :to="{name: 'BoxView', params: {box_id:
          box.id}}">{{ box.label }}</router-link>
        </b-list-group-item>
      </b-list-group>
    </b-card>
  </b-container>
</template>

<script>
import { HTTP } from "../main";
import Autocomplete from "../components/Autocomplete";
export default {
  name: "home",
  components: {
    Autocomplete
  },
  data() {
    return {
      doc: ""
    };
  },
  asyncComputed: {
    boxes() {
      return HTTP.get("/boxes/").then(
        response => {
          return response.data.results;
        },
        error => {
          console.log(error);
        }
      );
    }
  }
};
</script>
