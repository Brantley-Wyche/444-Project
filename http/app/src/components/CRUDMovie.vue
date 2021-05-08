<template>
  <div class="add">
    <h1> {{msg}}</h1>
    <p>Title: <input></p>
    <p>Description: <input></p>
    <p>Image URL: <input></p>
    <p>Year: <input></p>
    <p>Director: <input></p>
    <p>Genre: <input></p>
    <p>Duration: <input></p>
    <button>Submit</button>
    <hr />
    <h1>Get a Movie</h1>
    <p>Title: <input></p>
    <hr />
    <h1>Update a Movie</h1>
    <p>Title: <input></p>
    <hr />
    <h1>Delete a Movie</h1>
    <p>Title: <input></p>
  </div>
  
</template>

<script>
export default {
  name: 'AddMovie',
  data () {
    return {
      msg: 'Add a Movie',
      
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}
ul {
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
