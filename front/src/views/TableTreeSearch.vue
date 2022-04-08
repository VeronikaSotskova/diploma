<template lang="pug">
nav.navbar.navbar-light.bg-light
  a(@click="goToMain" role="button").btn.btn-outline-secondary Go to Main
  form.form-inline
    input.form-control.mr-sm-2(
      type="search"
      placeholder="Search"
      aria-label="Search"
      list="items"
      v-model="searchQuery"
      @keyup="submitSearch"
      @enter="goToSearchPage"
    )
    button.btn.btn-outline-success.my-2.my-sm-0(
      type="submit"
      @click="goToSearchPage"
    ) Search
    datalist#items
      option(v-for="(table, index) in tables" :value="table" :key="index")
tree(
  :nodes="nodes"
  :config="config"
)
</template>

<script>
import treeview from "vue3-treeview";
import "vue3-treeview/dist/style.css";

export default {
  name: "TableTreeSearch",

  components: {
    tree: treeview,
  },

  data() {
    return {
      nodes: {
      },
      config: {roots: []},
      searchQuery: ''
    }
  },

  computed: {
    tables() {
      return this.$store.getters["tables/tables"]
    }
  },
  mounted() {
    this.$store.dispatch("tables/getTableHierarchy", {name: this.$route.params.searchText}).then((data) => {
      this.nodes = data.nodes;
      this.config = data.config;
    });
  },
  methods: {
    goToSearchPage() {
      this.$router.push({path: `/search/${this.searchQuery}`});
    },
    submitSearch() {
      return this.$store.dispatch('tables/getTables', {q: this.searchQuery})
    },
    goToMain() {
       this.$router.push({path: '/'});
    }
  }
}
</script>

<style scoped>

</style>