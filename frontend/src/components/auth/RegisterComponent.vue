<script>
/*
Форма с логином и паролем, отправляющая запрос к апи
 */
import {defineComponent} from 'vue'
import {mapActions, mapState} from "vuex";

export default defineComponent({
  name: "RegisterComponent",

  data() {
    return {
      username: '',
      password: '',
      errors: null,
    }
  },

  computed: {
    ...mapState(['server'])
  },

  methods: {
    ...mapActions(['login']),
    register() {
      this.axios.post(
          `${this.server}users/api/registration/`,
          {
            username: this.username,
            password: this.password,
          }
      ).then((response) => {
        this.login(response)
      }).catch((error) => {
        if (error.response.data) {
          if (error.response.data.username) {
            this.errors = error.response.data.username[0]
          } else if (error.response.data.password) {
            this.errors = error.response.data.password[0]
          }
        }
      })
    },
  }
})
</script>

<template>
  <div>
    <h2>Registration</h2>
    <form @submit.prevent="register">
      <div>
        <label for="username">Login:</label>
        <input type="text" id="username" v-model="username">
      </div>
      <div>
        <label for="password">Password:</label>
        <input type="password" id="password" v-model="password">
      </div>
      <p v-if="errors" style="color: red">{{ errors }}</p>
      <button type="submit">Register</button>
      <router-link to="/login">Login</router-link>
    </form>
  </div>

</template>

<style scoped>

</style>