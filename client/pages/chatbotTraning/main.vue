<template>
  <div class="container pt-4 pt-md-4 pb-4">
    <div class="vl_navbar text-center mb-4">
      <div class="pt-3 txt_hc_title">Chatbot Training</div>
    </div>
    <div class="vl_navbar">
      <div class="container fitscreen pt-3 pt-md-3 plr_15p">
        <div class="row">
          <div class="col-md-12 pb_me-4">
            <div class="row d-flex justify-content-center">Test</div>
          </div>
        </div>
        <nuxt-child></nuxt-child>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  layout: 'noHeaderLayout',
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
