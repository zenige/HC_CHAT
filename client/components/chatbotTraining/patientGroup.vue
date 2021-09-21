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
      <!-- <div class="col-md-12 pb_me-4">
        <div class="row d-flex align-items-center">
          <v-data-table
            v-model="selected"
            :headers="headers"
            :items="desserts"
            :single-select="singleSelect"
            hide-default-footer
            item-key="name"
            show-select
            class="elevation-1"
          >
          </v-data-table>
              <v-btn
                elevation="2"
                fab
                @click="addCol"
                large
                class="text-black">+</v-btn>
        </div>
        <v-btn
              elevation="2"
              fab
              @click="addRowd"
              large
              class="text-black">-</v-btn>
      </div> -->
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
      headers: [
        {
          text: 'Dessert (100g serving)',
          align: 'start',
          value: 'name',
        },
        { text: 'Calories', value: 'calories' },
        { text: 'Fat (g)', value: 'fat' },
        { text: 'Carbs (g)', value: 'carbs' },
        { text: 'Protein (g)', value: 'protein' },
        { text: 'Iron (%)', value: 'iron' },
      ],
      desserts: [
        {
          name: 'Frozen Yogurt',
          calories: 159,
          fat: 6.0,
          carbs: 24,
          protein: 4.0,
          iron: '1%',
        },
        {
          name: 'Ice cream sandwich',
          calories: 237,
          fat: 9.0,
          carbs: 37,
          protein: 4.3,
          iron: '1%',
        },
      ],
      selected: [],
      count: 0,
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
    selectAll() {},
    addRowd() {
      this.desserts.push({
        name: 'new',
        calories: '',
        fat: '',
        carbs: '',
        protein: '',
        iron: '',
      })
    },
    addCol() {
      this.headers.push({
        text: 'new',
        value: '',
      })
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
  font-family: 'Prompt-Medium';
  font-size: 36px;
  font-style: normal;
  line-height: 1rem;
  color: #333333;
}

.txt_hc_content {
  font-family: 'Prompt-Medium';
  font-size: 24px;
  font-weight: 600;
  font-style: normal;
  line-height: 1rem;
  color: #333333;
}
</style>
