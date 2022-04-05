<template lang="pug">
p {{ $route.params.searchText }}
p {{ tableHierarchy }}
</template>

<script>

export default {
  name: "TableTreeSearch",

  mounted() {
    this.$store.dispatch("tables/getTableHierarchy", {name: this.$route.params.searchText});
  },

  computed: {
    tableHierarchy() {
      return this.$store.getters["tables/tableHierarchy"]
    },
  }
}
</script>

<style scoped>

</style>