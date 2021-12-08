<template>
  <div>
    <b-card
        title="newpage1"
    >
        <b-container class="bv-example-row">
            <b-row>
                <b-col cols="4"></b-col>
                <b-col cols="4">
                    <center>
                        <button 
                            v-if="questionIndex === 1"
                            class="btn btn-primary" 
                            @click="prev"
                            disabled>
                            prev
                        </button>
                        <button 
                            v-if="questionIndex !== 1"
                            class="btn btn-primary" 
                            @click="prev">
                            prev
                        </button>
                        <span> {{ this.questionIndex }} </span>
                        <button v-if="questionIndex === quiz.questions.length" class="btn btn-secondary" @click="next" disabled>
                            next
                        </button> 
                        <button v-if="questionIndex !== quiz.questions.length" class="btn btn-secondary" @click="next">
                            next
                        </button> 
                    </center> 
                </b-col>
                <b-col cols="4">
                    <center>
                        <button class="btn btn-success" @click="show" v-if="this.showg === false">
                            show
                        </button> 
                        <button class="btn btn-success" @click="close" v-if="this.showg === true">
                            close
                        </button> 
                    </center>
                </b-col>
            </b-row>
            <b-row v-if="this.showg === true">
                <div v-for="(item, index) in quiz.questions" :key="index">
                    <button v-if="item.check === true" class="btn btn-success"  @click="perpage(index)">{{ index+1 }}</button>
                    <button v-if="item.check === false" class="btn btn-secondary"  @click="perpage(index)">{{ index+1 }}</button>
                </div>
            </b-row>
            <b-row>
                <p>{{ quiz.questions[questionIndex-1].text }}</p>
            </b-row>
            <b-row v-for="(item, index) in quiz.questions[questionIndex-1].answers" :key="index">
                <button v-if="index === quiz.questions[questionIndex-1].checkpoint" class="btn btn-success" @click="checkpointbg(index, item.value)">{{ item.text }} {{ index }}</button>
                <button v-if="index !== quiz.questions[questionIndex-1].checkpoint" class="btn btn-secondary" @click="checkpointbg(index, item.value)">{{ item.text }} {{ index }}</button>
            </b-row>
        </b-container>
    </b-card>
  </div>
</template>

<script>
var quiz = {
  title: "quiz sample",
  questions: [
    {
      text: 'Question 1 description',
      answers: [
        {
          text: 'Answer 1',
          value: 1
        },
        {
          text: 'Answer 2',
          value: 2
        },
        {
          text: 'Answer 3',
          value: 3
        },
      ],
      checkpoint: '',
      check: false
    },
    {
      text: 'Question 2 description',
      answers: [
        {
          text: 'Answer 1a',
          value: 1
        },
        {
          text: 'Answer 2a',
          value: 2
        },
        {
          text: 'Answer 3a',
          value: 3
        },
      ],
      checkpoint: '',
      check: false
    },
    {
      text: 'Question 3 description',
      answers: [
        {
          text: 'Answer 1b',
          value: 1
        },
        {
          text: 'Answer 2b',
          value: 2
        },
        {
          text: 'Answer 3b',
          value: 3
        },
      ],
      checkpoint: '',
      check: false
    },
    {
      text: 'Question 4 description',
      answers: [
        {
          text: 'Answer 1n',
          value: 1
        },
        {
          text: 'Answer 2n',
          value: 2
        },
      ],
      checkpoint: '',
      check: false
    },
    {
      text: 'Question 5 description',
      answers: [
        {
          text: 'Answer 1i',
          value: 1
        },
        {
          text: 'Answer 2i',
          value: 2
        },
      ],
      checkpoint: '',
      check: false
    }
  ]
};

export default {
    data() {
        return {
            quiz: quiz,
            questionIndex: 1,
            showg: false,
            ans: []
        }
    },
    methods: {
        checkpointbg(value, score) {
            this.quiz.questions[this.questionIndex-1].checkpoint = value
            this.quiz.questions[this.questionIndex-1].check = true
            console.log(this.quiz.questions[this.questionIndex-1])
            console.log('nn', this.quiz.questions)
            console.log(value)
            this.ans[this.questionIndex-1] = score
            console.log('sc', this.ans)
        },
        prev() {
            if(this.questionIndex > 1){
                this.questionIndex--;
            }
        },
        next() {
            if(this.questionIndex >= 1 && this.questionIndex !== this.quiz.questions.length){
                this.questionIndex++;
            }
        },
        perpage(value) {
            console.log(value)
            this.questionIndex = value+1
        },
        show() {
            if(this.showg == false ) {
                this.showg = true
            }
            console.log('be', this.showg)
        },
        close() {
            if(this.showg == true ) {
                this.showg = false
            }
            console.log('be', this.showg)
        },
        playAgain() {
        this.questionIndex = 0;
        }
    }
}

</script>

<style>

</style>
