<template lang="pug">
nav.navbar.navbar-expand(
  aria-label="breadcrumb"
  ref="navbar_breadcrumb"
  @click="viewMenu=false"
)
  Breadcrumb(:path="path" @clickToNode="clickToNode" @clickMain="clickMain")
  .collapse.navbar-collapse(style="justify-content: flex-end;")
    ul.navbar-nav
      li.nav-item.dropdown
        a.nav-link.dropdown-toggle.btn.btn-success#dropdownMenuLink(
          role="button"
          href="#"
          data-toggle="dropdown"
          aria-haspopup="true"
          aria-expanded="false"
        ) Menu
        .dropdown-menu(aria-labelledby="dropdownMenuLink" style="left: auto; right: 5px;")
          router-link.dropdown-item(to="/search") Go to Search Page
  //.dropdown
  //  a.bth.btn-success.dropdown-toggle#dropdownMenuLink(
  //    href="#"
  //    role="button"
  //    data-toggle="dropdown"
  //    aria-haspopup="true"
  //    aria-expanded="false"
  //  ) Menu
  //  .dropdown-menu(aria-labelledby="dropdownMenuLink")
  //    router-link.dropdown-item(to="/tag_cloud") Go to Tag Cloud
  //    router-link.dropdown-item(to="/search") Go to Search Page

DialogWindow(@closeWindow="dialogState=false" :dialogState="dialogState" :dialogCircle="dialogCircle")

svg(preserveAspectRatio="none" :viewBox="`0 -10 ${width} ${height}`" @click="viewMenu=false")
  defs
    pattern(
      id="table-pattern"
      patternUnits="userSpaceOnUse"
      width="50"
      height="50"
    )
      image(
        xlink:href="data:image/svg+xml;base64,PHN2ZyB4bWxucz0naHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmcnIHdpZHRoPScxMCcgaGVpZ2h0PScxMCc+CiAgPHJlY3Qgd2lkdGg9JzEwJyBoZWlnaHQ9JzEwJyBmaWxsPSd3aGl0ZScgLz4KICA8cmVjdCB4PScwJyB5PScwJyB3aWR0aD0nMTAnIGhlaWdodD0nMScgZmlsbD0nYmxhY2snIC8+Cjwvc3ZnPg=="
        x="0"
        y="0"
        width="50"
        height="50"
      )
    mask(id="table-mask" x="0" y="0" width="1" height="1")
      rect(x="0" y="0" width="100%" height="100%" fill="url(#table-pattern)")
  g
    circle(
      v-if="rootNode.data"
      :cx="rootNode.x"
      :cy="rootNode.y"
      :r="rootNode.r"
      :stroke="rootNode.data.stroke ? rootNode.data.stroke : ''"
      :fill="rootNode.data.color"
      @click="clickBehind"
      class="mainCircle"
    )

    Circle(
      v-for="(c, key) in domains.children"
      :key="key"
      :c="c"
      @getChildren="click(c)"
      @rightClick="openMenu(c)"
      @showDialog="dialogState=true; dialogCircle=c"
      :color="c.data.color"
    )
ColorPicker(
  style="display: block;margin: 0;position: absolute; z-index: 999999;"
  tabindex="-1"
  v-if="viewMenu"
  theme="light"
  :color="colors"
  :sucker-hide="true"
  :sucker-canvas="suckerCanvas"
  :sucker-area="suckerArea"
  @changeColor="changeColor"
  v-on:blur.prevent="closeMenu"
  :style="{'top':top, 'left':left}"
  ref="colorPickerForm"
)

</template>

<script>
import {hierarchy, pack} from 'd3-hierarchy';
import Breadcrumb from "@/components/Breadcrumb";
import Circle from "@/components/Circle";
import DialogWindow from "@/components/DialogWindow";
import { ColorPicker } from 'vue-color-kit'
import 'vue-color-kit/dist/vue-color-kit.css'

let d3 = {
  hierarchy: hierarchy,
  pack: pack
}

export default {
  name: "CirclePacking",
  components: {Circle, ColorPicker, Breadcrumb, DialogWindow},
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
      path: [],
      navHeight: 0,
      viewMenu: false,
      top: '0px',
      left: '0px',
      rightClickItem: {
        id: 0,
        type: ''
      },
      colors: '',
      suckerCanvas: null,
      suckerArea: [],
      dialogState: false,
      dialogCircle: {}
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
      return document.documentElement.clientHeight - this.margin.top - this.margin.bottom - this.navHeight;
    }
  },
  mounted() {
    this.$store.dispatch("business_domains/getDomains").then((data) => {
      this.rootNode = this.pack(data)
    });
    this.navHeight =  this.$refs.navbar_breadcrumb.clientHeight;
  },
  methods: {
    clickMain() {
      this.viewMenu = false
      this.$store.dispatch("business_domains/getDomains").then((data) => {
        this.rootNode = this.pack(data)
        this.path = []
      });
    },
    click(nod) {
      this.viewMenu = false
      if (nod.data.has_children) {
        this.$store.dispatch("business_domains/getDomains", {id: nod.data.id}).then((data) => {
          this.rootNode = this.pack(data)
          this.path.push({text: this.rootNode.data.name, id: this.rootNode.data.id})
        });
      }
    },
    clickToNode(nod){
      this.viewMenu = false
      let nodeIndexPath = this.path.indexOf(nod);
      this.$store.dispatch("business_domains/getDomains", {id: nod.id}).then((data) => {
          this.rootNode = this.pack(data)
          this.path = this.path.slice(0, nodeIndexPath+1)
        });
    },
    clickBehind() {
      this.viewMenu = false
      this.path.pop()
      if (this.path.length > 0) {
        this.$store.dispatch("business_domains/getDomains", {id: this.path[this.path.length-1].id}).then((data) => {
          this.rootNode = this.pack(data)
        });
      } else {
        this.$store.dispatch("business_domains/getDomains").then((data) => {
          this.rootNode = this.pack(data)
        });
      }
    },
    pack(domainData) {
      let childrenLength = domainData.children ? domainData.children.length : 1
      let paddingCircles = childrenLength > 2 ? 5 : 20;
      let hierarchy = d3.hierarchy(domainData)
          .sum((d) => d.value)
          .sort((a, b) => b.value - a.value)
      return d3.pack()
          .size([this.width, this.height-11])
          .padding(paddingCircles)(hierarchy)
    },
    setMenu: function (top, left) {

      let largestHeight = window.innerHeight - 25;
      let largestWidth = window.innerWidth - 25;

      if (top > largestHeight) top = largestHeight;

      if (left > largestWidth) left = largestWidth;

      this.top = top + 'px';
      this.left = left + 'px';
    },

    closeMenu: function () {
      this.viewMenu = false;
    },

    openMenu(c) {
      this.colors = c.data.color
      this.viewMenu = true;
      this.setMenu(event.pageY, event.pageX)
      this.rightClickItem.id = c.data.id
      this.rightClickItem.type = c.data.type
      this.$refs.colorPickerForm.$el.focus = true
    },

    changeColor(color) {
      this.colors = color
      let pos = this.domains.children.findIndex(
          el => `${el.data.type}_${el.data.id}` === `${this.rightClickItem.type}_${this.rightClickItem.id}`
      )
      this.domains.children[pos].data.color = this.colors.hex
      this.$store.dispatch(
          "business_domains/changeColor",
          {type: this.rightClickItem.type, id: this.rightClickItem.id, color: this.colors.hex}
      )
    }
  }
}
</script>

<style scoped>

.mainCircle {
  fill-opacity: .5;
}
</style>