<template>
  <b-form-group id="subject_menu_group" label-for="subject_menu_select" label="Document subject">
    <b-form-select
      id="subject_menu_select"
      :value="value"
      @input="$emit('input', $event)"
      :options="choices"
    />
  </b-form-group>
</template>

<script>
import { HTTP } from "../main";
export default {
  name: "SubjectMenu",
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
    HTTP.get("/document_subjects/").then(
      results => {
        this.choices = [{ value: "", text: "all subjects" }].concat(
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