<template>
  <div class="container">
    <Header 
      @toggle-addNote="toggleAddNote" title="Post it like it's hot" />
    <router-view :showAddNote="showAddNote"></router-view>
    <Footer />
  </div>
</template>



<script>
import Header from "./components/Header"
import Footer from "./components/Footer"

export default {
  name: "App",
  components: {
    Header,
    Footer,
  },
  data() {
    return {
      showAddNote: false,
    };
  },
  methods: {
    toggleAddNote() {
      this.showAddNote = !this.showAddNote
    }
  },
};
</script>



<style>
@import url("https://fonts.googleapis.com/css2?family=Poppins:wght@300;400&display=swap");
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
  color: #333;
  background: #333;
}
a {
    color: #333;
}
a:hover {
  font-weight: bold;
}
body {
  font-family: "Poppins", sans-serif;
}
.container {
  margin: 30px auto;
  overflow: auto;
  border: 1px solid steelblue;
  padding: 10px 30px;
  border-radius: 5px;
  width: 90vw;
  height: auto;
  max-width: 800px;
  background: #ddd;
}
.btn {
  display: inline-block;
  background: #333;
  color: #ddd;
  border: none;
  padding: 10px 20px;
  margin: 5px 0;
  border-radius: 5px;
  cursor: pointer;
  text-decoration: none;
  font-size: 15px;
  font-family: inherit;
  text-transform: uppercase;
}
.btn:focus {
  outline: none;
}
.btn:active {
  transform: scale(0.98);
}
.btn-block {
  display: block;
  width: 100%;
}
</style>
