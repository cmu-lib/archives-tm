<template>
  <div>
    <span>
      {{ folder_label }}
      <b-button @click="visible=!visible" size="sm">+</b-button>
    </span>
    <b-collapse v-model="visible">
      <b-list-group v-if="folder">
        <b-list-group-item v-for="bundle in folder.bundles" :key="bundle.id">
          <Bundle :bundle_label="bundle.label" :bundle_id="bundle.id" />
        </b-list-group-item>
      </b-list-group>
    </b-collapse>
  </div>
</template>

<script>
import { HTTP } from "../main";
import Bundle from "./Bundle";
export default {
  name: "folder",
  components: {
    Bundle
  },
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
  }
};
</script>