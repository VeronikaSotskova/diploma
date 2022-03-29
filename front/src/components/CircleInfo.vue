<template lang="pug">
foreignObject(
    :x="rectangleArea.x"
    :y="rectangleArea.y"
    :width="rectangleArea.width"
    :height="isClicked ? rectangleArea.height : (rectangleArea.height-marginDiv)/4"
)
  div(
    :style="{width: `${rectangleArea.width}px`, maxHeight:`${(rectangleArea.height-marginDiv)/4}px`}"
    class="circleTitle btn btn-secondary card-title"
    @click="show"
  )
    p(
      class="circleTitleText"
    ) {{ circle.data.name }}
  div(
    v-if="isClicked && (circle.data.description || circle.data.business_name)"
    :style="{width: `${rectangleArea.width}px`, maxHeight: `${(rectangleArea.height-marginDiv)/4 * 3}px`}"
    class="circleDescription card-body"
    @click="isClicked=false"
  )
    p(class="card-text") {{ circle.data.description || circle.data.business_name }}
</template>

<script>
export default {
  name: "CircleInfo",
  props: {
    circle: Object
  },
  data() {
    return {
      isClicked: false,
      marginDiv: 10,
    }
  },
  computed: {
    rectangleArea() {
      return this.getRect(this.circle)
    }
  },
  methods: {
    show() {
      this.isClicked = !this.isClicked
    },
    getRect(c) {
      const angle = 90
      const angX = (180 - angle) / 2 * 3 + angle
      const angY = angX + angle
      const x1 = c.r * Math.cos(angX * (Math.PI / 180)) + c.x
      const y1 = c.r * Math.sin(angX * (Math.PI / 180)) + c.y

      const x2 = c.r * Math.cos(angY * (Math.PI / 180)) + c.x
      const y2 = c.r * Math.sin((angX - 180 + angle) * (Math.PI / 180)) + c.y
      const width = Math.abs(x1 - x2)
      const height = Math.abs(y1 - y2)
      return {
        x: x1 + 2,
        y: y1 + 5,
        height: height - 10,
        width: width - 4
      }
    }
  }
}
</script>

<style scoped lang="scss">
.circleTitleText {
  text-align: center;
  margin: 0;
  padding: 0;
}

.circleTitle {
  font-size: 15px;
  font-weight: 600;
  //line-height: 20px;
  text-align:center;
  white-space: pre-wrap;
  display: block;
  overflow-y: auto;
  overflow-x: hidden;
  word-break:break-all;
  -webkit-overflow-scrolling: touch;
}

/*.circleTitle:hover {*/
/*    outline: 2px solid #000; !* Чёрная рамка *!*/
/*}*/

.circleDescription {
  font-size: 12px;
  background: white;
  //line-height: 20px;
  text-align:center;
  color: black;
  //white-space: pre-wrap;
  overflow-y: auto;
  overflow-x: hidden;
  margin-top: 10px;
  //word-break:break-all;
  -webkit-overflow-scrolling: touch;
}

//.circleDescription::-webkit-scrollbar, .circleTitle::-webkit-scrollbar {
//  width: 10px;
//  background-color: #f9f9fd;
//}
.circleDescription, .circleTitle {
      overflow: auto;
      -ms-overflow-style: none;
      scrollbar-width: none;
}

.circleDescription::-webkit-scrollbar, .circleTitle::-webkit-scrollbar {
      width: 0;
      height: 0;
}

//.circleDescription::-webkit-scrollbar-thumb, .circleTitle::-webkit-scrollbar-thumb {
//  border-radius: 10px;
//  background-color: #505a5a;
//}
//
//.circleDescription::-webkit-scrollbar-track, .circleTitle::-webkit-scrollbar-track {
//  -webkit-box-shadow: inset 0 0 6px rgba(0,0,0,0.2);
//  border-radius: 10px;
//  background-color: #f9f9fd;
//}

foreignObject {
  transition: 0.4s linear;
}
</style>