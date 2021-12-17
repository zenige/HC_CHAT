<template>
  <b-modal
    id="modal-scoped"
    v-model="isModalOpen"
    size="md"
    modal-class="delete-word-modal"
    hide-footer
    @close="onCancel"
    @hidden="onCancel"
    @ok="onDelete"
  >
    <template v-slot:modal-header="{ close }">
      <div class="modal-header bg-white py-2 px-0 mx-3 mt-2">
        <h4 class="modal-title txt_hc_modaltitle mr-4 pr-2">Train word</h4>
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

    <template v-slot:default="{ close, ok }">
      <div class="modal-body px-3 px-md-3">
        <div class="text-center">
          <div style="font-size: 18px" class="mb-3">
            This action cannot undo later.<br />
            Do you want to train this word?
          </div>
        </div>
        <div class="row d-flex justify-content-center">
          <div class="col-12 col-md-4 col-lg-4">
            <div class="pt-2">
              <div class="form-group mb-0">
                <button
                  class="btn btn_red_modal h2dot5 btn-block py-2"
                  @click="close()"
                >
                  No
                </button>
              </div>
            </div>
          </div>
          <div class="col-12 col-md-4 col-lg-4">
            <div class="pt-2">
              <div class="form-group mb-0">
                <button
                  class="btn btn_green_modal h2dot5 btn-block py-2"
                  @click="ok()"
                >
                  Yes
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </template>
  </b-modal>
</template>

<script>
export default {
  name: 'DeleteWordModal',
  props: {
    isOpen: {
      type: Boolean,
      default: false,
    },
    onCancel: {
      type: Function,
      default: () => {},
    },
    onDelete: {
      type: Function,
      default: () => {},
    },
  },
  data: () => ({
    isModalOpen: false,
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
  },
}
</script>

<style lang="scss">
.delete-word-modal {
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
