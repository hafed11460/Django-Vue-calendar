<template>
  <div class="container p-5">
    <div class="row row-cols-1 row-cols-md-3 g-3">
      <PPakage  v-for="p in pakages" :key="p.id"
        :pakage="p"
      />
    </div>


    <router-view style="height: 100%" />
  </div>
</template>
  <script>
      import jwtInterceptor from '../shared/jwtInterceptor'

      import PPakage from '../components/pakages/PPakage.vue'

      export default{
        components: { PPakage },
          data(){
              return{
                    price:null,
                    pakages:[]
              }
          },
          methods:{

            async loadPakages(){
                await jwtInterceptor.get('/api/packages/')
                    .then((res) => {
                        this.pakages = res.data
                    })
                    .catch((err) => {
                        console.log('Packages', err)
                    })
                },
            },

          created(){
              this.loadPakages()
          }
      }
  </script>