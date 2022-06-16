<template>
    <div>
        <span @click="showForm()" class=" btn btn-sm btn-info d-block border" role="button">
            <i class="fas  fa-lg fa-pen"></i></span>
        <div v-show="showfrom" class="" >
        <form @submit.prevent="createSource()">
            <div class=" position-absolute p-2 py-1 bg-white  border shadow" >
                <div class="modal-dialog modal-md my-0">
                    <div class="modal-content">

                        <div class="modal-header">
                            <h5 class="modal-title" id="exampleModalLabel">Edit Source </h5>
                            <button @click="showForm()" class="close" data-dismiss="modal" aria-label="Close">
                                <span aria-hidden="true">&times;</span>
                            </button>
                        </div>

                        <div class="modal-body">
                            <div class="form-group">
                                <label for="recipient-name" class="col-form-label">Source Name *</label>
                                <input v-model.trim="source.name" type="text" class="form-control" >
                            </div>
                        </div>

                        <div class="modal-footer">
                            <button @click="showForm()" class="btn btn-secondary" data-dismiss="modal">Close</button>
                            <span   @click="removeSource()" class="btn btn-danger" data-dismiss="modal">Delete</span>
                            <button type="submit" class="btn btn-success">Save</button>
                        </div>
                    </div>
                </div>
            </div>
        </form>
        </div>
    </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
    export default{
        name:'EditSource',
        props:{
            source:Object,
        },
        data(){
            return {
                showfrom:false,
            }
        },
        computed:{
             ...mapGetters({
          getSourcesList:"getSourcesList",
        }),
        },
        methods:{
            ...mapActions({
             actionUpdateSource:'updateSource',
             actionDeleteSource:'deleteSource',
        }),
            initForm(){
                this.source.name = ''
            },
            showForm(){
                this.showfrom = !this.showfrom
            },
            async createSource(){
                const data = {
                        id:this.source.id,
                        name:this.source.name,
                        user:1
                    }
                if(await this.actionUpdateSource(data)){
                    this.showfrom = !this.showfrom
                    // this.initForm()
                }
            },
            async removeSource(){
                var r = confirm("Are you sure to delete  this source << "
                + this.source.name +" >> . \n Press button yes to delete  it .");
                if (r == true) {
                if(await this.actionDeleteSource(this.source.id)){
                    this.showfrom = !this.showfrom
                    // this.initForm()
                }
                }
            },
        }

    }
</script>

<style scoped>
.from {
    min-width: 350px;
}
</style>