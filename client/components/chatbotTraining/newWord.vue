<template>
  <div>
    <div class="row">
      <div class="col-md-12 pb_me-4 my-3">
        <div class="row d-flex align-items-center">
          <div class="col-8 col-md-4 pb_me-4">
            <div
              class="
                form-group
                mb-0
                border_search_gray
                form-group-feedback form-group-feedback-right
              "
            >
              <div class="input-group">
                <span class="input-group-append"
                  ><span
                    class="
                      input-group-text input-group-text-search-border
                      rounded-left
                    "
                    ><i class="icon-search4 txt_grey"></i></span
                ></span>
                <input
                  type="text"
                  class="
                    my-auto
                    form-control
                    txt_black
                    rounded-right
                    form-control-search-border
                    h2dot5
                  "
                  style="margin-right: 1rem"
                  placeholder="Type a word..."
                />
                <div class="form-control-feedback">
                  <i class="icon-cross3 txt_grey" style="height: 22px"></i>
                </div>
              </div>
            </div>
          </div>
          <div class="col-4 col-md-8 pb_me-4 text-right">
            <button
              @click="openTrainWordModal()"
              class="login__btn-submit hcb-btn btn btn_hcb_green btn-block"
              style="height: 2.5rem"
            >
              Train
            </button>
            <button
              @click="openDeleteWordModal()"
              class="login__btn-submit hcb-btn btn btn_hcb_red btn-block"
              style="height: 2.5rem"
            >
              Delete
            </button>
          </div>
        </div>
      </div>
    </div>
    <div class="row">
      <div class="col-md-12 pb_me-4 my-3">
        <div class="row d-flex align-items-center">
          <div class="txt_hc_content">
            Total words <span class="txt_vla_grey">(3)</span>
          </div>
        </div>
      </div>
    </div>
    <div class="row">
      <div class="col-md-12 pb_me-4">
        <div class="row d-flex align-items-center">
          <b-table striped hover :fields="fields" :items="items">
            <template #cell(age)="data">
              <input type="text" v-model="data.value" />
            </template>
            <template #cell(bbbbbbb)="data">
              <input type="checkbox" v-model="data.value" />
            </template>
          </b-table>
        </div>
      </div>
    </div>

    <DeleteWordModal
      :isOpen="isShowDeleteWordModal"
      :onCancel="closeDeleteWordModal"
      :onDelete="onDeleteWord"
    ></DeleteWordModal>
    <TrainWordModal
      :isOpen="isShowTrainWordModal"
      :onCancel="closeTrainWordModal"
      :onDelete="onTrainWord"
    ></TrainWordModal>
  </div>
</template>

<script>
export default {
  components: {
    DeleteWordModal: () =>
      import('~/components/chatbotTraining/DeleteWordModal.vue'),
    TrainWordModal: () =>
      import('~/components/chatbotTraining/TrainWordModal.vue'),
  },

  data() {
    return {
      isShowDeleteWordModal: false,
      isShowTrainWordModal: false,

      // Note 'isActive' is left out and will not appear in the rendered table
      fields: [
        {
          key: 'last_name',
          sortable: true,
        },
        {
          key: 'first_name',
          sortable: true,
        },
        {
          key: 'age',
          label: 'Person age',
          sortable: true,
          variant: 'danger',
        },
        {
          key: 'bbbbbbb',
          label: 'bg',
          selected: true,
        },
      ],
      items: [
        {
          isActive: true,
          age: 40,
          first_name: 'Dickerson',
          last_name: 'Macdonald',
          bbbbbbbb: '',
        },
        {
          isActive: false,
          age: 21,
          first_name: 'Larsen',
          last_name: 'Shaw',
          bbbbbbbb: '',
        },
        {
          isActive: false,
          age: 89,
          first_name: 'Geneva',
          last_name: 'Wilson',
          bbbbbbbb: '',
        },
        {
          isActive: true,
          age: 38,
          first_name: 'Jami',
          last_name: 'Carney',
          bbbbbbbb: '',
        },
      ],
    }
  },
  methods: {
    onPreviewClick(value, index, item) {},

    onDeleteWord() {
      console.log('delete word')
    },
    openDeleteWordModal() {
      this.isShowDeleteWordModal = true
    },
    closeDeleteWordModal() {
      this.isShowDeleteWordModal = false
    },
    onTrainWord() {
      console.log('trained word')
    },
    openTrainWordModal() {
      this.isShowTrainWordModal = true
    },
    closeTrainWordModal() {
      this.isShowTrainWordModal = false
    },
  },
}
</script>

<style lang="scss">
.hcb-btn {
  height: 40px;
  margin-top: 0 !important;
  max-width: 120px;
}

.txt_hc_title {
  font-family: 'TrueTextBOnline-Bold';
  font-size: 36px;
  font-style: normal;
  line-height: 1rem;
  color: #333333;
}

.txt_hc_content {
  font-family: 'TrueTextBOnline-Bold';
  font-size: 24px;
  font-weight: 600;
  font-style: normal;
  line-height: 1rem;
  color: #333333;
}
</style>
