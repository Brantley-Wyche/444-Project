import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import CRUDMovie from '@/components/CRUDMovie'
import AllMovies from '@/components/AllMovies'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/movie',
      name: 'AddMovie',
      component: CRUDMovie
    },
    {
      path: '/movies',
      name: 'AllMovies',
      component: AllMovies
    }
  ]
})
