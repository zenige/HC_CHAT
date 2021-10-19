<template>
  <b-modal
    id="modal-scoped"
    v-model="isModalOpen"
    size="md"
    hide-footer
    modal-class="create-new-group-modal"
    @close="onCancel"
    @hidden="onCancel"
    @ok="onCreateNewGroup"
  >
    <template v-slot:modal-header="{ close }">
      <div class="modal-header bg-white py-2 px-0 mx-3 mt-2">
        <h4 class="modal-title txt_hc_modaltitle mr-4 pr-2">Add a new group</h4>
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
        <form method="post" @submit.prevent="onCreateNewGroup">
          <div class="d-flex flex-column text-left mb-3">
            <div class="learning-area-title">Group name</div>
            <input
              v-model="groupName"
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
                    Create
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
const english = /^[A-Za-z0-9^*()_+=[/\]{}|\\,.?: -]*$/

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
    getGroupData: {
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
    groupName: '',
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
    async onCreateNewGroup() {
      const body = {
        Name: this.groupName,
      }
      if (this.groupName) {
        if (english.test(this.groupName)) {
          await this.$axios.post('group', body)
          this.$emit('getGroupData')
          this.$router.push(
            this.localePath(
              '/chatbot-training/group-management/group/' + this.groupName
            )
          )
          this.groupName = null
          this.onCancel()
        } else {
          this.$bvToast.toast('Please fill in matching text.', {
            variant: 'danger',
            toaster: 'b-toaster-bottom-left',
            noCloseButton: true,
          })
          this.groupName = null
        }
      } else if (!this.groupName) {
        this.$bvToast.toast('Please fill group name.', {
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
.create-new-group-modal {
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
