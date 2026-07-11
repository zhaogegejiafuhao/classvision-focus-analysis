<template>
    <div class="component-5550_11435">
        <div id="5550_11435" class="Pixso-symbol-5550_11435">
            <div
                id="5550_11626"
                class="Pixso-symbol-5550_11626 fill-gray20-36_1844"
                v-if="
                    IsActive === 'False' &&
                    Size === 'sm' &&
                    State === 'Default' &&
                    IsIcon === 'False'
                "
            >
                <slot name="slot_5550_11627">
                    <div id="5550_11627" class="Pixso-vector-5550_11627"></div>
                </slot>
            </div>
            <div
                id="5550_11643"
                class="Pixso-symbol-5550_11643 fill-brand60-1257_33467"
                v-if="
                    IsActive === 'True' &&
                    Size === 'sm' &&
                    State === 'Default' &&
                    IsIcon === 'False'
                "
            >
                <slot name="slot_5550_11644">
                    <div id="5550_11644" class="Pixso-vector-5550_11644"></div>
                </slot>
            </div>
            <div
                id="5550_11484"
                class="Pixso-symbol-5550_11484 fill-gray20-36_1844"
                v-if="
                    IsActive === 'False' &&
                    Size === 'md' &&
                    State === 'Default' &&
                    IsIcon === 'False'
                "
            >
                <slot name="slot_5550_11485">
                    <div id="5550_11485" class="Pixso-vector-5550_11485"></div>
                </slot>
            </div>
            <div
                id="5550_11452"
                class="Pixso-symbol-5550_11452 fill-brand60-1257_33467"
                v-if="
                    IsActive === 'True' &&
                    Size === 'md' &&
                    State === 'Default' &&
                    IsIcon === 'False'
                "
            >
                <slot name="slot_5550_11453">
                    <div id="5550_11453" class="Pixso-vector-5550_11453"></div>
                </slot>
            </div>
            <div
                id="5550_11554"
                class="Pixso-symbol-5550_11554 fill-gray20-36_1844"
                v-if="
                    IsActive === 'False' &&
                    Size === 'lg' &&
                    State === 'Default' &&
                    IsIcon === 'False'
                "
            >
                <slot name="slot_5550_11555">
                    <div id="5550_11555" class="Pixso-vector-5550_11555"></div>
                </slot>
            </div>
            <div
                id="5550_11570"
                class="Pixso-symbol-5550_11570 fill-brand60-1257_33467"
                v-if="
                    IsActive === 'True' &&
                    Size === 'lg' &&
                    State === 'Default' &&
                    IsIcon === 'False'
                "
            >
                <slot name="slot_5550_11571">
                    <div id="5550_11571" class="Pixso-vector-5550_11571"></div>
                </slot>
            </div>
            <div
                id="5550_11649"
                class="Pixso-symbol-5550_11649 fill-gray30-35_1481"
                v-if="
                    IsActive === 'False' &&
                    Size === 'sm' &&
                    State === 'Hover' &&
                    IsIcon === 'False'
                "
            >
                <slot name="slot_5550_11650">
                    <div id="5550_11650" class="Pixso-vector-5550_11650"></div>
                </slot>
            </div>
            <div
                id="5550_11651"
                class="Pixso-symbol-5550_11651 fill-brand60-1257_33467"
                v-if="
                    IsActive === 'True' &&
                    Size === 'sm' &&
                    State === 'Hover' &&
                    IsIcon === 'False'
                "
            >
                <slot name="slot_5550_11652">
                    <div id="5550_11652" class="Pixso-vector-5550_11652"></div>
                </slot>
            </div>
            <div
                id="5550_11518"
                class="Pixso-symbol-5550_11518 fill-gray30-35_1481"
                v-if="
                    IsActive === 'False' &&
                    Size === 'md' &&
                    State === 'Hover' &&
                    IsIcon === 'False'
                "
            >
                <slot name="slot_5550_11519">
                    <div id="5550_11519" class="Pixso-vector-5550_11519"></div>
                </slot>
            </div>
            <div
                id="5550_11516"
                class="Pixso-symbol-5550_11516 fill-brand60-1257_33467"
                v-if="
                    IsActive === 'True' &&
                    Size === 'md' &&
                    State === 'Hover' &&
                    IsIcon === 'False'
                "
            >
                <slot name="slot_5550_11517">
                    <div id="5550_11517" class="Pixso-vector-5550_11517"></div>
                </slot>
            </div>
            <div
                id="5550_11580"
                class="Pixso-symbol-5550_11580 fill-gray30-35_1481"
                v-if="
                    IsActive === 'False' &&
                    Size === 'lg' &&
                    State === 'Hover' &&
                    IsIcon === 'False'
                "
            >
                <slot name="slot_5550_11581">
                    <div id="5550_11581" class="Pixso-vector-5550_11581"></div>
                </slot>
            </div>
            <div
                id="5550_11582"
                class="Pixso-symbol-5550_11582 fill-brand60-1257_33467"
                v-if="
                    IsActive === 'True' &&
                    Size === 'lg' &&
                    State === 'Hover' &&
                    IsIcon === 'False'
                "
            >
                <slot name="slot_5550_11583">
                    <div id="5550_11583" class="Pixso-vector-5550_11583"></div>
                </slot>
            </div>
            <div
                id="5550_11657"
                class="Pixso-symbol-5550_11657 fill-gray20-36_1844 effect-focusring-brand-5459_24463"
                v-if="
                    IsActive === 'False' &&
                    Size === 'sm' &&
                    State === 'Focus' &&
                    IsIcon === 'False'
                "
            >
                <slot name="slot_5550_11658">
                    <div id="5550_11658" class="Pixso-vector-5550_11658"></div>
                </slot>
            </div>
            <div
                id="5550_11659"
                class="Pixso-symbol-5550_11659 fill-brand60-1257_33467 effect-focusring-brand-5459_24463"
                v-if="
                    IsActive === 'True' &&
                    Size === 'sm' &&
                    State === 'Focus' &&
                    IsIcon === 'False'
                "
            >
                <slot name="slot_5550_11660">
                    <div id="5550_11660" class="Pixso-vector-5550_11660"></div>
                </slot>
            </div>
            <div
                id="5550_11526"
                class="Pixso-symbol-5550_11526 fill-gray20-36_1844 effect-focusring-brand-5459_24463"
                v-if="
                    IsActive === 'False' &&
                    Size === 'md' &&
                    State === 'Focus' &&
                    IsIcon === 'False'
                "
            >
                <slot name="slot_5550_11527">
                    <div id="5550_11527" class="Pixso-vector-5550_11527"></div>
                </slot>
            </div>
            <div
                id="5550_11524"
                class="Pixso-symbol-5550_11524 fill-brand60-1257_33467 effect-focusring-brand-5459_24463"
                v-if="
                    IsActive === 'True' &&
                    Size === 'md' &&
                    State === 'Focus' &&
                    IsIcon === 'False'
                "
            >
                <slot name="slot_5550_11525">
                    <div id="5550_11525" class="Pixso-vector-5550_11525"></div>
                </slot>
            </div>
            <div
                id="5550_11588"
                class="Pixso-symbol-5550_11588 fill-gray20-36_1844 effect-focusring-brand-5459_24463"
                v-if="
                    IsActive === 'False' &&
                    Size === 'lg' &&
                    State === 'Focus' &&
                    IsIcon === 'False'
                "
            >
                <slot name="slot_5550_11589">
                    <div id="5550_11589" class="Pixso-vector-5550_11589"></div>
                </slot>
            </div>
            <div
                id="5550_11590"
                class="Pixso-symbol-5550_11590 fill-brand60-1257_33467 effect-focusring-brand-5459_24463"
                v-if="
                    IsActive === 'True' &&
                    Size === 'lg' &&
                    State === 'Focus' &&
                    IsIcon === 'False'
                "
            >
                <slot name="slot_5550_11591">
                    <div id="5550_11591" class="Pixso-vector-5550_11591"></div>
                </slot>
            </div>
            <div
                id="5550_11665"
                class="Pixso-symbol-5550_11665 fill-gray20-36_1844"
                v-if="
                    IsActive === 'False' &&
                    Size === 'sm' &&
                    State === 'Disabled' &&
                    IsIcon === 'False'
                "
            >
                <slot name="slot_5550_11666">
                    <div id="5550_11666" class="Pixso-vector-5550_11666"></div>
                </slot>
            </div>
            <div
                id="5550_11667"
                class="Pixso-symbol-5550_11667 fill-brand10-1257_33461"
                v-if="
                    IsActive === 'True' &&
                    Size === 'sm' &&
                    State === 'Disabled' &&
                    IsIcon === 'False'
                "
            >
                <slot name="slot_5550_11668">
                    <div id="5550_11668" class="Pixso-vector-5550_11668"></div>
                </slot>
            </div>
            <div
                id="5550_11534"
                class="Pixso-symbol-5550_11534 fill-gray20-36_1844"
                v-if="
                    IsActive === 'False' &&
                    Size === 'md' &&
                    State === 'Disabled' &&
                    IsIcon === 'False'
                "
            >
                <slot name="slot_5550_11535">
                    <div id="5550_11535" class="Pixso-vector-5550_11535"></div>
                </slot>
            </div>
            <div
                id="5550_11532"
                class="Pixso-symbol-5550_11532 fill-brand10-1257_33461"
                v-if="
                    IsActive === 'True' &&
                    Size === 'md' &&
                    State === 'Disabled' &&
                    IsIcon === 'False'
                "
            >
                <slot name="slot_5550_11533">
                    <div id="5550_11533" class="Pixso-vector-5550_11533"></div>
                </slot>
            </div>
            <div
                id="5550_11596"
                class="Pixso-symbol-5550_11596 fill-gray20-36_1844"
                v-if="
                    IsActive === 'False' &&
                    Size === 'lg' &&
                    State === 'Disabled' &&
                    IsIcon === 'False'
                "
            >
                <slot name="slot_5550_11597">
                    <div id="5550_11597" class="Pixso-vector-5550_11597"></div>
                </slot>
            </div>
            <div
                id="5550_11598"
                class="Pixso-symbol-5550_11598 fill-brand10-1257_33461"
                v-if="
                    IsActive === 'True' &&
                    Size === 'lg' &&
                    State === 'Disabled' &&
                    IsIcon === 'False'
                "
            >
                <slot name="slot_5550_11599">
                    <div id="5550_11599" class="Pixso-vector-5550_11599"></div>
                </slot>
            </div>
            <div
                id="5550_12434"
                class="Pixso-symbol-5550_12434 fill-gray20-36_1844"
                v-if="
                    IsActive === 'False' &&
                    Size === 'sm' &&
                    State === 'Default' &&
                    IsIcon === 'True'
                "
            >
                <div
                    id="5550_12450"
                    class="Pixso-frame-5550_12450 fill-gray0-white-67_3285 effect-shadowmd-5457_24364"
                >
                    <slot name="slot_5550_12452">
                        <X
                            id="5550_12452"
                            class="Pixso-instance-5550_12452"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div id="5550_12451" class="Pixso-frame-5550_12451">
                    <slot name="slot_5550_12454">
                        <Check
                            id="5550_12454"
                            class="Pixso-instance-5550_12454"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
            </div>
            <div
                id="5550_12442"
                class="Pixso-symbol-5550_12442 fill-brand60-1257_33467"
                v-if="
                    IsActive === 'True' &&
                    Size === 'sm' &&
                    State === 'Default' &&
                    IsIcon === 'True'
                "
            >
                <div id="5550_12458" class="Pixso-frame-5550_12458">
                    <slot name="slot_5550_12457">
                        <X
                            id="5550_12457"
                            class="Pixso-instance-5550_12457"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div
                    id="5550_12456"
                    class="Pixso-frame-5550_12456 fill-gray0-white-67_3285 effect-shadowmd-5457_24364"
                >
                    <slot name="slot_5550_12459">
                        <Check
                            id="5550_12459"
                            class="Pixso-instance-5550_12459"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
            </div>
            <div
                id="5550_11719"
                class="Pixso-symbol-5550_11719 fill-gray20-36_1844"
                v-if="
                    IsActive === 'False' &&
                    Size === 'md' &&
                    State === 'Default' &&
                    IsIcon === 'True'
                "
            >
                <div
                    id="5550_11773"
                    class="Pixso-frame-5550_11773 fill-gray0-white-67_3285 effect-shadowmd-5457_24364"
                >
                    <slot name="slot_5550_11770">
                        <X
                            id="5550_11770"
                            class="Pixso-instance-5550_11770"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div
                    id="5550_12260"
                    class="Pixso-frame-5550_12260 effect-shadowmd-5457_24364"
                >
                    <slot name="slot_5550_12261">
                        <Check
                            id="5550_12261"
                            class="Pixso-instance-5550_12261"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
            </div>
            <div
                id="5550_11717"
                class="Pixso-symbol-5550_11717 fill-brand60-1257_33467"
                v-if="
                    IsActive === 'True' &&
                    Size === 'md' &&
                    State === 'Default' &&
                    IsIcon === 'True'
                "
            >
                <div id="5550_12282" class="Pixso-frame-5550_12282">
                    <slot name="slot_5550_12283">
                        <X
                            id="5550_12283"
                            class="Pixso-instance-5550_12283"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div
                    id="5550_12284"
                    class="Pixso-frame-5550_12284 fill-gray0-white-67_3285 effect-shadowmd-5457_24364"
                >
                    <slot name="slot_5550_12285">
                        <Check
                            id="5550_12285"
                            class="Pixso-instance-5550_12285"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
            </div>
            <div
                id="5550_12514"
                class="Pixso-symbol-5550_12514 fill-gray20-36_1844"
                v-if="
                    IsActive === 'False' &&
                    Size === 'lg' &&
                    State === 'Default' &&
                    IsIcon === 'True'
                "
            >
                <div
                    id="5550_12530"
                    class="Pixso-frame-5550_12530 fill-gray0-white-67_3285 effect-shadowmd-5457_24364"
                >
                    <slot name="slot_5550_12532">
                        <X
                            id="5550_12532"
                            class="Pixso-instance-5550_12532"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div id="5550_12534" class="Pixso-frame-5550_12534">
                    <slot name="slot_5550_12535">
                        <Check
                            id="5550_12535"
                            class="Pixso-instance-5550_12535"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
            </div>
            <div
                id="5550_12522"
                class="Pixso-symbol-5550_12522 fill-brand60-1257_33467"
                v-if="
                    IsActive === 'True' &&
                    Size === 'lg' &&
                    State === 'Default' &&
                    IsIcon === 'True'
                "
            >
                <div id="5550_12554" class="Pixso-frame-5550_12554">
                    <slot name="slot_5550_12555">
                        <X
                            id="5550_12555"
                            class="Pixso-instance-5550_12555"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div
                    id="5550_12552"
                    class="Pixso-frame-5550_12552 fill-gray0-white-67_3285 effect-shadowmd-5457_24364"
                >
                    <slot name="slot_5550_12553">
                        <Check
                            id="5550_12553"
                            class="Pixso-instance-5550_12553"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
            </div>
            <div
                id="5550_12440"
                class="Pixso-symbol-5550_12440 fill-gray30-35_1481"
                v-if="
                    IsActive === 'False' &&
                    Size === 'sm' &&
                    State === 'Hover' &&
                    IsIcon === 'True'
                "
            >
                <div
                    id="5550_12462"
                    class="Pixso-frame-5550_12462 fill-gray0-white-67_3285 effect-shadowmd-5457_24364"
                >
                    <slot name="slot_5550_12463">
                        <X
                            id="5550_12463"
                            class="Pixso-instance-5550_12463"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div id="5550_12464" class="Pixso-frame-5550_12464">
                    <slot name="slot_5550_12465">
                        <Check
                            id="5550_12465"
                            class="Pixso-instance-5550_12465"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
            </div>
            <div
                id="5550_12448"
                class="Pixso-symbol-5550_12448 fill-brand60-1257_33467"
                v-if="
                    IsActive === 'True' &&
                    Size === 'sm' &&
                    State === 'Hover' &&
                    IsIcon === 'True'
                "
            >
                <div id="5550_12468" class="Pixso-frame-5550_12468">
                    <slot name="slot_5550_12469">
                        <X
                            id="5550_12469"
                            class="Pixso-instance-5550_12469"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div
                    id="5550_12470"
                    class="Pixso-frame-5550_12470 fill-gray0-white-67_3285 effect-shadowmd-5457_24364"
                >
                    <slot name="slot_5550_12471">
                        <Check
                            id="5550_12471"
                            class="Pixso-instance-5550_12471"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
            </div>
            <div
                id="5550_11759"
                class="Pixso-symbol-5550_11759 fill-gray30-35_1481"
                v-if="
                    IsActive === 'False' &&
                    Size === 'md' &&
                    State === 'Hover' &&
                    IsIcon === 'True'
                "
            >
                <div
                    id="5550_12264"
                    class="Pixso-frame-5550_12264 fill-gray0-white-67_3285 effect-shadowmd-5457_24364"
                >
                    <slot name="slot_5550_12265">
                        <X
                            id="5550_12265"
                            class="Pixso-instance-5550_12265"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div
                    id="5550_12267"
                    class="Pixso-frame-5550_12267 effect-shadowmd-5457_24364"
                >
                    <slot name="slot_5550_12268">
                        <Check
                            id="5550_12268"
                            class="Pixso-instance-5550_12268"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
            </div>
            <div
                id="5550_11757"
                class="Pixso-symbol-5550_11757 fill-brand60-1257_33467"
                v-if="
                    IsActive === 'True' &&
                    Size === 'md' &&
                    State === 'Hover' &&
                    IsIcon === 'True'
                "
            >
                <div id="5550_12288" class="Pixso-frame-5550_12288">
                    <slot name="slot_5550_12289">
                        <X
                            id="5550_12289"
                            class="Pixso-instance-5550_12289"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div
                    id="5550_12290"
                    class="Pixso-frame-5550_12290 fill-gray0-white-67_3285 effect-shadowmd-5457_24364"
                >
                    <slot name="slot_5550_12291">
                        <Check
                            id="5550_12291"
                            class="Pixso-instance-5550_12291"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
            </div>
            <div
                id="5550_12516"
                class="Pixso-symbol-5550_12516 fill-gray30-35_1481"
                v-if="
                    IsActive === 'False' &&
                    Size === 'lg' &&
                    State === 'Hover' &&
                    IsIcon === 'True'
                "
            >
                <div
                    id="5550_12540"
                    class="Pixso-frame-5550_12540 fill-gray0-white-67_3285 effect-shadowmd-5457_24364"
                >
                    <slot name="slot_5550_12541">
                        <X
                            id="5550_12541"
                            class="Pixso-instance-5550_12541"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div id="5550_12542" class="Pixso-frame-5550_12542">
                    <slot name="slot_5550_12543">
                        <Check
                            id="5550_12543"
                            class="Pixso-instance-5550_12543"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
            </div>
            <div
                id="5550_12524"
                class="Pixso-symbol-5550_12524 fill-brand60-1257_33467"
                v-if="
                    IsActive === 'True' &&
                    Size === 'lg' &&
                    State === 'Hover' &&
                    IsIcon === 'True'
                "
            >
                <div id="5550_12566" class="Pixso-frame-5550_12566">
                    <slot name="slot_5550_12567">
                        <X
                            id="5550_12567"
                            class="Pixso-instance-5550_12567"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div
                    id="5550_12568"
                    class="Pixso-frame-5550_12568 fill-gray0-white-67_3285 effect-shadowmd-5457_24364"
                >
                    <slot name="slot_5550_12569">
                        <Check
                            id="5550_12569"
                            class="Pixso-instance-5550_12569"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
            </div>
            <div
                id="5550_12436"
                class="Pixso-symbol-5550_12436 fill-gray20-36_1844 effect-focusring-brand-5459_24463"
                v-if="
                    IsActive === 'False' &&
                    Size === 'sm' &&
                    State === 'Focus' &&
                    IsIcon === 'True'
                "
            >
                <div
                    id="5550_12474"
                    class="Pixso-frame-5550_12474 fill-gray0-white-67_3285 effect-shadowmd-5457_24364"
                >
                    <slot name="slot_5550_12475">
                        <X
                            id="5550_12475"
                            class="Pixso-instance-5550_12475"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div id="5550_12476" class="Pixso-frame-5550_12476">
                    <slot name="slot_5550_12477">
                        <Check
                            id="5550_12477"
                            class="Pixso-instance-5550_12477"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
            </div>
            <div
                id="5550_12444"
                class="Pixso-symbol-5550_12444 fill-brand60-1257_33467 effect-focusring-brand-5459_24463"
                v-if="
                    IsActive === 'True' &&
                    Size === 'sm' &&
                    State === 'Focus' &&
                    IsIcon === 'True'
                "
            >
                <div id="5550_12480" class="Pixso-frame-5550_12480">
                    <slot name="slot_5550_12481">
                        <X
                            id="5550_12481"
                            class="Pixso-instance-5550_12481"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div
                    id="5550_12482"
                    class="Pixso-frame-5550_12482 fill-gray0-white-67_3285 effect-shadowmd-5457_24364"
                >
                    <slot name="slot_5550_12483">
                        <Check
                            id="5550_12483"
                            class="Pixso-instance-5550_12483"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
            </div>
            <div
                id="5550_11753"
                class="Pixso-symbol-5550_11753 fill-gray20-36_1844 effect-focusring-brand-5459_24463"
                v-if="
                    IsActive === 'False' &&
                    Size === 'md' &&
                    State === 'Focus' &&
                    IsIcon === 'True'
                "
            >
                <div
                    id="5550_12270"
                    class="Pixso-frame-5550_12270 fill-gray0-white-67_3285 effect-shadowmd-5457_24364"
                >
                    <slot name="slot_5550_12271">
                        <X
                            id="5550_12271"
                            class="Pixso-instance-5550_12271"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div
                    id="5550_12273"
                    class="Pixso-frame-5550_12273 effect-shadowmd-5457_24364"
                >
                    <slot name="slot_5550_12274">
                        <Check
                            id="5550_12274"
                            class="Pixso-instance-5550_12274"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
            </div>
            <div
                id="5550_11749"
                class="Pixso-symbol-5550_11749 fill-brand60-1257_33467 effect-focusring-brand-5459_24463"
                v-if="
                    IsActive === 'True' &&
                    Size === 'md' &&
                    State === 'Focus' &&
                    IsIcon === 'True'
                "
            >
                <div id="5550_12294" class="Pixso-frame-5550_12294">
                    <slot name="slot_5550_12295">
                        <X
                            id="5550_12295"
                            class="Pixso-instance-5550_12295"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div
                    id="5550_12296"
                    class="Pixso-frame-5550_12296 fill-gray0-white-67_3285 effect-shadowmd-5457_24364"
                >
                    <slot name="slot_5550_12297">
                        <Check
                            id="5550_12297"
                            class="Pixso-instance-5550_12297"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
            </div>
            <div
                id="5550_12518"
                class="Pixso-symbol-5550_12518 fill-gray20-36_1844 effect-focusring-brand-5459_24463"
                v-if="
                    IsActive === 'False' &&
                    Size === 'lg' &&
                    State === 'Focus' &&
                    IsIcon === 'True'
                "
            >
                <div
                    id="5550_12546"
                    class="Pixso-frame-5550_12546 fill-gray0-white-67_3285 effect-shadowmd-5457_24364"
                >
                    <slot name="slot_5550_12547">
                        <X
                            id="5550_12547"
                            class="Pixso-instance-5550_12547"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div id="5550_12548" class="Pixso-frame-5550_12548">
                    <slot name="slot_5550_12549">
                        <Check
                            id="5550_12549"
                            class="Pixso-instance-5550_12549"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
            </div>
            <div
                id="5550_12526"
                class="Pixso-symbol-5550_12526 fill-brand60-1257_33467 effect-focusring-brand-5459_24463"
                v-if="
                    IsActive === 'True' &&
                    Size === 'lg' &&
                    State === 'Focus' &&
                    IsIcon === 'True'
                "
            >
                <div id="5550_12572" class="Pixso-frame-5550_12572">
                    <slot name="slot_5550_12573">
                        <X
                            id="5550_12573"
                            class="Pixso-instance-5550_12573"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div
                    id="5550_12574"
                    class="Pixso-frame-5550_12574 fill-gray0-white-67_3285 effect-shadowmd-5457_24364"
                >
                    <slot name="slot_5550_12575">
                        <Check
                            id="5550_12575"
                            class="Pixso-instance-5550_12575"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
            </div>
            <div
                id="5550_12438"
                class="Pixso-symbol-5550_12438 fill-gray20-36_1844"
                v-if="
                    IsActive === 'False' &&
                    Size === 'sm' &&
                    State === 'Disabled' &&
                    IsIcon === 'True'
                "
            >
                <div
                    id="5550_12486"
                    class="Pixso-frame-5550_12486 fill-gray5-32_4120 effect-shadowmd-5457_24364"
                >
                    <slot name="slot_5550_12487">
                        <X
                            id="5550_12487"
                            class="Pixso-instance-5550_12487"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div id="5550_12488" class="Pixso-frame-5550_12488">
                    <slot name="slot_5550_12489">
                        <Check
                            id="5550_12489"
                            class="Pixso-instance-5550_12489"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
            </div>
            <div
                id="5550_12446"
                class="Pixso-symbol-5550_12446 fill-brand10-1257_33461"
                v-if="
                    IsActive === 'True' &&
                    Size === 'sm' &&
                    State === 'Disabled' &&
                    IsIcon === 'True'
                "
            >
                <div id="5550_12492" class="Pixso-frame-5550_12492">
                    <slot name="slot_5550_12493">
                        <X
                            id="5550_12493"
                            class="Pixso-instance-5550_12493"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div
                    id="5550_12494"
                    class="Pixso-frame-5550_12494 fill-brand5-1257_33460 effect-shadowmd-5457_24364"
                >
                    <slot name="slot_5550_12495">
                        <Check
                            id="5550_12495"
                            class="Pixso-instance-5550_12495"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
            </div>
            <div
                id="5550_11755"
                class="Pixso-symbol-5550_11755 fill-gray20-36_1844"
                v-if="
                    IsActive === 'False' &&
                    Size === 'md' &&
                    State === 'Disabled' &&
                    IsIcon === 'True'
                "
            >
                <div
                    id="5550_12276"
                    class="Pixso-frame-5550_12276 fill-gray5-32_4120 effect-shadowmd-5457_24364"
                >
                    <slot name="slot_5550_12277">
                        <X
                            id="5550_12277"
                            class="Pixso-instance-5550_12277"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div
                    id="5550_12279"
                    class="Pixso-frame-5550_12279 effect-shadowmd-5457_24364"
                >
                    <slot name="slot_5550_12280">
                        <Check
                            id="5550_12280"
                            class="Pixso-instance-5550_12280"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
            </div>
            <div
                id="5550_11751"
                class="Pixso-symbol-5550_11751 fill-brand10-1257_33461"
                v-if="
                    IsActive === 'True' &&
                    Size === 'md' &&
                    State === 'Disabled' &&
                    IsIcon === 'True'
                "
            >
                <div id="5550_12300" class="Pixso-frame-5550_12300">
                    <slot name="slot_5550_12301">
                        <X
                            id="5550_12301"
                            class="Pixso-instance-5550_12301"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div
                    id="5550_12302"
                    class="Pixso-frame-5550_12302 fill-brand5-1257_33460 effect-shadowmd-5457_24364"
                >
                    <slot name="slot_5550_12303">
                        <Check
                            id="5550_12303"
                            class="Pixso-instance-5550_12303"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
            </div>
            <div
                id="5550_12520"
                class="Pixso-symbol-5550_12520 fill-gray20-36_1844"
                v-if="
                    IsActive === 'False' &&
                    Size === 'lg' &&
                    State === 'Disabled' &&
                    IsIcon === 'True'
                "
            >
                <div
                    id="5550_12578"
                    class="Pixso-frame-5550_12578 fill-gray5-32_4120 effect-shadowmd-5457_24364"
                >
                    <slot name="slot_5550_12579">
                        <X
                            id="5550_12579"
                            class="Pixso-instance-5550_12579"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div id="5550_12580" class="Pixso-frame-5550_12580">
                    <slot name="slot_5550_12581">
                        <Check
                            id="5550_12581"
                            class="Pixso-instance-5550_12581"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
            </div>
            <div
                id="5550_12528"
                class="Pixso-symbol-5550_12528 fill-brand10-1257_33461"
                v-if="
                    IsActive === 'True' &&
                    Size === 'lg' &&
                    State === 'Disabled' &&
                    IsIcon === 'True'
                "
            >
                <div id="5550_12584" class="Pixso-frame-5550_12584">
                    <slot name="slot_5550_12585">
                        <X
                            id="5550_12585"
                            class="Pixso-instance-5550_12585"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div
                    id="5550_12586"
                    class="Pixso-frame-5550_12586 fill-gray0-white-67_3285 effect-shadowmd-5457_24364"
                >
                    <slot name="slot_5550_12587">
                        <Check
                            id="5550_12587"
                            class="Pixso-instance-5550_12587"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
            </div>
        </div>
    </div>
</template>
<script lang="ts" setup>
import X from "@/components/X.vue";
import Check from "@/components/Check.vue";
const props = defineProps({
    IsActive: { type: String },
    Size: { type: String },
    State: { type: String },
    IsIcon: { type: String }
});
</script>
<style>
.Pixso-symbol-5550_11435 {
}
.Pixso-symbol-5550_11626 {
    width: 36px;
    height: 20px;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    align-items: center;
    padding: 2px 2px 2px 2px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-vector-5550_11627 {
    width: 28px;
    height: 28px;
    background-image: url(@/assets/images/Button23.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: relative;
    flex-shrink: 0;
}
.Pixso-symbol-5550_11643 {
    width: 36px;
    height: 20px;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    justify-content: flex-end;
    align-items: center;
    padding: 2px 2px 2px 2px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-vector-5550_11644 {
    width: 28px;
    height: 28px;
    background-image: url(@/assets/images/Button22.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: relative;
    flex-shrink: 0;
}
.Pixso-symbol-5550_11484 {
    width: 44px;
    height: 24px;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    align-items: center;
    padding: 2px 2px 2px 2px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-vector-5550_11485 {
    width: 32px;
    height: 32px;
    background-image: url(@/assets/images/Button21.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: relative;
    flex-shrink: 0;
}
.Pixso-symbol-5550_11452 {
    width: 44px;
    height: 24px;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    justify-content: flex-end;
    align-items: center;
    padding: 2px 2px 2px 2px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-vector-5550_11453 {
    width: 32px;
    height: 32px;
    background-image: url(@/assets/images/Button20.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: relative;
    flex-shrink: 0;
}
.Pixso-symbol-5550_11554 {
    width: 52px;
    height: 28px;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    align-items: center;
    padding: 2px 2px 2px 2px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-vector-5550_11555 {
    width: 36px;
    height: 36px;
    background-image: url(@/assets/images/Button19.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: relative;
    flex-shrink: 0;
}
.Pixso-symbol-5550_11570 {
    width: 52px;
    height: 28px;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    justify-content: flex-end;
    align-items: center;
    padding: 2px 2px 2px 2px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-vector-5550_11571 {
    width: 36px;
    height: 36px;
    background-image: url(@/assets/images/Button18.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: relative;
    flex-shrink: 0;
}
.Pixso-symbol-5550_11649 {
    width: 36px;
    height: 20px;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    align-items: center;
    padding: 2px 2px 2px 2px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-vector-5550_11650 {
    width: 28px;
    height: 28px;
    background-image: url(@/assets/images/Button17.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: relative;
    flex-shrink: 0;
}
.Pixso-symbol-5550_11651 {
    width: 36px;
    height: 20px;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    justify-content: flex-end;
    align-items: center;
    padding: 2px 2px 2px 2px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-vector-5550_11652 {
    width: 28px;
    height: 28px;
    background-image: url(@/assets/images/Button16.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: relative;
    flex-shrink: 0;
}
.Pixso-symbol-5550_11518 {
    width: 44px;
    height: 24px;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    align-items: center;
    padding: 2px 2px 2px 2px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-vector-5550_11519 {
    width: 32px;
    height: 32px;
    background-image: url(@/assets/images/Button15.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: relative;
    flex-shrink: 0;
}
.Pixso-symbol-5550_11516 {
    width: 44px;
    height: 24px;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    justify-content: flex-end;
    align-items: center;
    padding: 2px 2px 2px 2px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-vector-5550_11517 {
    width: 32px;
    height: 32px;
    background-image: url(@/assets/images/Button14.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: relative;
    flex-shrink: 0;
}
.Pixso-symbol-5550_11580 {
    width: 52px;
    height: 28px;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    align-items: center;
    padding: 2px 2px 2px 2px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-vector-5550_11581 {
    width: 36px;
    height: 36px;
    background-image: url(@/assets/images/Button13.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: relative;
    flex-shrink: 0;
}
.Pixso-symbol-5550_11582 {
    width: 52px;
    height: 28px;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    justify-content: flex-end;
    align-items: center;
    padding: 2px 2px 2px 2px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-vector-5550_11583 {
    width: 36px;
    height: 36px;
    background-image: url(@/assets/images/Button12.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: relative;
    flex-shrink: 0;
}
.Pixso-symbol-5550_11657 {
    width: 36px;
    height: 20px;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    align-items: center;
    padding: 2px 2px 2px 2px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-vector-5550_11658 {
    width: 28px;
    height: 28px;
    background-image: url(@/assets/images/Button11.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: relative;
    flex-shrink: 0;
}
.Pixso-symbol-5550_11659 {
    width: 36px;
    height: 20px;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    justify-content: flex-end;
    align-items: center;
    padding: 2px 2px 2px 2px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-vector-5550_11660 {
    width: 28px;
    height: 28px;
    background-image: url(@/assets/images/Button10.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: relative;
    flex-shrink: 0;
}
.Pixso-symbol-5550_11526 {
    width: 44px;
    height: 24px;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    align-items: center;
    padding: 2px 2px 2px 2px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-vector-5550_11527 {
    width: 32px;
    height: 32px;
    background-image: url(@/assets/images/Button9.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: relative;
    flex-shrink: 0;
}
.Pixso-symbol-5550_11524 {
    width: 44px;
    height: 24px;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    justify-content: flex-end;
    align-items: center;
    padding: 2px 2px 2px 2px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-vector-5550_11525 {
    width: 32px;
    height: 32px;
    background-image: url(@/assets/images/Button8.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: relative;
    flex-shrink: 0;
}
.Pixso-symbol-5550_11588 {
    width: 52px;
    height: 28px;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    align-items: center;
    padding: 2px 2px 2px 2px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-vector-5550_11589 {
    width: 36px;
    height: 36px;
    background-image: url(@/assets/images/Button7.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: relative;
    flex-shrink: 0;
}
.Pixso-symbol-5550_11590 {
    width: 52px;
    height: 28px;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    justify-content: flex-end;
    align-items: center;
    padding: 2px 2px 2px 2px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-vector-5550_11591 {
    width: 36px;
    height: 36px;
    background-image: url(@/assets/images/Button6.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: relative;
    flex-shrink: 0;
}
.Pixso-symbol-5550_11665 {
    width: 36px;
    height: 20px;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    align-items: center;
    padding: 2px 2px 2px 2px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-vector-5550_11666 {
    width: 28px;
    height: 28px;
    background-image: url(@/assets/images/Button5.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: relative;
    flex-shrink: 0;
}
.Pixso-symbol-5550_11667 {
    width: 36px;
    height: 20px;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    justify-content: flex-end;
    align-items: center;
    padding: 2px 2px 2px 2px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-vector-5550_11668 {
    width: 28px;
    height: 28px;
    background-image: url(@/assets/images/Button4.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: relative;
    flex-shrink: 0;
}
.Pixso-symbol-5550_11534 {
    width: 44px;
    height: 24px;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    align-items: center;
    padding: 2px 2px 2px 2px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-vector-5550_11535 {
    width: 32px;
    height: 32px;
    background-image: url(@/assets/images/Button3.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: relative;
    flex-shrink: 0;
}
.Pixso-symbol-5550_11532 {
    width: 44px;
    height: 24px;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    justify-content: flex-end;
    align-items: center;
    padding: 2px 2px 2px 2px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-vector-5550_11533 {
    width: 32px;
    height: 32px;
    background-image: url(@/assets/images/Button2.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: relative;
    flex-shrink: 0;
}
.Pixso-symbol-5550_11596 {
    width: 52px;
    height: 28px;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    align-items: center;
    padding: 2px 2px 2px 2px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-vector-5550_11597 {
    width: 36px;
    height: 36px;
    background-image: url(@/assets/images/Button1.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: relative;
    flex-shrink: 0;
}
.Pixso-symbol-5550_11598 {
    width: 52px;
    height: 28px;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    justify-content: flex-end;
    align-items: center;
    padding: 2px 2px 2px 2px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-vector-5550_11599 {
    width: 36px;
    height: 36px;
    background-image: url(@/assets/images/Button0.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: relative;
    flex-shrink: 0;
}
.Pixso-symbol-5550_12434 {
    width: 36px;
    height: 20px;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    align-items: center;
    padding: 2px 2px 2px 2px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-frame-5550_12450 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5550_12452 {
    width: 8px;
    height: 8px;
}
.Pixso-frame-5550_12451 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5550_12454 {
    width: 8px;
    height: 8px;
}
.Pixso-symbol-5550_12442 {
    width: 36px;
    height: 20px;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    justify-content: flex-end;
    align-items: center;
    padding: 2px 2px 2px 2px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-frame-5550_12458 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5550_12457 {
    width: 8px;
    height: 8px;
}
.Pixso-frame-5550_12456 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5550_12459 {
    width: 8px;
    height: 8px;
}
.Pixso-symbol-5550_11719 {
    width: 44px;
    height: 24px;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    align-items: center;
    padding: 2px 2px 2px 2px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-frame-5550_11773 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5550_11770 {
    width: 10px;
    height: 10px;
}
.Pixso-frame-5550_12260 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5550_12261 {
    width: 10px;
    height: 10px;
}
.Pixso-symbol-5550_11717 {
    width: 44px;
    height: 24px;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    justify-content: flex-end;
    align-items: center;
    padding: 2px 2px 2px 2px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-frame-5550_12282 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5550_12283 {
    width: 10px;
    height: 10px;
}
.Pixso-frame-5550_12284 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5550_12285 {
    width: 10px;
    height: 10px;
}
.Pixso-symbol-5550_12514 {
    width: 52px;
    height: 28px;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    align-items: center;
    padding: 2px 2px 2px 2px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-frame-5550_12530 {
    width: 24px;
    height: 24px;
    position: relative;
    flex-shrink: 0;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5550_12532 {
    width: 12px;
    height: 12px;
}
.Pixso-frame-5550_12534 {
    width: 24px;
    height: 24px;
    position: relative;
    flex-shrink: 0;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5550_12535 {
    width: 12px;
    height: 12px;
}
.Pixso-symbol-5550_12522 {
    width: 52px;
    height: 28px;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    justify-content: flex-end;
    align-items: center;
    padding: 2px 2px 2px 2px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-frame-5550_12554 {
    width: 24px;
    height: 24px;
    position: relative;
    flex-shrink: 0;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5550_12555 {
    width: 12px;
    height: 12px;
}
.Pixso-frame-5550_12552 {
    width: 24px;
    height: 24px;
    position: relative;
    flex-shrink: 0;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5550_12553 {
    width: 12px;
    height: 12px;
}
.Pixso-symbol-5550_12440 {
    width: 36px;
    height: 20px;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    align-items: center;
    padding: 2px 2px 2px 2px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-frame-5550_12462 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5550_12463 {
    width: 8px;
    height: 8px;
}
.Pixso-frame-5550_12464 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5550_12465 {
    width: 8px;
    height: 8px;
}
.Pixso-symbol-5550_12448 {
    width: 36px;
    height: 20px;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    justify-content: flex-end;
    align-items: center;
    padding: 2px 2px 2px 2px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-frame-5550_12468 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5550_12469 {
    width: 8px;
    height: 8px;
}
.Pixso-frame-5550_12470 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5550_12471 {
    width: 8px;
    height: 8px;
}
.Pixso-symbol-5550_11759 {
    width: 44px;
    height: 24px;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    align-items: center;
    padding: 2px 2px 2px 2px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-frame-5550_12264 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5550_12265 {
    width: 10px;
    height: 10px;
}
.Pixso-frame-5550_12267 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5550_12268 {
    width: 10px;
    height: 10px;
}
.Pixso-symbol-5550_11757 {
    width: 44px;
    height: 24px;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    justify-content: flex-end;
    align-items: center;
    padding: 2px 2px 2px 2px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-frame-5550_12288 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5550_12289 {
    width: 10px;
    height: 10px;
}
.Pixso-frame-5550_12290 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5550_12291 {
    width: 10px;
    height: 10px;
}
.Pixso-symbol-5550_12516 {
    width: 52px;
    height: 28px;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    align-items: center;
    padding: 2px 2px 2px 2px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-frame-5550_12540 {
    width: 24px;
    height: 24px;
    position: relative;
    flex-shrink: 0;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5550_12541 {
    width: 12px;
    height: 12px;
}
.Pixso-frame-5550_12542 {
    width: 24px;
    height: 24px;
    position: relative;
    flex-shrink: 0;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5550_12543 {
    width: 12px;
    height: 12px;
}
.Pixso-symbol-5550_12524 {
    width: 52px;
    height: 28px;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    justify-content: flex-end;
    align-items: center;
    padding: 2px 2px 2px 2px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-frame-5550_12566 {
    width: 24px;
    height: 24px;
    position: relative;
    flex-shrink: 0;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5550_12567 {
    width: 12px;
    height: 12px;
}
.Pixso-frame-5550_12568 {
    width: 24px;
    height: 24px;
    position: relative;
    flex-shrink: 0;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5550_12569 {
    width: 12px;
    height: 12px;
}
.Pixso-symbol-5550_12436 {
    width: 36px;
    height: 20px;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    align-items: center;
    padding: 2px 2px 2px 2px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-frame-5550_12474 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5550_12475 {
    width: 8px;
    height: 8px;
}
.Pixso-frame-5550_12476 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5550_12477 {
    width: 8px;
    height: 8px;
}
.Pixso-symbol-5550_12444 {
    width: 36px;
    height: 20px;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    justify-content: flex-end;
    align-items: center;
    padding: 2px 2px 2px 2px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-frame-5550_12480 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5550_12481 {
    width: 8px;
    height: 8px;
}
.Pixso-frame-5550_12482 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5550_12483 {
    width: 8px;
    height: 8px;
}
.Pixso-symbol-5550_11753 {
    width: 44px;
    height: 24px;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    align-items: center;
    padding: 2px 2px 2px 2px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-frame-5550_12270 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5550_12271 {
    width: 10px;
    height: 10px;
}
.Pixso-frame-5550_12273 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5550_12274 {
    width: 10px;
    height: 10px;
}
.Pixso-symbol-5550_11749 {
    width: 44px;
    height: 24px;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    justify-content: flex-end;
    align-items: center;
    padding: 2px 2px 2px 2px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-frame-5550_12294 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5550_12295 {
    width: 10px;
    height: 10px;
}
.Pixso-frame-5550_12296 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5550_12297 {
    width: 10px;
    height: 10px;
}
.Pixso-symbol-5550_12518 {
    width: 52px;
    height: 28px;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    align-items: center;
    padding: 2px 2px 2px 2px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-frame-5550_12546 {
    width: 24px;
    height: 24px;
    position: relative;
    flex-shrink: 0;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5550_12547 {
    width: 12px;
    height: 12px;
}
.Pixso-frame-5550_12548 {
    width: 24px;
    height: 24px;
    position: relative;
    flex-shrink: 0;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5550_12549 {
    width: 12px;
    height: 12px;
}
.Pixso-symbol-5550_12526 {
    width: 52px;
    height: 28px;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    justify-content: flex-end;
    align-items: center;
    padding: 2px 2px 2px 2px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-frame-5550_12572 {
    width: 24px;
    height: 24px;
    position: relative;
    flex-shrink: 0;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5550_12573 {
    width: 12px;
    height: 12px;
}
.Pixso-frame-5550_12574 {
    width: 24px;
    height: 24px;
    position: relative;
    flex-shrink: 0;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5550_12575 {
    width: 12px;
    height: 12px;
}
.Pixso-symbol-5550_12438 {
    width: 36px;
    height: 20px;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    align-items: center;
    padding: 2px 2px 2px 2px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-frame-5550_12486 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5550_12487 {
    width: 8px;
    height: 8px;
}
.Pixso-frame-5550_12488 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5550_12489 {
    width: 8px;
    height: 8px;
}
.Pixso-symbol-5550_12446 {
    width: 36px;
    height: 20px;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    justify-content: flex-end;
    align-items: center;
    padding: 2px 2px 2px 2px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-frame-5550_12492 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5550_12493 {
    width: 8px;
    height: 8px;
}
.Pixso-frame-5550_12494 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5550_12495 {
    width: 8px;
    height: 8px;
}
.Pixso-symbol-5550_11755 {
    width: 44px;
    height: 24px;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    align-items: center;
    padding: 2px 2px 2px 2px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-frame-5550_12276 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5550_12277 {
    width: 10px;
    height: 10px;
}
.Pixso-frame-5550_12279 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5550_12280 {
    width: 10px;
    height: 10px;
}
.Pixso-symbol-5550_11751 {
    width: 44px;
    height: 24px;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    justify-content: flex-end;
    align-items: center;
    padding: 2px 2px 2px 2px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-frame-5550_12300 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5550_12301 {
    width: 10px;
    height: 10px;
}
.Pixso-frame-5550_12302 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5550_12303 {
    width: 10px;
    height: 10px;
}
.Pixso-symbol-5550_12520 {
    width: 52px;
    height: 28px;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    align-items: center;
    padding: 2px 2px 2px 2px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-frame-5550_12578 {
    width: 24px;
    height: 24px;
    position: relative;
    flex-shrink: 0;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5550_12579 {
    width: 12px;
    height: 12px;
}
.Pixso-frame-5550_12580 {
    width: 24px;
    height: 24px;
    position: relative;
    flex-shrink: 0;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5550_12581 {
    width: 12px;
    height: 12px;
}
.Pixso-symbol-5550_12528 {
    width: 52px;
    height: 28px;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    justify-content: flex-end;
    align-items: center;
    padding: 2px 2px 2px 2px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-frame-5550_12584 {
    width: 24px;
    height: 24px;
    position: relative;
    flex-shrink: 0;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5550_12585 {
    width: 12px;
    height: 12px;
}
.Pixso-frame-5550_12586 {
    width: 24px;
    height: 24px;
    position: relative;
    flex-shrink: 0;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5550_12587 {
    width: 12px;
    height: 12px;
}

.Pixso-instance-5550_12452 .Pixso-symbol-5579_151156 {
    width: 8px;
    height: 8px;
    position: absolute;
    left: 4px;
    top: 4px;
    background-color: transparent;
}
.Pixso-instance-5550_12452 .Pixso-vector-5579_151157 {
    width: 65.64%;
    height: 65.65%;
    position: absolute;
    left: 17.18%;
    right: 17.18%;
    top: 17.17%;
    bottom: 17.18%;
}
.Pixso-instance-5550_12454 .Pixso-symbol-5578_149511 {
    width: 8px;
    height: 8px;
    position: absolute;
    left: 4px;
    top: 4px;
    background-color: transparent;
}
.Pixso-instance-5550_12454 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5550_12457 .Pixso-symbol-5579_151156 {
    width: 8px;
    height: 8px;
    position: absolute;
    left: 4px;
    top: 4px;
    background-color: transparent;
}
.Pixso-instance-5550_12457 .Pixso-vector-5579_151157 {
    width: 65.64%;
    height: 65.65%;
    position: absolute;
    left: 17.18%;
    right: 17.18%;
    top: 17.17%;
    bottom: 17.18%;
}
.Pixso-instance-5550_12459 .Pixso-symbol-5578_149511 {
    width: 8px;
    height: 8px;
    position: absolute;
    left: 4px;
    top: 4px;
    background-color: transparent;
}
.Pixso-instance-5550_12459 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5550_11770 .Pixso-symbol-5579_151156 {
    width: 10px;
    height: 10px;
    position: absolute;
    left: 5px;
    top: 5px;
    background-color: transparent;
}
.Pixso-instance-5550_11770 .Pixso-vector-5579_151157 {
    width: 65.64%;
    height: 65.65%;
    position: absolute;
    left: 17.18%;
    right: 17.18%;
    top: 17.17%;
    bottom: 17.18%;
}
.Pixso-instance-5550_12261 .Pixso-symbol-5578_149511 {
    width: 10px;
    height: 10px;
    position: absolute;
    left: 5px;
    top: 5px;
    background-color: transparent;
}
.Pixso-instance-5550_12261 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5550_12283 .Pixso-symbol-5579_151156 {
    width: 10px;
    height: 10px;
    position: absolute;
    left: 5px;
    top: 5px;
    background-color: transparent;
}
.Pixso-instance-5550_12283 .Pixso-vector-5579_151157 {
    width: 65.64%;
    height: 65.65%;
    position: absolute;
    left: 17.18%;
    right: 17.18%;
    top: 17.17%;
    bottom: 17.18%;
}
.Pixso-instance-5550_12285 .Pixso-symbol-5578_149511 {
    width: 10px;
    height: 10px;
    position: absolute;
    left: 5px;
    top: 5px;
    background-color: transparent;
}
.Pixso-instance-5550_12285 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5550_12532 .Pixso-symbol-5579_151156 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 6px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5550_12532 .Pixso-vector-5579_151157 {
    width: 65.64%;
    height: 65.65%;
    position: absolute;
    left: 17.18%;
    right: 17.18%;
    top: 17.17%;
    bottom: 17.18%;
}
.Pixso-instance-5550_12535 .Pixso-symbol-5578_149511 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 6px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5550_12535 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5550_12555 .Pixso-symbol-5579_151156 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 6px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5550_12555 .Pixso-vector-5579_151157 {
    width: 65.64%;
    height: 65.65%;
    position: absolute;
    left: 17.18%;
    right: 17.18%;
    top: 17.17%;
    bottom: 17.18%;
}
.Pixso-instance-5550_12553 .Pixso-symbol-5578_149511 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 6px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5550_12553 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5550_12463 .Pixso-symbol-5579_151156 {
    width: 8px;
    height: 8px;
    position: absolute;
    left: 4px;
    top: 4px;
    background-color: transparent;
}
.Pixso-instance-5550_12463 .Pixso-vector-5579_151157 {
    width: 65.64%;
    height: 65.65%;
    position: absolute;
    left: 17.18%;
    right: 17.18%;
    top: 17.17%;
    bottom: 17.18%;
}
.Pixso-instance-5550_12465 .Pixso-symbol-5578_149511 {
    width: 8px;
    height: 8px;
    position: absolute;
    left: 4px;
    top: 4px;
    background-color: transparent;
}
.Pixso-instance-5550_12465 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5550_12469 .Pixso-symbol-5579_151156 {
    width: 8px;
    height: 8px;
    position: absolute;
    left: 4px;
    top: 4px;
    background-color: transparent;
}
.Pixso-instance-5550_12469 .Pixso-vector-5579_151157 {
    width: 65.64%;
    height: 65.65%;
    position: absolute;
    left: 17.18%;
    right: 17.18%;
    top: 17.17%;
    bottom: 17.18%;
}
.Pixso-instance-5550_12471 .Pixso-symbol-5578_149511 {
    width: 8px;
    height: 8px;
    position: absolute;
    left: 4px;
    top: 4px;
    background-color: transparent;
}
.Pixso-instance-5550_12471 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5550_12265 .Pixso-symbol-5579_151156 {
    width: 10px;
    height: 10px;
    position: absolute;
    left: 5px;
    top: 5px;
    background-color: transparent;
}
.Pixso-instance-5550_12265 .Pixso-vector-5579_151157 {
    width: 65.64%;
    height: 65.65%;
    position: absolute;
    left: 17.18%;
    right: 17.18%;
    top: 17.17%;
    bottom: 17.18%;
}
.Pixso-instance-5550_12268 .Pixso-symbol-5578_149511 {
    width: 10px;
    height: 10px;
    position: absolute;
    left: 5px;
    top: 5px;
    background-color: transparent;
}
.Pixso-instance-5550_12268 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5550_12289 .Pixso-symbol-5579_151156 {
    width: 10px;
    height: 10px;
    position: absolute;
    left: 5px;
    top: 5px;
    background-color: transparent;
}
.Pixso-instance-5550_12289 .Pixso-vector-5579_151157 {
    width: 65.64%;
    height: 65.65%;
    position: absolute;
    left: 17.18%;
    right: 17.18%;
    top: 17.17%;
    bottom: 17.18%;
}
.Pixso-instance-5550_12291 .Pixso-symbol-5578_149511 {
    width: 10px;
    height: 10px;
    position: absolute;
    left: 5px;
    top: 5px;
    background-color: transparent;
}
.Pixso-instance-5550_12291 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5550_12541 .Pixso-symbol-5579_151156 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 6px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5550_12541 .Pixso-vector-5579_151157 {
    width: 65.64%;
    height: 65.65%;
    position: absolute;
    left: 17.18%;
    right: 17.18%;
    top: 17.17%;
    bottom: 17.18%;
}
.Pixso-instance-5550_12543 .Pixso-symbol-5578_149511 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 6px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5550_12543 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5550_12567 .Pixso-symbol-5579_151156 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 6px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5550_12567 .Pixso-vector-5579_151157 {
    width: 65.64%;
    height: 65.65%;
    position: absolute;
    left: 17.18%;
    right: 17.18%;
    top: 17.17%;
    bottom: 17.18%;
}
.Pixso-instance-5550_12569 .Pixso-symbol-5578_149511 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 6px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5550_12569 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5550_12475 .Pixso-symbol-5579_151156 {
    width: 8px;
    height: 8px;
    position: absolute;
    left: 4px;
    top: 4px;
    background-color: transparent;
}
.Pixso-instance-5550_12475 .Pixso-vector-5579_151157 {
    width: 65.64%;
    height: 65.65%;
    position: absolute;
    left: 17.18%;
    right: 17.18%;
    top: 17.17%;
    bottom: 17.18%;
}
.Pixso-instance-5550_12477 .Pixso-symbol-5578_149511 {
    width: 8px;
    height: 8px;
    position: absolute;
    left: 4px;
    top: 4px;
    background-color: transparent;
}
.Pixso-instance-5550_12477 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5550_12481 .Pixso-symbol-5579_151156 {
    width: 8px;
    height: 8px;
    position: absolute;
    left: 4px;
    top: 4px;
    background-color: transparent;
}
.Pixso-instance-5550_12481 .Pixso-vector-5579_151157 {
    width: 65.64%;
    height: 65.65%;
    position: absolute;
    left: 17.18%;
    right: 17.18%;
    top: 17.17%;
    bottom: 17.18%;
}
.Pixso-instance-5550_12483 .Pixso-symbol-5578_149511 {
    width: 8px;
    height: 8px;
    position: absolute;
    left: 4px;
    top: 4px;
    background-color: transparent;
}
.Pixso-instance-5550_12483 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5550_12271 .Pixso-symbol-5579_151156 {
    width: 10px;
    height: 10px;
    position: absolute;
    left: 5px;
    top: 5px;
    background-color: transparent;
}
.Pixso-instance-5550_12271 .Pixso-vector-5579_151157 {
    width: 65.64%;
    height: 65.65%;
    position: absolute;
    left: 17.18%;
    right: 17.18%;
    top: 17.17%;
    bottom: 17.18%;
}
.Pixso-instance-5550_12274 .Pixso-symbol-5578_149511 {
    width: 10px;
    height: 10px;
    position: absolute;
    left: 5px;
    top: 5px;
    background-color: transparent;
}
.Pixso-instance-5550_12274 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5550_12295 .Pixso-symbol-5579_151156 {
    width: 10px;
    height: 10px;
    position: absolute;
    left: 5px;
    top: 5px;
    background-color: transparent;
}
.Pixso-instance-5550_12295 .Pixso-vector-5579_151157 {
    width: 65.64%;
    height: 65.65%;
    position: absolute;
    left: 17.18%;
    right: 17.18%;
    top: 17.17%;
    bottom: 17.18%;
}
.Pixso-instance-5550_12297 .Pixso-symbol-5578_149511 {
    width: 10px;
    height: 10px;
    position: absolute;
    left: 5px;
    top: 5px;
    background-color: transparent;
}
.Pixso-instance-5550_12297 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5550_12547 .Pixso-symbol-5579_151156 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 6px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5550_12547 .Pixso-vector-5579_151157 {
    width: 65.64%;
    height: 65.65%;
    position: absolute;
    left: 17.18%;
    right: 17.18%;
    top: 17.17%;
    bottom: 17.18%;
}
.Pixso-instance-5550_12549 .Pixso-symbol-5578_149511 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 6px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5550_12549 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5550_12573 .Pixso-symbol-5579_151156 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 6px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5550_12573 .Pixso-vector-5579_151157 {
    width: 65.64%;
    height: 65.65%;
    position: absolute;
    left: 17.18%;
    right: 17.18%;
    top: 17.17%;
    bottom: 17.18%;
}
.Pixso-instance-5550_12575 .Pixso-symbol-5578_149511 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 6px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5550_12575 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5550_12487 .Pixso-symbol-5579_151156 {
    width: 8px;
    height: 8px;
    position: absolute;
    left: 4px;
    top: 4px;
    background-color: transparent;
}
.Pixso-instance-5550_12487 .Pixso-vector-5579_151157 {
    width: 65.64%;
    height: 65.65%;
    position: absolute;
    left: 17.18%;
    right: 17.18%;
    top: 17.17%;
    bottom: 17.18%;
}
.Pixso-instance-5550_12489 .Pixso-symbol-5578_149511 {
    width: 8px;
    height: 8px;
    position: absolute;
    left: 4px;
    top: 4px;
    background-color: transparent;
}
.Pixso-instance-5550_12489 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5550_12493 .Pixso-symbol-5579_151156 {
    width: 8px;
    height: 8px;
    position: absolute;
    left: 4px;
    top: 4px;
    background-color: transparent;
}
.Pixso-instance-5550_12493 .Pixso-vector-5579_151157 {
    width: 65.64%;
    height: 65.65%;
    position: absolute;
    left: 17.18%;
    right: 17.18%;
    top: 17.17%;
    bottom: 17.18%;
}
.Pixso-instance-5550_12495 .Pixso-symbol-5578_149511 {
    width: 8px;
    height: 8px;
    position: absolute;
    left: 4px;
    top: 4px;
    background-color: transparent;
}
.Pixso-instance-5550_12495 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5550_12277 .Pixso-symbol-5579_151156 {
    width: 10px;
    height: 10px;
    position: absolute;
    left: 5px;
    top: 5px;
    background-color: transparent;
}
.Pixso-instance-5550_12277 .Pixso-vector-5579_151157 {
    width: 65.64%;
    height: 65.65%;
    position: absolute;
    left: 17.18%;
    right: 17.18%;
    top: 17.17%;
    bottom: 17.18%;
}
.Pixso-instance-5550_12280 .Pixso-symbol-5578_149511 {
    width: 10px;
    height: 10px;
    position: absolute;
    left: 5px;
    top: 5px;
    background-color: transparent;
}
.Pixso-instance-5550_12280 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5550_12301 .Pixso-symbol-5579_151156 {
    width: 10px;
    height: 10px;
    position: absolute;
    left: 5px;
    top: 5px;
    background-color: transparent;
}
.Pixso-instance-5550_12301 .Pixso-vector-5579_151157 {
    width: 65.64%;
    height: 65.65%;
    position: absolute;
    left: 17.18%;
    right: 17.18%;
    top: 17.17%;
    bottom: 17.18%;
}
.Pixso-instance-5550_12303 .Pixso-symbol-5578_149511 {
    width: 10px;
    height: 10px;
    position: absolute;
    left: 5px;
    top: 5px;
    background-color: transparent;
}
.Pixso-instance-5550_12303 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5550_12579 .Pixso-symbol-5579_151156 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 6px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5550_12579 .Pixso-vector-5579_151157 {
    width: 65.64%;
    height: 65.65%;
    position: absolute;
    left: 17.18%;
    right: 17.18%;
    top: 17.17%;
    bottom: 17.18%;
}
.Pixso-instance-5550_12581 .Pixso-symbol-5578_149511 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 6px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5550_12581 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5550_12585 .Pixso-symbol-5579_151156 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 6px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5550_12585 .Pixso-vector-5579_151157 {
    width: 65.64%;
    height: 65.65%;
    position: absolute;
    left: 17.18%;
    right: 17.18%;
    top: 17.17%;
    bottom: 17.18%;
}
.Pixso-instance-5550_12587 .Pixso-symbol-5578_149511 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 6px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5550_12587 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
</style>
