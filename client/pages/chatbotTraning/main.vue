<template>
  <div class="container pt-4 pt-md-4 pb-4">
    <div class="vl_navbar text-center mb-4">
      <div class="pt-3 txt_hc_title">Chatbot Training</div>
    </div>
    <div class="vl_navbar">
      <div class="container fitscreen pt-3 pt-md-3 plr_15p">
        <div class="row d-flex justify-content-center">
          <div class="col-12 pb_me-4">
            <b-tabs>
              <b-tab title="New Word" active>
                <newWord />
              </b-tab>
              <b-tab title="Trained Word">
                <b-card-text>Tab contents 2</b-card-text>
              </b-tab>
              <b-tab title="Patient Group">
                <patient/>
              </b-tab>
            </b-tabs>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import PatientGroup from '../../components/chatbotTraining/patientGroup.vue'
export default {
  layout: 'noHeaderLayout',
  props: {
    name: { required: true },
    selected: { default: false },
  },
  data: () => ({}),
  components: {    
    patient: () => import('~/components/chatbotTraining/patientGroup.vue'),
    newWord: () => import('~/components/chatbotTraining/newWord.vue')
  },
}
</script>

<style lang="scss">
.vl_navbar .nav-tabs {
  border-bottom: 1px solid #ddd;
}

.vl_navbar .nav-tabs .nav-item.show .nav-link,
.vl_navbar .nav-tabs .nav-link.active {
  color: #cc338b;
  background-color: #fff;
  border-bottom: 2px solid #cc338b;
  font-weight: 600;
}

.vl_navbar .nav-tabs .nav-link {
  padding: 0.5rem 1rem;
}

.txt_hc_title {
  font-family: 'TrueTextBOnline-Bold';
  font-size: 36px;
  font-style: normal;
  line-height: 1rem;
  color: #333333;
}
.fade-up-enter-active,
.fade-up-leave-active {
  transition: all 0.1s ease-in-out;
}
.fade-up-enter,
.fade-up-leave-to {
  height: 0;
  opacity: 0;
}
</style>
