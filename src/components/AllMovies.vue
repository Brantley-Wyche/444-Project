<template>
  <div class="all">
    <h1> {{msg}}</h1>
      <table align="center">
        <thead>
        <tr>
            <th>TITLE</th>
            <th>DESCRIPTION</th>
            <th>IMAGE URL</th>
            <th>YEAR</th>
            <th>DIRECTOR</th>
            <th>GENRE</th>
            <th>DURATION</th>
        </tr>
        </thead>
        <tbody>
            <tr v-for="movie in movies" :key="movie._id">
              <td>{{movie.title}}</td>
              <td>{{movie.description}}</td>
              <td>{{movie.imageUrl}}</td>
              <td>{{movie.year}}</td>
              <td>{{movie.director}}</td>
              <td>{{movie.genre}}</td>
              <td>{{movie.duration}}</td>
            </tr>
        </tbody>
      </table>
    
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'AllMovie',
  data () {
    return {
      msg: 'All Movies',
      movies: []
    }
  },
  methods: {
    getMovies() {;
      axios.get(this.$hostname)
        .then((res) => {
          console.log(res);
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
