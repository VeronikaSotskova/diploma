<template lang="pug">
.card.cards-block
  .card-body
    h5.card-title(@click="goToModelPage")
      | {{ obj.name }}
      |
      a.badge.badge-pill(:style="{'background-color': obj.color, 'color': 'white'}") {{ obj.type }}
    .card-tags
      a.badge.badge-pill(
        v-for="tag in obj.tags"
        :key="tag.id"
        href="#"
        style="margin-right:5px; margin-bottom: 2px; color: white"
        :style="{'background-color': tag.color, 'color': 'white'}"
      ) {{ tag.text }}
    p.card-text(v-if="obj.business_name || obj.description") {{ text }}
    button.btn.btn-link(
      v-if="(this.obj.business_name || this.obj.description || '').length > minLen"
      @click="collapse"
    ) {{ buttonText }}
</template>

<script>
export default {
  name: "ObjectCard",
  props: {
    obj: {
      type: Object,
      default: () => {
        return {
          id: 0,
          type: "domain",
          tags: [
            {
              id: 0,
              text: "My Tag",
              color: "#3a2deb"
            }
          ],
          name: "MyDomain",
          business_name: "Some desc",
          color: "#f24a4a"
        }
      }
    }
  },
  data() {
    return {
      isFull: false,
      minLen: 200
    }
  },
  methods: {
    collapse()  {
      this.isFull = !this.isFull
    },
    goToModelPage() {
      this.$router.push({path: '/model', query: {id: this.obj.id, model_type: this.obj.type}})
    }
  },
  computed: {
    text() {
      if (this.isFull || (this.obj.business_name || this.obj.description || '').length < this.minLen) {
        return (this.obj.business_name || this.obj.description || '')
      } else {
        return (this.obj.business_name || this.obj.description || '').substring(0, this.minLen) + "..."
      }
    },
    buttonText() {
      if (this.isFull) {
        return 'Скрыть'
      } else {
        return 'Подробнее'
      }
    }
  }
}
</script>

<style scoped>
.cards-block {
  margin-bottom: 10px;
}
.card-title:hover {
  color: red;
}
</style>