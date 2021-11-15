<template>
  <b-modal
    id="modal-scoped"
    v-model="isModalOpen"
    modal-class="patient-info-modal"
    size="xl"
    hide-footer
    @close="onCancel"
    @hidden="onCancel"
  >
    <template v-slot:modal-header="{ close }">
      <div class="modal-header modal-skin-img bg-white py-2 px-0 mx-3 mt-2">
        <button
          type="button"
          class="close pr-1 pt_15p"
          data-dismiss="modal"
          @click="close()"
        >
          <img
            src="~assets/hc-libs/images/main/ic_close_grey.svg"
            width="37"
            loading="lazy"
          />
        </button>
      </div>
    </template>

    <template>
      <div class="modal-body px-3 px-md-3">
        <div class="d-flex flex-column justify-content-start">
          <img class="img-modal-content" :src="imgModal.src" />
        </div>
      </div>
    </template>
  </b-modal>
</template>

<script>
export default {
  name: 'skinDiseaseImgModal',
  data: () => ({
    isModalOpen: false,
  }),
  props: {
    imgModal: {
      type: Object,
      default: () => {},
    },
    isOpen: {
      type: Boolean,
      default: false,
    },
    onCancel: {
      type: Function,
      default: () => {},
    },
  },
  watch: {
    isOpen(newVal) {
      this.isModalOpen = newVal
    },
    isModalOpen(newVal) {
      if (!newVal) {
        this.onModalHide()
      }
    },
  },
  methods: {
    onModalHide() {
      this.$emit('onModalHide', false)
    },
  },
}
</script>

<style scoped>
.modal-skin-img {
  border-bottom: 0px !important;
}
.img-modal-content {
  width: 100%;
  height: auto;
}
</style>
