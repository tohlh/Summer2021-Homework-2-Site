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
        <v-btn depressed color="white" href="/">Videos</v-btn>
        <v-btn depressed color="white" href="/channels">Channels</v-btn>
        <v-form v-if="searchtype == 'video'" method="POST" action="/search-videos">
            <slot name="token"></slot>
            <v-text-field 
                class="mx-3"
                name="searched"
                style="width:200px"
                hide-details
                label="Search for videos"
                prepend-icon="mdi-magnify"
                single-line
            >
            </v-text-field>
        </v-form>
        <v-form v-if="searchtype == 'channel'" method="POST" action="/search-channels">
            <slot name="token"></slot>
            <v-text-field 
                class="mx-3"
                name="searched"
                style="width:200px"
                hide-details
                label="Search for channels"
                prepend-icon="mdi-magnify"
                single-line
            >
            </v-text-field>
        </v-form>
    </v-toolbar>
    `,
    props: ['searchtype']
})