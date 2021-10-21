<template>
  <form @submit.prevent="createNote" class="add-form">
    <div class="form-control">
      <label>Title</label>
      <input type="text" v-model="formData.title" name="title" />
    </div>
    <div class="form-control">
      <label>Content</label>
      <textarea type="text" v-model="formData.content" name="content"></textarea>
    </div>
    <input type="submit" value="Post it !" class="btn btn-block" />
  </form>
</template>

<script>

export default {
  name: "AddNote",
  data() {
    return {
      formData: {
        title: "",
        content: "",
      },
    };
  },
  methods: {
    createNote() {
      fetch("http://5.135.119.239:3090/notes", {
        method: "POST",
        body: JSON.stringify({
          title: this.formData.title,
          content: this.formData.content
        }),
        headers: {
          "Content-type": "application/json; charset=UTF-8",
        },
      })
        .then((res) => res.json())
        // .then(console.log(this.formData))
        .then((json) => console.log(json))
        .catch((err) => console.log(err.message))
    },
  },

  // onSubmit(e) {
  //   e.preventDefault();

  //   if (!this.title) {
  //     alert(
  //       "Please add a title. A post-it without a title is like Tom Cruise without sunglasses."
  //     );
  //     return;
  //   }

  //   const newPostit = {
  //     id: uuid(),
  //     title: this.title,
  //     content: this.content,
  //   };

  //   this.$emit("add-postit", newPostit);
  //   (this.title = ""), (this.content = "");
  // },
};
</script>


<style scoped>
* {
  background: #ddd;
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
  font-size: 1.15rem;
  transition-duration: 0.3s;
}
input[type="submit"]:hover {
  background: rgb(100, 240, 100);
}
</style>