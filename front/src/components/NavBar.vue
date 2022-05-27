<template lang="pug">
nav.nav.navbar(style="margin-bottom: 20px")
  .navbar-brand(v-if="title") {{ title }}
  .btn-group.align-items-end
    router-link.nav-link.btn.btn-outline-success(to="/" v-if="currentPage!=='main'") Go to Main
    router-link.nav-link.btn.btn-outline-success(to="/search" v-if="currentPage!=='search'") Go to Search Page
</template>

<script>
export default {
  name: "NavBar",
  props: {
    currentPage: {
      type: String,
      default: ""
    },
    title: {
      type: String,
      default: null
    }
  }
}
</script>

<style scoped>

</style>