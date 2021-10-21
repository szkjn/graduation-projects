<template>
  <form @submit="onSubmit" class="add-form">
    <div class="top">
      <h3>Update your note</h3>
      <i @click="toggleUpdate" class="fa fa-minus"></i>
    </div>

    <div class="form-control">
      <label>Title</label>
      <input type="text" name="title" v-model="title" />
    </div>
    <div class="form-control">
      <label>Content</label>
      <textarea type="text" name="content" v-model="content"></textarea>
    </div>

    <input type="submit" value="Update !" class="btn btn-block" />
  </form>
</template>

<script>
export default {
  name: "UpdateNote",
  data() {
    return {
      showUpdateNote: true,
      title: this.postit.title,
      content: this.postit.content,
    };
  },
  props: ["postit"],
  methods: {
    toggleUpdate() {
      this.$emit("toggleUpdate");
      console.log("minus cliked");
    },
    updateNote(noteId) {
      console.log("update fn (noteId): " + noteId);
      const update = async () => {
        const res = await fetch("http://5.135.119.239:3090/notes/" + noteId, {
          method: "PUT",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({
            title: this.title,
            content: this.content,
          }),
        });
        const data = await res.json();
        console.log("update fn (data): " + JSON.stringify(data));
      };
      if (confirm("Only fools never change their mind. U fool ?")) {
        update();
      }
    },
    onSubmit(e) {
      e.preventDefault();
      console.log("on submit: " + this.postit);

      if (!this.title) {
        alert(
          "Please add a title. A sticky note without a title is like Tom Cruise without sunglasses."
        );
        return;
      } else if (!this.content) {
        alert(
          "Yo. Why on earth would you leave a sticky note without an actual note ? Try again smartass."
        );
        return;
      }

      this.updateNote(this.postit._id);

      (this.title = ""), (this.content = "");
    },
  },
};
</script>


<style scoped>
* {
  background: inherit;
}
.top {
  display: flex;
  align-items: center;
  justify-content: space-between;
}
h3 {
  font-size: 2rem;
  padding-bottom: 0px;
}
i {
  font-size: 1.5rem;
  transition-duration: 0.5s;
}
i:hover {
  transform: rotate(360deg);
}
.add-form {
  margin-bottom: 40px;
}
.form-control {
  margin: 12px 0;
}
.form-control label {
  display: block;
}
.form-control input[type="text"] {
  background: inherit;
  border: 1px solid #333;
  width: 100%;
  height: 30px;
  padding: 3px 7px;
  font-size: 17px;
}
.form-control textarea {
  border: 1px solid #333;
  width: 100%;
  height: 90px;
  padding: 3px 7px;
  font-size: 17px;
}
.form-control-check {
  display: flex;
  align-items: center;
  /* justify-content: flex-start; */
}
input[type="checkbox"] {
  margin-left: 10px;
}
input[type="submit"] {
  border: 1px solid #333;
  color: #333;
  font-size: 1.1rem;
  transition-property: background;
  transition-duration: 0.3s;
}
input[type="submit"]:hover {
  background: rgb(100, 240, 100);
}
</style>