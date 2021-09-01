<template>
  <div class="container pt-4 pt-md-4 pb-4">
    <div class="vl_navbar text-center mb-4">
      <div class="pt-3 txt_hc_title">Chatbot Training</div>
    </div>
    <div class="vl_navbar">
      <div class="container fitscreen pt-3 pt-md-3 plr_15p">
        <div class="row">
          <div class="col-md-12 pb_me-4">
            <div class="row d-flex justify-content-center">
              <div class="ml-5 mt-5">
                <b-card no-body>
                  <b-tabs card>
                    <b-tab title="Tab 1" active>
                      <newWord/>
                    </b-tab>
                    <b-tab title="Tab 2">
                      <b-card-text>Tab contents 2</b-card-text>
                    </b-tab>
                  </b-tabs>
                </b-card>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  layout: 'noHeaderLayout',
  components: {
    newWord: () => import('~/components/chatbotTraning/newWord.vue'),
  }
}
</script>

<style lang="scss">
.txt_hc_title {
  font-family: 'TrueTextBOnline-Bold';
  font-size: 36px;
  font-style: normal;
  line-height: 1rem;
  color: #333333;
}
</style>
