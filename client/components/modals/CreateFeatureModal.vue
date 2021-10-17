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
      <div class="modal-header bg-white py-2 px-0 mx-3 mt-2">
        <h4 class="modal-title txt_hc_modaltitle mr-4 pr-2">
          Create a new feature
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
              type="text"
              v-model="feature"
              class="form-control border-gray border"
            />
          </div>
          <div class="d-flex flex-column text-left mb-3">
            <div class="learning-area-title">Condition type</div>
            <b-form-select
              v-model="changedConditionType"
              class="form-control border-gray border"
              style="curser: pointer"
              autofocus
            >
              <b-form-select-option
                v-for="option in conditionTypeOptionFunction()"
                :key="option.label"
                :value="option.value"
                >{{ option.label }}</b-form-select-option
              >
            </b-form-select>
          </div>
          <div class="d-flex flex-column text-left mb-3">
            <div class="learning-area-title">Question</div>
            <input
              v-model="changedQuestion"
              type="text"
              class="form-control border-gray border"
              @keydown.prevent.space
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
const english = /^[A-Za-z]*$/

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
    featureData: {
      type: Array,
      default: [],
    },
  },
  data: () => ({
    isModalOpen: false,
    feature: '',
    changedConditionType: null,
    changedQuestion: '',
    conditionTypeOption: [
      {
        label: 'boolean',
        value: 'boolean',
      },
      {
        label: 'input',
        value: 'input',
      },
    ],
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
    conditionTypeOptionFunction() {
      // find feature that have input type in feature data
      let inputTypefeature = this.featureData.find(
        (item) => item.conditionType === 'input'
      )
      if (inputTypefeature) {
        return this.conditionTypeOption.filter((item) => item.label !== 'input')
      } else {
        return this.conditionTypeOption
      }
    },
    async onAddNewFeature() {
      const body = {
        Name: this.feature,
        Type: this.changedConditionType,
        Question: this.changedQuestion,
      }
      if (this.feature && this.changedConditionType && this.changedQuestion) {
        if (english.test(this.feature)) {
          await this.$axios.post('feature', body)
          this.$emit('getFeatureData')
          this.feature = null
          this.changedConditionType = null
          this.changedQuestion = null
          this.onCancel()
        } else {
          this.$bvToast.toast('Feature name must be in English only', {
            variant: 'danger',
            toaster: 'b-toaster-bottom-left',
            noCloseButton: true,
          })
        }
      } else {
        this.$bvToast.toast('Please fill all required fields', {
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
