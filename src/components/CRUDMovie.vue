<template>
  <div class="add" v-for="movie in movies">
    <h1> {{msg}}</h1>
    <p>Title: <input v-model="addMovieForm.title"></p>
    <p>Description: <input v-model="addMovieForm.description"></p>
    <p>Image URL: <input v-model="addMovieForm.imageUrl"></p>
    <p>Year: <input v-model="addMovieForm.year"></p>
    <p>Director: <input v-model="addMovieForm.director"></p>
    <p>Genre: <input v-model="addMovieForm.genre"></p>
    <p>Duration: <input v-model="addMovieForm.duration"></p>
    <button v:on-click="onSubmit($event)">Submit</button>
    <hr />
    <h1>Get a Movie</h1>
    <p>ID: <input v-model="id"></p>
    <button><router-link :to="{name: 'GetMovie', params: {id}}">Get</router-link></button>
    <hr />
    <h1>Update a Movie</h1>
    <p>ID: <input></p>
    <button v:on-click="editMovie(movie)">UPDATE</button>
    <hr />
    <h1>Delete a Movie</h1>
    <p>Title: <input></p>
    <button v:on-click="onDeleteMovie(movie)">DELETE</button>
  </div>
  
</template>

<script>
import axios from 'axios';

export default {
  name: 'AddMovie',
  data () {
    return {
      msg: 'Add a Movie',
      id: this.$route.params.id,
      movies: [],
      addMovieForm: {
        title: '',
        description: '',
        imageUrl: '',
        year: '',
        director: '',
        genre: '',
        duration: '',
      },
      editForm: {
        title: '',
        description: '',
        imageUrl: '',
        year: '',
        director: '',
        genre: '',
        duration: '',
      },
      message: '',
      showMessage: false,
    }
  },
  methods: {
    initForm() {
      this.addMovieForm.title = '';
      this.addMovieForm.description = '';
      this.addMovieForm.imageUrl = '';
      this.addMovieForm.year = '';
      this.addMovieForm.director = '';
      this.addMovieForm.genre = '';
      this.addMovieForm.duration = '';

      this.editForm.title = '';
      this.editForm.description = '';
      this.editForm.imageUrl = '';
      this.editForm.year = '';
      this.editForm.director = '';
      this.editForm.genre = '';
      this.editForm.duration = '';
    },
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
    addMovie(new_movie) {
      const path = 'http://localhost:8080/movie';
      axios.post(path, new_movie)
        .then(() => {
          this.getMovies();
          this.message = 'Movie added!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
          this.getMovies();
        });
    },
    onSubmit(event) {
      event.preventDefault();
      const info = {
        title: this.addMovieForm.title,
        description: this.addMovieForm.description,
        imageUrl: this.addMovieForm.imageUrl,
        year: this.addMovieForm.year,
        director: this.addMovieForm.director,
        genre: this.addMovieForm.genre,
        duration: this.addMovieForm.duration,
      };
      this.addMovie(info);
      this.initForm();
    },
    onSubmitUpdate(event) {
      event.preventDefault();
      const info = {
        title: this.editForm.title,
        description: this.editForm.description,
        imageUrl: this.editForm.imageUrl,
        year: this.editForm.year,
        director: this.editForm.director,
        genre: this.editForm.genre,
        duration: this.editForm.duration,
      };
      this.updateMovie(info, this.editForm.id);
    },
    updateMovie(info, movieID) {
      const path = `http://localhost:8080/movie/${movieID}`;
      axios.put(path, info)
        .then(() => {
          this.getMovies();
          this.message = 'Movie updated!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getMovies();
        });
    },
    editMovie(movie) {
      this.editForm = movie;
    },
    deleteMovie(movieID) {
      const path = `http://localhost:8080/movie/${movieID}`;
      axios.delete(path)
        .then(() => {
          this.getMovies();
          this.message = 'Book removed!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getMovies();
        });
    },
    onDeleteMovie(movie) {
      this.deleteMovie(movie.id);
    },
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
