<template>
  <b-container>
    <h1>Simon TM</h1>
    <p>A prototype application for document clustering in teh context of archival collections.</p>
    <b-card title="Boxes">
      <b-list-group>
        <b-list-group-item v-for="box in boxes" :key="box.id">
          <router-link :href="box.id">{{ box.label }}</router-link>
        </b-list-group-item>
      </b-list-group>
    </b-card>
  </b-container>
</template>

<script>
import { HTTP } from "../main";
export default {
  name: "home",
  asyncComputed: {
    boxes() {
      HTTP.get("boxes/").then(
        response => {
          return response.data;
        },
        error => {
          console.log(error);
        }
      );
    }
  }
};
</script>
