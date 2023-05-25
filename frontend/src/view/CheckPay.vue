<template>
    <div class=" p-5">
    <form >
        <div class="row ">
            <div class="col-md-8">
                <div class="card h-100 py-3" style="in-height:627px">
                    <iframe width="100%" height="800px" :src="paymob_url"></iframe>
                </div>
            </div>
            <div class=" col-sm-12 col-md-4">
                <div class="card hF-100 py-3">
                    <div v-if="pk" class="card-body text-center">
                        <h3>{{ pk.name }}</h3>
                        <h1 class="display-4 fw-bold ">{{ pk.monthly_price }} {{ currency }}
                            <small class="h6">/ Month</small></h1>
                        <h6 class="fw-bold ">{{ pk.annual_price }} {{ currency }}  annually</h6>
                        <div class='text-start px-4 mt-3'>
                            <span v-for="f in pk.features" :key="f.id" class="card-text d-block my-1">
                                <i class="bi bi-check-lg"></i> {{ f.title}}
                            </span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </form>
</div>

</template>
<script>
import jwtInterceptor from "../shared/jwtInterceptor";
export default {
    props:['name'],
    data() {
        return {
            pk:null,
            paymob_url:null,
            currency:null,
        };
  },
  methods: {
    async loadPakage() {
        await jwtInterceptor
            .get(`/payments/packages/${this.name}/`)
            .then((res) => {
                console.log(res.data)
                this.pk = res.data.package;
                this.paymob_url = res.data.paymob_url;
                this.currency = res.data.currency;
            })
            .catch((err) => {
                console.log("Packages", err);
            });
    },
  },

  created() {
    this.loadPakage();
  },
};
</script>