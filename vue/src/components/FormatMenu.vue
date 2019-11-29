<template>
  <b-form-group id="format_menu_group" label-for="format_menu_select" label="Document format">
    <b-form-select
      id="format_menu_select"
      :value="value"
      @input="$emit('input', $event)"
      :options="choices"
    />
  </b-form-group>
</template>

<script>
import { HTTP } from "../main";
export default {
  name: "FormatMenu",
  props: {
    value: {
      type: String,
      default: ""
    }
  },
  data() {
    return {
      choices: []
    };
  },
  mounted() {
    HTTP.get("/document_formats/").then(
      results => {
        this.choices = [{ value: "", text: "all formats" }].concat(
          results.data.results.map(x => {
            return { value: x.id, text: x.label };
          })
        );
      },
      error => {
        console.log(error);
      }
    );
  }
};
</script>