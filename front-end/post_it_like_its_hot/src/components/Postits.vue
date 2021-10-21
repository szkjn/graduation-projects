<template>
  <div v-if="postits.length">
    <div v-for="postit in postits" :key="postit.id">
      <Postit 
        @delete-postit="$emit('delete-postit', postit._id)" 
        :postit="postit"/>
    </div>
  </div>
  <div v-else>
    <p>Loading notes...</p>
  </div>
</template>

<script>
import Postit from './Postit'

export default {
  name: "Postits",
  props: {
    postits: Array,
  },
  components: {
      Postit
  },
  emits: ['delete-postit']
};
</script>

<style scoped>
* {
  background: #ddd;
}
</style>