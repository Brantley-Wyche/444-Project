<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <hr />
    <div>
      <p v-for="func in funcs" :key="func.id"><b>{{func.action}}</b> : {{func.desc}}</p>
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
        {id: 1, action: 'Home', desc: 'Come back to this page'},
        {id: 2, action: 'Add/Get/Update/Delete Movie', desc: 'Add a new movie, get information about an existing one,update an exisiting one, or delete an existing one'},
        {id: 3, action: 'Get All Movies', desc: 'Information about all of the movies in the inventory'}
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
