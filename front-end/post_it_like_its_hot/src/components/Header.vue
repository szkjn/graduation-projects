<template>
  <header>
    <router-link to="/" class="link"><h1>{{ title }}</h1></router-link>
    <Button
      @toggle-addNote="$emit('toggle-addNote')"
      v-show="homePage"
      text="+"
      color="#ddd"
    />
  </header>
</template>

<script>
import Button from "./Button";

export default {
  name: "Header",
  props: {
    title: String,
  },
  components: {
    Button,
  },
  computed: {
    homePage() {
      if (this.$route.path === "/") {
        return true;
      } else {
        return false;
      }
    },
  },
};
</script>

<style scoped>
* {
  background: #ddd;
}
header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin: 20px auto;
  font-family: monospace;
}
h1 {
  font-family: "Poppins", sans-serif;
  text-transform: uppercase;
  letter-spacing: 0.1rem;
}
.link {
  text-decoration: none;
}
.btn {
  width: 40px;
  padding: 0;
  margin: 0;
  color: #333;
  font-size: 2rem;
  border: 1px solid #333;
  transition-property: transform, border;
  transition-duration: 0.5s;
}
.btn:hover {
  transform: rotate(180deg);
  border: 1px solid #333;
}
.btn:active {
    border: 1px dashed #333;
}
</style>