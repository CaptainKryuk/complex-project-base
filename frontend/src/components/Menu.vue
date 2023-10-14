<script>
import { defineComponent } from 'vue'
import {mapMutations, mapState} from "vuex";

export default defineComponent({
  name: "MenuComponent",
  computed: mapState(['isAuthenticated']),

  methods: mapMutations(['logout'])
})
</script>

<template>
  <div style="display: flex; justify-content: space-between">
    <div>
      <router-link to="/">Home</router-link>
    </div>
    <div class="menu" style="display: flex; gap: 10px" v-if="!isAuthenticated">
      <router-link to="/login">Login</router-link>
      <router-link to="/registration">Register</router-link>
    </div>
    <div v-else>
      <button @click="logout">Logout</button>
    </div>
  </div>

</template>
