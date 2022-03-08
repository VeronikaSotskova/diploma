<template lang="pug">
h3(v-if="pathNodes") Path: {{ pathNodes }}

svg(:height="height" :width="width")
  g
    circle(
      v-if="rootNode.data"
      :cx="rootNode.x"
      :cy="rootNode.y"
      :r="rootNode.r"
      :stroke="rootNode.data.stroke ? rootNode.data.stroke : ''"
      :fill="rootNode.data.color"
      @click="clickBehind"
    )

    Circle(
      v-for="(c, key) in domains.children"
      :key="key"
      :c="c"
      @getChildren="click(c)"
    )

</template>

<script>
import {hierarchy, pack} from 'd3-hierarchy';
import Circle from "@/components/Circle";


let d3 = {
  hierarchy: hierarchy,
  pack: pack
}

export default {
  name: "CirclePacking",
  components: {Circle},
  props: {
    margin: {
      type: Object,
      default: function () {
        return {
          top: 20,
          right: 20,
          bottom: 20,
          left: 20
        }
      }
    }
  },
  data() {
    return {
      rootNode: {},
      prevNodeId: null,
      depth: 0,
      path: []

    }
  },
  computed: {
    domains() {
      return this.pack(this.$store.getters["business_domains/domains"])
    },
    width() {
      return document.documentElement.clientWidth - this.margin.right - this.margin.left;
    },
    height() {
      return document.documentElement.clientHeight - this.margin.top - this.margin.bottom;
    },
    pathNodes() {
      return this.path.join('->')
    }
  },
  mounted() {
    this.$store.dispatch("business_domains/getDomains").then((data) => {
      this.rootNode = this.pack(data)
    });

  },
  methods: {
    click(nod) {
      if (nod.data.has_children) {
        this.$store.dispatch("business_domains/getDomains", {id: nod.data.id}).then((data) => {
          this.prevNodeId = this.rootNode.data.id
          this.rootNode = this.pack(data)
          this.depth += 1
          this.path.push(this.rootNode.data.name)
        });
      }
    },
    clickBehind() {
      if (this.depth > 1) {
        this.$store.dispatch("business_domains/getDomains", {id: this.prevNodeId}).then((data) => {
          this.rootNode = this.pack(data)
          this.prevNodeId = this.rootNode.data.id
          this.depth -= 1

        });
      } else {
        this.$store.dispatch("business_domains/getDomains").then((data) => {
          this.rootNode = this.pack(data)
          this.prevNodeId = null
          this.depth -= 1
        });
      }
      this.path.pop()
    },
    pack(domainData) {
      let hh = d3.hierarchy(domainData)
          .sum((d) => d.value)
          .sort((a, b) => b.value - a.value)
      let resp = d3.pack()
          .size([this.width, this.height])
          .padding(30)(hh)
      return resp
    }
  }
}
</script>

<style scoped>

</style>