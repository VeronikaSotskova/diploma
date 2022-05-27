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
text.label(
  @click="$emit('showDialog', c)"
  :transform="`translate(${c.x},${c.y})`"
  word-spacing="-2"
  :width="c.r*2"
  :fill="textHover ? 'rgba(123, 12, 22, 0.99)' : '#1A01CC'"
  @mouseleave="textHover=false"
  @mouseover="textHover=true"
) {{ c.data.name }}
</template>

<script>
export default {
  name: "Circle",
  emits: ["getChildren", "rightClick", "showDialog"],
  props: {
    c: Object,
    key: Number,
    color: String
  },
  data() {
    return {
      hoverClass: '',
      textHover: false
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
circle, svg {
  transition: 0.4s linear;
}

.label {
  transition: transform 0.4s linear;
  text-anchor: middle;
  text-decoration: underline;
  font-weight: 500;
  dominant-baseline: middle;
  font-size: 1.1em;
}

</style>