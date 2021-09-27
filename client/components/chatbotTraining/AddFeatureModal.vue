<template>
  <b-modal
    id="modal-scoped"
    v-model="isModalOpen"
    size="md"
    hide-footer
    modal-class="add-new-feature-modal"
    @close="onCancel"
    @hidden="onCancel"
    @ok="onAddNewFeature"
  >
    <template v-slot:modal-header="{ close }">
      <!-- Emulate built in modal header close button action -->
      <div class="modal-header bg-white py-2 px-0 mx-3 mt-2">
        <h4 class="modal-title txt_hc_modaltitle mr-4 pr-2">
          Add a new feature
        </h4>
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

    <template v-slot:default>
      <div class="modal-body px-3 px-md-3">
        <form method="post" @submit.prevent="onAddNewFeature">
          <div class="d-flex flex-column text-left mb-3">
            <div class="learning-area-title">Feature name</div>
            <input
              v-model="feature"
              type="text"
              class="form-control border-gray border"
            />
          </div>
          <div class="row d-flex justify-content-center">
            <div class="col-12 col-md-4 col-lg-4 mt-3">
              <div class="pt-2">
                <div class="form-group mb-0">
                  <button
                    type="submit"
                    class="btn btn_green_modal h2dot5 btn-block py-2"
                  >
                    Add
                  </button>
                </div>
              </div>
            </div>
          </div>
        </form>
      </div>
    </template>
  </b-modal>
</template>

<script>
export default {
  name: 'AddNewWordModal',
  props: {
    isOpen: {
      type: Boolean,
      default: false,
    },
    onCancel: {
      type: Function,
      default: () => {},
    },
    getFeatureData: {
      type: Function,
      default: () => {},
    },
    currentPage: {
      type: Number,
      default: 1,
    },
    perPage: {
      type: Number,
      default: 10,
    },
  },
  data: () => ({
    isModalOpen: false,
    feature: '',
  }),
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
    async onAddNewFeature() {
      const body = {
        feature: this.question,
      }
      if (this.feature !== '') {
        await this.$axios.post('train/trained', body)
        this.$emit('getFeatureData', this.currentPage, this.perPage, 'question')
        this.feature = ''
        this.onCancel()
      } else {
        this.$bvToast.toast('Please fill feature name', {
          variant: 'danger',
          toaster: 'b-toaster-bottom-left',
          noCloseButton: true,
        })
      }
    },
  },
}
</script>

<style lang="scss">
.add-new-feature-modal {
  .modal-header {
    width: 100%;
    margin: 0 !important;
  }

  .modal-body {
    padding: 8px 0;
    overflow-y: auto;

    .btn {
      display: flex;
      justify-content: center;
      align-items: center;
    }
  }
}
</style>
