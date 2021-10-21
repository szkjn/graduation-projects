<template>
  <div v-if="postit" class="general">
    <div v-show="showUpdateNote">
        <UpdateNote 
          @update-postit="updatePostit" 
          :getPostit="updatePostit"
          @toggleUpdate="toggleUpdateNote" 
          :postit="postit"/>
      </div>
    <div class="top">
      <h3>{{ postit.title }}</h3>
      <i v-show="!showUpdateNote" @click="toggleUpdateNote" class="fa fa-edit " ></i>
    </div>
    <p>{{ ifEmpty() ? 'Post is empty': postit.content.toString() }}</p>
    <router-link to="/">Go back</router-link>
  </div>
	<div v-else>
		<p>Loading note details...</p>
	</div>
</template>

<script>
import UpdateNote from "../components/UpdateNote";

export default {
  name: "Note",
  components: {
    UpdateNote,
  },
  props: ['id'],
  data() {
    return {
      showUpdateNote: false,
      postit: null,
			currentId: this.$route.params.id,
    };
  },
  methods: {
    toggleUpdateNote() {
      this.showUpdateNote = !this.showUpdateNote;
    },
		ifEmpty() {
			if (this.postit.content == 0 || this.postit.content == undefined) {
				return true
			} 
			console.log(this.postit.content)
		}
  },
  // computed: {
  //   getPostit() {
  //     let storage = JSON.parse(localStorage.getItem("postits"));
  //     for (let i = 0; i < storage.length; i++) {
  //       if (storage[i]["id"] == this.$route.params.id) {
  //         return storage[i];
  //       }
  //     }
  //     return "Oops. Error. No match. Swipe left !";
  //   },
  // },
  mounted() {
    fetch('http://5.135.119.239:3090/notes/' + this.currentId)
      .then(res => res.json())
      .then(data => this.postit = data.note)
      .catch(err => console.log(err.message))
  }
};
</script>

<style scoped>
* {
  background: inherit;
}
.general {
  display: flex;
  flex-direction: column;
  background: rgb(255, 245, 0);
  max-width: 500px;
  min-height: 500px;
  margin: 30px auto;
  padding: 10px 10px;
  filter: drop-shadow(5px 5px 2px #333);
  padding: 20px;
}
.top {
  display: flex;
  align-items: baseline;
  justify-content: space-between;
}
h3 {
  font-size: 2rem;
  padding-bottom: 20px;
}
i {
  font-size: 1.5rem;
  transition-duration: 0.5s;
  margin-left: 10px;
}
i:hover {
  transform: rotate(360deg);
}
p {
  font-size: 1.25rem;
  padding-bottom: 20px;
}
footer {
  padding: 20px 0;
  border-top: 2px solid #333;
}
</style>