const VideoCard = Vue.component('video-card', {
    template:
    `
    <div>
        <v-card class="rounded-xl" height="300px" elevation="2" :href="'../../video/' + id">
            <v-img height="200px" :src="thumbnail"></v-img>
            <v-card-title class="col-11 text-truncate">[[ title ]]</v-card-title>
            <v-card-text> <v-icon> mdi-calendar </v-icon> [[ date ]] </v-card-text>
        </v-card>
    </div>
    `,
    delimiters: ['[[', ']]'],
    props: ['id', 'thumbnail', 'title', 'date'],
})

const ChannelCard = Vue.component('channel-card', {
    template:
    `
    <div>
        <v-card class="rounded-xl" height="280px" elevation="2" :href="'../../channel/' + id">
            <v-img max-height="180px" :src="profilepic"></v-img>
            <v-card-title class="col-11 text-truncate">[[ name ]]</v-card-title>
            <v-card-text v-if="subscribercount != ''"> 
                [[ subscribercount ]] subscribers 
            </v-card-text>
        </v-card>
    </div>    
    `,
    delimiters: ['[[', ']]'],
    props: ['id', 'profilepic', 'name', 'subscribercount'],
})

const Toolbar = Vue.component('toolbar', {
    template:
    `
    <v-toolbar flat>
        <v-spacer></v-spacer>
        <v-btn class="mx-3" depressed color="white" href="/">Videos</v-btn>
        <v-btn class="mr-3" depressed color="white" href="/channels">Channels</v-btn>
        <v-form method="POST" :action=" '/' + searchOption">
            <slot name="token"></slot>
            <v-row>
            <v-text-field 
                class="mt-4 mx-3"
                name="searched"
                style="width:200px"
                hide-details
                label="Search for..."
                prepend-icon="mdi-magnify"
                single-line
            ></v-text-field>
            <v-radio-group
                class="mt-5 mx-2"
                v-model=searchOption
                align="center"
                row
            >
            <v-radio
                label="Video"
                value="search-videos"
            ></v-radio>
            <v-radio
                label="Channel"
                value="search-channels"
            ></v-radio>
            </v-radio-group>
            <v-btn
                class="mt-5 mr-5"
                small
                depressed
                type="submit"
            >Search</v-btn>
            </v-row>
        </v-form>
    </v-toolbar>`,
    data() {
        return {
            searchOption: "search-videos"
        }
    }
})