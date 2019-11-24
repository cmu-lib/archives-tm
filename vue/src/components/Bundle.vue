<template>
  <div>
    <span>
      {{ bundle_label }}
      <b-button @click="visible=!visible" size="sm">+</b-button>
    </span>
    <b-collapse v-model="visible">
      <b-list-group v-if="bundle">
        <b-list-group-item v-for="document in bundle.documents" :key="document.id">
          <router-link
            :to="{name: 'DocumentDetailView', params: {document_id: document.id}}"
          >{{ document.label }}</router-link>
        </b-list-group-item>
      </b-list-group>
    </b-collapse>
  </div>
</template>

<script>
import { HTTP } from "../main";
export default {
  name: "bundle",
  props: {
    bundle_label: String,
    bundle_id: String
  },
  data() {
    return {
      visible: false
    };
  },
  asyncComputed: {
    bundle() {
      if (this.visible) {
        return HTTP.get("/bundles/" + this.bundle_id + "/").then(
          results => {
            return results.data;
          },
          error => {
            console.log(error);
          }
        );
      } else {
        return null;
      }
    }
  }
};
</script>