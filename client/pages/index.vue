<template>
  <div class="container">
    <div class="vl_navbar">
      <div class="row d-flex justify-content-center">
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
                        v-model="filter"
                        type="search"
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
                      <div class="form-control-feedback" @click="filter = ''">
                        <i
                          class="icon-cross3 txt_grey"
                          style="height: 22px"
                        ></i>
                      </div>
                    </div>
                  </div>
                </div>
                <div class="col-4 col-md-8 pb_me-4 text-right">
                  <button
                    @click="openTrainWordModal()"
                    class="
                      login__btn-submit
                      hcb-btn
                      btn btn_hcb_green btn-block
                    "
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
                  Total words
                  <span class="txt_vla_grey">({{ rows }})</span>
                </div>
              </div>
            </div>
          </div>
          <div class="row">
            <div class="col-md-12 pb_me-4">
              <div class="row d-flex align-items-center">
                <b-table
                  striped
                  hover
                  id="newWord-table"
                  :items="newWordData"
                  :per-page="0"
                  :current-page="currentPage"
                  :fields="fields"
                  :filter="filter"
                >
                  <template #cell(question)="data">
                    <div v-if="data.item.editable === false">
                      <div>
                        {{ data.item.question }}
                      </div>
                    </div>
                    <b-form-input
                      autofocus
                      v-if="data.item.editable === true"
                      v-model="changedQuestionData"
                      @keyup.enter="saveWord(data)"
                    />
                  </template>
                  <template #cell(answer)="data">
                    <div v-if="data.item.editable === false">
                      <div>
                        {{ data.item.answer }}
                      </div>
                    </div>
                    <b-form-input
                      autofocus
                      v-if="data.item.editable === true"
                      v-model="changedAnswerData"
                      @keyup.enter="saveWord(data)"
                    />
                  </template>
                  <template #cell(selected)="data">
                    <input type="checkbox" v-model="data.item.selected" />
                  </template>
                  <template #head(selected)>
                    <input type="checkbox" v-model="selectAll" />
                    <span>Select All</span>
                  </template>

                  <template #cell(actions)="data">
                    <b-button
                      v-if="data.item.editable === false"
                      variant="primary"
                      @click="editWord(data)"
                      >Edit</b-button
                    >
                    <b-button
                      v-if="data.item.editable === true"
                      variant="danger"
                      @click="cancleEditWord(data)"
                      >Cancle</b-button
                    >
                    <b-button
                      v-if="data.item.editable === true"
                      variant="success"
                      @click="saveWord(data)"
                      >Save</b-button
                    >
                  </template>
                </b-table>
                <div class="mt-3">
                  <b-pagination
                    v-model="currentPage"
                    :total-rows="totalNewWord"
                    :per-page="perPage"
                    first-text="First"
                    prev-text="<"
                    next-text=">"
                    last-text="Last"
                    aria-controls="newWord-table"
                  ></b-pagination>
                </div>
              </div>
            </div>
          </div>

          <TrainWordModal
            :isOpen="isShowTrainWordModal"
            :onCancel="closeTrainWordModal"
            :onDelete="onTrainWord"
          ></TrainWordModal>
          <DeleteWordModal
            :isOpen="isShowDeleteWordModal"
            :onCancel="closeDeleteWordModal"
            :onDelete="onDeleteWord"
          ></DeleteWordModal>
        </div>
      </div>
    </div>
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
  props: {},
  data() {
    return {
      isShowDeleteWordModal: false,
      isShowTrainWordModal: false,
      edit: false,
      selectAll: false,
      selectedRow: {},
      filter: '',
      perPage: 10,
      currentPage: 1,
      trainSelected: [],
      deleteSelected: [],
      totalNewWord: 0,
      changedQuestionData: '',
      changedAnswerData: '',
      fields: [
        {
          key: 'selected',
          label: 'Select',
        },
        {
          key: 'question',
          label: 'Word',
          sortable: true,
        },
        {
          key: 'answer',
          label: 'Answer',
          sortable: true,
        },
        {
          key: 'confident',
          label: 'Confident',
          sortable: true,
        },
        {
          key: 'count',
          label: 'Count',
          sortable: true,
        },
        {
          key: 'actions',
          label: '',
          sortable: false,
        },
      ],
      newWordData: [],
    }
  },
  watch: {
    selectAll(value) {
      this.newWordData.map(function (item) {
        item.selected = value
        return item
      })
    },
    currentPage(value) {
      this.getNewWordData(value, this.perPage, 'question')
    },
  },
  async mounted() {
    await this.getNewWordData(1, 10, 'question')
  },
  computed: {
    rows() {
      return this.totalNewWord
    },
  },
  methods: {
    openDeleteWordModal() {
      this.deleteSelected = this.newWordData.filter(
        (item) => item.selected === true
      )
      if (this.deleteSelected.length >= 1) {
        this.isShowDeleteWordModal = true
      } else {
        ;(this.isShowDeleteWordModal = false),
          this.$bvToast.toast('Please select any word', {
            variant: 'danger',
            toaster: 'b-toaster-bottom-left',
            noCloseButton: true,
          })
      }
    },
    closeDeleteWordModal() {
      this.isShowDeleteWordModal = false
    },
    async onTrainWord() {
      this.trainSelected = this.newWordData.filter(
        (item) => item.selected === true
      )
      await this.$axios.post('train/trained/many', this.trainSelected)
      this.onDeleteWord()
    },
    openTrainWordModal() {
      this.trainSelected = this.newWordData.filter(
        (item) => item.selected === true
      )
      if (this.trainSelected.length >= 1) {
        this.isShowTrainWordModal = true
      } else {
        ;(this.isShowTrainWordModal = false),
          this.$bvToast.toast('Please select any word', {
            variant: 'danger',
            toaster: 'b-toaster-bottom-left',
            noCloseButton: true,
          })
      }
    },
    closeTrainWordModal() {
      this.isShowTrainWordModal = false
    },
    async onDeleteWord() {
      this.deleteSelected = this.newWordData.filter(
        (item) => item.selected === true
      )
      await this.$axios.delete('train/training/delete/many', {
        data: this.deleteSelected,
      })
      await this.getNewWordData(this.currentPage, 10, 'question')
      this.selectAll = false
    },
    editWord(data) {
      this.changedQuestionData = data.item.question
      this.changedAnswerData = data.item.answer
      data.item.editable = true
    },
    cancleEditWord(data) {
      data.item.editable = false
    },
    async saveWord(data) {
      data.item.question = this.changedQuestionData
      data.item.answer = this.changedAnswerData
      data.item.editable = false
      await this.$axios.patch(`/train/training/` + data.item.id, {
        question: data.item.question,
        answer: data.item.answer,
      })
    },
    async getNewWordData(page, limit, orderBy) {
      let { data } = await this.$axios.get(
        `train/training?pages=${page}&limit=${limit}&order_by=${orderBy}`
      )
      this.newWordData = data.map((item) => {
        // collect total new word data
        if (item.total) {
          return (
            {
              id: undefined,
            },
            (this.totalNewWord = item.total)
          )
          // it will return undefined item
        } else {
          return {
            answer: item.answer,
            time: item.time,
            count: item.count,
            confident: item.confident,
            question: item.question,
            id: item.id,
            selected: false,
            editable: false,
          }
        }
      })
      // remove undefined item
      this.newWordData = this.newWordData.filter(function (element) {
        return element.id !== undefined
      })
      console.log(this.totalNewWord)
      console.log(this.newWordData)
    },
  },
}
</script>

<style lang="scss">
.hcb-btn {
  height: 40px;
  margin-top: 0 !important;
  max-width: 120px !important;
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
