<template lang="pug">
NavBar(:currentPage="'search'" :title="'Поиск'")
.container
  .row(style="margin: 5px")
    .col-3
    .col
      .btn-group(role="group")
        button.btn.btn-outline-primary(
          @click="selectType='table'"
          :class="selectType === 'table' ? 'active' : ''"
        ) Таблицы
        button.btn.btn-outline-primary(
          @click="selectType='domain'"
          :class="selectType === 'domain' ? 'active' : ''"
        ) Бизнес-домены
  .row
    .col-3(style="padding:0")
      .search-form
        h1 Поиск:
        form
          .form-group
            b Выбор тэгов:
            MultiSelectTags#select-tags(
              v-model="tagsInput"
              :tagsFunc="async function(query) { return await getTags({name: query, min: 10})}"
            )
          .form-group
            b Название:
            input.form-control.mr-sm-2#search-input(
              type="search"
              placeholder="Введите название"
              aria-label="Search"
              list="items"
              v-model="searchQuery"
            )
            datalist#items
              option(v-for="(obj, index) in hintObjects" :value="obj" :key="index")
          button.btn.btn-success(
            @click.prevent="updateSearch"
          ) Найти
    .col
      .results(v-if="searchResult[selectType] && searchResult[selectType].results && searchResult[selectType].results.length && searchResult[selectType].results.length > 0")
        p(v-html="`Общее количество: <b>${searchResult[selectType].count}</b>`")
        ObjectCard(v-for="o in searchResult[selectType].results" :key="`${o.type}-${o.id}`" :obj="o")
        nav
          ul.pagination.justify-content-center
            li.page-item.mr-2(v-if="searchResult[selectType].prev_page")
              a.btn.btn-outline-success(@click="prevPage") &lt;&lt;
            li.page-item.disabled.mr-2.ml-2
              a.page-link {{ searchResult[selectType].curr_page }} / {{ searchResult[selectType].page_count }}
            li.page-item.ml-2(v-if="searchResult[selectType].next_page")
              a.btn.btn-outline-success(@click="nextPage") >>
      p(v-else) Ничего не найдено
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
import NavBar from "@/components/NavBar";
import ObjectCard from "@/components/ObjectCard";
import MultiSelectTags from "@/components/MultiSelectTags";
import axios from 'axios'
import {api} from "../store/api";

export default {
  name: "SearchPage",
  components: {NavBar, MultiSelectTags, ObjectCard},
  data() {
    return {
      searchQuery: '',
      tagsInput: [],
      selectType: 'table',
      domainPage: 1,
      tablePage: 1,
      requestName: null
    }
  },

  computed: {
    ...mapGetters({
      hintObjects: 'search/hintObjects',
      searchResult: 'search/searchObjects'
    }),
    refactorTags() {
      return this.tagsInput + ""
    },
    totalCount() {
      return ""
    }
  },

  methods: {
    ...mapActions({
      submitSearch: ('search/getHintObjects'),
      getSearchResult: ('search/getSearchObjects'),
      getTags: ('tags/getTags')
    }),
    async hint() {
      this.cancelRequestName()
      const source = axios.CancelToken.source()
      this.requestName = { cancel: source.cancel }

      await api.get('hint_objects/', {
        params: {
          q: this.searchQuery
        },
        cancelToken: source.token
      }).then((response) => {
        this.$store.commit('search/UPDATE_HINT_OBJECTS', response.data)
        this.requestName = null
      }).catch(() => {})
    },
    nextPage() {
      if (this.selectType === 'table') {
        this.tablePage += 1
      }
      else if (this.selectType === 'domain') {
        this.domainPage += 1
      }
      this.search()
    },
    prevPage() {
      if (this.selectType === 'table') {
        this.tablePage -= 1
      }
      else if (this.selectType === 'domain') {
        this.domainPage -= 1
      }
      this.search()
    },
    search() {
      this.getSearchResult({name: this.searchQuery, tags: this.refactorTags, page_domain: this.domainPage, page_table: this.tablePage})
    },
    updateSearch() {
      this.tablePage = 1
      this.domainPage = 1
      this.search()
    },
    cancelRequestName() {
      if (this.requestName) {
        this.requestName.cancel()
      }
    }
  },
  mounted() {
    this.updateSearch()
  },
  watch: {
    searchQuery() {
      this.hint()
    }
  }
}
</script>

<style scoped>
.search-form {
  background-color: rgb(242 242 242);
  border-radius: 5px;
  padding: 10px;
  box-shadow: 2px 10px 10px rgb(0 0 0 / 33%);
}

.results{
  transition: transform 0.4s linear;
}
</style>