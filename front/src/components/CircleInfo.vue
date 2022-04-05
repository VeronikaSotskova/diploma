<template lang="pug">
foreignObject(
    :x="rectangleArea.x"
    :y="rectangleArea.y"
    :width="rectangleArea.width"
    height="1"
)
  GDialog(v-model="dialogState" max-width="500px" scrollable)
    .wrapper
      .content
        .title {{ circle.data.name }}
        p {{ circle.data.description || circle.data.business_name }}
      .actions.max
        button(class="btn btn-outline-dark" @click="dialogState = false") Close
  div(
    :style="{width: `${rectangleArea.width}px`, maxHeight:`${rectangleArea.height/2}px`}"
    class="circleTitle btn btn-secondary card-title"
    @click="dialogState = true"
    xmlns="http://www.w3.org/2000/xmlns/"
  )
    p(
      class="circleTitleText"
      :style="{fontSize: fontSizeTitle}"
    ) {{ circle.data.name }}
</template>

<script>
export default {
  name: "CircleInfo",
  props: {
    circle: Object
  },
  data() {
    return {
      dialogState: false,
    }
  },
  computed: {
    rectangleArea() {
      return this.getRect(this.circle)
    },
    fontSizeTitle() {
      if (this.rectangleArea.width < 35) {
        return "0.6vmin";
      } else if (this.rectangleArea.width < 40) {
        return "0.7vmin";
      } else if (this.rectangleArea.height < 45) {
        return "0.8vmin"
      } else if (this.rectangleArea.height < 49){
        return "0.9vmin"
      } else if (this.rectangleArea.height < 54){
        return "1vmin"
      } else if (this.rectangleArea.height < 59){
        return "1.1vmin"
      } else if (this.rectangleArea.height < 63){
        return "1.2vmin"
      } else if (this.rectangleArea.height < 68){
        return "1.3vmin"
      } else if (this.rectangleArea.height < 73){
        return "1.4vmin"
      } else if (this.rectangleArea.height < 77){
        return "1.5vmin"
      } else if (this.rectangleArea.height < 82){
        return "1.6vmin"
      } else if (this.rectangleArea.height < 87){
        return "1.7vmin"
      } else if (this.rectangleArea.height < 91){
        return "1.8vmin"
      } else if (this.rectangleArea.height < 96){
        return "1.9vmin"
      } else if (this.rectangleArea.height < 101){
        return "2vmin"
      } else if (this.rectangleArea.height < 105){
        return "2.1vmin"
      } else if (this.rectangleArea.height < 110){
        return "2.2vmin"
      } else if (this.rectangleArea.height < 115){
        return "2.3vmin"
      } else if (this.rectangleArea.height < 119){
        return "2.4vmin"
      } else {
        return "2.5vmin"
      }

    }
  },
  methods: {
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

<style scoped>

.wrapper {
  color: #000;
  display: flex;
  flex-direction: column;
  flex: 1;
}

.content {
  padding: 20px;
  white-space: pre-wrap;
  word-break:break-all;
  overflow: auto;
}

.title {
  font-size: 30px;
  font-weight: 700;
  margin-bottom: 20px;
}

.actions {
  padding: 10px 20px;
  border-top: 1px solid rgb(179, 179, 179);
  display: block;
}
/* Растягиваем второй блок на максимальнуцю ширину */
.actions.max {
  flex: 1;
}

.circleTitleText {
  text-align: center;
  margin: 0;
  padding: 0;
  font-size: 2vmin;
}

.circleTitle {
  font-weight: 600;
  text-align:center;
  white-space: pre-wrap;
  display: block;
  overflow-y: auto;
  overflow-x: hidden;
  word-break:break-all;
  -webkit-overflow-scrolling: touch;
  padding: 0;
  margin: 0;
  -ms-overflow-style: none;
  position: fixed;
}

.circleTitle::-webkit-scrollbar {
  width: 0;
  height: 0;
}

foreignObject {
  transition: 0.4s linear;
  overflow: visible;
}
</style>