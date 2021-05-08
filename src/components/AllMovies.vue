<template>
  <div class="all">
    <h1> {{msg}}</h1>
    
      <p v-for="movie in movies">
        {{movie.title}}
      </p>
    
  </div>
</template>

<script>
export default {
  name: 'AddMovie',
  data () {
    return {
      msg: 'All Movies',
      movies: [
        {title: 'foo'},
        {title: 'foo'},
        {title: 'foo'},
        {title: 'foo'},
        {title: 'foo'},
        {title: 'foo'},
      ]
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
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
