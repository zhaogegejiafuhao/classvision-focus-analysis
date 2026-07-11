<template>
    <div class="component-5468_1034">
        <div id="5468_1034" class="Pixso-symbol-5468_1034">
            <div
                id="5468_1031"
                class="Pixso-symbol-5468_1031 fill-avatar1-5468_692 fill-avatar2-5468_693 fill-avatar3-5468_694 fill-avatar4-5468_695 fill-avatar5-5468_696 fill-avatar6-5468_697 fill-avatar7-5468_698"
                v-if="Size === 'xs' && Type === 'Image' && Indicator === 'None'"
            ></div>
            <div
                id="5468_1032"
                class="Pixso-symbol-5468_1032 fill-avatar1-5468_692 fill-avatar2-5468_693 fill-avatar3-5468_694 fill-avatar4-5468_695 fill-avatar5-5468_696 fill-avatar6-5468_697 fill-avatar7-5468_698"
                v-if="Size === 'sm' && Type === 'Image' && Indicator === 'None'"
            ></div>
            <div
                id="5468_1033"
                class="Pixso-symbol-5468_1033 fill-avatar1-5468_692 fill-avatar7-5468_698 fill-avatar6-5468_697 fill-avatar5-5468_696 fill-avatar4-5468_695 fill-avatar3-5468_694 fill-avatar2-5468_693 fill-avatar11-5468_702 fill-avatar10-5468_701 fill-avatar9-5468_700 fill-avatar8-5468_699"
                v-if="Size === 'md' && Type === 'Image' && Indicator === 'None'"
            ></div>
            <div
                id="5468_1029"
                class="Pixso-symbol-5468_1029 fill-avatar1-5468_692 fill-avatar2-5468_693 fill-avatar3-5468_694"
                v-if="Size === 'lg' && Type === 'Image' && Indicator === 'None'"
            ></div>
            <div
                id="5468_1030"
                class="Pixso-symbol-5468_1030 fill-avatar1-5468_692"
                v-if="Size === 'xl' && Type === 'Image' && Indicator === 'None'"
            ></div>
            <div
                id="5468_1022"
                class="Pixso-symbol-5468_1022 fill-avatar1-5468_692"
                v-if="
                    Size === '2xl' && Type === 'Image' && Indicator === 'None'
                "
            ></div>
            <div
                id="5472_2395"
                class="Pixso-symbol-5472_2395 fill-brand5-1257_33460"
                v-if="
                    Size === 'xs' &&
                    Type === 'Placeholder' &&
                    Indicator === 'None'
                "
            >
                <slot name="slot_5472_2424">
                    <User
                        id="5472_2424"
                        class="Pixso-instance-5472_2424"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
            </div>
            <div
                id="5472_2396"
                class="Pixso-symbol-5472_2396 fill-brand5-1257_33460"
                v-if="
                    Size === 'sm' &&
                    Type === 'Placeholder' &&
                    Indicator === 'None'
                "
            >
                <slot name="slot_5472_2422">
                    <User
                        id="5472_2422"
                        class="Pixso-instance-5472_2422"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
            </div>
            <div
                id="5472_2397"
                class="Pixso-symbol-5472_2397 fill-brand5-1257_33460"
                v-if="
                    Size === 'md' &&
                    Type === 'Placeholder' &&
                    Indicator === 'None'
                "
            >
                <slot name="slot_5472_2420">
                    <User
                        id="5472_2420"
                        class="Pixso-instance-5472_2420"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
            </div>
            <div
                id="5472_2398"
                class="Pixso-symbol-5472_2398 fill-brand5-1257_33460"
                v-if="
                    Size === 'lg' &&
                    Type === 'Placeholder' &&
                    Indicator === 'None'
                "
            >
                <slot name="slot_5472_2418">
                    <User
                        id="5472_2418"
                        class="Pixso-instance-5472_2418"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
            </div>
            <div
                id="5472_2399"
                class="Pixso-symbol-5472_2399 fill-brand5-1257_33460"
                v-if="
                    Size === 'xl' &&
                    Type === 'Placeholder' &&
                    Indicator === 'None'
                "
            >
                <slot name="slot_5472_2416">
                    <User
                        id="5472_2416"
                        class="Pixso-instance-5472_2416"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
            </div>
            <div
                id="5472_2400"
                class="Pixso-symbol-5472_2400 fill-brand5-1257_33460"
                v-if="
                    Size === '2xl' &&
                    Type === 'Placeholder' &&
                    Indicator === 'None'
                "
            >
                <slot name="slot_5472_2414">
                    <User
                        id="5472_2414"
                        class="Pixso-instance-5472_2414"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
            </div>
            <div
                id="5472_2650"
                class="Pixso-symbol-5472_2650 fill-brand5-1257_33460"
                v-if="Size === 'xs' && Type === 'Text' && Indicator === 'None'"
            >
                <slot name="slot_5475_5120">
                    <p
                        id="5475_5120"
                        class="Pixso-paragraph-5475_5120 fill-brand60-1257_33467-paragraph text-text-xsextrabold-439_9519"
                    >
                        {{ "SL" }}
                    </p>
                </slot>
            </div>
            <div
                id="5472_2652"
                class="Pixso-symbol-5472_2652 fill-brand5-1257_33460"
                v-if="Size === 'sm' && Type === 'Text' && Indicator === 'None'"
            >
                <slot name="slot_5475_5119">
                    <p
                        id="5475_5119"
                        class="Pixso-paragraph-5475_5119 fill-brand60-1257_33467-paragraph text-text-smextrabold-423_3207"
                    >
                        {{ "SL" }}
                    </p>
                </slot>
            </div>
            <div
                id="5472_2654"
                class="Pixso-symbol-5472_2654 fill-brand5-1257_33460"
                v-if="Size === 'md' && Type === 'Text' && Indicator === 'None'"
            >
                <slot name="slot_5475_5118">
                    <p
                        id="5475_5118"
                        class="Pixso-paragraph-5475_5118 fill-brand60-1257_33467-paragraph text-text-mdextrabold-423_3204"
                    >
                        {{ "SL" }}
                    </p>
                </slot>
            </div>
            <div
                id="5472_2656"
                class="Pixso-symbol-5472_2656 fill-brand5-1257_33460"
                v-if="Size === 'lg' && Type === 'Text' && Indicator === 'None'"
            >
                <slot name="slot_5475_5117">
                    <p
                        id="5475_5117"
                        class="Pixso-paragraph-5475_5117 fill-brand60-1257_33467-paragraph text-text-lgextrabold-423_3201"
                    >
                        {{ "SL" }}
                    </p>
                </slot>
            </div>
            <div
                id="5472_2658"
                class="Pixso-symbol-5472_2658 fill-brand5-1257_33460"
                v-if="Size === 'xl' && Type === 'Text' && Indicator === 'None'"
            >
                <slot name="slot_5475_5116">
                    <p
                        id="5475_5116"
                        class="Pixso-paragraph-5475_5116 fill-brand60-1257_33467-paragraph text-text-xlextrabold-423_3198"
                    >
                        {{ "SL" }}
                    </p>
                </slot>
            </div>
            <div
                id="5472_2660"
                class="Pixso-symbol-5472_2660 fill-brand5-1257_33460"
                v-if="Size === '2xl' && Type === 'Text' && Indicator === 'None'"
            >
                <slot name="slot_5475_5115">
                    <p
                        id="5475_5115"
                        class="Pixso-paragraph-5475_5115 fill-brand60-1257_33467-paragraph text-text-2xlextrabold-423_3195"
                    >
                        {{ "SL" }}
                    </p>
                </slot>
            </div>
            <div
                id="5471_2071"
                class="Pixso-symbol-5471_2071 fill-avatar1-5468_692"
                v-if="
                    Size === 'xs' &&
                    Type === 'Image' &&
                    Indicator === 'Status Bar'
                "
            >
                <slot name="slot_5471_2232">
                    <AvatarIndicator
                        id="5471_2232"
                        class="Pixso-instance-5471_2232"
                        Size="xs"
                        Color="Success"
                        Type="Plain"
                    />
                </slot>
            </div>
            <div
                id="5471_2072"
                class="Pixso-symbol-5471_2072 fill-avatar1-5468_692"
                v-if="
                    Size === 'sm' &&
                    Type === 'Image' &&
                    Indicator === 'Status Bar'
                "
            >
                <slot name="slot_5471_2233">
                    <AvatarIndicator
                        id="5471_2233"
                        class="Pixso-instance-5471_2233"
                        Size="sm"
                        Color="Success"
                        Type="Plain"
                    />
                </slot>
            </div>
            <div
                id="5471_2073"
                class="Pixso-symbol-5471_2073 fill-avatar1-5468_692"
                v-if="
                    Size === 'md' &&
                    Type === 'Image' &&
                    Indicator === 'Status Bar'
                "
            >
                <slot name="slot_5471_2234">
                    <AvatarIndicator
                        id="5471_2234"
                        class="Pixso-instance-5471_2234"
                        Size="md"
                        Color="Success"
                        Type="Plain"
                    />
                </slot>
            </div>
            <div
                id="5471_2074"
                class="Pixso-symbol-5471_2074 fill-avatar1-5468_692"
                v-if="
                    Size === 'lg' &&
                    Type === 'Image' &&
                    Indicator === 'Status Bar'
                "
            >
                <slot name="slot_5471_2235">
                    <AvatarIndicator
                        id="5471_2235"
                        class="Pixso-instance-5471_2235"
                        Size="lg"
                        Color="Success"
                        Type="Plain"
                    />
                </slot>
            </div>
            <div
                id="5471_2075"
                class="Pixso-symbol-5471_2075 fill-avatar1-5468_692"
                v-if="
                    Size === 'xl' &&
                    Type === 'Image' &&
                    Indicator === 'Status Bar'
                "
            >
                <slot name="slot_5471_2236">
                    <AvatarIndicator
                        id="5471_2236"
                        class="Pixso-instance-5471_2236"
                        Size="xl"
                        Color="Success"
                        Type="Plain"
                    />
                </slot>
            </div>
            <div
                id="5471_2076"
                class="Pixso-symbol-5471_2076 fill-avatar1-5468_692"
                v-if="
                    Size === '2xl' &&
                    Type === 'Image' &&
                    Indicator === 'Status Bar'
                "
            >
                <slot name="slot_5471_2237">
                    <AvatarIndicator
                        id="5471_2237"
                        class="Pixso-instance-5471_2237"
                        Size="2xl"
                        Color="Success"
                        Type="Plain"
                    />
                </slot>
            </div>
            <div
                id="5472_2426"
                class="Pixso-symbol-5472_2426 fill-brand5-1257_33460"
                v-if="
                    Size === 'xs' &&
                    Type === 'Placeholder' &&
                    Indicator === 'Status Bar'
                "
            >
                <slot name="slot_5472_2427">
                    <User
                        id="5472_2427"
                        class="Pixso-instance-5472_2427"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <slot name="slot_5472_2449">
                    <AvatarIndicator
                        id="5472_2449"
                        class="Pixso-instance-5472_2449"
                        Size="xs"
                        Color="Success"
                        Type="Plain"
                    />
                </slot>
            </div>
            <div
                id="5472_2428"
                class="Pixso-symbol-5472_2428 fill-brand5-1257_33460"
                v-if="
                    Size === 'sm' &&
                    Type === 'Placeholder' &&
                    Indicator === 'Status Bar'
                "
            >
                <slot name="slot_5472_2429">
                    <User
                        id="5472_2429"
                        class="Pixso-instance-5472_2429"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <slot name="slot_5472_2448">
                    <AvatarIndicator
                        id="5472_2448"
                        class="Pixso-instance-5472_2448"
                        Size="sm"
                        Color="Success"
                        Type="Plain"
                    />
                </slot>
            </div>
            <div
                id="5472_2430"
                class="Pixso-symbol-5472_2430 fill-brand5-1257_33460"
                v-if="
                    Size === 'md' &&
                    Type === 'Placeholder' &&
                    Indicator === 'Status Bar'
                "
            >
                <slot name="slot_5472_2431">
                    <User
                        id="5472_2431"
                        class="Pixso-instance-5472_2431"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <slot name="slot_5472_2447">
                    <AvatarIndicator
                        id="5472_2447"
                        class="Pixso-instance-5472_2447"
                        Size="md"
                        Color="Success"
                        Type="Plain"
                    />
                </slot>
            </div>
            <div
                id="5472_2432"
                class="Pixso-symbol-5472_2432 fill-brand5-1257_33460"
                v-if="
                    Size === 'lg' &&
                    Type === 'Placeholder' &&
                    Indicator === 'Status Bar'
                "
            >
                <slot name="slot_5472_2433">
                    <User
                        id="5472_2433"
                        class="Pixso-instance-5472_2433"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <slot name="slot_5472_2446">
                    <AvatarIndicator
                        id="5472_2446"
                        class="Pixso-instance-5472_2446"
                        Size="lg"
                        Color="Success"
                        Type="Plain"
                    />
                </slot>
            </div>
            <div
                id="5472_2434"
                class="Pixso-symbol-5472_2434 fill-brand5-1257_33460"
                v-if="
                    Size === 'xl' &&
                    Type === 'Placeholder' &&
                    Indicator === 'Status Bar'
                "
            >
                <slot name="slot_5472_2435">
                    <User
                        id="5472_2435"
                        class="Pixso-instance-5472_2435"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <slot name="slot_5472_2445">
                    <AvatarIndicator
                        id="5472_2445"
                        class="Pixso-instance-5472_2445"
                        Size="xl"
                        Color="Success"
                        Type="Plain"
                    />
                </slot>
            </div>
            <div
                id="5472_2436"
                class="Pixso-symbol-5472_2436 fill-brand5-1257_33460"
                v-if="
                    Size === '2xl' &&
                    Type === 'Placeholder' &&
                    Indicator === 'Status Bar'
                "
            >
                <slot name="slot_5472_2437">
                    <User
                        id="5472_2437"
                        class="Pixso-instance-5472_2437"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <slot name="slot_5472_2444">
                    <AvatarIndicator
                        id="5472_2444"
                        class="Pixso-instance-5472_2444"
                        Size="2xl"
                        Color="Success"
                        Type="Plain"
                    />
                </slot>
            </div>
            <div
                id="5472_2662"
                class="Pixso-symbol-5472_2662 fill-brand5-1257_33460"
                v-if="
                    Size === 'xs' &&
                    Type === 'Text' &&
                    Indicator === 'Status Bar'
                "
            >
                <slot name="slot_5472_2664">
                    <AvatarIndicator
                        id="5472_2664"
                        class="Pixso-instance-5472_2664"
                        Size="xs"
                        Color="Success"
                        Type="Plain"
                    />
                </slot>
                <slot name="slot_5475_5147">
                    <p
                        id="5475_5147"
                        class="Pixso-paragraph-5475_5147 fill-brand60-1257_33467-paragraph text-text-xsextrabold-439_9519"
                    >
                        {{ "SL" }}
                    </p>
                </slot>
            </div>
            <div
                id="5472_2665"
                class="Pixso-symbol-5472_2665 fill-brand5-1257_33460"
                v-if="
                    Size === 'sm' &&
                    Type === 'Text' &&
                    Indicator === 'Status Bar'
                "
            >
                <slot name="slot_5472_2667">
                    <AvatarIndicator
                        id="5472_2667"
                        class="Pixso-instance-5472_2667"
                        Size="sm"
                        Color="Success"
                        Type="Plain"
                    />
                </slot>
                <slot name="slot_5475_5143">
                    <p
                        id="5475_5143"
                        class="Pixso-paragraph-5475_5143 fill-brand60-1257_33467-paragraph text-text-smextrabold-423_3207"
                    >
                        {{ "SL" }}
                    </p>
                </slot>
            </div>
            <div
                id="5472_2668"
                class="Pixso-symbol-5472_2668 fill-brand5-1257_33460"
                v-if="
                    Size === 'md' &&
                    Type === 'Text' &&
                    Indicator === 'Status Bar'
                "
            >
                <slot name="slot_5472_2670">
                    <AvatarIndicator
                        id="5472_2670"
                        class="Pixso-instance-5472_2670"
                        Size="md"
                        Color="Success"
                        Type="Plain"
                    />
                </slot>
                <slot name="slot_5475_5139">
                    <p
                        id="5475_5139"
                        class="Pixso-paragraph-5475_5139 fill-brand60-1257_33467-paragraph text-text-mdextrabold-423_3204"
                    >
                        {{ "SL" }}
                    </p>
                </slot>
            </div>
            <div
                id="5472_2671"
                class="Pixso-symbol-5472_2671 fill-brand5-1257_33460"
                v-if="
                    Size === 'lg' &&
                    Type === 'Text' &&
                    Indicator === 'Status Bar'
                "
            >
                <slot name="slot_5472_2673">
                    <AvatarIndicator
                        id="5472_2673"
                        class="Pixso-instance-5472_2673"
                        Size="lg"
                        Color="Success"
                        Type="Plain"
                    />
                </slot>
                <slot name="slot_5475_5135">
                    <p
                        id="5475_5135"
                        class="Pixso-paragraph-5475_5135 fill-brand60-1257_33467-paragraph text-text-lgextrabold-423_3201"
                    >
                        {{ "SL" }}
                    </p>
                </slot>
            </div>
            <div
                id="5472_2674"
                class="Pixso-symbol-5472_2674 fill-brand5-1257_33460"
                v-if="
                    Size === 'xl' &&
                    Type === 'Text' &&
                    Indicator === 'Status Bar'
                "
            >
                <slot name="slot_5472_2676">
                    <AvatarIndicator
                        id="5472_2676"
                        class="Pixso-instance-5472_2676"
                        Size="xl"
                        Color="Success"
                        Type="Plain"
                    />
                </slot>
                <slot name="slot_5475_5131">
                    <p
                        id="5475_5131"
                        class="Pixso-paragraph-5475_5131 fill-brand60-1257_33467-paragraph text-text-xlextrabold-423_3198"
                    >
                        {{ "SL" }}
                    </p>
                </slot>
            </div>
            <div
                id="5472_2677"
                class="Pixso-symbol-5472_2677 fill-brand5-1257_33460"
                v-if="
                    Size === '2xl' &&
                    Type === 'Text' &&
                    Indicator === 'Status Bar'
                "
            >
                <slot name="slot_5472_2679">
                    <AvatarIndicator
                        id="5472_2679"
                        class="Pixso-instance-5472_2679"
                        Size="2xl"
                        Color="Success"
                        Type="Plain"
                    />
                </slot>
                <slot name="slot_5475_5127">
                    <p
                        id="5475_5127"
                        class="Pixso-paragraph-5475_5127 fill-brand60-1257_33467-paragraph text-text-2xlextrabold-423_3195"
                    >
                        {{ "SL" }}
                    </p>
                </slot>
            </div>
            <div
                id="5471_2243"
                class="Pixso-symbol-5471_2243 fill-avatar1-5468_692"
                v-if="Size === 'xs' && Type === 'Image' && Indicator === 'Text'"
            >
                <slot name="slot_5471_2244">
                    <AvatarIndicator
                        id="5471_2244"
                        class="Pixso-instance-5471_2244"
                        Size="xs"
                        Color="Destructive"
                        Type="Text"
                    />
                </slot>
            </div>
            <div
                id="5471_2245"
                class="Pixso-symbol-5471_2245 fill-avatar1-5468_692"
                v-if="Size === 'sm' && Type === 'Image' && Indicator === 'Text'"
            >
                <slot name="slot_5471_2246">
                    <AvatarIndicator
                        id="5471_2246"
                        class="Pixso-instance-5471_2246"
                        Size="sm"
                        Color="Destructive"
                        Type="Text"
                    />
                </slot>
            </div>
            <div
                id="5471_2247"
                class="Pixso-symbol-5471_2247 fill-avatar1-5468_692"
                v-if="Size === 'md' && Type === 'Image' && Indicator === 'Text'"
            >
                <slot name="slot_5471_2248">
                    <AvatarIndicator
                        id="5471_2248"
                        class="Pixso-instance-5471_2248"
                        Size="md"
                        Color="Destructive"
                        Type="Text"
                    />
                </slot>
            </div>
            <div
                id="5471_2249"
                class="Pixso-symbol-5471_2249 fill-avatar1-5468_692"
                v-if="Size === 'lg' && Type === 'Image' && Indicator === 'Text'"
            >
                <slot name="slot_5471_2250">
                    <AvatarIndicator
                        id="5471_2250"
                        class="Pixso-instance-5471_2250"
                        Size="lg"
                        Color="Destructive"
                        Type="Text"
                    />
                </slot>
            </div>
            <div
                id="5471_2251"
                class="Pixso-symbol-5471_2251 fill-avatar1-5468_692"
                v-if="Size === 'xl' && Type === 'Image' && Indicator === 'Text'"
            >
                <slot name="slot_5471_2252">
                    <AvatarIndicator
                        id="5471_2252"
                        class="Pixso-instance-5471_2252"
                        Size="xl"
                        Color="Destructive"
                        Type="Text"
                    />
                </slot>
            </div>
            <div
                id="5471_2253"
                class="Pixso-symbol-5471_2253 fill-avatar1-5468_692"
                v-if="
                    Size === '2xl' && Type === 'Image' && Indicator === 'Text'
                "
            >
                <slot name="slot_5471_2254">
                    <AvatarIndicator
                        id="5471_2254"
                        class="Pixso-instance-5471_2254"
                        Size="2xl"
                        Color="Destructive"
                        Type="Text"
                    />
                </slot>
            </div>
            <div
                id="5472_2456"
                class="Pixso-symbol-5472_2456 fill-brand5-1257_33460"
                v-if="
                    Size === 'xs' &&
                    Type === 'Placeholder' &&
                    Indicator === 'Text'
                "
            >
                <slot name="slot_5472_2457">
                    <User
                        id="5472_2457"
                        class="Pixso-instance-5472_2457"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <slot name="slot_5472_2458">
                    <AvatarIndicator
                        id="5472_2458"
                        class="Pixso-instance-5472_2458"
                        Size="xs"
                        Color="Destructive"
                        Type="Text"
                    />
                </slot>
            </div>
            <div
                id="5472_2459"
                class="Pixso-symbol-5472_2459 fill-brand5-1257_33460"
                v-if="
                    Size === 'sm' &&
                    Type === 'Placeholder' &&
                    Indicator === 'Text'
                "
            >
                <slot name="slot_5472_2460">
                    <User
                        id="5472_2460"
                        class="Pixso-instance-5472_2460"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <slot name="slot_5472_2461">
                    <AvatarIndicator
                        id="5472_2461"
                        class="Pixso-instance-5472_2461"
                        Size="sm"
                        Color="Destructive"
                        Type="Text"
                    />
                </slot>
            </div>
            <div
                id="5472_2462"
                class="Pixso-symbol-5472_2462 fill-brand5-1257_33460"
                v-if="
                    Size === 'md' &&
                    Type === 'Placeholder' &&
                    Indicator === 'Text'
                "
            >
                <slot name="slot_5472_2463">
                    <User
                        id="5472_2463"
                        class="Pixso-instance-5472_2463"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <slot name="slot_5472_2464">
                    <AvatarIndicator
                        id="5472_2464"
                        class="Pixso-instance-5472_2464"
                        Size="md"
                        Color="Destructive"
                        Type="Text"
                    />
                </slot>
            </div>
            <div
                id="5472_2465"
                class="Pixso-symbol-5472_2465 fill-brand5-1257_33460"
                v-if="
                    Size === 'lg' &&
                    Type === 'Placeholder' &&
                    Indicator === 'Text'
                "
            >
                <slot name="slot_5472_2466">
                    <User
                        id="5472_2466"
                        class="Pixso-instance-5472_2466"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <slot name="slot_5472_2467">
                    <AvatarIndicator
                        id="5472_2467"
                        class="Pixso-instance-5472_2467"
                        Size="lg"
                        Color="Destructive"
                        Type="Text"
                    />
                </slot>
            </div>
            <div
                id="5472_2468"
                class="Pixso-symbol-5472_2468 fill-brand5-1257_33460"
                v-if="
                    Size === 'xl' &&
                    Type === 'Placeholder' &&
                    Indicator === 'Text'
                "
            >
                <slot name="slot_5472_2469">
                    <User
                        id="5472_2469"
                        class="Pixso-instance-5472_2469"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <slot name="slot_5472_2470">
                    <AvatarIndicator
                        id="5472_2470"
                        class="Pixso-instance-5472_2470"
                        Size="xl"
                        Color="Destructive"
                        Type="Text"
                    />
                </slot>
            </div>
            <div
                id="5472_2471"
                class="Pixso-symbol-5472_2471 fill-brand5-1257_33460"
                v-if="
                    Size === '2xl' &&
                    Type === 'Placeholder' &&
                    Indicator === 'Text'
                "
            >
                <slot name="slot_5472_2472">
                    <User
                        id="5472_2472"
                        class="Pixso-instance-5472_2472"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <slot name="slot_5472_2473">
                    <AvatarIndicator
                        id="5472_2473"
                        class="Pixso-instance-5472_2473"
                        Size="2xl"
                        Color="Destructive"
                        Type="Text"
                    />
                </slot>
            </div>
            <div
                id="5472_2680"
                class="Pixso-symbol-5472_2680 fill-brand5-1257_33460"
                v-if="Size === 'xs' && Type === 'Text' && Indicator === 'Text'"
            >
                <slot name="slot_5472_2682">
                    <AvatarIndicator
                        id="5472_2682"
                        class="Pixso-instance-5472_2682"
                        Size="xs"
                        Color="Destructive"
                        Type="Text"
                    />
                </slot>
                <slot name="slot_5475_5148">
                    <p
                        id="5475_5148"
                        class="Pixso-paragraph-5475_5148 fill-brand60-1257_33467-paragraph text-text-xsextrabold-439_9519"
                    >
                        {{ "SL" }}
                    </p>
                </slot>
            </div>
            <div
                id="5472_2683"
                class="Pixso-symbol-5472_2683 fill-brand5-1257_33460"
                v-if="Size === 'sm' && Type === 'Text' && Indicator === 'Text'"
            >
                <slot name="slot_5472_2685">
                    <AvatarIndicator
                        id="5472_2685"
                        class="Pixso-instance-5472_2685"
                        Size="sm"
                        Color="Destructive"
                        Type="Text"
                    />
                </slot>
                <slot name="slot_5475_5144">
                    <p
                        id="5475_5144"
                        class="Pixso-paragraph-5475_5144 fill-brand60-1257_33467-paragraph text-text-smextrabold-423_3207"
                    >
                        {{ "SL" }}
                    </p>
                </slot>
            </div>
            <div
                id="5472_2686"
                class="Pixso-symbol-5472_2686 fill-brand5-1257_33460"
                v-if="Size === 'md' && Type === 'Text' && Indicator === 'Text'"
            >
                <slot name="slot_5472_2688">
                    <AvatarIndicator
                        id="5472_2688"
                        class="Pixso-instance-5472_2688"
                        Size="md"
                        Color="Destructive"
                        Type="Text"
                    />
                </slot>
                <slot name="slot_5475_5140">
                    <p
                        id="5475_5140"
                        class="Pixso-paragraph-5475_5140 fill-brand60-1257_33467-paragraph text-text-mdextrabold-423_3204"
                    >
                        {{ "SL" }}
                    </p>
                </slot>
            </div>
            <div
                id="5472_2689"
                class="Pixso-symbol-5472_2689 fill-brand5-1257_33460"
                v-if="Size === 'lg' && Type === 'Text' && Indicator === 'Text'"
            >
                <slot name="slot_5472_2691">
                    <AvatarIndicator
                        id="5472_2691"
                        class="Pixso-instance-5472_2691"
                        Size="lg"
                        Color="Destructive"
                        Type="Text"
                    />
                </slot>
                <slot name="slot_5475_5136">
                    <p
                        id="5475_5136"
                        class="Pixso-paragraph-5475_5136 fill-brand60-1257_33467-paragraph text-text-lgextrabold-423_3201"
                    >
                        {{ "SL" }}
                    </p>
                </slot>
            </div>
            <div
                id="5472_2692"
                class="Pixso-symbol-5472_2692 fill-brand5-1257_33460"
                v-if="Size === 'xl' && Type === 'Text' && Indicator === 'Text'"
            >
                <slot name="slot_5472_2694">
                    <AvatarIndicator
                        id="5472_2694"
                        class="Pixso-instance-5472_2694"
                        Size="xl"
                        Color="Destructive"
                        Type="Text"
                    />
                </slot>
                <slot name="slot_5475_5132">
                    <p
                        id="5475_5132"
                        class="Pixso-paragraph-5475_5132 fill-brand60-1257_33467-paragraph text-text-xlextrabold-423_3198"
                    >
                        {{ "SL" }}
                    </p>
                </slot>
            </div>
            <div
                id="5472_2695"
                class="Pixso-symbol-5472_2695 fill-brand5-1257_33460"
                v-if="Size === '2xl' && Type === 'Text' && Indicator === 'Text'"
            >
                <slot name="slot_5472_2697">
                    <AvatarIndicator
                        id="5472_2697"
                        class="Pixso-instance-5472_2697"
                        Size="2xl"
                        Color="Destructive"
                        Type="Text"
                    />
                </slot>
                <slot name="slot_5475_5128">
                    <p
                        id="5475_5128"
                        class="Pixso-paragraph-5475_5128 fill-brand60-1257_33467-paragraph text-text-2xlextrabold-423_3195"
                    >
                        {{ "SL" }}
                    </p>
                </slot>
            </div>
            <div
                id="5471_2282"
                class="Pixso-symbol-5471_2282 fill-avatar1-5468_692"
                v-if="
                    Size === 'xs' &&
                    Type === 'Image' &&
                    Indicator === 'Verified'
                "
            >
                <slot name="slot_6168_17874">
                    <AvatarVerifiedIcon
                        id="6168_17874"
                        class="Pixso-instance-6168_17874"
                        Size="sm"
                    />
                </slot>
            </div>
            <div
                id="5471_2284"
                class="Pixso-symbol-5471_2284 fill-avatar1-5468_692"
                v-if="
                    Size === 'sm' &&
                    Type === 'Image' &&
                    Indicator === 'Verified'
                "
            >
                <slot name="slot_6168_17869">
                    <AvatarVerifiedIcon
                        id="6168_17869"
                        class="Pixso-instance-6168_17869"
                        Size="md"
                    />
                </slot>
            </div>
            <div
                id="5471_2286"
                class="Pixso-symbol-5471_2286 fill-avatar1-5468_692"
                v-if="
                    Size === 'md' &&
                    Type === 'Image' &&
                    Indicator === 'Verified'
                "
            >
                <slot name="slot_6168_17864">
                    <AvatarVerifiedIcon
                        id="6168_17864"
                        class="Pixso-instance-6168_17864"
                        Size="lg"
                    />
                </slot>
            </div>
            <div
                id="5471_2288"
                class="Pixso-symbol-5471_2288 fill-avatar1-5468_692"
                v-if="
                    Size === 'lg' &&
                    Type === 'Image' &&
                    Indicator === 'Verified'
                "
            >
                <slot name="slot_6168_17858">
                    <AvatarVerifiedIcon
                        id="6168_17858"
                        class="Pixso-instance-6168_17858"
                        Size="xl"
                    />
                </slot>
            </div>
            <div
                id="5471_2290"
                class="Pixso-symbol-5471_2290 fill-avatar1-5468_692"
                v-if="
                    Size === 'xl' &&
                    Type === 'Image' &&
                    Indicator === 'Verified'
                "
            >
                <slot name="slot_6168_17852">
                    <AvatarVerifiedIcon
                        id="6168_17852"
                        class="Pixso-instance-6168_17852"
                        Size="2xl"
                    />
                </slot>
            </div>
            <div
                id="5471_2292"
                class="Pixso-symbol-5471_2292 fill-avatar1-5468_692"
                v-if="
                    Size === '2xl' &&
                    Type === 'Image' &&
                    Indicator === 'Verified'
                "
            >
                <slot name="slot_6168_17844">
                    <AvatarVerifiedIcon
                        id="6168_17844"
                        class="Pixso-instance-6168_17844"
                        Size="3xl"
                    />
                </slot>
            </div>
            <div
                id="5472_2492"
                class="Pixso-symbol-5472_2492 fill-brand5-1257_33460"
                v-if="
                    Size === 'xs' &&
                    Type === 'Placeholder' &&
                    Indicator === 'Verified'
                "
            >
                <slot name="slot_5472_2493">
                    <User
                        id="5472_2493"
                        class="Pixso-instance-5472_2493"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <slot name="slot_6169_17972">
                    <AvatarVerifiedIcon
                        id="6169_17972"
                        class="Pixso-instance-6169_17972"
                        Size="sm"
                    />
                </slot>
            </div>
            <div
                id="5472_2495"
                class="Pixso-symbol-5472_2495 fill-brand5-1257_33460"
                v-if="
                    Size === 'sm' &&
                    Type === 'Placeholder' &&
                    Indicator === 'Verified'
                "
            >
                <slot name="slot_5472_2496">
                    <User
                        id="5472_2496"
                        class="Pixso-instance-5472_2496"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <slot name="slot_6169_17978">
                    <AvatarVerifiedIcon
                        id="6169_17978"
                        class="Pixso-instance-6169_17978"
                        Size="md"
                    />
                </slot>
            </div>
            <div
                id="5472_2498"
                class="Pixso-symbol-5472_2498 fill-brand5-1257_33460"
                v-if="
                    Size === 'md' &&
                    Type === 'Placeholder' &&
                    Indicator === 'Verified'
                "
            >
                <slot name="slot_5472_2499">
                    <User
                        id="5472_2499"
                        class="Pixso-instance-5472_2499"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <slot name="slot_6169_17984">
                    <AvatarVerifiedIcon
                        id="6169_17984"
                        class="Pixso-instance-6169_17984"
                        Size="lg"
                    />
                </slot>
            </div>
            <div
                id="5472_2501"
                class="Pixso-symbol-5472_2501 fill-brand5-1257_33460"
                v-if="
                    Size === 'lg' &&
                    Type === 'Placeholder' &&
                    Indicator === 'Verified'
                "
            >
                <slot name="slot_5472_2502">
                    <User
                        id="5472_2502"
                        class="Pixso-instance-5472_2502"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <slot name="slot_6169_17990">
                    <AvatarVerifiedIcon
                        id="6169_17990"
                        class="Pixso-instance-6169_17990"
                        Size="xl"
                    />
                </slot>
            </div>
            <div
                id="5472_2504"
                class="Pixso-symbol-5472_2504 fill-brand5-1257_33460"
                v-if="
                    Size === 'xl' &&
                    Type === 'Placeholder' &&
                    Indicator === 'Verified'
                "
            >
                <slot name="slot_5472_2505">
                    <User
                        id="5472_2505"
                        class="Pixso-instance-5472_2505"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <slot name="slot_6169_17998">
                    <AvatarVerifiedIcon
                        id="6169_17998"
                        class="Pixso-instance-6169_17998"
                        Size="2xl"
                    />
                </slot>
            </div>
            <div
                id="5472_2507"
                class="Pixso-symbol-5472_2507 fill-brand5-1257_33460"
                v-if="
                    Size === '2xl' &&
                    Type === 'Placeholder' &&
                    Indicator === 'Verified'
                "
            >
                <slot name="slot_5472_2508">
                    <User
                        id="5472_2508"
                        class="Pixso-instance-5472_2508"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <slot name="slot_6169_18004">
                    <AvatarVerifiedIcon
                        id="6169_18004"
                        class="Pixso-instance-6169_18004"
                        Size="3xl"
                    />
                </slot>
            </div>
            <div
                id="5472_2698"
                class="Pixso-symbol-5472_2698 fill-brand5-1257_33460"
                v-if="
                    Size === 'xs' && Type === 'Text' && Indicator === 'Verified'
                "
            >
                <slot name="slot_5475_5149">
                    <p
                        id="5475_5149"
                        class="Pixso-paragraph-5475_5149 fill-brand60-1257_33467-paragraph text-text-xsextrabold-439_9519"
                    >
                        {{ "SL" }}
                    </p>
                </slot>
                <slot name="slot_6169_17975">
                    <AvatarVerifiedIcon
                        id="6169_17975"
                        class="Pixso-instance-6169_17975"
                        Size="sm"
                    />
                </slot>
            </div>
            <div
                id="5472_2701"
                class="Pixso-symbol-5472_2701 fill-brand5-1257_33460"
                v-if="
                    Size === 'sm' && Type === 'Text' && Indicator === 'Verified'
                "
            >
                <slot name="slot_5475_5145">
                    <p
                        id="5475_5145"
                        class="Pixso-paragraph-5475_5145 fill-brand60-1257_33467-paragraph text-text-smextrabold-423_3207"
                    >
                        {{ "SL" }}
                    </p>
                </slot>
                <slot name="slot_6169_17981">
                    <AvatarVerifiedIcon
                        id="6169_17981"
                        class="Pixso-instance-6169_17981"
                        Size="md"
                    />
                </slot>
            </div>
            <div
                id="5472_2704"
                class="Pixso-symbol-5472_2704 fill-brand5-1257_33460"
                v-if="
                    Size === 'md' && Type === 'Text' && Indicator === 'Verified'
                "
            >
                <slot name="slot_5475_5141">
                    <p
                        id="5475_5141"
                        class="Pixso-paragraph-5475_5141 fill-brand60-1257_33467-paragraph text-text-mdextrabold-423_3204"
                    >
                        {{ "SL" }}
                    </p>
                </slot>
                <slot name="slot_6169_17987">
                    <AvatarVerifiedIcon
                        id="6169_17987"
                        class="Pixso-instance-6169_17987"
                        Size="lg"
                    />
                </slot>
            </div>
            <div
                id="5472_2707"
                class="Pixso-symbol-5472_2707 fill-brand5-1257_33460"
                v-if="
                    Size === 'lg' && Type === 'Text' && Indicator === 'Verified'
                "
            >
                <slot name="slot_5475_5137">
                    <p
                        id="5475_5137"
                        class="Pixso-paragraph-5475_5137 fill-brand60-1257_33467-paragraph text-text-lgextrabold-423_3201"
                    >
                        {{ "SL" }}
                    </p>
                </slot>
                <slot name="slot_6169_17994">
                    <AvatarVerifiedIcon
                        id="6169_17994"
                        class="Pixso-instance-6169_17994"
                        Size="xl"
                    />
                </slot>
            </div>
            <div
                id="5472_2710"
                class="Pixso-symbol-5472_2710 fill-brand5-1257_33460"
                v-if="
                    Size === 'xl' && Type === 'Text' && Indicator === 'Verified'
                "
            >
                <slot name="slot_5475_5133">
                    <p
                        id="5475_5133"
                        class="Pixso-paragraph-5475_5133 fill-brand60-1257_33467-paragraph text-text-xlextrabold-423_3198"
                    >
                        {{ "SL" }}
                    </p>
                </slot>
                <slot name="slot_6169_18001">
                    <AvatarVerifiedIcon
                        id="6169_18001"
                        class="Pixso-instance-6169_18001"
                        Size="2xl"
                    />
                </slot>
            </div>
            <div
                id="5472_2713"
                class="Pixso-symbol-5472_2713 fill-brand5-1257_33460"
                v-if="
                    Size === '2xl' &&
                    Type === 'Text' &&
                    Indicator === 'Verified'
                "
            >
                <slot name="slot_5475_5129">
                    <p
                        id="5475_5129"
                        class="Pixso-paragraph-5475_5129 fill-brand60-1257_33467-paragraph text-text-2xlextrabold-423_3195"
                    >
                        {{ "SL" }}
                    </p>
                </slot>
                <slot name="slot_6169_18007">
                    <AvatarVerifiedIcon
                        id="6169_18007"
                        class="Pixso-instance-6169_18007"
                        Size="3xl"
                    />
                </slot>
            </div>
            <div
                id="5472_2325"
                class="Pixso-symbol-5472_2325 fill-avatar1-5468_692"
                v-if="
                    Size === 'xs' &&
                    Type === 'Image' &&
                    Indicator === 'Company Logo'
                "
            >
                <slot name="slot_5472_2349">
                    <AvatarCompanyIcon
                        id="5472_2349"
                        class="Pixso-instance-5472_2349"
                        Size="xs"
                    />
                </slot>
            </div>
            <div
                id="5472_2327"
                class="Pixso-symbol-5472_2327 fill-avatar1-5468_692"
                v-if="
                    Size === 'sm' &&
                    Type === 'Image' &&
                    Indicator === 'Company Logo'
                "
            >
                <slot name="slot_5472_2354">
                    <AvatarCompanyIcon
                        id="5472_2354"
                        class="Pixso-instance-5472_2354"
                        Size="sm"
                    />
                </slot>
            </div>
            <div
                id="5472_2329"
                class="Pixso-symbol-5472_2329 fill-avatar1-5468_692"
                v-if="
                    Size === 'md' &&
                    Type === 'Image' &&
                    Indicator === 'Company Logo'
                "
            >
                <slot name="slot_5472_2359">
                    <AvatarCompanyIcon
                        id="5472_2359"
                        class="Pixso-instance-5472_2359"
                        Size="md"
                    />
                </slot>
            </div>
            <div
                id="5472_2331"
                class="Pixso-symbol-5472_2331 fill-avatar1-5468_692"
                v-if="
                    Size === 'lg' &&
                    Type === 'Image' &&
                    Indicator === 'Company Logo'
                "
            >
                <slot name="slot_5472_2368">
                    <AvatarCompanyIcon
                        id="5472_2368"
                        class="Pixso-instance-5472_2368"
                        Size="lg"
                    />
                </slot>
            </div>
            <div
                id="5472_2333"
                class="Pixso-symbol-5472_2333 fill-avatar1-5468_692"
                v-if="
                    Size === 'xl' &&
                    Type === 'Image' &&
                    Indicator === 'Company Logo'
                "
            >
                <slot name="slot_5472_2377">
                    <AvatarCompanyIcon
                        id="5472_2377"
                        class="Pixso-instance-5472_2377"
                        Size="xl"
                    />
                </slot>
            </div>
            <div
                id="5472_2335"
                class="Pixso-symbol-5472_2335 fill-avatar1-5468_692"
                v-if="
                    Size === '2xl' &&
                    Type === 'Image' &&
                    Indicator === 'Company Logo'
                "
            >
                <slot name="slot_5472_2386">
                    <AvatarCompanyIcon
                        id="5472_2386"
                        class="Pixso-instance-5472_2386"
                        Size="2xl"
                    />
                </slot>
            </div>
            <div
                id="5472_2584"
                class="Pixso-symbol-5472_2584 fill-brand5-1257_33460"
                v-if="
                    Size === 'xs' &&
                    Type === 'Placeholder' &&
                    Indicator === 'Company Logo'
                "
            >
                <slot name="slot_5472_2585">
                    <User
                        id="5472_2585"
                        class="Pixso-instance-5472_2585"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <slot name="slot_5472_2645">
                    <AvatarCompanyIcon
                        id="5472_2645"
                        class="Pixso-instance-5472_2645"
                        Size="xs"
                    />
                </slot>
            </div>
            <div
                id="5472_2587"
                class="Pixso-symbol-5472_2587 fill-brand5-1257_33460"
                v-if="
                    Size === 'sm' &&
                    Type === 'Placeholder' &&
                    Indicator === 'Company Logo'
                "
            >
                <slot name="slot_5472_2588">
                    <User
                        id="5472_2588"
                        class="Pixso-instance-5472_2588"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <slot name="slot_5472_2640">
                    <AvatarCompanyIcon
                        id="5472_2640"
                        class="Pixso-instance-5472_2640"
                        Size="sm"
                    />
                </slot>
            </div>
            <div
                id="5472_2590"
                class="Pixso-symbol-5472_2590 fill-brand5-1257_33460"
                v-if="
                    Size === 'md' &&
                    Type === 'Placeholder' &&
                    Indicator === 'Company Logo'
                "
            >
                <slot name="slot_5472_2591">
                    <User
                        id="5472_2591"
                        class="Pixso-instance-5472_2591"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <slot name="slot_5472_2635">
                    <AvatarCompanyIcon
                        id="5472_2635"
                        class="Pixso-instance-5472_2635"
                        Size="md"
                    />
                </slot>
            </div>
            <div
                id="5472_2593"
                class="Pixso-symbol-5472_2593 fill-brand5-1257_33460"
                v-if="
                    Size === 'lg' &&
                    Type === 'Placeholder' &&
                    Indicator === 'Company Logo'
                "
            >
                <slot name="slot_5472_2594">
                    <User
                        id="5472_2594"
                        class="Pixso-instance-5472_2594"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <slot name="slot_5472_2630">
                    <AvatarCompanyIcon
                        id="5472_2630"
                        class="Pixso-instance-5472_2630"
                        Size="lg"
                    />
                </slot>
            </div>
            <div
                id="5472_2596"
                class="Pixso-symbol-5472_2596 fill-brand5-1257_33460"
                v-if="
                    Size === 'xl' &&
                    Type === 'Placeholder' &&
                    Indicator === 'Company Logo'
                "
            >
                <slot name="slot_5472_2597">
                    <User
                        id="5472_2597"
                        class="Pixso-instance-5472_2597"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <slot name="slot_5472_2625">
                    <AvatarCompanyIcon
                        id="5472_2625"
                        class="Pixso-instance-5472_2625"
                        Size="xl"
                    />
                </slot>
            </div>
            <div
                id="5472_2599"
                class="Pixso-symbol-5472_2599 fill-brand5-1257_33460"
                v-if="
                    Size === '2xl' &&
                    Type === 'Placeholder' &&
                    Indicator === 'Company Logo'
                "
            >
                <slot name="slot_5472_2600">
                    <User
                        id="5472_2600"
                        class="Pixso-instance-5472_2600"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <slot name="slot_5472_2620">
                    <AvatarCompanyIcon
                        id="5472_2620"
                        class="Pixso-instance-5472_2620"
                        Size="2xl"
                    />
                </slot>
            </div>
            <div
                id="5472_2716"
                class="Pixso-symbol-5472_2716 fill-brand5-1257_33460"
                v-if="
                    Size === 'xs' &&
                    Type === 'Text' &&
                    Indicator === 'Company Logo'
                "
            >
                <slot name="slot_5472_2718">
                    <AvatarCompanyIcon
                        id="5472_2718"
                        class="Pixso-instance-5472_2718"
                        Size="xs"
                    />
                </slot>
                <slot name="slot_5475_5150">
                    <p
                        id="5475_5150"
                        class="Pixso-paragraph-5475_5150 fill-brand60-1257_33467-paragraph text-text-xsextrabold-439_9519"
                    >
                        {{ "SL" }}
                    </p>
                </slot>
            </div>
            <div
                id="5472_2719"
                class="Pixso-symbol-5472_2719 fill-brand5-1257_33460"
                v-if="
                    Size === 'sm' &&
                    Type === 'Text' &&
                    Indicator === 'Company Logo'
                "
            >
                <slot name="slot_5472_2721">
                    <AvatarCompanyIcon
                        id="5472_2721"
                        class="Pixso-instance-5472_2721"
                        Size="sm"
                    />
                </slot>
                <slot name="slot_5475_5146">
                    <p
                        id="5475_5146"
                        class="Pixso-paragraph-5475_5146 fill-brand60-1257_33467-paragraph text-text-smextrabold-423_3207"
                    >
                        {{ "SL" }}
                    </p>
                </slot>
            </div>
            <div
                id="5472_2722"
                class="Pixso-symbol-5472_2722 fill-brand5-1257_33460"
                v-if="
                    Size === 'md' &&
                    Type === 'Text' &&
                    Indicator === 'Company Logo'
                "
            >
                <slot name="slot_5472_2724">
                    <AvatarCompanyIcon
                        id="5472_2724"
                        class="Pixso-instance-5472_2724"
                        Size="md"
                    />
                </slot>
                <slot name="slot_5475_5142">
                    <p
                        id="5475_5142"
                        class="Pixso-paragraph-5475_5142 fill-brand60-1257_33467-paragraph text-text-mdextrabold-423_3204"
                    >
                        {{ "SL" }}
                    </p>
                </slot>
            </div>
            <div
                id="5472_2725"
                class="Pixso-symbol-5472_2725 fill-brand5-1257_33460"
                v-if="
                    Size === 'lg' &&
                    Type === 'Text' &&
                    Indicator === 'Company Logo'
                "
            >
                <slot name="slot_5472_2727">
                    <AvatarCompanyIcon
                        id="5472_2727"
                        class="Pixso-instance-5472_2727"
                        Size="lg"
                    />
                </slot>
                <slot name="slot_5475_5138">
                    <p
                        id="5475_5138"
                        class="Pixso-paragraph-5475_5138 fill-brand60-1257_33467-paragraph text-text-lgextrabold-423_3201"
                    >
                        {{ "SL" }}
                    </p>
                </slot>
            </div>
            <div
                id="5472_2728"
                class="Pixso-symbol-5472_2728 fill-brand5-1257_33460"
                v-if="
                    Size === 'xl' &&
                    Type === 'Text' &&
                    Indicator === 'Company Logo'
                "
            >
                <slot name="slot_5472_2730">
                    <AvatarCompanyIcon
                        id="5472_2730"
                        class="Pixso-instance-5472_2730"
                        Size="xl"
                    />
                </slot>
                <slot name="slot_5475_5134">
                    <p
                        id="5475_5134"
                        class="Pixso-paragraph-5475_5134 fill-brand60-1257_33467-paragraph text-text-xlextrabold-423_3198"
                    >
                        {{ "SL" }}
                    </p>
                </slot>
            </div>
            <div
                id="5472_2731"
                class="Pixso-symbol-5472_2731 fill-brand5-1257_33460"
                v-if="
                    Size === '2xl' &&
                    Type === 'Text' &&
                    Indicator === 'Company Logo'
                "
            >
                <slot name="slot_5472_2733">
                    <AvatarCompanyIcon
                        id="5472_2733"
                        class="Pixso-instance-5472_2733"
                        Size="2xl"
                    />
                </slot>
                <slot name="slot_5475_5130">
                    <p
                        id="5475_5130"
                        class="Pixso-paragraph-5475_5130 fill-brand60-1257_33467-paragraph text-text-2xlextrabold-423_3195"
                    >
                        {{ "SL" }}
                    </p>
                </slot>
            </div>
        </div>
    </div>
</template>
<script lang="ts" setup>
import User from "@/components/User.vue";
import AvatarIndicator from "@/components/Avatarindicator.vue";
import AvatarVerifiedIcon from "@/components/Avatarverifiedicon.vue";
import AvatarCompanyIcon from "@/components/Avatarcompanyicon.vue";
const props = defineProps({
    Size: { type: String },
    Type: { type: String },
    Indicator: { type: String }
});
</script>
<style>
.Pixso-symbol-5468_1034 {
}
.Pixso-symbol-5468_1031 {
    width: 24px;
    height: 24px;
    position: relative;
    border-radius: 46.125px 46.125px 46.125px 46.125px;
}
.Pixso-symbol-5468_1032 {
    width: 32px;
    height: 32px;
    position: relative;
    border-radius: 61.5px 61.5px 61.5px 61.5px;
}
.Pixso-symbol-5468_1033 {
    width: 40px;
    height: 40px;
    position: relative;
    border-radius: 76.875px 76.875px 76.875px 76.875px;
}
.Pixso-symbol-5468_1029 {
    width: 48px;
    height: 48px;
    position: relative;
    border-radius: 92.25px 92.25px 92.25px 92.25px;
}
.Pixso-symbol-5468_1030 {
    width: 56px;
    height: 56px;
    position: relative;
    border-radius: 107.625px 107.625px 107.625px 107.625px;
}
.Pixso-symbol-5468_1022 {
    width: 64px;
    height: 64px;
    position: relative;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-symbol-5472_2395 {
    width: 24px;
    height: 24px;
    position: relative;
    border-radius: 46.125px 46.125px 46.125px 46.125px;
}
.Pixso-instance-5472_2424 {
    width: 16px;
    height: 16px;
}
.Pixso-symbol-5472_2396 {
    width: 32px;
    height: 32px;
    position: relative;
    border-radius: 61.5px 61.5px 61.5px 61.5px;
}
.Pixso-instance-5472_2422 {
    width: 20px;
    height: 20px;
}
.Pixso-symbol-5472_2397 {
    width: 40px;
    height: 40px;
    position: relative;
    border-radius: 76.875px 76.875px 76.875px 76.875px;
}
.Pixso-instance-5472_2420 {
    width: 24px;
    height: 24px;
}
.Pixso-symbol-5472_2398 {
    width: 48px;
    height: 48px;
    position: relative;
    border-radius: 92.25px 92.25px 92.25px 92.25px;
}
.Pixso-instance-5472_2418 {
    width: 28.000002px;
    height: 28.000002px;
}
.Pixso-symbol-5472_2399 {
    width: 56px;
    height: 56px;
    position: relative;
    border-radius: 107.625px 107.625px 107.625px 107.625px;
}
.Pixso-instance-5472_2416 {
    width: 32px;
    height: 32px;
}
.Pixso-symbol-5472_2400 {
    width: 64px;
    height: 64px;
    position: relative;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5472_2414 {
    width: 32px;
    height: 32px;
}
.Pixso-symbol-5472_2650 {
    width: 24px;
    height: 24px;
    position: relative;
    border-radius: 46.125px 46.125px 46.125px 46.125px;
}
.Pixso-paragraph-5475_5120 {
    text-align: center;
    width: 24px;
    height: auto;
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translateX(calc(-50% + 0px)) translateY(calc(-50% + 0px));
}
.Pixso-symbol-5472_2652 {
    width: 32px;
    height: 32px;
    position: relative;
    border-radius: 61.5px 61.5px 61.5px 61.5px;
}
.Pixso-paragraph-5475_5119 {
    text-align: center;
    width: 32px;
    height: auto;
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translateX(calc(-50% + 0px)) translateY(calc(-50% + 0px));
}
.Pixso-symbol-5472_2654 {
    width: 40px;
    height: 40px;
    position: relative;
    border-radius: 76.875px 76.875px 76.875px 76.875px;
}
.Pixso-paragraph-5475_5118 {
    text-align: center;
    width: 40px;
    height: auto;
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translateX(calc(-50% + 0px)) translateY(calc(-50% + 0px));
}
.Pixso-symbol-5472_2656 {
    width: 48px;
    height: 48px;
    position: relative;
    border-radius: 92.25px 92.25px 92.25px 92.25px;
}
.Pixso-paragraph-5475_5117 {
    text-align: center;
    width: 48px;
    height: auto;
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translateX(calc(-50% + 0px)) translateY(calc(-50% + -1px));
}
.Pixso-symbol-5472_2658 {
    width: 56px;
    height: 56px;
    position: relative;
    border-radius: 107.625px 107.625px 107.625px 107.625px;
}
.Pixso-paragraph-5475_5116 {
    text-align: center;
    width: 55px;
    height: auto;
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translateX(calc(-50% + 0.5px)) translateY(calc(-50% + -1px));
}
.Pixso-symbol-5472_2660 {
    width: 64px;
    height: 64px;
    position: relative;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-paragraph-5475_5115 {
    text-align: center;
    width: 64px;
    height: auto;
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translateX(calc(-50% + 0px)) translateY(calc(-50% + -1px));
}
.Pixso-symbol-5471_2071 {
    width: 24px;
    height: 24px;
    position: relative;
    border-radius: 46.125px 46.125px 46.125px 46.125px;
}
.Pixso-instance-5471_2232 {
    width: 6px;
    height: 6px;
}
.Pixso-symbol-5471_2072 {
    width: 32px;
    height: 32px;
    position: relative;
    border-radius: 61.5px 61.5px 61.5px 61.5px;
}
.Pixso-instance-5471_2233 {
    width: 8px;
    height: 8px;
}
.Pixso-symbol-5471_2073 {
    width: 40px;
    height: 40px;
    position: relative;
    border-radius: 76.875px 76.875px 76.875px 76.875px;
}
.Pixso-instance-5471_2234 {
    width: 10px;
    height: 10px;
}
.Pixso-symbol-5471_2074 {
    width: 48px;
    height: 48px;
    position: relative;
    border-radius: 92.25px 92.25px 92.25px 92.25px;
}
.Pixso-instance-5471_2235 {
    width: 12px;
    height: 12px;
}
.Pixso-symbol-5471_2075 {
    width: 56px;
    height: 56px;
    position: relative;
    border-radius: 107.625px 107.625px 107.625px 107.625px;
}
.Pixso-instance-5471_2236 {
    width: 14px;
    height: 14px;
}
.Pixso-symbol-5471_2076 {
    width: 64px;
    height: 64px;
    position: relative;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5471_2237 {
    width: 16px;
    height: 16px;
}
.Pixso-symbol-5472_2426 {
    width: 24px;
    height: 24px;
    position: relative;
    border-radius: 46.125px 46.125px 46.125px 46.125px;
}
.Pixso-instance-5472_2427 {
    width: 16px;
    height: 16px;
}
.Pixso-instance-5472_2449 {
    width: 6px;
    height: 6px;
}
.Pixso-symbol-5472_2428 {
    width: 32px;
    height: 32px;
    position: relative;
    border-radius: 61.5px 61.5px 61.5px 61.5px;
}
.Pixso-instance-5472_2429 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5472_2448 {
    width: 8px;
    height: 8px;
}
.Pixso-symbol-5472_2430 {
    width: 40px;
    height: 40px;
    position: relative;
    border-radius: 76.875px 76.875px 76.875px 76.875px;
}
.Pixso-instance-5472_2431 {
    width: 24px;
    height: 24px;
}
.Pixso-instance-5472_2447 {
    width: 10px;
    height: 10px;
}
.Pixso-symbol-5472_2432 {
    width: 48px;
    height: 48px;
    position: relative;
    border-radius: 92.25px 92.25px 92.25px 92.25px;
}
.Pixso-instance-5472_2433 {
    width: 28.000002px;
    height: 28.000002px;
}
.Pixso-instance-5472_2446 {
    width: 12px;
    height: 12px;
}
.Pixso-symbol-5472_2434 {
    width: 56px;
    height: 56px;
    position: relative;
    border-radius: 107.625px 107.625px 107.625px 107.625px;
}
.Pixso-instance-5472_2435 {
    width: 32px;
    height: 32px;
}
.Pixso-instance-5472_2445 {
    width: 14px;
    height: 14px;
}
.Pixso-symbol-5472_2436 {
    width: 64px;
    height: 64px;
    position: relative;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5472_2437 {
    width: 32px;
    height: 32px;
}
.Pixso-instance-5472_2444 {
    width: 16px;
    height: 16px;
}
.Pixso-symbol-5472_2662 {
    width: 24px;
    height: 24px;
    position: relative;
    border-radius: 46.125px 46.125px 46.125px 46.125px;
}
.Pixso-instance-5472_2664 {
    width: 6px;
    height: 6px;
}
.Pixso-paragraph-5475_5147 {
    text-align: center;
    width: 24px;
    height: auto;
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translateX(calc(-50% + 0px)) translateY(calc(-50% + 0px));
}
.Pixso-symbol-5472_2665 {
    width: 32px;
    height: 32px;
    position: relative;
    border-radius: 61.5px 61.5px 61.5px 61.5px;
}
.Pixso-instance-5472_2667 {
    width: 8px;
    height: 8px;
}
.Pixso-paragraph-5475_5143 {
    text-align: center;
    width: 32px;
    height: auto;
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translateX(calc(-50% + 0px)) translateY(calc(-50% + 0px));
}
.Pixso-symbol-5472_2668 {
    width: 40px;
    height: 40px;
    position: relative;
    border-radius: 76.875px 76.875px 76.875px 76.875px;
}
.Pixso-instance-5472_2670 {
    width: 10px;
    height: 10px;
}
.Pixso-paragraph-5475_5139 {
    text-align: center;
    width: 40px;
    height: auto;
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translateX(calc(-50% + 0px)) translateY(calc(-50% + 0px));
}
.Pixso-symbol-5472_2671 {
    width: 48px;
    height: 48px;
    position: relative;
    border-radius: 92.25px 92.25px 92.25px 92.25px;
}
.Pixso-instance-5472_2673 {
    width: 12px;
    height: 12px;
}
.Pixso-paragraph-5475_5135 {
    text-align: center;
    width: 48px;
    height: auto;
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translateX(calc(-50% + 0px)) translateY(calc(-50% + -1px));
}
.Pixso-symbol-5472_2674 {
    width: 56px;
    height: 56px;
    position: relative;
    border-radius: 107.625px 107.625px 107.625px 107.625px;
}
.Pixso-instance-5472_2676 {
    width: 14px;
    height: 14px;
}
.Pixso-paragraph-5475_5131 {
    text-align: center;
    width: 55px;
    height: auto;
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translateX(calc(-50% + 0.5px)) translateY(calc(-50% + -1px));
}
.Pixso-symbol-5472_2677 {
    width: 64px;
    height: 64px;
    position: relative;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5472_2679 {
    width: 16px;
    height: 16px;
}
.Pixso-paragraph-5475_5127 {
    text-align: center;
    width: 64px;
    height: auto;
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translateX(calc(-50% + 0px)) translateY(calc(-50% + -1px));
}
.Pixso-symbol-5471_2243 {
    width: 24px;
    height: 24px;
    position: relative;
    border-radius: 46.125px 46.125px 46.125px 46.125px;
}
.Pixso-instance-5471_2244 {
    width: 6px;
    height: 6px;
}
.Pixso-symbol-5471_2245 {
    width: 32px;
    height: 32px;
    position: relative;
    border-radius: 61.5px 61.5px 61.5px 61.5px;
}
.Pixso-instance-5471_2246 {
    width: 8px;
    height: 8px;
}
.Pixso-symbol-5471_2247 {
    width: 40px;
    height: 40px;
    position: relative;
    border-radius: 76.875px 76.875px 76.875px 76.875px;
}
.Pixso-instance-5471_2248 {
    width: 10px;
    height: 10px;
}
.Pixso-symbol-5471_2249 {
    width: 48px;
    height: 48px;
    position: relative;
    border-radius: 92.25px 92.25px 92.25px 92.25px;
}
.Pixso-instance-5471_2250 {
    width: 12px;
    height: 12px;
}
.Pixso-symbol-5471_2251 {
    width: 56px;
    height: 56px;
    position: relative;
    border-radius: 107.625px 107.625px 107.625px 107.625px;
}
.Pixso-instance-5471_2252 {
    width: 14px;
    height: 14px;
}
.Pixso-symbol-5471_2253 {
    width: 64px;
    height: 64px;
    position: relative;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5471_2254 {
    width: 16px;
    height: 16px;
}
.Pixso-symbol-5472_2456 {
    width: 24px;
    height: 24px;
    position: relative;
    border-radius: 46.125px 46.125px 46.125px 46.125px;
}
.Pixso-instance-5472_2457 {
    width: 16px;
    height: 16px;
}
.Pixso-instance-5472_2458 {
    width: 6px;
    height: 6px;
}
.Pixso-symbol-5472_2459 {
    width: 32px;
    height: 32px;
    position: relative;
    border-radius: 61.5px 61.5px 61.5px 61.5px;
}
.Pixso-instance-5472_2460 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5472_2461 {
    width: 8px;
    height: 8px;
}
.Pixso-symbol-5472_2462 {
    width: 40px;
    height: 40px;
    position: relative;
    border-radius: 76.875px 76.875px 76.875px 76.875px;
}
.Pixso-instance-5472_2463 {
    width: 24px;
    height: 24px;
}
.Pixso-instance-5472_2464 {
    width: 10px;
    height: 10px;
}
.Pixso-symbol-5472_2465 {
    width: 48px;
    height: 48px;
    position: relative;
    border-radius: 92.25px 92.25px 92.25px 92.25px;
}
.Pixso-instance-5472_2466 {
    width: 28.000002px;
    height: 28.000002px;
}
.Pixso-instance-5472_2467 {
    width: 12px;
    height: 12px;
}
.Pixso-symbol-5472_2468 {
    width: 56px;
    height: 56px;
    position: relative;
    border-radius: 107.625px 107.625px 107.625px 107.625px;
}
.Pixso-instance-5472_2469 {
    width: 32px;
    height: 32px;
}
.Pixso-instance-5472_2470 {
    width: 14px;
    height: 14px;
}
.Pixso-symbol-5472_2471 {
    width: 64px;
    height: 64px;
    position: relative;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5472_2472 {
    width: 32px;
    height: 32px;
}
.Pixso-instance-5472_2473 {
    width: 16px;
    height: 16px;
}
.Pixso-symbol-5472_2680 {
    width: 24px;
    height: 24px;
    position: relative;
    border-radius: 46.125px 46.125px 46.125px 46.125px;
}
.Pixso-instance-5472_2682 {
    width: 6px;
    height: 6px;
}
.Pixso-paragraph-5475_5148 {
    text-align: center;
    width: 24px;
    height: auto;
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translateX(calc(-50% + 0px)) translateY(calc(-50% + 0px));
}
.Pixso-symbol-5472_2683 {
    width: 32px;
    height: 32px;
    position: relative;
    border-radius: 61.5px 61.5px 61.5px 61.5px;
}
.Pixso-instance-5472_2685 {
    width: 8px;
    height: 8px;
}
.Pixso-paragraph-5475_5144 {
    text-align: center;
    width: 32px;
    height: auto;
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translateX(calc(-50% + 0px)) translateY(calc(-50% + 0px));
}
.Pixso-symbol-5472_2686 {
    width: 40px;
    height: 40px;
    position: relative;
    border-radius: 76.875px 76.875px 76.875px 76.875px;
}
.Pixso-instance-5472_2688 {
    width: 10px;
    height: 10px;
}
.Pixso-paragraph-5475_5140 {
    text-align: center;
    width: 40px;
    height: auto;
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translateX(calc(-50% + 0px)) translateY(calc(-50% + 0px));
}
.Pixso-symbol-5472_2689 {
    width: 48px;
    height: 48px;
    position: relative;
    border-radius: 92.25px 92.25px 92.25px 92.25px;
}
.Pixso-instance-5472_2691 {
    width: 12px;
    height: 12px;
}
.Pixso-paragraph-5475_5136 {
    text-align: center;
    width: 48px;
    height: auto;
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translateX(calc(-50% + 0px)) translateY(calc(-50% + -1px));
}
.Pixso-symbol-5472_2692 {
    width: 56px;
    height: 56px;
    position: relative;
    border-radius: 107.625px 107.625px 107.625px 107.625px;
}
.Pixso-instance-5472_2694 {
    width: 14px;
    height: 14px;
}
.Pixso-paragraph-5475_5132 {
    text-align: center;
    width: 55px;
    height: auto;
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translateX(calc(-50% + 0.5px)) translateY(calc(-50% + -1px));
}
.Pixso-symbol-5472_2695 {
    width: 64px;
    height: 64px;
    position: relative;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5472_2697 {
    width: 16px;
    height: 16px;
}
.Pixso-paragraph-5475_5128 {
    text-align: center;
    width: 64px;
    height: auto;
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translateX(calc(-50% + 0px)) translateY(calc(-50% + -1px));
}
.Pixso-symbol-5471_2282 {
    width: 24px;
    height: 24px;
    position: relative;
    border-radius: 46.125px 46.125px 46.125px 46.125px;
}
.Pixso-instance-6168_17874 {
    width: 12px;
    height: 12px;
}
.Pixso-symbol-5471_2284 {
    width: 32px;
    height: 32px;
    position: relative;
    border-radius: 61.5px 61.5px 61.5px 61.5px;
}
.Pixso-instance-6168_17869 {
    width: 14px;
    height: 14px;
}
.Pixso-symbol-5471_2286 {
    width: 40px;
    height: 40px;
    position: relative;
    border-radius: 76.875px 76.875px 76.875px 76.875px;
}
.Pixso-instance-6168_17864 {
    width: 16px;
    height: 16px;
}
.Pixso-symbol-5471_2288 {
    width: 48px;
    height: 48px;
    position: relative;
    border-radius: 92.25px 92.25px 92.25px 92.25px;
}
.Pixso-instance-6168_17858 {
    width: 18px;
    height: 18px;
}
.Pixso-symbol-5471_2290 {
    width: 56px;
    height: 56px;
    position: relative;
    border-radius: 107.625px 107.625px 107.625px 107.625px;
}
.Pixso-instance-6168_17852 {
    width: 20px;
    height: 20px;
}
.Pixso-symbol-5471_2292 {
    width: 64px;
    height: 64px;
    position: relative;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-6168_17844 {
    width: 24px;
    height: 24px;
}
.Pixso-symbol-5472_2492 {
    width: 24px;
    height: 24px;
    position: relative;
    border-radius: 46.125px 46.125px 46.125px 46.125px;
}
.Pixso-instance-5472_2493 {
    width: 16px;
    height: 16px;
}
.Pixso-instance-6169_17972 {
    width: 12px;
    height: 12px;
}
.Pixso-symbol-5472_2495 {
    width: 32px;
    height: 32px;
    position: relative;
    border-radius: 61.5px 61.5px 61.5px 61.5px;
}
.Pixso-instance-5472_2496 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-6169_17978 {
    width: 14px;
    height: 14px;
}
.Pixso-symbol-5472_2498 {
    width: 40px;
    height: 40px;
    position: relative;
    border-radius: 76.875px 76.875px 76.875px 76.875px;
}
.Pixso-instance-5472_2499 {
    width: 24px;
    height: 24px;
}
.Pixso-instance-6169_17984 {
    width: 16px;
    height: 16px;
}
.Pixso-symbol-5472_2501 {
    width: 48px;
    height: 48px;
    position: relative;
    border-radius: 92.25px 92.25px 92.25px 92.25px;
}
.Pixso-instance-5472_2502 {
    width: 28.000002px;
    height: 28.000002px;
}
.Pixso-instance-6169_17990 {
    width: 18px;
    height: 18px;
}
.Pixso-symbol-5472_2504 {
    width: 56px;
    height: 56px;
    position: relative;
    border-radius: 107.625px 107.625px 107.625px 107.625px;
}
.Pixso-instance-5472_2505 {
    width: 32px;
    height: 32px;
}
.Pixso-instance-6169_17998 {
    width: 20px;
    height: 20px;
}
.Pixso-symbol-5472_2507 {
    width: 64px;
    height: 64px;
    position: relative;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5472_2508 {
    width: 32px;
    height: 32px;
}
.Pixso-instance-6169_18004 {
    width: 24px;
    height: 24px;
}
.Pixso-symbol-5472_2698 {
    width: 24px;
    height: 24px;
    position: relative;
    border-radius: 46.125px 46.125px 46.125px 46.125px;
}
.Pixso-paragraph-5475_5149 {
    text-align: center;
    width: 24px;
    height: auto;
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translateX(calc(-50% + 0px)) translateY(calc(-50% + 0px));
}
.Pixso-instance-6169_17975 {
    width: 12px;
    height: 12px;
}
.Pixso-symbol-5472_2701 {
    width: 32px;
    height: 32px;
    position: relative;
    border-radius: 61.5px 61.5px 61.5px 61.5px;
}
.Pixso-paragraph-5475_5145 {
    text-align: center;
    width: 32px;
    height: auto;
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translateX(calc(-50% + 0px)) translateY(calc(-50% + 0px));
}
.Pixso-instance-6169_17981 {
    width: 14px;
    height: 14px;
}
.Pixso-symbol-5472_2704 {
    width: 40px;
    height: 40px;
    position: relative;
    border-radius: 76.875px 76.875px 76.875px 76.875px;
}
.Pixso-paragraph-5475_5141 {
    text-align: center;
    width: 40px;
    height: auto;
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translateX(calc(-50% + 0px)) translateY(calc(-50% + 0px));
}
.Pixso-instance-6169_17987 {
    width: 16px;
    height: 16px;
}
.Pixso-symbol-5472_2707 {
    width: 48px;
    height: 48px;
    position: relative;
    border-radius: 92.25px 92.25px 92.25px 92.25px;
}
.Pixso-paragraph-5475_5137 {
    text-align: center;
    width: 48px;
    height: auto;
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translateX(calc(-50% + 0px)) translateY(calc(-50% + -1px));
}
.Pixso-instance-6169_17994 {
    width: 18px;
    height: 18px;
}
.Pixso-symbol-5472_2710 {
    width: 56px;
    height: 56px;
    position: relative;
    border-radius: 107.625px 107.625px 107.625px 107.625px;
}
.Pixso-paragraph-5475_5133 {
    text-align: center;
    width: 55px;
    height: auto;
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translateX(calc(-50% + 0.5px)) translateY(calc(-50% + -1px));
}
.Pixso-instance-6169_18001 {
    width: 20px;
    height: 20px;
}
.Pixso-symbol-5472_2713 {
    width: 64px;
    height: 64px;
    position: relative;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-paragraph-5475_5129 {
    text-align: center;
    width: 64px;
    height: auto;
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translateX(calc(-50% + 0px)) translateY(calc(-50% + -1px));
}
.Pixso-instance-6169_18007 {
    width: 24px;
    height: 24px;
}
.Pixso-symbol-5472_2325 {
    width: 24px;
    height: 24px;
    position: relative;
    border-radius: 46.125px 46.125px 46.125px 46.125px;
}
.Pixso-instance-5472_2349 {
    width: 10px;
    height: 10px;
}
.Pixso-symbol-5472_2327 {
    width: 32px;
    height: 32px;
    position: relative;
    border-radius: 61.5px 61.5px 61.5px 61.5px;
}
.Pixso-instance-5472_2354 {
    width: 12px;
    height: 12px;
}
.Pixso-symbol-5472_2329 {
    width: 40px;
    height: 40px;
    position: relative;
    border-radius: 76.875px 76.875px 76.875px 76.875px;
}
.Pixso-instance-5472_2359 {
    width: 14px;
    height: 14px;
}
.Pixso-symbol-5472_2331 {
    width: 48px;
    height: 48px;
    position: relative;
    border-radius: 92.25px 92.25px 92.25px 92.25px;
}
.Pixso-instance-5472_2368 {
    width: 16px;
    height: 16px;
}
.Pixso-symbol-5472_2333 {
    width: 56px;
    height: 56px;
    position: relative;
    border-radius: 107.625px 107.625px 107.625px 107.625px;
}
.Pixso-instance-5472_2377 {
    width: 18px;
    height: 18px;
}
.Pixso-symbol-5472_2335 {
    width: 64px;
    height: 64px;
    position: relative;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5472_2386 {
    width: 20px;
    height: 20px;
}
.Pixso-symbol-5472_2584 {
    width: 24px;
    height: 24px;
    position: relative;
    border-radius: 46.125px 46.125px 46.125px 46.125px;
}
.Pixso-instance-5472_2585 {
    width: 16px;
    height: 16px;
}
.Pixso-instance-5472_2645 {
    width: 10px;
    height: 10px;
}
.Pixso-symbol-5472_2587 {
    width: 32px;
    height: 32px;
    position: relative;
    border-radius: 61.5px 61.5px 61.5px 61.5px;
}
.Pixso-instance-5472_2588 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5472_2640 {
    width: 12px;
    height: 12px;
}
.Pixso-symbol-5472_2590 {
    width: 40px;
    height: 40px;
    position: relative;
    border-radius: 76.875px 76.875px 76.875px 76.875px;
}
.Pixso-instance-5472_2591 {
    width: 24px;
    height: 24px;
}
.Pixso-instance-5472_2635 {
    width: 14px;
    height: 14px;
}
.Pixso-symbol-5472_2593 {
    width: 48px;
    height: 48px;
    position: relative;
    border-radius: 92.25px 92.25px 92.25px 92.25px;
}
.Pixso-instance-5472_2594 {
    width: 28.000002px;
    height: 28.000002px;
}
.Pixso-instance-5472_2630 {
    width: 16px;
    height: 16px;
}
.Pixso-symbol-5472_2596 {
    width: 56px;
    height: 56px;
    position: relative;
    border-radius: 107.625px 107.625px 107.625px 107.625px;
}
.Pixso-instance-5472_2597 {
    width: 32px;
    height: 32px;
}
.Pixso-instance-5472_2625 {
    width: 18px;
    height: 18px;
}
.Pixso-symbol-5472_2599 {
    width: 64px;
    height: 64px;
    position: relative;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5472_2600 {
    width: 32px;
    height: 32px;
}
.Pixso-instance-5472_2620 {
    width: 20px;
    height: 20px;
}
.Pixso-symbol-5472_2716 {
    width: 24px;
    height: 24px;
    position: relative;
    border-radius: 46.125px 46.125px 46.125px 46.125px;
}
.Pixso-instance-5472_2718 {
    width: 10px;
    height: 10px;
}
.Pixso-paragraph-5475_5150 {
    text-align: center;
    width: 24px;
    height: auto;
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translateX(calc(-50% + 0px)) translateY(calc(-50% + 0px));
}
.Pixso-symbol-5472_2719 {
    width: 32px;
    height: 32px;
    position: relative;
    border-radius: 61.5px 61.5px 61.5px 61.5px;
}
.Pixso-instance-5472_2721 {
    width: 12px;
    height: 12px;
}
.Pixso-paragraph-5475_5146 {
    text-align: center;
    width: 32px;
    height: auto;
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translateX(calc(-50% + 0px)) translateY(calc(-50% + 0px));
}
.Pixso-symbol-5472_2722 {
    width: 40px;
    height: 40px;
    position: relative;
    border-radius: 76.875px 76.875px 76.875px 76.875px;
}
.Pixso-instance-5472_2724 {
    width: 14px;
    height: 14px;
}
.Pixso-paragraph-5475_5142 {
    text-align: center;
    width: 40px;
    height: auto;
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translateX(calc(-50% + 0px)) translateY(calc(-50% + 0px));
}
.Pixso-symbol-5472_2725 {
    width: 48px;
    height: 48px;
    position: relative;
    border-radius: 92.25px 92.25px 92.25px 92.25px;
}
.Pixso-instance-5472_2727 {
    width: 16px;
    height: 16px;
}
.Pixso-paragraph-5475_5138 {
    text-align: center;
    width: 48px;
    height: auto;
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translateX(calc(-50% + 0px)) translateY(calc(-50% + -1px));
}
.Pixso-symbol-5472_2728 {
    width: 56px;
    height: 56px;
    position: relative;
    border-radius: 107.625px 107.625px 107.625px 107.625px;
}
.Pixso-instance-5472_2730 {
    width: 18px;
    height: 18px;
}
.Pixso-paragraph-5475_5134 {
    text-align: center;
    width: 55px;
    height: auto;
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translateX(calc(-50% + 0.5px)) translateY(calc(-50% + -1px));
}
.Pixso-symbol-5472_2731 {
    width: 64px;
    height: 64px;
    position: relative;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5472_2733 {
    width: 20px;
    height: 20px;
}
.Pixso-paragraph-5475_5130 {
    text-align: center;
    width: 64px;
    height: auto;
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translateX(calc(-50% + 0px)) translateY(calc(-50% + -1px));
}

.Pixso-instance-5472_2424 .Pixso-symbol-5579_152455 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 4px;
    top: 4px;
    background-color: transparent;
}
.Pixso-instance-5472_2424 .Pixso-vector-5579_152456 {
    width: 84.37%;
    height: 81.39%;
    position: absolute;
    left: 7.74%;
    right: 7.89%;
    top: 7.8%;
    bottom: 10.81%;
}
.Pixso-instance-5472_2422 .Pixso-symbol-5579_152455 {
    width: 20px;
    height: 20px;
    position: absolute;
    left: 6px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5472_2422 .Pixso-vector-5579_152456 {
    width: 84.37%;
    height: 81.39%;
    position: absolute;
    left: 7.74%;
    right: 7.89%;
    top: 7.8%;
    bottom: 10.81%;
}
.Pixso-instance-5472_2420 .Pixso-symbol-5579_152455 {
    width: 24px;
    height: 24px;
    position: absolute;
    left: 8px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5472_2420 .Pixso-vector-5579_152456 {
    width: 84.37%;
    height: 81.39%;
    position: absolute;
    left: 7.74%;
    right: 7.89%;
    top: 7.8%;
    bottom: 10.81%;
}
.Pixso-instance-5472_2418 .Pixso-symbol-5579_152455 {
    width: 28.000002px;
    height: 28.000002px;
    position: absolute;
    left: 10px;
    top: 10px;
    background-color: transparent;
}
.Pixso-instance-5472_2418 .Pixso-vector-5579_152456 {
    width: 84.37%;
    height: 81.39%;
    position: absolute;
    left: 7.74%;
    right: 7.89%;
    top: 7.8%;
    bottom: 10.81%;
}
.Pixso-instance-5472_2416 .Pixso-symbol-5579_152455 {
    width: 32px;
    height: 32px;
    position: absolute;
    left: 12px;
    top: 12px;
    background-color: transparent;
}
.Pixso-instance-5472_2416 .Pixso-vector-5579_152456 {
    width: 84.37%;
    height: 81.39%;
    position: absolute;
    left: 7.74%;
    right: 7.89%;
    top: 7.8%;
    bottom: 10.81%;
}
.Pixso-instance-5472_2414 .Pixso-symbol-5579_152455 {
    width: 32px;
    height: 32px;
    position: absolute;
    left: 16px;
    top: 16px;
    background-color: transparent;
}
.Pixso-instance-5472_2414 .Pixso-vector-5579_152456 {
    width: 84.37%;
    height: 81.39%;
    position: absolute;
    left: 7.74%;
    right: 7.89%;
    top: 7.8%;
    bottom: 10.81%;
}
.Pixso-instance-5471_2232 .Pixso-symbol-5464_43227 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5471_2232 .stroke-wrapper-5464_43227 {
    width: 6px;
    height: 6px;
}
.Pixso-instance-5471_2232 .stroke-5464_43227 {
    inset: -1.5px -1.5px -1.5px -1.5px;
    border-radius: 124.5px 124.5px 124.5px 124.5px;
    pointer-events: none;
    border-width: 1.5px 1.5px 1.5px 1.5px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5471_2233 .Pixso-symbol-5464_43229 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5471_2233 .stroke-wrapper-5464_43229 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5471_2233 .stroke-5464_43229 {
    inset: -1.5px -1.5px -1.5px -1.5px;
    border-radius: 124.5px 124.5px 124.5px 124.5px;
    pointer-events: none;
    border-width: 1.5px 1.5px 1.5px 1.5px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5471_2234 .Pixso-symbol-5464_43231 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5471_2234 .stroke-wrapper-5464_43231 {
    width: 10px;
    height: 10px;
}
.Pixso-instance-5471_2234 .stroke-5464_43231 {
    inset: -1.5px -1.5px -1.5px -1.5px;
    border-radius: 124.5px 124.5px 124.5px 124.5px;
    pointer-events: none;
    border-width: 1.5px 1.5px 1.5px 1.5px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5471_2235 .Pixso-symbol-5464_43233 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5471_2235 .stroke-wrapper-5464_43233 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5471_2235 .stroke-5464_43233 {
    inset: -1.5px -1.5px -1.5px -1.5px;
    border-radius: 124.5px 124.5px 124.5px 124.5px;
    pointer-events: none;
    border-width: 1.5px 1.5px 1.5px 1.5px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5471_2236 .Pixso-symbol-5464_43236 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5471_2236 .stroke-wrapper-5464_43236 {
    width: 14px;
    height: 14px;
}
.Pixso-instance-5471_2236 .stroke-5464_43236 {
    inset: -1.5px -1.5px -1.5px -1.5px;
    border-radius: 124.5px 124.5px 124.5px 124.5px;
    pointer-events: none;
    border-width: 1.5px 1.5px 1.5px 1.5px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5471_2237 .Pixso-symbol-5464_43237 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5471_2237 .stroke-wrapper-5464_43237 {
    width: 16px;
    height: 16px;
}
.Pixso-instance-5471_2237 .stroke-5464_43237 {
    inset: -1.5px -1.5px -1.5px -1.5px;
    border-radius: 124.5px 124.5px 124.5px 124.5px;
    pointer-events: none;
    border-width: 1.5px 1.5px 1.5px 1.5px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5472_2427 .Pixso-symbol-5579_152455 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 4px;
    top: 4px;
    background-color: transparent;
}
.Pixso-instance-5472_2427 .Pixso-vector-5579_152456 {
    width: 84.37%;
    height: 81.39%;
    position: absolute;
    left: 7.74%;
    right: 7.89%;
    top: 7.8%;
    bottom: 10.81%;
}
.Pixso-instance-5472_2449 .Pixso-symbol-5464_43227 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5472_2449 .stroke-wrapper-5464_43227 {
    width: 6px;
    height: 6px;
}
.Pixso-instance-5472_2449 .stroke-5464_43227 {
    inset: -1.5px -1.5px -1.5px -1.5px;
    border-radius: 124.5px 124.5px 124.5px 124.5px;
    pointer-events: none;
    border-width: 1.5px 1.5px 1.5px 1.5px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5472_2429 .Pixso-symbol-5579_152455 {
    width: 20px;
    height: 20px;
    position: absolute;
    left: 6px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5472_2429 .Pixso-vector-5579_152456 {
    width: 84.37%;
    height: 81.39%;
    position: absolute;
    left: 7.74%;
    right: 7.89%;
    top: 7.8%;
    bottom: 10.81%;
}
.Pixso-instance-5472_2448 .Pixso-symbol-5464_43229 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5472_2448 .stroke-wrapper-5464_43229 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5472_2448 .stroke-5464_43229 {
    inset: -1.5px -1.5px -1.5px -1.5px;
    border-radius: 124.5px 124.5px 124.5px 124.5px;
    pointer-events: none;
    border-width: 1.5px 1.5px 1.5px 1.5px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5472_2431 .Pixso-symbol-5579_152455 {
    width: 24px;
    height: 24px;
    position: absolute;
    left: 8px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5472_2431 .Pixso-vector-5579_152456 {
    width: 84.37%;
    height: 81.39%;
    position: absolute;
    left: 7.74%;
    right: 7.89%;
    top: 7.8%;
    bottom: 10.81%;
}
.Pixso-instance-5472_2447 .Pixso-symbol-5464_43231 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5472_2447 .stroke-wrapper-5464_43231 {
    width: 10px;
    height: 10px;
}
.Pixso-instance-5472_2447 .stroke-5464_43231 {
    inset: -1.5px -1.5px -1.5px -1.5px;
    border-radius: 124.5px 124.5px 124.5px 124.5px;
    pointer-events: none;
    border-width: 1.5px 1.5px 1.5px 1.5px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5472_2433 .Pixso-symbol-5579_152455 {
    width: 28.000002px;
    height: 28.000002px;
    position: absolute;
    left: 10px;
    top: 10px;
    background-color: transparent;
}
.Pixso-instance-5472_2433 .Pixso-vector-5579_152456 {
    width: 84.37%;
    height: 81.39%;
    position: absolute;
    left: 7.74%;
    right: 7.89%;
    top: 7.8%;
    bottom: 10.81%;
}
.Pixso-instance-5472_2446 .Pixso-symbol-5464_43233 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5472_2446 .stroke-wrapper-5464_43233 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5472_2446 .stroke-5464_43233 {
    inset: -1.5px -1.5px -1.5px -1.5px;
    border-radius: 124.5px 124.5px 124.5px 124.5px;
    pointer-events: none;
    border-width: 1.5px 1.5px 1.5px 1.5px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5472_2435 .Pixso-symbol-5579_152455 {
    width: 32px;
    height: 32px;
    position: absolute;
    left: 12px;
    top: 12px;
    background-color: transparent;
}
.Pixso-instance-5472_2435 .Pixso-vector-5579_152456 {
    width: 84.37%;
    height: 81.39%;
    position: absolute;
    left: 7.74%;
    right: 7.89%;
    top: 7.8%;
    bottom: 10.81%;
}
.Pixso-instance-5472_2445 .Pixso-symbol-5464_43236 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5472_2445 .stroke-wrapper-5464_43236 {
    width: 14px;
    height: 14px;
}
.Pixso-instance-5472_2445 .stroke-5464_43236 {
    inset: -1.5px -1.5px -1.5px -1.5px;
    border-radius: 124.5px 124.5px 124.5px 124.5px;
    pointer-events: none;
    border-width: 1.5px 1.5px 1.5px 1.5px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5472_2437 .Pixso-symbol-5579_152455 {
    width: 32px;
    height: 32px;
    position: absolute;
    left: 16px;
    top: 16px;
    background-color: transparent;
}
.Pixso-instance-5472_2437 .Pixso-vector-5579_152456 {
    width: 84.37%;
    height: 81.39%;
    position: absolute;
    left: 7.74%;
    right: 7.89%;
    top: 7.8%;
    bottom: 10.81%;
}
.Pixso-instance-5472_2444 .Pixso-symbol-5464_43237 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5472_2444 .stroke-wrapper-5464_43237 {
    width: 16px;
    height: 16px;
}
.Pixso-instance-5472_2444 .stroke-5464_43237 {
    inset: -1.5px -1.5px -1.5px -1.5px;
    border-radius: 124.5px 124.5px 124.5px 124.5px;
    pointer-events: none;
    border-width: 1.5px 1.5px 1.5px 1.5px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5472_2664 .Pixso-symbol-5464_43227 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5472_2664 .stroke-wrapper-5464_43227 {
    width: 6px;
    height: 6px;
}
.Pixso-instance-5472_2664 .stroke-5464_43227 {
    inset: -1.5px -1.5px -1.5px -1.5px;
    border-radius: 124.5px 124.5px 124.5px 124.5px;
    pointer-events: none;
    border-width: 1.5px 1.5px 1.5px 1.5px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5472_2667 .Pixso-symbol-5464_43229 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5472_2667 .stroke-wrapper-5464_43229 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5472_2667 .stroke-5464_43229 {
    inset: -1.5px -1.5px -1.5px -1.5px;
    border-radius: 124.5px 124.5px 124.5px 124.5px;
    pointer-events: none;
    border-width: 1.5px 1.5px 1.5px 1.5px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5472_2670 .Pixso-symbol-5464_43231 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5472_2670 .stroke-wrapper-5464_43231 {
    width: 10px;
    height: 10px;
}
.Pixso-instance-5472_2670 .stroke-5464_43231 {
    inset: -1.5px -1.5px -1.5px -1.5px;
    border-radius: 124.5px 124.5px 124.5px 124.5px;
    pointer-events: none;
    border-width: 1.5px 1.5px 1.5px 1.5px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5472_2673 .Pixso-symbol-5464_43233 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5472_2673 .stroke-wrapper-5464_43233 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5472_2673 .stroke-5464_43233 {
    inset: -1.5px -1.5px -1.5px -1.5px;
    border-radius: 124.5px 124.5px 124.5px 124.5px;
    pointer-events: none;
    border-width: 1.5px 1.5px 1.5px 1.5px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5472_2676 .Pixso-symbol-5464_43236 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5472_2676 .stroke-wrapper-5464_43236 {
    width: 14px;
    height: 14px;
}
.Pixso-instance-5472_2676 .stroke-5464_43236 {
    inset: -1.5px -1.5px -1.5px -1.5px;
    border-radius: 124.5px 124.5px 124.5px 124.5px;
    pointer-events: none;
    border-width: 1.5px 1.5px 1.5px 1.5px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5472_2679 .Pixso-symbol-5464_43237 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5472_2679 .stroke-wrapper-5464_43237 {
    width: 16px;
    height: 16px;
}
.Pixso-instance-5472_2679 .stroke-5464_43237 {
    inset: -1.5px -1.5px -1.5px -1.5px;
    border-radius: 124.5px 124.5px 124.5px 124.5px;
    pointer-events: none;
    border-width: 1.5px 1.5px 1.5px 1.5px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5471_2244 .Pixso-symbol-5468_1146 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5471_2244 .stroke-wrapper-5468_1146 {
    width: 6px;
    height: 6px;
}
.Pixso-instance-5471_2244 .stroke-5468_1146 {
    inset: -1.5px -1.5px -1.5px -1.5px;
    border-radius: 124.5px 124.5px 124.5px 124.5px;
    pointer-events: none;
    border-width: 1.5px 1.5px 1.5px 1.5px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5471_2246 .Pixso-symbol-5468_1148 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5471_2246 .stroke-wrapper-5468_1148 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5471_2246 .stroke-5468_1148 {
    inset: -1.5px -1.5px -1.5px -1.5px;
    border-radius: 124.5px 124.5px 124.5px 124.5px;
    pointer-events: none;
    border-width: 1.5px 1.5px 1.5px 1.5px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5471_2248 .Pixso-symbol-5468_1150 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5471_2248 .stroke-wrapper-5468_1150 {
    width: 10px;
    height: 10px;
}
.Pixso-instance-5471_2248 .stroke-5468_1150 {
    inset: -1.5px -1.5px -1.5px -1.5px;
    border-radius: 124.5px 124.5px 124.5px 124.5px;
    pointer-events: none;
    border-width: 1.5px 1.5px 1.5px 1.5px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5471_2250 .Pixso-symbol-5468_1152 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5471_2250 .stroke-wrapper-5468_1152 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5471_2250 .stroke-5468_1152 {
    inset: -1.5px -1.5px -1.5px -1.5px;
    border-radius: 124.5px 124.5px 124.5px 124.5px;
    pointer-events: none;
    border-width: 1.5px 1.5px 1.5px 1.5px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5471_2252 .Pixso-symbol-5468_1154 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5471_2252 .stroke-wrapper-5468_1154 {
    width: 14px;
    height: 14px;
}
.Pixso-instance-5471_2252 .stroke-5468_1154 {
    inset: -1.5px -1.5px -1.5px -1.5px;
    border-radius: 124.5px 124.5px 124.5px 124.5px;
    pointer-events: none;
    border-width: 1.5px 1.5px 1.5px 1.5px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5471_2254 .Pixso-symbol-5468_1156 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5471_2254 .stroke-wrapper-5468_1156 {
    width: 16px;
    height: 16px;
}
.Pixso-instance-5471_2254 .stroke-5468_1156 {
    inset: -1.5px -1.5px -1.5px -1.5px;
    border-radius: 124.5px 124.5px 124.5px 124.5px;
    pointer-events: none;
    border-width: 1.5px 1.5px 1.5px 1.5px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5472_2457 .Pixso-symbol-5579_152455 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 4px;
    top: 4px;
    background-color: transparent;
}
.Pixso-instance-5472_2457 .Pixso-vector-5579_152456 {
    width: 84.37%;
    height: 81.39%;
    position: absolute;
    left: 7.74%;
    right: 7.89%;
    top: 7.8%;
    bottom: 10.81%;
}
.Pixso-instance-5472_2458 .Pixso-symbol-5468_1146 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5472_2458 .stroke-wrapper-5468_1146 {
    width: 6px;
    height: 6px;
}
.Pixso-instance-5472_2458 .stroke-5468_1146 {
    inset: -1.5px -1.5px -1.5px -1.5px;
    border-radius: 124.5px 124.5px 124.5px 124.5px;
    pointer-events: none;
    border-width: 1.5px 1.5px 1.5px 1.5px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5472_2460 .Pixso-symbol-5579_152455 {
    width: 20px;
    height: 20px;
    position: absolute;
    left: 6px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5472_2460 .Pixso-vector-5579_152456 {
    width: 84.37%;
    height: 81.39%;
    position: absolute;
    left: 7.74%;
    right: 7.89%;
    top: 7.8%;
    bottom: 10.81%;
}
.Pixso-instance-5472_2461 .Pixso-symbol-5468_1148 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5472_2461 .stroke-wrapper-5468_1148 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5472_2461 .stroke-5468_1148 {
    inset: -1.5px -1.5px -1.5px -1.5px;
    border-radius: 124.5px 124.5px 124.5px 124.5px;
    pointer-events: none;
    border-width: 1.5px 1.5px 1.5px 1.5px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5472_2463 .Pixso-symbol-5579_152455 {
    width: 24px;
    height: 24px;
    position: absolute;
    left: 8px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5472_2463 .Pixso-vector-5579_152456 {
    width: 84.37%;
    height: 81.39%;
    position: absolute;
    left: 7.74%;
    right: 7.89%;
    top: 7.8%;
    bottom: 10.81%;
}
.Pixso-instance-5472_2464 .Pixso-symbol-5468_1150 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5472_2464 .stroke-wrapper-5468_1150 {
    width: 10px;
    height: 10px;
}
.Pixso-instance-5472_2464 .stroke-5468_1150 {
    inset: -1.5px -1.5px -1.5px -1.5px;
    border-radius: 124.5px 124.5px 124.5px 124.5px;
    pointer-events: none;
    border-width: 1.5px 1.5px 1.5px 1.5px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5472_2466 .Pixso-symbol-5579_152455 {
    width: 28.000002px;
    height: 28.000002px;
    position: absolute;
    left: 10px;
    top: 10px;
    background-color: transparent;
}
.Pixso-instance-5472_2466 .Pixso-vector-5579_152456 {
    width: 84.37%;
    height: 81.39%;
    position: absolute;
    left: 7.74%;
    right: 7.89%;
    top: 7.8%;
    bottom: 10.81%;
}
.Pixso-instance-5472_2467 .Pixso-symbol-5468_1152 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5472_2467 .stroke-wrapper-5468_1152 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5472_2467 .stroke-5468_1152 {
    inset: -1.5px -1.5px -1.5px -1.5px;
    border-radius: 124.5px 124.5px 124.5px 124.5px;
    pointer-events: none;
    border-width: 1.5px 1.5px 1.5px 1.5px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5472_2469 .Pixso-symbol-5579_152455 {
    width: 32px;
    height: 32px;
    position: absolute;
    left: 12px;
    top: 12px;
    background-color: transparent;
}
.Pixso-instance-5472_2469 .Pixso-vector-5579_152456 {
    width: 84.37%;
    height: 81.39%;
    position: absolute;
    left: 7.74%;
    right: 7.89%;
    top: 7.8%;
    bottom: 10.81%;
}
.Pixso-instance-5472_2470 .Pixso-symbol-5468_1154 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5472_2470 .stroke-wrapper-5468_1154 {
    width: 14px;
    height: 14px;
}
.Pixso-instance-5472_2470 .stroke-5468_1154 {
    inset: -1.5px -1.5px -1.5px -1.5px;
    border-radius: 124.5px 124.5px 124.5px 124.5px;
    pointer-events: none;
    border-width: 1.5px 1.5px 1.5px 1.5px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5472_2472 .Pixso-symbol-5579_152455 {
    width: 32px;
    height: 32px;
    position: absolute;
    left: 16px;
    top: 16px;
    background-color: transparent;
}
.Pixso-instance-5472_2472 .Pixso-vector-5579_152456 {
    width: 84.37%;
    height: 81.39%;
    position: absolute;
    left: 7.74%;
    right: 7.89%;
    top: 7.8%;
    bottom: 10.81%;
}
.Pixso-instance-5472_2473 .Pixso-symbol-5468_1156 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5472_2473 .stroke-wrapper-5468_1156 {
    width: 16px;
    height: 16px;
}
.Pixso-instance-5472_2473 .stroke-5468_1156 {
    inset: -1.5px -1.5px -1.5px -1.5px;
    border-radius: 124.5px 124.5px 124.5px 124.5px;
    pointer-events: none;
    border-width: 1.5px 1.5px 1.5px 1.5px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5472_2682 .Pixso-symbol-5468_1146 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5472_2682 .stroke-wrapper-5468_1146 {
    width: 6px;
    height: 6px;
}
.Pixso-instance-5472_2682 .stroke-5468_1146 {
    inset: -1.5px -1.5px -1.5px -1.5px;
    border-radius: 124.5px 124.5px 124.5px 124.5px;
    pointer-events: none;
    border-width: 1.5px 1.5px 1.5px 1.5px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5472_2685 .Pixso-symbol-5468_1148 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5472_2685 .stroke-wrapper-5468_1148 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5472_2685 .stroke-5468_1148 {
    inset: -1.5px -1.5px -1.5px -1.5px;
    border-radius: 124.5px 124.5px 124.5px 124.5px;
    pointer-events: none;
    border-width: 1.5px 1.5px 1.5px 1.5px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5472_2688 .Pixso-symbol-5468_1150 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5472_2688 .stroke-wrapper-5468_1150 {
    width: 10px;
    height: 10px;
}
.Pixso-instance-5472_2688 .stroke-5468_1150 {
    inset: -1.5px -1.5px -1.5px -1.5px;
    border-radius: 124.5px 124.5px 124.5px 124.5px;
    pointer-events: none;
    border-width: 1.5px 1.5px 1.5px 1.5px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5472_2691 .Pixso-symbol-5468_1152 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5472_2691 .stroke-wrapper-5468_1152 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5472_2691 .stroke-5468_1152 {
    inset: -1.5px -1.5px -1.5px -1.5px;
    border-radius: 124.5px 124.5px 124.5px 124.5px;
    pointer-events: none;
    border-width: 1.5px 1.5px 1.5px 1.5px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5472_2694 .Pixso-symbol-5468_1154 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5472_2694 .stroke-wrapper-5468_1154 {
    width: 14px;
    height: 14px;
}
.Pixso-instance-5472_2694 .stroke-5468_1154 {
    inset: -1.5px -1.5px -1.5px -1.5px;
    border-radius: 124.5px 124.5px 124.5px 124.5px;
    pointer-events: none;
    border-width: 1.5px 1.5px 1.5px 1.5px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5472_2697 .Pixso-symbol-5468_1156 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5472_2697 .stroke-wrapper-5468_1156 {
    width: 16px;
    height: 16px;
}
.Pixso-instance-5472_2697 .stroke-5468_1156 {
    inset: -1.5px -1.5px -1.5px -1.5px;
    border-radius: 124.5px 124.5px 124.5px 124.5px;
    pointer-events: none;
    border-width: 1.5px 1.5px 1.5px 1.5px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5472_2493 .Pixso-symbol-5579_152455 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 4px;
    top: 4px;
    background-color: transparent;
}
.Pixso-instance-5472_2493 .Pixso-vector-5579_152456 {
    width: 84.37%;
    height: 81.39%;
    position: absolute;
    left: 7.74%;
    right: 7.89%;
    top: 7.8%;
    bottom: 10.81%;
}
.Pixso-instance-5472_2496 .Pixso-symbol-5579_152455 {
    width: 20px;
    height: 20px;
    position: absolute;
    left: 6px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5472_2496 .Pixso-vector-5579_152456 {
    width: 84.37%;
    height: 81.39%;
    position: absolute;
    left: 7.74%;
    right: 7.89%;
    top: 7.8%;
    bottom: 10.81%;
}
.Pixso-instance-5472_2499 .Pixso-symbol-5579_152455 {
    width: 24px;
    height: 24px;
    position: absolute;
    left: 8px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5472_2499 .Pixso-vector-5579_152456 {
    width: 84.37%;
    height: 81.39%;
    position: absolute;
    left: 7.74%;
    right: 7.89%;
    top: 7.8%;
    bottom: 10.81%;
}
.Pixso-instance-5472_2502 .Pixso-symbol-5579_152455 {
    width: 28.000002px;
    height: 28.000002px;
    position: absolute;
    left: 10px;
    top: 10px;
    background-color: transparent;
}
.Pixso-instance-5472_2502 .Pixso-vector-5579_152456 {
    width: 84.37%;
    height: 81.39%;
    position: absolute;
    left: 7.74%;
    right: 7.89%;
    top: 7.8%;
    bottom: 10.81%;
}
.Pixso-instance-5472_2505 .Pixso-symbol-5579_152455 {
    width: 32px;
    height: 32px;
    position: absolute;
    left: 12px;
    top: 12px;
    background-color: transparent;
}
.Pixso-instance-5472_2505 .Pixso-vector-5579_152456 {
    width: 84.37%;
    height: 81.39%;
    position: absolute;
    left: 7.74%;
    right: 7.89%;
    top: 7.8%;
    bottom: 10.81%;
}
.Pixso-instance-5472_2508 .Pixso-symbol-5579_152455 {
    width: 32px;
    height: 32px;
    position: absolute;
    left: 16px;
    top: 16px;
    background-color: transparent;
}
.Pixso-instance-5472_2508 .Pixso-vector-5579_152456 {
    width: 84.37%;
    height: 81.39%;
    position: absolute;
    left: 7.74%;
    right: 7.89%;
    top: 7.8%;
    bottom: 10.81%;
}
.Pixso-instance-5472_2349 .Pixso-symbol-5464_43239 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    border-radius: 12px 12px 12px 12px;
}
.Pixso-instance-5472_2349 .stroke-wrapper-5464_43239 {
    width: 10px;
    height: 10px;
    display: flex;
}
.Pixso-instance-5472_2349 .stroke-5464_43239 {
    inset: -1.5px -1.5px -1.5px -1.5px;
    border-radius: 13.5px 13.5px 13.5px 13.5px;
    pointer-events: none;
    border-width: 1.5px 1.5px 1.5px 1.5px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5472_2354 .Pixso-symbol-5464_43240 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    border-radius: 12px 12px 12px 12px;
}
.Pixso-instance-5472_2354 .stroke-wrapper-5464_43240 {
    width: 12px;
    height: 12px;
    display: flex;
}
.Pixso-instance-5472_2354 .stroke-5464_43240 {
    inset: -1.5px -1.5px -1.5px -1.5px;
    border-radius: 13.5px 13.5px 13.5px 13.5px;
    pointer-events: none;
    border-width: 1.5px 1.5px 1.5px 1.5px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5472_2359 .Pixso-symbol-5464_43241 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    border-radius: 12px 12px 12px 12px;
}
.Pixso-instance-5472_2359 .stroke-wrapper-5464_43241 {
    width: 14px;
    height: 14px;
    display: flex;
}
.Pixso-instance-5472_2359 .stroke-5464_43241 {
    inset: -1.5px -1.5px -1.5px -1.5px;
    border-radius: 13.5px 13.5px 13.5px 13.5px;
    pointer-events: none;
    border-width: 1.5px 1.5px 1.5px 1.5px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5472_2368 .Pixso-symbol-5464_43242 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    border-radius: 12px 12px 12px 12px;
}
.Pixso-instance-5472_2368 .stroke-wrapper-5464_43242 {
    width: 16px;
    height: 16px;
    display: flex;
}
.Pixso-instance-5472_2368 .stroke-5464_43242 {
    inset: -1.5px -1.5px -1.5px -1.5px;
    border-radius: 13.5px 13.5px 13.5px 13.5px;
    pointer-events: none;
    border-width: 1.5px 1.5px 1.5px 1.5px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5472_2377 .Pixso-symbol-5464_43243 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    border-radius: 12px 12px 12px 12px;
}
.Pixso-instance-5472_2377 .stroke-wrapper-5464_43243 {
    width: 18px;
    height: 18px;
    display: flex;
}
.Pixso-instance-5472_2377 .stroke-5464_43243 {
    inset: -1.5px -1.5px -1.5px -1.5px;
    border-radius: 13.5px 13.5px 13.5px 13.5px;
    pointer-events: none;
    border-width: 1.5px 1.5px 1.5px 1.5px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5472_2386 .Pixso-symbol-5464_43244 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5472_2386 .stroke-wrapper-5464_43244 {
    width: 20px;
    height: 20px;
    display: flex;
}
.Pixso-instance-5472_2386 .stroke-5464_43244 {
    inset: -1.666667px -1.666667px -1.666667px -1.666667px;
    border-radius: 1235.666667px 1235.666667px 1235.666667px 1235.666667px;
    pointer-events: none;
    border-width: 1.666667px 1.666667px 1.666667px 1.666667px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5472_2585 .Pixso-symbol-5579_152455 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 4px;
    top: 4px;
    background-color: transparent;
}
.Pixso-instance-5472_2585 .Pixso-vector-5579_152456 {
    width: 84.37%;
    height: 81.39%;
    position: absolute;
    left: 7.74%;
    right: 7.89%;
    top: 7.8%;
    bottom: 10.81%;
}
.Pixso-instance-5472_2645 .Pixso-symbol-5464_43239 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    border-radius: 12px 12px 12px 12px;
}
.Pixso-instance-5472_2645 .stroke-wrapper-5464_43239 {
    width: 10px;
    height: 10px;
    display: flex;
}
.Pixso-instance-5472_2645 .stroke-5464_43239 {
    inset: -1.5px -1.5px -1.5px -1.5px;
    border-radius: 13.5px 13.5px 13.5px 13.5px;
    pointer-events: none;
    border-width: 1.5px 1.5px 1.5px 1.5px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5472_2588 .Pixso-symbol-5579_152455 {
    width: 20px;
    height: 20px;
    position: absolute;
    left: 6px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5472_2588 .Pixso-vector-5579_152456 {
    width: 84.37%;
    height: 81.39%;
    position: absolute;
    left: 7.74%;
    right: 7.89%;
    top: 7.8%;
    bottom: 10.81%;
}
.Pixso-instance-5472_2640 .Pixso-symbol-5464_43240 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    border-radius: 12px 12px 12px 12px;
}
.Pixso-instance-5472_2640 .stroke-wrapper-5464_43240 {
    width: 12px;
    height: 12px;
    display: flex;
}
.Pixso-instance-5472_2640 .stroke-5464_43240 {
    inset: -1.5px -1.5px -1.5px -1.5px;
    border-radius: 13.5px 13.5px 13.5px 13.5px;
    pointer-events: none;
    border-width: 1.5px 1.5px 1.5px 1.5px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5472_2591 .Pixso-symbol-5579_152455 {
    width: 24px;
    height: 24px;
    position: absolute;
    left: 8px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5472_2591 .Pixso-vector-5579_152456 {
    width: 84.37%;
    height: 81.39%;
    position: absolute;
    left: 7.74%;
    right: 7.89%;
    top: 7.8%;
    bottom: 10.81%;
}
.Pixso-instance-5472_2635 .Pixso-symbol-5464_43241 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    border-radius: 12px 12px 12px 12px;
}
.Pixso-instance-5472_2635 .stroke-wrapper-5464_43241 {
    width: 14px;
    height: 14px;
    display: flex;
}
.Pixso-instance-5472_2635 .stroke-5464_43241 {
    inset: -1.5px -1.5px -1.5px -1.5px;
    border-radius: 13.5px 13.5px 13.5px 13.5px;
    pointer-events: none;
    border-width: 1.5px 1.5px 1.5px 1.5px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5472_2594 .Pixso-symbol-5579_152455 {
    width: 28.000002px;
    height: 28.000002px;
    position: absolute;
    left: 10px;
    top: 10px;
    background-color: transparent;
}
.Pixso-instance-5472_2594 .Pixso-vector-5579_152456 {
    width: 84.37%;
    height: 81.39%;
    position: absolute;
    left: 7.74%;
    right: 7.89%;
    top: 7.8%;
    bottom: 10.81%;
}
.Pixso-instance-5472_2630 .Pixso-symbol-5464_43242 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    border-radius: 12px 12px 12px 12px;
}
.Pixso-instance-5472_2630 .stroke-wrapper-5464_43242 {
    width: 16px;
    height: 16px;
    display: flex;
}
.Pixso-instance-5472_2630 .stroke-5464_43242 {
    inset: -1.5px -1.5px -1.5px -1.5px;
    border-radius: 13.5px 13.5px 13.5px 13.5px;
    pointer-events: none;
    border-width: 1.5px 1.5px 1.5px 1.5px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5472_2597 .Pixso-symbol-5579_152455 {
    width: 32px;
    height: 32px;
    position: absolute;
    left: 12px;
    top: 12px;
    background-color: transparent;
}
.Pixso-instance-5472_2597 .Pixso-vector-5579_152456 {
    width: 84.37%;
    height: 81.39%;
    position: absolute;
    left: 7.74%;
    right: 7.89%;
    top: 7.8%;
    bottom: 10.81%;
}
.Pixso-instance-5472_2625 .Pixso-symbol-5464_43243 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    border-radius: 12px 12px 12px 12px;
}
.Pixso-instance-5472_2625 .stroke-wrapper-5464_43243 {
    width: 18px;
    height: 18px;
    display: flex;
}
.Pixso-instance-5472_2625 .stroke-5464_43243 {
    inset: -1.5px -1.5px -1.5px -1.5px;
    border-radius: 13.5px 13.5px 13.5px 13.5px;
    pointer-events: none;
    border-width: 1.5px 1.5px 1.5px 1.5px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5472_2600 .Pixso-symbol-5579_152455 {
    width: 32px;
    height: 32px;
    position: absolute;
    left: 16px;
    top: 16px;
    background-color: transparent;
}
.Pixso-instance-5472_2600 .Pixso-vector-5579_152456 {
    width: 84.37%;
    height: 81.39%;
    position: absolute;
    left: 7.74%;
    right: 7.89%;
    top: 7.8%;
    bottom: 10.81%;
}
.Pixso-instance-5472_2620 .Pixso-symbol-5464_43244 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5472_2620 .stroke-wrapper-5464_43244 {
    width: 20px;
    height: 20px;
    display: flex;
}
.Pixso-instance-5472_2620 .stroke-5464_43244 {
    inset: -1.666667px -1.666667px -1.666667px -1.666667px;
    border-radius: 1235.666667px 1235.666667px 1235.666667px 1235.666667px;
    pointer-events: none;
    border-width: 1.666667px 1.666667px 1.666667px 1.666667px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5472_2718 .Pixso-symbol-5464_43239 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    border-radius: 12px 12px 12px 12px;
}
.Pixso-instance-5472_2718 .stroke-wrapper-5464_43239 {
    width: 10px;
    height: 10px;
    display: flex;
}
.Pixso-instance-5472_2718 .stroke-5464_43239 {
    inset: -1.5px -1.5px -1.5px -1.5px;
    border-radius: 13.5px 13.5px 13.5px 13.5px;
    pointer-events: none;
    border-width: 1.5px 1.5px 1.5px 1.5px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5472_2721 .Pixso-symbol-5464_43240 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    border-radius: 12px 12px 12px 12px;
}
.Pixso-instance-5472_2721 .stroke-wrapper-5464_43240 {
    width: 12px;
    height: 12px;
    display: flex;
}
.Pixso-instance-5472_2721 .stroke-5464_43240 {
    inset: -1.5px -1.5px -1.5px -1.5px;
    border-radius: 13.5px 13.5px 13.5px 13.5px;
    pointer-events: none;
    border-width: 1.5px 1.5px 1.5px 1.5px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5472_2724 .Pixso-symbol-5464_43241 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    border-radius: 12px 12px 12px 12px;
}
.Pixso-instance-5472_2724 .stroke-wrapper-5464_43241 {
    width: 14px;
    height: 14px;
    display: flex;
}
.Pixso-instance-5472_2724 .stroke-5464_43241 {
    inset: -1.5px -1.5px -1.5px -1.5px;
    border-radius: 13.5px 13.5px 13.5px 13.5px;
    pointer-events: none;
    border-width: 1.5px 1.5px 1.5px 1.5px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5472_2727 .Pixso-symbol-5464_43242 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    border-radius: 12px 12px 12px 12px;
}
.Pixso-instance-5472_2727 .stroke-wrapper-5464_43242 {
    width: 16px;
    height: 16px;
    display: flex;
}
.Pixso-instance-5472_2727 .stroke-5464_43242 {
    inset: -1.5px -1.5px -1.5px -1.5px;
    border-radius: 13.5px 13.5px 13.5px 13.5px;
    pointer-events: none;
    border-width: 1.5px 1.5px 1.5px 1.5px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5472_2730 .Pixso-symbol-5464_43243 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    border-radius: 12px 12px 12px 12px;
}
.Pixso-instance-5472_2730 .stroke-wrapper-5464_43243 {
    width: 18px;
    height: 18px;
    display: flex;
}
.Pixso-instance-5472_2730 .stroke-5464_43243 {
    inset: -1.5px -1.5px -1.5px -1.5px;
    border-radius: 13.5px 13.5px 13.5px 13.5px;
    pointer-events: none;
    border-width: 1.5px 1.5px 1.5px 1.5px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5472_2733 .Pixso-symbol-5464_43244 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5472_2733 .stroke-wrapper-5464_43244 {
    width: 20px;
    height: 20px;
    display: flex;
}
.Pixso-instance-5472_2733 .stroke-5464_43244 {
    inset: -1.666667px -1.666667px -1.666667px -1.666667px;
    border-radius: 1235.666667px 1235.666667px 1235.666667px 1235.666667px;
    pointer-events: none;
    border-width: 1.666667px 1.666667px 1.666667px 1.666667px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-6168_17874 .Pixso-symbol-6168_17829 {
    width: 12px;
    height: 12px;
    overflow: hidden;
    position: absolute;
    left: 14px;
    top: 14px;
    background-color: transparent;
}
.Pixso-instance-6169_17972 .Pixso-symbol-6168_17829 {
    width: 12px;
    height: 12px;
    overflow: hidden;
    position: absolute;
    left: 14px;
    top: 14px;
    background-color: transparent;
}
.Pixso-instance-6169_17975 .Pixso-symbol-6168_17829 {
    width: 12px;
    height: 12px;
    overflow: hidden;
    position: absolute;
    left: 14px;
    top: 14px;
    background-color: transparent;
}
.Pixso-instance-6168_17869 .Pixso-symbol-6168_17841 {
    width: 14px;
    height: 14px;
    overflow: hidden;
    position: absolute;
    left: 20px;
    top: 20px;
    background-color: transparent;
}
.Pixso-instance-6169_17978 .Pixso-symbol-6168_17841 {
    width: 14px;
    height: 14px;
    overflow: hidden;
    position: absolute;
    left: 20px;
    top: 20px;
    background-color: transparent;
}
.Pixso-instance-6169_17981 .Pixso-symbol-6168_17841 {
    width: 14px;
    height: 14px;
    overflow: hidden;
    position: absolute;
    left: 20px;
    top: 20px;
    background-color: transparent;
}
.Pixso-instance-6168_17864 .Pixso-symbol-6168_17820 {
    width: 16px;
    height: 16px;
    overflow: hidden;
    position: absolute;
    left: 26px;
    top: 26px;
    background-color: transparent;
}
.Pixso-instance-6169_17984 .Pixso-symbol-6168_17820 {
    width: 16px;
    height: 16px;
    overflow: hidden;
    position: absolute;
    left: 26px;
    top: 26px;
    background-color: transparent;
}
.Pixso-instance-6169_17987 .Pixso-symbol-6168_17820 {
    width: 16px;
    height: 16px;
    overflow: hidden;
    position: absolute;
    left: 26px;
    top: 26px;
    background-color: transparent;
}
.Pixso-instance-6168_17858 .Pixso-symbol-6168_17808 {
    width: 18px;
    height: 18px;
    overflow: hidden;
    position: absolute;
    left: 32px;
    top: 32px;
    background-color: transparent;
}
.Pixso-instance-6169_17990 .Pixso-symbol-6168_17808 {
    width: 18px;
    height: 18px;
    overflow: hidden;
    position: absolute;
    left: 32px;
    top: 32px;
    background-color: transparent;
}
.Pixso-instance-6169_17994 .Pixso-symbol-6168_17808 {
    width: 18px;
    height: 18px;
    overflow: hidden;
    position: absolute;
    left: 32px;
    top: 32px;
    background-color: transparent;
}
.Pixso-instance-6168_17852 .Pixso-symbol-6168_17800 {
    width: 20px;
    height: 20px;
    overflow: hidden;
    position: absolute;
    left: 38px;
    top: 38px;
    background-color: transparent;
}
.Pixso-instance-6169_17998 .Pixso-symbol-6168_17800 {
    width: 20px;
    height: 20px;
    overflow: hidden;
    position: absolute;
    left: 38px;
    top: 38px;
    background-color: transparent;
}
.Pixso-instance-6169_18001 .Pixso-symbol-6168_17800 {
    width: 20px;
    height: 20px;
    overflow: hidden;
    position: absolute;
    left: 38px;
    top: 38px;
    background-color: transparent;
}
.Pixso-instance-6168_17844 .Pixso-symbol-6168_17792 {
    width: 24px;
    height: 24px;
    overflow: hidden;
    position: absolute;
    left: 43px;
    top: 43px;
    background-color: transparent;
}
.Pixso-instance-6169_18004 .Pixso-symbol-6168_17792 {
    width: 24px;
    height: 24px;
    overflow: hidden;
    position: absolute;
    left: 43px;
    top: 43px;
    background-color: transparent;
}
.Pixso-instance-6169_18007 .Pixso-symbol-6168_17792 {
    width: 24px;
    height: 24px;
    overflow: hidden;
    position: absolute;
    left: 43px;
    top: 43px;
    background-color: transparent;
}
</style>
