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
  data() {
    return { viewer: null };
  },
  computed: {
    options() {
      return {
        id: this.id,
        prefixUrl: "/osd/",
        tileSources: this.info_urls,
        maxZoomLevel: 3,
        panHorizontal: false,
        defaultZoomLevel: 1,
        minZoomLevel: 1,
        visibilityRatio: 1,
        sequenceMode: true,
        preserveViewport: false,
        showReferenceStrip: false,
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
    this.viewer = OpenSeadragon(this.options);
  },
  watch: {
    info_urls() {
      this.viewer.destroy();
      this.viewer = OpenSeadragon(this.options);
    }
  }
};
</script>

<style>
.osd {
  height: 900px;
  width: 100%;
}
</style>
