<template lang="pug">
GDialog(v-model="dialogState" max-width="500px" scrollable)
  .wrapper
    .content
      .title(@click="goToModelPage") {{ dialogCircle.data.name }}
      .tags(style="margin-bottom: 20px;" v-if="dialogCircle.data.tags")
        a.badge.badge-pill(
          v-for="tag in dialogCircle.data.tags"
          :key="tag.id"
          href="#"
          style="margin-right:5px; margin-bottom: 2px; color: white"
          :style="{'background-color': tag.color, 'color': 'white'}"
        ) {{ tag.text }}
      p {{ dialogCircle.data.description || dialogCircle.data.business_name }}
    .actions.max
      button(class="btn btn-outline-dark" @click="$emit('closeWindow')") Закрыть
</template>

<script>
import MultiSelectTags from "@/components/MultiSelectTags";


export default {
  name: "DialogWindow",
  components: { MultiSelectTags },
  emits: ["closeWindow"],
  props: {
    dialogState: Boolean,
    dialogCircle: Object
  },
  data() {
    return {
      tags: [
        "Tag1",
        "Tag2"
      ],
      selectTag: {}
    }
  },
  methods: {
    goToModelPage() {
      this.$router.push({path: '/model', query: {id: this.dialogCircle.data.id, model_type: this.dialogCircle.data.type}})
    }
  },
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
  text-decoration: underline;
}

.title:hover {
  color: blue
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
</style>