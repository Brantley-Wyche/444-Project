<template>
  <div class="getmovie">
    <h1>{{ msg }}</h1>
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
    <p>{{$route.params.id}}</p>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'GetMovie',
  data () {
    return {
      msg: 'Movie Info',
      
    }
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
  margin-bottom: 15px;
}
a {
  color: #42b983;
}
</style>
