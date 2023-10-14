<script>
import {defineComponent} from "vue";
import {mapGetters, mapState} from "vuex";

export default defineComponent({
  name: 'AuthCheck',

  mounted() {
    this.checkAuth()
  },
  computed: {
    ...mapGetters(['headers']),
    ...mapState(['server'])
  },

  methods: {
    checkAuth() {
      this.axios.get(
          `${this.server}users/api/info/`,
          this.headers
      ).then(() => {
        this.$store.commit('authenticate')
      }).catch(() => {
        // nothing
      })
    }
  }
})
</script>

<template></template>