<template>
  <div class="getmovie">
    <h1>{{ msg }}</h1>
    <table align="center">
        <thead>
        <tr>
            <th>ID</th>
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
              <td>{{movie.id}}</td>
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
  name: 'GetMovie',
  data () {
    return {
      msg: 'Movie Info',
      movies: [],
    }
  },
  methods: {
      loggy(){
          console.log(this.$route.params.id);
      },
      getMovie(movieID) {
      const path = `${this.$hostname}/movie/${movieID}`;
      axios.get(path)
        .then((res) => {
          console.log(res);
          this.movies = res.data;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  created() {
      this.getMovie(this.$route.params.id);
      this.loggy();
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
  margin-bottom: 15px;
}
a {
  color: #42b983;
}
</style>
