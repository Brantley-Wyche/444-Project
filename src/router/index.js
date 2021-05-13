import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import CRUDMovie from '@/components/CRUDMovie'
import AllMovies from '@/components/AllMovies'
import GetMovie from '@/components/GetMovie'

Vue.use(Router)

export default new Router({
  //mode: 'history',
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/movie',
      name: 'CRUDMovie',
      component: CRUDMovie
    },
    {
      path: '/movie/:id',
      name: 'GetMovie',
      component: GetMovie
    },
    {
      path: '/movies',
      name: 'AllMovies',
      component: AllMovies
    }
  ]
})
