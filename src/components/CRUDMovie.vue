<template>
  <div class="add">
    <h1> {{msg}}</h1>
    <div>

      <!-- Form for adding a movie using POST -->
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
              <tr>
                <td><input v-model="addMovieForm.title"/></td>
                <td><input v-model="addMovieForm.description"></td>
                <td><input v-model="addMovieForm.imageUrl"></td>
                <td><input v-model="addMovieForm.year"></td>
                <td><input v-model="addMovieForm.director"></td>
                <td><input v-model="addMovieForm.genre"></td>
                <td><input v-model="addMovieForm.duration"></td>
              </tr>
          </tbody>
        </table>
      </div>
      <br />
      <button @click="onSubmit">Submit</button>

    <!-- Get a movie by ID -->
    <hr />
    <h1>Get a Movie</h1>
    <p>ID: <input v-model="id"></p>
    <button><router-link :to="{name: 'GetMovie', params: {id}}">Get</router-link></button>
    <hr />

    <br />

    <!-- Update a movie's info -->
    <h1>Update a Movie</h1>
    <div>
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
            <tr>
              <td><input v-model="editForm.id"/></td>
              <td><input v-model="editForm.title"/></td>
              <td><input v-model="editForm.description"></td>
              <td><input v-model="editForm.imageUrl"></td>
              <td><input v-model="editForm.year"></td>
              <td><input v-model="editForm.director"></td>
              <td><input v-model="editForm.genre"></td>
              <td><input v-model="editForm.duration"></td>
            </tr>
        </tbody>
      </table>
      
    </div>
    <br />
    <button @click="onSubmitUpdate">UPDATE</button>
    <hr />

    <br />

    <!-- Delete a movie -->
    <h1>Delete a Movie</h1>
    <p>ID: <input v-model="delID"></p>
    <button @click="deleteMovie(delID)">DELETE</button>
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
      delID: '',
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
        id: '',
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

      this.editForm.id = '';
      this.editForm.title = '';
      this.editForm.description = '';
      this.editForm.imageUrl = '';
      this.editForm.year = '';
      this.editForm.director = '';
      this.editForm.genre = '';
      this.editForm.duration = '';

      
    },
    getMovies() {
      axios.get(`${this.$hostname}/movies`)
        .then((res) => {
          this.movies = res.data.movies;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    addMovie(new_movie) {
      axios.post(`${this.$hostname}/movie`, new_movie)
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
        'title': this.addMovieForm.title,
        'description': this.addMovieForm.description,
        'imageUrl': this.addMovieForm.imageUrl,
        'year': this.addMovieForm.year,
        'director': this.addMovieForm.director,
        'genre': this.addMovieForm.genre,
        'duration': this.addMovieForm.duration,
      };
      this.addMovie(info);
      this.initForm();
    },
    onSubmitUpdate(event) {
      event.preventDefault();
      const info = {
        'id': this.editForm.id,
        'title': this.editForm.title,
        'description': this.editForm.description,
        'imageUrl': this.editForm.imageUrl,
        'year': this.editForm.year,
        'director': this.editForm.director,
        'genre': this.editForm.genre,
        'duration': this.editForm.duration,
      };
      this.updateMovie(info, this.editForm.id);
      this.initForm();
    },
    updateMovie(info, movieID) {
      const path = `${this.$hostname}/movie/${movieID}`;
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
    deleteMovie(movieID) {
      const path = `${this.$hostname}/movie/${movieID}`;
      axios.delete(path)
        .then(() => {
          this.getMovies();
          this.message = 'Book removed!';
          console.log(this.message);
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getMovies();
        });
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
