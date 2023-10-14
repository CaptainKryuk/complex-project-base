<script>
import MenuComponent from '@/components/Menu.vue'
import AuthCheck from "@/components/auth/AuthCheck.vue";
import {defineComponent} from "vue";
import {mapState} from "vuex";

export default defineComponent({
  name: 'HomeView',
  components: {MenuComponent, AuthCheck},
  computed: mapState(['isAuthenticated'])
})
</script>

<template>
  <main>
    <AuthCheck></AuthCheck>
    <MenuComponent></MenuComponent>
  </main>
</template>
