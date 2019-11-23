<template>
  <div :id="id" class="osd"></div>
</template>

<script>
import OpenSeadragon from "openseadragon";

export default {
  name: "IIIFSequence",
  props: {
    id: {
      type: String,
      default: "osd-viewer"
    },
    info_urls: Array
  },
  computed: {
    options() {
      return {
        id: this.id,
        prefixUrl: "/osd/",
        tileSources: this.info_urls,
        maxZoomLevel: 3,
        sequenceMode: true,
        preserveViewport: true,
        showReferenceStrip: true,
        // Show rotation buttons
        showRotationControl: true,
        // Enable touch rotation on tactile devices
        gestureSettingsTouch: {
          pinchRotate: true
        }
      };
    }
  },
  mounted() {
    OpenSeadragon(this.options);
  },
  updated() {
    OpenSeadragon(this.options);
  }
};
</script>

<style>
.osd {
  height: 900px;
  width: 100%;
}
</style>
