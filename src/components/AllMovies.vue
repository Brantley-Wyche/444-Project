<template>
  <div class="all">
    <h1> {{msg}}</h1>
      <table>
        <thead>
        <tr>
            <th>TITLE</th>
            <th>DESCRIPTION</th>
            <th>YEAR</th>
            <th>DIRECTOR</th>
            <th>GENRE</th>
            <th>DURATION</th>
        </tr>
        </thead>
        <tbody>
            
        </tbody>
      </table>
    
  </div>
</template>

<script>
export default {
  name: 'AllMovie',
  data () {
    return {
      msg: 'All Movies',
      movies: []
    }
  },
  methods: {
    getMovies() {
      const path = 'http://localhost:8080/movies';
      axios.get(path)
        .then((res) => {
          this.movies = res.data.movies;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  created() {
    this.getMovies();
  },
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
