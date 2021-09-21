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
                  <i class="icon-cross3 txt_grey" style="height: 22px"></i>
                </div>
              </div>
            </div>
          </div>
          <div class="col-4 col-md-8 pb_me-4 text-right">
            <button
              @click="openAddWordModal()"
              class="login__btn-submit hcb-btn btn btn_hcb_green btn-block"
              style="height: 2.5rem"
            >
              Add Word
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
            <span class="txt_vla_grey">({{ totalTrainedWord }})</span>
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
            id="trainedWord-table"
            :items="trainedWordData"
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
            <template #head(selected)>
              <input type="checkbox" v-model="selectAll" />
              <span>Select All</span>
            </template>
            <template #cell(selected)="data">
              <input type="checkbox" v-model="data.item.selected" />
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
              :total-rows="totalTrainedWord"
              :per-page="perPage"
              first-text="First"
              prev-text="<"
              next-text=">"
              last-text="Last"
              aria-controls="trainedWord-table"
            ></b-pagination>
          </div>
        </div>
      </div>
    </div>

    <DeleteWordModal
      :isOpen="isShowDeleteWordModal"
      :onCancel="closeDeleteWordModal"
      :onDelete="onDeleteWord"
    ></DeleteWordModal>
    <AddNewWordModal
      :isOpen="isShowAddNewWordModal"
      :onCancel="closeAddWordModal"
      @getTrainedWordData="getTrainedWordData"
      :currentPage="currentPage"
      :perPage="perPage"
    ></AddNewWordModal>
  </div>
</template>

<script>
export default {
  components: {
    DeleteWordModal: () =>
      import('~/components/chatbotTraining/DeleteWordModal.vue'),
    AddNewWordModal: () =>
      import('~/components/chatbotTraining/AddNewWordModal.vue'),
  },
  props: {},
  data() {
    return {
      isShowDeleteWordModal: false,
      isShowAddNewWordModal: false,
      edit: false,
      selectAll: false,
      selectedRow: {},
      filter: '',
      perPage: 10,
      currentPage: 1,
      deleteSelected: [],
      totalTrainedWord: 0,
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
          key: 'actions',
          label: '',
          sortable: false,
        },
      ],
      trainedWordData: [],
    }
  },
  watch: {
    selectAll(value) {
      this.trainedWordData.map(function (item) {
        item.selected = value
        // return item
      })
    },
    currentPage(value) {
      this.getTrainedWordData(value, this.perPage, 'question')
    },
  },
  async mounted() {
    await this.getTrainedWordData(1, 10, 'question')
  },
  computed: {},
  methods: {
    openDeleteWordModal() {
      this.deleteSelected = this.trainedWordData.filter(
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
      this.selectAll = false
      this.isShowDeleteWordModal = false
    },
    openAddWordModal() {
      this.isShowAddNewWordModal = true
    },
    closeAddWordModal() {
      this.isShowAddNewWordModal = false
    },
    async onDeleteWord() {
      this.deleteSelected = this.trainedWordData.filter(
        (item) => item.selected === true
      )
      await this.$axios.delete('train/trained/delete/many', {
        data: this.deleteSelected,
      })
      await this.getTrainedWordData(this.currentPage, 10, 'question')
      if (this.trainedWordData.length === 0) {
        this.totalTrainedWord = 0
      }
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
      await this.$axios.patch(`/train/trained/` + data.item.id, {
        question: data.item.question,
        answer: data.item.answer,
      })
    },
    async getTrainedWordData(page, limit, orderBy) {
      let { data } = await this.$axios.get(
        `train/trained?pages=${page}&limit=${limit}&order_by=${orderBy}`
      )
      this.trainedWordData = data.map((item) => {
        // collect total trained word data
        if (item.total) {
          return (
            {
              id: undefined,
            },
            (this.totalTrainedWord = item.total)
          )
          // it will return undefined item
        } else {
          return {
            answer: item.answer,
            time: item.time,
            question: item.question,
            id: item.id,
            selected: false,
            editable: false,
          }
        }
      })
      // remove undefined item
      this.trainedWordData = this.trainedWordData.filter(function (element) {
        return element.id !== undefined
      })
      if (this.trainedWordData.length === 0) {
        this.totalTrainedWord = 0
      }
      console.log(
        'page: ',
        page,
        'data: ',
        this.trainedWordData.length,
        'total: ',
        this.totalTrainedWord
      )
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
