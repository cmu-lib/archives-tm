<template>
  <b-row>
    <b-col cols="3">
      <h1>{{ box.label }}</h1>
      <b-list-group>
        <b-list-group-item v-for="folder in box.folders" :key="folder.id">
          <Folder :folder_label="folder.label" :folder_id="folder.id" />
        </b-list-group-item>
      </b-list-group>
    </b-col>
    <b-col cols="9">
      <router-view />
    </b-col>
  </b-row>
</template>

<script>
import { HTTP } from "../main";
import Folder from "../components/Folder";
export default {
  name: "Box",
  components: {
    Folder
  },
  props: {
    box_id: String
  },
  asyncComputed: {
    box() {
      return HTTP.get("/boxes/" + this.box_id + "/").then(
        results => {
          return results.data;
        },
        error => {
          console.log(error);
        }
      );
    }
  }
};
</script>