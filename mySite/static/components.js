const Toolbar = Vue.component('toolbar', {
    template:
    `
    <v-toolbar color="black" flat id="toolbar">
        <v-spacer></v-spacer>
        <v-btn class="mx-3" depressed color="#000000" href="/">Videos</v-btn>
        <v-btn class="mr-3" depressed color="#000000" href="/channels">Channels</v-btn>
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
                outlined
                dense
                single-line
            ></v-text-field>
            <v-btn
                class="mt-6 mr-5"
                small
                depressed
                type="submit"
            >Search</v-btn>
            <v-radio-group
                class="mt-6 mx-2"
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
            </v-row>
        </v-form>
    </v-toolbar>`,
    data() {
        return {
            searchOption: "search-videos"
        }
    }
})

const Footer = Vue.component('page-footer', {
    template: `
    <v-footer class="my-5" color="black" padless>
        <v-row>
            <v-col class="text-center" cols="12">
                2021 - tohlh
            </v-col>
        </v-row>
    </v-footer>`,
})

const VideoCard = Vue.component('video-card', {
    template:
    `
    <div>
        <v-card class="rounded-lg" height="300px" elevation="2" :href="'../../video/' + id">
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
        <v-card class="rounded-lg" max-height="280px" elevation="2" :href="'../../channel/' + id">
            <v-img height="180px" :src="profilepic"></v-img>
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

const theme = {
    theme: {
        dark: true,
        themes: {
            dark: {
                primary: "#E040FB",
                secondary: "#673ab7",
                accent: "#E040FB",
            },
        },
    }
}