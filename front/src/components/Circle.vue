<template lang="pug">
circle(
  :r="c.r"
  :key="key"
  :fill="color"
  @mouseover="hoverClass=mouseInClass()"
  :class="hoverClass"
  @mouseleave="hoverClass=''"
  :cx="c.x"
  :cy="c.y"
  background-color="blue"
  @click="$emit('getChildren')"
  :mask="c.data.type === 'table' ? 'url(#table-mask)' : ''"
  @contextmenu.prevent="$emit('rightClick')"
)
</template>

<script>
export default {
  name: "Circle",
  emits: ["getChildren", "rightClick"],
  props: {
    c: Object,
    key: Number,
    color: String
  },
  data() {
    return {
      hoverClass: '',
    }
  },
  methods: {
    mouseInClass() {
      if (this.c.data.color == '#000000') {
        return 'mousein_white';
      } else {
        return 'mousein';
      }
    }
  }
}
</script>

<style scoped>
.mousein {
  stroke: #000;
  stroke-width: 2;
}

.mousein_white {
  stroke: #f3d575;
  stroke-width: 2;
}

</style>