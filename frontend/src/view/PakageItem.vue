<template>
    <div class="col">
       <div class="card h-100 py-3">
         <form @submit.prevent="startPay()">
           <div class="card-body">
             <h1 class="mb-3"><i class="bi bi-boxes"></i></h1>
             <h3 class="text-center">{{ pakage.title }}</h3>
             <div class=" px-4 mt-3">
             <div class="text-start">

               <div class="custom-control custom-radio">
               <input
                 type="radio"
                 :id="'customRadio0' + pakage.id"
                 :name="'customRadio2' + pakage.id"
                 class="custom-control-input"
                 v-model="duration"
                 :value="'1'"
               />
               <label
                 class="custom-control-label"
                 :for="'customRadio0' + pakage.id"
                 >{{ pakage.six_months_price }} {{ pakage.currency }}<small class="h6">/ Month</small>

                 </label
               >
             </div>
             <div class="custom-control custom-radio">
               <input
                 type="radio"
                 :id="'customRadio1' + pakage.id"
                 :name="'customRadio2' + pakage.id"
                 class="custom-control-input"
                 v-model="duration"
                 :value="2"
               />
               <label
                 class="custom-control-label"
                 :for="'customRadio1' + pakage.id"
                 >{{ pakage.one_year_price }} {{ pakage.currency }}<small class="h6">/ One year</small>
                 </label>
             </div>
             <div class="custom-control custom-radio">
               <input
                 type="radio"
                 :id="'customRadio2' + pakage.id"
                 :name="'customRadio2' + pakage.id"
                 class="custom-control-input"
                 v-model="duration"
                 :value="3"
               />
               <label
                 class="custom-control-label"
                 :for="'customRadio2' + pakage.id"
                 >
                 {{ pakage.two_years_price }} {{ pakage.currency }} <small class="h6">/ Two years</small>
                 </label>
             </div>
             </div>
               <button
                 class="
                   btn btn-success
                   d-block
                   w-100
                   mt-3
                   rounded-0
                   fw-bold
                   py-1
                 "
               >
               <span v-show="isLoading"
                 class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span>
                 Start Plan
               </button>

               <!-- <router-link
                 class="d-block btn btn-warning rounded-0 mt-2"
                 :to="{ path: '/check-pay', query: { name: pakage.id } }"
                 >Start Plan Demo 1</router-link
               > -->
             </div>
             <div class="text-start mt-3">
               <span
                 v-for="f in pakage.features"
                 :key="f.id"
                 class="d-block my-1 border text-start"
               >
                 <i class="bi bi-check-lg"></i> {{ f.title }}
               </span>
             </div>
           </div>
         </form>
       </div>
     </div>
</template>

<script>
import jwtInterceptor from '../../store/modules/jwtInterceptor'
     export default{
       name:'PakageItem',
       props:{
           pakage:Object,
       },
       data(){
             return{
               isLoading:false,
               duration:null,
             }
         },
       methods:{
           async startPay(){
              if (this.duration != null){

                const data = {
                  'package':this.pakage.id,
                  'duration':this.duration,
                 }

                 console.log(data)

                 this.isLoading = true
                 await jwtInterceptor.post(`/api/payments/pay/`,data)
                 .then((res) => {
                   console.log(res.data)
                   window.location.href = res.data.paymob_url
                 })
                 .catch((err) => {
                   console.log('Packages', err)
                 })
               }else{
                 alert('Select duration')
               }
           },
     }
     }
 </script>