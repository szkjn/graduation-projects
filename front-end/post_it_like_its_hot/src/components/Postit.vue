<template>
  <div class="postit">
    <div class="between">
      <h3>{{ postit.title }}</h3>
      <i @click="onDelete(postit._id)" class="fas fa-times"></i>
    </div>
    <div class="between">
      <p>{{ postit.content.toString() }}</p>
      <router-link :to="{ name: 'Note', params: { id: postit._id } }">
        <i class="fas fa-angle-double-right"></i>
      </router-link>
    </div>
  </div>
</template>

<script>
export default {
  name: "Postit",
  props: {
    postit: Object,
  },
  methods: {
    onDelete(id) {
      this.$emit("delete-postit", id);
    },
  },
};
</script>

<style scoped>
* {
  background: rgb(255, 245, 0);
}
.postit {
  background: rgb(255, 245, 0);
  border-radius: 2%;
  margin: 10px 0;
  padding: 10px 10px;
  filter: drop-shadow(5px 5px 2px #333);
  transition-duration: 0.1s;
}
.postit:hover {
  filter: drop-shadow(8px 8px 2px #333);
  transform: translate(-1px, -1px);
}
h3 {
  user-select: none;
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
}
/* .urgent {
  border-left: 10px solid #333;
} */
.between {
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.fa-times {
  background: #333;
  color: rgb(255, 245, 0);
  border-radius: 10%;
  padding: 7px 9px;
  width: 30px;
  height: 30px;
  margin-bottom: 8px;
  transition-duration: 0.1s;
}
.fa-times:hover {
  background: red;
  color: #fff;
  cursor: pointer;
}
.bottom {
  display: flex;
  justify-content: flex-start;
  align-items: center;
  width: 85%;
}
p {
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
  /* user-select: none; */
}
.fa-angle-double-right {
  box-sizing: border-box;
  background: rgb(255, 245, 0);
  padding: 6px 7px;
  width: 30px;
  height: 30px;
  border-radius: 10%;
  border: 1px solid #333;
  margin-left: 12px;
  transition-duration: 0.1s;
}
.fa-angle-double-right:hover {
  background: rgb(100, 240, 100);
  border: 1px solid rgb(100, 240, 100);
  color: #fff;
}
</style>