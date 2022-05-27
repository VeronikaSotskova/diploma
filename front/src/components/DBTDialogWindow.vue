<template lang="pug">
GDialog(v-model="dialogState" max-width="500px" scrollable)
  .wrapper
    .content
      .title {{ dialogCircle.data.name }}
      .tags(style="margin-bottom: 20px;" v-if="dialogCircle.data.tags")
        //CustomMultiSelect.badge.badge-pill(
        //  :objectType="dialogCircle.data.type"
        //  :objectId="dialogCircle.data.id"
        //)
        a.badge.badge-pill(
          v-for="tag in dialogCircle.data.tags"
          :key="tag.id"
          href="#"
          style="margin-right:5px; margin-bottom: 2px; color: white"
          :style="{'background-color': tag.color, 'color': 'white'}"
        ) {{ tag.text }}
      p {{ dialogCircle.data.description || dialogCircle.data.business_name }}
    .actions.max
      button(class="btn btn-outline-dark" @click="$emit('closeWindow')") Close
</template>


<script>
export default {
  name: "DBTDialogWindow",
  emits: ["closeWindow"],
  props: {
    dialogState: Boolean,
    dialogCircle: Object
  },
}
</script>

<style scoped>

</style>