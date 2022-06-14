<template lang="pug">
Multiselect(
  :options="tagsFunc"
  :label="'text'"
  :valueProp="'id'"
  :filter-results="false"
  :min-chars="0"
  :resolve-on-load="true"
  :delay="0"
  :close-on-select="false"
  :searchable="true"
  :noOptionsText="'Ничего не найдено'"
  :noResultsText="'Ничего не найдено'"
  v-model="inputVal"
  mode="tags"
  placeholder="Выберите тэги"
)
  template(v-slot:tag="{ option, handleTagRemove, disabled }")
    .multiselect-tag(:style="{'background': option.color}") {{ option.text }}
      span.multiselect-tag-remove(
        v-if="!disabled"
        @mousedown.prevent="handleTagRemove(option, $event)"
      )
        span.multiselect-tag-remove-icon
</template>

<script>
import Multiselect from '@vueform/multiselect'

export default {
  name: "MultiSelectTags",
  components: {
    Multiselect
  },
  props: {
    value: {
      type: Array,
      default: () => []
    },
    tagsFunc: {
      type: Function,
    }

  },
  computed: {
    inputVal: {
      get() {
        return this.value;
      },
      set(val) {
        this.$emit('input', val);
      }
    }
  }
}
</script>

<style src="@vueform/multiselect/themes/default.css"></style>