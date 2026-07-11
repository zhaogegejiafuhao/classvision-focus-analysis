<template>
    <div class="component-5517_25829">
        <div id="5517_25829" class="Pixso-symbol-5517_25829">
            <div
                id="5517_25995"
                class="Pixso-symbol-5517_25995"
                v-if="Platform === 'Facebook' && Style === 'Original'"
            ></div>
            <div
                id="5517_25993"
                class="Pixso-symbol-5517_25993"
                v-if="Platform === 'X (Twitter)' && Style === 'Original'"
            >
                <slot name="slot_5517_25994">
                    <div id="5517_25994" class="Pixso-vector-5517_25994"></div>
                </slot>
            </div>
            <div
                id="5517_25989"
                class="Pixso-symbol-5517_25989"
                v-if="Platform === 'Instagram' && Style === 'Original'"
            >
                <slot name="slot_5517_25990">
                    <div id="5517_25990" class="Pixso-vector-5517_25990"></div>
                </slot>
                <slot name="slot_5517_25991">
                    <div id="5517_25991" class="Pixso-vector-5517_25991"></div>
                </slot>
                <slot name="slot_5517_25992">
                    <div id="5517_25992" class="Pixso-vector-5517_25992"></div>
                </slot>
            </div>
            <div
                id="5517_25987"
                class="Pixso-symbol-5517_25987"
                v-if="Platform === 'LinkedIn' && Style === 'Original'"
            ></div>
            <div
                id="5517_25981"
                class="Pixso-symbol-5517_25981"
                v-if="Platform === 'Google' && Style === 'Original'"
            >
                <div id="5517_25982" class="Pixso-group-5517_25982">
                    <slot name="slot_5517_25983">
                        <div
                            id="5517_25983"
                            class="Pixso-vector-5517_25983"
                        ></div>
                    </slot>
                    <slot name="slot_5517_25984">
                        <div
                            id="5517_25984"
                            class="Pixso-vector-5517_25984"
                        ></div>
                    </slot>
                    <slot name="slot_5517_25985">
                        <div
                            id="5517_25985"
                            class="Pixso-vector-5517_25985"
                        ></div>
                    </slot>
                    <slot name="slot_5517_25986">
                        <div
                            id="5517_25986"
                            class="Pixso-vector-5517_25986"
                        ></div>
                    </slot>
                </div>
            </div>
            <div
                id="5517_25978"
                class="Pixso-symbol-5517_25978"
                v-if="Platform === 'YouTube' && Style === 'Original'"
            >
                <slot name="slot_5517_25979">
                    <div id="5517_25979" class="Pixso-vector-5517_25979"></div>
                </slot>
                <slot name="slot_5517_25980">
                    <div id="5517_25980" class="Pixso-vector-5517_25980"></div>
                </slot>
            </div>
            <div
                id="5517_25976"
                class="Pixso-symbol-5517_25976"
                v-if="Platform === 'Apple' && Style === 'Original'"
            >
                <slot name="slot_5517_25977">
                    <div id="5517_25977" class="Pixso-vector-5517_25977"></div>
                </slot>
            </div>
            <div
                id="5517_25973"
                class="Pixso-symbol-5517_25973"
                v-if="Platform === 'Snapchat' && Style === 'Original'"
            >
                <slot name="slot_5517_25974">
                    <div id="5517_25974" class="Pixso-vector-5517_25974"></div>
                </slot>
                <slot name="slot_5517_25975">
                    <div id="5517_25975" class="Pixso-vector-5517_25975"></div>
                </slot>
            </div>
            <div
                id="5517_25970"
                class="Pixso-symbol-5517_25970"
                v-if="Platform === 'Pinterest' && Style === 'Original'"
            ></div>
            <div
                id="5517_25966"
                class="Pixso-symbol-5517_25966"
                v-if="Platform === 'Medium' && Style === 'Original'"
            >
                <slot name="slot_5517_25967">
                    <div id="5517_25967" class="Pixso-vector-5517_25967"></div>
                </slot>
                <slot name="slot_5517_25968">
                    <div id="5517_25968" class="Pixso-vector-5517_25968"></div>
                </slot>
                <slot name="slot_5517_25969">
                    <div id="5517_25969" class="Pixso-vector-5517_25969"></div>
                </slot>
            </div>
            <div
                id="5517_25964"
                class="Pixso-symbol-5517_25964"
                v-if="Platform === 'Github' && Style === 'Original'"
            >
                <slot name="slot_5517_25965">
                    <div id="5517_25965" class="Pixso-vector-5517_25965"></div>
                </slot>
            </div>
            <div
                id="5517_25962"
                class="Pixso-symbol-5517_25962"
                v-if="Platform === 'Threads' && Style === 'Original'"
            >
                <slot name="slot_5517_25963">
                    <div id="5517_25963" class="Pixso-vector-5517_25963"></div>
                </slot>
            </div>
            <div
                id="5517_25960"
                class="Pixso-symbol-5517_25960"
                v-if="Platform === 'WhatsApp' && Style === 'Original'"
            >
                <slot name="slot_5517_25961">
                    <div id="5517_25961" class="Pixso-vector-5517_25961"></div>
                </slot>
            </div>
            <div
                id="5570_32521"
                class="Pixso-symbol-5570_32521"
                v-if="Platform === 'Behance' && Style === 'Original'"
            >
                <slot name="slot_5570_32518">
                    <div id="5570_32518" class="Pixso-vector-5570_32518"></div>
                </slot>
                <slot name="slot_5570_32519">
                    <div id="5570_32519" class="Pixso-vector-5570_32519"></div>
                </slot>
                <slot name="slot_5570_32520">
                    <div id="5570_32520" class="Pixso-vector-5570_32520"></div>
                </slot>
            </div>
            <div
                id="5517_25954"
                class="Pixso-symbol-5517_25954"
                v-if="Platform === 'Figma' && Style === 'Original'"
            >
                <slot name="slot_5517_25955">
                    <div id="5517_25955" class="Pixso-vector-5517_25955"></div>
                </slot>
                <slot name="slot_5517_25956">
                    <div id="5517_25956" class="Pixso-vector-5517_25956"></div>
                </slot>
                <slot name="slot_5517_25957">
                    <div id="5517_25957" class="Pixso-vector-5517_25957"></div>
                </slot>
                <slot name="slot_5517_25958">
                    <div id="5517_25958" class="Pixso-vector-5517_25958"></div>
                </slot>
                <slot name="slot_5517_25959">
                    <div id="5517_25959" class="Pixso-vector-5517_25959"></div>
                </slot>
            </div>
            <div
                id="5517_25949"
                class="Pixso-symbol-5517_25949"
                v-if="Platform === 'Dribbble' && Style === 'Original'"
            >
                <slot name="slot_5517_25950">
                    <div id="5517_25950" class="Pixso-vector-5517_25950"></div>
                </slot>
                <slot name="slot_5517_25951">
                    <div id="5517_25951" class="Pixso-vector-5517_25951"></div>
                </slot>
                <slot name="slot_5517_25952">
                    <div id="5517_25952" class="Pixso-vector-5517_25952"></div>
                </slot>
                <slot name="slot_5517_25953">
                    <div id="5517_25953" class="Pixso-vector-5517_25953"></div>
                </slot>
            </div>
            <div
                id="5517_25930"
                class="Pixso-symbol-5517_25930"
                v-if="Platform === 'Reddit' && Style === 'Original'"
            >
                <div id="5517_25931" class="Pixso-group-5517_25931">
                    <slot name="slot_5517_25932">
                        <div
                            id="5517_25932"
                            class="Pixso-vector-5517_25932"
                        ></div>
                    </slot>
                    <slot name="slot_5517_25933">
                        <div
                            id="5517_25933"
                            class="Pixso-vector-5517_25933"
                        ></div>
                    </slot>
                    <slot name="slot_5517_25934">
                        <div
                            id="5517_25934"
                            class="Pixso-vector-5517_25934"
                        ></div>
                    </slot>
                    <slot name="slot_5517_25935">
                        <div
                            id="5517_25935"
                            class="Pixso-vector-5517_25935"
                        ></div>
                    </slot>
                    <slot name="slot_5517_25936">
                        <div
                            id="5517_25936"
                            class="Pixso-vector-5517_25936"
                        ></div>
                    </slot>
                    <slot name="slot_5517_25937">
                        <div
                            id="5517_25937"
                            class="Pixso-vector-5517_25937"
                        ></div>
                    </slot>
                    <slot name="slot_5517_25938">
                        <div
                            id="5517_25938"
                            class="Pixso-vector-5517_25938"
                        ></div>
                    </slot>
                    <slot name="slot_5517_25939">
                        <div
                            id="5517_25939"
                            class="Pixso-vector-5517_25939"
                        ></div>
                    </slot>
                    <slot name="slot_5517_25940">
                        <div
                            id="5517_25940"
                            class="Pixso-vector-5517_25940"
                        ></div>
                    </slot>
                    <slot name="slot_5517_25941">
                        <div
                            id="5517_25941"
                            class="Pixso-vector-5517_25941"
                        ></div>
                    </slot>
                    <slot name="slot_5517_25942">
                        <div
                            id="5517_25942"
                            class="Pixso-vector-5517_25942"
                        ></div>
                    </slot>
                    <slot name="slot_5517_25943">
                        <div
                            id="5517_25943"
                            class="Pixso-vector-5517_25943"
                        ></div>
                    </slot>
                    <slot name="slot_5517_25944">
                        <div
                            id="5517_25944"
                            class="Pixso-vector-5517_25944"
                        ></div>
                    </slot>
                    <slot name="slot_5517_25945">
                        <div
                            id="5517_25945"
                            class="Pixso-vector-5517_25945"
                        ></div>
                    </slot>
                    <slot name="slot_5517_25946">
                        <div
                            id="5517_25946"
                            class="Pixso-vector-5517_25946"
                        ></div>
                    </slot>
                    <slot name="slot_5517_25947">
                        <div
                            id="5517_25947"
                            class="Pixso-vector-5517_25947"
                        ></div>
                    </slot>
                    <slot name="slot_5517_25948">
                        <div
                            id="5517_25948"
                            class="Pixso-vector-5517_25948"
                        ></div>
                    </slot>
                </div>
            </div>
            <div
                id="5517_25928"
                class="Pixso-symbol-5517_25928"
                v-if="Platform === 'Discord' && Style === 'Original'"
            >
                <slot name="slot_5517_25929">
                    <div id="5517_25929" class="Pixso-vector-5517_25929"></div>
                </slot>
            </div>
            <div
                id="5517_25924"
                class="Pixso-symbol-5517_25924"
                v-if="Platform === 'TikTok' && Style === 'Original'"
            >
                <slot name="slot_5517_25925">
                    <div id="5517_25925" class="Pixso-vector-5517_25925"></div>
                </slot>
                <slot name="slot_5517_25926">
                    <div id="5517_25926" class="Pixso-vector-5517_25926"></div>
                </slot>
                <slot name="slot_5517_25927">
                    <div id="5517_25927" class="Pixso-vector-5517_25927"></div>
                </slot>
            </div>
            <div
                id="5517_25922"
                class="Pixso-symbol-5517_25922"
                v-if="Platform === 'Tumblr' && Style === 'Original'"
            >
                <slot name="slot_5517_25923">
                    <div id="5517_25923" class="Pixso-vector-5517_25923"></div>
                </slot>
            </div>
            <div
                id="5517_25919"
                class="Pixso-symbol-5517_25919"
                v-if="Platform === 'Telegram' && Style === 'Original'"
            >
                <slot name="slot_5517_25920">
                    <div id="5517_25920" class="Pixso-vector-5517_25920"></div>
                </slot>
                <slot name="slot_5517_25921">
                    <div id="5517_25921" class="Pixso-vector-5517_25921"></div>
                </slot>
            </div>
            <div
                id="5517_25911"
                class="Pixso-symbol-5517_25911"
                v-if="Platform === 'Clubhouse' && Style === 'Original'"
            >
                <div id="5517_25912" class="Pixso-group-5517_25912">
                    <slot name="slot_5517_25913">
                        <div
                            id="5517_25913"
                            class="Pixso-vector-5517_25913"
                        ></div>
                    </slot>
                    <slot name="slot_5517_25914">
                        <div
                            id="5517_25914"
                            class="Pixso-vector-5517_25914"
                        ></div>
                    </slot>
                    <slot name="slot_5517_25915">
                        <div
                            id="5517_25915"
                            class="Pixso-vector-5517_25915"
                        ></div>
                    </slot>
                    <slot name="slot_5517_25916">
                        <div
                            id="5517_25916"
                            class="Pixso-vector-5517_25916"
                        ></div>
                    </slot>
                    <slot name="slot_5517_25917">
                        <div
                            id="5517_25917"
                            class="Pixso-vector-5517_25917"
                        ></div>
                    </slot>
                    <slot name="slot_5517_25918">
                        <div
                            id="5517_25918"
                            class="Pixso-vector-5517_25918"
                        ></div>
                    </slot>
                </div>
            </div>
            <div
                id="5517_25909"
                class="Pixso-symbol-5517_25909"
                v-if="Platform === 'Signal' && Style === 'Original'"
            >
                <slot name="slot_5517_25910">
                    <div id="5517_25910" class="Pixso-vector-5517_25910"></div>
                </slot>
            </div>
            <div
                id="5517_25906"
                class="Pixso-symbol-5517_25906"
                v-if="Platform === 'VK' && Style === 'Original'"
            >
                <slot name="slot_5517_25907">
                    <div id="5517_25907" class="Pixso-vector-5517_25907"></div>
                </slot>
                <slot name="slot_5517_25908">
                    <div id="5517_25908" class="Pixso-vector-5517_25908"></div>
                </slot>
            </div>
            <div
                id="5517_25904"
                class="Pixso-symbol-5517_25904"
                v-if="Platform === 'Spotify' && Style === 'Original'"
            >
                <slot name="slot_5517_25905">
                    <div id="5517_25905" class="Pixso-vector-5517_25905"></div>
                </slot>
            </div>
            <div
                id="5517_25899"
                class="Pixso-symbol-5517_25899"
                v-if="Platform === 'Twitch' && Style === 'Original'"
            >
                <slot name="slot_5517_25900">
                    <div id="5517_25900" class="Pixso-vector-5517_25900"></div>
                </slot>
                <slot name="slot_5517_25901">
                    <div id="5517_25901" class="Pixso-vector-5517_25901"></div>
                </slot>
                <slot name="slot_5517_25902">
                    <div id="5517_25902" class="Pixso-vector-5517_25902"></div>
                </slot>
                <slot name="slot_5517_25903">
                    <div id="5517_25903" class="Pixso-vector-5517_25903"></div>
                </slot>
            </div>
            <div
                id="5517_25896"
                class="Pixso-symbol-5517_25896"
                v-if="Platform === 'Messenger' && Style === 'Original'"
            >
                <slot name="slot_5517_25897">
                    <div id="5517_25897" class="Pixso-vector-5517_25897"></div>
                </slot>
                <slot name="slot_5517_25898">
                    <div id="5517_25898" class="Pixso-vector-5517_25898"></div>
                </slot>
            </div>
            <div
                id="5517_25894"
                class="Pixso-symbol-5517_25894"
                v-if="Platform === 'Facebook' && Style === 'White'"
            >
                <slot name="slot_5517_25895">
                    <div id="5517_25895" class="Pixso-vector-5517_25895"></div>
                </slot>
            </div>
            <div
                id="5517_25892"
                class="Pixso-symbol-5517_25892"
                v-if="Platform === 'X (Twitter)' && Style === 'White'"
            >
                <slot name="slot_5517_25893">
                    <div id="5517_25893" class="Pixso-vector-5517_25893"></div>
                </slot>
            </div>
            <div
                id="5517_25888"
                class="Pixso-symbol-5517_25888"
                v-if="Platform === 'Instagram' && Style === 'White'"
            >
                <slot name="slot_5517_25889">
                    <div id="5517_25889" class="Pixso-vector-5517_25889"></div>
                </slot>
                <slot name="slot_5517_25890">
                    <div id="5517_25890" class="Pixso-vector-5517_25890"></div>
                </slot>
                <slot name="slot_5517_25891">
                    <div id="5517_25891" class="Pixso-vector-5517_25891"></div>
                </slot>
            </div>
            <div
                id="5517_25886"
                class="Pixso-symbol-5517_25886"
                v-if="Platform === 'LinkedIn' && Style === 'White'"
            >
                <slot name="slot_5517_25887">
                    <div id="5517_25887" class="Pixso-vector-5517_25887"></div>
                </slot>
            </div>
            <div
                id="5517_25880"
                class="Pixso-symbol-5517_25880"
                v-if="Platform === 'Google' && Style === 'White'"
            >
                <div id="5517_25881" class="Pixso-group-5517_25881">
                    <slot name="slot_5517_25882">
                        <div
                            id="5517_25882"
                            class="Pixso-vector-5517_25882"
                        ></div>
                    </slot>
                    <slot name="slot_5517_25883">
                        <div
                            id="5517_25883"
                            class="Pixso-vector-5517_25883"
                        ></div>
                    </slot>
                    <slot name="slot_5517_25884">
                        <div
                            id="5517_25884"
                            class="Pixso-vector-5517_25884"
                        ></div>
                    </slot>
                    <slot name="slot_5517_25885">
                        <div
                            id="5517_25885"
                            class="Pixso-vector-5517_25885"
                        ></div>
                    </slot>
                </div>
            </div>
            <div
                id="5517_25878"
                class="Pixso-symbol-5517_25878"
                v-if="Platform === 'YouTube' && Style === 'White'"
            >
                <slot name="slot_5517_25879">
                    <div id="5517_25879" class="Pixso-vector-5517_25879"></div>
                </slot>
            </div>
            <div
                id="5517_25876"
                class="Pixso-symbol-5517_25876"
                v-if="Platform === 'Apple' && Style === 'White'"
            >
                <slot name="slot_5517_25877">
                    <div id="5517_25877" class="Pixso-vector-5517_25877"></div>
                </slot>
            </div>
            <div
                id="5517_25874"
                class="Pixso-symbol-5517_25874"
                v-if="Platform === 'Snapchat' && Style === 'White'"
            >
                <slot name="slot_5517_25875">
                    <div id="5517_25875" class="Pixso-vector-5517_25875"></div>
                </slot>
            </div>
            <div
                id="5517_25872"
                class="Pixso-symbol-5517_25872"
                v-if="Platform === 'Pinterest' && Style === 'White'"
            >
                <slot name="slot_5517_25873">
                    <div id="5517_25873" class="Pixso-vector-5517_25873"></div>
                </slot>
            </div>
            <div
                id="5517_25868"
                class="Pixso-symbol-5517_25868"
                v-if="Platform === 'Medium' && Style === 'White'"
            >
                <slot name="slot_5517_25869">
                    <div id="5517_25869" class="Pixso-vector-5517_25869"></div>
                </slot>
                <slot name="slot_5517_25870">
                    <div id="5517_25870" class="Pixso-vector-5517_25870"></div>
                </slot>
                <slot name="slot_5517_25871">
                    <div id="5517_25871" class="Pixso-vector-5517_25871"></div>
                </slot>
            </div>
            <div
                id="5517_25866"
                class="Pixso-symbol-5517_25866"
                v-if="Platform === 'Github' && Style === 'White'"
            >
                <slot name="slot_5517_25867">
                    <div id="5517_25867" class="Pixso-vector-5517_25867"></div>
                </slot>
            </div>
            <div
                id="5517_25864"
                class="Pixso-symbol-5517_25864"
                v-if="Platform === 'Threads' && Style === 'White'"
            >
                <slot name="slot_5517_25865">
                    <div id="5517_25865" class="Pixso-vector-5517_25865"></div>
                </slot>
            </div>
            <div
                id="5517_25862"
                class="Pixso-symbol-5517_25862"
                v-if="Platform === 'WhatsApp' && Style === 'White'"
            >
                <slot name="slot_5517_25863">
                    <div id="5517_25863" class="Pixso-vector-5517_25863"></div>
                </slot>
            </div>
            <div
                id="5570_32526"
                class="Pixso-symbol-5570_32526"
                v-if="Platform === 'Behance' && Style === 'White'"
            >
                <slot name="slot_5570_32527">
                    <div id="5570_32527" class="Pixso-vector-5570_32527"></div>
                </slot>
                <slot name="slot_5570_32528">
                    <div id="5570_32528" class="Pixso-vector-5570_32528"></div>
                </slot>
                <slot name="slot_5570_32529">
                    <div id="5570_32529" class="Pixso-vector-5570_32529"></div>
                </slot>
            </div>
            <div
                id="5517_25860"
                class="Pixso-symbol-5517_25860"
                v-if="Platform === 'Figma' && Style === 'White'"
            >
                <slot name="slot_5517_25861">
                    <div id="5517_25861" class="Pixso-vector-5517_25861"></div>
                </slot>
            </div>
            <div
                id="5517_25858"
                class="Pixso-symbol-5517_25858"
                v-if="Platform === 'Dribbble' && Style === 'White'"
            >
                <slot name="slot_5517_25859">
                    <div id="5517_25859" class="Pixso-vector-5517_25859"></div>
                </slot>
            </div>
            <div
                id="5517_25856"
                class="Pixso-symbol-5517_25856"
                v-if="Platform === 'Reddit' && Style === 'White'"
            >
                <slot name="slot_5517_25857">
                    <div id="5517_25857" class="Pixso-vector-5517_25857"></div>
                </slot>
            </div>
            <div
                id="5517_25854"
                class="Pixso-symbol-5517_25854"
                v-if="Platform === 'Discord' && Style === 'White'"
            >
                <slot name="slot_5517_25855">
                    <div id="5517_25855" class="Pixso-vector-5517_25855"></div>
                </slot>
            </div>
            <div
                id="5517_25852"
                class="Pixso-symbol-5517_25852"
                v-if="Platform === 'TikTok' && Style === 'White'"
            >
                <slot name="slot_5517_25853">
                    <div id="5517_25853" class="Pixso-vector-5517_25853"></div>
                </slot>
            </div>
            <div
                id="5517_25850"
                class="Pixso-symbol-5517_25850"
                v-if="Platform === 'Tumblr' && Style === 'White'"
            >
                <slot name="slot_5517_25851">
                    <div id="5517_25851" class="Pixso-vector-5517_25851"></div>
                </slot>
            </div>
            <div
                id="5517_25848"
                class="Pixso-symbol-5517_25848"
                v-if="Platform === 'Telegram' && Style === 'White'"
            >
                <slot name="slot_5517_25849">
                    <div id="5517_25849" class="Pixso-vector-5517_25849"></div>
                </slot>
            </div>
            <div
                id="5517_25842"
                class="Pixso-symbol-5517_25842"
                v-if="Platform === 'Clubhouse' && Style === 'White'"
            >
                <div id="5517_25843" class="Pixso-group-5517_25843">
                    <slot name="slot_5517_25844">
                        <div
                            id="5517_25844"
                            class="Pixso-vector-5517_25844"
                        ></div>
                    </slot>
                    <slot name="slot_5517_25845">
                        <div
                            id="5517_25845"
                            class="Pixso-vector-5517_25845"
                        ></div>
                    </slot>
                    <slot name="slot_5517_25846">
                        <div
                            id="5517_25846"
                            class="Pixso-vector-5517_25846"
                        ></div>
                    </slot>
                    <slot name="slot_5517_25847">
                        <div
                            id="5517_25847"
                            class="Pixso-vector-5517_25847"
                        ></div>
                    </slot>
                </div>
            </div>
            <div
                id="5517_25840"
                class="Pixso-symbol-5517_25840"
                v-if="Platform === 'Signal' && Style === 'White'"
            >
                <slot name="slot_5517_25841">
                    <div id="5517_25841" class="Pixso-vector-5517_25841"></div>
                </slot>
            </div>
            <div
                id="5517_25838"
                class="Pixso-symbol-5517_25838"
                v-if="Platform === 'VK' && Style === 'White'"
            >
                <slot name="slot_5517_25839">
                    <div id="5517_25839" class="Pixso-vector-5517_25839"></div>
                </slot>
            </div>
            <div
                id="5517_25836"
                class="Pixso-symbol-5517_25836"
                v-if="Platform === 'Spotify' && Style === 'White'"
            >
                <slot name="slot_5517_25837">
                    <div id="5517_25837" class="Pixso-vector-5517_25837"></div>
                </slot>
            </div>
            <div
                id="5517_25832"
                class="Pixso-symbol-5517_25832"
                v-if="Platform === 'Twitch' && Style === 'White'"
            >
                <slot name="slot_5517_25833">
                    <div id="5517_25833" class="Pixso-vector-5517_25833"></div>
                </slot>
                <slot name="slot_5517_25834">
                    <div id="5517_25834" class="Pixso-vector-5517_25834"></div>
                </slot>
                <slot name="slot_5517_25835">
                    <div id="5517_25835" class="Pixso-vector-5517_25835"></div>
                </slot>
            </div>
            <div
                id="5517_25830"
                class="Pixso-symbol-5517_25830"
                v-if="Platform === 'Messenger' && Style === 'White'"
            >
                <slot name="slot_5517_25831">
                    <div id="5517_25831" class="Pixso-vector-5517_25831"></div>
                </slot>
            </div>
            <div
                id="5517_25998"
                class="Pixso-symbol-5517_25998"
                v-if="Platform === 'Facebook' && Style === 'Dark'"
            >
                <slot name="slot_5517_25999">
                    <div id="5517_25999" class="Pixso-vector-5517_25999"></div>
                </slot>
            </div>
            <div
                id="5517_26000"
                class="Pixso-symbol-5517_26000"
                v-if="Platform === 'X (Twitter)' && Style === 'Dark'"
            >
                <slot name="slot_5517_26001">
                    <div id="5517_26001" class="Pixso-vector-5517_26001"></div>
                </slot>
            </div>
            <div
                id="5517_26002"
                class="Pixso-symbol-5517_26002"
                v-if="Platform === 'Instagram' && Style === 'Dark'"
            >
                <slot name="slot_5517_26003">
                    <div id="5517_26003" class="Pixso-vector-5517_26003"></div>
                </slot>
                <slot name="slot_5517_26004">
                    <div id="5517_26004" class="Pixso-vector-5517_26004"></div>
                </slot>
                <slot name="slot_5517_26005">
                    <div id="5517_26005" class="Pixso-vector-5517_26005"></div>
                </slot>
            </div>
            <div
                id="5517_26006"
                class="Pixso-symbol-5517_26006"
                v-if="Platform === 'LinkedIn' && Style === 'Dark'"
            >
                <slot name="slot_5517_26007">
                    <div id="5517_26007" class="Pixso-vector-5517_26007"></div>
                </slot>
            </div>
            <div
                id="5517_26008"
                class="Pixso-symbol-5517_26008"
                v-if="Platform === 'Google' && Style === 'Dark'"
            >
                <div id="5517_26009" class="Pixso-group-5517_26009">
                    <slot name="slot_5517_26010">
                        <div
                            id="5517_26010"
                            class="Pixso-vector-5517_26010"
                        ></div>
                    </slot>
                    <slot name="slot_5517_26011">
                        <div
                            id="5517_26011"
                            class="Pixso-vector-5517_26011"
                        ></div>
                    </slot>
                    <slot name="slot_5517_26012">
                        <div
                            id="5517_26012"
                            class="Pixso-vector-5517_26012"
                        ></div>
                    </slot>
                    <slot name="slot_5517_26013">
                        <div
                            id="5517_26013"
                            class="Pixso-vector-5517_26013"
                        ></div>
                    </slot>
                </div>
            </div>
            <div
                id="5517_26014"
                class="Pixso-symbol-5517_26014"
                v-if="Platform === 'YouTube' && Style === 'Dark'"
            >
                <slot name="slot_5517_26015">
                    <div id="5517_26015" class="Pixso-vector-5517_26015"></div>
                </slot>
            </div>
            <div
                id="5517_26016"
                class="Pixso-symbol-5517_26016"
                v-if="Platform === 'Apple' && Style === 'Dark'"
            >
                <slot name="slot_5517_26017">
                    <div id="5517_26017" class="Pixso-vector-5517_26017"></div>
                </slot>
            </div>
            <div
                id="5517_26018"
                class="Pixso-symbol-5517_26018"
                v-if="Platform === 'Snapchat' && Style === 'Dark'"
            >
                <slot name="slot_5517_26019">
                    <div id="5517_26019" class="Pixso-vector-5517_26019"></div>
                </slot>
            </div>
            <div
                id="5517_26020"
                class="Pixso-symbol-5517_26020"
                v-if="Platform === 'Pinterest' && Style === 'Dark'"
            >
                <slot name="slot_5517_26021">
                    <div id="5517_26021" class="Pixso-vector-5517_26021"></div>
                </slot>
            </div>
            <div
                id="5517_26022"
                class="Pixso-symbol-5517_26022"
                v-if="Platform === 'Medium' && Style === 'Dark'"
            >
                <slot name="slot_5517_26023">
                    <div id="5517_26023" class="Pixso-vector-5517_26023"></div>
                </slot>
                <slot name="slot_5517_26024">
                    <div id="5517_26024" class="Pixso-vector-5517_26024"></div>
                </slot>
                <slot name="slot_5517_26025">
                    <div id="5517_26025" class="Pixso-vector-5517_26025"></div>
                </slot>
            </div>
            <div
                id="5517_26026"
                class="Pixso-symbol-5517_26026"
                v-if="Platform === 'Github' && Style === 'Dark'"
            >
                <slot name="slot_5517_26027">
                    <div id="5517_26027" class="Pixso-vector-5517_26027"></div>
                </slot>
            </div>
            <div
                id="5517_26028"
                class="Pixso-symbol-5517_26028"
                v-if="Platform === 'Threads' && Style === 'Dark'"
            >
                <slot name="slot_5517_26029">
                    <div id="5517_26029" class="Pixso-vector-5517_26029"></div>
                </slot>
            </div>
            <div
                id="5517_26030"
                class="Pixso-symbol-5517_26030"
                v-if="Platform === 'WhatsApp' && Style === 'Dark'"
            >
                <slot name="slot_5517_26031">
                    <div id="5517_26031" class="Pixso-vector-5517_26031"></div>
                </slot>
            </div>
            <div
                id="5570_32534"
                class="Pixso-symbol-5570_32534"
                v-if="Platform === 'Behance' && Style === 'Dark'"
            >
                <slot name="slot_5570_32535">
                    <div id="5570_32535" class="Pixso-vector-5570_32535"></div>
                </slot>
                <slot name="slot_5570_32536">
                    <div id="5570_32536" class="Pixso-vector-5570_32536"></div>
                </slot>
                <slot name="slot_5570_32537">
                    <div id="5570_32537" class="Pixso-vector-5570_32537"></div>
                </slot>
            </div>
            <div
                id="5517_26032"
                class="Pixso-symbol-5517_26032"
                v-if="Platform === 'Figma' && Style === 'Dark'"
            >
                <slot name="slot_5517_26033">
                    <div id="5517_26033" class="Pixso-vector-5517_26033"></div>
                </slot>
            </div>
            <div
                id="5517_26034"
                class="Pixso-symbol-5517_26034"
                v-if="Platform === 'Dribbble' && Style === 'Dark'"
            >
                <slot name="slot_5517_26035">
                    <div id="5517_26035" class="Pixso-vector-5517_26035"></div>
                </slot>
            </div>
            <div
                id="5517_26036"
                class="Pixso-symbol-5517_26036"
                v-if="Platform === 'Reddit' && Style === 'Dark'"
            >
                <slot name="slot_5517_26037">
                    <div id="5517_26037" class="Pixso-vector-5517_26037"></div>
                </slot>
            </div>
            <div
                id="5517_26038"
                class="Pixso-symbol-5517_26038"
                v-if="Platform === 'Discord' && Style === 'Dark'"
            >
                <slot name="slot_5517_26039">
                    <div id="5517_26039" class="Pixso-vector-5517_26039"></div>
                </slot>
            </div>
            <div
                id="5517_26040"
                class="Pixso-symbol-5517_26040"
                v-if="Platform === 'TikTok' && Style === 'Dark'"
            >
                <slot name="slot_5517_26041">
                    <div id="5517_26041" class="Pixso-vector-5517_26041"></div>
                </slot>
            </div>
            <div
                id="5517_26042"
                class="Pixso-symbol-5517_26042"
                v-if="Platform === 'Tumblr' && Style === 'Dark'"
            >
                <slot name="slot_5517_26043">
                    <div id="5517_26043" class="Pixso-vector-5517_26043"></div>
                </slot>
            </div>
            <div
                id="5517_26044"
                class="Pixso-symbol-5517_26044"
                v-if="Platform === 'Telegram' && Style === 'Dark'"
            >
                <slot name="slot_5517_26045">
                    <div id="5517_26045" class="Pixso-vector-5517_26045"></div>
                </slot>
            </div>
            <div
                id="5517_26046"
                class="Pixso-symbol-5517_26046"
                v-if="Platform === 'Clubhouse' && Style === 'Dark'"
            >
                <div id="5517_26047" class="Pixso-group-5517_26047">
                    <slot name="slot_5517_26048">
                        <div
                            id="5517_26048"
                            class="Pixso-vector-5517_26048"
                        ></div>
                    </slot>
                    <slot name="slot_5517_26049">
                        <div
                            id="5517_26049"
                            class="Pixso-vector-5517_26049"
                        ></div>
                    </slot>
                    <slot name="slot_5517_26050">
                        <div
                            id="5517_26050"
                            class="Pixso-vector-5517_26050"
                        ></div>
                    </slot>
                    <slot name="slot_5517_26051">
                        <div
                            id="5517_26051"
                            class="Pixso-vector-5517_26051"
                        ></div>
                    </slot>
                </div>
            </div>
            <div
                id="5517_26052"
                class="Pixso-symbol-5517_26052"
                v-if="Platform === 'Signal' && Style === 'Dark'"
            >
                <slot name="slot_5517_26053">
                    <div id="5517_26053" class="Pixso-vector-5517_26053"></div>
                </slot>
            </div>
            <div
                id="5517_26054"
                class="Pixso-symbol-5517_26054"
                v-if="Platform === 'VK' && Style === 'Dark'"
            >
                <slot name="slot_5517_26055">
                    <div id="5517_26055" class="Pixso-vector-5517_26055"></div>
                </slot>
            </div>
            <div
                id="5517_26056"
                class="Pixso-symbol-5517_26056"
                v-if="Platform === 'Spotify' && Style === 'Dark'"
            >
                <slot name="slot_5517_26057">
                    <div id="5517_26057" class="Pixso-vector-5517_26057"></div>
                </slot>
            </div>
            <div
                id="5517_26058"
                class="Pixso-symbol-5517_26058"
                v-if="Platform === 'Twitch' && Style === 'Dark'"
            >
                <slot name="slot_5517_26059">
                    <div id="5517_26059" class="Pixso-vector-5517_26059"></div>
                </slot>
                <slot name="slot_5517_26060">
                    <div id="5517_26060" class="Pixso-vector-5517_26060"></div>
                </slot>
                <slot name="slot_5517_26061">
                    <div id="5517_26061" class="Pixso-vector-5517_26061"></div>
                </slot>
            </div>
            <div
                id="5517_26062"
                class="Pixso-symbol-5517_26062"
                v-if="Platform === 'Messenger' && Style === 'Dark'"
            >
                <slot name="slot_5517_26063">
                    <div id="5517_26063" class="Pixso-vector-5517_26063"></div>
                </slot>
            </div>
        </div>
    </div>
</template>
<script lang="ts" setup>
const props = defineProps({
    Platform: { type: String },
    Style: { type: String }
});
</script>
<style>
.Pixso-symbol-5517_25829 {
}
.Pixso-symbol-5517_25995 {
    width: 24px;
    height: 24px;
    background-image: url(@/assets/images/PlatformFacebookStyleOriginal0.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    overflow: hidden;
    position: relative;
    background-color: transparent;
}
.Pixso-symbol-5517_25993 {
    width: 24px;
    height: 24px;
    overflow: hidden;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5517_25994 {
    width: 91.66%;
    height: 82.86%;
    background-image: url(@/assets/images/Vector294.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 4.17%;
    right: 4.17%;
    top: 7.93%;
    bottom: 9.21%;
}
.Pixso-symbol-5517_25989 {
    width: 24px;
    height: 24px;
    overflow: hidden;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5517_25990 {
    width: 99.94%;
    height: 99.98%;
    background-image: url(@/assets/images/Vector283.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 0%;
    right: 0.06%;
    top: 0%;
    bottom: 0.02%;
}
.Pixso-vector-5517_25991 {
    width: 51.36%;
    height: 51.36%;
    background-image: url(@/assets/images/Vector284.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 24.32%;
    right: 24.32%;
    top: 24.32%;
    bottom: 24.32%;
}
.Pixso-vector-5517_25992 {
    width: 12%;
    height: 12%;
    background-image: url(@/assets/images/Vector282.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 70.7%;
    right: 17.3%;
    top: 17.3%;
    bottom: 70.7%;
}
.Pixso-symbol-5517_25987 {
    width: 24px;
    height: 24px;
    background-image: url(@/assets/images/PlatformLinkedInStyleOriginal0.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    overflow: hidden;
    position: relative;
    background-color: transparent;
}
.Pixso-symbol-5517_25981 {
    width: 24px;
    height: 24px;
    overflow: hidden;
    position: relative;
    background-color: transparent;
}
.Pixso-group-5517_25982 {
    width: 23.519753px;
    height: 24px;
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translateX(calc(-50% + -0.24012349999999927px))
        translateY(calc(-50% + 0px));
}
.Pixso-vector-5517_25983 {
    width: 48.98%;
    height: 47%;
    background-image: url(@/assets/images/Vector288.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 51.02%;
    right: 0%;
    top: 40.91%;
    bottom: 12.09%;
}
.Pixso-vector-5517_25984 {
    width: 79.32%;
    height: 40.48%;
    background-image: url(@/assets/images/Vector287.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 5.47%;
    right: 15.21%;
    top: 59.52%;
    bottom: 0%;
}
.Pixso-vector-5517_25985 {
    width: 22.45%;
    height: 44.82%;
    background-image: url(@/assets/images/Vector286.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 0%;
    right: 77.55%;
    top: 27.59%;
    bottom: 27.59%;
}
.Pixso-vector-5517_25986 {
    width: 79.69%;
    height: 40.5%;
    background-image: url(@/assets/images/Vector285.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 5.47%;
    right: 14.84%;
    top: 0%;
    bottom: 59.5%;
}
.Pixso-symbol-5517_25978 {
    width: 24px;
    height: 24px;
    overflow: hidden;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5517_25979 {
    width: 100%;
    height: 70.46%;
    background-image: url(@/assets/images/Vector215.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 0.1%;
    right: -0.1%;
    top: 14.77%;
    bottom: 14.77%;
}
.Pixso-vector-5517_25980 {
    width: 26.14%;
    height: 29.74%;
    background-image: url(@/assets/images/Vector216.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 39.87%;
    right: 33.99%;
    top: 35.13%;
    bottom: 35.13%;
}
.Pixso-symbol-5517_25976 {
    width: 24px;
    height: 24px;
    overflow: hidden;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5517_25977 {
    width: 84.24%;
    height: 100%;
    background-image: url(@/assets/images/Vector214.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 8.33%;
    right: 7.43%;
    top: 0%;
    bottom: 0%;
}
.Pixso-symbol-5517_25973 {
    width: 24px;
    height: 24px;
    position: relative;
}
.Pixso-vector-5517_25974 {
    width: 88.32%;
    height: 87.29%;
    background-image: url(@/assets/images/Vector213.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 5.85%;
    right: 5.83%;
    top: 6.32%;
    bottom: 6.39%;
}
.Pixso-vector-5517_25975 {
    width: 100%;
    height: 98.52%;
    background-image: url(@/assets/images/Vector212.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 0%;
    right: 0%;
    top: 0.73%;
    bottom: 0.75%;
}
.Pixso-symbol-5517_25970 {
    width: 24px;
    height: 24px;
    background-image: url(@/assets/images/PlatformPinterestStyleOriginal0.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    overflow: hidden;
    position: relative;
    background-color: transparent;
}
.Pixso-symbol-5517_25966 {
    width: 24px;
    height: 24px;
    overflow: hidden;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5517_25967 {
    width: 9.92%;
    height: 47.98%;
    background-image: url(@/assets/images/Vector211.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 90.08%;
    right: 0%;
    top: 25.29%;
    bottom: 26.73%;
}
.Pixso-vector-5517_25968 {
    width: 28.2%;
    height: 53.56%;
    background-image: url(@/assets/images/Vector210.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 59.14%;
    right: 12.66%;
    top: 22.5%;
    bottom: 23.94%;
}
.Pixso-vector-5517_25969 {
    width: 56.41%;
    height: 56.9%;
    background-image: url(@/assets/images/Vector209.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 0%;
    right: 43.59%;
    top: 20.83%;
    bottom: 22.27%;
}
.Pixso-symbol-5517_25964 {
    width: 24px;
    height: 24px;
    overflow: hidden;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5517_25965 {
    width: 100%;
    height: 98.33%;
    background-image: url(@/assets/images/Vector208.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 0%;
    right: 0%;
    top: 0%;
    bottom: 1.67%;
}
.Pixso-symbol-5517_25962 {
    width: 24px;
    height: 24px;
    overflow: hidden;
    position: relative;
}
.Pixso-vector-5517_25963 {
    width: 86.03%;
    height: 100%;
    background-image: url(@/assets/images/Vector207.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 6.77%;
    right: 7.2%;
    top: 0%;
    bottom: 0%;
}
.Pixso-symbol-5517_25960 {
    width: 24.000053px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5517_25961 {
    width: 99.52%;
    height: 100%;
    background-image: url(@/assets/images/Vector206.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 0%;
    right: 0.48%;
    top: 0%;
    bottom: 0%;
}
.Pixso-symbol-5570_32521 {
    width: 24px;
    height: 24px;
    overflow: hidden;
    position: relative;
}
.Pixso-vector-5570_32518 {
    width: 42.9%;
    height: 53.96%;
    background-image: url(@/assets/images/vector1.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 8.33%;
    right: 48.77%;
    top: 22.51%;
    bottom: 23.53%;
}
.Pixso-vector-5570_32519 {
    width: 37.15%;
    height: 41.2%;
    background-image: url(@/assets/images/vector0.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 54.52%;
    right: 8.33%;
    top: 36.29%;
    bottom: 22.51%;
}
.Pixso-vector-5570_32520 {
    width: 20.75%;
    height: 5.3%;
    background-image: url(@/assets/images/vector.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 62.65%;
    right: 16.6%;
    top: 26.12%;
    bottom: 68.58%;
}
.Pixso-symbol-5517_25954 {
    width: 24px;
    height: 24px;
    overflow: hidden;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5517_25955 {
    width: 33.33%;
    height: 33.33%;
    background-image: url(@/assets/images/Vector201.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 16.67%;
    right: 50%;
    top: 66.67%;
    bottom: 0%;
}
.Pixso-vector-5517_25956 {
    width: 33.33%;
    height: 33.34%;
    background-image: url(@/assets/images/Vector202.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 16.67%;
    right: 50%;
    top: 33.33%;
    bottom: 33.33%;
}
.Pixso-vector-5517_25957 {
    width: 33.33%;
    height: 33.33%;
    background-image: url(@/assets/images/Vector205.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 16.67%;
    right: 50%;
    top: 0%;
    bottom: 66.67%;
}
.Pixso-vector-5517_25958 {
    width: 33.33%;
    height: 33.33%;
    background-image: url(@/assets/images/Vector204.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 50%;
    right: 16.67%;
    top: 0%;
    bottom: 66.67%;
}
.Pixso-vector-5517_25959 {
    width: 33.33%;
    height: 33.34%;
    background-image: url(@/assets/images/Vector203.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 50%;
    right: 16.67%;
    top: 33.33%;
    bottom: 33.33%;
}
.Pixso-symbol-5517_25949 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5517_25950 {
    width: 100%;
    height: 100%;
    background-image: url(@/assets/images/Vector197.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 0%;
    right: 0%;
    top: 0%;
    bottom: 0%;
}
.Pixso-vector-5517_25951 {
    width: 96.88%;
    height: 96.88%;
    background-image: url(@/assets/images/Vector198.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 1.56%;
    right: 1.56%;
    top: 1.56%;
    bottom: 1.56%;
}
.Pixso-vector-5517_25952 {
    width: 100%;
    height: 100%;
    background-image: url(@/assets/images/Vector200.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 0%;
    right: 0%;
    top: 0%;
    bottom: 0%;
}
.Pixso-vector-5517_25953 {
    width: 100%;
    height: 100%;
    background-image: url(@/assets/images/Vector199.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 0%;
    right: 0%;
    top: 0%;
    bottom: 0%;
}
.Pixso-symbol-5517_25930 {
    width: 24px;
    height: 24px;
    overflow: hidden;
    position: relative;
}
.Pixso-group-5517_25931 {
    width: 24px;
    height: 24px;
    position: absolute;
    left: 0px;
    top: 0px;
}
.Pixso-vector-5517_25932 {
    width: 100%;
    height: 100%;
    background-image: url(@/assets/images/Vector194.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 0%;
    right: 0%;
    top: 0%;
    bottom: 0%;
}
.Pixso-vector-5517_25933 {
    width: 23.35%;
    height: 23.36%;
    background-image: url(@/assets/images/Vector191.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 66.67%;
    right: 9.98%;
    top: 36.62%;
    bottom: 40.02%;
}
.Pixso-vector-5517_25934 {
    width: 23.35%;
    height: 23.36%;
    background-image: url(@/assets/images/Vector185.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 9.98%;
    right: 66.67%;
    top: 36.62%;
    bottom: 40.02%;
}
.Pixso-vector-5517_25935 {
    width: 66.66%;
    height: 50%;
    background-image: url(@/assets/images/Vector182.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 16.7%;
    right: 16.64%;
    top: 33.33%;
    bottom: 16.67%;
}
.Pixso-vector-5517_25936 {
    width: 11.87%;
    height: 13.45%;
    background-image: url(@/assets/images/Vector184.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 28.31%;
    right: 59.82%;
    top: 48.23%;
    bottom: 38.32%;
}
.Pixso-vector-5517_25937 {
    width: 11.88%;
    height: 13.44%;
    background-image: url(@/assets/images/Vector186.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 59.87%;
    right: 28.25%;
    top: 48.23%;
    bottom: 38.33%;
}
.Pixso-vector-5517_25938 {
    width: 11.11%;
    height: 12.67%;
    background-image: url(@/assets/images/Vector192.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 59.87%;
    right: 29.02%;
    top: 49%;
    bottom: 38.33%;
}
.Pixso-vector-5517_25939 {
    width: 11.11%;
    height: 12.67%;
    background-image: url(@/assets/images/Vector190.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 29.08%;
    right: 59.81%;
    top: 49%;
    bottom: 38.33%;
}
.Pixso-vector-5517_25940 {
    width: 25.22%;
    height: 10.02%;
    background-image: url(@/assets/images/Vector189.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 37.42%;
    right: 37.36%;
    top: 64.5%;
    bottom: 25.48%;
}
.Pixso-vector-5517_25941 {
    width: 25.14%;
    height: 10.18%;
    background-image: url(@/assets/images/Vector188.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 37.46%;
    right: 37.4%;
    top: 65.42%;
    bottom: 24.4%;
}
.Pixso-vector-5517_25942 {
    width: 24.75%;
    height: 10.02%;
    background-image: url(@/assets/images/Vector183.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 37.65%;
    right: 37.6%;
    top: 64.94%;
    bottom: 25.04%;
}
.Pixso-vector-5517_25943 {
    width: 16.55%;
    height: 16.54%;
    background-image: url(@/assets/images/Vector195.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 60.01%;
    right: 23.44%;
    top: 13.39%;
    bottom: 70.07%;
}
.Pixso-vector-5517_25944 {
    width: 15.23%;
    height: 14.5%;
    background-image: url(@/assets/images/Vector196.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 48.12%;
    right: 36.65%;
    top: 19.89%;
    bottom: 65.61%;
}
.Pixso-vector-5517_25945 {
    width: 7.29%;
    height: 5%;
    background-image: url(@/assets/images/Vector193.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 30.71%;
    right: 62%;
    top: 55.45%;
    bottom: 39.55%;
}
.Pixso-vector-5517_25946 {
    width: 7.29%;
    height: 5%;
    background-image: url(@/assets/images/Vector187.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 62.06%;
    right: 30.65%;
    top: 55.45%;
    bottom: 39.55%;
}
.Pixso-vector-5517_25947 {
    width: 2.59%;
    height: 2.83%;
    background-image: url(@/assets/images/Vector181.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 35.57%;
    right: 61.84%;
    top: 51.24%;
    bottom: 45.93%;
}
.Pixso-vector-5517_25948 {
    width: 2.6%;
    height: 2.83%;
    background-image: url(@/assets/images/Vector180.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 66.39%;
    right: 31.01%;
    top: 51.24%;
    bottom: 45.93%;
}
.Pixso-symbol-5517_25928 {
    width: 24px;
    height: 24px;
    overflow: hidden;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5517_25929 {
    width: 100%;
    height: 76.22%;
    background-image: url(@/assets/images/Vector179.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 0%;
    right: 0%;
    top: 11%;
    bottom: 12.78%;
}
.Pixso-symbol-5517_25924 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5517_25925 {
    width: 74.72%;
    height: 96%;
    background-image: url(@/assets/images/Vector178.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 19.67%;
    right: 5.61%;
    top: 4%;
    bottom: 0%;
}
.Pixso-vector-5517_25926 {
    width: 78.55%;
    height: 92%;
    background-image: url(@/assets/images/Vector177.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 11.04%;
    right: 10.41%;
    top: 4%;
    bottom: 4%;
}
.Pixso-vector-5517_25927 {
    width: 83.34%;
    height: 90.86%;
    background-image: url(@/assets/images/Vector176.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 6.25%;
    right: 10.41%;
    top: 0%;
    bottom: 9.14%;
}
.Pixso-symbol-5517_25922 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5517_25923 {
    width: 56.67%;
    height: 100%;
    background-image: url(@/assets/images/Vector175.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 20.83%;
    right: 22.5%;
    top: 0%;
    bottom: 0%;
}
.Pixso-symbol-5517_25919 {
    width: 24px;
    height: 24px;
    overflow: hidden;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5517_25920 {
    width: 100%;
    height: 100%;
    background-image: url(@/assets/images/Vector174.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 0%;
    right: 0%;
    top: 0%;
    bottom: 0%;
}
.Pixso-vector-5517_25921 {
    width: 54.3%;
    height: 45%;
    background-image: url(@/assets/images/Vector173.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 18.9%;
    right: 26.8%;
    top: 30.1%;
    bottom: 24.9%;
}
.Pixso-symbol-5517_25911 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-group-5517_25912 {
    width: 23.609318px;
    height: 19.441521px;
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translateX(calc(-50% + -0.19534100000000088px))
        translateY(calc(-50% + 0.2207605000000008px));
}
.Pixso-vector-5517_25913 {
    width: 75.61%;
    height: 100%;
    background-image: url(@/assets/images/Vector172.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 24.39%;
    right: 0%;
    top: 0%;
    bottom: 0%;
}
.Pixso-vector-5517_25914 {
    width: 67.11%;
    height: 85.91%;
    background-image: url(@/assets/images/Vector171.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 28.62%;
    right: 4.27%;
    top: 8.96%;
    bottom: 5.13%;
}
.Pixso-vector-5517_25915 {
    width: 16.28%;
    height: 40.34%;
    background-image: url(@/assets/images/Vector169.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 47.25%;
    right: 36.47%;
    top: 5.16%;
    bottom: 54.5%;
}
.Pixso-vector-5517_25916 {
    width: 16.51%;
    height: 12.97%;
    background-image: url(@/assets/images/Vector167.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 6.84%;
    right: 76.65%;
    top: 61.57%;
    bottom: 25.46%;
}
.Pixso-vector-5517_25917 {
    width: 17.43%;
    height: 8.29%;
    background-image: url(@/assets/images/Vector168.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 0%;
    right: 82.57%;
    top: 38.53%;
    bottom: 53.18%;
}
.Pixso-vector-5517_25918 {
    width: 16.17%;
    height: 15.26%;
    background-image: url(@/assets/images/Vector170.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 3.37%;
    right: 80.46%;
    top: 9.91%;
    bottom: 74.83%;
}
.Pixso-symbol-5517_25909 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5517_25910 {
    width: 100%;
    height: 100%;
    background-image: url(@/assets/images/Vector166.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 0%;
    right: 0%;
    top: 0%;
    bottom: 0%;
}
.Pixso-symbol-5517_25906 {
    width: 24px;
    height: 24px;
    overflow: hidden;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5517_25907 {
    width: 100%;
    height: 100%;
    background-image: url(@/assets/images/Vector165.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 0%;
    right: 0%;
    top: 0%;
    bottom: 0%;
}
.Pixso-vector-5517_25908 {
    width: 66.7%;
    height: 41.62%;
    background-image: url(@/assets/images/Vector164.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 16.88%;
    right: 16.42%;
    top: 30.42%;
    bottom: 27.96%;
}
.Pixso-symbol-5517_25904 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5517_25905 {
    width: 99.69%;
    height: 99.69%;
    background-image: url(@/assets/images/Vector163.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 0%;
    right: 0.31%;
    top: 0%;
    bottom: 0.31%;
}
.Pixso-symbol-5517_25899 {
    width: 24px;
    height: 24px;
    overflow: hidden;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5517_25900 {
    width: 57.15%;
    height: 66.07%;
    background-image: url(@/assets/images/Vector162.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 28.57%;
    right: 14.28%;
    top: 7.14%;
    bottom: 26.79%;
}
.Pixso-vector-5517_25901 {
    width: 85.71%;
    height: 100%;
    background-image: url(@/assets/images/Vector161.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 7.15%;
    right: 7.14%;
    top: 0%;
    bottom: 0%;
}
.Pixso-vector-5517_25902 {
    width: 7.14%;
    height: 21.43%;
    background-image: url(@/assets/images/Vector160.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 67.86%;
    right: 25%;
    top: 19.64%;
    bottom: 58.93%;
}
.Pixso-vector-5517_25903 {
    width: 7.14%;
    height: 21.43%;
    background-image: url(@/assets/images/Vector159.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 48.22%;
    right: 44.64%;
    top: 19.64%;
    bottom: 58.93%;
}
.Pixso-symbol-5517_25896 {
    width: 24px;
    height: 24.00066px;
    position: relative;
}
.Pixso-vector-5517_25897 {
    width: 100%;
    height: 100%;
    background-image: url(@/assets/images/Vector158.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 0%;
    right: 0%;
    top: 0%;
    bottom: 0%;
}
.Pixso-vector-5517_25898 {
    width: 60.83%;
    height: 32.68%;
    background-image: url(@/assets/images/Vector157.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 19.59%;
    right: 19.58%;
    top: 33.66%;
    bottom: 33.66%;
}
.Pixso-symbol-5517_25894 {
    width: 24px;
    height: 24px;
    overflow: hidden;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5517_25895 {
    width: 100%;
    height: 99.63%;
    background-image: url(@/assets/images/Vector156.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 0%;
    right: 0%;
    top: 0%;
    bottom: 0.37%;
}
.Pixso-symbol-5517_25892 {
    width: 24px;
    height: 24px;
    overflow: hidden;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5517_25893 {
    width: 91.66%;
    height: 82.86%;
    background-image: url(@/assets/images/Vector155.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 4.17%;
    right: 4.17%;
    top: 7.93%;
    bottom: 9.21%;
}
.Pixso-symbol-5517_25888 {
    width: 24px;
    height: 24px;
    overflow: hidden;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5517_25889 {
    width: 99.94%;
    height: 99.98%;
    background-image: url(@/assets/images/Vector153.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 0%;
    right: 0.06%;
    top: 0%;
    bottom: 0.02%;
}
.Pixso-vector-5517_25890 {
    width: 51.36%;
    height: 51.36%;
    background-image: url(@/assets/images/Vector154.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 24.32%;
    right: 24.32%;
    top: 24.32%;
    bottom: 24.32%;
}
.Pixso-vector-5517_25891 {
    width: 12%;
    height: 12%;
    background-image: url(@/assets/images/Vector152.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 70.7%;
    right: 17.3%;
    top: 17.3%;
    bottom: 70.7%;
}
.Pixso-symbol-5517_25886 {
    width: 24px;
    height: 24px;
    overflow: hidden;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5517_25887 {
    width: 100%;
    height: 100%;
    background-image: url(@/assets/images/Vector151.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 0%;
    right: 0%;
    top: 0%;
    bottom: 0%;
}
.Pixso-symbol-5517_25880 {
    width: 24px;
    height: 24px;
    overflow: hidden;
    position: relative;
    background-color: transparent;
}
.Pixso-group-5517_25881 {
    width: 98%;
    height: 100%;
    position: absolute;
    left: 0%;
    right: 2%;
    top: 0%;
    bottom: 0%;
}
.Pixso-vector-5517_25882 {
    width: 48.98%;
    height: 47%;
    background-image: url(@/assets/images/Vector293.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 51.02%;
    right: 0%;
    top: 40.91%;
    bottom: 12.09%;
}
.Pixso-vector-5517_25883 {
    width: 79.32%;
    height: 40.48%;
    background-image: url(@/assets/images/Vector292.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 5.47%;
    right: 15.21%;
    top: 59.52%;
    bottom: 0%;
}
.Pixso-vector-5517_25884 {
    width: 22.45%;
    height: 44.82%;
    background-image: url(@/assets/images/Vector291.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 0%;
    right: 77.55%;
    top: 27.59%;
    bottom: 27.59%;
}
.Pixso-vector-5517_25885 {
    width: 79.69%;
    height: 40.5%;
    background-image: url(@/assets/images/Vector290.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 5.47%;
    right: 14.84%;
    top: 0%;
    bottom: 59.5%;
}
.Pixso-symbol-5517_25878 {
    width: 24px;
    height: 24px;
    overflow: hidden;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5517_25879 {
    width: 100%;
    height: 70.34%;
    background-image: url(@/assets/images/Vector281.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 0%;
    right: 0%;
    top: 14.82%;
    bottom: 14.84%;
}
.Pixso-symbol-5517_25876 {
    width: 24px;
    height: 24px;
    overflow: hidden;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5517_25877 {
    width: 84.24%;
    height: 100%;
    background-image: url(@/assets/images/Vector289.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 8.33%;
    right: 7.43%;
    top: 0%;
    bottom: 0%;
}
.Pixso-symbol-5517_25874 {
    width: 24px;
    height: 24px;
    position: relative;
}
.Pixso-vector-5517_25875 {
    width: 100%;
    height: 98.44%;
    background-image: url(@/assets/images/Vector280.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 0%;
    right: 0%;
    top: 0.73%;
    bottom: 0.83%;
}
.Pixso-symbol-5517_25872 {
    width: 24px;
    height: 24px;
    overflow: hidden;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5517_25873 {
    width: 100%;
    height: 100%;
    background-image: url(@/assets/images/Vector275.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 0%;
    right: 0%;
    top: 0%;
    bottom: 0%;
}
.Pixso-symbol-5517_25868 {
    width: 24px;
    height: 24px;
    overflow: hidden;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5517_25869 {
    width: 9.92%;
    height: 47.98%;
    background-image: url(@/assets/images/Vector268.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 90.08%;
    right: 0%;
    top: 25.29%;
    bottom: 26.73%;
}
.Pixso-vector-5517_25870 {
    width: 28.2%;
    height: 53.56%;
    background-image: url(@/assets/images/Vector266.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 59.14%;
    right: 12.66%;
    top: 22.5%;
    bottom: 23.94%;
}
.Pixso-vector-5517_25871 {
    width: 56.41%;
    height: 56.9%;
    background-image: url(@/assets/images/Vector267.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 0%;
    right: 43.59%;
    top: 20.83%;
    bottom: 22.27%;
}
.Pixso-symbol-5517_25866 {
    width: 24px;
    height: 24px;
    overflow: hidden;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5517_25867 {
    width: 100%;
    height: 98.33%;
    background-image: url(@/assets/images/Vector260.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 0%;
    right: 0%;
    top: 0%;
    bottom: 1.67%;
}
.Pixso-symbol-5517_25864 {
    width: 24px;
    height: 24px;
    overflow: hidden;
    position: relative;
}
.Pixso-vector-5517_25865 {
    width: 86.03%;
    height: 100%;
    background-image: url(@/assets/images/Vector252.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 6.77%;
    right: 7.2%;
    top: 0%;
    bottom: 0%;
}
.Pixso-symbol-5517_25862 {
    width: 24.000053px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5517_25863 {
    width: 99.52%;
    height: 100%;
    background-image: url(@/assets/images/Vector259.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 0%;
    right: 0.48%;
    top: 0%;
    bottom: 0%;
}
.Pixso-symbol-5570_32526 {
    width: 24px;
    height: 24px;
    overflow: hidden;
    position: relative;
}
.Pixso-vector-5570_32527 {
    width: 42.9%;
    height: 53.96%;
    background-image: url(@/assets/images/vector7.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 8.33%;
    right: 48.77%;
    top: 22.51%;
    bottom: 23.53%;
}
.Pixso-vector-5570_32528 {
    width: 37.15%;
    height: 41.2%;
    background-image: url(@/assets/images/vector6.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 54.52%;
    right: 8.33%;
    top: 36.29%;
    bottom: 22.51%;
}
.Pixso-vector-5570_32529 {
    width: 20.75%;
    height: 5.3%;
    background-image: url(@/assets/images/vector5.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 62.65%;
    right: 16.6%;
    top: 26.12%;
    bottom: 68.58%;
}
.Pixso-symbol-5517_25860 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5517_25861 {
    width: 68%;
    height: 100%;
    background-image: url(@/assets/images/Vector269.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 16%;
    right: 16%;
    top: 0%;
    bottom: 0%;
}
.Pixso-symbol-5517_25858 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5517_25859 {
    width: 100%;
    height: 100%;
    background-image: url(@/assets/images/Vector265.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 0%;
    right: 0%;
    top: 0%;
    bottom: 0%;
}
.Pixso-symbol-5517_25856 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5517_25857 {
    width: 80.04%;
    height: 70.01%;
    background-image: url(@/assets/images/Vector264.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 9.98%;
    right: 9.98%;
    top: 13.33%;
    bottom: 16.66%;
}
.Pixso-symbol-5517_25854 {
    width: 24px;
    height: 24px;
    overflow: hidden;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5517_25855 {
    width: 100%;
    height: 76.22%;
    background-image: url(@/assets/images/Vector262.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 0%;
    right: 0%;
    top: 11%;
    bottom: 12.78%;
}
.Pixso-symbol-5517_25852 {
    width: 24px;
    height: 24px;
    overflow: hidden;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5517_25853 {
    width: 85.42%;
    height: 100%;
    background-image: url(@/assets/images/Vector258.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 8.33%;
    right: 6.25%;
    top: 0%;
    bottom: 0%;
}
.Pixso-symbol-5517_25850 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5517_25851 {
    width: 56.67%;
    height: 100%;
    background-image: url(@/assets/images/Vector278.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 20.83%;
    right: 22.5%;
    top: 0%;
    bottom: 0%;
}
.Pixso-symbol-5517_25848 {
    width: 24px;
    height: 24px;
    overflow: hidden;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5517_25849 {
    width: 100%;
    height: 100%;
    background-image: url(@/assets/images/Vector279.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 0%;
    right: 0%;
    top: 0%;
    bottom: 0%;
}
.Pixso-symbol-5517_25842 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-group-5517_25843 {
    width: 98.37%;
    height: 81%;
    position: absolute;
    left: 0%;
    right: 1.63%;
    top: 10.42%;
    bottom: 8.58%;
}
.Pixso-vector-5517_25844 {
    width: 75.61%;
    height: 100%;
    background-image: url(@/assets/images/Vector272.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 24.39%;
    right: 0%;
    top: 0%;
    bottom: 0%;
}
.Pixso-vector-5517_25845 {
    width: 16.51%;
    height: 12.97%;
    background-image: url(@/assets/images/Vector270.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 6.84%;
    right: 76.65%;
    top: 61.57%;
    bottom: 25.46%;
}
.Pixso-vector-5517_25846 {
    width: 17.43%;
    height: 8.29%;
    background-image: url(@/assets/images/Vector271.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 0%;
    right: 82.57%;
    top: 38.53%;
    bottom: 53.18%;
}
.Pixso-vector-5517_25847 {
    width: 16.17%;
    height: 15.26%;
    background-image: url(@/assets/images/Vector273.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 3.37%;
    right: 80.46%;
    top: 9.91%;
    bottom: 74.83%;
}
.Pixso-symbol-5517_25840 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5517_25841 {
    width: 100%;
    height: 100%;
    background-image: url(@/assets/images/Vector261.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 0%;
    right: 0%;
    top: 0%;
    bottom: 0%;
}
.Pixso-symbol-5517_25838 {
    width: 24px;
    height: 24px;
    overflow: hidden;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5517_25839 {
    width: 100%;
    height: 100%;
    background-image: url(@/assets/images/Vector251.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 0%;
    right: 0%;
    top: 0%;
    bottom: 0%;
}
.Pixso-symbol-5517_25836 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5517_25837 {
    width: 99.69%;
    height: 99.69%;
    background-image: url(@/assets/images/Vector250.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 0%;
    right: 0.31%;
    top: 0%;
    bottom: 0.31%;
}
.Pixso-symbol-5517_25832 {
    width: 24px;
    height: 24px;
    overflow: hidden;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5517_25833 {
    width: 85.71%;
    height: 100%;
    background-image: url(@/assets/images/Vector249.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 7.15%;
    right: 7.14%;
    top: 0%;
    bottom: 0%;
}
.Pixso-vector-5517_25834 {
    width: 7.14%;
    height: 21.43%;
    background-image: url(@/assets/images/Vector248.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 67.86%;
    right: 25%;
    top: 19.64%;
    bottom: 58.93%;
}
.Pixso-vector-5517_25835 {
    width: 7.14%;
    height: 21.43%;
    background-image: url(@/assets/images/Vector247.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 48.22%;
    right: 44.64%;
    top: 19.64%;
    bottom: 58.93%;
}
.Pixso-symbol-5517_25830 {
    width: 24px;
    height: 24.00066px;
    position: relative;
}
.Pixso-vector-5517_25831 {
    width: 100%;
    height: 100%;
    background-image: url(@/assets/images/Vector246.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 0%;
    right: 0%;
    top: 0%;
    bottom: 0%;
}
.Pixso-symbol-5517_25998 {
    width: 24px;
    height: 24px;
    overflow: hidden;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5517_25999 {
    width: 100%;
    height: 99.63%;
    background-image: url(@/assets/images/Vector245.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 0%;
    right: 0%;
    top: 0%;
    bottom: 0.37%;
}
.Pixso-symbol-5517_26000 {
    width: 24px;
    height: 24px;
    overflow: hidden;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5517_26001 {
    width: 91.66%;
    height: 82.86%;
    background-image: url(@/assets/images/Vector244.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 4.17%;
    right: 4.17%;
    top: 7.93%;
    bottom: 9.21%;
}
.Pixso-symbol-5517_26002 {
    width: 24px;
    height: 24px;
    overflow: hidden;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5517_26003 {
    width: 99.94%;
    height: 99.98%;
    background-image: url(@/assets/images/Vector242.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 0%;
    right: 0.06%;
    top: 0%;
    bottom: 0.02%;
}
.Pixso-vector-5517_26004 {
    width: 51.36%;
    height: 51.36%;
    background-image: url(@/assets/images/Vector243.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 24.32%;
    right: 24.32%;
    top: 24.32%;
    bottom: 24.32%;
}
.Pixso-vector-5517_26005 {
    width: 12%;
    height: 12%;
    background-image: url(@/assets/images/Vector241.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 70.7%;
    right: 17.3%;
    top: 17.3%;
    bottom: 70.7%;
}
.Pixso-symbol-5517_26006 {
    width: 24px;
    height: 24px;
    overflow: hidden;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5517_26007 {
    width: 100%;
    height: 100%;
    background-image: url(@/assets/images/Vector240.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 0%;
    right: 0%;
    top: 0%;
    bottom: 0%;
}
.Pixso-symbol-5517_26008 {
    width: 24px;
    height: 24px;
    overflow: hidden;
    position: relative;
    background-color: transparent;
}
.Pixso-group-5517_26009 {
    width: 98%;
    height: 100%;
    position: absolute;
    left: 0%;
    right: 2%;
    top: 0%;
    bottom: 0%;
}
.Pixso-vector-5517_26010 {
    width: 48.98%;
    height: 47%;
    background-image: url(@/assets/images/Vector239.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 51.02%;
    right: 0%;
    top: 40.91%;
    bottom: 12.09%;
}
.Pixso-vector-5517_26011 {
    width: 79.32%;
    height: 40.48%;
    background-image: url(@/assets/images/Vector238.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 5.47%;
    right: 15.21%;
    top: 59.52%;
    bottom: 0%;
}
.Pixso-vector-5517_26012 {
    width: 22.45%;
    height: 44.82%;
    background-image: url(@/assets/images/Vector237.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 0%;
    right: 77.55%;
    top: 27.59%;
    bottom: 27.59%;
}
.Pixso-vector-5517_26013 {
    width: 79.69%;
    height: 40.5%;
    background-image: url(@/assets/images/Vector236.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 5.47%;
    right: 14.84%;
    top: 0%;
    bottom: 59.5%;
}
.Pixso-symbol-5517_26014 {
    width: 24px;
    height: 24px;
    overflow: hidden;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5517_26015 {
    width: 100%;
    height: 70.34%;
    background-image: url(@/assets/images/Vector235.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 0%;
    right: 0%;
    top: 14.82%;
    bottom: 14.84%;
}
.Pixso-symbol-5517_26016 {
    width: 24px;
    height: 24px;
    overflow: hidden;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5517_26017 {
    width: 84.24%;
    height: 100%;
    background-image: url(@/assets/images/Vector276.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 8.33%;
    right: 7.43%;
    top: 0%;
    bottom: 0%;
}
.Pixso-symbol-5517_26018 {
    width: 24px;
    height: 24px;
    position: relative;
}
.Pixso-vector-5517_26019 {
    width: 100%;
    height: 98.44%;
    background-image: url(@/assets/images/Vector277.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 0%;
    right: 0%;
    top: 0.73%;
    bottom: 0.83%;
}
.Pixso-symbol-5517_26020 {
    width: 24px;
    height: 24px;
    overflow: hidden;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5517_26021 {
    width: 100%;
    height: 100%;
    background-image: url(@/assets/images/Vector257.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 0%;
    right: 0%;
    top: 0%;
    bottom: 0%;
}
.Pixso-symbol-5517_26022 {
    width: 24px;
    height: 24px;
    overflow: hidden;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5517_26023 {
    width: 9.92%;
    height: 47.98%;
    background-image: url(@/assets/images/Vector256.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 90.08%;
    right: 0%;
    top: 25.29%;
    bottom: 26.73%;
}
.Pixso-vector-5517_26024 {
    width: 28.2%;
    height: 53.56%;
    background-image: url(@/assets/images/Vector254.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 59.14%;
    right: 12.66%;
    top: 22.5%;
    bottom: 23.94%;
}
.Pixso-vector-5517_26025 {
    width: 56.41%;
    height: 56.9%;
    background-image: url(@/assets/images/Vector255.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 0%;
    right: 43.59%;
    top: 20.83%;
    bottom: 22.27%;
}
.Pixso-symbol-5517_26026 {
    width: 24px;
    height: 24px;
    overflow: hidden;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5517_26027 {
    width: 100%;
    height: 98.33%;
    background-image: url(@/assets/images/Vector253.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 0%;
    right: 0%;
    top: 0%;
    bottom: 1.67%;
}
.Pixso-symbol-5517_26028 {
    width: 24px;
    height: 24px;
    overflow: hidden;
    position: relative;
}
.Pixso-vector-5517_26029 {
    width: 86.03%;
    height: 100%;
    background-image: url(@/assets/images/Vector274.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 6.77%;
    right: 7.2%;
    top: 0%;
    bottom: 0%;
}
.Pixso-symbol-5517_26030 {
    width: 24.000053px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5517_26031 {
    width: 99.52%;
    height: 100%;
    background-image: url(@/assets/images/Vector263.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 0%;
    right: 0.48%;
    top: 0%;
    bottom: 0%;
}
.Pixso-symbol-5570_32534 {
    width: 24px;
    height: 24px;
    overflow: hidden;
    position: relative;
}
.Pixso-vector-5570_32535 {
    width: 42.9%;
    height: 53.96%;
    background-image: url(@/assets/images/vector4.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 8.33%;
    right: 48.77%;
    top: 22.51%;
    bottom: 23.53%;
}
.Pixso-vector-5570_32536 {
    width: 37.15%;
    height: 41.2%;
    background-image: url(@/assets/images/vector3.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 54.52%;
    right: 8.33%;
    top: 36.29%;
    bottom: 22.51%;
}
.Pixso-vector-5570_32537 {
    width: 20.75%;
    height: 5.3%;
    background-image: url(@/assets/images/vector2.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 62.65%;
    right: 16.6%;
    top: 26.12%;
    bottom: 68.58%;
}
.Pixso-symbol-5517_26032 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5517_26033 {
    width: 68%;
    height: 100%;
    background-image: url(@/assets/images/Vector234.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 16%;
    right: 16%;
    top: 0%;
    bottom: 0%;
}
.Pixso-symbol-5517_26034 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5517_26035 {
    width: 100%;
    height: 100%;
    background-image: url(@/assets/images/Vector233.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 0%;
    right: 0%;
    top: 0%;
    bottom: 0%;
}
.Pixso-symbol-5517_26036 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5517_26037 {
    width: 80.04%;
    height: 70.01%;
    background-image: url(@/assets/images/Vector232.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 9.98%;
    right: 9.98%;
    top: 13.33%;
    bottom: 16.66%;
}
.Pixso-symbol-5517_26038 {
    width: 24px;
    height: 24px;
    overflow: hidden;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5517_26039 {
    width: 100%;
    height: 76.22%;
    background-image: url(@/assets/images/Vector231.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 0%;
    right: 0%;
    top: 11%;
    bottom: 12.78%;
}
.Pixso-symbol-5517_26040 {
    width: 24px;
    height: 24px;
    overflow: hidden;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5517_26041 {
    width: 85.42%;
    height: 100%;
    background-image: url(@/assets/images/Vector230.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 8.33%;
    right: 6.25%;
    top: 0%;
    bottom: 0%;
}
.Pixso-symbol-5517_26042 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5517_26043 {
    width: 56.67%;
    height: 100%;
    background-image: url(@/assets/images/Vector229.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 20.83%;
    right: 22.5%;
    top: 0%;
    bottom: 0%;
}
.Pixso-symbol-5517_26044 {
    width: 24px;
    height: 24px;
    overflow: hidden;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5517_26045 {
    width: 100%;
    height: 100%;
    background-image: url(@/assets/images/Vector228.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 0%;
    right: 0%;
    top: 0%;
    bottom: 0%;
}
.Pixso-symbol-5517_26046 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-group-5517_26047 {
    width: 98.37%;
    height: 81%;
    position: absolute;
    left: 0%;
    right: 1.63%;
    top: 10.42%;
    bottom: 8.58%;
}
.Pixso-vector-5517_26048 {
    width: 75.61%;
    height: 100%;
    background-image: url(@/assets/images/Vector226.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 24.39%;
    right: 0%;
    top: 0%;
    bottom: 0%;
}
.Pixso-vector-5517_26049 {
    width: 16.51%;
    height: 12.97%;
    background-image: url(@/assets/images/Vector224.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 6.84%;
    right: 76.65%;
    top: 61.57%;
    bottom: 25.46%;
}
.Pixso-vector-5517_26050 {
    width: 17.43%;
    height: 8.29%;
    background-image: url(@/assets/images/Vector225.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 0%;
    right: 82.57%;
    top: 38.53%;
    bottom: 53.18%;
}
.Pixso-vector-5517_26051 {
    width: 16.17%;
    height: 15.26%;
    background-image: url(@/assets/images/Vector227.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 3.37%;
    right: 80.46%;
    top: 9.91%;
    bottom: 74.83%;
}
.Pixso-symbol-5517_26052 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5517_26053 {
    width: 100%;
    height: 100%;
    background-image: url(@/assets/images/Vector223.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 0%;
    right: 0%;
    top: 0%;
    bottom: 0%;
}
.Pixso-symbol-5517_26054 {
    width: 24px;
    height: 24px;
    overflow: hidden;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5517_26055 {
    width: 100%;
    height: 100%;
    background-image: url(@/assets/images/Vector222.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 0%;
    right: 0%;
    top: 0%;
    bottom: 0%;
}
.Pixso-symbol-5517_26056 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5517_26057 {
    width: 99.69%;
    height: 99.69%;
    background-image: url(@/assets/images/Vector221.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 0%;
    right: 0.31%;
    top: 0%;
    bottom: 0.31%;
}
.Pixso-symbol-5517_26058 {
    width: 24px;
    height: 24px;
    overflow: hidden;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5517_26059 {
    width: 85.71%;
    height: 100%;
    background-image: url(@/assets/images/Vector220.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 7.15%;
    right: 7.14%;
    top: 0%;
    bottom: 0%;
}
.Pixso-vector-5517_26060 {
    width: 7.14%;
    height: 21.43%;
    background-image: url(@/assets/images/Vector219.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 67.86%;
    right: 25%;
    top: 19.64%;
    bottom: 58.93%;
}
.Pixso-vector-5517_26061 {
    width: 7.14%;
    height: 21.43%;
    background-image: url(@/assets/images/Vector218.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 48.22%;
    right: 44.64%;
    top: 19.64%;
    bottom: 58.93%;
}
.Pixso-symbol-5517_26062 {
    width: 24px;
    height: 24.00066px;
    position: relative;
}
.Pixso-vector-5517_26063 {
    width: 100%;
    height: 100%;
    background-image: url(@/assets/images/Vector217.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 0%;
    right: 0%;
    top: 0%;
    bottom: 0%;
}
</style>
