<template lang="pug">
circle(
  :r="c.r"
  :key="key"
  :fill="c.data.color"
  @mouseover="hoverClass=mouseInClass()"
  :class="hoverClass"
  @mouseleave="hoverClass=''"
  :cx="c.x"
  :cy="c.y"
  @click="$emit('getChildren')"
)
rect(
  :x="rectangleArea.x"
  :y="rectangleArea.y"
  :width="rectangleArea.width"
  :height="rectangleArea.height"
  fill="white"
  stroke="black"
  rx="10"
  @click="clicked = !clicked"
  @mouseover="textHover='text_hover'; hoverClass=mouseInClass()"
  @mouseleave="textHover='text'; hoverClass=mouseInClass()"
)
text(
  :key="'t_'+key"
  :x="rectangleArea.x + rectangleArea.width / 2"
  :dy="rectangleArea.y + rectangleArea.height / 2"
  dominant-baseline="middle"
  text-anchor="middle"
  :class="textHover"
  @mouseover="textHover='text_hover'; hoverClass=mouseInClass()"
  @mouseleave="textHover='text'; hoverClass=mouseInClass()"
  @click="clicked = !clicked"
) {{ c.data.name }}
text(
  v-if="clicked"
  dominant-baseline="middle"
  text-anchor="middle"
  :x="rectangleArea.x + rectangleArea.width / 2"
  :y="rectangleArea.y + rectangleArea.height + c.r / 10"
) {{ c.data.description || c.data.business_name }}
</template>

<script>
export default {
  name: "Circle",
  emits: ["getChildren"],
  props: {
    c: Object,
    key: Number
  },
  data() {
    return {
      hoverClass: '',
      textHover: 'text',
      clicked: false
    }
  },
  computed: {
    rectangleArea() {
      return this.getRect()
    }
  },
  methods: {
    mouseInClass() {
      if (this.c.data.color == '#000000') {
        return 'mousein_white';
      } else {
        return 'mousein';
      }
    },
    getRect() {
      const angle = 110
      const angX = (180-angle) / 2 * 3 + angle
      const angY = angX + angle
      const x1 = this.c.r * Math.cos(angX * (Math.PI / 180)) + this.c.x
      const y1 = this.c.r * Math.sin(angX * (Math.PI / 180)) + this.c.y

      const x2 = this.c.r * Math.cos(angY * (Math.PI / 180)) + this.c.x
      const width = Math.abs(x1-x2)
      const height = this.c.r * 1/3;
      return {
        x: x1,
        y: y1,
        height: height,
        width: width
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

.text_hover {
  background: #bfbcbc;
  fill: blue;
  text-decoration: underline;
}

.text {
  background: #bfbcbc;
  fill: black;
  text-decoration: underline;
}
</style>