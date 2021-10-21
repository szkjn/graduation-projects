<template>
  <div>
    <div v-show="showAddNote">
      <AddNote @add-postit="addPostit" />
    </div>
    <Postits @delete-postit="deleteNote" :postits="postits" />
  </div>
</template>

<script>
import Postits from "../components/Postits";
import AddNote from "../components/AddNote";

export default {
  name: "Home",
  components: {
    Postits,
    AddNote,
  },
  props: ["showAddNote"],
  data() {
    return {
      postits: [],
    };
  },
  methods: {
    addPostit(postit) {
      this.postits = [...this.postits, postit];
    },
    // deletePostit(id) {
    //   if (confirm("U sure about that, sailor ?")) {
    //     this.postits = this.postits.filter((postit) => postit.id !== id);
    //   }
    // },
    deleteNote(noteId) {
      const toDelete = { id: noteId };
      console.log(noteId);
      const del = async () => {
        const res = await fetch("http://5.135.119.239:3090/notes/" + noteId, {
          method: "DELETE",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(toDelete),
        });
        const data = await res.json();
        console.log(data);
      };
      if (confirm("U sure about that, sailor ?")) {
        del();
      }
    },
  },
  async mounted() {
    const response = await fetch("http://5.135.119.239:3090/notes");
    const data = await response.json();
    this.postits = data.notes
  },
  // mounted() {
  //   fetch("http://5.135.119.239:3090/notes")
  //     .then((res) => res.json())
  //     .then((data) => (this.postits = data.notes))
  //     .catch((err) => console.log(err.message));
  // },


  //---------------------- data population 002 : localStorage ----------------------------
  // mounted() {
  //   console.log("App Mounted");
  //   if (localStorage.getItem("postits"))
  //     this.postits = JSON.parse(localStorage.getItem("postits"));
  // },
  // watch: {
  //   postits: {
  //     handler() {
  //       console.log("Postits array changed");
  // localStorage.setItem("postits", JSON.stringify(this.postits));
  //     },
  //     deep: true,
  //   },
  // },
  //----------------------- data population 001 : hardcoding ----------------------------
  // created() {
  //   this.postits = [
  //     {
  //       id: 1,
  //       title: "Coding Mantras",
  //       content:
  //         "Stay calm. Learn methodically. Be grateful for what you know already.",
  //       urgent: true,
  //     },
  //     {
  //       id: 2,
  //       title: "TO-DOs (arts)",
  //       content:
  //         "Moodboard Jimmy Q mv. VVV footage. Concept Exiles party. Stems Maury111.",
  //       urgent: true,
  //     },
  //     {
  //       id: 3,
  //       title: "TO-DOs (other)",
  //       content:
  //         "Eat. Do laundry. Shower. Take a break. Jog. Meditate. Get drunk. Buy ice cream.",
  //       urgent: false,
  //     },
  //   ];
  // },
};
</script>


<style scoped>
* {
  background: inherit;
}
</style>