<template>
  <div>
    <span>
      <b-button @click="visible=!visible" size="sm">{{ sigil }}</b-button>
      {{ folder_label }}
    </span>
    <b-collapse v-model="visible">
      <b-list-group v-if="folder" flush>
        <b-list-group-item v-for="document in documents" :key="document.id">
          <router-link
            :to="{name: 'DocumentDetailView', params: {document_id: document.id}}"
          >{{ document.record.label }}</router-link>
        </b-list-group-item>
      </b-list-group>
    </b-collapse>
  </div>
</template>

<script>
import { HTTP } from "../main";
export default {
  name: "folder",
  props: {
    folder_label: String,
    folder_id: String
  },
  data() {
    return {
      visible: false
    };
  },
  asyncComputed: {
    folder() {
      if (this.visible) {
        return HTTP.get("/folders/" + this.folder_id + "/").then(
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
  },
  computed: {
    sigil() {
      if (this.visible) {
        return "-";
      } else {
        return "+";
      }
    },
    documents() {
      // Create a flat list of all the documents in the folder, bypassing the bundle hierarchy
      return this.folder.bundles.map(x => x.documents).flat(Infinity);
    }
  }
};
</script>