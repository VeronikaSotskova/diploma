<template lang="pug">
NavBar(:currentPage="'model_page'" :title="entity.name")
.container
  .loader(v-if="isLoad")
    loader(
      object="#ff9633"
      color1="#ffffff"
      color2="#17fd3d"
      size="5"
      speed="2"
      bg="#343a40"
      objectbg="#999793"
      opacity="80"
      name="circular"
    )
  .row(v-else)
    .col-6
      div(v-if="entity.description || entity.business_name")
        b Описание
        p {{ entity.description || entity.business_name }}
      .tags
        b Дата-тэги:
        MultiSelectTags(
          v-model="selectTags"
          :tagsFunc="async function (query) {return await getTagsForObject({name:query})}"
        )
        br
        button.btn.btn-primary(
          @click="appendTags"
        ) Сохранить

    .col-6
      MyTagCanvas(
        v-if="tags?.length || 0 > 0"
        :lock="options.lock"
        :speed="options.speed"
        :tags="tags"
        :width="500"
        :height="400"
      )
      b(v-else) No tags


GDialog(v-model="dialogState" max-width="500px" scrollable)
  .wrapper
    .content
      .title {{ entity.name }} ({{ entity.type }})
      v-network-graph(
        v-if="nodes"
        :nodes="nodes"
        :edges="edges"
        :configs="configs"
        :event-handlers="eventHandlers"
        :selectedNodes="[currentNode,]"
      )
      p(v-else) Не найдено в DBT витрине
    .actions.max
      button(class="btn btn-outline-dark" @click="dialogState=false") Закрыть
.fab
  button.btn.btn-primary.btn-lg(@click="dialogState=true") DBT
</template>

<script>
import MyTagCanvas from "@/components/MyTagCanvas";
import NavBar from "@/components/NavBar";
import MultiSelectTags from "@/components/MultiSelectTags";

import {mapActions, mapGetters} from 'vuex'

const baseSpeed = 0.1;

export default {
  name: "ModelPage",
  components: {NavBar, MyTagCanvas, MultiSelectTags},
  data() {
    return {
      configs: {
        edge: {
          selectable: true,
          normal: {
            width: 3,
            color: "#4466cc",
            dasharray: "0",
            linecap: "butt",
            animate: false,
            animationSpeed: 50,
          },
          hover: {
            width: 4,
            color: "#3355bb",
            dasharray: "0",
            linecap: "butt",
            animate: false,
            animationSpeed: 50,
          },
          selected: {
            width: 3,
            color: "#dd8800",
            dasharray: "6",
            linecap: "round",
            animate: false,
            animationSpeed: 50,
          },
          gap: 5,
          type: "straight",
          margin: 2,
          marker: {
            source: {
              type: "none",
              width: 4,
              height: 4,
              margin: -1,
              units: "strokeWidth",
              color: null,
            },
            target: {
              type: "arrow",
              width: 4,
              height: 4,
              margin: -1,
              units: "strokeWidth",
              color: null,
            },
          },
        }
      },
      options: {shape: 'sphere', lock: '', speed: [baseSpeed, baseSpeed]},
      dialogState: false,
      selectTags: [],
      isLoad: true
    }
  },
  methods: {
    ...mapActions({
      getDependencies: ('dbt/getDependencies'),
      getTagsForObject: ('tags/getTagsForObject'),
      addTags: ('dbt/addTags')
    }),
    appendTags() {
      this.addTags({type:this.entity.type, id:this.entity.id, tags_id:this.selectTags + ''})
      this.getTagsForObject({type:this.entity.type, id:this.entity.id})
    }
  },
  mounted() {
    this.getDependencies({id: this.$route.query.id, model_type: this.$route.query.model_type}).then(
        () => {
          this.isLoad = false
          const tagsIds = this.tags.map(x => x.id);
          this.selectTags = tagsIds
        }
    )
  },
  computed: {
    ...mapGetters({
      nodes: 'dbt/nodes',
      edges: 'dbt/edges',
      currentNode: 'dbt/currentNode',
      tags: 'dbt/tags',
      entity: 'dbt/entity'
    })
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
}


.title {
  font-size: 30px;
  font-weight: 700;
  border-bottom: 1px solid rgb(179, 179, 179);
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

.fab {
  display: block;
  position: fixed;
  right: 20px;
  top: 90%;
  z-index: 999999;
  box-shadow: 0 0 10px rgba(0,0,0,0.5);
}
</style>