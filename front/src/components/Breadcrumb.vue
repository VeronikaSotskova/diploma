<template lang="pug">
ol(class="breadcrumb")
  li(class="breadcrumb-item" :class="[path.length > 0 ? '' : 'active']" @click="$emit('clickMain')") Root
  li(
    v-for="pathNode in path"
    :key="pathNode.id"
    class="breadcrumb-item"
    :class="[pathNode.id === path[path.length-1].id ? 'active' : '']"
    @click="$emit('clickToNode', pathNode)"
  ) {{ pathNode.text }}
</template>

<script>
export default {
  name: "Breadcrumb",
  emits: ["clickToNode", "clickMain"],
  props: {
    path: Array,
  },
}
</script>

<style scoped>
.breadcrumb {
  padding: 0
}
.breadcrumb-item {
  font-weight: 500;
  font-size: 1.4rem;
}
.breadcrumb-item:hover {
  font-weight: 700;
}
.breadcrumb {
  margin-bottom: 5px;
  background-color: #e6e6fa;
}
</style>