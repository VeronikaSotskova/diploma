<template lang="pug">
#myCanvasContainer
  canvas#myCanvas(:width="width" :height="height")
    p Anything in here will be replaced on browsers that support the canvas element
  #tags
    a(
      v-for="tag in tags"
      :key="tag.id"
      href="#"
      style="border-radius: 12"
      :style="{'background-color': tag.color}"
      :data-weight="(tag.weight+4) * 3"
      @click="handleClick(tag)"
      :id="tag.id"
    ) {{ tag.text }}
</template>

<script>
import TagCanvas from '@/assets/js/tagcanvas';


export default {
  name: "MyTagCanvas",
  props: {
    width: {
      type: Number,
      default: 1600
    },
    height: {
      type: Number,
      default: 600
    },
    options: {
      type: Object
    },
    shape: {
      type: String,
      default: 'sphere'
    },
    lock: {
      type: String,
      default: ''
    },
    speed: {
      type: Array,
      default: () => [0.5, 0.5]
    },
    tags: {
      type: Array,
      default: () => []
    }
  },
  data() {
    return {
      canvasWidth: null,
      canvasHeight: null,
      canvasId: "myCanvas"
    }
  },
  watch: {
    data() {
      this.$nextTick(() => {
        this.reload()
      })
    },
    options: {
      handler() {
        this.update()
      }
    },
    shape() {
      this.start();
      this.setSpeed(this.speed);
    }
  },
  computed: {
    styles() {
      return {
        width: this.width,
        height: this.height
      }
    }
  },
  methods: {
    handleClick(item) {
      /**
       * 点击时触发
       * @event click
       * @param {Object} item 数据项
       */
      this.tagToFront({id: item.id});
    },
    setCanvasSize() {
      this.canvasWidth = 300
      this.canvasHeight = 300
    },
    start() {
      TagCanvas.Start(this.canvasId, 'tags', {
        // //textColour: '#ff0000',
        // outlineColour: '#2251c7',
        reverse: true,
        depth: 0.5,
        maxSpeed: 0.07,
        textColour: 'white',
        weightMode: 'size',
        weight: true,
        weightFrom: 'data-weight',
        shape: this.shape,
        textFont: 'Montserrat',
        bgRadius: 30,
        outlineRadius: 30,
        bgColour: 'tag',
        padding: 10,
        minBrightness: 0.2,
        outlineColour: 'tagbg',
        lock: this.lock
      })
    },
    pause() {
      TagCanvas.Pause(this.canvasId)
    },
    resume() {
      TagCanvas.Resume(this.canvasId)
    },
    reload() {
      TagCanvas.Reload(this.canvasId)
    },
    update() {
      TagCanvas.Update(this.canvasId)
    },
    tagToFront(options) {
      TagCanvas.TagToFront(this.canvasId, options)
    },
    rotateTag(options) {
      TagCanvas.RotateTag(this.canvasId, options)
    },
    setSpeed(speed) {
      TagCanvas.SetSpeed(this.canvasId, speed)
    }
  },
  mounted() {
    this.start();
    this.setSpeed(this.speed);
  },
  updated() {
    this.reload();
    this.setSpeed(this.speed);
  },
  beforeUnmount() {
    TagCanvas.Delete(this.canvasId)
  }
}
</script>

<style scoped>

</style>