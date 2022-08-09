<template>
  <div>
    <div>
      <b-navbar variant="light" type="light" class="py-3">
        <b-navbar-brand href="#">
          <img src="../assets/georgianlogo.png" alt=" Logo">
        </b-navbar-brand>
        <h1 class="font-weight-bold font-italic ">Group 4 Course Dashboard </h1>
      </b-navbar>
    </div>
    <div class="p-4">
      <div style="min-height: 500px;">
        <div class="row h-75">
            <div class="col">
              <h1 class="pt-3">Welcome to the Dashboard of the Data programming course project</h1>
              <p>This website is using Online mongodb Database to get the data and the API is hosted in Huroku free account. API is written in Python using Flask library</p>

              <div class="d-flex justify-content-center p-2 mt-4 pt-4">
                <div class="col">
                  <div class="row">
                    <div class="col">
                      <h3>Search the Title of the Movie</h3>
                    </div>
                  </div>
                  <div class="d-flex justify-content-center row pt-4">
                    <input v-model="movieTitle" placeholder="Enter Movie Title" class="mx-2" type="text">
                    <b-button variant="outline-primary" v-on:click="getMovieDetails(movieTitle)" size="sm">Search</b-button>
                  </div>
                  <div class=" d-flex justify-content-center row">
                    <div >
                      <circle-spin v-if="isLoading &&  movieDetail.length>0" loading="isLoading"></circle-spin>
                      <h5 class="my-4 " v-if="movieDetail.length>0"  >Movie Details are shown below </h5>
                      <div v-if="movieDetail.length>0"  class="table-wrap">
                        <table class="table table-striped">
                          <thead>
                            <tr>
                              <th scope="col">Title</th>
                              <th scope="col">Overview</th>
                              <th scope="col">Release date</th>
                              <th scope="col">Popularity</th>
                              <th scope="col">Original Title</th>
                              <th scope="col">Vote Count</th>
                              <th scope="col">Video</th>
                              <th scope="col">Adult</th>
                              <th scope="col">Vote Average</th>
                              <th scope="col">Media Type</th>
                              <th scope="col">Original Language</th>
                            </tr>
                          </thead>
                          <tbody>
                            <tr v-for="(item,i) in movieDetail" :key="i">
                              <th scope="row">{{ item[0] }}</th>  
                              <td>{{ item[1]}}</td> 
                              <td>{{ item[2] }}</td>
                              <td>{{ item[3]}}</td> 
                              <td>{{ item[4] }}</td> 
                              <td>{{ item[5]}}</td> 
                              <td>{{ item[6] }}</td> 
                              <td>{{ item[7]}}</td> 
                              <td>{{ item[8] }}</td> 
                              <td>{{ item[9]}}</td> 
                              <td>{{ item[10] }}</td> 
                              <td>{{ item[11]}}</td> 
                            </tr>
                          </tbody>
                        </table>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
      </div>
      <hr class="p-4 m-4"/>
      <h3>Google Charts for languages used for top movies</h3>
      <div class="row p-4">
        <div class="col">
            <GChart
            type="PieChart"
            :data="chartData"
            :options="chartOptions.chart"/>
        </div>
         <div class="col">
            <GChart
            type="ColumnChart"
            :data="chartData"
            :options="chartOptions.chart"/>
        </div>
      </div>
      <hr class="p-4 m-4"/>
      <div class="row p-4 mt-4">
        <div class="col">
          <h2>Top 10 movies based on Popularity</h2>
          <ul class="list-group">
            <li v-for="(item,i) in topPopularity" :key="i"  :class="i%2==0? 'list-group-item ':'list-group-item list-group-item-light'">{{item}}</li>
          </ul>
        </div>
        <div class="col">
          <h2>Top 10 movies based on Vote count</h2>
          <ul class="list-group">
            <li v-for="(item,i) in topVotedMovie" :key="i"  :class="i%2==0? 'list-group-item ':'list-group-item list-group-item-light'">{{item}}</li>
          </ul>
        </div>
      </div>
      <hr class="p-4 m-4"/>
      <div class="row p-4 mt-4">
        <div class="col">
          <h2>Top 10 movies based on Voting Average</h2>
          <ul class="list-group">
            <li v-for="(item,i) in topVotedAverage" :key="i"  :class="i%2==0? 'list-group-item ':'list-group-item list-group-item-light'">{{item}}</li>
          </ul>
        </div>
        <div class="col">
          <h2>Top 10 movies based on Least Popularity</h2>
          <ul class="list-group">
            <li v-for="(item,i) in leastPopularity" :key="i"  :class="i%2==0? 'list-group-item ':'list-group-item list-group-item-light'">{{item}}</li>
          </ul>
        </div>
      </div>
    </div> 
  </div>
</template>

<script>
import { GChart } from 'vue-google-charts/legacy'
import axios from 'axios'

export default {
  name: "charts-page",
  components: {
    GChart
  },
  data() {
    return {
      // Array will be automatically processed with visualization.arrayToDataTable function
      chartData: [],
      chartOptions: {
        chart: {
          title: "Distribution of language",
          pieHole: 0
        }
      },
      DataFile : '',
      topVotedMovie: [],
      isLoading : false,
      topPopularity: [],
      leastPopularity:[],
      topVotedAverage: [],
      movieDetail : [],
      movieTitle:''
    };
  },
  methods: {
    getTopLanguage: function () {
      this.isLoading =  true
      axios
      .get('https://boiling-cove-12297.herokuapp.com/getTopLanguage')
      .then(response => {
        this.isLoading =  false
        this.chartData = response.data.values
      })
    },
    getTopPopularity: function () {
      this.isLoading =  true
      axios
      .get('https://boiling-cove-12297.herokuapp.com/getTopPopularity')
      .then(response => {
        this.isLoading =  false
        this.topPopularity = response.data.values
      })
    },
    getTopVotedMovie : function () {
      this.isLoading =  true
      axios
      .get('https://boiling-cove-12297.herokuapp.com/getTopVoteCount')
      .then(response => {
        this.isLoading =  false
        this.topVotedMovie = response.data.values
      })
    },
    getLeastPopularity: function () {
      this.isLoading =  true
      axios
      .get('https://boiling-cove-12297.herokuapp.com/getLeastPopularity')
      .then(response => {
        this.isLoading =  false
        this.leastPopularity = response.data.values
      })
    },
    getTopVotedAverage : function () {
      this.isLoading =  true
      axios
      .get('https://boiling-cove-12297.herokuapp.com/getTopVoteAverage')
      .then(response => {
        this.isLoading =  false
        this.topVotedAverage = response.data.values
      })
    },
    getMovieDetails : function (msg) {
      this.isLoading =  true
      axios
      .get('https://boiling-cove-12297.herokuapp.com/getMovieDetail/'+msg)
      .then(response => {
        this.isLoading =  false
        this.movieDetail = response.data.values
        console.log(this.movieDetail.shift())
      })
    }
  },
  created() {
    this.getTopLanguage()
    this.getTopPopularity()
    this.getTopVotedMovie()
    this.getLeastPopularity()
    this.getTopVotedAverage()
    this.getMovieDetails()
  }
};
</script>
