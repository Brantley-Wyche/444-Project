<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <hr />
    <div>
      <ul>
        <li v-for="func in funcs">
          <b>{{func.action}}</b> : {{func.desc}}
        </li>
      </ul>
    </div>
    <hr />
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  data () {
    return {
      msg: 'Movie Registry',
      funcs: [
        {action: 'Home', desc: 'Come back to the homepage'},
        {action: 'Add/Get/Update/Delete Movie', desc: 'You can add a new movie, get information about an existing one,update an exisiting one, or delete an existing one'},
        {action: 'Get All Movies', desc: 'You can get information about all of the movies in the inventory'}
        
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
  margin-bottom: 15px;
}
a {
  color: #42b983;
}
</style>
