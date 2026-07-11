<template>
    <div class="component-5489_8967">
        <div id="5489_8967" class="Pixso-symbol-5489_8967">
            <div
                id="5588_11190"
                class="Pixso-symbol-5588_11190 fill-brand60-1257_33467"
                v-if="
                    Size === 'lg' &&
                    Color === 'Brand' &&
                    Hierarchy === 'Primary' &&
                    State === 'Default'
                "
            >
                <slot name="slot_5588_11191" v-if="visible_5586_123">
                    <Circle
                        id="5588_11191"
                        class="Pixso-instance-5588_11191"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <div id="5588_11216" class="Pixso-frame-5588_11216">
                    <slot name="slot_5588_11192" v-if="visible_5586_119">
                        <Dot
                            id="5588_11192"
                            class="Pixso-instance-5588_11192"
                            Size="sm"
                        />
                    </slot>
                    <slot name="slot_5588_11193">
                        <p
                            id="5588_11193"
                            class="Pixso-paragraph-5588_11193 fill-gray0-white-67_3285-paragraph text-text-smsemibold-423_3209"
                        >
                            {{ text_5588_129 ?? "Label" }}
                        </p>
                    </slot>
                </div>
                <slot name="slot_5588_11194" v-if="visible_5586_121">
                    <Check
                        id="5588_11194"
                        class="Pixso-instance-5588_11194"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
            </div>
            <div
                id="5588_13000"
                class="Pixso-symbol-5588_13000 fill-brand70-1257_33468"
                v-if="
                    Size === 'lg' &&
                    Color === 'Brand' &&
                    Hierarchy === 'Primary' &&
                    State === 'Hover'
                "
            >
                <slot name="slot_5588_13001" v-if="visible_5586_123">
                    <Circle
                        id="5588_13001"
                        class="Pixso-instance-5588_13001"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <div id="5588_13002" class="Pixso-frame-5588_13002">
                    <slot name="slot_5588_13003" v-if="visible_5586_119">
                        <Dot
                            id="5588_13003"
                            class="Pixso-instance-5588_13003"
                            Size="sm"
                        />
                    </slot>
                    <slot name="slot_5588_13004">
                        <p
                            id="5588_13004"
                            class="Pixso-paragraph-5588_13004 fill-gray0-white-67_3285-paragraph text-text-smsemibold-423_3209"
                        >
                            {{ text_5588_129 ?? "Label" }}
                        </p>
                    </slot>
                </div>
                <slot name="slot_5588_13005" v-if="visible_5586_121">
                    <Check
                        id="5588_13005"
                        class="Pixso-instance-5588_13005"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
            </div>
            <div
                id="5588_13819"
                class="Pixso-symbol-5588_13819 fill-brand20-1257_33462"
                v-if="
                    Size === 'lg' &&
                    Color === 'Brand' &&
                    Hierarchy === 'Primary' &&
                    State === 'Disabled'
                "
            >
                <slot name="slot_5588_13820" v-if="visible_5586_123">
                    <Circle
                        id="5588_13820"
                        class="Pixso-instance-5588_13820"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <div id="5588_13821" class="Pixso-frame-5588_13821">
                    <slot name="slot_5588_13822" v-if="visible_5586_119">
                        <Dot
                            id="5588_13822"
                            class="Pixso-instance-5588_13822"
                            Size="sm"
                        />
                    </slot>
                    <slot name="slot_5588_13823">
                        <p
                            id="5588_13823"
                            class="Pixso-paragraph-5588_13823 fill-brand40-1257_33464-paragraph text-text-smsemibold-423_3209"
                        >
                            {{ text_5588_129 ?? "Label" }}
                        </p>
                    </slot>
                </div>
                <slot name="slot_5588_13824" v-if="visible_5586_121">
                    <Check
                        id="5588_13824"
                        class="Pixso-instance-5588_13824"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
            </div>
            <div
                id="5588_13006"
                class="Pixso-symbol-5588_13006 fill-brand10-1257_33461"
                v-if="
                    Size === 'lg' &&
                    Color === 'Brand' &&
                    Hierarchy === 'Secondary' &&
                    State === 'Hover'
                "
            >
                <slot name="slot_5588_13007" v-if="visible_5586_123">
                    <Circle
                        id="5588_13007"
                        class="Pixso-instance-5588_13007"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <div id="5588_13008" class="Pixso-frame-5588_13008">
                    <slot name="slot_5588_13009" v-if="visible_5586_119">
                        <Dot
                            id="5588_13009"
                            class="Pixso-instance-5588_13009"
                            Size="sm"
                        />
                    </slot>
                    <slot name="slot_5588_13010">
                        <p
                            id="5588_13010"
                            class="Pixso-paragraph-5588_13010 fill-brand60-1257_33467-paragraph text-text-smsemibold-423_3209"
                        >
                            {{ text_5588_129 ?? "Label" }}
                        </p>
                    </slot>
                </div>
                <slot name="slot_5588_13011" v-if="visible_5586_121">
                    <Check
                        id="5588_13011"
                        class="Pixso-instance-5588_13011"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
            </div>
            <div
                id="5588_11346"
                class="Pixso-symbol-5588_11346 fill-brand5-1257_33460"
                v-if="
                    Size === 'lg' &&
                    Color === 'Brand' &&
                    Hierarchy === 'Secondary' &&
                    State === 'Default'
                "
            >
                <slot name="slot_5588_11347" v-if="visible_5586_123">
                    <Circle
                        id="5588_11347"
                        class="Pixso-instance-5588_11347"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <div id="5588_11348" class="Pixso-frame-5588_11348">
                    <slot name="slot_5588_11349" v-if="visible_5586_119">
                        <Dot
                            id="5588_11349"
                            class="Pixso-instance-5588_11349"
                            Size="sm"
                        />
                    </slot>
                    <slot name="slot_5588_11350">
                        <p
                            id="5588_11350"
                            class="Pixso-paragraph-5588_11350 fill-brand60-1257_33467-paragraph text-text-smsemibold-423_3209"
                        >
                            {{ text_5588_129 ?? "Label" }}
                        </p>
                    </slot>
                </div>
                <slot name="slot_5588_11351" v-if="visible_5586_121">
                    <Check
                        id="5588_11351"
                        class="Pixso-instance-5588_11351"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
            </div>
            <div
                id="5588_13012"
                class="stroke-wrapper-5588_13012"
                v-if="
                    Size === 'lg' &&
                    Color === 'Brand' &&
                    Hierarchy === 'Outlined' &&
                    State === 'Hover'
                "
            >
                <div class="Pixso-symbol-5588_13012 fill-brand5-1257_33460">
                    <slot name="slot_5588_13013" v-if="visible_5586_123">
                        <Circle
                            id="5588_13013"
                            class="Pixso-instance-5588_13013"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                    <div id="5588_13014" class="Pixso-frame-5588_13014">
                        <slot name="slot_5588_13015" v-if="visible_5586_119">
                            <Dot
                                id="5588_13015"
                                class="Pixso-instance-5588_13015"
                                Size="sm"
                            />
                        </slot>
                        <slot name="slot_5588_13016">
                            <p
                                id="5588_13016"
                                class="Pixso-paragraph-5588_13016 fill-brand60-1257_33467-paragraph text-text-smsemibold-423_3209"
                            >
                                {{ text_5588_129 ?? "Label" }}
                            </p>
                        </slot>
                    </div>
                    <slot name="slot_5588_13017" v-if="visible_5586_121">
                        <Check
                            id="5588_13017"
                            class="Pixso-instance-5588_13017"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div class="stroke-5588_13012 stroke-brand60-1257_33467"></div>
            </div>
            <div
                id="5588_13825"
                class="Pixso-symbol-5588_13825 fill-brand5-1257_33460"
                v-if="
                    Size === 'lg' &&
                    Color === 'Brand' &&
                    Hierarchy === 'Secondary' &&
                    State === 'Disabled'
                "
            >
                <slot name="slot_5588_13826" v-if="visible_5586_123">
                    <Circle
                        id="5588_13826"
                        class="Pixso-instance-5588_13826"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <div id="5588_13827" class="Pixso-frame-5588_13827">
                    <slot name="slot_5588_13828" v-if="visible_5586_119">
                        <Dot
                            id="5588_13828"
                            class="Pixso-instance-5588_13828"
                            Size="sm"
                        />
                    </slot>
                    <slot name="slot_5588_13829">
                        <p
                            id="5588_13829"
                            class="Pixso-paragraph-5588_13829 fill-brand30-1257_33463-paragraph text-text-smsemibold-423_3209"
                        >
                            {{ text_5588_129 ?? "Label" }}
                        </p>
                    </slot>
                </div>
                <slot name="slot_5588_13830" v-if="visible_5586_121">
                    <Check
                        id="5588_13830"
                        class="Pixso-instance-5588_13830"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
            </div>
            <div
                id="5588_13018"
                class="Pixso-symbol-5588_13018 fill-destructive60-438_3719"
                v-if="
                    Size === 'lg' &&
                    Color === 'Destructive' &&
                    Hierarchy === 'Primary' &&
                    State === 'Hover'
                "
            >
                <slot name="slot_5588_13019" v-if="visible_5586_123">
                    <Circle
                        id="5588_13019"
                        class="Pixso-instance-5588_13019"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <div id="5588_13020" class="Pixso-frame-5588_13020">
                    <slot name="slot_5588_13021" v-if="visible_5586_119">
                        <Dot
                            id="5588_13021"
                            class="Pixso-instance-5588_13021"
                            Size="sm"
                        />
                    </slot>
                    <slot name="slot_5588_13022">
                        <p
                            id="5588_13022"
                            class="Pixso-paragraph-5588_13022 fill-gray0-white-67_3285-paragraph text-text-smsemibold-423_3209"
                        >
                            {{ text_5588_129 ?? "Label" }}
                        </p>
                    </slot>
                </div>
                <slot name="slot_5588_13023" v-if="visible_5586_121">
                    <Check
                        id="5588_13023"
                        class="Pixso-instance-5588_13023"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
            </div>
            <div
                id="5588_11409"
                class="stroke-wrapper-5588_11409"
                v-if="
                    Size === 'lg' &&
                    Color === 'Brand' &&
                    Hierarchy === 'Outlined' &&
                    State === 'Default'
                "
            >
                <div class="Pixso-symbol-5588_11409">
                    <slot name="slot_5588_11410" v-if="visible_5586_123">
                        <Circle
                            id="5588_11410"
                            class="Pixso-instance-5588_11410"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                    <div id="5588_11411" class="Pixso-frame-5588_11411">
                        <slot name="slot_5588_11412" v-if="visible_5586_119">
                            <Dot
                                id="5588_11412"
                                class="Pixso-instance-5588_11412"
                                Size="sm"
                            />
                        </slot>
                        <slot name="slot_5588_11413">
                            <p
                                id="5588_11413"
                                class="Pixso-paragraph-5588_11413 fill-brand60-1257_33467-paragraph text-text-smsemibold-423_3209"
                            >
                                {{ text_5588_129 ?? "Label" }}
                            </p>
                        </slot>
                    </div>
                    <slot name="slot_5588_11414" v-if="visible_5586_121">
                        <Check
                            id="5588_11414"
                            class="Pixso-instance-5588_11414"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div class="stroke-5588_11409 stroke-brand60-1257_33467"></div>
            </div>
            <div
                id="5588_13024"
                class="Pixso-symbol-5588_13024 fill-warning60-438_3718"
                v-if="
                    Size === 'lg' &&
                    Color === 'Warning' &&
                    Hierarchy === 'Primary' &&
                    State === 'Hover'
                "
            >
                <slot name="slot_5588_13025" v-if="visible_5586_123">
                    <Circle
                        id="5588_13025"
                        class="Pixso-instance-5588_13025"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <div id="5588_13026" class="Pixso-frame-5588_13026">
                    <slot name="slot_5588_13027" v-if="visible_5586_119">
                        <Dot
                            id="5588_13027"
                            class="Pixso-instance-5588_13027"
                            Size="sm"
                        />
                    </slot>
                    <slot name="slot_5588_13028">
                        <p
                            id="5588_13028"
                            class="Pixso-paragraph-5588_13028 fill-gray0-white-67_3285-paragraph text-text-smsemibold-423_3209"
                        >
                            {{ text_5588_129 ?? "Label" }}
                        </p>
                    </slot>
                </div>
                <slot name="slot_5588_13029" v-if="visible_5586_121">
                    <Check
                        id="5588_13029"
                        class="Pixso-instance-5588_13029"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
            </div>
            <div
                id="5588_13831"
                class="stroke-wrapper-5588_13831"
                v-if="
                    Size === 'lg' &&
                    Color === 'Brand' &&
                    Hierarchy === 'Outlined' &&
                    State === 'Disabled'
                "
            >
                <div class="Pixso-symbol-5588_13831">
                    <slot name="slot_5588_13832" v-if="visible_5586_123">
                        <Circle
                            id="5588_13832"
                            class="Pixso-instance-5588_13832"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                    <div id="5588_13833" class="Pixso-frame-5588_13833">
                        <slot name="slot_5588_13834" v-if="visible_5586_119">
                            <Dot
                                id="5588_13834"
                                class="Pixso-instance-5588_13834"
                                Size="sm"
                            />
                        </slot>
                        <slot name="slot_5588_13835">
                            <p
                                id="5588_13835"
                                class="Pixso-paragraph-5588_13835 fill-brand30-1257_33463-paragraph text-text-smsemibold-423_3209"
                            >
                                {{ text_5588_129 ?? "Label" }}
                            </p>
                        </slot>
                    </div>
                    <slot name="slot_5588_13836" v-if="visible_5586_121">
                        <Check
                            id="5588_13836"
                            class="Pixso-instance-5588_13836"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div class="stroke-5588_13831 stroke-brand30-1257_33463"></div>
            </div>
            <div
                id="5588_13030"
                class="Pixso-symbol-5588_13030 fill-success60-1636_81206"
                v-if="
                    Size === 'lg' &&
                    Color === 'Success' &&
                    Hierarchy === 'Primary' &&
                    State === 'Hover'
                "
            >
                <slot name="slot_5588_13031" v-if="visible_5586_123">
                    <Circle
                        id="5588_13031"
                        class="Pixso-instance-5588_13031"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <div id="5588_13032" class="Pixso-frame-5588_13032">
                    <slot name="slot_5588_13033" v-if="visible_5586_119">
                        <Dot
                            id="5588_13033"
                            class="Pixso-instance-5588_13033"
                            Size="sm"
                        />
                    </slot>
                    <slot name="slot_5588_13034">
                        <p
                            id="5588_13034"
                            class="Pixso-paragraph-5588_13034 fill-gray0-white-67_3285-paragraph text-text-smsemibold-423_3209"
                        >
                            {{ text_5588_129 ?? "Label" }}
                        </p>
                    </slot>
                </div>
                <slot name="slot_5588_13035" v-if="visible_5586_121">
                    <Check
                        id="5588_13035"
                        class="Pixso-instance-5588_13035"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
            </div>
            <div
                id="5588_11841"
                class="Pixso-symbol-5588_11841 fill-destructive50-423_3219"
                v-if="
                    Size === 'lg' &&
                    Color === 'Destructive' &&
                    Hierarchy === 'Primary' &&
                    State === 'Default'
                "
            >
                <slot name="slot_5588_11842" v-if="visible_5586_123">
                    <Circle
                        id="5588_11842"
                        class="Pixso-instance-5588_11842"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <div id="5588_11843" class="Pixso-frame-5588_11843">
                    <slot name="slot_5588_11844" v-if="visible_5586_119">
                        <Dot
                            id="5588_11844"
                            class="Pixso-instance-5588_11844"
                            Size="sm"
                        />
                    </slot>
                    <slot name="slot_5588_11845">
                        <p
                            id="5588_11845"
                            class="Pixso-paragraph-5588_11845 fill-gray0-white-67_3285-paragraph text-text-smsemibold-423_3209"
                        >
                            {{ text_5588_129 ?? "Label" }}
                        </p>
                    </slot>
                </div>
                <slot name="slot_5588_11846" v-if="visible_5586_121">
                    <Check
                        id="5588_11846"
                        class="Pixso-instance-5588_11846"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
            </div>
            <div
                id="5588_13036"
                class="Pixso-symbol-5588_13036 fill-destructive10-423_3221"
                v-if="
                    Size === 'lg' &&
                    Color === 'Destructive' &&
                    Hierarchy === 'Secondary' &&
                    State === 'Hover'
                "
            >
                <slot name="slot_5588_13037" v-if="visible_5586_123">
                    <Circle
                        id="5588_13037"
                        class="Pixso-instance-5588_13037"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <div id="5588_13038" class="Pixso-frame-5588_13038">
                    <slot name="slot_5588_13039" v-if="visible_5586_119">
                        <Dot
                            id="5588_13039"
                            class="Pixso-instance-5588_13039"
                            Size="sm"
                        />
                    </slot>
                    <slot name="slot_5588_13040">
                        <p
                            id="5588_13040"
                            class="Pixso-paragraph-5588_13040 fill-destructive50-423_3219-paragraph text-text-smsemibold-423_3209"
                        >
                            {{ text_5588_129 ?? "Label" }}
                        </p>
                    </slot>
                </div>
                <slot name="slot_5588_13041" v-if="visible_5586_121">
                    <Check
                        id="5588_13041"
                        class="Pixso-instance-5588_13041"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
            </div>
            <div
                id="5588_13837"
                class="Pixso-symbol-5588_13837 fill-destructive20-438_3720"
                v-if="
                    Size === 'lg' &&
                    Color === 'Destructive' &&
                    Hierarchy === 'Primary' &&
                    State === 'Disabled'
                "
            >
                <slot name="slot_5588_13838" v-if="visible_5586_123">
                    <Circle
                        id="5588_13838"
                        class="Pixso-instance-5588_13838"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <div id="5588_13839" class="Pixso-frame-5588_13839">
                    <slot name="slot_5588_13840" v-if="visible_5586_119">
                        <Dot
                            id="5588_13840"
                            class="Pixso-instance-5588_13840"
                            Size="sm"
                        />
                    </slot>
                    <slot name="slot_5588_13841">
                        <p
                            id="5588_13841"
                            class="Pixso-paragraph-5588_13841 fill-destructive40-32_4110-paragraph text-text-smsemibold-423_3209"
                        >
                            {{ text_5588_129 ?? "Label" }}
                        </p>
                    </slot>
                </div>
                <slot name="slot_5588_13842" v-if="visible_5586_121">
                    <Check
                        id="5588_13842"
                        class="Pixso-instance-5588_13842"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
            </div>
            <div
                id="5588_13042"
                class="Pixso-symbol-5588_13042 fill-warning10-423_3215"
                v-if="
                    Size === 'lg' &&
                    Color === 'Warning' &&
                    Hierarchy === 'Secondary' &&
                    State === 'Hover'
                "
            >
                <slot name="slot_5588_13043" v-if="visible_5586_123">
                    <Circle
                        id="5588_13043"
                        class="Pixso-instance-5588_13043"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <div id="5588_13044" class="Pixso-frame-5588_13044">
                    <slot name="slot_5588_13045" v-if="visible_5586_119">
                        <Dot
                            id="5588_13045"
                            class="Pixso-instance-5588_13045"
                            Size="sm"
                        />
                    </slot>
                    <slot name="slot_5588_13046">
                        <p
                            id="5588_13046"
                            class="Pixso-paragraph-5588_13046 fill-warning50-423_3213-paragraph text-text-smsemibold-423_3209"
                        >
                            {{ text_5588_129 ?? "Label" }}
                        </p>
                    </slot>
                </div>
                <slot name="slot_5588_13047" v-if="visible_5586_121">
                    <Check
                        id="5588_13047"
                        class="Pixso-instance-5588_13047"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
            </div>
            <div
                id="5588_12012"
                class="Pixso-symbol-5588_12012 fill-warning50-423_3213"
                v-if="
                    Size === 'lg' &&
                    Color === 'Warning' &&
                    Hierarchy === 'Primary' &&
                    State === 'Default'
                "
            >
                <slot name="slot_5588_12013" v-if="visible_5586_123">
                    <Circle
                        id="5588_12013"
                        class="Pixso-instance-5588_12013"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <div id="5588_12014" class="Pixso-frame-5588_12014">
                    <slot name="slot_5588_12015" v-if="visible_5586_119">
                        <Dot
                            id="5588_12015"
                            class="Pixso-instance-5588_12015"
                            Size="sm"
                        />
                    </slot>
                    <slot name="slot_5588_12016">
                        <p
                            id="5588_12016"
                            class="Pixso-paragraph-5588_12016 fill-gray0-white-67_3285-paragraph text-text-smsemibold-423_3209"
                        >
                            {{ text_5588_129 ?? "Label" }}
                        </p>
                    </slot>
                </div>
                <slot name="slot_5588_12017" v-if="visible_5586_121">
                    <Check
                        id="5588_12017"
                        class="Pixso-instance-5588_12017"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
            </div>
            <div
                id="5588_13048"
                class="Pixso-symbol-5588_13048 fill-success10-1636_81201"
                v-if="
                    Size === 'lg' &&
                    Color === 'Success' &&
                    Hierarchy === 'Secondary' &&
                    State === 'Hover'
                "
            >
                <slot name="slot_5588_13049" v-if="visible_5586_123">
                    <Circle
                        id="5588_13049"
                        class="Pixso-instance-5588_13049"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <div id="5588_13050" class="Pixso-frame-5588_13050">
                    <slot name="slot_5588_13051" v-if="visible_5586_119">
                        <Dot
                            id="5588_13051"
                            class="Pixso-instance-5588_13051"
                            Size="sm"
                        />
                    </slot>
                    <slot name="slot_5588_13052">
                        <p
                            id="5588_13052"
                            class="Pixso-paragraph-5588_13052 fill-success50-1636_81205-paragraph text-text-smsemibold-423_3209"
                        >
                            {{ text_5588_129 ?? "Label" }}
                        </p>
                    </slot>
                </div>
                <slot name="slot_5588_13053" v-if="visible_5586_121">
                    <Check
                        id="5588_13053"
                        class="Pixso-instance-5588_13053"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
            </div>
            <div
                id="5588_13843"
                class="Pixso-symbol-5588_13843 fill-warning20-428_4551"
                v-if="
                    Size === 'lg' &&
                    Color === 'Warning' &&
                    Hierarchy === 'Primary' &&
                    State === 'Disabled'
                "
            >
                <slot name="slot_5588_13844" v-if="visible_5586_123">
                    <Circle
                        id="5588_13844"
                        class="Pixso-instance-5588_13844"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <div id="5588_13845" class="Pixso-frame-5588_13845">
                    <slot name="slot_5588_13846" v-if="visible_5586_119">
                        <Dot
                            id="5588_13846"
                            class="Pixso-instance-5588_13846"
                            Size="sm"
                        />
                    </slot>
                    <slot name="slot_5588_13847">
                        <p
                            id="5588_13847"
                            class="Pixso-paragraph-5588_13847 fill-warning40-428_4549-paragraph text-text-smsemibold-423_3209"
                        >
                            {{ text_5588_129 ?? "Label" }}
                        </p>
                    </slot>
                </div>
                <slot name="slot_5588_13848" v-if="visible_5586_121">
                    <Check
                        id="5588_13848"
                        class="Pixso-instance-5588_13848"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
            </div>
            <div
                id="5588_13054"
                class="stroke-wrapper-5588_13054"
                v-if="
                    Size === 'lg' &&
                    Color === 'Destructive' &&
                    Hierarchy === 'Outlined' &&
                    State === 'Hover'
                "
            >
                <div class="Pixso-symbol-5588_13054 fill-destructive5-83_2719">
                    <slot name="slot_5588_13055" v-if="visible_5586_123">
                        <Circle
                            id="5588_13055"
                            class="Pixso-instance-5588_13055"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                    <div id="5588_13056" class="Pixso-frame-5588_13056">
                        <slot name="slot_5588_13057" v-if="visible_5586_119">
                            <Dot
                                id="5588_13057"
                                class="Pixso-instance-5588_13057"
                                Size="sm"
                            />
                        </slot>
                        <slot name="slot_5588_13058">
                            <p
                                id="5588_13058"
                                class="Pixso-paragraph-5588_13058 fill-destructive50-423_3219-paragraph text-text-smsemibold-423_3209"
                            >
                                {{ text_5588_129 ?? "Label" }}
                            </p>
                        </slot>
                    </div>
                    <slot name="slot_5588_13059" v-if="visible_5586_121">
                        <Check
                            id="5588_13059"
                            class="Pixso-instance-5588_13059"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div
                    class="stroke-5588_13054 stroke-destructive50-423_3219"
                ></div>
            </div>
            <div
                id="5588_12174"
                class="Pixso-symbol-5588_12174 fill-success50-1636_81205"
                v-if="
                    Size === 'lg' &&
                    Color === 'Success' &&
                    Hierarchy === 'Primary' &&
                    State === 'Default'
                "
            >
                <slot name="slot_5588_12175" v-if="visible_5586_123">
                    <Circle
                        id="5588_12175"
                        class="Pixso-instance-5588_12175"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <div id="5588_12176" class="Pixso-frame-5588_12176">
                    <slot name="slot_5588_12177" v-if="visible_5586_119">
                        <Dot
                            id="5588_12177"
                            class="Pixso-instance-5588_12177"
                            Size="sm"
                        />
                    </slot>
                    <slot name="slot_5588_12178">
                        <p
                            id="5588_12178"
                            class="Pixso-paragraph-5588_12178 fill-gray0-white-67_3285-paragraph text-text-smsemibold-423_3209"
                        >
                            {{ text_5588_129 ?? "Label" }}
                        </p>
                    </slot>
                </div>
                <slot name="slot_5588_12179" v-if="visible_5586_121">
                    <Check
                        id="5588_12179"
                        class="Pixso-instance-5588_12179"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
            </div>
            <div
                id="5588_13060"
                class="stroke-wrapper-5588_13060"
                v-if="
                    Size === 'lg' &&
                    Color === 'Warning' &&
                    Hierarchy === 'Outlined' &&
                    State === 'Hover'
                "
            >
                <div class="Pixso-symbol-5588_13060 fill-warning5-83_2717">
                    <slot name="slot_5588_13061" v-if="visible_5586_123">
                        <Circle
                            id="5588_13061"
                            class="Pixso-instance-5588_13061"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                    <div id="5588_13062" class="Pixso-frame-5588_13062">
                        <slot name="slot_5588_13063" v-if="visible_5586_119">
                            <Dot
                                id="5588_13063"
                                class="Pixso-instance-5588_13063"
                                Size="sm"
                            />
                        </slot>
                        <slot name="slot_5588_13064">
                            <p
                                id="5588_13064"
                                class="Pixso-paragraph-5588_13064 fill-warning50-423_3213-paragraph text-text-smsemibold-423_3209"
                            >
                                {{ text_5588_129 ?? "Label" }}
                            </p>
                        </slot>
                    </div>
                    <slot name="slot_5588_13065" v-if="visible_5586_121">
                        <Check
                            id="5588_13065"
                            class="Pixso-instance-5588_13065"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div class="stroke-5588_13060 stroke-warning50-423_3213"></div>
            </div>
            <div
                id="5588_13849"
                class="Pixso-symbol-5588_13849 fill-success20-1636_81202"
                v-if="
                    Size === 'lg' &&
                    Color === 'Success' &&
                    Hierarchy === 'Primary' &&
                    State === 'Disabled'
                "
            >
                <slot name="slot_5588_13850" v-if="visible_5586_123">
                    <Circle
                        id="5588_13850"
                        class="Pixso-instance-5588_13850"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <div id="5588_13851" class="Pixso-frame-5588_13851">
                    <slot name="slot_5588_13852" v-if="visible_5586_119">
                        <Dot
                            id="5588_13852"
                            class="Pixso-instance-5588_13852"
                            Size="sm"
                        />
                    </slot>
                    <slot name="slot_5588_13853">
                        <p
                            id="5588_13853"
                            class="Pixso-paragraph-5588_13853 fill-success40-1636_81204-paragraph text-text-smsemibold-423_3209"
                        >
                            {{ text_5588_129 ?? "Label" }}
                        </p>
                    </slot>
                </div>
                <slot name="slot_5588_13854" v-if="visible_5586_121">
                    <Check
                        id="5588_13854"
                        class="Pixso-instance-5588_13854"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
            </div>
            <div
                id="5588_13066"
                class="stroke-wrapper-5588_13066"
                v-if="
                    Size === 'lg' &&
                    Color === 'Success' &&
                    Hierarchy === 'Outlined' &&
                    State === 'Hover'
                "
            >
                <div class="Pixso-symbol-5588_13066 fill-success5-1636_81199">
                    <slot name="slot_5588_13067" v-if="visible_5586_123">
                        <Circle
                            id="5588_13067"
                            class="Pixso-instance-5588_13067"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                    <div id="5588_13068" class="Pixso-frame-5588_13068">
                        <slot name="slot_5588_13069" v-if="visible_5586_119">
                            <Dot
                                id="5588_13069"
                                class="Pixso-instance-5588_13069"
                                Size="sm"
                            />
                        </slot>
                        <slot name="slot_5588_13070">
                            <p
                                id="5588_13070"
                                class="Pixso-paragraph-5588_13070 fill-success50-1636_81205-paragraph text-text-smsemibold-423_3209"
                            >
                                {{ text_5588_129 ?? "Label" }}
                            </p>
                        </slot>
                    </div>
                    <slot name="slot_5588_13071" v-if="visible_5586_121">
                        <Check
                            id="5588_13071"
                            class="Pixso-instance-5588_13071"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div
                    class="stroke-5588_13066 stroke-success50-1636_81205"
                ></div>
            </div>
            <div
                id="5588_11847"
                class="Pixso-symbol-5588_11847 fill-destructive5-83_2719"
                v-if="
                    Size === 'lg' &&
                    Color === 'Destructive' &&
                    Hierarchy === 'Secondary' &&
                    State === 'Default'
                "
            >
                <slot name="slot_5588_11848" v-if="visible_5586_123">
                    <Circle
                        id="5588_11848"
                        class="Pixso-instance-5588_11848"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <div id="5588_11849" class="Pixso-frame-5588_11849">
                    <slot name="slot_5588_11850" v-if="visible_5586_119">
                        <Dot
                            id="5588_11850"
                            class="Pixso-instance-5588_11850"
                            Size="sm"
                        />
                    </slot>
                    <slot name="slot_5588_11851">
                        <p
                            id="5588_11851"
                            class="Pixso-paragraph-5588_11851 fill-destructive50-423_3219-paragraph text-text-smsemibold-423_3209"
                        >
                            {{ text_5588_129 ?? "Label" }}
                        </p>
                    </slot>
                </div>
                <slot name="slot_5588_11852" v-if="visible_5586_121">
                    <Check
                        id="5588_11852"
                        class="Pixso-instance-5588_11852"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
            </div>
            <div
                id="5588_13072"
                class="Pixso-symbol-5588_13072 fill-brand70-1257_33468"
                v-if="
                    Size === 'md' &&
                    Color === 'Brand' &&
                    Hierarchy === 'Primary' &&
                    State === 'Hover'
                "
            >
                <slot name="slot_5588_13073" v-if="visible_5586_123">
                    <Circle
                        id="5588_13073"
                        class="Pixso-instance-5588_13073"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <div id="5588_13074" class="Pixso-frame-5588_13074">
                    <slot name="slot_5588_13075" v-if="visible_5586_119">
                        <Dot
                            id="5588_13075"
                            class="Pixso-instance-5588_13075"
                            Size="sm"
                        />
                    </slot>
                    <slot name="slot_5588_13076">
                        <p
                            id="5588_13076"
                            class="Pixso-paragraph-5588_13076 fill-gray0-white-67_3285-paragraph text-text-smsemibold-423_3209"
                        >
                            {{ text_5588_129 ?? "Label" }}
                        </p>
                    </slot>
                </div>
                <slot name="slot_5588_13077" v-if="visible_5586_121">
                    <Check
                        id="5588_13077"
                        class="Pixso-instance-5588_13077"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
            </div>
            <div
                id="5588_13855"
                class="Pixso-symbol-5588_13855 fill-destructive5-83_2719"
                v-if="
                    Size === 'lg' &&
                    Color === 'Destructive' &&
                    Hierarchy === 'Secondary' &&
                    State === 'Disabled'
                "
            >
                <slot name="slot_5588_13856" v-if="visible_5586_123">
                    <Circle
                        id="5588_13856"
                        class="Pixso-instance-5588_13856"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <div id="5588_13857" class="Pixso-frame-5588_13857">
                    <slot name="slot_5588_13858" v-if="visible_5586_119">
                        <Dot
                            id="5588_13858"
                            class="Pixso-instance-5588_13858"
                            Size="sm"
                        />
                    </slot>
                    <slot name="slot_5588_13859">
                        <p
                            id="5588_13859"
                            class="Pixso-paragraph-5588_13859 fill-destructive30-423_3220-paragraph text-text-smsemibold-423_3209"
                        >
                            {{ text_5588_129 ?? "Label" }}
                        </p>
                    </slot>
                </div>
                <slot name="slot_5588_13860" v-if="visible_5586_121">
                    <Check
                        id="5588_13860"
                        class="Pixso-instance-5588_13860"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
            </div>
            <div
                id="5588_13078"
                class="Pixso-symbol-5588_13078 fill-brand10-1257_33461"
                v-if="
                    Size === 'md' &&
                    Color === 'Brand' &&
                    Hierarchy === 'Secondary' &&
                    State === 'Hover'
                "
            >
                <slot name="slot_5588_13079" v-if="visible_5586_123">
                    <Circle
                        id="5588_13079"
                        class="Pixso-instance-5588_13079"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <div id="5588_13080" class="Pixso-frame-5588_13080">
                    <slot name="slot_5588_13081" v-if="visible_5586_119">
                        <Dot
                            id="5588_13081"
                            class="Pixso-instance-5588_13081"
                            Size="sm"
                        />
                    </slot>
                    <slot name="slot_5588_13082">
                        <p
                            id="5588_13082"
                            class="Pixso-paragraph-5588_13082 fill-brand60-1257_33467-paragraph text-text-smsemibold-423_3209"
                        >
                            {{ text_5588_129 ?? "Label" }}
                        </p>
                    </slot>
                </div>
                <slot name="slot_5588_13083" v-if="visible_5586_121">
                    <Check
                        id="5588_13083"
                        class="Pixso-instance-5588_13083"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
            </div>
            <div
                id="5588_12018"
                class="Pixso-symbol-5588_12018 fill-warning5-83_2717"
                v-if="
                    Size === 'lg' &&
                    Color === 'Warning' &&
                    Hierarchy === 'Secondary' &&
                    State === 'Default'
                "
            >
                <slot name="slot_5588_12019" v-if="visible_5586_123">
                    <Circle
                        id="5588_12019"
                        class="Pixso-instance-5588_12019"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <div id="5588_12020" class="Pixso-frame-5588_12020">
                    <slot name="slot_5588_12021" v-if="visible_5586_119">
                        <Dot
                            id="5588_12021"
                            class="Pixso-instance-5588_12021"
                            Size="sm"
                        />
                    </slot>
                    <slot name="slot_5588_12022">
                        <p
                            id="5588_12022"
                            class="Pixso-paragraph-5588_12022 fill-warning50-423_3213-paragraph text-text-smsemibold-423_3209"
                        >
                            {{ text_5588_129 ?? "Label" }}
                        </p>
                    </slot>
                </div>
                <slot name="slot_5588_12023" v-if="visible_5586_121">
                    <Check
                        id="5588_12023"
                        class="Pixso-instance-5588_12023"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
            </div>
            <div
                id="5588_13084"
                class="stroke-wrapper-5588_13084"
                v-if="
                    Size === 'md' &&
                    Color === 'Brand' &&
                    Hierarchy === 'Outlined' &&
                    State === 'Hover'
                "
            >
                <div class="Pixso-symbol-5588_13084 fill-brand5-1257_33460">
                    <slot name="slot_5588_13085" v-if="visible_5586_123">
                        <Circle
                            id="5588_13085"
                            class="Pixso-instance-5588_13085"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                    <div id="5588_13086" class="Pixso-frame-5588_13086">
                        <slot name="slot_5588_13087" v-if="visible_5586_119">
                            <Dot
                                id="5588_13087"
                                class="Pixso-instance-5588_13087"
                                Size="sm"
                            />
                        </slot>
                        <slot name="slot_5588_13088">
                            <p
                                id="5588_13088"
                                class="Pixso-paragraph-5588_13088 fill-brand60-1257_33467-paragraph text-text-smsemibold-423_3209"
                            >
                                {{ text_5588_129 ?? "Label" }}
                            </p>
                        </slot>
                    </div>
                    <slot name="slot_5588_13089" v-if="visible_5586_121">
                        <Check
                            id="5588_13089"
                            class="Pixso-instance-5588_13089"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div class="stroke-5588_13084 stroke-brand60-1257_33467"></div>
            </div>
            <div
                id="5588_13861"
                class="Pixso-symbol-5588_13861 fill-warning5-83_2717"
                v-if="
                    Size === 'lg' &&
                    Color === 'Warning' &&
                    Hierarchy === 'Secondary' &&
                    State === 'Disabled'
                "
            >
                <slot name="slot_5588_13862" v-if="visible_5586_123">
                    <Circle
                        id="5588_13862"
                        class="Pixso-instance-5588_13862"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <div id="5588_13863" class="Pixso-frame-5588_13863">
                    <slot name="slot_5588_13864" v-if="visible_5586_119">
                        <Dot
                            id="5588_13864"
                            class="Pixso-instance-5588_13864"
                            Size="sm"
                        />
                    </slot>
                    <slot name="slot_5588_13865">
                        <p
                            id="5588_13865"
                            class="Pixso-paragraph-5588_13865 fill-warning30-32_4109-paragraph text-text-smsemibold-423_3209"
                        >
                            {{ text_5588_129 ?? "Label" }}
                        </p>
                    </slot>
                </div>
                <slot name="slot_5588_13866" v-if="visible_5586_121">
                    <Check
                        id="5588_13866"
                        class="Pixso-instance-5588_13866"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
            </div>
            <div
                id="5588_13090"
                class="Pixso-symbol-5588_13090 fill-gray60-83_2722"
                v-if="
                    Size === 'lg' &&
                    Color === 'Gray' &&
                    Hierarchy === 'Primary' &&
                    State === 'Hover'
                "
            >
                <slot name="slot_5588_13091" v-if="visible_5586_123">
                    <Circle
                        id="5588_13091"
                        class="Pixso-instance-5588_13091"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <div id="5588_13092" class="Pixso-frame-5588_13092">
                    <slot name="slot_5588_13093" v-if="visible_5586_119">
                        <Dot
                            id="5588_13093"
                            class="Pixso-instance-5588_13093"
                            Size="sm"
                        />
                    </slot>
                    <slot name="slot_5588_13094">
                        <p
                            id="5588_13094"
                            class="Pixso-paragraph-5588_13094 fill-gray0-white-67_3285-paragraph text-text-smsemibold-423_3209"
                        >
                            {{ text_5588_129 ?? "Label" }}
                        </p>
                    </slot>
                </div>
                <slot name="slot_5588_13095" v-if="visible_5586_121">
                    <Check
                        id="5588_13095"
                        class="Pixso-instance-5588_13095"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
            </div>
            <div
                id="5588_12180"
                class="Pixso-symbol-5588_12180 fill-success5-1636_81199"
                v-if="
                    Size === 'lg' &&
                    Color === 'Success' &&
                    Hierarchy === 'Secondary' &&
                    State === 'Default'
                "
            >
                <slot name="slot_5588_12181" v-if="visible_5586_123">
                    <Circle
                        id="5588_12181"
                        class="Pixso-instance-5588_12181"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <div id="5588_12182" class="Pixso-frame-5588_12182">
                    <slot name="slot_5588_12183" v-if="visible_5586_119">
                        <Dot
                            id="5588_12183"
                            class="Pixso-instance-5588_12183"
                            Size="sm"
                        />
                    </slot>
                    <slot name="slot_5588_12184">
                        <p
                            id="5588_12184"
                            class="Pixso-paragraph-5588_12184 fill-success50-1636_81205-paragraph text-text-smsemibold-423_3209"
                        >
                            {{ text_5588_129 ?? "Label" }}
                        </p>
                    </slot>
                </div>
                <slot name="slot_5588_12185" v-if="visible_5586_121">
                    <Check
                        id="5588_12185"
                        class="Pixso-instance-5588_12185"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
            </div>
            <div
                id="5588_13096"
                class="Pixso-symbol-5588_13096 fill-gray10-83_2713"
                v-if="
                    Size === 'lg' &&
                    Color === 'Gray' &&
                    Hierarchy === 'Secondary' &&
                    State === 'Hover'
                "
            >
                <slot name="slot_5588_13097" v-if="visible_5586_123">
                    <Circle
                        id="5588_13097"
                        class="Pixso-instance-5588_13097"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <div id="5588_13098" class="Pixso-frame-5588_13098">
                    <slot name="slot_5588_13099" v-if="visible_5586_119">
                        <Dot
                            id="5588_13099"
                            class="Pixso-instance-5588_13099"
                            Size="sm"
                        />
                    </slot>
                    <slot name="slot_5588_13100">
                        <p
                            id="5588_13100"
                            class="Pixso-paragraph-5588_13100 fill-gray60-83_2722-paragraph text-text-smsemibold-423_3209"
                        >
                            {{ text_5588_129 ?? "Label" }}
                        </p>
                    </slot>
                </div>
                <slot name="slot_5588_13101" v-if="visible_5586_121">
                    <Check
                        id="5588_13101"
                        class="Pixso-instance-5588_13101"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
            </div>
            <div
                id="5588_13867"
                class="Pixso-symbol-5588_13867 fill-success5-1636_81199"
                v-if="
                    Size === 'lg' &&
                    Color === 'Success' &&
                    Hierarchy === 'Secondary' &&
                    State === 'Disabled'
                "
            >
                <slot name="slot_5588_13868" v-if="visible_5586_123">
                    <Circle
                        id="5588_13868"
                        class="Pixso-instance-5588_13868"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <div id="5588_13869" class="Pixso-frame-5588_13869">
                    <slot name="slot_5588_13870" v-if="visible_5586_119">
                        <Dot
                            id="5588_13870"
                            class="Pixso-instance-5588_13870"
                            Size="sm"
                        />
                    </slot>
                    <slot name="slot_5588_13871">
                        <p
                            id="5588_13871"
                            class="Pixso-paragraph-5588_13871 fill-success30-1636_81203-paragraph text-text-smsemibold-423_3209"
                        >
                            {{ text_5588_129 ?? "Label" }}
                        </p>
                    </slot>
                </div>
                <slot name="slot_5588_13872" v-if="visible_5586_121">
                    <Check
                        id="5588_13872"
                        class="Pixso-instance-5588_13872"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
            </div>
            <div
                id="5588_13102"
                class="stroke-wrapper-5588_13102"
                v-if="
                    Size === 'lg' &&
                    Color === 'Gray' &&
                    Hierarchy === 'Outlined' &&
                    State === 'Hover'
                "
            >
                <div class="Pixso-symbol-5588_13102 fill-gray5-32_4120">
                    <slot name="slot_5588_13103" v-if="visible_5586_123">
                        <Circle
                            id="5588_13103"
                            class="Pixso-instance-5588_13103"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                    <div id="5588_13104" class="Pixso-frame-5588_13104">
                        <slot name="slot_5588_13105" v-if="visible_5586_119">
                            <Dot
                                id="5588_13105"
                                class="Pixso-instance-5588_13105"
                                Size="sm"
                            />
                        </slot>
                        <slot name="slot_5588_13106">
                            <p
                                id="5588_13106"
                                class="Pixso-paragraph-5588_13106 fill-gray60-83_2722-paragraph text-text-smsemibold-423_3209"
                            >
                                {{ text_5588_129 ?? "Label" }}
                            </p>
                        </slot>
                    </div>
                    <slot name="slot_5588_13107" v-if="visible_5586_121">
                        <Check
                            id="5588_13107"
                            class="Pixso-instance-5588_13107"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div class="stroke-5588_13102 stroke-gray40-83_2714"></div>
            </div>
            <div
                id="5588_11853"
                class="stroke-wrapper-5588_11853"
                v-if="
                    Size === 'lg' &&
                    Color === 'Destructive' &&
                    Hierarchy === 'Outlined' &&
                    State === 'Default'
                "
            >
                <div class="Pixso-symbol-5588_11853">
                    <slot name="slot_5588_11854" v-if="visible_5586_123">
                        <Circle
                            id="5588_11854"
                            class="Pixso-instance-5588_11854"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                    <div id="5588_11855" class="Pixso-frame-5588_11855">
                        <slot name="slot_5588_11856" v-if="visible_5586_119">
                            <Dot
                                id="5588_11856"
                                class="Pixso-instance-5588_11856"
                                Size="sm"
                            />
                        </slot>
                        <slot name="slot_5588_11857">
                            <p
                                id="5588_11857"
                                class="Pixso-paragraph-5588_11857 fill-destructive50-423_3219-paragraph text-text-smsemibold-423_3209"
                            >
                                {{ text_5588_129 ?? "Label" }}
                            </p>
                        </slot>
                    </div>
                    <slot name="slot_5588_11858" v-if="visible_5586_121">
                        <Check
                            id="5588_11858"
                            class="Pixso-instance-5588_11858"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div
                    class="stroke-5588_11853 stroke-destructive50-423_3219"
                ></div>
            </div>
            <div
                id="5588_13108"
                class="Pixso-symbol-5588_13108 fill-brand70-1257_33468"
                v-if="
                    Size === 'sm' &&
                    Color === 'Brand' &&
                    Hierarchy === 'Primary' &&
                    State === 'Hover'
                "
            >
                <slot name="slot_5588_13109" v-if="visible_5586_123">
                    <Circle
                        id="5588_13109"
                        class="Pixso-instance-5588_13109"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <div id="5588_13110" class="Pixso-frame-5588_13110">
                    <slot name="slot_5588_13111" v-if="visible_5586_119">
                        <Dot
                            id="5588_13111"
                            class="Pixso-instance-5588_13111"
                            Size="sm"
                        />
                    </slot>
                    <slot name="slot_5588_13112">
                        <p
                            id="5588_13112"
                            class="Pixso-paragraph-5588_13112 fill-gray0-white-67_3285-paragraph text-text-xssemibold-439_9521"
                        >
                            {{ text_5588_129 ?? "Label" }}
                        </p>
                    </slot>
                </div>
                <slot name="slot_5588_13113" v-if="visible_5586_121">
                    <Check
                        id="5588_13113"
                        class="Pixso-instance-5588_13113"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
            </div>
            <div
                id="5588_13873"
                class="stroke-wrapper-5588_13873"
                v-if="
                    Size === 'lg' &&
                    Color === 'Destructive' &&
                    Hierarchy === 'Outlined' &&
                    State === 'Disabled'
                "
            >
                <div class="Pixso-symbol-5588_13873">
                    <slot name="slot_5588_13874" v-if="visible_5586_123">
                        <Circle
                            id="5588_13874"
                            class="Pixso-instance-5588_13874"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                    <div id="5588_13875" class="Pixso-frame-5588_13875">
                        <slot name="slot_5588_13876" v-if="visible_5586_119">
                            <Dot
                                id="5588_13876"
                                class="Pixso-instance-5588_13876"
                                Size="sm"
                            />
                        </slot>
                        <slot name="slot_5588_13877">
                            <p
                                id="5588_13877"
                                class="Pixso-paragraph-5588_13877 fill-destructive30-423_3220-paragraph text-text-smsemibold-423_3209"
                            >
                                {{ text_5588_129 ?? "Label" }}
                            </p>
                        </slot>
                    </div>
                    <slot name="slot_5588_13878" v-if="visible_5586_121">
                        <Check
                            id="5588_13878"
                            class="Pixso-instance-5588_13878"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div
                    class="stroke-5588_13873 stroke-destructive30-423_3220"
                ></div>
            </div>
            <div
                id="5588_13114"
                class="Pixso-symbol-5588_13114 fill-brand10-1257_33461"
                v-if="
                    Size === 'sm' &&
                    Color === 'Brand' &&
                    Hierarchy === 'Secondary' &&
                    State === 'Hover'
                "
            >
                <slot name="slot_5588_13115" v-if="visible_5586_123">
                    <Circle
                        id="5588_13115"
                        class="Pixso-instance-5588_13115"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <div id="5588_13116" class="Pixso-frame-5588_13116">
                    <slot name="slot_5588_13117" v-if="visible_5586_119">
                        <Dot
                            id="5588_13117"
                            class="Pixso-instance-5588_13117"
                            Size="sm"
                        />
                    </slot>
                    <slot name="slot_5588_13118">
                        <p
                            id="5588_13118"
                            class="Pixso-paragraph-5588_13118 fill-brand60-1257_33467-paragraph text-text-xssemibold-439_9521"
                        >
                            {{ text_5588_129 ?? "Label" }}
                        </p>
                    </slot>
                </div>
                <slot name="slot_5588_13119" v-if="visible_5586_121">
                    <Check
                        id="5588_13119"
                        class="Pixso-instance-5588_13119"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
            </div>
            <div
                id="5588_12024"
                class="stroke-wrapper-5588_12024"
                v-if="
                    Size === 'lg' &&
                    Color === 'Warning' &&
                    Hierarchy === 'Outlined' &&
                    State === 'Default'
                "
            >
                <div class="Pixso-symbol-5588_12024">
                    <slot name="slot_5588_12025" v-if="visible_5586_123">
                        <Circle
                            id="5588_12025"
                            class="Pixso-instance-5588_12025"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                    <div id="5588_12026" class="Pixso-frame-5588_12026">
                        <slot name="slot_5588_12027" v-if="visible_5586_119">
                            <Dot
                                id="5588_12027"
                                class="Pixso-instance-5588_12027"
                                Size="sm"
                            />
                        </slot>
                        <slot name="slot_5588_12028">
                            <p
                                id="5588_12028"
                                class="Pixso-paragraph-5588_12028 fill-warning50-423_3213-paragraph text-text-smsemibold-423_3209"
                            >
                                {{ text_5588_129 ?? "Label" }}
                            </p>
                        </slot>
                    </div>
                    <slot name="slot_5588_12029" v-if="visible_5586_121">
                        <Check
                            id="5588_12029"
                            class="Pixso-instance-5588_12029"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div class="stroke-5588_12024 stroke-warning50-423_3213"></div>
            </div>
            <div
                id="5588_13120"
                class="stroke-wrapper-5588_13120"
                v-if="
                    Size === 'sm' &&
                    Color === 'Brand' &&
                    Hierarchy === 'Outlined' &&
                    State === 'Hover'
                "
            >
                <div class="Pixso-symbol-5588_13120 fill-brand5-1257_33460">
                    <slot name="slot_5588_13121" v-if="visible_5586_123">
                        <Circle
                            id="5588_13121"
                            class="Pixso-instance-5588_13121"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                    <div id="5588_13122" class="Pixso-frame-5588_13122">
                        <slot name="slot_5588_13123" v-if="visible_5586_119">
                            <Dot
                                id="5588_13123"
                                class="Pixso-instance-5588_13123"
                                Size="sm"
                            />
                        </slot>
                        <slot name="slot_5588_13124">
                            <p
                                id="5588_13124"
                                class="Pixso-paragraph-5588_13124 fill-brand60-1257_33467-paragraph text-text-xssemibold-439_9521"
                            >
                                {{ text_5588_129 ?? "Label" }}
                            </p>
                        </slot>
                    </div>
                    <slot name="slot_5588_13125" v-if="visible_5586_121">
                        <Check
                            id="5588_13125"
                            class="Pixso-instance-5588_13125"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div class="stroke-5588_13120 stroke-brand60-1257_33467"></div>
            </div>
            <div
                id="5588_13879"
                class="stroke-wrapper-5588_13879"
                v-if="
                    Size === 'lg' &&
                    Color === 'Warning' &&
                    Hierarchy === 'Outlined' &&
                    State === 'Disabled'
                "
            >
                <div class="Pixso-symbol-5588_13879">
                    <slot name="slot_5588_13880" v-if="visible_5586_123">
                        <Circle
                            id="5588_13880"
                            class="Pixso-instance-5588_13880"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                    <div id="5588_13881" class="Pixso-frame-5588_13881">
                        <slot name="slot_5588_13882" v-if="visible_5586_119">
                            <Dot
                                id="5588_13882"
                                class="Pixso-instance-5588_13882"
                                Size="sm"
                            />
                        </slot>
                        <slot name="slot_5588_13883">
                            <p
                                id="5588_13883"
                                class="Pixso-paragraph-5588_13883 fill-warning30-32_4109-paragraph text-text-smsemibold-423_3209"
                            >
                                {{ text_5588_129 ?? "Label" }}
                            </p>
                        </slot>
                    </div>
                    <slot name="slot_5588_13884" v-if="visible_5586_121">
                        <Check
                            id="5588_13884"
                            class="Pixso-instance-5588_13884"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div class="stroke-5588_13879 stroke-warning30-32_4109"></div>
            </div>
            <div
                id="5588_13126"
                class="Pixso-symbol-5588_13126 fill-destructive60-438_3719"
                v-if="
                    Size === 'md' &&
                    Color === 'Destructive' &&
                    Hierarchy === 'Primary' &&
                    State === 'Hover'
                "
            >
                <slot name="slot_5588_13127" v-if="visible_5586_123">
                    <Circle
                        id="5588_13127"
                        class="Pixso-instance-5588_13127"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <div id="5588_13128" class="Pixso-frame-5588_13128">
                    <slot name="slot_5588_13129" v-if="visible_5586_119">
                        <Dot
                            id="5588_13129"
                            class="Pixso-instance-5588_13129"
                            Size="sm"
                        />
                    </slot>
                    <slot name="slot_5588_13130">
                        <p
                            id="5588_13130"
                            class="Pixso-paragraph-5588_13130 fill-gray0-white-67_3285-paragraph text-text-smsemibold-423_3209"
                        >
                            {{ text_5588_129 ?? "Label" }}
                        </p>
                    </slot>
                </div>
                <slot name="slot_5588_13131" v-if="visible_5586_121">
                    <Check
                        id="5588_13131"
                        class="Pixso-instance-5588_13131"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
            </div>
            <div
                id="5588_12186"
                class="stroke-wrapper-5588_12186"
                v-if="
                    Size === 'lg' &&
                    Color === 'Success' &&
                    Hierarchy === 'Outlined' &&
                    State === 'Default'
                "
            >
                <div class="Pixso-symbol-5588_12186">
                    <slot name="slot_5588_12187" v-if="visible_5586_123">
                        <Circle
                            id="5588_12187"
                            class="Pixso-instance-5588_12187"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                    <div id="5588_12188" class="Pixso-frame-5588_12188">
                        <slot name="slot_5588_12189" v-if="visible_5586_119">
                            <Dot
                                id="5588_12189"
                                class="Pixso-instance-5588_12189"
                                Size="sm"
                            />
                        </slot>
                        <slot name="slot_5588_12190">
                            <p
                                id="5588_12190"
                                class="Pixso-paragraph-5588_12190 fill-success50-1636_81205-paragraph text-text-smsemibold-423_3209"
                            >
                                {{ text_5588_129 ?? "Label" }}
                            </p>
                        </slot>
                    </div>
                    <slot name="slot_5588_12191" v-if="visible_5586_121">
                        <Check
                            id="5588_12191"
                            class="Pixso-instance-5588_12191"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div
                    class="stroke-5588_12186 stroke-success50-1636_81205"
                ></div>
            </div>
            <div
                id="5588_13132"
                class="Pixso-symbol-5588_13132 fill-warning60-438_3718"
                v-if="
                    Size === 'md' &&
                    Color === 'Warning' &&
                    Hierarchy === 'Primary' &&
                    State === 'Hover'
                "
            >
                <slot name="slot_5588_13133" v-if="visible_5586_123">
                    <Circle
                        id="5588_13133"
                        class="Pixso-instance-5588_13133"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <div id="5588_13134" class="Pixso-frame-5588_13134">
                    <slot name="slot_5588_13135" v-if="visible_5586_119">
                        <Dot
                            id="5588_13135"
                            class="Pixso-instance-5588_13135"
                            Size="sm"
                        />
                    </slot>
                    <slot name="slot_5588_13136">
                        <p
                            id="5588_13136"
                            class="Pixso-paragraph-5588_13136 fill-gray0-white-67_3285-paragraph text-text-smsemibold-423_3209"
                        >
                            {{ text_5588_129 ?? "Label" }}
                        </p>
                    </slot>
                </div>
                <slot name="slot_5588_13137" v-if="visible_5586_121">
                    <Check
                        id="5588_13137"
                        class="Pixso-instance-5588_13137"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
            </div>
            <div
                id="5588_13885"
                class="stroke-wrapper-5588_13885"
                v-if="
                    Size === 'lg' &&
                    Color === 'Success' &&
                    Hierarchy === 'Outlined' &&
                    State === 'Disabled'
                "
            >
                <div class="Pixso-symbol-5588_13885">
                    <slot name="slot_5588_13886" v-if="visible_5586_123">
                        <Circle
                            id="5588_13886"
                            class="Pixso-instance-5588_13886"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                    <div id="5588_13887" class="Pixso-frame-5588_13887">
                        <slot name="slot_5588_13888" v-if="visible_5586_119">
                            <Dot
                                id="5588_13888"
                                class="Pixso-instance-5588_13888"
                                Size="sm"
                            />
                        </slot>
                        <slot name="slot_5588_13889">
                            <p
                                id="5588_13889"
                                class="Pixso-paragraph-5588_13889 fill-success30-1636_81203-paragraph text-text-smsemibold-423_3209"
                            >
                                {{ text_5588_129 ?? "Label" }}
                            </p>
                        </slot>
                    </div>
                    <slot name="slot_5588_13890" v-if="visible_5586_121">
                        <Check
                            id="5588_13890"
                            class="Pixso-instance-5588_13890"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div
                    class="stroke-5588_13885 stroke-success30-1636_81203"
                ></div>
            </div>
            <div
                id="5588_13138"
                class="Pixso-symbol-5588_13138 fill-success60-1636_81206"
                v-if="
                    Size === 'md' &&
                    Color === 'Success' &&
                    Hierarchy === 'Primary' &&
                    State === 'Hover'
                "
            >
                <slot name="slot_5588_13139" v-if="visible_5586_123">
                    <Circle
                        id="5588_13139"
                        class="Pixso-instance-5588_13139"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <div id="5588_13140" class="Pixso-frame-5588_13140">
                    <slot name="slot_5588_13141" v-if="visible_5586_119">
                        <Dot
                            id="5588_13141"
                            class="Pixso-instance-5588_13141"
                            Size="sm"
                        />
                    </slot>
                    <slot name="slot_5588_13142">
                        <p
                            id="5588_13142"
                            class="Pixso-paragraph-5588_13142 fill-gray0-white-67_3285-paragraph text-text-smsemibold-423_3209"
                        >
                            {{ text_5588_129 ?? "Label" }}
                        </p>
                    </slot>
                </div>
                <slot name="slot_5588_13143" v-if="visible_5586_121">
                    <Check
                        id="5588_13143"
                        class="Pixso-instance-5588_13143"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
            </div>
            <div
                id="5588_11163"
                class="Pixso-symbol-5588_11163 fill-brand60-1257_33467"
                v-if="
                    Size === 'md' &&
                    Color === 'Brand' &&
                    Hierarchy === 'Primary' &&
                    State === 'Default'
                "
            >
                <slot name="slot_5588_11164" v-if="visible_5586_123">
                    <Circle
                        id="5588_11164"
                        class="Pixso-instance-5588_11164"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <div id="5588_11215" class="Pixso-frame-5588_11215">
                    <slot name="slot_5588_11165" v-if="visible_5586_119">
                        <Dot
                            id="5588_11165"
                            class="Pixso-instance-5588_11165"
                            Size="sm"
                        />
                    </slot>
                    <slot name="slot_5588_11166">
                        <p
                            id="5588_11166"
                            class="Pixso-paragraph-5588_11166 fill-gray0-white-67_3285-paragraph text-text-smsemibold-423_3209"
                        >
                            {{ text_5588_129 ?? "Label" }}
                        </p>
                    </slot>
                </div>
                <slot name="slot_5588_11167" v-if="visible_5586_121">
                    <Check
                        id="5588_11167"
                        class="Pixso-instance-5588_11167"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
            </div>
            <div
                id="5588_13144"
                class="Pixso-symbol-5588_13144 fill-destructive10-423_3221"
                v-if="
                    Size === 'md' &&
                    Color === 'Destructive' &&
                    Hierarchy === 'Secondary' &&
                    State === 'Hover'
                "
            >
                <slot name="slot_5588_13145" v-if="visible_5586_123">
                    <Circle
                        id="5588_13145"
                        class="Pixso-instance-5588_13145"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <div id="5588_13146" class="Pixso-frame-5588_13146">
                    <slot name="slot_5588_13147" v-if="visible_5586_119">
                        <Dot
                            id="5588_13147"
                            class="Pixso-instance-5588_13147"
                            Size="sm"
                        />
                    </slot>
                    <slot name="slot_5588_13148">
                        <p
                            id="5588_13148"
                            class="Pixso-paragraph-5588_13148 fill-destructive50-423_3219-paragraph text-text-smsemibold-423_3209"
                        >
                            {{ text_5588_129 ?? "Label" }}
                        </p>
                    </slot>
                </div>
                <slot name="slot_5588_13149" v-if="visible_5586_121">
                    <Check
                        id="5588_13149"
                        class="Pixso-instance-5588_13149"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
            </div>
            <div
                id="5588_13891"
                class="Pixso-symbol-5588_13891 fill-brand20-1257_33462"
                v-if="
                    Size === 'md' &&
                    Color === 'Brand' &&
                    Hierarchy === 'Primary' &&
                    State === 'Disabled'
                "
            >
                <slot name="slot_5588_13892" v-if="visible_5586_123">
                    <Circle
                        id="5588_13892"
                        class="Pixso-instance-5588_13892"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <div id="5588_13893" class="Pixso-frame-5588_13893">
                    <slot name="slot_5588_13894" v-if="visible_5586_119">
                        <Dot
                            id="5588_13894"
                            class="Pixso-instance-5588_13894"
                            Size="sm"
                        />
                    </slot>
                    <slot name="slot_5588_13895">
                        <p
                            id="5588_13895"
                            class="Pixso-paragraph-5588_13895 fill-brand40-1257_33464-paragraph text-text-smsemibold-423_3209"
                        >
                            {{ text_5588_129 ?? "Label" }}
                        </p>
                    </slot>
                </div>
                <slot name="slot_5588_13896" v-if="visible_5586_121">
                    <Check
                        id="5588_13896"
                        class="Pixso-instance-5588_13896"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
            </div>
            <div
                id="5588_13150"
                class="Pixso-symbol-5588_13150 fill-warning10-423_3215"
                v-if="
                    Size === 'md' &&
                    Color === 'Warning' &&
                    Hierarchy === 'Secondary' &&
                    State === 'Hover'
                "
            >
                <slot name="slot_5588_13151" v-if="visible_5586_123">
                    <Circle
                        id="5588_13151"
                        class="Pixso-instance-5588_13151"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <div id="5588_13152" class="Pixso-frame-5588_13152">
                    <slot name="slot_5588_13153" v-if="visible_5586_119">
                        <Dot
                            id="5588_13153"
                            class="Pixso-instance-5588_13153"
                            Size="sm"
                        />
                    </slot>
                    <slot name="slot_5588_13154">
                        <p
                            id="5588_13154"
                            class="Pixso-paragraph-5588_13154 fill-warning50-423_3213-paragraph text-text-smsemibold-423_3209"
                        >
                            {{ text_5588_129 ?? "Label" }}
                        </p>
                    </slot>
                </div>
                <slot name="slot_5588_13155" v-if="visible_5586_121">
                    <Check
                        id="5588_13155"
                        class="Pixso-instance-5588_13155"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
            </div>
            <div
                id="5588_11352"
                class="Pixso-symbol-5588_11352 fill-brand5-1257_33460"
                v-if="
                    Size === 'md' &&
                    Color === 'Brand' &&
                    Hierarchy === 'Secondary' &&
                    State === 'Default'
                "
            >
                <slot name="slot_5588_11353" v-if="visible_5586_123">
                    <Circle
                        id="5588_11353"
                        class="Pixso-instance-5588_11353"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <div id="5588_11354" class="Pixso-frame-5588_11354">
                    <slot name="slot_5588_11355" v-if="visible_5586_119">
                        <Dot
                            id="5588_11355"
                            class="Pixso-instance-5588_11355"
                            Size="sm"
                        />
                    </slot>
                    <slot name="slot_5588_11356">
                        <p
                            id="5588_11356"
                            class="Pixso-paragraph-5588_11356 fill-brand60-1257_33467-paragraph text-text-smsemibold-423_3209"
                        >
                            {{ text_5588_129 ?? "Label" }}
                        </p>
                    </slot>
                </div>
                <slot name="slot_5588_11357" v-if="visible_5586_121">
                    <Check
                        id="5588_11357"
                        class="Pixso-instance-5588_11357"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
            </div>
            <div
                id="5588_13156"
                class="Pixso-symbol-5588_13156 fill-success10-1636_81201"
                v-if="
                    Size === 'md' &&
                    Color === 'Success' &&
                    Hierarchy === 'Secondary' &&
                    State === 'Hover'
                "
            >
                <slot name="slot_5588_13157" v-if="visible_5586_123">
                    <Circle
                        id="5588_13157"
                        class="Pixso-instance-5588_13157"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <div id="5588_13158" class="Pixso-frame-5588_13158">
                    <slot name="slot_5588_13159" v-if="visible_5586_119">
                        <Dot
                            id="5588_13159"
                            class="Pixso-instance-5588_13159"
                            Size="sm"
                        />
                    </slot>
                    <slot name="slot_5588_13160">
                        <p
                            id="5588_13160"
                            class="Pixso-paragraph-5588_13160 fill-success50-1636_81205-paragraph text-text-smsemibold-423_3209"
                        >
                            {{ text_5588_129 ?? "Label" }}
                        </p>
                    </slot>
                </div>
                <slot name="slot_5588_13161" v-if="visible_5586_121">
                    <Check
                        id="5588_13161"
                        class="Pixso-instance-5588_13161"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
            </div>
            <div
                id="5588_13897"
                class="Pixso-symbol-5588_13897 fill-brand5-1257_33460"
                v-if="
                    Size === 'md' &&
                    Color === 'Brand' &&
                    Hierarchy === 'Secondary' &&
                    State === 'Disabled'
                "
            >
                <slot name="slot_5588_13898" v-if="visible_5586_123">
                    <Circle
                        id="5588_13898"
                        class="Pixso-instance-5588_13898"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <div id="5588_13899" class="Pixso-frame-5588_13899">
                    <slot name="slot_5588_13900" v-if="visible_5586_119">
                        <Dot
                            id="5588_13900"
                            class="Pixso-instance-5588_13900"
                            Size="sm"
                        />
                    </slot>
                    <slot name="slot_5588_13901">
                        <p
                            id="5588_13901"
                            class="Pixso-paragraph-5588_13901 fill-brand30-1257_33463-paragraph text-text-smsemibold-423_3209"
                        >
                            {{ text_5588_129 ?? "Label" }}
                        </p>
                    </slot>
                </div>
                <slot name="slot_5588_13902" v-if="visible_5586_121">
                    <Check
                        id="5588_13902"
                        class="Pixso-instance-5588_13902"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
            </div>
            <div
                id="5588_13162"
                class="stroke-wrapper-5588_13162"
                v-if="
                    Size === 'md' &&
                    Color === 'Destructive' &&
                    Hierarchy === 'Outlined' &&
                    State === 'Hover'
                "
            >
                <div class="Pixso-symbol-5588_13162 fill-destructive5-83_2719">
                    <slot name="slot_5588_13163" v-if="visible_5586_123">
                        <Circle
                            id="5588_13163"
                            class="Pixso-instance-5588_13163"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                    <div id="5588_13164" class="Pixso-frame-5588_13164">
                        <slot name="slot_5588_13165" v-if="visible_5586_119">
                            <Dot
                                id="5588_13165"
                                class="Pixso-instance-5588_13165"
                                Size="sm"
                            />
                        </slot>
                        <slot name="slot_5588_13166">
                            <p
                                id="5588_13166"
                                class="Pixso-paragraph-5588_13166 fill-destructive50-423_3219-paragraph text-text-smsemibold-423_3209"
                            >
                                {{ text_5588_129 ?? "Label" }}
                            </p>
                        </slot>
                    </div>
                    <slot name="slot_5588_13167" v-if="visible_5586_121">
                        <Check
                            id="5588_13167"
                            class="Pixso-instance-5588_13167"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div
                    class="stroke-5588_13162 stroke-destructive50-423_3219"
                ></div>
            </div>
            <div
                id="5588_11415"
                class="stroke-wrapper-5588_11415"
                v-if="
                    Size === 'md' &&
                    Color === 'Brand' &&
                    Hierarchy === 'Outlined' &&
                    State === 'Default'
                "
            >
                <div class="Pixso-symbol-5588_11415">
                    <slot name="slot_5588_11416" v-if="visible_5586_123">
                        <Circle
                            id="5588_11416"
                            class="Pixso-instance-5588_11416"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                    <div id="5588_11417" class="Pixso-frame-5588_11417">
                        <slot name="slot_5588_11418" v-if="visible_5586_119">
                            <Dot
                                id="5588_11418"
                                class="Pixso-instance-5588_11418"
                                Size="sm"
                            />
                        </slot>
                        <slot name="slot_5588_11419">
                            <p
                                id="5588_11419"
                                class="Pixso-paragraph-5588_11419 fill-brand60-1257_33467-paragraph text-text-smsemibold-423_3209"
                            >
                                {{ text_5588_129 ?? "Label" }}
                            </p>
                        </slot>
                    </div>
                    <slot name="slot_5588_11420" v-if="visible_5586_121">
                        <Check
                            id="5588_11420"
                            class="Pixso-instance-5588_11420"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div class="stroke-5588_11415 stroke-brand60-1257_33467"></div>
            </div>
            <div
                id="5588_13168"
                class="stroke-wrapper-5588_13168"
                v-if="
                    Size === 'md' &&
                    Color === 'Warning' &&
                    Hierarchy === 'Outlined' &&
                    State === 'Hover'
                "
            >
                <div class="Pixso-symbol-5588_13168 fill-warning5-83_2717">
                    <slot name="slot_5588_13169" v-if="visible_5586_123">
                        <Circle
                            id="5588_13169"
                            class="Pixso-instance-5588_13169"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                    <div id="5588_13170" class="Pixso-frame-5588_13170">
                        <slot name="slot_5588_13171" v-if="visible_5586_119">
                            <Dot
                                id="5588_13171"
                                class="Pixso-instance-5588_13171"
                                Size="sm"
                            />
                        </slot>
                        <slot name="slot_5588_13172">
                            <p
                                id="5588_13172"
                                class="Pixso-paragraph-5588_13172 fill-warning50-423_3213-paragraph text-text-smsemibold-423_3209"
                            >
                                {{ text_5588_129 ?? "Label" }}
                            </p>
                        </slot>
                    </div>
                    <slot name="slot_5588_13173" v-if="visible_5586_121">
                        <Check
                            id="5588_13173"
                            class="Pixso-instance-5588_13173"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div class="stroke-5588_13168 stroke-warning50-423_3213"></div>
            </div>
            <div
                id="5588_13903"
                class="stroke-wrapper-5588_13903"
                v-if="
                    Size === 'md' &&
                    Color === 'Brand' &&
                    Hierarchy === 'Outlined' &&
                    State === 'Disabled'
                "
            >
                <div class="Pixso-symbol-5588_13903">
                    <slot name="slot_5588_13904" v-if="visible_5586_123">
                        <Circle
                            id="5588_13904"
                            class="Pixso-instance-5588_13904"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                    <div id="5588_13905" class="Pixso-frame-5588_13905">
                        <slot name="slot_5588_13906" v-if="visible_5586_119">
                            <Dot
                                id="5588_13906"
                                class="Pixso-instance-5588_13906"
                                Size="sm"
                            />
                        </slot>
                        <slot name="slot_5588_13907">
                            <p
                                id="5588_13907"
                                class="Pixso-paragraph-5588_13907 fill-brand30-1257_33463-paragraph text-text-smsemibold-423_3209"
                            >
                                {{ text_5588_129 ?? "Label" }}
                            </p>
                        </slot>
                    </div>
                    <slot name="slot_5588_13908" v-if="visible_5586_121">
                        <Check
                            id="5588_13908"
                            class="Pixso-instance-5588_13908"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div class="stroke-5588_13903 stroke-brand30-1257_33463"></div>
            </div>
            <div
                id="5588_13174"
                class="stroke-wrapper-5588_13174"
                v-if="
                    Size === 'md' &&
                    Color === 'Success' &&
                    Hierarchy === 'Outlined' &&
                    State === 'Hover'
                "
            >
                <div class="Pixso-symbol-5588_13174 fill-success5-1636_81199">
                    <slot name="slot_5588_13175" v-if="visible_5586_123">
                        <Circle
                            id="5588_13175"
                            class="Pixso-instance-5588_13175"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                    <div id="5588_13176" class="Pixso-frame-5588_13176">
                        <slot name="slot_5588_13177" v-if="visible_5586_119">
                            <Dot
                                id="5588_13177"
                                class="Pixso-instance-5588_13177"
                                Size="sm"
                            />
                        </slot>
                        <slot name="slot_5588_13178">
                            <p
                                id="5588_13178"
                                class="Pixso-paragraph-5588_13178 fill-success50-1636_81205-paragraph text-text-smsemibold-423_3209"
                            >
                                {{ text_5588_129 ?? "Label" }}
                            </p>
                        </slot>
                    </div>
                    <slot name="slot_5588_13179" v-if="visible_5586_121">
                        <Check
                            id="5588_13179"
                            class="Pixso-instance-5588_13179"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div
                    class="stroke-5588_13174 stroke-success50-1636_81205"
                ></div>
            </div>
            <div
                id="5588_11517"
                class="Pixso-symbol-5588_11517 fill-gray80-32_4123"
                v-if="
                    Size === 'lg' &&
                    Color === 'Gray' &&
                    Hierarchy === 'Primary' &&
                    State === 'Default'
                "
            >
                <slot name="slot_5588_11518" v-if="visible_5586_123">
                    <Circle
                        id="5588_11518"
                        class="Pixso-instance-5588_11518"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <div id="5588_11519" class="Pixso-frame-5588_11519">
                    <slot name="slot_5588_11520" v-if="visible_5586_119">
                        <Dot
                            id="5588_11520"
                            class="Pixso-instance-5588_11520"
                            Size="sm"
                        />
                    </slot>
                    <slot name="slot_5588_11521">
                        <p
                            id="5588_11521"
                            class="Pixso-paragraph-5588_11521 fill-gray0-white-67_3285-paragraph text-text-smsemibold-423_3209"
                        >
                            {{ text_5588_129 ?? "Label" }}
                        </p>
                    </slot>
                </div>
                <slot name="slot_5588_11522" v-if="visible_5586_121">
                    <Check
                        id="5588_11522"
                        class="Pixso-instance-5588_11522"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
            </div>
            <div
                id="5588_13180"
                class="Pixso-symbol-5588_13180 fill-gray60-83_2722"
                v-if="
                    Size === 'md' &&
                    Color === 'Gray' &&
                    Hierarchy === 'Primary' &&
                    State === 'Hover'
                "
            >
                <slot name="slot_5588_13181" v-if="visible_5586_123">
                    <Circle
                        id="5588_13181"
                        class="Pixso-instance-5588_13181"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <div id="5588_13182" class="Pixso-frame-5588_13182">
                    <slot name="slot_5588_13183" v-if="visible_5586_119">
                        <Dot
                            id="5588_13183"
                            class="Pixso-instance-5588_13183"
                            Size="sm"
                        />
                    </slot>
                    <slot name="slot_5588_13184">
                        <p
                            id="5588_13184"
                            class="Pixso-paragraph-5588_13184 fill-gray0-white-67_3285-paragraph text-text-smsemibold-423_3209"
                        >
                            {{ text_5588_129 ?? "Label" }}
                        </p>
                    </slot>
                </div>
                <slot name="slot_5588_13185" v-if="visible_5586_121">
                    <Check
                        id="5588_13185"
                        class="Pixso-instance-5588_13185"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
            </div>
            <div
                id="5588_13909"
                class="Pixso-symbol-5588_13909 fill-gray20-36_1844"
                v-if="
                    Size === 'lg' &&
                    Color === 'Gray' &&
                    Hierarchy === 'Primary' &&
                    State === 'Disabled'
                "
            >
                <slot name="slot_5588_13910" v-if="visible_5586_123">
                    <Circle
                        id="5588_13910"
                        class="Pixso-instance-5588_13910"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <div id="5588_13911" class="Pixso-frame-5588_13911">
                    <slot name="slot_5588_13912" v-if="visible_5586_119">
                        <Dot
                            id="5588_13912"
                            class="Pixso-instance-5588_13912"
                            Size="sm"
                        />
                    </slot>
                    <slot name="slot_5588_13913">
                        <p
                            id="5588_13913"
                            class="Pixso-paragraph-5588_13913 fill-gray40-83_2714-paragraph text-text-smsemibold-423_3209"
                        >
                            {{ text_5588_129 ?? "Label" }}
                        </p>
                    </slot>
                </div>
                <slot name="slot_5588_13914" v-if="visible_5586_121">
                    <Check
                        id="5588_13914"
                        class="Pixso-instance-5588_13914"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
            </div>
            <div
                id="5588_13186"
                class="Pixso-symbol-5588_13186 fill-gray10-83_2713"
                v-if="
                    Size === 'md' &&
                    Color === 'Gray' &&
                    Hierarchy === 'Secondary' &&
                    State === 'Hover'
                "
            >
                <slot name="slot_5588_13187" v-if="visible_5586_123">
                    <Circle
                        id="5588_13187"
                        class="Pixso-instance-5588_13187"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <div id="5588_13188" class="Pixso-frame-5588_13188">
                    <slot name="slot_5588_13189" v-if="visible_5586_119">
                        <Dot
                            id="5588_13189"
                            class="Pixso-instance-5588_13189"
                            Size="sm"
                        />
                    </slot>
                    <slot name="slot_5588_13190">
                        <p
                            id="5588_13190"
                            class="Pixso-paragraph-5588_13190 fill-gray60-83_2722-paragraph text-text-smsemibold-423_3209"
                        >
                            {{ text_5588_129 ?? "Label" }}
                        </p>
                    </slot>
                </div>
                <slot name="slot_5588_13191" v-if="visible_5586_121">
                    <Check
                        id="5588_13191"
                        class="Pixso-instance-5588_13191"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
            </div>
            <div
                id="5588_11535"
                class="Pixso-symbol-5588_11535 fill-gray5-32_4120"
                v-if="
                    Size === 'lg' &&
                    Color === 'Gray' &&
                    Hierarchy === 'Secondary' &&
                    State === 'Default'
                "
            >
                <slot name="slot_5588_11536" v-if="visible_5586_123">
                    <Circle
                        id="5588_11536"
                        class="Pixso-instance-5588_11536"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <div id="5588_11537" class="Pixso-frame-5588_11537">
                    <slot name="slot_5588_11538" v-if="visible_5586_119">
                        <Dot
                            id="5588_11538"
                            class="Pixso-instance-5588_11538"
                            Size="sm"
                        />
                    </slot>
                    <slot name="slot_5588_11539">
                        <p
                            id="5588_11539"
                            class="Pixso-paragraph-5588_11539 fill-gray60-83_2722-paragraph text-text-smsemibold-423_3209"
                        >
                            {{ text_5588_129 ?? "Label" }}
                        </p>
                    </slot>
                </div>
                <slot name="slot_5588_11540" v-if="visible_5586_121">
                    <Check
                        id="5588_11540"
                        class="Pixso-instance-5588_11540"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
            </div>
            <div
                id="5588_13192"
                class="stroke-wrapper-5588_13192"
                v-if="
                    Size === 'md' &&
                    Color === 'Gray' &&
                    Hierarchy === 'Outlined' &&
                    State === 'Hover'
                "
            >
                <div class="Pixso-symbol-5588_13192 fill-gray5-32_4120">
                    <slot name="slot_5588_13193" v-if="visible_5586_123">
                        <Circle
                            id="5588_13193"
                            class="Pixso-instance-5588_13193"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                    <div id="5588_13194" class="Pixso-frame-5588_13194">
                        <slot name="slot_5588_13195" v-if="visible_5586_119">
                            <Dot
                                id="5588_13195"
                                class="Pixso-instance-5588_13195"
                                Size="sm"
                            />
                        </slot>
                        <slot name="slot_5588_13196">
                            <p
                                id="5588_13196"
                                class="Pixso-paragraph-5588_13196 fill-gray60-83_2722-paragraph text-text-smsemibold-423_3209"
                            >
                                {{ text_5588_129 ?? "Label" }}
                            </p>
                        </slot>
                    </div>
                    <slot name="slot_5588_13197" v-if="visible_5586_121">
                        <Check
                            id="5588_13197"
                            class="Pixso-instance-5588_13197"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div class="stroke-5588_13192 stroke-gray40-83_2714"></div>
            </div>
            <div
                id="5588_13915"
                class="Pixso-symbol-5588_13915 fill-gray5-32_4120"
                v-if="
                    Size === 'lg' &&
                    Color === 'Gray' &&
                    Hierarchy === 'Secondary' &&
                    State === 'Disabled'
                "
            >
                <slot name="slot_5588_13916" v-if="visible_5586_123">
                    <Circle
                        id="5588_13916"
                        class="Pixso-instance-5588_13916"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <div id="5588_13917" class="Pixso-frame-5588_13917">
                    <slot name="slot_5588_13918" v-if="visible_5586_119">
                        <Dot
                            id="5588_13918"
                            class="Pixso-instance-5588_13918"
                            Size="sm"
                        />
                    </slot>
                    <slot name="slot_5588_13919">
                        <p
                            id="5588_13919"
                            class="Pixso-paragraph-5588_13919 fill-gray30-35_1481-paragraph text-text-smsemibold-423_3209"
                        >
                            {{ text_5588_129 ?? "Label" }}
                        </p>
                    </slot>
                </div>
                <slot name="slot_5588_13920" v-if="visible_5586_121">
                    <Check
                        id="5588_13920"
                        class="Pixso-instance-5588_13920"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
            </div>
            <div
                id="5588_13198"
                class="Pixso-symbol-5588_13198 fill-destructive60-438_3719"
                v-if="
                    Size === 'sm' &&
                    Color === 'Destructive' &&
                    Hierarchy === 'Primary' &&
                    State === 'Hover'
                "
            >
                <slot name="slot_5588_13199" v-if="visible_5586_123">
                    <Circle
                        id="5588_13199"
                        class="Pixso-instance-5588_13199"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <div id="5588_13200" class="Pixso-frame-5588_13200">
                    <slot name="slot_5588_13201" v-if="visible_5586_119">
                        <Dot
                            id="5588_13201"
                            class="Pixso-instance-5588_13201"
                            Size="sm"
                        />
                    </slot>
                    <slot name="slot_5588_13202">
                        <p
                            id="5588_13202"
                            class="Pixso-paragraph-5588_13202 fill-gray0-white-67_3285-paragraph text-text-xssemibold-439_9521"
                        >
                            {{ text_5588_129 ?? "Label" }}
                        </p>
                    </slot>
                </div>
                <slot name="slot_5588_13203" v-if="visible_5586_121">
                    <Check
                        id="5588_13203"
                        class="Pixso-instance-5588_13203"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
            </div>
            <div
                id="5588_11541"
                class="stroke-wrapper-5588_11541"
                v-if="
                    Size === 'lg' &&
                    Color === 'Gray' &&
                    Hierarchy === 'Outlined' &&
                    State === 'Default'
                "
            >
                <div class="Pixso-symbol-5588_11541">
                    <slot name="slot_5588_11542" v-if="visible_5586_123">
                        <Circle
                            id="5588_11542"
                            class="Pixso-instance-5588_11542"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                    <div id="5588_11543" class="Pixso-frame-5588_11543">
                        <slot name="slot_5588_11544" v-if="visible_5586_119">
                            <Dot
                                id="5588_11544"
                                class="Pixso-instance-5588_11544"
                                Size="sm"
                            />
                        </slot>
                        <slot name="slot_5588_11545">
                            <p
                                id="5588_11545"
                                class="Pixso-paragraph-5588_11545 fill-gray60-83_2722-paragraph text-text-smsemibold-423_3209"
                            >
                                {{ text_5588_129 ?? "Label" }}
                            </p>
                        </slot>
                    </div>
                    <slot name="slot_5588_11546" v-if="visible_5586_121">
                        <Check
                            id="5588_11546"
                            class="Pixso-instance-5588_11546"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div class="stroke-5588_11541 stroke-gray30-35_1481"></div>
            </div>
            <div
                id="5588_13204"
                class="Pixso-symbol-5588_13204 fill-warning60-438_3718"
                v-if="
                    Size === 'sm' &&
                    Color === 'Warning' &&
                    Hierarchy === 'Primary' &&
                    State === 'Hover'
                "
            >
                <slot name="slot_5588_13205" v-if="visible_5586_123">
                    <Circle
                        id="5588_13205"
                        class="Pixso-instance-5588_13205"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <div id="5588_13206" class="Pixso-frame-5588_13206">
                    <slot name="slot_5588_13207" v-if="visible_5586_119">
                        <Dot
                            id="5588_13207"
                            class="Pixso-instance-5588_13207"
                            Size="sm"
                        />
                    </slot>
                    <slot name="slot_5588_13208">
                        <p
                            id="5588_13208"
                            class="Pixso-paragraph-5588_13208 fill-gray0-white-67_3285-paragraph text-text-xssemibold-439_9521"
                        >
                            {{ text_5588_129 ?? "Label" }}
                        </p>
                    </slot>
                </div>
                <slot name="slot_5588_13209" v-if="visible_5586_121">
                    <Check
                        id="5588_13209"
                        class="Pixso-instance-5588_13209"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
            </div>
            <div
                id="5588_13921"
                class="stroke-wrapper-5588_13921"
                v-if="
                    Size === 'lg' &&
                    Color === 'Gray' &&
                    Hierarchy === 'Outlined' &&
                    State === 'Disabled'
                "
            >
                <div class="Pixso-symbol-5588_13921">
                    <slot name="slot_5588_13922" v-if="visible_5586_123">
                        <Circle
                            id="5588_13922"
                            class="Pixso-instance-5588_13922"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                    <div id="5588_13923" class="Pixso-frame-5588_13923">
                        <slot name="slot_5588_13924" v-if="visible_5586_119">
                            <Dot
                                id="5588_13924"
                                class="Pixso-instance-5588_13924"
                                Size="sm"
                            />
                        </slot>
                        <slot name="slot_5588_13925">
                            <p
                                id="5588_13925"
                                class="Pixso-paragraph-5588_13925 fill-gray30-35_1481-paragraph text-text-smsemibold-423_3209"
                            >
                                {{ text_5588_129 ?? "Label" }}
                            </p>
                        </slot>
                    </div>
                    <slot name="slot_5588_13926" v-if="visible_5586_121">
                        <Check
                            id="5588_13926"
                            class="Pixso-instance-5588_13926"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div class="stroke-5588_13921 stroke-gray30-35_1481"></div>
            </div>
            <div
                id="5588_13210"
                class="Pixso-symbol-5588_13210 fill-success60-1636_81206"
                v-if="
                    Size === 'sm' &&
                    Color === 'Success' &&
                    Hierarchy === 'Primary' &&
                    State === 'Hover'
                "
            >
                <slot name="slot_5588_13211" v-if="visible_5586_123">
                    <Circle
                        id="5588_13211"
                        class="Pixso-instance-5588_13211"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <div id="5588_13212" class="Pixso-frame-5588_13212">
                    <slot name="slot_5588_13213" v-if="visible_5586_119">
                        <Dot
                            id="5588_13213"
                            class="Pixso-instance-5588_13213"
                            Size="sm"
                        />
                    </slot>
                    <slot name="slot_5588_13214">
                        <p
                            id="5588_13214"
                            class="Pixso-paragraph-5588_13214 fill-gray0-white-67_3285-paragraph text-text-xssemibold-439_9521"
                        >
                            {{ text_5588_129 ?? "Label" }}
                        </p>
                    </slot>
                </div>
                <slot name="slot_5588_13215" v-if="visible_5586_121">
                    <Check
                        id="5588_13215"
                        class="Pixso-instance-5588_13215"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
            </div>
            <div
                id="5494_4827"
                class="Pixso-symbol-5494_4827 fill-brand60-1257_33467"
                v-if="
                    Size === 'sm' &&
                    Color === 'Brand' &&
                    Hierarchy === 'Primary' &&
                    State === 'Default'
                "
            >
                <slot name="slot_5494_4828" v-if="visible_5586_123">
                    <Circle
                        id="5494_4828"
                        class="Pixso-instance-5494_4828"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <div id="5588_11214" class="Pixso-frame-5588_11214">
                    <slot name="slot_5586_11117" v-if="visible_5586_119">
                        <Dot
                            id="5586_11117"
                            class="Pixso-instance-5586_11117"
                            Size="sm"
                        />
                    </slot>
                    <slot name="slot_5494_4829">
                        <p
                            id="5494_4829"
                            class="Pixso-paragraph-5494_4829 fill-gray0-white-67_3285-paragraph text-text-xssemibold-439_9521"
                        >
                            {{ text_5588_129 ?? "Label" }}
                        </p>
                    </slot>
                </div>
                <slot name="slot_5586_11112" v-if="visible_5586_121">
                    <Check
                        id="5586_11112"
                        class="Pixso-instance-5586_11112"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
            </div>
            <div
                id="5588_13216"
                class="Pixso-symbol-5588_13216 fill-destructive10-423_3221"
                v-if="
                    Size === 'sm' &&
                    Color === 'Destructive' &&
                    Hierarchy === 'Secondary' &&
                    State === 'Hover'
                "
            >
                <slot name="slot_5588_13217" v-if="visible_5586_123">
                    <Circle
                        id="5588_13217"
                        class="Pixso-instance-5588_13217"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <div id="5588_13218" class="Pixso-frame-5588_13218">
                    <slot name="slot_5588_13219" v-if="visible_5586_119">
                        <Dot
                            id="5588_13219"
                            class="Pixso-instance-5588_13219"
                            Size="sm"
                        />
                    </slot>
                    <slot name="slot_5588_13220">
                        <p
                            id="5588_13220"
                            class="Pixso-paragraph-5588_13220 fill-destructive50-423_3219-paragraph text-text-xssemibold-439_9521"
                        >
                            {{ text_5588_129 ?? "Label" }}
                        </p>
                    </slot>
                </div>
                <slot name="slot_5588_13221" v-if="visible_5586_121">
                    <Check
                        id="5588_13221"
                        class="Pixso-instance-5588_13221"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
            </div>
            <div
                id="5588_13927"
                class="Pixso-symbol-5588_13927 fill-brand20-1257_33462"
                v-if="
                    Size === 'sm' &&
                    Color === 'Brand' &&
                    Hierarchy === 'Primary' &&
                    State === 'Disabled'
                "
            >
                <slot name="slot_5588_13928" v-if="visible_5586_123">
                    <Circle
                        id="5588_13928"
                        class="Pixso-instance-5588_13928"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <div id="5588_13929" class="Pixso-frame-5588_13929">
                    <slot name="slot_5588_13930" v-if="visible_5586_119">
                        <Dot
                            id="5588_13930"
                            class="Pixso-instance-5588_13930"
                            Size="sm"
                        />
                    </slot>
                    <slot name="slot_5588_13931">
                        <p
                            id="5588_13931"
                            class="Pixso-paragraph-5588_13931 fill-brand40-1257_33464-paragraph text-text-xssemibold-439_9521"
                        >
                            {{ text_5588_129 ?? "Label" }}
                        </p>
                    </slot>
                </div>
                <slot name="slot_5588_13932" v-if="visible_5586_121">
                    <Check
                        id="5588_13932"
                        class="Pixso-instance-5588_13932"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
            </div>
            <div
                id="5588_13222"
                class="Pixso-symbol-5588_13222 fill-warning10-423_3215"
                v-if="
                    Size === 'sm' &&
                    Color === 'Warning' &&
                    Hierarchy === 'Secondary' &&
                    State === 'Hover'
                "
            >
                <slot name="slot_5588_13223" v-if="visible_5586_123">
                    <Circle
                        id="5588_13223"
                        class="Pixso-instance-5588_13223"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <div id="5588_13224" class="Pixso-frame-5588_13224">
                    <slot name="slot_5588_13225" v-if="visible_5586_119">
                        <Dot
                            id="5588_13225"
                            class="Pixso-instance-5588_13225"
                            Size="sm"
                        />
                    </slot>
                    <slot name="slot_5588_13226">
                        <p
                            id="5588_13226"
                            class="Pixso-paragraph-5588_13226 fill-warning50-423_3213-paragraph text-text-xssemibold-439_9521"
                        >
                            {{ text_5588_129 ?? "Label" }}
                        </p>
                    </slot>
                </div>
                <slot name="slot_5588_13227" v-if="visible_5586_121">
                    <Check
                        id="5588_13227"
                        class="Pixso-instance-5588_13227"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
            </div>
            <div
                id="5588_11358"
                class="Pixso-symbol-5588_11358 fill-brand5-1257_33460"
                v-if="
                    Size === 'sm' &&
                    Color === 'Brand' &&
                    Hierarchy === 'Secondary' &&
                    State === 'Default'
                "
            >
                <slot name="slot_5588_11359" v-if="visible_5586_123">
                    <Circle
                        id="5588_11359"
                        class="Pixso-instance-5588_11359"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <div id="5588_11360" class="Pixso-frame-5588_11360">
                    <slot name="slot_5588_11361" v-if="visible_5586_119">
                        <Dot
                            id="5588_11361"
                            class="Pixso-instance-5588_11361"
                            Size="sm"
                        />
                    </slot>
                    <slot name="slot_5588_11362">
                        <p
                            id="5588_11362"
                            class="Pixso-paragraph-5588_11362 fill-brand60-1257_33467-paragraph text-text-xssemibold-439_9521"
                        >
                            {{ text_5588_129 ?? "Label" }}
                        </p>
                    </slot>
                </div>
                <slot name="slot_5588_11363" v-if="visible_5586_121">
                    <Check
                        id="5588_11363"
                        class="Pixso-instance-5588_11363"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
            </div>
            <div
                id="5588_13228"
                class="Pixso-symbol-5588_13228 fill-success10-1636_81201"
                v-if="
                    Size === 'sm' &&
                    Color === 'Success' &&
                    Hierarchy === 'Secondary' &&
                    State === 'Hover'
                "
            >
                <slot name="slot_5588_13229" v-if="visible_5586_123">
                    <Circle
                        id="5588_13229"
                        class="Pixso-instance-5588_13229"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <div id="5588_13230" class="Pixso-frame-5588_13230">
                    <slot name="slot_5588_13231" v-if="visible_5586_119">
                        <Dot
                            id="5588_13231"
                            class="Pixso-instance-5588_13231"
                            Size="sm"
                        />
                    </slot>
                    <slot name="slot_5588_13232">
                        <p
                            id="5588_13232"
                            class="Pixso-paragraph-5588_13232 fill-success50-1636_81205-paragraph text-text-xssemibold-439_9521"
                        >
                            {{ text_5588_129 ?? "Label" }}
                        </p>
                    </slot>
                </div>
                <slot name="slot_5588_13233" v-if="visible_5586_121">
                    <Check
                        id="5588_13233"
                        class="Pixso-instance-5588_13233"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
            </div>
            <div
                id="5588_13933"
                class="Pixso-symbol-5588_13933 fill-brand5-1257_33460"
                v-if="
                    Size === 'sm' &&
                    Color === 'Brand' &&
                    Hierarchy === 'Secondary' &&
                    State === 'Disabled'
                "
            >
                <slot name="slot_5588_13934" v-if="visible_5586_123">
                    <Circle
                        id="5588_13934"
                        class="Pixso-instance-5588_13934"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <div id="5588_13935" class="Pixso-frame-5588_13935">
                    <slot name="slot_5588_13936" v-if="visible_5586_119">
                        <Dot
                            id="5588_13936"
                            class="Pixso-instance-5588_13936"
                            Size="sm"
                        />
                    </slot>
                    <slot name="slot_5588_13937">
                        <p
                            id="5588_13937"
                            class="Pixso-paragraph-5588_13937 fill-brand30-1257_33463-paragraph text-text-xssemibold-439_9521"
                        >
                            {{ text_5588_129 ?? "Label" }}
                        </p>
                    </slot>
                </div>
                <slot name="slot_5588_13938" v-if="visible_5586_121">
                    <Check
                        id="5588_13938"
                        class="Pixso-instance-5588_13938"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
            </div>
            <div
                id="5588_13234"
                class="stroke-wrapper-5588_13234"
                v-if="
                    Size === 'sm' &&
                    Color === 'Destructive' &&
                    Hierarchy === 'Outlined' &&
                    State === 'Hover'
                "
            >
                <div class="Pixso-symbol-5588_13234 fill-destructive5-83_2719">
                    <slot name="slot_5588_13235" v-if="visible_5586_123">
                        <Circle
                            id="5588_13235"
                            class="Pixso-instance-5588_13235"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                    <div id="5588_13236" class="Pixso-frame-5588_13236">
                        <slot name="slot_5588_13237" v-if="visible_5586_119">
                            <Dot
                                id="5588_13237"
                                class="Pixso-instance-5588_13237"
                                Size="sm"
                            />
                        </slot>
                        <slot name="slot_5588_13238">
                            <p
                                id="5588_13238"
                                class="Pixso-paragraph-5588_13238 fill-destructive50-423_3219-paragraph text-text-xssemibold-439_9521"
                            >
                                {{ text_5588_129 ?? "Label" }}
                            </p>
                        </slot>
                    </div>
                    <slot name="slot_5588_13239" v-if="visible_5586_121">
                        <Check
                            id="5588_13239"
                            class="Pixso-instance-5588_13239"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div
                    class="stroke-5588_13234 stroke-destructive50-423_3219"
                ></div>
            </div>
            <div
                id="5588_11421"
                class="stroke-wrapper-5588_11421"
                v-if="
                    Size === 'sm' &&
                    Color === 'Brand' &&
                    Hierarchy === 'Outlined' &&
                    State === 'Default'
                "
            >
                <div class="Pixso-symbol-5588_11421">
                    <slot name="slot_5588_11422" v-if="visible_5586_123">
                        <Circle
                            id="5588_11422"
                            class="Pixso-instance-5588_11422"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                    <div id="5588_11423" class="Pixso-frame-5588_11423">
                        <slot name="slot_5588_11424" v-if="visible_5586_119">
                            <Dot
                                id="5588_11424"
                                class="Pixso-instance-5588_11424"
                                Size="sm"
                            />
                        </slot>
                        <slot name="slot_5588_11425">
                            <p
                                id="5588_11425"
                                class="Pixso-paragraph-5588_11425 fill-brand60-1257_33467-paragraph text-text-xssemibold-439_9521"
                            >
                                {{ text_5588_129 ?? "Label" }}
                            </p>
                        </slot>
                    </div>
                    <slot name="slot_5588_11426" v-if="visible_5586_121">
                        <Check
                            id="5588_11426"
                            class="Pixso-instance-5588_11426"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div class="stroke-5588_11421 stroke-brand60-1257_33467"></div>
            </div>
            <div
                id="5588_13240"
                class="stroke-wrapper-5588_13240"
                v-if="
                    Size === 'sm' &&
                    Color === 'Warning' &&
                    Hierarchy === 'Outlined' &&
                    State === 'Hover'
                "
            >
                <div class="Pixso-symbol-5588_13240 fill-warning5-83_2717">
                    <slot name="slot_5588_13241" v-if="visible_5586_123">
                        <Circle
                            id="5588_13241"
                            class="Pixso-instance-5588_13241"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                    <div id="5588_13242" class="Pixso-frame-5588_13242">
                        <slot name="slot_5588_13243" v-if="visible_5586_119">
                            <Dot
                                id="5588_13243"
                                class="Pixso-instance-5588_13243"
                                Size="sm"
                            />
                        </slot>
                        <slot name="slot_5588_13244">
                            <p
                                id="5588_13244"
                                class="Pixso-paragraph-5588_13244 fill-warning50-423_3213-paragraph text-text-xssemibold-439_9521"
                            >
                                {{ text_5588_129 ?? "Label" }}
                            </p>
                        </slot>
                    </div>
                    <slot name="slot_5588_13245" v-if="visible_5586_121">
                        <Check
                            id="5588_13245"
                            class="Pixso-instance-5588_13245"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div class="stroke-5588_13240 stroke-warning50-423_3213"></div>
            </div>
            <div
                id="5588_13939"
                class="stroke-wrapper-5588_13939"
                v-if="
                    Size === 'sm' &&
                    Color === 'Brand' &&
                    Hierarchy === 'Outlined' &&
                    State === 'Disabled'
                "
            >
                <div class="Pixso-symbol-5588_13939">
                    <slot name="slot_5588_13940" v-if="visible_5586_123">
                        <Circle
                            id="5588_13940"
                            class="Pixso-instance-5588_13940"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                    <div id="5588_13941" class="Pixso-frame-5588_13941">
                        <slot name="slot_5588_13942" v-if="visible_5586_119">
                            <Dot
                                id="5588_13942"
                                class="Pixso-instance-5588_13942"
                                Size="sm"
                            />
                        </slot>
                        <slot name="slot_5588_13943">
                            <p
                                id="5588_13943"
                                class="Pixso-paragraph-5588_13943 fill-brand30-1257_33463-paragraph text-text-xssemibold-439_9521"
                            >
                                {{ text_5588_129 ?? "Label" }}
                            </p>
                        </slot>
                    </div>
                    <slot name="slot_5588_13944" v-if="visible_5586_121">
                        <Check
                            id="5588_13944"
                            class="Pixso-instance-5588_13944"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div class="stroke-5588_13939 stroke-brand30-1257_33463"></div>
            </div>
            <div
                id="5588_13246"
                class="stroke-wrapper-5588_13246"
                v-if="
                    Size === 'sm' &&
                    Color === 'Success' &&
                    Hierarchy === 'Outlined' &&
                    State === 'Hover'
                "
            >
                <div class="Pixso-symbol-5588_13246 fill-success5-1636_81199">
                    <slot name="slot_5588_13247" v-if="visible_5586_123">
                        <Circle
                            id="5588_13247"
                            class="Pixso-instance-5588_13247"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                    <div id="5588_13248" class="Pixso-frame-5588_13248">
                        <slot name="slot_5588_13249" v-if="visible_5586_119">
                            <Dot
                                id="5588_13249"
                                class="Pixso-instance-5588_13249"
                                Size="sm"
                            />
                        </slot>
                        <slot name="slot_5588_13250">
                            <p
                                id="5588_13250"
                                class="Pixso-paragraph-5588_13250 fill-success50-1636_81205-paragraph text-text-xssemibold-439_9521"
                            >
                                {{ text_5588_129 ?? "Label" }}
                            </p>
                        </slot>
                    </div>
                    <slot name="slot_5588_13251" v-if="visible_5586_121">
                        <Check
                            id="5588_13251"
                            class="Pixso-instance-5588_13251"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div
                    class="stroke-5588_13246 stroke-success50-1636_81205"
                ></div>
            </div>
            <div
                id="5588_11859"
                class="Pixso-symbol-5588_11859 fill-destructive50-423_3219"
                v-if="
                    Size === 'md' &&
                    Color === 'Destructive' &&
                    Hierarchy === 'Primary' &&
                    State === 'Default'
                "
            >
                <slot name="slot_5588_11860" v-if="visible_5586_123">
                    <Circle
                        id="5588_11860"
                        class="Pixso-instance-5588_11860"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <div id="5588_11861" class="Pixso-frame-5588_11861">
                    <slot name="slot_5588_11862" v-if="visible_5586_119">
                        <Dot
                            id="5588_11862"
                            class="Pixso-instance-5588_11862"
                            Size="sm"
                        />
                    </slot>
                    <slot name="slot_5588_11863">
                        <p
                            id="5588_11863"
                            class="Pixso-paragraph-5588_11863 fill-gray0-white-67_3285-paragraph text-text-smsemibold-423_3209"
                        >
                            {{ text_5588_129 ?? "Label" }}
                        </p>
                    </slot>
                </div>
                <slot name="slot_5588_11864" v-if="visible_5586_121">
                    <Check
                        id="5588_11864"
                        class="Pixso-instance-5588_11864"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
            </div>
            <div
                id="5588_13252"
                class="Pixso-symbol-5588_13252 fill-gray60-83_2722"
                v-if="
                    Size === 'sm' &&
                    Color === 'Gray' &&
                    Hierarchy === 'Primary' &&
                    State === 'Hover'
                "
            >
                <slot name="slot_5588_13253" v-if="visible_5586_123">
                    <Circle
                        id="5588_13253"
                        class="Pixso-instance-5588_13253"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <div id="5588_13254" class="Pixso-frame-5588_13254">
                    <slot name="slot_5588_13255" v-if="visible_5586_119">
                        <Dot
                            id="5588_13255"
                            class="Pixso-instance-5588_13255"
                            Size="sm"
                        />
                    </slot>
                    <slot name="slot_5588_13256">
                        <p
                            id="5588_13256"
                            class="Pixso-paragraph-5588_13256 fill-gray0-white-67_3285-paragraph text-text-xssemibold-439_9521"
                        >
                            {{ text_5588_129 ?? "Label" }}
                        </p>
                    </slot>
                </div>
                <slot name="slot_5588_13257" v-if="visible_5586_121">
                    <Check
                        id="5588_13257"
                        class="Pixso-instance-5588_13257"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
            </div>
            <div
                id="5588_13945"
                class="Pixso-symbol-5588_13945 fill-destructive20-438_3720"
                v-if="
                    Size === 'md' &&
                    Color === 'Destructive' &&
                    Hierarchy === 'Primary' &&
                    State === 'Disabled'
                "
            >
                <slot name="slot_5588_13946" v-if="visible_5586_123">
                    <Circle
                        id="5588_13946"
                        class="Pixso-instance-5588_13946"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <div id="5588_13947" class="Pixso-frame-5588_13947">
                    <slot name="slot_5588_13948" v-if="visible_5586_119">
                        <Dot
                            id="5588_13948"
                            class="Pixso-instance-5588_13948"
                            Size="sm"
                        />
                    </slot>
                    <slot name="slot_5588_13949">
                        <p
                            id="5588_13949"
                            class="Pixso-paragraph-5588_13949 fill-destructive40-32_4110-paragraph text-text-smsemibold-423_3209"
                        >
                            {{ text_5588_129 ?? "Label" }}
                        </p>
                    </slot>
                </div>
                <slot name="slot_5588_13950" v-if="visible_5586_121">
                    <Check
                        id="5588_13950"
                        class="Pixso-instance-5588_13950"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
            </div>
            <div
                id="5588_13258"
                class="Pixso-symbol-5588_13258 fill-gray10-83_2713"
                v-if="
                    Size === 'sm' &&
                    Color === 'Gray' &&
                    Hierarchy === 'Secondary' &&
                    State === 'Hover'
                "
            >
                <slot name="slot_5588_13259" v-if="visible_5586_123">
                    <Circle
                        id="5588_13259"
                        class="Pixso-instance-5588_13259"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <div id="5588_13260" class="Pixso-frame-5588_13260">
                    <slot name="slot_5588_13261" v-if="visible_5586_119">
                        <Dot
                            id="5588_13261"
                            class="Pixso-instance-5588_13261"
                            Size="sm"
                        />
                    </slot>
                    <slot name="slot_5588_13262">
                        <p
                            id="5588_13262"
                            class="Pixso-paragraph-5588_13262 fill-gray60-83_2722-paragraph text-text-xssemibold-439_9521"
                        >
                            {{ text_5588_129 ?? "Label" }}
                        </p>
                    </slot>
                </div>
                <slot name="slot_5588_13263" v-if="visible_5586_121">
                    <Check
                        id="5588_13263"
                        class="Pixso-instance-5588_13263"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
            </div>
            <div
                id="5588_12030"
                class="Pixso-symbol-5588_12030 fill-warning50-423_3213"
                v-if="
                    Size === 'md' &&
                    Color === 'Warning' &&
                    Hierarchy === 'Primary' &&
                    State === 'Default'
                "
            >
                <slot name="slot_5588_12031" v-if="visible_5586_123">
                    <Circle
                        id="5588_12031"
                        class="Pixso-instance-5588_12031"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <div id="5588_12032" class="Pixso-frame-5588_12032">
                    <slot name="slot_5588_12033" v-if="visible_5586_119">
                        <Dot
                            id="5588_12033"
                            class="Pixso-instance-5588_12033"
                            Size="sm"
                        />
                    </slot>
                    <slot name="slot_5588_12034">
                        <p
                            id="5588_12034"
                            class="Pixso-paragraph-5588_12034 fill-gray0-white-67_3285-paragraph text-text-smsemibold-423_3209"
                        >
                            {{ text_5588_129 ?? "Label" }}
                        </p>
                    </slot>
                </div>
                <slot name="slot_5588_12035" v-if="visible_5586_121">
                    <Check
                        id="5588_12035"
                        class="Pixso-instance-5588_12035"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
            </div>
            <div
                id="5588_13264"
                class="stroke-wrapper-5588_13264"
                v-if="
                    Size === 'sm' &&
                    Color === 'Gray' &&
                    Hierarchy === 'Outlined' &&
                    State === 'Hover'
                "
            >
                <div class="Pixso-symbol-5588_13264 fill-gray5-32_4120">
                    <slot name="slot_5588_13265" v-if="visible_5586_123">
                        <Circle
                            id="5588_13265"
                            class="Pixso-instance-5588_13265"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                    <div id="5588_13266" class="Pixso-frame-5588_13266">
                        <slot name="slot_5588_13267" v-if="visible_5586_119">
                            <Dot
                                id="5588_13267"
                                class="Pixso-instance-5588_13267"
                                Size="sm"
                            />
                        </slot>
                        <slot name="slot_5588_13268">
                            <p
                                id="5588_13268"
                                class="Pixso-paragraph-5588_13268 fill-gray60-83_2722-paragraph text-text-xssemibold-439_9521"
                            >
                                {{ text_5588_129 ?? "Label" }}
                            </p>
                        </slot>
                    </div>
                    <slot name="slot_5588_13269" v-if="visible_5586_121">
                        <Check
                            id="5588_13269"
                            class="Pixso-instance-5588_13269"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div class="stroke-5588_13264 stroke-gray40-83_2714"></div>
            </div>
            <div
                id="5588_13951"
                class="Pixso-symbol-5588_13951 fill-warning20-428_4551"
                v-if="
                    Size === 'md' &&
                    Color === 'Warning' &&
                    Hierarchy === 'Primary' &&
                    State === 'Disabled'
                "
            >
                <slot name="slot_5588_13952" v-if="visible_5586_123">
                    <Circle
                        id="5588_13952"
                        class="Pixso-instance-5588_13952"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <div id="5588_13953" class="Pixso-frame-5588_13953">
                    <slot name="slot_5588_13954" v-if="visible_5586_119">
                        <Dot
                            id="5588_13954"
                            class="Pixso-instance-5588_13954"
                            Size="sm"
                        />
                    </slot>
                    <slot name="slot_5588_13955">
                        <p
                            id="5588_13955"
                            class="Pixso-paragraph-5588_13955 fill-warning40-428_4549-paragraph text-text-smsemibold-423_3209"
                        >
                            {{ text_5588_129 ?? "Label" }}
                        </p>
                    </slot>
                </div>
                <slot name="slot_5588_13956" v-if="visible_5586_121">
                    <Check
                        id="5588_13956"
                        class="Pixso-instance-5588_13956"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
            </div>
            <div
                id="5588_12192"
                class="Pixso-symbol-5588_12192 fill-success50-1636_81205"
                v-if="
                    Size === 'md' &&
                    Color === 'Success' &&
                    Hierarchy === 'Primary' &&
                    State === 'Default'
                "
            >
                <slot name="slot_5588_12193" v-if="visible_5586_123">
                    <Circle
                        id="5588_12193"
                        class="Pixso-instance-5588_12193"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <div id="5588_12194" class="Pixso-frame-5588_12194">
                    <slot name="slot_5588_12195" v-if="visible_5586_119">
                        <Dot
                            id="5588_12195"
                            class="Pixso-instance-5588_12195"
                            Size="sm"
                        />
                    </slot>
                    <slot name="slot_5588_12196">
                        <p
                            id="5588_12196"
                            class="Pixso-paragraph-5588_12196 fill-gray0-white-67_3285-paragraph text-text-smsemibold-423_3209"
                        >
                            {{ text_5588_129 ?? "Label" }}
                        </p>
                    </slot>
                </div>
                <slot name="slot_5588_12197" v-if="visible_5586_121">
                    <Check
                        id="5588_12197"
                        class="Pixso-instance-5588_12197"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
            </div>
            <div
                id="5588_13957"
                class="Pixso-symbol-5588_13957 fill-success20-1636_81202"
                v-if="
                    Size === 'md' &&
                    Color === 'Success' &&
                    Hierarchy === 'Primary' &&
                    State === 'Disabled'
                "
            >
                <slot name="slot_5588_13958" v-if="visible_5586_123">
                    <Circle
                        id="5588_13958"
                        class="Pixso-instance-5588_13958"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <div id="5588_13959" class="Pixso-frame-5588_13959">
                    <slot name="slot_5588_13960" v-if="visible_5586_119">
                        <Dot
                            id="5588_13960"
                            class="Pixso-instance-5588_13960"
                            Size="sm"
                        />
                    </slot>
                    <slot name="slot_5588_13961">
                        <p
                            id="5588_13961"
                            class="Pixso-paragraph-5588_13961 fill-success40-1636_81204-paragraph text-text-smsemibold-423_3209"
                        >
                            {{ text_5588_129 ?? "Label" }}
                        </p>
                    </slot>
                </div>
                <slot name="slot_5588_13962" v-if="visible_5586_121">
                    <Check
                        id="5588_13962"
                        class="Pixso-instance-5588_13962"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
            </div>
            <div
                id="5588_11865"
                class="Pixso-symbol-5588_11865 fill-destructive5-83_2719"
                v-if="
                    Size === 'md' &&
                    Color === 'Destructive' &&
                    Hierarchy === 'Secondary' &&
                    State === 'Default'
                "
            >
                <slot name="slot_5588_11866" v-if="visible_5586_123">
                    <Circle
                        id="5588_11866"
                        class="Pixso-instance-5588_11866"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <div id="5588_11867" class="Pixso-frame-5588_11867">
                    <slot name="slot_5588_11868" v-if="visible_5586_119">
                        <Dot
                            id="5588_11868"
                            class="Pixso-instance-5588_11868"
                            Size="sm"
                        />
                    </slot>
                    <slot name="slot_5588_11869">
                        <p
                            id="5588_11869"
                            class="Pixso-paragraph-5588_11869 fill-destructive50-423_3219-paragraph text-text-smsemibold-423_3209"
                        >
                            {{ text_5588_129 ?? "Label" }}
                        </p>
                    </slot>
                </div>
                <slot name="slot_5588_11870" v-if="visible_5586_121">
                    <Check
                        id="5588_11870"
                        class="Pixso-instance-5588_11870"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
            </div>
            <div
                id="5588_13963"
                class="Pixso-symbol-5588_13963 fill-destructive5-83_2719"
                v-if="
                    Size === 'md' &&
                    Color === 'Destructive' &&
                    Hierarchy === 'Secondary' &&
                    State === 'Disabled'
                "
            >
                <slot name="slot_5588_13964" v-if="visible_5586_123">
                    <Circle
                        id="5588_13964"
                        class="Pixso-instance-5588_13964"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <div id="5588_13965" class="Pixso-frame-5588_13965">
                    <slot name="slot_5588_13966" v-if="visible_5586_119">
                        <Dot
                            id="5588_13966"
                            class="Pixso-instance-5588_13966"
                            Size="sm"
                        />
                    </slot>
                    <slot name="slot_5588_13967">
                        <p
                            id="5588_13967"
                            class="Pixso-paragraph-5588_13967 fill-destructive30-423_3220-paragraph text-text-smsemibold-423_3209"
                        >
                            {{ text_5588_129 ?? "Label" }}
                        </p>
                    </slot>
                </div>
                <slot name="slot_5588_13968" v-if="visible_5586_121">
                    <Check
                        id="5588_13968"
                        class="Pixso-instance-5588_13968"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
            </div>
            <div
                id="5588_12036"
                class="Pixso-symbol-5588_12036 fill-warning5-83_2717"
                v-if="
                    Size === 'md' &&
                    Color === 'Warning' &&
                    Hierarchy === 'Secondary' &&
                    State === 'Default'
                "
            >
                <slot name="slot_5588_12037" v-if="visible_5586_123">
                    <Circle
                        id="5588_12037"
                        class="Pixso-instance-5588_12037"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <div id="5588_12038" class="Pixso-frame-5588_12038">
                    <slot name="slot_5588_12039" v-if="visible_5586_119">
                        <Dot
                            id="5588_12039"
                            class="Pixso-instance-5588_12039"
                            Size="sm"
                        />
                    </slot>
                    <slot name="slot_5588_12040">
                        <p
                            id="5588_12040"
                            class="Pixso-paragraph-5588_12040 fill-warning50-423_3213-paragraph text-text-smsemibold-423_3209"
                        >
                            {{ text_5588_129 ?? "Label" }}
                        </p>
                    </slot>
                </div>
                <slot name="slot_5588_12041" v-if="visible_5586_121">
                    <Check
                        id="5588_12041"
                        class="Pixso-instance-5588_12041"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
            </div>
            <div
                id="5588_13969"
                class="Pixso-symbol-5588_13969 fill-warning5-83_2717"
                v-if="
                    Size === 'md' &&
                    Color === 'Warning' &&
                    Hierarchy === 'Secondary' &&
                    State === 'Disabled'
                "
            >
                <slot name="slot_5588_13970" v-if="visible_5586_123">
                    <Circle
                        id="5588_13970"
                        class="Pixso-instance-5588_13970"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <div id="5588_13971" class="Pixso-frame-5588_13971">
                    <slot name="slot_5588_13972" v-if="visible_5586_119">
                        <Dot
                            id="5588_13972"
                            class="Pixso-instance-5588_13972"
                            Size="sm"
                        />
                    </slot>
                    <slot name="slot_5588_13973">
                        <p
                            id="5588_13973"
                            class="Pixso-paragraph-5588_13973 fill-warning30-32_4109-paragraph text-text-smsemibold-423_3209"
                        >
                            {{ text_5588_129 ?? "Label" }}
                        </p>
                    </slot>
                </div>
                <slot name="slot_5588_13974" v-if="visible_5586_121">
                    <Check
                        id="5588_13974"
                        class="Pixso-instance-5588_13974"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
            </div>
            <div
                id="5588_12198"
                class="Pixso-symbol-5588_12198 fill-success5-1636_81199"
                v-if="
                    Size === 'md' &&
                    Color === 'Success' &&
                    Hierarchy === 'Secondary' &&
                    State === 'Default'
                "
            >
                <slot name="slot_5588_12199" v-if="visible_5586_123">
                    <Circle
                        id="5588_12199"
                        class="Pixso-instance-5588_12199"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <div id="5588_12200" class="Pixso-frame-5588_12200">
                    <slot name="slot_5588_12201" v-if="visible_5586_119">
                        <Dot
                            id="5588_12201"
                            class="Pixso-instance-5588_12201"
                            Size="sm"
                        />
                    </slot>
                    <slot name="slot_5588_12202">
                        <p
                            id="5588_12202"
                            class="Pixso-paragraph-5588_12202 fill-success50-1636_81205-paragraph text-text-smsemibold-423_3209"
                        >
                            {{ text_5588_129 ?? "Label" }}
                        </p>
                    </slot>
                </div>
                <slot name="slot_5588_12203" v-if="visible_5586_121">
                    <Check
                        id="5588_12203"
                        class="Pixso-instance-5588_12203"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
            </div>
            <div
                id="5588_13975"
                class="Pixso-symbol-5588_13975 fill-success5-1636_81199"
                v-if="
                    Size === 'md' &&
                    Color === 'Success' &&
                    Hierarchy === 'Secondary' &&
                    State === 'Disabled'
                "
            >
                <slot name="slot_5588_13976" v-if="visible_5586_123">
                    <Circle
                        id="5588_13976"
                        class="Pixso-instance-5588_13976"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <div id="5588_13977" class="Pixso-frame-5588_13977">
                    <slot name="slot_5588_13978" v-if="visible_5586_119">
                        <Dot
                            id="5588_13978"
                            class="Pixso-instance-5588_13978"
                            Size="sm"
                        />
                    </slot>
                    <slot name="slot_5588_13979">
                        <p
                            id="5588_13979"
                            class="Pixso-paragraph-5588_13979 fill-success30-1636_81203-paragraph text-text-smsemibold-423_3209"
                        >
                            {{ text_5588_129 ?? "Label" }}
                        </p>
                    </slot>
                </div>
                <slot name="slot_5588_13980" v-if="visible_5586_121">
                    <Check
                        id="5588_13980"
                        class="Pixso-instance-5588_13980"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
            </div>
            <div
                id="5588_11871"
                class="stroke-wrapper-5588_11871"
                v-if="
                    Size === 'md' &&
                    Color === 'Destructive' &&
                    Hierarchy === 'Outlined' &&
                    State === 'Default'
                "
            >
                <div class="Pixso-symbol-5588_11871">
                    <slot name="slot_5588_11872" v-if="visible_5586_123">
                        <Circle
                            id="5588_11872"
                            class="Pixso-instance-5588_11872"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                    <div id="5588_11873" class="Pixso-frame-5588_11873">
                        <slot name="slot_5588_11874" v-if="visible_5586_119">
                            <Dot
                                id="5588_11874"
                                class="Pixso-instance-5588_11874"
                                Size="sm"
                            />
                        </slot>
                        <slot name="slot_5588_11875">
                            <p
                                id="5588_11875"
                                class="Pixso-paragraph-5588_11875 fill-destructive50-423_3219-paragraph text-text-smsemibold-423_3209"
                            >
                                {{ text_5588_129 ?? "Label" }}
                            </p>
                        </slot>
                    </div>
                    <slot name="slot_5588_11876" v-if="visible_5586_121">
                        <Check
                            id="5588_11876"
                            class="Pixso-instance-5588_11876"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div
                    class="stroke-5588_11871 stroke-destructive50-423_3219"
                ></div>
            </div>
            <div
                id="5588_13981"
                class="stroke-wrapper-5588_13981"
                v-if="
                    Size === 'md' &&
                    Color === 'Destructive' &&
                    Hierarchy === 'Outlined' &&
                    State === 'Disabled'
                "
            >
                <div class="Pixso-symbol-5588_13981">
                    <slot name="slot_5588_13982" v-if="visible_5586_123">
                        <Circle
                            id="5588_13982"
                            class="Pixso-instance-5588_13982"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                    <div id="5588_13983" class="Pixso-frame-5588_13983">
                        <slot name="slot_5588_13984" v-if="visible_5586_119">
                            <Dot
                                id="5588_13984"
                                class="Pixso-instance-5588_13984"
                                Size="sm"
                            />
                        </slot>
                        <slot name="slot_5588_13985">
                            <p
                                id="5588_13985"
                                class="Pixso-paragraph-5588_13985 fill-destructive30-423_3220-paragraph text-text-smsemibold-423_3209"
                            >
                                {{ text_5588_129 ?? "Label" }}
                            </p>
                        </slot>
                    </div>
                    <slot name="slot_5588_13986" v-if="visible_5586_121">
                        <Check
                            id="5588_13986"
                            class="Pixso-instance-5588_13986"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div
                    class="stroke-5588_13981 stroke-destructive30-423_3220"
                ></div>
            </div>
            <div
                id="5588_12042"
                class="stroke-wrapper-5588_12042"
                v-if="
                    Size === 'md' &&
                    Color === 'Warning' &&
                    Hierarchy === 'Outlined' &&
                    State === 'Default'
                "
            >
                <div class="Pixso-symbol-5588_12042">
                    <slot name="slot_5588_12043" v-if="visible_5586_123">
                        <Circle
                            id="5588_12043"
                            class="Pixso-instance-5588_12043"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                    <div id="5588_12044" class="Pixso-frame-5588_12044">
                        <slot name="slot_5588_12045" v-if="visible_5586_119">
                            <Dot
                                id="5588_12045"
                                class="Pixso-instance-5588_12045"
                                Size="sm"
                            />
                        </slot>
                        <slot name="slot_5588_12046">
                            <p
                                id="5588_12046"
                                class="Pixso-paragraph-5588_12046 fill-warning50-423_3213-paragraph text-text-smsemibold-423_3209"
                            >
                                {{ text_5588_129 ?? "Label" }}
                            </p>
                        </slot>
                    </div>
                    <slot name="slot_5588_12047" v-if="visible_5586_121">
                        <Check
                            id="5588_12047"
                            class="Pixso-instance-5588_12047"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div class="stroke-5588_12042 stroke-warning50-423_3213"></div>
            </div>
            <div
                id="5588_13987"
                class="stroke-wrapper-5588_13987"
                v-if="
                    Size === 'md' &&
                    Color === 'Warning' &&
                    Hierarchy === 'Outlined' &&
                    State === 'Disabled'
                "
            >
                <div class="Pixso-symbol-5588_13987">
                    <slot name="slot_5588_13988" v-if="visible_5586_123">
                        <Circle
                            id="5588_13988"
                            class="Pixso-instance-5588_13988"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                    <div id="5588_13989" class="Pixso-frame-5588_13989">
                        <slot name="slot_5588_13990" v-if="visible_5586_119">
                            <Dot
                                id="5588_13990"
                                class="Pixso-instance-5588_13990"
                                Size="sm"
                            />
                        </slot>
                        <slot name="slot_5588_13991">
                            <p
                                id="5588_13991"
                                class="Pixso-paragraph-5588_13991 fill-warning30-32_4109-paragraph text-text-smsemibold-423_3209"
                            >
                                {{ text_5588_129 ?? "Label" }}
                            </p>
                        </slot>
                    </div>
                    <slot name="slot_5588_13992" v-if="visible_5586_121">
                        <Check
                            id="5588_13992"
                            class="Pixso-instance-5588_13992"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div class="stroke-5588_13987 stroke-warning30-32_4109"></div>
            </div>
            <div
                id="5588_12204"
                class="stroke-wrapper-5588_12204"
                v-if="
                    Size === 'md' &&
                    Color === 'Success' &&
                    Hierarchy === 'Outlined' &&
                    State === 'Default'
                "
            >
                <div class="Pixso-symbol-5588_12204">
                    <slot name="slot_5588_12205" v-if="visible_5586_123">
                        <Circle
                            id="5588_12205"
                            class="Pixso-instance-5588_12205"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                    <div id="5588_12206" class="Pixso-frame-5588_12206">
                        <slot name="slot_5588_12207" v-if="visible_5586_119">
                            <Dot
                                id="5588_12207"
                                class="Pixso-instance-5588_12207"
                                Size="sm"
                            />
                        </slot>
                        <slot name="slot_5588_12208">
                            <p
                                id="5588_12208"
                                class="Pixso-paragraph-5588_12208 fill-success50-1636_81205-paragraph text-text-smsemibold-423_3209"
                            >
                                {{ text_5588_129 ?? "Label" }}
                            </p>
                        </slot>
                    </div>
                    <slot name="slot_5588_12209" v-if="visible_5586_121">
                        <Check
                            id="5588_12209"
                            class="Pixso-instance-5588_12209"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div
                    class="stroke-5588_12204 stroke-success50-1636_81205"
                ></div>
            </div>
            <div
                id="5588_13993"
                class="stroke-wrapper-5588_13993"
                v-if="
                    Size === 'md' &&
                    Color === 'Success' &&
                    Hierarchy === 'Outlined' &&
                    State === 'Disabled'
                "
            >
                <div class="Pixso-symbol-5588_13993">
                    <slot name="slot_5588_13994" v-if="visible_5586_123">
                        <Circle
                            id="5588_13994"
                            class="Pixso-instance-5588_13994"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                    <div id="5588_13995" class="Pixso-frame-5588_13995">
                        <slot name="slot_5588_13996" v-if="visible_5586_119">
                            <Dot
                                id="5588_13996"
                                class="Pixso-instance-5588_13996"
                                Size="sm"
                            />
                        </slot>
                        <slot name="slot_5588_13997">
                            <p
                                id="5588_13997"
                                class="Pixso-paragraph-5588_13997 fill-success30-1636_81203-paragraph text-text-smsemibold-423_3209"
                            >
                                {{ text_5588_129 ?? "Label" }}
                            </p>
                        </slot>
                    </div>
                    <slot name="slot_5588_13998" v-if="visible_5586_121">
                        <Check
                            id="5588_13998"
                            class="Pixso-instance-5588_13998"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div
                    class="stroke-5588_13993 stroke-success30-1636_81203"
                ></div>
            </div>
            <div
                id="5588_11523"
                class="Pixso-symbol-5588_11523 fill-gray80-32_4123 fill-gray0-white-67_3285"
                v-if="
                    Size === 'md' &&
                    Color === 'Gray' &&
                    Hierarchy === 'Primary' &&
                    State === 'Default'
                "
            >
                <slot name="slot_5588_11524" v-if="visible_5586_123">
                    <Circle
                        id="5588_11524"
                        class="Pixso-instance-5588_11524"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <div id="5588_11525" class="Pixso-frame-5588_11525">
                    <slot name="slot_5588_11526" v-if="visible_5586_119">
                        <Dot
                            id="5588_11526"
                            class="Pixso-instance-5588_11526"
                            Size="sm"
                        />
                    </slot>
                    <slot name="slot_5588_11527">
                        <p
                            id="5588_11527"
                            class="Pixso-paragraph-5588_11527 fill-gray0-white-67_3285-paragraph text-text-smsemibold-423_3209 fill-brand60-1257_33467-paragraph"
                        >
                            {{ text_5588_129 ?? "Label" }}
                        </p>
                    </slot>
                </div>
                <slot name="slot_5588_11528" v-if="visible_5586_121">
                    <Check
                        id="5588_11528"
                        class="Pixso-instance-5588_11528"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
            </div>
            <div
                id="5588_13999"
                class="Pixso-symbol-5588_13999 fill-gray20-36_1844"
                v-if="
                    Size === 'md' &&
                    Color === 'Gray' &&
                    Hierarchy === 'Primary' &&
                    State === 'Disabled'
                "
            >
                <slot name="slot_5588_14000" v-if="visible_5586_123">
                    <Circle
                        id="5588_14000"
                        class="Pixso-instance-5588_14000"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <div id="5588_14001" class="Pixso-frame-5588_14001">
                    <slot name="slot_5588_14002" v-if="visible_5586_119">
                        <Dot
                            id="5588_14002"
                            class="Pixso-instance-5588_14002"
                            Size="sm"
                        />
                    </slot>
                    <slot name="slot_5588_14003">
                        <p
                            id="5588_14003"
                            class="Pixso-paragraph-5588_14003 fill-gray40-83_2714-paragraph text-text-smsemibold-423_3209"
                        >
                            {{ text_5588_129 ?? "Label" }}
                        </p>
                    </slot>
                </div>
                <slot name="slot_5588_14004" v-if="visible_5586_121">
                    <Check
                        id="5588_14004"
                        class="Pixso-instance-5588_14004"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
            </div>
            <div
                id="5588_11547"
                class="Pixso-symbol-5588_11547 fill-gray5-32_4120"
                v-if="
                    Size === 'md' &&
                    Color === 'Gray' &&
                    Hierarchy === 'Secondary' &&
                    State === 'Default'
                "
            >
                <slot name="slot_5588_11548" v-if="visible_5586_123">
                    <Circle
                        id="5588_11548"
                        class="Pixso-instance-5588_11548"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <div id="5588_11549" class="Pixso-frame-5588_11549">
                    <slot name="slot_5588_11550" v-if="visible_5586_119">
                        <Dot
                            id="5588_11550"
                            class="Pixso-instance-5588_11550"
                            Size="sm"
                        />
                    </slot>
                    <slot name="slot_5588_11551">
                        <p
                            id="5588_11551"
                            class="Pixso-paragraph-5588_11551 fill-gray60-83_2722-paragraph text-text-smsemibold-423_3209"
                        >
                            {{ text_5588_129 ?? "Label" }}
                        </p>
                    </slot>
                </div>
                <slot name="slot_5588_11552" v-if="visible_5586_121">
                    <Check
                        id="5588_11552"
                        class="Pixso-instance-5588_11552"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
            </div>
            <div
                id="5588_14005"
                class="Pixso-symbol-5588_14005 fill-gray5-32_4120"
                v-if="
                    Size === 'md' &&
                    Color === 'Gray' &&
                    Hierarchy === 'Secondary' &&
                    State === 'Disabled'
                "
            >
                <slot name="slot_5588_14006" v-if="visible_5586_123">
                    <Circle
                        id="5588_14006"
                        class="Pixso-instance-5588_14006"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <div id="5588_14007" class="Pixso-frame-5588_14007">
                    <slot name="slot_5588_14008" v-if="visible_5586_119">
                        <Dot
                            id="5588_14008"
                            class="Pixso-instance-5588_14008"
                            Size="sm"
                        />
                    </slot>
                    <slot name="slot_5588_14009">
                        <p
                            id="5588_14009"
                            class="Pixso-paragraph-5588_14009 fill-gray30-35_1481-paragraph text-text-smsemibold-423_3209"
                        >
                            {{ text_5588_129 ?? "Label" }}
                        </p>
                    </slot>
                </div>
                <slot name="slot_5588_14010" v-if="visible_5586_121">
                    <Check
                        id="5588_14010"
                        class="Pixso-instance-5588_14010"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
            </div>
            <div
                id="5588_11553"
                class="stroke-wrapper-5588_11553"
                v-if="
                    Size === 'md' &&
                    Color === 'Gray' &&
                    Hierarchy === 'Outlined' &&
                    State === 'Default'
                "
            >
                <div class="Pixso-symbol-5588_11553">
                    <slot name="slot_5588_11554" v-if="visible_5586_123">
                        <Circle
                            id="5588_11554"
                            class="Pixso-instance-5588_11554"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                    <div id="5588_11555" class="Pixso-frame-5588_11555">
                        <slot name="slot_5588_11556" v-if="visible_5586_119">
                            <Dot
                                id="5588_11556"
                                class="Pixso-instance-5588_11556"
                                Size="sm"
                            />
                        </slot>
                        <slot name="slot_5588_11557">
                            <p
                                id="5588_11557"
                                class="Pixso-paragraph-5588_11557 fill-gray60-83_2722-paragraph text-text-smsemibold-423_3209"
                            >
                                {{ text_5588_129 ?? "Label" }}
                            </p>
                        </slot>
                    </div>
                    <slot name="slot_5588_11558" v-if="visible_5586_121">
                        <Check
                            id="5588_11558"
                            class="Pixso-instance-5588_11558"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div class="stroke-5588_11553 stroke-gray30-35_1481"></div>
            </div>
            <div
                id="5588_14011"
                class="stroke-wrapper-5588_14011"
                v-if="
                    Size === 'md' &&
                    Color === 'Gray' &&
                    Hierarchy === 'Outlined' &&
                    State === 'Disabled'
                "
            >
                <div class="Pixso-symbol-5588_14011">
                    <slot name="slot_5588_14012" v-if="visible_5586_123">
                        <Circle
                            id="5588_14012"
                            class="Pixso-instance-5588_14012"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                    <div id="5588_14013" class="Pixso-frame-5588_14013">
                        <slot name="slot_5588_14014" v-if="visible_5586_119">
                            <Dot
                                id="5588_14014"
                                class="Pixso-instance-5588_14014"
                                Size="sm"
                            />
                        </slot>
                        <slot name="slot_5588_14015">
                            <p
                                id="5588_14015"
                                class="Pixso-paragraph-5588_14015 fill-gray30-35_1481-paragraph text-text-smsemibold-423_3209"
                            >
                                {{ text_5588_129 ?? "Label" }}
                            </p>
                        </slot>
                    </div>
                    <slot name="slot_5588_14016" v-if="visible_5586_121">
                        <Check
                            id="5588_14016"
                            class="Pixso-instance-5588_14016"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div class="stroke-5588_14011 stroke-gray30-35_1481"></div>
            </div>
            <div
                id="5588_11877"
                class="Pixso-symbol-5588_11877 fill-destructive50-423_3219"
                v-if="
                    Size === 'sm' &&
                    Color === 'Destructive' &&
                    Hierarchy === 'Primary' &&
                    State === 'Default'
                "
            >
                <slot name="slot_5588_11878" v-if="visible_5586_123">
                    <Circle
                        id="5588_11878"
                        class="Pixso-instance-5588_11878"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <div id="5588_11879" class="Pixso-frame-5588_11879">
                    <slot name="slot_5588_11880" v-if="visible_5586_119">
                        <Dot
                            id="5588_11880"
                            class="Pixso-instance-5588_11880"
                            Size="sm"
                        />
                    </slot>
                    <slot name="slot_5588_11881">
                        <p
                            id="5588_11881"
                            class="Pixso-paragraph-5588_11881 fill-gray0-white-67_3285-paragraph text-text-xssemibold-439_9521"
                        >
                            {{ text_5588_129 ?? "Label" }}
                        </p>
                    </slot>
                </div>
                <slot name="slot_5588_11882" v-if="visible_5586_121">
                    <Check
                        id="5588_11882"
                        class="Pixso-instance-5588_11882"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
            </div>
            <div
                id="5588_14017"
                class="Pixso-symbol-5588_14017 fill-destructive20-438_3720"
                v-if="
                    Size === 'sm' &&
                    Color === 'Destructive' &&
                    Hierarchy === 'Primary' &&
                    State === 'Disabled'
                "
            >
                <slot name="slot_5588_14018" v-if="visible_5586_123">
                    <Circle
                        id="5588_14018"
                        class="Pixso-instance-5588_14018"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <div id="5588_14019" class="Pixso-frame-5588_14019">
                    <slot name="slot_5588_14020" v-if="visible_5586_119">
                        <Dot
                            id="5588_14020"
                            class="Pixso-instance-5588_14020"
                            Size="sm"
                        />
                    </slot>
                    <slot name="slot_5588_14021">
                        <p
                            id="5588_14021"
                            class="Pixso-paragraph-5588_14021 fill-destructive40-32_4110-paragraph text-text-xssemibold-439_9521"
                        >
                            {{ text_5588_129 ?? "Label" }}
                        </p>
                    </slot>
                </div>
                <slot name="slot_5588_14022" v-if="visible_5586_121">
                    <Check
                        id="5588_14022"
                        class="Pixso-instance-5588_14022"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
            </div>
            <div
                id="5588_12048"
                class="Pixso-symbol-5588_12048 fill-warning50-423_3213"
                v-if="
                    Size === 'sm' &&
                    Color === 'Warning' &&
                    Hierarchy === 'Primary' &&
                    State === 'Default'
                "
            >
                <slot name="slot_5588_12049" v-if="visible_5586_123">
                    <Circle
                        id="5588_12049"
                        class="Pixso-instance-5588_12049"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <div id="5588_12050" class="Pixso-frame-5588_12050">
                    <slot name="slot_5588_12051" v-if="visible_5586_119">
                        <Dot
                            id="5588_12051"
                            class="Pixso-instance-5588_12051"
                            Size="sm"
                        />
                    </slot>
                    <slot name="slot_5588_12052">
                        <p
                            id="5588_12052"
                            class="Pixso-paragraph-5588_12052 fill-gray0-white-67_3285-paragraph text-text-xssemibold-439_9521"
                        >
                            {{ text_5588_129 ?? "Label" }}
                        </p>
                    </slot>
                </div>
                <slot name="slot_5588_12053" v-if="visible_5586_121">
                    <Check
                        id="5588_12053"
                        class="Pixso-instance-5588_12053"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
            </div>
            <div
                id="5588_14023"
                class="Pixso-symbol-5588_14023 fill-warning20-428_4551"
                v-if="
                    Size === 'sm' &&
                    Color === 'Warning' &&
                    Hierarchy === 'Primary' &&
                    State === 'Disabled'
                "
            >
                <slot name="slot_5588_14024" v-if="visible_5586_123">
                    <Circle
                        id="5588_14024"
                        class="Pixso-instance-5588_14024"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <div id="5588_14025" class="Pixso-frame-5588_14025">
                    <slot name="slot_5588_14026" v-if="visible_5586_119">
                        <Dot
                            id="5588_14026"
                            class="Pixso-instance-5588_14026"
                            Size="sm"
                        />
                    </slot>
                    <slot name="slot_5588_14027">
                        <p
                            id="5588_14027"
                            class="Pixso-paragraph-5588_14027 fill-warning40-428_4549-paragraph text-text-xssemibold-439_9521"
                        >
                            {{ text_5588_129 ?? "Label" }}
                        </p>
                    </slot>
                </div>
                <slot name="slot_5588_14028" v-if="visible_5586_121">
                    <Check
                        id="5588_14028"
                        class="Pixso-instance-5588_14028"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
            </div>
            <div
                id="5588_12210"
                class="Pixso-symbol-5588_12210 fill-success50-1636_81205"
                v-if="
                    Size === 'sm' &&
                    Color === 'Success' &&
                    Hierarchy === 'Primary' &&
                    State === 'Default'
                "
            >
                <slot name="slot_5588_12211" v-if="visible_5586_123">
                    <Circle
                        id="5588_12211"
                        class="Pixso-instance-5588_12211"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <div id="5588_12212" class="Pixso-frame-5588_12212">
                    <slot name="slot_5588_12213" v-if="visible_5586_119">
                        <Dot
                            id="5588_12213"
                            class="Pixso-instance-5588_12213"
                            Size="sm"
                        />
                    </slot>
                    <slot name="slot_5588_12214">
                        <p
                            id="5588_12214"
                            class="Pixso-paragraph-5588_12214 fill-gray0-white-67_3285-paragraph text-text-xssemibold-439_9521"
                        >
                            {{ text_5588_129 ?? "Label" }}
                        </p>
                    </slot>
                </div>
                <slot name="slot_5588_12215" v-if="visible_5586_121">
                    <Check
                        id="5588_12215"
                        class="Pixso-instance-5588_12215"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
            </div>
            <div
                id="5588_14029"
                class="Pixso-symbol-5588_14029 fill-success20-1636_81202"
                v-if="
                    Size === 'sm' &&
                    Color === 'Success' &&
                    Hierarchy === 'Primary' &&
                    State === 'Disabled'
                "
            >
                <slot name="slot_5588_14030" v-if="visible_5586_123">
                    <Circle
                        id="5588_14030"
                        class="Pixso-instance-5588_14030"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <div id="5588_14031" class="Pixso-frame-5588_14031">
                    <slot name="slot_5588_14032" v-if="visible_5586_119">
                        <Dot
                            id="5588_14032"
                            class="Pixso-instance-5588_14032"
                            Size="sm"
                        />
                    </slot>
                    <slot name="slot_5588_14033">
                        <p
                            id="5588_14033"
                            class="Pixso-paragraph-5588_14033 fill-success40-1636_81204-paragraph text-text-xssemibold-439_9521"
                        >
                            {{ text_5588_129 ?? "Label" }}
                        </p>
                    </slot>
                </div>
                <slot name="slot_5588_14034" v-if="visible_5586_121">
                    <Check
                        id="5588_14034"
                        class="Pixso-instance-5588_14034"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
            </div>
            <div
                id="5588_11883"
                class="Pixso-symbol-5588_11883 fill-destructive5-83_2719"
                v-if="
                    Size === 'sm' &&
                    Color === 'Destructive' &&
                    Hierarchy === 'Secondary' &&
                    State === 'Default'
                "
            >
                <slot name="slot_5588_11884" v-if="visible_5586_123">
                    <Circle
                        id="5588_11884"
                        class="Pixso-instance-5588_11884"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <div id="5588_11885" class="Pixso-frame-5588_11885">
                    <slot name="slot_5588_11886" v-if="visible_5586_119">
                        <Dot
                            id="5588_11886"
                            class="Pixso-instance-5588_11886"
                            Size="sm"
                        />
                    </slot>
                    <slot name="slot_5588_11887">
                        <p
                            id="5588_11887"
                            class="Pixso-paragraph-5588_11887 fill-destructive50-423_3219-paragraph text-text-xssemibold-439_9521"
                        >
                            {{ text_5588_129 ?? "Label" }}
                        </p>
                    </slot>
                </div>
                <slot name="slot_5588_11888" v-if="visible_5586_121">
                    <Check
                        id="5588_11888"
                        class="Pixso-instance-5588_11888"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
            </div>
            <div
                id="5588_14035"
                class="Pixso-symbol-5588_14035 fill-destructive5-83_2719"
                v-if="
                    Size === 'sm' &&
                    Color === 'Destructive' &&
                    Hierarchy === 'Secondary' &&
                    State === 'Disabled'
                "
            >
                <slot name="slot_5588_14036" v-if="visible_5586_123">
                    <Circle
                        id="5588_14036"
                        class="Pixso-instance-5588_14036"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <div id="5588_14037" class="Pixso-frame-5588_14037">
                    <slot name="slot_5588_14038" v-if="visible_5586_119">
                        <Dot
                            id="5588_14038"
                            class="Pixso-instance-5588_14038"
                            Size="sm"
                        />
                    </slot>
                    <slot name="slot_5588_14039">
                        <p
                            id="5588_14039"
                            class="Pixso-paragraph-5588_14039 fill-destructive30-423_3220-paragraph text-text-xssemibold-439_9521"
                        >
                            {{ text_5588_129 ?? "Label" }}
                        </p>
                    </slot>
                </div>
                <slot name="slot_5588_14040" v-if="visible_5586_121">
                    <Check
                        id="5588_14040"
                        class="Pixso-instance-5588_14040"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
            </div>
            <div
                id="5588_12054"
                class="Pixso-symbol-5588_12054 fill-warning5-83_2717"
                v-if="
                    Size === 'sm' &&
                    Color === 'Warning' &&
                    Hierarchy === 'Secondary' &&
                    State === 'Default'
                "
            >
                <slot name="slot_5588_12055" v-if="visible_5586_123">
                    <Circle
                        id="5588_12055"
                        class="Pixso-instance-5588_12055"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <div id="5588_12056" class="Pixso-frame-5588_12056">
                    <slot name="slot_5588_12057" v-if="visible_5586_119">
                        <Dot
                            id="5588_12057"
                            class="Pixso-instance-5588_12057"
                            Size="sm"
                        />
                    </slot>
                    <slot name="slot_5588_12058">
                        <p
                            id="5588_12058"
                            class="Pixso-paragraph-5588_12058 fill-warning50-423_3213-paragraph text-text-xssemibold-439_9521"
                        >
                            {{ text_5588_129 ?? "Label" }}
                        </p>
                    </slot>
                </div>
                <slot name="slot_5588_12059" v-if="visible_5586_121">
                    <Check
                        id="5588_12059"
                        class="Pixso-instance-5588_12059"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
            </div>
            <div
                id="5588_14041"
                class="Pixso-symbol-5588_14041 fill-warning5-83_2717"
                v-if="
                    Size === 'sm' &&
                    Color === 'Warning' &&
                    Hierarchy === 'Secondary' &&
                    State === 'Disabled'
                "
            >
                <slot name="slot_5588_14042" v-if="visible_5586_123">
                    <Circle
                        id="5588_14042"
                        class="Pixso-instance-5588_14042"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <div id="5588_14043" class="Pixso-frame-5588_14043">
                    <slot name="slot_5588_14044" v-if="visible_5586_119">
                        <Dot
                            id="5588_14044"
                            class="Pixso-instance-5588_14044"
                            Size="sm"
                        />
                    </slot>
                    <slot name="slot_5588_14045">
                        <p
                            id="5588_14045"
                            class="Pixso-paragraph-5588_14045 fill-warning30-32_4109-paragraph text-text-xssemibold-439_9521"
                        >
                            {{ text_5588_129 ?? "Label" }}
                        </p>
                    </slot>
                </div>
                <slot name="slot_5588_14046" v-if="visible_5586_121">
                    <Check
                        id="5588_14046"
                        class="Pixso-instance-5588_14046"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
            </div>
            <div
                id="5588_12216"
                class="Pixso-symbol-5588_12216 fill-success5-1636_81199"
                v-if="
                    Size === 'sm' &&
                    Color === 'Success' &&
                    Hierarchy === 'Secondary' &&
                    State === 'Default'
                "
            >
                <slot name="slot_5588_12217" v-if="visible_5586_123">
                    <Circle
                        id="5588_12217"
                        class="Pixso-instance-5588_12217"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <div id="5588_12218" class="Pixso-frame-5588_12218">
                    <slot name="slot_5588_12219" v-if="visible_5586_119">
                        <Dot
                            id="5588_12219"
                            class="Pixso-instance-5588_12219"
                            Size="sm"
                        />
                    </slot>
                    <slot name="slot_5588_12220">
                        <p
                            id="5588_12220"
                            class="Pixso-paragraph-5588_12220 fill-success50-1636_81205-paragraph text-text-xssemibold-439_9521"
                        >
                            {{ text_5588_129 ?? "Label" }}
                        </p>
                    </slot>
                </div>
                <slot name="slot_5588_12221" v-if="visible_5586_121">
                    <Check
                        id="5588_12221"
                        class="Pixso-instance-5588_12221"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
            </div>
            <div
                id="5588_14047"
                class="Pixso-symbol-5588_14047 fill-success5-1636_81199"
                v-if="
                    Size === 'sm' &&
                    Color === 'Success' &&
                    Hierarchy === 'Secondary' &&
                    State === 'Disabled'
                "
            >
                <slot name="slot_5588_14048" v-if="visible_5586_123">
                    <Circle
                        id="5588_14048"
                        class="Pixso-instance-5588_14048"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <div id="5588_14049" class="Pixso-frame-5588_14049">
                    <slot name="slot_5588_14050" v-if="visible_5586_119">
                        <Dot
                            id="5588_14050"
                            class="Pixso-instance-5588_14050"
                            Size="sm"
                        />
                    </slot>
                    <slot name="slot_5588_14051">
                        <p
                            id="5588_14051"
                            class="Pixso-paragraph-5588_14051 fill-success30-1636_81203-paragraph text-text-xssemibold-439_9521"
                        >
                            {{ text_5588_129 ?? "Label" }}
                        </p>
                    </slot>
                </div>
                <slot name="slot_5588_14052" v-if="visible_5586_121">
                    <Check
                        id="5588_14052"
                        class="Pixso-instance-5588_14052"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
            </div>
            <div
                id="5588_11889"
                class="stroke-wrapper-5588_11889"
                v-if="
                    Size === 'sm' &&
                    Color === 'Destructive' &&
                    Hierarchy === 'Outlined' &&
                    State === 'Default'
                "
            >
                <div class="Pixso-symbol-5588_11889">
                    <slot name="slot_5588_11890" v-if="visible_5586_123">
                        <Circle
                            id="5588_11890"
                            class="Pixso-instance-5588_11890"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                    <div id="5588_11891" class="Pixso-frame-5588_11891">
                        <slot name="slot_5588_11892" v-if="visible_5586_119">
                            <Dot
                                id="5588_11892"
                                class="Pixso-instance-5588_11892"
                                Size="sm"
                            />
                        </slot>
                        <slot name="slot_5588_11893">
                            <p
                                id="5588_11893"
                                class="Pixso-paragraph-5588_11893 fill-destructive50-423_3219-paragraph text-text-xssemibold-439_9521"
                            >
                                {{ text_5588_129 ?? "Label" }}
                            </p>
                        </slot>
                    </div>
                    <slot name="slot_5588_11894" v-if="visible_5586_121">
                        <Check
                            id="5588_11894"
                            class="Pixso-instance-5588_11894"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div
                    class="stroke-5588_11889 stroke-destructive50-423_3219"
                ></div>
            </div>
            <div
                id="5588_14053"
                class="stroke-wrapper-5588_14053"
                v-if="
                    Size === 'sm' &&
                    Color === 'Destructive' &&
                    Hierarchy === 'Outlined' &&
                    State === 'Disabled'
                "
            >
                <div class="Pixso-symbol-5588_14053">
                    <slot name="slot_5588_14054" v-if="visible_5586_123">
                        <Circle
                            id="5588_14054"
                            class="Pixso-instance-5588_14054"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                    <div id="5588_14055" class="Pixso-frame-5588_14055">
                        <slot name="slot_5588_14056" v-if="visible_5586_119">
                            <Dot
                                id="5588_14056"
                                class="Pixso-instance-5588_14056"
                                Size="sm"
                            />
                        </slot>
                        <slot name="slot_5588_14057">
                            <p
                                id="5588_14057"
                                class="Pixso-paragraph-5588_14057 fill-destructive30-423_3220-paragraph text-text-xssemibold-439_9521"
                            >
                                {{ text_5588_129 ?? "Label" }}
                            </p>
                        </slot>
                    </div>
                    <slot name="slot_5588_14058" v-if="visible_5586_121">
                        <Check
                            id="5588_14058"
                            class="Pixso-instance-5588_14058"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div
                    class="stroke-5588_14053 stroke-destructive30-423_3220"
                ></div>
            </div>
            <div
                id="5588_12060"
                class="stroke-wrapper-5588_12060"
                v-if="
                    Size === 'sm' &&
                    Color === 'Warning' &&
                    Hierarchy === 'Outlined' &&
                    State === 'Default'
                "
            >
                <div class="Pixso-symbol-5588_12060">
                    <slot name="slot_5588_12061" v-if="visible_5586_123">
                        <Circle
                            id="5588_12061"
                            class="Pixso-instance-5588_12061"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                    <div id="5588_12062" class="Pixso-frame-5588_12062">
                        <slot name="slot_5588_12063" v-if="visible_5586_119">
                            <Dot
                                id="5588_12063"
                                class="Pixso-instance-5588_12063"
                                Size="sm"
                            />
                        </slot>
                        <slot name="slot_5588_12064">
                            <p
                                id="5588_12064"
                                class="Pixso-paragraph-5588_12064 fill-warning50-423_3213-paragraph text-text-xssemibold-439_9521"
                            >
                                {{ text_5588_129 ?? "Label" }}
                            </p>
                        </slot>
                    </div>
                    <slot name="slot_5588_12065" v-if="visible_5586_121">
                        <Check
                            id="5588_12065"
                            class="Pixso-instance-5588_12065"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div class="stroke-5588_12060 stroke-warning50-423_3213"></div>
            </div>
            <div
                id="5588_14059"
                class="stroke-wrapper-5588_14059"
                v-if="
                    Size === 'sm' &&
                    Color === 'Warning' &&
                    Hierarchy === 'Outlined' &&
                    State === 'Disabled'
                "
            >
                <div class="Pixso-symbol-5588_14059">
                    <slot name="slot_5588_14060" v-if="visible_5586_123">
                        <Circle
                            id="5588_14060"
                            class="Pixso-instance-5588_14060"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                    <div id="5588_14061" class="Pixso-frame-5588_14061">
                        <slot name="slot_5588_14062" v-if="visible_5586_119">
                            <Dot
                                id="5588_14062"
                                class="Pixso-instance-5588_14062"
                                Size="sm"
                            />
                        </slot>
                        <slot name="slot_5588_14063">
                            <p
                                id="5588_14063"
                                class="Pixso-paragraph-5588_14063 fill-warning30-32_4109-paragraph text-text-xssemibold-439_9521"
                            >
                                {{ text_5588_129 ?? "Label" }}
                            </p>
                        </slot>
                    </div>
                    <slot name="slot_5588_14064" v-if="visible_5586_121">
                        <Check
                            id="5588_14064"
                            class="Pixso-instance-5588_14064"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div class="stroke-5588_14059 stroke-warning30-32_4109"></div>
            </div>
            <div
                id="5588_12222"
                class="stroke-wrapper-5588_12222"
                v-if="
                    Size === 'sm' &&
                    Color === 'Success' &&
                    Hierarchy === 'Outlined' &&
                    State === 'Default'
                "
            >
                <div class="Pixso-symbol-5588_12222">
                    <slot name="slot_5588_12223" v-if="visible_5586_123">
                        <Circle
                            id="5588_12223"
                            class="Pixso-instance-5588_12223"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                    <div id="5588_12224" class="Pixso-frame-5588_12224">
                        <slot name="slot_5588_12225" v-if="visible_5586_119">
                            <Dot
                                id="5588_12225"
                                class="Pixso-instance-5588_12225"
                                Size="sm"
                            />
                        </slot>
                        <slot name="slot_5588_12226">
                            <p
                                id="5588_12226"
                                class="Pixso-paragraph-5588_12226 fill-success50-1636_81205-paragraph text-text-xssemibold-439_9521"
                            >
                                {{ text_5588_129 ?? "Label" }}
                            </p>
                        </slot>
                    </div>
                    <slot name="slot_5588_12227" v-if="visible_5586_121">
                        <Check
                            id="5588_12227"
                            class="Pixso-instance-5588_12227"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div
                    class="stroke-5588_12222 stroke-success50-1636_81205"
                ></div>
            </div>
            <div
                id="5588_14065"
                class="stroke-wrapper-5588_14065"
                v-if="
                    Size === 'sm' &&
                    Color === 'Success' &&
                    Hierarchy === 'Outlined' &&
                    State === 'Disabled'
                "
            >
                <div class="Pixso-symbol-5588_14065">
                    <slot name="slot_5588_14066" v-if="visible_5586_123">
                        <Circle
                            id="5588_14066"
                            class="Pixso-instance-5588_14066"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                    <div id="5588_14067" class="Pixso-frame-5588_14067">
                        <slot name="slot_5588_14068" v-if="visible_5586_119">
                            <Dot
                                id="5588_14068"
                                class="Pixso-instance-5588_14068"
                                Size="sm"
                            />
                        </slot>
                        <slot name="slot_5588_14069">
                            <p
                                id="5588_14069"
                                class="Pixso-paragraph-5588_14069 fill-success30-1636_81203-paragraph text-text-xssemibold-439_9521"
                            >
                                {{ text_5588_129 ?? "Label" }}
                            </p>
                        </slot>
                    </div>
                    <slot name="slot_5588_14070" v-if="visible_5586_121">
                        <Check
                            id="5588_14070"
                            class="Pixso-instance-5588_14070"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div
                    class="stroke-5588_14065 stroke-success30-1636_81203"
                ></div>
            </div>
            <div
                id="5588_11529"
                class="Pixso-symbol-5588_11529 fill-gray80-32_4123"
                v-if="
                    Size === 'sm' &&
                    Color === 'Gray' &&
                    Hierarchy === 'Primary' &&
                    State === 'Default'
                "
            >
                <slot name="slot_5588_11530" v-if="visible_5586_123">
                    <Circle
                        id="5588_11530"
                        class="Pixso-instance-5588_11530"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <div id="5588_11531" class="Pixso-frame-5588_11531">
                    <slot name="slot_5588_11532" v-if="visible_5586_119">
                        <Dot
                            id="5588_11532"
                            class="Pixso-instance-5588_11532"
                            Size="sm"
                        />
                    </slot>
                    <slot name="slot_5588_11533">
                        <p
                            id="5588_11533"
                            class="Pixso-paragraph-5588_11533 fill-gray0-white-67_3285-paragraph text-text-xssemibold-439_9521"
                        >
                            {{ text_5588_129 ?? "Label" }}
                        </p>
                    </slot>
                </div>
                <slot name="slot_5588_11534" v-if="visible_5586_121">
                    <Check
                        id="5588_11534"
                        class="Pixso-instance-5588_11534"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
            </div>
            <div
                id="5588_14071"
                class="Pixso-symbol-5588_14071 fill-gray20-36_1844"
                v-if="
                    Size === 'sm' &&
                    Color === 'Gray' &&
                    Hierarchy === 'Primary' &&
                    State === 'Disabled'
                "
            >
                <slot name="slot_5588_14072" v-if="visible_5586_123">
                    <Circle
                        id="5588_14072"
                        class="Pixso-instance-5588_14072"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <div id="5588_14073" class="Pixso-frame-5588_14073">
                    <slot name="slot_5588_14074" v-if="visible_5586_119">
                        <Dot
                            id="5588_14074"
                            class="Pixso-instance-5588_14074"
                            Size="sm"
                        />
                    </slot>
                    <slot name="slot_5588_14075">
                        <p
                            id="5588_14075"
                            class="Pixso-paragraph-5588_14075 fill-gray40-83_2714-paragraph text-text-xssemibold-439_9521"
                        >
                            {{ text_5588_129 ?? "Label" }}
                        </p>
                    </slot>
                </div>
                <slot name="slot_5588_14076" v-if="visible_5586_121">
                    <Check
                        id="5588_14076"
                        class="Pixso-instance-5588_14076"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
            </div>
            <div
                id="5588_11559"
                class="Pixso-symbol-5588_11559 fill-gray5-32_4120"
                v-if="
                    Size === 'sm' &&
                    Color === 'Gray' &&
                    Hierarchy === 'Secondary' &&
                    State === 'Default'
                "
            >
                <slot name="slot_5588_11560" v-if="visible_5586_123">
                    <Circle
                        id="5588_11560"
                        class="Pixso-instance-5588_11560"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <div id="5588_11561" class="Pixso-frame-5588_11561">
                    <slot name="slot_5588_11562" v-if="visible_5586_119">
                        <Dot
                            id="5588_11562"
                            class="Pixso-instance-5588_11562"
                            Size="sm"
                        />
                    </slot>
                    <slot name="slot_5588_11563">
                        <p
                            id="5588_11563"
                            class="Pixso-paragraph-5588_11563 fill-gray60-83_2722-paragraph text-text-xssemibold-439_9521"
                        >
                            {{ text_5588_129 ?? "Label" }}
                        </p>
                    </slot>
                </div>
                <slot name="slot_5588_11564" v-if="visible_5586_121">
                    <Check
                        id="5588_11564"
                        class="Pixso-instance-5588_11564"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
            </div>
            <div
                id="5588_14077"
                class="Pixso-symbol-5588_14077 fill-gray5-32_4120"
                v-if="
                    Size === 'sm' &&
                    Color === 'Gray' &&
                    Hierarchy === 'Secondary' &&
                    State === 'Disabled'
                "
            >
                <slot name="slot_5588_14078" v-if="visible_5586_123">
                    <Circle
                        id="5588_14078"
                        class="Pixso-instance-5588_14078"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <div id="5588_14079" class="Pixso-frame-5588_14079">
                    <slot name="slot_5588_14080" v-if="visible_5586_119">
                        <Dot
                            id="5588_14080"
                            class="Pixso-instance-5588_14080"
                            Size="sm"
                        />
                    </slot>
                    <slot name="slot_5588_14081">
                        <p
                            id="5588_14081"
                            class="Pixso-paragraph-5588_14081 fill-gray30-35_1481-paragraph text-text-xssemibold-439_9521"
                        >
                            {{ text_5588_129 ?? "Label" }}
                        </p>
                    </slot>
                </div>
                <slot name="slot_5588_14082" v-if="visible_5586_121">
                    <Check
                        id="5588_14082"
                        class="Pixso-instance-5588_14082"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
            </div>
            <div
                id="5588_11565"
                class="stroke-wrapper-5588_11565"
                v-if="
                    Size === 'sm' &&
                    Color === 'Gray' &&
                    Hierarchy === 'Outlined' &&
                    State === 'Default'
                "
            >
                <div class="Pixso-symbol-5588_11565">
                    <slot name="slot_5588_11566" v-if="visible_5586_123">
                        <Circle
                            id="5588_11566"
                            class="Pixso-instance-5588_11566"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                    <div id="5588_11567" class="Pixso-frame-5588_11567">
                        <slot name="slot_5588_11568" v-if="visible_5586_119">
                            <Dot
                                id="5588_11568"
                                class="Pixso-instance-5588_11568"
                                Size="sm"
                            />
                        </slot>
                        <slot name="slot_5588_11569">
                            <p
                                id="5588_11569"
                                class="Pixso-paragraph-5588_11569 fill-gray60-83_2722-paragraph text-text-xssemibold-439_9521"
                            >
                                {{ text_5588_129 ?? "Label" }}
                            </p>
                        </slot>
                    </div>
                    <slot name="slot_5588_11570" v-if="visible_5586_121">
                        <Check
                            id="5588_11570"
                            class="Pixso-instance-5588_11570"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div class="stroke-5588_11565 stroke-gray30-35_1481"></div>
            </div>
            <div
                id="5588_14083"
                class="stroke-wrapper-5588_14083"
                v-if="
                    Size === 'sm' &&
                    Color === 'Gray' &&
                    Hierarchy === 'Outlined' &&
                    State === 'Disabled'
                "
            >
                <div class="Pixso-symbol-5588_14083">
                    <slot name="slot_5588_14084" v-if="visible_5586_123">
                        <Circle
                            id="5588_14084"
                            class="Pixso-instance-5588_14084"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                    <div id="5588_14085" class="Pixso-frame-5588_14085">
                        <slot name="slot_5588_14086" v-if="visible_5586_119">
                            <Dot
                                id="5588_14086"
                                class="Pixso-instance-5588_14086"
                                Size="sm"
                            />
                        </slot>
                        <slot name="slot_5588_14087">
                            <p
                                id="5588_14087"
                                class="Pixso-paragraph-5588_14087 fill-gray30-35_1481-paragraph text-text-xssemibold-439_9521"
                            >
                                {{ text_5588_129 ?? "Label" }}
                            </p>
                        </slot>
                    </div>
                    <slot name="slot_5588_14088" v-if="visible_5586_121">
                        <Check
                            id="5588_14088"
                            class="Pixso-instance-5588_14088"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div class="stroke-5588_14083 stroke-gray30-35_1481"></div>
            </div>
        </div>
    </div>
</template>
<script lang="ts" setup>
import Circle from "@/components/Circle.vue";
import Dot from "@/components/Dot.vue";
import Check from "@/components/Check.vue";
const props = defineProps({
    visible_5586_119: { type: Boolean, default: true },
    visible_5586_121: { type: Boolean, default: true },
    visible_5586_123: { type: Boolean, default: true },
    instance_5586_125: { type: String, default: "Component_5578_149511" },
    instance_5586_127: { type: String, default: "Component_5578_148941" },
    text_5588_129: { type: String, default: "Label" },
    Size: { type: String },
    Color: { type: String },
    Hierarchy: { type: String },
    State: { type: String }
});
</script>
<style>
.Pixso-symbol-5489_8967 {
}
.Pixso-symbol-5588_11190 {
    width: auto;
    height: auto;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 6px 12px 6px 12px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5588_11191 {
    width: 16px;
    height: 16px;
}
.Pixso-frame-5588_11216 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 6px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5588_11192 {
    width: 8px;
    height: 8px;
}
.Pixso-paragraph-5588_11193 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5588_11194 {
    width: 16px;
    height: 16px;
}
.Pixso-symbol-5588_13000 {
    width: auto;
    height: auto;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 6px 12px 6px 12px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5588_13001 {
    width: 16px;
    height: 16px;
}
.Pixso-frame-5588_13002 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 6px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5588_13003 {
    width: 8px;
    height: 8px;
}
.Pixso-paragraph-5588_13004 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5588_13005 {
    width: 16px;
    height: 16px;
}
.Pixso-symbol-5588_13819 {
    width: auto;
    height: auto;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 6px 12px 6px 12px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5588_13820 {
    width: 16px;
    height: 16px;
}
.Pixso-frame-5588_13821 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 6px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5588_13822 {
    width: 8px;
    height: 8px;
}
.Pixso-paragraph-5588_13823 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5588_13824 {
    width: 16px;
    height: 16px;
}
.Pixso-symbol-5588_13006 {
    width: auto;
    height: auto;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 6px 12px 6px 12px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5588_13007 {
    width: 16px;
    height: 16px;
}
.Pixso-frame-5588_13008 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 6px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5588_13009 {
    width: 8px;
    height: 8px;
}
.Pixso-paragraph-5588_13010 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5588_13011 {
    width: 16px;
    height: 16px;
}
.Pixso-symbol-5588_11346 {
    width: auto;
    height: auto;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 6px 12px 6px 12px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5588_11347 {
    width: 16px;
    height: 16px;
}
.Pixso-frame-5588_11348 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 6px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5588_11349 {
    width: 8px;
    height: 8px;
}
.Pixso-paragraph-5588_11350 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5588_11351 {
    width: 16px;
    height: 16px;
}
.Pixso-symbol-5588_13012 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 6px 12px 6px 12px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.stroke-wrapper-5588_13012 {
    position: relative;
    width: auto;
    height: auto;
    display: flex;
}
.stroke-5588_13012 {
    position: absolute;
    inset: 0px;
    border-radius: 1234px 1234px 1234px 1234px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5588_13013 {
    width: 16px;
    height: 16px;
}
.Pixso-frame-5588_13014 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 6px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5588_13015 {
    width: 8px;
    height: 8px;
}
.Pixso-paragraph-5588_13016 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5588_13017 {
    width: 16px;
    height: 16px;
}
.Pixso-symbol-5588_13825 {
    width: auto;
    height: auto;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 6px 12px 6px 12px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5588_13826 {
    width: 16px;
    height: 16px;
}
.Pixso-frame-5588_13827 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 6px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5588_13828 {
    width: 8px;
    height: 8px;
}
.Pixso-paragraph-5588_13829 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5588_13830 {
    width: 16px;
    height: 16px;
}
.Pixso-symbol-5588_13018 {
    width: auto;
    height: auto;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 6px 12px 6px 12px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5588_13019 {
    width: 16px;
    height: 16px;
}
.Pixso-frame-5588_13020 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 6px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5588_13021 {
    width: 8px;
    height: 8px;
}
.Pixso-paragraph-5588_13022 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5588_13023 {
    width: 16px;
    height: 16px;
}
.Pixso-symbol-5588_11409 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 6px 12px 6px 12px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.stroke-wrapper-5588_11409 {
    position: relative;
    width: auto;
    height: auto;
    display: flex;
}
.stroke-5588_11409 {
    position: absolute;
    inset: 0px;
    border-radius: 1234px 1234px 1234px 1234px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5588_11410 {
    width: 16px;
    height: 16px;
}
.Pixso-frame-5588_11411 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 6px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5588_11412 {
    width: 8px;
    height: 8px;
}
.Pixso-paragraph-5588_11413 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5588_11414 {
    width: 16px;
    height: 16px;
}
.Pixso-symbol-5588_13024 {
    width: auto;
    height: auto;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 6px 12px 6px 12px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5588_13025 {
    width: 16px;
    height: 16px;
}
.Pixso-frame-5588_13026 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 6px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5588_13027 {
    width: 8px;
    height: 8px;
}
.Pixso-paragraph-5588_13028 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5588_13029 {
    width: 16px;
    height: 16px;
}
.Pixso-symbol-5588_13831 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 6px 12px 6px 12px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.stroke-wrapper-5588_13831 {
    position: relative;
    width: auto;
    height: auto;
    display: flex;
}
.stroke-5588_13831 {
    position: absolute;
    inset: 0px;
    border-radius: 1234px 1234px 1234px 1234px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5588_13832 {
    width: 16px;
    height: 16px;
}
.Pixso-frame-5588_13833 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 6px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5588_13834 {
    width: 8px;
    height: 8px;
}
.Pixso-paragraph-5588_13835 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5588_13836 {
    width: 16px;
    height: 16px;
}
.Pixso-symbol-5588_13030 {
    width: auto;
    height: auto;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 6px 12px 6px 12px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5588_13031 {
    width: 16px;
    height: 16px;
}
.Pixso-frame-5588_13032 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 6px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5588_13033 {
    width: 8px;
    height: 8px;
}
.Pixso-paragraph-5588_13034 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5588_13035 {
    width: 16px;
    height: 16px;
}
.Pixso-symbol-5588_11841 {
    width: auto;
    height: auto;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 6px 12px 6px 12px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5588_11842 {
    width: 16px;
    height: 16px;
}
.Pixso-frame-5588_11843 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 6px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5588_11844 {
    width: 8px;
    height: 8px;
}
.Pixso-paragraph-5588_11845 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5588_11846 {
    width: 16px;
    height: 16px;
}
.Pixso-symbol-5588_13036 {
    width: auto;
    height: auto;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 6px 12px 6px 12px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5588_13037 {
    width: 16px;
    height: 16px;
}
.Pixso-frame-5588_13038 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 6px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5588_13039 {
    width: 8px;
    height: 8px;
}
.Pixso-paragraph-5588_13040 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5588_13041 {
    width: 16px;
    height: 16px;
}
.Pixso-symbol-5588_13837 {
    width: auto;
    height: auto;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 6px 12px 6px 12px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5588_13838 {
    width: 16px;
    height: 16px;
}
.Pixso-frame-5588_13839 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 6px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5588_13840 {
    width: 8px;
    height: 8px;
}
.Pixso-paragraph-5588_13841 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5588_13842 {
    width: 16px;
    height: 16px;
}
.Pixso-symbol-5588_13042 {
    width: auto;
    height: auto;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 6px 12px 6px 12px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5588_13043 {
    width: 16px;
    height: 16px;
}
.Pixso-frame-5588_13044 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 6px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5588_13045 {
    width: 8px;
    height: 8px;
}
.Pixso-paragraph-5588_13046 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5588_13047 {
    width: 16px;
    height: 16px;
}
.Pixso-symbol-5588_12012 {
    width: auto;
    height: auto;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 6px 12px 6px 12px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5588_12013 {
    width: 16px;
    height: 16px;
}
.Pixso-frame-5588_12014 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 6px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5588_12015 {
    width: 8px;
    height: 8px;
}
.Pixso-paragraph-5588_12016 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5588_12017 {
    width: 16px;
    height: 16px;
}
.Pixso-symbol-5588_13048 {
    width: auto;
    height: auto;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 6px 12px 6px 12px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5588_13049 {
    width: 16px;
    height: 16px;
}
.Pixso-frame-5588_13050 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 6px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5588_13051 {
    width: 8px;
    height: 8px;
}
.Pixso-paragraph-5588_13052 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5588_13053 {
    width: 16px;
    height: 16px;
}
.Pixso-symbol-5588_13843 {
    width: auto;
    height: auto;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 6px 12px 6px 12px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5588_13844 {
    width: 16px;
    height: 16px;
}
.Pixso-frame-5588_13845 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 6px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5588_13846 {
    width: 8px;
    height: 8px;
}
.Pixso-paragraph-5588_13847 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5588_13848 {
    width: 16px;
    height: 16px;
}
.Pixso-symbol-5588_13054 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 6px 12px 6px 12px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.stroke-wrapper-5588_13054 {
    position: relative;
    width: auto;
    height: auto;
    display: flex;
}
.stroke-5588_13054 {
    position: absolute;
    inset: 0px;
    border-radius: 1234px 1234px 1234px 1234px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5588_13055 {
    width: 16px;
    height: 16px;
}
.Pixso-frame-5588_13056 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 6px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5588_13057 {
    width: 8px;
    height: 8px;
}
.Pixso-paragraph-5588_13058 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5588_13059 {
    width: 16px;
    height: 16px;
}
.Pixso-symbol-5588_12174 {
    width: auto;
    height: auto;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 6px 12px 6px 12px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5588_12175 {
    width: 16px;
    height: 16px;
}
.Pixso-frame-5588_12176 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 6px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5588_12177 {
    width: 8px;
    height: 8px;
}
.Pixso-paragraph-5588_12178 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5588_12179 {
    width: 16px;
    height: 16px;
}
.Pixso-symbol-5588_13060 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 6px 12px 6px 12px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.stroke-wrapper-5588_13060 {
    position: relative;
    width: auto;
    height: auto;
    display: flex;
}
.stroke-5588_13060 {
    position: absolute;
    inset: 0px;
    border-radius: 1234px 1234px 1234px 1234px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5588_13061 {
    width: 16px;
    height: 16px;
}
.Pixso-frame-5588_13062 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 6px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5588_13063 {
    width: 8px;
    height: 8px;
}
.Pixso-paragraph-5588_13064 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5588_13065 {
    width: 16px;
    height: 16px;
}
.Pixso-symbol-5588_13849 {
    width: auto;
    height: auto;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 6px 12px 6px 12px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5588_13850 {
    width: 16px;
    height: 16px;
}
.Pixso-frame-5588_13851 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 6px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5588_13852 {
    width: 8px;
    height: 8px;
}
.Pixso-paragraph-5588_13853 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5588_13854 {
    width: 16px;
    height: 16px;
}
.Pixso-symbol-5588_13066 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 6px 12px 6px 12px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.stroke-wrapper-5588_13066 {
    position: relative;
    width: auto;
    height: auto;
    display: flex;
}
.stroke-5588_13066 {
    position: absolute;
    inset: 0px;
    border-radius: 1234px 1234px 1234px 1234px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5588_13067 {
    width: 16px;
    height: 16px;
}
.Pixso-frame-5588_13068 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 6px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5588_13069 {
    width: 8px;
    height: 8px;
}
.Pixso-paragraph-5588_13070 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5588_13071 {
    width: 16px;
    height: 16px;
}
.Pixso-symbol-5588_11847 {
    width: auto;
    height: auto;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 6px 12px 6px 12px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5588_11848 {
    width: 16px;
    height: 16px;
}
.Pixso-frame-5588_11849 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 6px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5588_11850 {
    width: 8px;
    height: 8px;
}
.Pixso-paragraph-5588_11851 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5588_11852 {
    width: 16px;
    height: 16px;
}
.Pixso-symbol-5588_13072 {
    width: auto;
    height: auto;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 6px;
    justify-content: center;
    align-items: center;
    padding: 4px 10px 4px 10px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5588_13073 {
    width: 16px;
    height: 16px;
}
.Pixso-frame-5588_13074 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 5px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5588_13075 {
    width: 8px;
    height: 8px;
}
.Pixso-paragraph-5588_13076 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5588_13077 {
    width: 16px;
    height: 16px;
}
.Pixso-symbol-5588_13855 {
    width: auto;
    height: auto;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 6px 12px 6px 12px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5588_13856 {
    width: 16px;
    height: 16px;
}
.Pixso-frame-5588_13857 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 6px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5588_13858 {
    width: 8px;
    height: 8px;
}
.Pixso-paragraph-5588_13859 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5588_13860 {
    width: 16px;
    height: 16px;
}
.Pixso-symbol-5588_13078 {
    width: auto;
    height: auto;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 6px;
    justify-content: center;
    align-items: center;
    padding: 4px 10px 4px 10px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5588_13079 {
    width: 16px;
    height: 16px;
}
.Pixso-frame-5588_13080 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 5px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5588_13081 {
    width: 8px;
    height: 8px;
}
.Pixso-paragraph-5588_13082 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5588_13083 {
    width: 16px;
    height: 16px;
}
.Pixso-symbol-5588_12018 {
    width: auto;
    height: auto;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 6px 12px 6px 12px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5588_12019 {
    width: 16px;
    height: 16px;
}
.Pixso-frame-5588_12020 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 6px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5588_12021 {
    width: 8px;
    height: 8px;
}
.Pixso-paragraph-5588_12022 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5588_12023 {
    width: 16px;
    height: 16px;
}
.Pixso-symbol-5588_13084 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 6px;
    justify-content: center;
    align-items: center;
    padding: 4px 10px 4px 10px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.stroke-wrapper-5588_13084 {
    position: relative;
    width: auto;
    height: auto;
    display: flex;
}
.stroke-5588_13084 {
    position: absolute;
    inset: 0px;
    border-radius: 1234px 1234px 1234px 1234px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5588_13085 {
    width: 16px;
    height: 16px;
}
.Pixso-frame-5588_13086 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 5px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5588_13087 {
    width: 8px;
    height: 8px;
}
.Pixso-paragraph-5588_13088 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5588_13089 {
    width: 16px;
    height: 16px;
}
.Pixso-symbol-5588_13861 {
    width: auto;
    height: auto;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 6px 12px 6px 12px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5588_13862 {
    width: 16px;
    height: 16px;
}
.Pixso-frame-5588_13863 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 6px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5588_13864 {
    width: 8px;
    height: 8px;
}
.Pixso-paragraph-5588_13865 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5588_13866 {
    width: 16px;
    height: 16px;
}
.Pixso-symbol-5588_13090 {
    width: auto;
    height: auto;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 6px 12px 6px 12px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5588_13091 {
    width: 16px;
    height: 16px;
}
.Pixso-frame-5588_13092 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 6px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5588_13093 {
    width: 8px;
    height: 8px;
}
.Pixso-paragraph-5588_13094 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5588_13095 {
    width: 16px;
    height: 16px;
}
.Pixso-symbol-5588_12180 {
    width: auto;
    height: auto;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 6px 12px 6px 12px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5588_12181 {
    width: 16px;
    height: 16px;
}
.Pixso-frame-5588_12182 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 6px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5588_12183 {
    width: 8px;
    height: 8px;
}
.Pixso-paragraph-5588_12184 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5588_12185 {
    width: 16px;
    height: 16px;
}
.Pixso-symbol-5588_13096 {
    width: auto;
    height: auto;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 6px 12px 6px 12px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5588_13097 {
    width: 16px;
    height: 16px;
}
.Pixso-frame-5588_13098 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 6px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5588_13099 {
    width: 8px;
    height: 8px;
}
.Pixso-paragraph-5588_13100 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5588_13101 {
    width: 16px;
    height: 16px;
}
.Pixso-symbol-5588_13867 {
    width: auto;
    height: auto;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 6px 12px 6px 12px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5588_13868 {
    width: 16px;
    height: 16px;
}
.Pixso-frame-5588_13869 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 6px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5588_13870 {
    width: 8px;
    height: 8px;
}
.Pixso-paragraph-5588_13871 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5588_13872 {
    width: 16px;
    height: 16px;
}
.Pixso-symbol-5588_13102 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 6px 12px 6px 12px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.stroke-wrapper-5588_13102 {
    position: relative;
    width: auto;
    height: auto;
    display: flex;
}
.stroke-5588_13102 {
    position: absolute;
    inset: 0px;
    border-radius: 1234px 1234px 1234px 1234px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5588_13103 {
    width: 16px;
    height: 16px;
}
.Pixso-frame-5588_13104 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 6px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5588_13105 {
    width: 8px;
    height: 8px;
}
.Pixso-paragraph-5588_13106 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5588_13107 {
    width: 16px;
    height: 16px;
}
.Pixso-symbol-5588_11853 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 6px 12px 6px 12px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.stroke-wrapper-5588_11853 {
    position: relative;
    width: auto;
    height: auto;
    display: flex;
}
.stroke-5588_11853 {
    position: absolute;
    inset: 0px;
    border-radius: 1234px 1234px 1234px 1234px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5588_11854 {
    width: 16px;
    height: 16px;
}
.Pixso-frame-5588_11855 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 6px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5588_11856 {
    width: 8px;
    height: 8px;
}
.Pixso-paragraph-5588_11857 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5588_11858 {
    width: 16px;
    height: 16px;
}
.Pixso-symbol-5588_13108 {
    width: auto;
    height: auto;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
    padding: 4px 8px 4px 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5588_13109 {
    width: 12px;
    height: 12px;
}
.Pixso-frame-5588_13110 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5588_13111 {
    width: 8px;
    height: 8px;
}
.Pixso-paragraph-5588_13112 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5588_13113 {
    width: 12px;
    height: 12px;
}
.Pixso-symbol-5588_13873 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 6px 12px 6px 12px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.stroke-wrapper-5588_13873 {
    position: relative;
    width: auto;
    height: auto;
    display: flex;
}
.stroke-5588_13873 {
    position: absolute;
    inset: 0px;
    border-radius: 1234px 1234px 1234px 1234px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5588_13874 {
    width: 16px;
    height: 16px;
}
.Pixso-frame-5588_13875 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 6px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5588_13876 {
    width: 8px;
    height: 8px;
}
.Pixso-paragraph-5588_13877 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5588_13878 {
    width: 16px;
    height: 16px;
}
.Pixso-symbol-5588_13114 {
    width: auto;
    height: auto;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
    padding: 4px 8px 4px 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5588_13115 {
    width: 12px;
    height: 12px;
}
.Pixso-frame-5588_13116 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5588_13117 {
    width: 8px;
    height: 8px;
}
.Pixso-paragraph-5588_13118 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5588_13119 {
    width: 12px;
    height: 12px;
}
.Pixso-symbol-5588_12024 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 6px 12px 6px 12px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.stroke-wrapper-5588_12024 {
    position: relative;
    width: auto;
    height: auto;
    display: flex;
}
.stroke-5588_12024 {
    position: absolute;
    inset: 0px;
    border-radius: 1234px 1234px 1234px 1234px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5588_12025 {
    width: 16px;
    height: 16px;
}
.Pixso-frame-5588_12026 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 6px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5588_12027 {
    width: 8px;
    height: 8px;
}
.Pixso-paragraph-5588_12028 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5588_12029 {
    width: 16px;
    height: 16px;
}
.Pixso-symbol-5588_13120 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
    padding: 4px 8px 4px 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.stroke-wrapper-5588_13120 {
    position: relative;
    width: auto;
    height: auto;
    display: flex;
}
.stroke-5588_13120 {
    position: absolute;
    inset: 0px;
    border-radius: 1234px 1234px 1234px 1234px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5588_13121 {
    width: 12px;
    height: 12px;
}
.Pixso-frame-5588_13122 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5588_13123 {
    width: 8px;
    height: 8px;
}
.Pixso-paragraph-5588_13124 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5588_13125 {
    width: 12px;
    height: 12px;
}
.Pixso-symbol-5588_13879 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 6px 12px 6px 12px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.stroke-wrapper-5588_13879 {
    position: relative;
    width: auto;
    height: auto;
    display: flex;
}
.stroke-5588_13879 {
    position: absolute;
    inset: 0px;
    border-radius: 1234px 1234px 1234px 1234px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5588_13880 {
    width: 16px;
    height: 16px;
}
.Pixso-frame-5588_13881 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 6px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5588_13882 {
    width: 8px;
    height: 8px;
}
.Pixso-paragraph-5588_13883 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5588_13884 {
    width: 16px;
    height: 16px;
}
.Pixso-symbol-5588_13126 {
    width: auto;
    height: auto;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 6px;
    justify-content: center;
    align-items: center;
    padding: 4px 10px 4px 10px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5588_13127 {
    width: 16px;
    height: 16px;
}
.Pixso-frame-5588_13128 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 5px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5588_13129 {
    width: 8px;
    height: 8px;
}
.Pixso-paragraph-5588_13130 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5588_13131 {
    width: 16px;
    height: 16px;
}
.Pixso-symbol-5588_12186 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 6px 12px 6px 12px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.stroke-wrapper-5588_12186 {
    position: relative;
    width: auto;
    height: auto;
    display: flex;
}
.stroke-5588_12186 {
    position: absolute;
    inset: 0px;
    border-radius: 1234px 1234px 1234px 1234px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5588_12187 {
    width: 16px;
    height: 16px;
}
.Pixso-frame-5588_12188 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 6px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5588_12189 {
    width: 8px;
    height: 8px;
}
.Pixso-paragraph-5588_12190 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5588_12191 {
    width: 16px;
    height: 16px;
}
.Pixso-symbol-5588_13132 {
    width: auto;
    height: auto;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 6px;
    justify-content: center;
    align-items: center;
    padding: 4px 10px 4px 10px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5588_13133 {
    width: 16px;
    height: 16px;
}
.Pixso-frame-5588_13134 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 5px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5588_13135 {
    width: 8px;
    height: 8px;
}
.Pixso-paragraph-5588_13136 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5588_13137 {
    width: 16px;
    height: 16px;
}
.Pixso-symbol-5588_13885 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 6px 12px 6px 12px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.stroke-wrapper-5588_13885 {
    position: relative;
    width: auto;
    height: auto;
    display: flex;
}
.stroke-5588_13885 {
    position: absolute;
    inset: 0px;
    border-radius: 1234px 1234px 1234px 1234px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5588_13886 {
    width: 16px;
    height: 16px;
}
.Pixso-frame-5588_13887 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 6px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5588_13888 {
    width: 8px;
    height: 8px;
}
.Pixso-paragraph-5588_13889 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5588_13890 {
    width: 16px;
    height: 16px;
}
.Pixso-symbol-5588_13138 {
    width: auto;
    height: auto;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 6px;
    justify-content: center;
    align-items: center;
    padding: 4px 10px 4px 10px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5588_13139 {
    width: 16px;
    height: 16px;
}
.Pixso-frame-5588_13140 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 5px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5588_13141 {
    width: 8px;
    height: 8px;
}
.Pixso-paragraph-5588_13142 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5588_13143 {
    width: 16px;
    height: 16px;
}
.Pixso-symbol-5588_11163 {
    width: auto;
    height: auto;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 6px;
    justify-content: center;
    align-items: center;
    padding: 4px 10px 4px 10px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5588_11164 {
    width: 16px;
    height: 16px;
}
.Pixso-frame-5588_11215 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 5px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5588_11165 {
    width: 8px;
    height: 8px;
}
.Pixso-paragraph-5588_11166 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5588_11167 {
    width: 16px;
    height: 16px;
}
.Pixso-symbol-5588_13144 {
    width: auto;
    height: auto;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 6px;
    justify-content: center;
    align-items: center;
    padding: 4px 10px 4px 10px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5588_13145 {
    width: 16px;
    height: 16px;
}
.Pixso-frame-5588_13146 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 5px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5588_13147 {
    width: 8px;
    height: 8px;
}
.Pixso-paragraph-5588_13148 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5588_13149 {
    width: 16px;
    height: 16px;
}
.Pixso-symbol-5588_13891 {
    width: auto;
    height: auto;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 6px;
    justify-content: center;
    align-items: center;
    padding: 4px 10px 4px 10px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5588_13892 {
    width: 16px;
    height: 16px;
}
.Pixso-frame-5588_13893 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 5px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5588_13894 {
    width: 8px;
    height: 8px;
}
.Pixso-paragraph-5588_13895 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5588_13896 {
    width: 16px;
    height: 16px;
}
.Pixso-symbol-5588_13150 {
    width: auto;
    height: auto;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 6px;
    justify-content: center;
    align-items: center;
    padding: 4px 10px 4px 10px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5588_13151 {
    width: 16px;
    height: 16px;
}
.Pixso-frame-5588_13152 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 5px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5588_13153 {
    width: 8px;
    height: 8px;
}
.Pixso-paragraph-5588_13154 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5588_13155 {
    width: 16px;
    height: 16px;
}
.Pixso-symbol-5588_11352 {
    width: auto;
    height: auto;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 6px;
    justify-content: center;
    align-items: center;
    padding: 4px 10px 4px 10px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5588_11353 {
    width: 16px;
    height: 16px;
}
.Pixso-frame-5588_11354 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 5px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5588_11355 {
    width: 8px;
    height: 8px;
}
.Pixso-paragraph-5588_11356 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5588_11357 {
    width: 16px;
    height: 16px;
}
.Pixso-symbol-5588_13156 {
    width: auto;
    height: auto;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 6px;
    justify-content: center;
    align-items: center;
    padding: 4px 10px 4px 10px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5588_13157 {
    width: 16px;
    height: 16px;
}
.Pixso-frame-5588_13158 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 5px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5588_13159 {
    width: 8px;
    height: 8px;
}
.Pixso-paragraph-5588_13160 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5588_13161 {
    width: 16px;
    height: 16px;
}
.Pixso-symbol-5588_13897 {
    width: auto;
    height: auto;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 6px;
    justify-content: center;
    align-items: center;
    padding: 4px 10px 4px 10px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5588_13898 {
    width: 16px;
    height: 16px;
}
.Pixso-frame-5588_13899 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 5px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5588_13900 {
    width: 8px;
    height: 8px;
}
.Pixso-paragraph-5588_13901 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5588_13902 {
    width: 16px;
    height: 16px;
}
.Pixso-symbol-5588_13162 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 6px;
    justify-content: center;
    align-items: center;
    padding: 4px 10px 4px 10px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.stroke-wrapper-5588_13162 {
    position: relative;
    width: auto;
    height: auto;
    display: flex;
}
.stroke-5588_13162 {
    position: absolute;
    inset: 0px;
    border-radius: 1234px 1234px 1234px 1234px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5588_13163 {
    width: 16px;
    height: 16px;
}
.Pixso-frame-5588_13164 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 5px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5588_13165 {
    width: 8px;
    height: 8px;
}
.Pixso-paragraph-5588_13166 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5588_13167 {
    width: 16px;
    height: 16px;
}
.Pixso-symbol-5588_11415 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 6px;
    justify-content: center;
    align-items: center;
    padding: 4px 10px 4px 10px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.stroke-wrapper-5588_11415 {
    position: relative;
    width: auto;
    height: auto;
    display: flex;
}
.stroke-5588_11415 {
    position: absolute;
    inset: 0px;
    border-radius: 1234px 1234px 1234px 1234px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5588_11416 {
    width: 16px;
    height: 16px;
}
.Pixso-frame-5588_11417 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 5px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5588_11418 {
    width: 8px;
    height: 8px;
}
.Pixso-paragraph-5588_11419 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5588_11420 {
    width: 16px;
    height: 16px;
}
.Pixso-symbol-5588_13168 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 6px;
    justify-content: center;
    align-items: center;
    padding: 4px 10px 4px 10px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.stroke-wrapper-5588_13168 {
    position: relative;
    width: auto;
    height: auto;
    display: flex;
}
.stroke-5588_13168 {
    position: absolute;
    inset: 0px;
    border-radius: 1234px 1234px 1234px 1234px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5588_13169 {
    width: 16px;
    height: 16px;
}
.Pixso-frame-5588_13170 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 5px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5588_13171 {
    width: 8px;
    height: 8px;
}
.Pixso-paragraph-5588_13172 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5588_13173 {
    width: 16px;
    height: 16px;
}
.Pixso-symbol-5588_13903 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 6px;
    justify-content: center;
    align-items: center;
    padding: 4px 10px 4px 10px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.stroke-wrapper-5588_13903 {
    position: relative;
    width: auto;
    height: auto;
    display: flex;
}
.stroke-5588_13903 {
    position: absolute;
    inset: 0px;
    border-radius: 1234px 1234px 1234px 1234px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5588_13904 {
    width: 16px;
    height: 16px;
}
.Pixso-frame-5588_13905 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 5px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5588_13906 {
    width: 8px;
    height: 8px;
}
.Pixso-paragraph-5588_13907 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5588_13908 {
    width: 16px;
    height: 16px;
}
.Pixso-symbol-5588_13174 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 6px;
    justify-content: center;
    align-items: center;
    padding: 4px 10px 4px 10px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.stroke-wrapper-5588_13174 {
    position: relative;
    width: auto;
    height: auto;
    display: flex;
}
.stroke-5588_13174 {
    position: absolute;
    inset: 0px;
    border-radius: 1234px 1234px 1234px 1234px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5588_13175 {
    width: 16px;
    height: 16px;
}
.Pixso-frame-5588_13176 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 5px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5588_13177 {
    width: 8px;
    height: 8px;
}
.Pixso-paragraph-5588_13178 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5588_13179 {
    width: 16px;
    height: 16px;
}
.Pixso-symbol-5588_11517 {
    width: auto;
    height: auto;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 6px 12px 6px 12px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5588_11518 {
    width: 16px;
    height: 16px;
}
.Pixso-frame-5588_11519 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 6px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5588_11520 {
    width: 8px;
    height: 8px;
}
.Pixso-paragraph-5588_11521 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5588_11522 {
    width: 16px;
    height: 16px;
}
.Pixso-symbol-5588_13180 {
    width: auto;
    height: auto;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 6px;
    justify-content: center;
    align-items: center;
    padding: 4px 10px 4px 10px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5588_13181 {
    width: 16px;
    height: 16px;
}
.Pixso-frame-5588_13182 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 5px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5588_13183 {
    width: 8px;
    height: 8px;
}
.Pixso-paragraph-5588_13184 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5588_13185 {
    width: 16px;
    height: 16px;
}
.Pixso-symbol-5588_13909 {
    width: auto;
    height: auto;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 6px 12px 6px 12px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5588_13910 {
    width: 16px;
    height: 16px;
}
.Pixso-frame-5588_13911 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 6px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5588_13912 {
    width: 8px;
    height: 8px;
}
.Pixso-paragraph-5588_13913 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5588_13914 {
    width: 16px;
    height: 16px;
}
.Pixso-symbol-5588_13186 {
    width: auto;
    height: auto;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 6px;
    justify-content: center;
    align-items: center;
    padding: 4px 10px 4px 10px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5588_13187 {
    width: 16px;
    height: 16px;
}
.Pixso-frame-5588_13188 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 5px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5588_13189 {
    width: 8px;
    height: 8px;
}
.Pixso-paragraph-5588_13190 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5588_13191 {
    width: 16px;
    height: 16px;
}
.Pixso-symbol-5588_11535 {
    width: auto;
    height: auto;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 6px 12px 6px 12px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5588_11536 {
    width: 16px;
    height: 16px;
}
.Pixso-frame-5588_11537 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 6px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5588_11538 {
    width: 8px;
    height: 8px;
}
.Pixso-paragraph-5588_11539 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5588_11540 {
    width: 16px;
    height: 16px;
}
.Pixso-symbol-5588_13192 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 6px;
    justify-content: center;
    align-items: center;
    padding: 4px 10px 4px 10px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.stroke-wrapper-5588_13192 {
    position: relative;
    width: auto;
    height: auto;
    display: flex;
}
.stroke-5588_13192 {
    position: absolute;
    inset: 0px;
    border-radius: 1234px 1234px 1234px 1234px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5588_13193 {
    width: 16px;
    height: 16px;
}
.Pixso-frame-5588_13194 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 5px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5588_13195 {
    width: 8px;
    height: 8px;
}
.Pixso-paragraph-5588_13196 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5588_13197 {
    width: 16px;
    height: 16px;
}
.Pixso-symbol-5588_13915 {
    width: auto;
    height: auto;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 6px 12px 6px 12px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5588_13916 {
    width: 16px;
    height: 16px;
}
.Pixso-frame-5588_13917 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 6px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5588_13918 {
    width: 8px;
    height: 8px;
}
.Pixso-paragraph-5588_13919 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5588_13920 {
    width: 16px;
    height: 16px;
}
.Pixso-symbol-5588_13198 {
    width: auto;
    height: auto;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
    padding: 4px 8px 4px 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5588_13199 {
    width: 12px;
    height: 12px;
}
.Pixso-frame-5588_13200 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5588_13201 {
    width: 8px;
    height: 8px;
}
.Pixso-paragraph-5588_13202 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5588_13203 {
    width: 12px;
    height: 12px;
}
.Pixso-symbol-5588_11541 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 6px 12px 6px 12px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.stroke-wrapper-5588_11541 {
    position: relative;
    width: auto;
    height: auto;
    display: flex;
}
.stroke-5588_11541 {
    position: absolute;
    inset: 0px;
    border-radius: 1234px 1234px 1234px 1234px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5588_11542 {
    width: 16px;
    height: 16px;
}
.Pixso-frame-5588_11543 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 6px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5588_11544 {
    width: 8px;
    height: 8px;
}
.Pixso-paragraph-5588_11545 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5588_11546 {
    width: 16px;
    height: 16px;
}
.Pixso-symbol-5588_13204 {
    width: auto;
    height: auto;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
    padding: 4px 8px 4px 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5588_13205 {
    width: 12px;
    height: 12px;
}
.Pixso-frame-5588_13206 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5588_13207 {
    width: 8px;
    height: 8px;
}
.Pixso-paragraph-5588_13208 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5588_13209 {
    width: 12px;
    height: 12px;
}
.Pixso-symbol-5588_13921 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 6px 12px 6px 12px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.stroke-wrapper-5588_13921 {
    position: relative;
    width: auto;
    height: auto;
    display: flex;
}
.stroke-5588_13921 {
    position: absolute;
    inset: 0px;
    border-radius: 1234px 1234px 1234px 1234px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5588_13922 {
    width: 16px;
    height: 16px;
}
.Pixso-frame-5588_13923 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 6px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5588_13924 {
    width: 8px;
    height: 8px;
}
.Pixso-paragraph-5588_13925 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5588_13926 {
    width: 16px;
    height: 16px;
}
.Pixso-symbol-5588_13210 {
    width: auto;
    height: auto;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
    padding: 4px 8px 4px 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5588_13211 {
    width: 12px;
    height: 12px;
}
.Pixso-frame-5588_13212 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5588_13213 {
    width: 8px;
    height: 8px;
}
.Pixso-paragraph-5588_13214 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5588_13215 {
    width: 12px;
    height: 12px;
}
.Pixso-symbol-5494_4827 {
    width: auto;
    height: auto;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
    padding: 4px 8px 4px 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5494_4828 {
    width: 12px;
    height: 12px;
}
.Pixso-frame-5588_11214 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5586_11117 {
    width: 8px;
    height: 8px;
}
.Pixso-paragraph-5494_4829 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5586_11112 {
    width: 12px;
    height: 12px;
}
.Pixso-symbol-5588_13216 {
    width: auto;
    height: auto;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
    padding: 4px 8px 4px 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5588_13217 {
    width: 12px;
    height: 12px;
}
.Pixso-frame-5588_13218 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5588_13219 {
    width: 8px;
    height: 8px;
}
.Pixso-paragraph-5588_13220 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5588_13221 {
    width: 12px;
    height: 12px;
}
.Pixso-symbol-5588_13927 {
    width: auto;
    height: auto;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
    padding: 4px 8px 4px 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5588_13928 {
    width: 12px;
    height: 12px;
}
.Pixso-frame-5588_13929 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5588_13930 {
    width: 8px;
    height: 8px;
}
.Pixso-paragraph-5588_13931 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5588_13932 {
    width: 12px;
    height: 12px;
}
.Pixso-symbol-5588_13222 {
    width: auto;
    height: auto;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
    padding: 4px 8px 4px 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5588_13223 {
    width: 12px;
    height: 12px;
}
.Pixso-frame-5588_13224 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5588_13225 {
    width: 8px;
    height: 8px;
}
.Pixso-paragraph-5588_13226 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5588_13227 {
    width: 12px;
    height: 12px;
}
.Pixso-symbol-5588_11358 {
    width: auto;
    height: auto;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
    padding: 4px 8px 4px 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-frame-5588_11360 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-symbol-5588_13228 {
    width: auto;
    height: auto;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
    padding: 4px 8px 4px 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5588_13229 {
    width: 12px;
    height: 12px;
}
.Pixso-frame-5588_13230 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5588_13231 {
    width: 8px;
    height: 8px;
}
.Pixso-paragraph-5588_13232 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5588_13233 {
    width: 12px;
    height: 12px;
}
.Pixso-symbol-5588_13933 {
    width: auto;
    height: auto;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
    padding: 4px 8px 4px 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5588_13934 {
    width: 12px;
    height: 12px;
}
.Pixso-frame-5588_13935 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5588_13936 {
    width: 8px;
    height: 8px;
}
.Pixso-paragraph-5588_13937 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5588_13938 {
    width: 12px;
    height: 12px;
}
.Pixso-symbol-5588_13234 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
    padding: 4px 8px 4px 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.stroke-wrapper-5588_13234 {
    position: relative;
    width: auto;
    height: auto;
    display: flex;
}
.stroke-5588_13234 {
    position: absolute;
    inset: 0px;
    border-radius: 1234px 1234px 1234px 1234px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5588_13235 {
    width: 12px;
    height: 12px;
}
.Pixso-frame-5588_13236 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5588_13237 {
    width: 8px;
    height: 8px;
}
.Pixso-paragraph-5588_13238 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5588_13239 {
    width: 12px;
    height: 12px;
}
.Pixso-symbol-5588_11421 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
    padding: 4px 8px 4px 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.stroke-wrapper-5588_11421 {
    position: relative;
    width: auto;
    height: auto;
    display: flex;
}
.stroke-5588_11421 {
    position: absolute;
    inset: 0px;
    border-radius: 1234px 1234px 1234px 1234px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5588_11422 {
    width: 12px;
    height: 12px;
}
.Pixso-frame-5588_11423 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5588_11424 {
    width: 8px;
    height: 8px;
}
.Pixso-paragraph-5588_11425 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5588_11426 {
    width: 12px;
    height: 12px;
}
.Pixso-symbol-5588_13240 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
    padding: 4px 8px 4px 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.stroke-wrapper-5588_13240 {
    position: relative;
    width: auto;
    height: auto;
    display: flex;
}
.stroke-5588_13240 {
    position: absolute;
    inset: 0px;
    border-radius: 1234px 1234px 1234px 1234px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5588_13241 {
    width: 12px;
    height: 12px;
}
.Pixso-frame-5588_13242 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5588_13243 {
    width: 8px;
    height: 8px;
}
.Pixso-paragraph-5588_13244 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5588_13245 {
    width: 12px;
    height: 12px;
}
.Pixso-symbol-5588_13939 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
    padding: 4px 8px 4px 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.stroke-wrapper-5588_13939 {
    position: relative;
    width: auto;
    height: auto;
    display: flex;
}
.stroke-5588_13939 {
    position: absolute;
    inset: 0px;
    border-radius: 1234px 1234px 1234px 1234px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5588_13940 {
    width: 12px;
    height: 12px;
}
.Pixso-frame-5588_13941 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5588_13942 {
    width: 8px;
    height: 8px;
}
.Pixso-paragraph-5588_13943 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5588_13944 {
    width: 12px;
    height: 12px;
}
.Pixso-symbol-5588_13246 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
    padding: 4px 8px 4px 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.stroke-wrapper-5588_13246 {
    position: relative;
    width: auto;
    height: auto;
    display: flex;
}
.stroke-5588_13246 {
    position: absolute;
    inset: 0px;
    border-radius: 1234px 1234px 1234px 1234px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5588_13247 {
    width: 12px;
    height: 12px;
}
.Pixso-frame-5588_13248 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5588_13249 {
    width: 8px;
    height: 8px;
}
.Pixso-paragraph-5588_13250 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5588_13251 {
    width: 12px;
    height: 12px;
}
.Pixso-symbol-5588_11859 {
    width: auto;
    height: auto;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 6px;
    justify-content: center;
    align-items: center;
    padding: 4px 10px 4px 10px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5588_11860 {
    width: 16px;
    height: 16px;
}
.Pixso-frame-5588_11861 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 5px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5588_11862 {
    width: 8px;
    height: 8px;
}
.Pixso-paragraph-5588_11863 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5588_11864 {
    width: 16px;
    height: 16px;
}
.Pixso-symbol-5588_13252 {
    width: auto;
    height: auto;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
    padding: 4px 8px 4px 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5588_13253 {
    width: 12px;
    height: 12px;
}
.Pixso-frame-5588_13254 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5588_13255 {
    width: 8px;
    height: 8px;
}
.Pixso-paragraph-5588_13256 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5588_13257 {
    width: 12px;
    height: 12px;
}
.Pixso-symbol-5588_13945 {
    width: auto;
    height: auto;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 6px;
    justify-content: center;
    align-items: center;
    padding: 4px 10px 4px 10px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5588_13946 {
    width: 16px;
    height: 16px;
}
.Pixso-frame-5588_13947 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 5px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5588_13948 {
    width: 8px;
    height: 8px;
}
.Pixso-paragraph-5588_13949 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5588_13950 {
    width: 16px;
    height: 16px;
}
.Pixso-symbol-5588_13258 {
    width: auto;
    height: auto;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
    padding: 4px 8px 4px 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5588_13259 {
    width: 12px;
    height: 12px;
}
.Pixso-frame-5588_13260 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5588_13261 {
    width: 8px;
    height: 8px;
}
.Pixso-paragraph-5588_13262 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5588_13263 {
    width: 12px;
    height: 12px;
}
.Pixso-symbol-5588_12030 {
    width: auto;
    height: auto;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 6px;
    justify-content: center;
    align-items: center;
    padding: 4px 10px 4px 10px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5588_12031 {
    width: 16px;
    height: 16px;
}
.Pixso-frame-5588_12032 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 5px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5588_12033 {
    width: 8px;
    height: 8px;
}
.Pixso-paragraph-5588_12034 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5588_12035 {
    width: 16px;
    height: 16px;
}
.Pixso-symbol-5588_13264 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
    padding: 4px 8px 4px 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.stroke-wrapper-5588_13264 {
    position: relative;
    width: auto;
    height: auto;
    display: flex;
}
.stroke-5588_13264 {
    position: absolute;
    inset: 0px;
    border-radius: 1234px 1234px 1234px 1234px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5588_13265 {
    width: 12px;
    height: 12px;
}
.Pixso-frame-5588_13266 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5588_13267 {
    width: 8px;
    height: 8px;
}
.Pixso-paragraph-5588_13268 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5588_13269 {
    width: 12px;
    height: 12px;
}
.Pixso-symbol-5588_13951 {
    width: auto;
    height: auto;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 6px;
    justify-content: center;
    align-items: center;
    padding: 4px 10px 4px 10px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5588_13952 {
    width: 16px;
    height: 16px;
}
.Pixso-frame-5588_13953 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 5px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5588_13954 {
    width: 8px;
    height: 8px;
}
.Pixso-paragraph-5588_13955 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5588_13956 {
    width: 16px;
    height: 16px;
}
.Pixso-symbol-5588_12192 {
    width: auto;
    height: auto;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 6px;
    justify-content: center;
    align-items: center;
    padding: 4px 10px 4px 10px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5588_12193 {
    width: 16px;
    height: 16px;
}
.Pixso-frame-5588_12194 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 5px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5588_12195 {
    width: 8px;
    height: 8px;
}
.Pixso-paragraph-5588_12196 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5588_12197 {
    width: 16px;
    height: 16px;
}
.Pixso-symbol-5588_13957 {
    width: auto;
    height: auto;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 6px;
    justify-content: center;
    align-items: center;
    padding: 4px 10px 4px 10px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5588_13958 {
    width: 16px;
    height: 16px;
}
.Pixso-frame-5588_13959 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 5px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5588_13960 {
    width: 8px;
    height: 8px;
}
.Pixso-paragraph-5588_13961 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5588_13962 {
    width: 16px;
    height: 16px;
}
.Pixso-symbol-5588_11865 {
    width: auto;
    height: auto;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 6px;
    justify-content: center;
    align-items: center;
    padding: 4px 10px 4px 10px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5588_11866 {
    width: 16px;
    height: 16px;
}
.Pixso-frame-5588_11867 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 5px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5588_11868 {
    width: 8px;
    height: 8px;
}
.Pixso-paragraph-5588_11869 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5588_11870 {
    width: 16px;
    height: 16px;
}
.Pixso-symbol-5588_13963 {
    width: auto;
    height: auto;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 6px;
    justify-content: center;
    align-items: center;
    padding: 4px 10px 4px 10px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5588_13964 {
    width: 16px;
    height: 16px;
}
.Pixso-frame-5588_13965 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 5px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5588_13966 {
    width: 8px;
    height: 8px;
}
.Pixso-paragraph-5588_13967 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5588_13968 {
    width: 16px;
    height: 16px;
}
.Pixso-symbol-5588_12036 {
    width: auto;
    height: auto;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 6px;
    justify-content: center;
    align-items: center;
    padding: 4px 10px 4px 10px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5588_12037 {
    width: 16px;
    height: 16px;
}
.Pixso-frame-5588_12038 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 5px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5588_12039 {
    width: 8px;
    height: 8px;
}
.Pixso-paragraph-5588_12040 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5588_12041 {
    width: 16px;
    height: 16px;
}
.Pixso-symbol-5588_13969 {
    width: auto;
    height: auto;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 6px;
    justify-content: center;
    align-items: center;
    padding: 4px 10px 4px 10px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5588_13970 {
    width: 16px;
    height: 16px;
}
.Pixso-frame-5588_13971 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 5px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5588_13972 {
    width: 8px;
    height: 8px;
}
.Pixso-paragraph-5588_13973 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5588_13974 {
    width: 16px;
    height: 16px;
}
.Pixso-symbol-5588_12198 {
    width: auto;
    height: auto;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 6px;
    justify-content: center;
    align-items: center;
    padding: 4px 10px 4px 10px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5588_12199 {
    width: 16px;
    height: 16px;
}
.Pixso-frame-5588_12200 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 5px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5588_12201 {
    width: 8px;
    height: 8px;
}
.Pixso-paragraph-5588_12202 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5588_12203 {
    width: 16px;
    height: 16px;
}
.Pixso-symbol-5588_13975 {
    width: auto;
    height: auto;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 6px;
    justify-content: center;
    align-items: center;
    padding: 4px 10px 4px 10px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5588_13976 {
    width: 16px;
    height: 16px;
}
.Pixso-frame-5588_13977 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 5px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5588_13978 {
    width: 8px;
    height: 8px;
}
.Pixso-paragraph-5588_13979 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5588_13980 {
    width: 16px;
    height: 16px;
}
.Pixso-symbol-5588_11871 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 6px;
    justify-content: center;
    align-items: center;
    padding: 4px 10px 4px 10px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.stroke-wrapper-5588_11871 {
    position: relative;
    width: auto;
    height: auto;
    display: flex;
}
.stroke-5588_11871 {
    position: absolute;
    inset: 0px;
    border-radius: 1234px 1234px 1234px 1234px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5588_11872 {
    width: 16px;
    height: 16px;
}
.Pixso-frame-5588_11873 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 5px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5588_11874 {
    width: 8px;
    height: 8px;
}
.Pixso-paragraph-5588_11875 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5588_11876 {
    width: 16px;
    height: 16px;
}
.Pixso-symbol-5588_13981 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 6px;
    justify-content: center;
    align-items: center;
    padding: 4px 10px 4px 10px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.stroke-wrapper-5588_13981 {
    position: relative;
    width: auto;
    height: auto;
    display: flex;
}
.stroke-5588_13981 {
    position: absolute;
    inset: 0px;
    border-radius: 1234px 1234px 1234px 1234px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5588_13982 {
    width: 16px;
    height: 16px;
}
.Pixso-frame-5588_13983 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 5px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5588_13984 {
    width: 8px;
    height: 8px;
}
.Pixso-paragraph-5588_13985 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5588_13986 {
    width: 16px;
    height: 16px;
}
.Pixso-symbol-5588_12042 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 6px;
    justify-content: center;
    align-items: center;
    padding: 4px 10px 4px 10px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.stroke-wrapper-5588_12042 {
    position: relative;
    width: auto;
    height: auto;
    display: flex;
}
.stroke-5588_12042 {
    position: absolute;
    inset: 0px;
    border-radius: 1234px 1234px 1234px 1234px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5588_12043 {
    width: 16px;
    height: 16px;
}
.Pixso-frame-5588_12044 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 5px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5588_12045 {
    width: 8px;
    height: 8px;
}
.Pixso-paragraph-5588_12046 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5588_12047 {
    width: 16px;
    height: 16px;
}
.Pixso-symbol-5588_13987 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 6px;
    justify-content: center;
    align-items: center;
    padding: 4px 10px 4px 10px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.stroke-wrapper-5588_13987 {
    position: relative;
    width: auto;
    height: auto;
    display: flex;
}
.stroke-5588_13987 {
    position: absolute;
    inset: 0px;
    border-radius: 1234px 1234px 1234px 1234px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5588_13988 {
    width: 16px;
    height: 16px;
}
.Pixso-frame-5588_13989 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 5px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5588_13990 {
    width: 8px;
    height: 8px;
}
.Pixso-paragraph-5588_13991 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5588_13992 {
    width: 16px;
    height: 16px;
}
.Pixso-symbol-5588_12204 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 6px;
    justify-content: center;
    align-items: center;
    padding: 4px 10px 4px 10px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.stroke-wrapper-5588_12204 {
    position: relative;
    width: auto;
    height: auto;
    display: flex;
}
.stroke-5588_12204 {
    position: absolute;
    inset: 0px;
    border-radius: 1234px 1234px 1234px 1234px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5588_12205 {
    width: 16px;
    height: 16px;
}
.Pixso-frame-5588_12206 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 5px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5588_12207 {
    width: 8px;
    height: 8px;
}
.Pixso-paragraph-5588_12208 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5588_12209 {
    width: 16px;
    height: 16px;
}
.Pixso-symbol-5588_13993 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 6px;
    justify-content: center;
    align-items: center;
    padding: 4px 10px 4px 10px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.stroke-wrapper-5588_13993 {
    position: relative;
    width: auto;
    height: auto;
    display: flex;
}
.stroke-5588_13993 {
    position: absolute;
    inset: 0px;
    border-radius: 1234px 1234px 1234px 1234px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5588_13994 {
    width: 16px;
    height: 16px;
}
.Pixso-frame-5588_13995 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 5px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5588_13996 {
    width: 8px;
    height: 8px;
}
.Pixso-paragraph-5588_13997 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5588_13998 {
    width: 16px;
    height: 16px;
}
.Pixso-symbol-5588_11523 {
    width: auto;
    height: auto;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 6px;
    justify-content: center;
    align-items: center;
    padding: 4px 10px 4px 10px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5588_11524 {
    width: 16px;
    height: 16px;
}
.Pixso-frame-5588_11525 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 5px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5588_11526 {
    width: 8px;
    height: 8px;
}
.Pixso-paragraph-5588_11527 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5588_11528 {
    width: 16px;
    height: 16px;
}
.Pixso-symbol-5588_13999 {
    width: auto;
    height: auto;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 6px;
    justify-content: center;
    align-items: center;
    padding: 4px 10px 4px 10px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5588_14000 {
    width: 16px;
    height: 16px;
}
.Pixso-frame-5588_14001 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 5px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5588_14002 {
    width: 8px;
    height: 8px;
}
.Pixso-paragraph-5588_14003 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5588_14004 {
    width: 16px;
    height: 16px;
}
.Pixso-symbol-5588_11547 {
    width: auto;
    height: auto;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 6px;
    justify-content: center;
    align-items: center;
    padding: 4px 10px 4px 10px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5588_11548 {
    width: 16px;
    height: 16px;
}
.Pixso-frame-5588_11549 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 5px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5588_11550 {
    width: 8px;
    height: 8px;
}
.Pixso-paragraph-5588_11551 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5588_11552 {
    width: 16px;
    height: 16px;
}
.Pixso-symbol-5588_14005 {
    width: auto;
    height: auto;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 6px;
    justify-content: center;
    align-items: center;
    padding: 4px 10px 4px 10px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5588_14006 {
    width: 16px;
    height: 16px;
}
.Pixso-frame-5588_14007 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 5px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5588_14008 {
    width: 8px;
    height: 8px;
}
.Pixso-paragraph-5588_14009 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5588_14010 {
    width: 16px;
    height: 16px;
}
.Pixso-symbol-5588_11553 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 6px;
    justify-content: center;
    align-items: center;
    padding: 4px 10px 4px 10px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.stroke-wrapper-5588_11553 {
    position: relative;
    width: auto;
    height: auto;
    display: flex;
}
.stroke-5588_11553 {
    position: absolute;
    inset: 0px;
    border-radius: 1234px 1234px 1234px 1234px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5588_11554 {
    width: 16px;
    height: 16px;
}
.Pixso-frame-5588_11555 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 5px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5588_11556 {
    width: 8px;
    height: 8px;
}
.Pixso-paragraph-5588_11557 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5588_11558 {
    width: 16px;
    height: 16px;
}
.Pixso-symbol-5588_14011 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 6px;
    justify-content: center;
    align-items: center;
    padding: 4px 10px 4px 10px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.stroke-wrapper-5588_14011 {
    position: relative;
    width: auto;
    height: auto;
    display: flex;
}
.stroke-5588_14011 {
    position: absolute;
    inset: 0px;
    border-radius: 1234px 1234px 1234px 1234px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5588_14012 {
    width: 16px;
    height: 16px;
}
.Pixso-frame-5588_14013 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 5px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5588_14014 {
    width: 8px;
    height: 8px;
}
.Pixso-paragraph-5588_14015 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5588_14016 {
    width: 16px;
    height: 16px;
}
.Pixso-symbol-5588_11877 {
    width: auto;
    height: auto;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
    padding: 4px 8px 4px 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5588_11878 {
    width: 12px;
    height: 12px;
}
.Pixso-frame-5588_11879 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5588_11880 {
    width: 8px;
    height: 8px;
}
.Pixso-paragraph-5588_11881 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5588_11882 {
    width: 12px;
    height: 12px;
}
.Pixso-symbol-5588_14017 {
    width: auto;
    height: auto;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
    padding: 4px 8px 4px 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5588_14018 {
    width: 12px;
    height: 12px;
}
.Pixso-frame-5588_14019 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5588_14020 {
    width: 8px;
    height: 8px;
}
.Pixso-paragraph-5588_14021 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5588_14022 {
    width: 12px;
    height: 12px;
}
.Pixso-symbol-5588_12048 {
    width: auto;
    height: auto;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
    padding: 4px 8px 4px 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5588_12049 {
    width: 12px;
    height: 12px;
}
.Pixso-frame-5588_12050 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5588_12051 {
    width: 8px;
    height: 8px;
}
.Pixso-paragraph-5588_12052 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5588_12053 {
    width: 12px;
    height: 12px;
}
.Pixso-symbol-5588_14023 {
    width: auto;
    height: auto;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
    padding: 4px 8px 4px 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5588_14024 {
    width: 12px;
    height: 12px;
}
.Pixso-frame-5588_14025 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5588_14026 {
    width: 8px;
    height: 8px;
}
.Pixso-paragraph-5588_14027 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5588_14028 {
    width: 12px;
    height: 12px;
}
.Pixso-symbol-5588_12210 {
    width: auto;
    height: auto;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
    padding: 4px 8px 4px 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5588_12211 {
    width: 12px;
    height: 12px;
}
.Pixso-frame-5588_12212 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5588_12213 {
    width: 8px;
    height: 8px;
}
.Pixso-paragraph-5588_12214 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5588_12215 {
    width: 12px;
    height: 12px;
}
.Pixso-symbol-5588_14029 {
    width: auto;
    height: auto;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
    padding: 4px 8px 4px 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5588_14030 {
    width: 12px;
    height: 12px;
}
.Pixso-frame-5588_14031 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5588_14032 {
    width: 8px;
    height: 8px;
}
.Pixso-paragraph-5588_14033 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5588_14034 {
    width: 12px;
    height: 12px;
}
.Pixso-symbol-5588_11883 {
    width: auto;
    height: auto;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
    padding: 4px 8px 4px 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5588_11884 {
    width: 12px;
    height: 12px;
}
.Pixso-frame-5588_11885 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5588_11886 {
    width: 8px;
    height: 8px;
}
.Pixso-paragraph-5588_11887 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5588_11888 {
    width: 12px;
    height: 12px;
}
.Pixso-symbol-5588_14035 {
    width: auto;
    height: auto;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
    padding: 4px 8px 4px 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5588_14036 {
    width: 12px;
    height: 12px;
}
.Pixso-frame-5588_14037 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5588_14038 {
    width: 8px;
    height: 8px;
}
.Pixso-paragraph-5588_14039 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5588_14040 {
    width: 12px;
    height: 12px;
}
.Pixso-symbol-5588_12054 {
    width: auto;
    height: auto;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
    padding: 4px 8px 4px 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5588_12055 {
    width: 12px;
    height: 12px;
}
.Pixso-frame-5588_12056 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5588_12057 {
    width: 8px;
    height: 8px;
}
.Pixso-paragraph-5588_12058 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5588_12059 {
    width: 12px;
    height: 12px;
}
.Pixso-symbol-5588_14041 {
    width: auto;
    height: auto;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
    padding: 4px 8px 4px 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5588_14042 {
    width: 12px;
    height: 12px;
}
.Pixso-frame-5588_14043 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5588_14044 {
    width: 8px;
    height: 8px;
}
.Pixso-paragraph-5588_14045 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5588_14046 {
    width: 12px;
    height: 12px;
}
.Pixso-symbol-5588_12216 {
    width: auto;
    height: auto;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
    padding: 4px 8px 4px 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5588_12217 {
    width: 12px;
    height: 12px;
}
.Pixso-frame-5588_12218 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5588_12219 {
    width: 8px;
    height: 8px;
}
.Pixso-paragraph-5588_12220 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5588_12221 {
    width: 12px;
    height: 12px;
}
.Pixso-symbol-5588_14047 {
    width: auto;
    height: auto;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
    padding: 4px 8px 4px 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5588_14048 {
    width: 12px;
    height: 12px;
}
.Pixso-frame-5588_14049 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5588_14050 {
    width: 8px;
    height: 8px;
}
.Pixso-paragraph-5588_14051 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5588_14052 {
    width: 12px;
    height: 12px;
}
.Pixso-symbol-5588_11889 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
    padding: 4px 8px 4px 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.stroke-wrapper-5588_11889 {
    position: relative;
    width: auto;
    height: auto;
    display: flex;
}
.stroke-5588_11889 {
    position: absolute;
    inset: 0px;
    border-radius: 1234px 1234px 1234px 1234px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5588_11890 {
    width: 12px;
    height: 12px;
}
.Pixso-frame-5588_11891 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5588_11892 {
    width: 8px;
    height: 8px;
}
.Pixso-paragraph-5588_11893 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5588_11894 {
    width: 12px;
    height: 12px;
}
.Pixso-symbol-5588_14053 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
    padding: 4px 8px 4px 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.stroke-wrapper-5588_14053 {
    position: relative;
    width: auto;
    height: auto;
    display: flex;
}
.stroke-5588_14053 {
    position: absolute;
    inset: 0px;
    border-radius: 1234px 1234px 1234px 1234px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5588_14054 {
    width: 12px;
    height: 12px;
}
.Pixso-frame-5588_14055 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5588_14056 {
    width: 8px;
    height: 8px;
}
.Pixso-paragraph-5588_14057 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5588_14058 {
    width: 12px;
    height: 12px;
}
.Pixso-symbol-5588_12060 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
    padding: 4px 8px 4px 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.stroke-wrapper-5588_12060 {
    position: relative;
    width: auto;
    height: auto;
    display: flex;
}
.stroke-5588_12060 {
    position: absolute;
    inset: 0px;
    border-radius: 1234px 1234px 1234px 1234px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5588_12061 {
    width: 12px;
    height: 12px;
}
.Pixso-frame-5588_12062 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5588_12063 {
    width: 8px;
    height: 8px;
}
.Pixso-paragraph-5588_12064 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5588_12065 {
    width: 12px;
    height: 12px;
}
.Pixso-symbol-5588_14059 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
    padding: 4px 8px 4px 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.stroke-wrapper-5588_14059 {
    position: relative;
    width: auto;
    height: auto;
    display: flex;
}
.stroke-5588_14059 {
    position: absolute;
    inset: 0px;
    border-radius: 1234px 1234px 1234px 1234px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5588_14060 {
    width: 12px;
    height: 12px;
}
.Pixso-frame-5588_14061 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5588_14062 {
    width: 8px;
    height: 8px;
}
.Pixso-paragraph-5588_14063 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5588_14064 {
    width: 12px;
    height: 12px;
}
.Pixso-symbol-5588_12222 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
    padding: 4px 8px 4px 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.stroke-wrapper-5588_12222 {
    position: relative;
    width: auto;
    height: auto;
    display: flex;
}
.stroke-5588_12222 {
    position: absolute;
    inset: 0px;
    border-radius: 1234px 1234px 1234px 1234px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5588_12223 {
    width: 12px;
    height: 12px;
}
.Pixso-frame-5588_12224 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5588_12225 {
    width: 8px;
    height: 8px;
}
.Pixso-paragraph-5588_12226 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5588_12227 {
    width: 12px;
    height: 12px;
}
.Pixso-symbol-5588_14065 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
    padding: 4px 8px 4px 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.stroke-wrapper-5588_14065 {
    position: relative;
    width: auto;
    height: auto;
    display: flex;
}
.stroke-5588_14065 {
    position: absolute;
    inset: 0px;
    border-radius: 1234px 1234px 1234px 1234px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5588_14066 {
    width: 12px;
    height: 12px;
}
.Pixso-frame-5588_14067 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5588_14068 {
    width: 8px;
    height: 8px;
}
.Pixso-paragraph-5588_14069 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5588_14070 {
    width: 12px;
    height: 12px;
}
.Pixso-symbol-5588_11529 {
    width: auto;
    height: auto;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
    padding: 4px 8px 4px 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5588_11530 {
    width: 12px;
    height: 12px;
}
.Pixso-frame-5588_11531 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5588_11532 {
    width: 8px;
    height: 8px;
}
.Pixso-paragraph-5588_11533 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5588_11534 {
    width: 12px;
    height: 12px;
}
.Pixso-symbol-5588_14071 {
    width: auto;
    height: auto;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
    padding: 4px 8px 4px 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5588_14072 {
    width: 12px;
    height: 12px;
}
.Pixso-frame-5588_14073 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5588_14074 {
    width: 8px;
    height: 8px;
}
.Pixso-paragraph-5588_14075 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5588_14076 {
    width: 12px;
    height: 12px;
}
.Pixso-symbol-5588_11559 {
    width: auto;
    height: auto;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
    padding: 4px 8px 4px 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5588_11560 {
    width: 12px;
    height: 12px;
}
.Pixso-frame-5588_11561 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5588_11562 {
    width: 8px;
    height: 8px;
}
.Pixso-paragraph-5588_11563 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5588_11564 {
    width: 12px;
    height: 12px;
}
.Pixso-symbol-5588_14077 {
    width: auto;
    height: auto;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
    padding: 4px 8px 4px 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5588_14078 {
    width: 12px;
    height: 12px;
}
.Pixso-frame-5588_14079 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5588_14080 {
    width: 8px;
    height: 8px;
}
.Pixso-paragraph-5588_14081 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5588_14082 {
    width: 12px;
    height: 12px;
}
.Pixso-symbol-5588_11565 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
    padding: 4px 8px 4px 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.stroke-wrapper-5588_11565 {
    position: relative;
    width: auto;
    height: auto;
    display: flex;
}
.stroke-5588_11565 {
    position: absolute;
    inset: 0px;
    border-radius: 1234px 1234px 1234px 1234px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5588_11566 {
    width: 12px;
    height: 12px;
}
.Pixso-frame-5588_11567 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5588_11568 {
    width: 8px;
    height: 8px;
}
.Pixso-paragraph-5588_11569 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5588_11570 {
    width: 12px;
    height: 12px;
}
.Pixso-symbol-5588_14083 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
    padding: 4px 8px 4px 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.stroke-wrapper-5588_14083 {
    position: relative;
    width: auto;
    height: auto;
    display: flex;
}
.stroke-5588_14083 {
    position: absolute;
    inset: 0px;
    border-radius: 1234px 1234px 1234px 1234px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5588_14084 {
    width: 12px;
    height: 12px;
}
.Pixso-frame-5588_14085 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5588_14086 {
    width: 8px;
    height: 8px;
}
.Pixso-paragraph-5588_14087 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5588_14088 {
    width: 12px;
    height: 12px;
}

.Pixso-instance-5588_11191 .Pixso-vector-5578_148942 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5588_11191 .Pixso-symbol-5578_148941 .Pixso-symbol-6042_8547 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_11191 .Pixso-symbol-5578_148941 .Pixso-symbol-5579_151118 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_11191 .Pixso-symbol-5578_148941 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_11194 .Pixso-symbol-5578_149511 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_11194 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5588_13001 .Pixso-vector-5578_148942 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5588_13001 .Pixso-symbol-5578_148941 .Pixso-symbol-6042_8547 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13001 .Pixso-symbol-5578_148941 .Pixso-symbol-5579_151118 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13001 .Pixso-symbol-5578_148941 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13005 .Pixso-symbol-5578_149511 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13005 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5588_13820 .Pixso-vector-5578_148942 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5588_13820 .Pixso-symbol-5578_148941 .Pixso-symbol-6042_8547 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13820 .Pixso-symbol-5578_148941 .Pixso-symbol-5579_151118 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13820 .Pixso-symbol-5578_148941 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13824 .Pixso-symbol-5578_149511 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13824 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5588_13007 .Pixso-vector-5578_148942 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5588_13007 .Pixso-symbol-5578_148941 .Pixso-symbol-6042_8547 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13007 .Pixso-symbol-5578_148941 .Pixso-symbol-5579_151118 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13007 .Pixso-symbol-5578_148941 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13011 .Pixso-symbol-5578_149511 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13011 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5588_11347 .Pixso-vector-5578_148942 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5588_11347 .Pixso-symbol-5578_148941 .Pixso-symbol-6042_8547 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_11347 .Pixso-symbol-5578_148941 .Pixso-symbol-5579_151118 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_11347 .Pixso-symbol-5578_148941 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_11351 .Pixso-symbol-5578_149511 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_11351 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5588_13013 .Pixso-vector-5578_148942 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5588_13013 .Pixso-symbol-5578_148941 .Pixso-symbol-6042_8547 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13013 .Pixso-symbol-5578_148941 .Pixso-symbol-5579_151118 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13013 .Pixso-symbol-5578_148941 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13017 .Pixso-symbol-5578_149511 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13017 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5588_13826 .Pixso-vector-5578_148942 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5588_13826 .Pixso-symbol-5578_148941 .Pixso-symbol-6042_8547 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13826 .Pixso-symbol-5578_148941 .Pixso-symbol-5579_151118 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13826 .Pixso-symbol-5578_148941 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13830 .Pixso-symbol-5578_149511 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13830 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5588_13019 .Pixso-vector-5578_148942 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5588_13019 .Pixso-symbol-5578_148941 .Pixso-symbol-6042_8547 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13019 .Pixso-symbol-5578_148941 .Pixso-symbol-5579_151118 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13019 .Pixso-symbol-5578_148941 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13023 .Pixso-symbol-5578_149511 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13023 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5588_11410 .Pixso-vector-5578_148942 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5588_11410 .Pixso-symbol-5578_148941 .Pixso-symbol-6042_8547 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_11410 .Pixso-symbol-5578_148941 .Pixso-symbol-5579_151118 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_11410 .Pixso-symbol-5578_148941 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_11414 .Pixso-symbol-5578_149511 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_11414 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5588_13025 .Pixso-vector-5578_148942 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5588_13025 .Pixso-symbol-5578_148941 .Pixso-symbol-6042_8547 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13025 .Pixso-symbol-5578_148941 .Pixso-symbol-5579_151118 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13025 .Pixso-symbol-5578_148941 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13029 .Pixso-symbol-5578_149511 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13029 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5588_13832 .Pixso-vector-5578_148942 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5588_13832 .Pixso-symbol-5578_148941 .Pixso-symbol-6042_8547 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13832 .Pixso-symbol-5578_148941 .Pixso-symbol-5579_151118 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13832 .Pixso-symbol-5578_148941 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13836 .Pixso-symbol-5578_149511 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13836 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5588_13031 .Pixso-vector-5578_148942 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5588_13031 .Pixso-symbol-5578_148941 .Pixso-symbol-6042_8547 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13031 .Pixso-symbol-5578_148941 .Pixso-symbol-5579_151118 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13031 .Pixso-symbol-5578_148941 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13035 .Pixso-symbol-5578_149511 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13035 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5588_11842 .Pixso-vector-5578_148942 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5588_11842 .Pixso-symbol-5578_148941 .Pixso-symbol-6042_8547 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_11842 .Pixso-symbol-5578_148941 .Pixso-symbol-5579_151118 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_11842 .Pixso-symbol-5578_148941 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_11846 .Pixso-symbol-5578_149511 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_11846 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5588_13037 .Pixso-vector-5578_148942 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5588_13037 .Pixso-symbol-5578_148941 .Pixso-symbol-6042_8547 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13037 .Pixso-symbol-5578_148941 .Pixso-symbol-5579_151118 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13037 .Pixso-symbol-5578_148941 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13041 .Pixso-symbol-5578_149511 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13041 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5588_13838 .Pixso-vector-5578_148942 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5588_13838 .Pixso-symbol-5578_148941 .Pixso-symbol-6042_8547 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13838 .Pixso-symbol-5578_148941 .Pixso-symbol-5579_151118 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13838 .Pixso-symbol-5578_148941 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13842 .Pixso-symbol-5578_149511 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13842 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5588_13043 .Pixso-vector-5578_148942 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5588_13043 .Pixso-symbol-5578_148941 .Pixso-symbol-6042_8547 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13043 .Pixso-symbol-5578_148941 .Pixso-symbol-5579_151118 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13043 .Pixso-symbol-5578_148941 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13047 .Pixso-symbol-5578_149511 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13047 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5588_12013 .Pixso-vector-5578_148942 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5588_12013 .Pixso-symbol-5578_148941 .Pixso-symbol-6042_8547 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_12013 .Pixso-symbol-5578_148941 .Pixso-symbol-5579_151118 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_12013 .Pixso-symbol-5578_148941 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_12017 .Pixso-symbol-5578_149511 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_12017 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5588_13049 .Pixso-vector-5578_148942 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5588_13049 .Pixso-symbol-5578_148941 .Pixso-symbol-6042_8547 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13049 .Pixso-symbol-5578_148941 .Pixso-symbol-5579_151118 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13049 .Pixso-symbol-5578_148941 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13053 .Pixso-symbol-5578_149511 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13053 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5588_13844 .Pixso-vector-5578_148942 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5588_13844 .Pixso-symbol-5578_148941 .Pixso-symbol-6042_8547 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13844 .Pixso-symbol-5578_148941 .Pixso-symbol-5579_151118 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13844 .Pixso-symbol-5578_148941 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13848 .Pixso-symbol-5578_149511 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13848 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5588_13055 .Pixso-vector-5578_148942 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5588_13055 .Pixso-symbol-5578_148941 .Pixso-symbol-6042_8547 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13055 .Pixso-symbol-5578_148941 .Pixso-symbol-5579_151118 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13055 .Pixso-symbol-5578_148941 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13059 .Pixso-symbol-5578_149511 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13059 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5588_12175 .Pixso-vector-5578_148942 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5588_12175 .Pixso-symbol-5578_148941 .Pixso-symbol-6042_8547 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_12175 .Pixso-symbol-5578_148941 .Pixso-symbol-5579_151118 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_12175 .Pixso-symbol-5578_148941 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_12179 .Pixso-symbol-5578_149511 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_12179 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5588_13061 .Pixso-vector-5578_148942 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5588_13061 .Pixso-symbol-5578_148941 .Pixso-symbol-6042_8547 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13061 .Pixso-symbol-5578_148941 .Pixso-symbol-5579_151118 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13061 .Pixso-symbol-5578_148941 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13065 .Pixso-symbol-5578_149511 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13065 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5588_13850 .Pixso-vector-5578_148942 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5588_13850 .Pixso-symbol-5578_148941 .Pixso-symbol-6042_8547 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13850 .Pixso-symbol-5578_148941 .Pixso-symbol-5579_151118 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13850 .Pixso-symbol-5578_148941 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13854 .Pixso-symbol-5578_149511 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13854 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5588_13067 .Pixso-vector-5578_148942 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5588_13067 .Pixso-symbol-5578_148941 .Pixso-symbol-6042_8547 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13067 .Pixso-symbol-5578_148941 .Pixso-symbol-5579_151118 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13067 .Pixso-symbol-5578_148941 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13071 .Pixso-symbol-5578_149511 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13071 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5588_11848 .Pixso-vector-5578_148942 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5588_11848 .Pixso-symbol-5578_148941 .Pixso-symbol-6042_8547 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_11848 .Pixso-symbol-5578_148941 .Pixso-symbol-5579_151118 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_11848 .Pixso-symbol-5578_148941 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_11852 .Pixso-symbol-5578_149511 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_11852 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5588_13073 .Pixso-vector-5578_148942 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5588_13073 .Pixso-symbol-5578_148941 .Pixso-symbol-6042_8547 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13073 .Pixso-symbol-5578_148941 .Pixso-symbol-5579_151118 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13073 .Pixso-symbol-5578_148941 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13077 .Pixso-symbol-5578_149511 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13077 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5588_13856 .Pixso-vector-5578_148942 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5588_13856 .Pixso-symbol-5578_148941 .Pixso-symbol-6042_8547 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13856 .Pixso-symbol-5578_148941 .Pixso-symbol-5579_151118 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13856 .Pixso-symbol-5578_148941 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13860 .Pixso-symbol-5578_149511 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13860 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5588_13079 .Pixso-vector-5578_148942 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5588_13079 .Pixso-symbol-5578_148941 .Pixso-symbol-6042_8547 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13079 .Pixso-symbol-5578_148941 .Pixso-symbol-5579_151118 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13079 .Pixso-symbol-5578_148941 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13083 .Pixso-symbol-5578_149511 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13083 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5588_12019 .Pixso-vector-5578_148942 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5588_12019 .Pixso-symbol-5578_148941 .Pixso-symbol-6042_8547 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_12019 .Pixso-symbol-5578_148941 .Pixso-symbol-5579_151118 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_12019 .Pixso-symbol-5578_148941 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_12023 .Pixso-symbol-5578_149511 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_12023 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5588_13085 .Pixso-vector-5578_148942 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5588_13085 .Pixso-symbol-5578_148941 .Pixso-symbol-6042_8547 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13085 .Pixso-symbol-5578_148941 .Pixso-symbol-5579_151118 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13085 .Pixso-symbol-5578_148941 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13089 .Pixso-symbol-5578_149511 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13089 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5588_13862 .Pixso-vector-5578_148942 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5588_13862 .Pixso-symbol-5578_148941 .Pixso-symbol-6042_8547 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13862 .Pixso-symbol-5578_148941 .Pixso-symbol-5579_151118 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13862 .Pixso-symbol-5578_148941 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13866 .Pixso-symbol-5578_149511 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13866 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5588_13091 .Pixso-vector-5578_148942 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5588_13091 .Pixso-symbol-5578_148941 .Pixso-symbol-6042_8547 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13091 .Pixso-symbol-5578_148941 .Pixso-symbol-5579_151118 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13091 .Pixso-symbol-5578_148941 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13095 .Pixso-symbol-5578_149511 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13095 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5588_12181 .Pixso-vector-5578_148942 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5588_12181 .Pixso-symbol-5578_148941 .Pixso-symbol-6042_8547 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_12181 .Pixso-symbol-5578_148941 .Pixso-symbol-5579_151118 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_12181 .Pixso-symbol-5578_148941 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_12185 .Pixso-symbol-5578_149511 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_12185 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5588_13097 .Pixso-vector-5578_148942 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5588_13097 .Pixso-symbol-5578_148941 .Pixso-symbol-6042_8547 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13097 .Pixso-symbol-5578_148941 .Pixso-symbol-5579_151118 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13097 .Pixso-symbol-5578_148941 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13101 .Pixso-symbol-5578_149511 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13101 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5588_13868 .Pixso-vector-5578_148942 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5588_13868 .Pixso-symbol-5578_148941 .Pixso-symbol-6042_8547 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13868 .Pixso-symbol-5578_148941 .Pixso-symbol-5579_151118 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13868 .Pixso-symbol-5578_148941 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13872 .Pixso-symbol-5578_149511 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13872 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5588_13103 .Pixso-vector-5578_148942 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5588_13103 .Pixso-symbol-5578_148941 .Pixso-symbol-6042_8547 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13103 .Pixso-symbol-5578_148941 .Pixso-symbol-5579_151118 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13103 .Pixso-symbol-5578_148941 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13107 .Pixso-symbol-5578_149511 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13107 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5588_11854 .Pixso-vector-5578_148942 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5588_11854 .Pixso-symbol-5578_148941 .Pixso-symbol-6042_8547 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_11854 .Pixso-symbol-5578_148941 .Pixso-symbol-5579_151118 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_11854 .Pixso-symbol-5578_148941 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_11858 .Pixso-symbol-5578_149511 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_11858 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5588_13109 .Pixso-vector-5578_148942 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5588_13109 .Pixso-symbol-5578_148941 .Pixso-symbol-6042_8547 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13109 .Pixso-symbol-5578_148941 .Pixso-symbol-5579_151118 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13109 .Pixso-symbol-5578_148941 {
    width: 12px;
    height: 12px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13113 .Pixso-symbol-5578_149511 {
    width: 12px;
    height: 12px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13113 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5588_13874 .Pixso-vector-5578_148942 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5588_13874 .Pixso-symbol-5578_148941 .Pixso-symbol-6042_8547 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13874 .Pixso-symbol-5578_148941 .Pixso-symbol-5579_151118 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13874 .Pixso-symbol-5578_148941 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13878 .Pixso-symbol-5578_149511 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13878 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5588_13115 .Pixso-vector-5578_148942 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5588_13115 .Pixso-symbol-5578_148941 .Pixso-symbol-6042_8547 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13115 .Pixso-symbol-5578_148941 .Pixso-symbol-5579_151118 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13115 .Pixso-symbol-5578_148941 {
    width: 12px;
    height: 12px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13119 .Pixso-symbol-5578_149511 {
    width: 12px;
    height: 12px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13119 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5588_12025 .Pixso-vector-5578_148942 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5588_12025 .Pixso-symbol-5578_148941 .Pixso-symbol-6042_8547 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_12025 .Pixso-symbol-5578_148941 .Pixso-symbol-5579_151118 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_12025 .Pixso-symbol-5578_148941 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_12029 .Pixso-symbol-5578_149511 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_12029 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5588_13121 .Pixso-vector-5578_148942 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5588_13121 .Pixso-symbol-5578_148941 .Pixso-symbol-6042_8547 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13121 .Pixso-symbol-5578_148941 .Pixso-symbol-5579_151118 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13121 .Pixso-symbol-5578_148941 {
    width: 12px;
    height: 12px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13125 .Pixso-symbol-5578_149511 {
    width: 12px;
    height: 12px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13125 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5588_13880 .Pixso-vector-5578_148942 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5588_13880 .Pixso-symbol-5578_148941 .Pixso-symbol-6042_8547 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13880 .Pixso-symbol-5578_148941 .Pixso-symbol-5579_151118 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13880 .Pixso-symbol-5578_148941 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13884 .Pixso-symbol-5578_149511 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13884 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5588_13127 .Pixso-vector-5578_148942 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5588_13127 .Pixso-symbol-5578_148941 .Pixso-symbol-6042_8547 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13127 .Pixso-symbol-5578_148941 .Pixso-symbol-5579_151118 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13127 .Pixso-symbol-5578_148941 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13131 .Pixso-symbol-5578_149511 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13131 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5588_12187 .Pixso-vector-5578_148942 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5588_12187 .Pixso-symbol-5578_148941 .Pixso-symbol-6042_8547 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_12187 .Pixso-symbol-5578_148941 .Pixso-symbol-5579_151118 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_12187 .Pixso-symbol-5578_148941 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_12191 .Pixso-symbol-5578_149511 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_12191 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5588_13133 .Pixso-vector-5578_148942 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5588_13133 .Pixso-symbol-5578_148941 .Pixso-symbol-6042_8547 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13133 .Pixso-symbol-5578_148941 .Pixso-symbol-5579_151118 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13133 .Pixso-symbol-5578_148941 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13137 .Pixso-symbol-5578_149511 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13137 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5588_13886 .Pixso-vector-5578_148942 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5588_13886 .Pixso-symbol-5578_148941 .Pixso-symbol-6042_8547 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13886 .Pixso-symbol-5578_148941 .Pixso-symbol-5579_151118 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13886 .Pixso-symbol-5578_148941 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13890 .Pixso-symbol-5578_149511 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13890 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5588_13139 .Pixso-vector-5578_148942 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5588_13139 .Pixso-symbol-5578_148941 .Pixso-symbol-6042_8547 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13139 .Pixso-symbol-5578_148941 .Pixso-symbol-5579_151118 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13139 .Pixso-symbol-5578_148941 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13143 .Pixso-symbol-5578_149511 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13143 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5588_11164 .Pixso-vector-5578_148942 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5588_11164 .Pixso-symbol-5578_148941 .Pixso-symbol-6042_8547 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_11164 .Pixso-symbol-5578_148941 .Pixso-symbol-5579_151118 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_11164 .Pixso-symbol-5578_148941 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_11167 .Pixso-symbol-5578_149511 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_11167 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5588_13145 .Pixso-vector-5578_148942 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5588_13145 .Pixso-symbol-5578_148941 .Pixso-symbol-6042_8547 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13145 .Pixso-symbol-5578_148941 .Pixso-symbol-5579_151118 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13145 .Pixso-symbol-5578_148941 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13149 .Pixso-symbol-5578_149511 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13149 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5588_13892 .Pixso-vector-5578_148942 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5588_13892 .Pixso-symbol-5578_148941 .Pixso-symbol-6042_8547 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13892 .Pixso-symbol-5578_148941 .Pixso-symbol-5579_151118 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13892 .Pixso-symbol-5578_148941 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13896 .Pixso-symbol-5578_149511 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13896 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5588_13151 .Pixso-vector-5578_148942 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5588_13151 .Pixso-symbol-5578_148941 .Pixso-symbol-6042_8547 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13151 .Pixso-symbol-5578_148941 .Pixso-symbol-5579_151118 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13151 .Pixso-symbol-5578_148941 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13155 .Pixso-symbol-5578_149511 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13155 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5588_11353 .Pixso-vector-5578_148942 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5588_11353 .Pixso-symbol-5578_148941 .Pixso-symbol-6042_8547 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_11353 .Pixso-symbol-5578_148941 .Pixso-symbol-5579_151118 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_11353 .Pixso-symbol-5578_148941 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_11357 .Pixso-symbol-5578_149511 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_11357 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5588_13157 .Pixso-vector-5578_148942 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5588_13157 .Pixso-symbol-5578_148941 .Pixso-symbol-6042_8547 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13157 .Pixso-symbol-5578_148941 .Pixso-symbol-5579_151118 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13157 .Pixso-symbol-5578_148941 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13161 .Pixso-symbol-5578_149511 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13161 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5588_13898 .Pixso-vector-5578_148942 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5588_13898 .Pixso-symbol-5578_148941 .Pixso-symbol-6042_8547 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13898 .Pixso-symbol-5578_148941 .Pixso-symbol-5579_151118 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13898 .Pixso-symbol-5578_148941 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13902 .Pixso-symbol-5578_149511 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13902 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5588_13163 .Pixso-vector-5578_148942 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5588_13163 .Pixso-symbol-5578_148941 .Pixso-symbol-6042_8547 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13163 .Pixso-symbol-5578_148941 .Pixso-symbol-5579_151118 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13163 .Pixso-symbol-5578_148941 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13167 .Pixso-symbol-5578_149511 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13167 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5588_11416 .Pixso-vector-5578_148942 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5588_11416 .Pixso-symbol-5578_148941 .Pixso-symbol-6042_8547 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_11416 .Pixso-symbol-5578_148941 .Pixso-symbol-5579_151118 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_11416 .Pixso-symbol-5578_148941 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_11420 .Pixso-symbol-5578_149511 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_11420 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5588_13169 .Pixso-vector-5578_148942 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5588_13169 .Pixso-symbol-5578_148941 .Pixso-symbol-6042_8547 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13169 .Pixso-symbol-5578_148941 .Pixso-symbol-5579_151118 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13169 .Pixso-symbol-5578_148941 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13173 .Pixso-symbol-5578_149511 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13173 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5588_13904 .Pixso-vector-5578_148942 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5588_13904 .Pixso-symbol-5578_148941 .Pixso-symbol-6042_8547 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13904 .Pixso-symbol-5578_148941 .Pixso-symbol-5579_151118 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13904 .Pixso-symbol-5578_148941 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13908 .Pixso-symbol-5578_149511 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13908 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5588_13175 .Pixso-vector-5578_148942 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5588_13175 .Pixso-symbol-5578_148941 .Pixso-symbol-6042_8547 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13175 .Pixso-symbol-5578_148941 .Pixso-symbol-5579_151118 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13175 .Pixso-symbol-5578_148941 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13179 .Pixso-symbol-5578_149511 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13179 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5588_11518 .Pixso-vector-5578_148942 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5588_11518 .Pixso-symbol-5578_148941 .Pixso-symbol-6042_8547 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_11518 .Pixso-symbol-5578_148941 .Pixso-symbol-5579_151118 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_11518 .Pixso-symbol-5578_148941 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_11522 .Pixso-symbol-5578_149511 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_11522 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5588_13181 .Pixso-vector-5578_148942 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5588_13181 .Pixso-symbol-5578_148941 .Pixso-symbol-6042_8547 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13181 .Pixso-symbol-5578_148941 .Pixso-symbol-5579_151118 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13181 .Pixso-symbol-5578_148941 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13185 .Pixso-symbol-5578_149511 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13185 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5588_13910 .Pixso-vector-5578_148942 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5588_13910 .Pixso-symbol-5578_148941 .Pixso-symbol-6042_8547 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13910 .Pixso-symbol-5578_148941 .Pixso-symbol-5579_151118 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13910 .Pixso-symbol-5578_148941 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13914 .Pixso-symbol-5578_149511 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13914 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5588_13187 .Pixso-vector-5578_148942 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5588_13187 .Pixso-symbol-5578_148941 .Pixso-symbol-6042_8547 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13187 .Pixso-symbol-5578_148941 .Pixso-symbol-5579_151118 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13187 .Pixso-symbol-5578_148941 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13191 .Pixso-symbol-5578_149511 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13191 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5588_11536 .Pixso-vector-5578_148942 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5588_11536 .Pixso-symbol-5578_148941 .Pixso-symbol-6042_8547 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_11536 .Pixso-symbol-5578_148941 .Pixso-symbol-5579_151118 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_11536 .Pixso-symbol-5578_148941 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_11540 .Pixso-symbol-5578_149511 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_11540 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5588_13193 .Pixso-vector-5578_148942 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5588_13193 .Pixso-symbol-5578_148941 .Pixso-symbol-6042_8547 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13193 .Pixso-symbol-5578_148941 .Pixso-symbol-5579_151118 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13193 .Pixso-symbol-5578_148941 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13197 .Pixso-symbol-5578_149511 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13197 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5588_13916 .Pixso-vector-5578_148942 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5588_13916 .Pixso-symbol-5578_148941 .Pixso-symbol-6042_8547 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13916 .Pixso-symbol-5578_148941 .Pixso-symbol-5579_151118 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13916 .Pixso-symbol-5578_148941 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13920 .Pixso-symbol-5578_149511 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13920 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5588_13199 .Pixso-vector-5578_148942 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5588_13199 .Pixso-symbol-5578_148941 .Pixso-symbol-6042_8547 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13199 .Pixso-symbol-5578_148941 .Pixso-symbol-5579_151118 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13199 .Pixso-symbol-5578_148941 {
    width: 12px;
    height: 12px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13203 .Pixso-symbol-5578_149511 {
    width: 12px;
    height: 12px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13203 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5588_11542 .Pixso-vector-5578_148942 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5588_11542 .Pixso-symbol-5578_148941 .Pixso-symbol-6042_8547 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_11542 .Pixso-symbol-5578_148941 .Pixso-symbol-5579_151118 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_11542 .Pixso-symbol-5578_148941 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_11546 .Pixso-symbol-5578_149511 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_11546 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5588_13205 .Pixso-vector-5578_148942 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5588_13205 .Pixso-symbol-5578_148941 .Pixso-symbol-6042_8547 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13205 .Pixso-symbol-5578_148941 .Pixso-symbol-5579_151118 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13205 .Pixso-symbol-5578_148941 {
    width: 12px;
    height: 12px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13209 .Pixso-symbol-5578_149511 {
    width: 12px;
    height: 12px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13209 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5588_13922 .Pixso-vector-5578_148942 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5588_13922 .Pixso-symbol-5578_148941 .Pixso-symbol-6042_8547 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13922 .Pixso-symbol-5578_148941 .Pixso-symbol-5579_151118 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13922 .Pixso-symbol-5578_148941 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13926 .Pixso-symbol-5578_149511 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13926 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5588_13211 .Pixso-vector-5578_148942 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5588_13211 .Pixso-symbol-5578_148941 .Pixso-symbol-6042_8547 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13211 .Pixso-symbol-5578_148941 .Pixso-symbol-5579_151118 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13211 .Pixso-symbol-5578_148941 {
    width: 12px;
    height: 12px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13215 .Pixso-symbol-5578_149511 {
    width: 12px;
    height: 12px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13215 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5494_4828 .Pixso-vector-5578_148942 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5494_4828 .Pixso-symbol-5578_148941 .Pixso-symbol-6042_8547 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5494_4828 .Pixso-symbol-5578_148941 .Pixso-symbol-5579_151118 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5494_4828 .Pixso-symbol-5578_148941 {
    width: 12px;
    height: 12px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5586_11112 .Pixso-symbol-5578_149511 {
    width: 12px;
    height: 12px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5586_11112 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5588_13217 .Pixso-vector-5578_148942 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5588_13217 .Pixso-symbol-5578_148941 .Pixso-symbol-6042_8547 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13217 .Pixso-symbol-5578_148941 .Pixso-symbol-5579_151118 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13217 .Pixso-symbol-5578_148941 {
    width: 12px;
    height: 12px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13221 .Pixso-symbol-5578_149511 {
    width: 12px;
    height: 12px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13221 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5588_13928 .Pixso-vector-5578_148942 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5588_13928 .Pixso-symbol-5578_148941 .Pixso-symbol-6042_8547 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13928 .Pixso-symbol-5578_148941 .Pixso-symbol-5579_151118 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13928 .Pixso-symbol-5578_148941 {
    width: 12px;
    height: 12px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13932 .Pixso-symbol-5578_149511 {
    width: 12px;
    height: 12px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13932 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5588_13223 .Pixso-vector-5578_148942 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5588_13223 .Pixso-symbol-5578_148941 .Pixso-symbol-6042_8547 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13223 .Pixso-symbol-5578_148941 .Pixso-symbol-5579_151118 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13223 .Pixso-symbol-5578_148941 {
    width: 12px;
    height: 12px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13227 .Pixso-symbol-5578_149511 {
    width: 12px;
    height: 12px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13227 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5588_11359 .Pixso-vector-5578_148942 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5588_11359 .Pixso-symbol-5578_148941 .Pixso-symbol-6042_8547 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_11359 .Pixso-symbol-5578_148941 .Pixso-symbol-5579_151118 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_11359 .Pixso-symbol-5578_148941 {
    width: 12px;
    height: 12px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_11363 .Pixso-symbol-5578_149511 {
    width: 12px;
    height: 12px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_11363 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5588_13229 .Pixso-vector-5578_148942 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5588_13229 .Pixso-symbol-5578_148941 .Pixso-symbol-6042_8547 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13229 .Pixso-symbol-5578_148941 .Pixso-symbol-5579_151118 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13229 .Pixso-symbol-5578_148941 {
    width: 12px;
    height: 12px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13233 .Pixso-symbol-5578_149511 {
    width: 12px;
    height: 12px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13233 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5588_13934 .Pixso-vector-5578_148942 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5588_13934 .Pixso-symbol-5578_148941 .Pixso-symbol-6042_8547 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13934 .Pixso-symbol-5578_148941 .Pixso-symbol-5579_151118 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13934 .Pixso-symbol-5578_148941 {
    width: 12px;
    height: 12px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13938 .Pixso-symbol-5578_149511 {
    width: 12px;
    height: 12px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13938 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5588_13235 .Pixso-vector-5578_148942 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5588_13235 .Pixso-symbol-5578_148941 .Pixso-symbol-6042_8547 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13235 .Pixso-symbol-5578_148941 .Pixso-symbol-5579_151118 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13235 .Pixso-symbol-5578_148941 {
    width: 12px;
    height: 12px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13239 .Pixso-symbol-5578_149511 {
    width: 12px;
    height: 12px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13239 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5588_11422 .Pixso-vector-5578_148942 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5588_11422 .Pixso-symbol-5578_148941 .Pixso-symbol-6042_8547 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_11422 .Pixso-symbol-5578_148941 .Pixso-symbol-5579_151118 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_11422 .Pixso-symbol-5578_148941 {
    width: 12px;
    height: 12px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_11426 .Pixso-symbol-5578_149511 {
    width: 12px;
    height: 12px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_11426 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5588_13241 .Pixso-vector-5578_148942 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5588_13241 .Pixso-symbol-5578_148941 .Pixso-symbol-6042_8547 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13241 .Pixso-symbol-5578_148941 .Pixso-symbol-5579_151118 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13241 .Pixso-symbol-5578_148941 {
    width: 12px;
    height: 12px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13245 .Pixso-symbol-5578_149511 {
    width: 12px;
    height: 12px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13245 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5588_13940 .Pixso-vector-5578_148942 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5588_13940 .Pixso-symbol-5578_148941 .Pixso-symbol-6042_8547 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13940 .Pixso-symbol-5578_148941 .Pixso-symbol-5579_151118 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13940 .Pixso-symbol-5578_148941 {
    width: 12px;
    height: 12px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13944 .Pixso-symbol-5578_149511 {
    width: 12px;
    height: 12px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13944 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5588_13247 .Pixso-vector-5578_148942 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5588_13247 .Pixso-symbol-5578_148941 .Pixso-symbol-6042_8547 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13247 .Pixso-symbol-5578_148941 .Pixso-symbol-5579_151118 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13247 .Pixso-symbol-5578_148941 {
    width: 12px;
    height: 12px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13251 .Pixso-symbol-5578_149511 {
    width: 12px;
    height: 12px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13251 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5588_11860 .Pixso-vector-5578_148942 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5588_11860 .Pixso-symbol-5578_148941 .Pixso-symbol-6042_8547 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_11860 .Pixso-symbol-5578_148941 .Pixso-symbol-5579_151118 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_11860 .Pixso-symbol-5578_148941 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_11864 .Pixso-symbol-5578_149511 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_11864 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5588_13253 .Pixso-vector-5578_148942 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5588_13253 .Pixso-symbol-5578_148941 .Pixso-symbol-6042_8547 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13253 .Pixso-symbol-5578_148941 .Pixso-symbol-5579_151118 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13253 .Pixso-symbol-5578_148941 {
    width: 12px;
    height: 12px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13257 .Pixso-symbol-5578_149511 {
    width: 12px;
    height: 12px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13257 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5588_13946 .Pixso-vector-5578_148942 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5588_13946 .Pixso-symbol-5578_148941 .Pixso-symbol-6042_8547 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13946 .Pixso-symbol-5578_148941 .Pixso-symbol-5579_151118 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13946 .Pixso-symbol-5578_148941 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13950 .Pixso-symbol-5578_149511 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13950 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5588_13259 .Pixso-vector-5578_148942 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5588_13259 .Pixso-symbol-5578_148941 .Pixso-symbol-6042_8547 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13259 .Pixso-symbol-5578_148941 .Pixso-symbol-5579_151118 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13259 .Pixso-symbol-5578_148941 {
    width: 12px;
    height: 12px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13263 .Pixso-symbol-5578_149511 {
    width: 12px;
    height: 12px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13263 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5588_12031 .Pixso-vector-5578_148942 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5588_12031 .Pixso-symbol-5578_148941 .Pixso-symbol-6042_8547 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_12031 .Pixso-symbol-5578_148941 .Pixso-symbol-5579_151118 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_12031 .Pixso-symbol-5578_148941 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_12035 .Pixso-symbol-5578_149511 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_12035 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5588_13265 .Pixso-vector-5578_148942 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5588_13265 .Pixso-symbol-5578_148941 .Pixso-symbol-6042_8547 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13265 .Pixso-symbol-5578_148941 .Pixso-symbol-5579_151118 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13265 .Pixso-symbol-5578_148941 {
    width: 12px;
    height: 12px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13269 .Pixso-symbol-5578_149511 {
    width: 12px;
    height: 12px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13269 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5588_13952 .Pixso-vector-5578_148942 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5588_13952 .Pixso-symbol-5578_148941 .Pixso-symbol-6042_8547 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13952 .Pixso-symbol-5578_148941 .Pixso-symbol-5579_151118 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13952 .Pixso-symbol-5578_148941 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13956 .Pixso-symbol-5578_149511 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13956 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5588_12193 .Pixso-vector-5578_148942 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5588_12193 .Pixso-symbol-5578_148941 .Pixso-symbol-6042_8547 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_12193 .Pixso-symbol-5578_148941 .Pixso-symbol-5579_151118 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_12193 .Pixso-symbol-5578_148941 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_12197 .Pixso-symbol-5578_149511 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_12197 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5588_13958 .Pixso-vector-5578_148942 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5588_13958 .Pixso-symbol-5578_148941 .Pixso-symbol-6042_8547 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13958 .Pixso-symbol-5578_148941 .Pixso-symbol-5579_151118 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13958 .Pixso-symbol-5578_148941 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13962 .Pixso-symbol-5578_149511 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13962 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5588_11866 .Pixso-vector-5578_148942 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5588_11866 .Pixso-symbol-5578_148941 .Pixso-symbol-6042_8547 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_11866 .Pixso-symbol-5578_148941 .Pixso-symbol-5579_151118 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_11866 .Pixso-symbol-5578_148941 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_11870 .Pixso-symbol-5578_149511 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_11870 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5588_13964 .Pixso-vector-5578_148942 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5588_13964 .Pixso-symbol-5578_148941 .Pixso-symbol-6042_8547 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13964 .Pixso-symbol-5578_148941 .Pixso-symbol-5579_151118 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13964 .Pixso-symbol-5578_148941 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13968 .Pixso-symbol-5578_149511 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13968 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5588_12037 .Pixso-vector-5578_148942 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5588_12037 .Pixso-symbol-5578_148941 .Pixso-symbol-6042_8547 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_12037 .Pixso-symbol-5578_148941 .Pixso-symbol-5579_151118 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_12037 .Pixso-symbol-5578_148941 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_12041 .Pixso-symbol-5578_149511 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_12041 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5588_13970 .Pixso-vector-5578_148942 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5588_13970 .Pixso-symbol-5578_148941 .Pixso-symbol-6042_8547 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13970 .Pixso-symbol-5578_148941 .Pixso-symbol-5579_151118 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13970 .Pixso-symbol-5578_148941 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13974 .Pixso-symbol-5578_149511 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13974 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5588_12199 .Pixso-vector-5578_148942 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5588_12199 .Pixso-symbol-5578_148941 .Pixso-symbol-6042_8547 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_12199 .Pixso-symbol-5578_148941 .Pixso-symbol-5579_151118 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_12199 .Pixso-symbol-5578_148941 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_12203 .Pixso-symbol-5578_149511 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_12203 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5588_13976 .Pixso-vector-5578_148942 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5588_13976 .Pixso-symbol-5578_148941 .Pixso-symbol-6042_8547 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13976 .Pixso-symbol-5578_148941 .Pixso-symbol-5579_151118 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13976 .Pixso-symbol-5578_148941 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13980 .Pixso-symbol-5578_149511 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13980 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5588_11872 .Pixso-vector-5578_148942 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5588_11872 .Pixso-symbol-5578_148941 .Pixso-symbol-6042_8547 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_11872 .Pixso-symbol-5578_148941 .Pixso-symbol-5579_151118 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_11872 .Pixso-symbol-5578_148941 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_11876 .Pixso-symbol-5578_149511 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_11876 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5588_13982 .Pixso-vector-5578_148942 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5588_13982 .Pixso-symbol-5578_148941 .Pixso-symbol-6042_8547 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13982 .Pixso-symbol-5578_148941 .Pixso-symbol-5579_151118 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13982 .Pixso-symbol-5578_148941 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13986 .Pixso-symbol-5578_149511 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13986 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5588_12043 .Pixso-vector-5578_148942 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5588_12043 .Pixso-symbol-5578_148941 .Pixso-symbol-6042_8547 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_12043 .Pixso-symbol-5578_148941 .Pixso-symbol-5579_151118 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_12043 .Pixso-symbol-5578_148941 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_12047 .Pixso-symbol-5578_149511 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_12047 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5588_13988 .Pixso-vector-5578_148942 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5588_13988 .Pixso-symbol-5578_148941 .Pixso-symbol-6042_8547 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13988 .Pixso-symbol-5578_148941 .Pixso-symbol-5579_151118 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13988 .Pixso-symbol-5578_148941 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13992 .Pixso-symbol-5578_149511 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13992 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5588_12205 .Pixso-vector-5578_148942 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5588_12205 .Pixso-symbol-5578_148941 .Pixso-symbol-6042_8547 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_12205 .Pixso-symbol-5578_148941 .Pixso-symbol-5579_151118 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_12205 .Pixso-symbol-5578_148941 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_12209 .Pixso-symbol-5578_149511 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_12209 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5588_13994 .Pixso-vector-5578_148942 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5588_13994 .Pixso-symbol-5578_148941 .Pixso-symbol-6042_8547 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13994 .Pixso-symbol-5578_148941 .Pixso-symbol-5579_151118 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13994 .Pixso-symbol-5578_148941 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13998 .Pixso-symbol-5578_149511 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_13998 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5588_11524 .Pixso-vector-5578_148942 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5588_11524 .Pixso-symbol-5578_148941 .Pixso-symbol-6042_8547 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_11524 .Pixso-symbol-5578_148941 .Pixso-symbol-5579_151118 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_11524 .Pixso-symbol-5578_148941 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_11528 .Pixso-symbol-5578_149511 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_11528 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5588_14000 .Pixso-vector-5578_148942 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5588_14000 .Pixso-symbol-5578_148941 .Pixso-symbol-6042_8547 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_14000 .Pixso-symbol-5578_148941 .Pixso-symbol-5579_151118 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_14000 .Pixso-symbol-5578_148941 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_14004 .Pixso-symbol-5578_149511 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_14004 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5588_11548 .Pixso-vector-5578_148942 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5588_11548 .Pixso-symbol-5578_148941 .Pixso-symbol-6042_8547 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_11548 .Pixso-symbol-5578_148941 .Pixso-symbol-5579_151118 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_11548 .Pixso-symbol-5578_148941 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_11552 .Pixso-symbol-5578_149511 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_11552 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5588_14006 .Pixso-vector-5578_148942 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5588_14006 .Pixso-symbol-5578_148941 .Pixso-symbol-6042_8547 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_14006 .Pixso-symbol-5578_148941 .Pixso-symbol-5579_151118 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_14006 .Pixso-symbol-5578_148941 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_14010 .Pixso-symbol-5578_149511 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_14010 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5588_11554 .Pixso-vector-5578_148942 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5588_11554 .Pixso-symbol-5578_148941 .Pixso-symbol-6042_8547 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_11554 .Pixso-symbol-5578_148941 .Pixso-symbol-5579_151118 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_11554 .Pixso-symbol-5578_148941 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_11558 .Pixso-symbol-5578_149511 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_11558 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5588_14012 .Pixso-vector-5578_148942 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5588_14012 .Pixso-symbol-5578_148941 .Pixso-symbol-6042_8547 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_14012 .Pixso-symbol-5578_148941 .Pixso-symbol-5579_151118 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_14012 .Pixso-symbol-5578_148941 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_14016 .Pixso-symbol-5578_149511 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_14016 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5588_11878 .Pixso-vector-5578_148942 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5588_11878 .Pixso-symbol-5578_148941 .Pixso-symbol-6042_8547 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_11878 .Pixso-symbol-5578_148941 .Pixso-symbol-5579_151118 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_11878 .Pixso-symbol-5578_148941 {
    width: 12px;
    height: 12px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_11882 .Pixso-symbol-5578_149511 {
    width: 12px;
    height: 12px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_11882 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5588_14018 .Pixso-vector-5578_148942 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5588_14018 .Pixso-symbol-5578_148941 .Pixso-symbol-6042_8547 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_14018 .Pixso-symbol-5578_148941 .Pixso-symbol-5579_151118 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_14018 .Pixso-symbol-5578_148941 {
    width: 12px;
    height: 12px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_14022 .Pixso-symbol-5578_149511 {
    width: 12px;
    height: 12px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_14022 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5588_12049 .Pixso-vector-5578_148942 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5588_12049 .Pixso-symbol-5578_148941 .Pixso-symbol-6042_8547 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_12049 .Pixso-symbol-5578_148941 .Pixso-symbol-5579_151118 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_12049 .Pixso-symbol-5578_148941 {
    width: 12px;
    height: 12px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_12053 .Pixso-symbol-5578_149511 {
    width: 12px;
    height: 12px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_12053 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5588_14024 .Pixso-vector-5578_148942 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5588_14024 .Pixso-symbol-5578_148941 .Pixso-symbol-6042_8547 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_14024 .Pixso-symbol-5578_148941 .Pixso-symbol-5579_151118 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_14024 .Pixso-symbol-5578_148941 {
    width: 12px;
    height: 12px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_14028 .Pixso-symbol-5578_149511 {
    width: 12px;
    height: 12px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_14028 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5588_12211 .Pixso-vector-5578_148942 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5588_12211 .Pixso-symbol-5578_148941 .Pixso-symbol-6042_8547 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_12211 .Pixso-symbol-5578_148941 .Pixso-symbol-5579_151118 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_12211 .Pixso-symbol-5578_148941 {
    width: 12px;
    height: 12px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_12215 .Pixso-symbol-5578_149511 {
    width: 12px;
    height: 12px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_12215 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5588_14030 .Pixso-vector-5578_148942 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5588_14030 .Pixso-symbol-5578_148941 .Pixso-symbol-6042_8547 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_14030 .Pixso-symbol-5578_148941 .Pixso-symbol-5579_151118 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_14030 .Pixso-symbol-5578_148941 {
    width: 12px;
    height: 12px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_14034 .Pixso-symbol-5578_149511 {
    width: 12px;
    height: 12px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_14034 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5588_11884 .Pixso-vector-5578_148942 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5588_11884 .Pixso-symbol-5578_148941 .Pixso-symbol-6042_8547 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_11884 .Pixso-symbol-5578_148941 .Pixso-symbol-5579_151118 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_11884 .Pixso-symbol-5578_148941 {
    width: 12px;
    height: 12px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_11888 .Pixso-symbol-5578_149511 {
    width: 12px;
    height: 12px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_11888 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5588_14036 .Pixso-vector-5578_148942 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5588_14036 .Pixso-symbol-5578_148941 .Pixso-symbol-6042_8547 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_14036 .Pixso-symbol-5578_148941 .Pixso-symbol-5579_151118 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_14036 .Pixso-symbol-5578_148941 {
    width: 12px;
    height: 12px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_14040 .Pixso-symbol-5578_149511 {
    width: 12px;
    height: 12px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_14040 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5588_12055 .Pixso-vector-5578_148942 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5588_12055 .Pixso-symbol-5578_148941 .Pixso-symbol-6042_8547 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_12055 .Pixso-symbol-5578_148941 .Pixso-symbol-5579_151118 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_12055 .Pixso-symbol-5578_148941 {
    width: 12px;
    height: 12px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_12059 .Pixso-symbol-5578_149511 {
    width: 12px;
    height: 12px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_12059 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5588_14042 .Pixso-vector-5578_148942 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5588_14042 .Pixso-symbol-5578_148941 .Pixso-symbol-6042_8547 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_14042 .Pixso-symbol-5578_148941 .Pixso-symbol-5579_151118 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_14042 .Pixso-symbol-5578_148941 {
    width: 12px;
    height: 12px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_14046 .Pixso-symbol-5578_149511 {
    width: 12px;
    height: 12px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_14046 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5588_12217 .Pixso-vector-5578_148942 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5588_12217 .Pixso-symbol-5578_148941 .Pixso-symbol-6042_8547 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_12217 .Pixso-symbol-5578_148941 .Pixso-symbol-5579_151118 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_12217 .Pixso-symbol-5578_148941 {
    width: 12px;
    height: 12px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_12221 .Pixso-symbol-5578_149511 {
    width: 12px;
    height: 12px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_12221 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5588_14048 .Pixso-vector-5578_148942 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5588_14048 .Pixso-symbol-5578_148941 .Pixso-symbol-6042_8547 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_14048 .Pixso-symbol-5578_148941 .Pixso-symbol-5579_151118 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_14048 .Pixso-symbol-5578_148941 {
    width: 12px;
    height: 12px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_14052 .Pixso-symbol-5578_149511 {
    width: 12px;
    height: 12px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_14052 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5588_11890 .Pixso-vector-5578_148942 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5588_11890 .Pixso-symbol-5578_148941 .Pixso-symbol-6042_8547 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_11890 .Pixso-symbol-5578_148941 .Pixso-symbol-5579_151118 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_11890 .Pixso-symbol-5578_148941 {
    width: 12px;
    height: 12px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_11894 .Pixso-symbol-5578_149511 {
    width: 12px;
    height: 12px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_11894 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5588_14054 .Pixso-vector-5578_148942 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5588_14054 .Pixso-symbol-5578_148941 .Pixso-symbol-6042_8547 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_14054 .Pixso-symbol-5578_148941 .Pixso-symbol-5579_151118 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_14054 .Pixso-symbol-5578_148941 {
    width: 12px;
    height: 12px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_14058 .Pixso-symbol-5578_149511 {
    width: 12px;
    height: 12px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_14058 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5588_12061 .Pixso-vector-5578_148942 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5588_12061 .Pixso-symbol-5578_148941 .Pixso-symbol-6042_8547 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_12061 .Pixso-symbol-5578_148941 .Pixso-symbol-5579_151118 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_12061 .Pixso-symbol-5578_148941 {
    width: 12px;
    height: 12px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_12065 .Pixso-symbol-5578_149511 {
    width: 12px;
    height: 12px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_12065 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5588_14060 .Pixso-vector-5578_148942 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5588_14060 .Pixso-symbol-5578_148941 .Pixso-symbol-6042_8547 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_14060 .Pixso-symbol-5578_148941 .Pixso-symbol-5579_151118 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_14060 .Pixso-symbol-5578_148941 {
    width: 12px;
    height: 12px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_14064 .Pixso-symbol-5578_149511 {
    width: 12px;
    height: 12px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_14064 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5588_12223 .Pixso-vector-5578_148942 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5588_12223 .Pixso-symbol-5578_148941 .Pixso-symbol-6042_8547 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_12223 .Pixso-symbol-5578_148941 .Pixso-symbol-5579_151118 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_12223 .Pixso-symbol-5578_148941 {
    width: 12px;
    height: 12px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_12227 .Pixso-symbol-5578_149511 {
    width: 12px;
    height: 12px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_12227 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5588_14066 .Pixso-vector-5578_148942 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5588_14066 .Pixso-symbol-5578_148941 .Pixso-symbol-6042_8547 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_14066 .Pixso-symbol-5578_148941 .Pixso-symbol-5579_151118 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_14066 .Pixso-symbol-5578_148941 {
    width: 12px;
    height: 12px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_14070 .Pixso-symbol-5578_149511 {
    width: 12px;
    height: 12px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_14070 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5588_11530 .Pixso-vector-5578_148942 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5588_11530 .Pixso-symbol-5578_148941 .Pixso-symbol-6042_8547 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_11530 .Pixso-symbol-5578_148941 .Pixso-symbol-5579_151118 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_11530 .Pixso-symbol-5578_148941 {
    width: 12px;
    height: 12px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_11534 .Pixso-symbol-5578_149511 {
    width: 12px;
    height: 12px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_11534 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5588_14072 .Pixso-vector-5578_148942 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5588_14072 .Pixso-symbol-5578_148941 .Pixso-symbol-6042_8547 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_14072 .Pixso-symbol-5578_148941 .Pixso-symbol-5579_151118 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_14072 .Pixso-symbol-5578_148941 {
    width: 12px;
    height: 12px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_14076 .Pixso-symbol-5578_149511 {
    width: 12px;
    height: 12px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_14076 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5588_11560 .Pixso-vector-5578_148942 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5588_11560 .Pixso-symbol-5578_148941 .Pixso-symbol-6042_8547 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_11560 .Pixso-symbol-5578_148941 .Pixso-symbol-5579_151118 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_11560 .Pixso-symbol-5578_148941 {
    width: 12px;
    height: 12px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_11564 .Pixso-symbol-5578_149511 {
    width: 12px;
    height: 12px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_11564 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5588_14078 .Pixso-vector-5578_148942 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5588_14078 .Pixso-symbol-5578_148941 .Pixso-symbol-6042_8547 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_14078 .Pixso-symbol-5578_148941 .Pixso-symbol-5579_151118 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_14078 .Pixso-symbol-5578_148941 {
    width: 12px;
    height: 12px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_14082 .Pixso-symbol-5578_149511 {
    width: 12px;
    height: 12px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_14082 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5588_11566 .Pixso-vector-5578_148942 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5588_11566 .Pixso-symbol-5578_148941 .Pixso-symbol-6042_8547 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_11566 .Pixso-symbol-5578_148941 .Pixso-symbol-5579_151118 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_11566 .Pixso-symbol-5578_148941 {
    width: 12px;
    height: 12px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_11570 .Pixso-symbol-5578_149511 {
    width: 12px;
    height: 12px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_11570 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5588_14084 .Pixso-vector-5578_148942 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5588_14084 .Pixso-symbol-5578_148941 .Pixso-symbol-6042_8547 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_14084 .Pixso-symbol-5578_148941 .Pixso-symbol-5579_151118 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_14084 .Pixso-symbol-5578_148941 {
    width: 12px;
    height: 12px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_14088 .Pixso-symbol-5578_149511 {
    width: 12px;
    height: 12px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5588_14088 .Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-instance-5588_11191 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59165 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13001 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59165 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13820 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59165 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13007 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59165 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_11347 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59165 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13013 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59165 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13826 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59165 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13019 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59165 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_11410 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59165 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13025 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59165 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13832 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59165 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13031 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59165 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_11842 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59165 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13037 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59165 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13838 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59165 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13043 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59165 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_12013 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59165 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13049 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59165 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13844 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59165 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13055 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59165 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_12175 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59165 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13061 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59165 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13850 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59165 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13067 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59165 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_11848 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59165 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13073 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59165 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13856 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59165 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13079 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59165 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_12019 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59165 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13085 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59165 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13862 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59165 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13091 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59165 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_12181 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59165 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13097 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59165 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13868 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59165 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13103 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59165 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_11854 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59165 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13109 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59165 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13874 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59165 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13115 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59165 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_12025 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59165 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13121 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59165 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13880 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59165 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13127 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59165 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_12187 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59165 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13133 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59165 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13886 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59165 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13139 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59165 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_11164 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59165 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13145 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59165 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13892 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59165 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13151 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59165 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_11353 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59165 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13157 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59165 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13898 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59165 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13163 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59165 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_11416 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59165 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13169 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59165 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13904 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59165 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13175 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59165 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_11518 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59165 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13181 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59165 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13910 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59165 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13187 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59165 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_11536 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59165 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13193 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59165 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13916 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59165 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13199 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59165 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_11542 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59165 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13205 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59165 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13922 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59165 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13211 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59165 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5494_4828 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59165 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13217 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59165 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13928 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59165 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13223 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59165 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_11359 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59165 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13229 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59165 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13934 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59165 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13235 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59165 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_11422 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59165 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13241 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59165 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13940 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59165 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13247 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59165 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_11860 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59165 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13253 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59165 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13946 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59165 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13259 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59165 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_12031 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59165 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13265 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59165 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13952 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59165 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_12193 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59165 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13958 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59165 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_11866 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59165 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13964 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59165 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_12037 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59165 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13970 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59165 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_12199 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59165 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13976 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59165 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_11872 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59165 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13982 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59165 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_12043 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59165 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13988 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59165 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_12205 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59165 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13994 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59165 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_11524 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59165 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_14000 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59165 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_11548 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59165 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_14006 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59165 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_11554 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59165 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_14012 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59165 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_11878 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59165 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_14018 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59165 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_12049 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59165 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_14024 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59165 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_12211 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59165 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_14030 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59165 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_11884 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59165 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_14036 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59165 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_12055 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59165 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_14042 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59165 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_12217 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59165 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_14048 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59165 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_11890 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59165 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_14054 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59165 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_12061 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59165 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_14060 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59165 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_12223 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59165 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_14066 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59165 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_11530 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59165 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_14072 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59165 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_11560 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59165 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_14078 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59165 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_11566 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59165 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_14084 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59165 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_11191 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59186 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13001 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59186 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13820 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59186 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13007 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59186 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_11347 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59186 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13013 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59186 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13826 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59186 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13019 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59186 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_11410 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59186 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13025 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59186 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13832 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59186 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13031 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59186 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_11842 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59186 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13037 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59186 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13838 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59186 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13043 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59186 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_12013 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59186 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13049 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59186 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13844 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59186 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13055 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59186 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_12175 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59186 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13061 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59186 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13850 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59186 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13067 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59186 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_11848 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59186 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13073 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59186 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13856 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59186 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13079 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59186 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_12019 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59186 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13085 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59186 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13862 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59186 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13091 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59186 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_12181 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59186 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13097 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59186 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13868 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59186 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13103 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59186 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_11854 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59186 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13109 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59186 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13874 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59186 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13115 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59186 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_12025 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59186 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13121 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59186 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13880 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59186 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13127 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59186 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_12187 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59186 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13133 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59186 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13886 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59186 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13139 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59186 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_11164 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59186 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13145 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59186 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13892 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59186 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13151 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59186 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_11353 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59186 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13157 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59186 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13898 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59186 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13163 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59186 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_11416 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59186 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13169 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59186 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13904 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59186 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13175 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59186 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_11518 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59186 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13181 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59186 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13910 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59186 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13187 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59186 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_11536 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59186 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13193 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59186 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13916 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59186 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13199 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59186 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_11542 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59186 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13205 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59186 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13922 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59186 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13211 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59186 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5494_4828 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59186 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13217 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59186 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13928 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59186 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13223 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59186 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_11359 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59186 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13229 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59186 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13934 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59186 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13235 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59186 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_11422 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59186 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13241 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59186 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13940 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59186 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13247 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59186 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_11860 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59186 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13253 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59186 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13946 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59186 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13259 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59186 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_12031 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59186 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13265 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59186 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13952 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59186 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_12193 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59186 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13958 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59186 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_11866 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59186 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13964 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59186 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_12037 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59186 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13970 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59186 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_12199 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59186 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13976 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59186 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_11872 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59186 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13982 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59186 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_12043 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59186 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13988 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59186 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_12205 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59186 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13994 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59186 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_11524 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59186 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_14000 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59186 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_11548 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59186 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_14006 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59186 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_11554 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59186 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_14012 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59186 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_11878 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59186 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_14018 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59186 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_12049 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59186 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_14024 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59186 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_12211 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59186 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_14030 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59186 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_11884 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59186 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_14036 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59186 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_12055 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59186 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_14042 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59186 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_12217 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59186 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_14048 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59186 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_11890 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59186 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_14054 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59186 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_12061 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59186 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_14060 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59186 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_12223 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59186 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_14066 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59186 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_11530 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59186 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_14072 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59186 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_11560 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59186 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_14078 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59186 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_11566 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59186 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_14084 .Pixso-symbol-5578_148941 .Pixso-symbol-6041_59186 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_11192 .Pixso-symbol-5489_8978 {
    width: 8px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5588_13003 .Pixso-symbol-5489_8978 {
    width: 8px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5588_13822 .Pixso-symbol-5489_8978 {
    width: 8px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5588_13009 .Pixso-symbol-5489_8978 {
    width: 8px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5588_11349 .Pixso-symbol-5489_8978 {
    width: 8px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5588_13015 .Pixso-symbol-5489_8978 {
    width: 8px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5588_13828 .Pixso-symbol-5489_8978 {
    width: 8px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5588_13021 .Pixso-symbol-5489_8978 {
    width: 8px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5588_11412 .Pixso-symbol-5489_8978 {
    width: 8px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5588_13027 .Pixso-symbol-5489_8978 {
    width: 8px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5588_13834 .Pixso-symbol-5489_8978 {
    width: 8px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5588_13033 .Pixso-symbol-5489_8978 {
    width: 8px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5588_11844 .Pixso-symbol-5489_8978 {
    width: 8px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5588_13039 .Pixso-symbol-5489_8978 {
    width: 8px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5588_13840 .Pixso-symbol-5489_8978 {
    width: 8px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5588_13045 .Pixso-symbol-5489_8978 {
    width: 8px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5588_12015 .Pixso-symbol-5489_8978 {
    width: 8px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5588_13051 .Pixso-symbol-5489_8978 {
    width: 8px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5588_13846 .Pixso-symbol-5489_8978 {
    width: 8px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5588_13057 .Pixso-symbol-5489_8978 {
    width: 8px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5588_12177 .Pixso-symbol-5489_8978 {
    width: 8px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5588_13063 .Pixso-symbol-5489_8978 {
    width: 8px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5588_13852 .Pixso-symbol-5489_8978 {
    width: 8px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5588_13069 .Pixso-symbol-5489_8978 {
    width: 8px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5588_11850 .Pixso-symbol-5489_8978 {
    width: 8px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5588_13075 .Pixso-symbol-5489_8978 {
    width: 8px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5588_13858 .Pixso-symbol-5489_8978 {
    width: 8px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5588_13081 .Pixso-symbol-5489_8978 {
    width: 8px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5588_12021 .Pixso-symbol-5489_8978 {
    width: 8px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5588_13087 .Pixso-symbol-5489_8978 {
    width: 8px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5588_13864 .Pixso-symbol-5489_8978 {
    width: 8px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5588_13093 .Pixso-symbol-5489_8978 {
    width: 8px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5588_12183 .Pixso-symbol-5489_8978 {
    width: 8px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5588_13099 .Pixso-symbol-5489_8978 {
    width: 8px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5588_13870 .Pixso-symbol-5489_8978 {
    width: 8px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5588_13105 .Pixso-symbol-5489_8978 {
    width: 8px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5588_11856 .Pixso-symbol-5489_8978 {
    width: 8px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5588_13111 .Pixso-symbol-5489_8978 {
    width: 8px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5588_13876 .Pixso-symbol-5489_8978 {
    width: 8px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5588_13117 .Pixso-symbol-5489_8978 {
    width: 8px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5588_12027 .Pixso-symbol-5489_8978 {
    width: 8px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5588_13123 .Pixso-symbol-5489_8978 {
    width: 8px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5588_13882 .Pixso-symbol-5489_8978 {
    width: 8px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5588_13129 .Pixso-symbol-5489_8978 {
    width: 8px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5588_12189 .Pixso-symbol-5489_8978 {
    width: 8px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5588_13135 .Pixso-symbol-5489_8978 {
    width: 8px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5588_13888 .Pixso-symbol-5489_8978 {
    width: 8px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5588_13141 .Pixso-symbol-5489_8978 {
    width: 8px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5588_11165 .Pixso-symbol-5489_8978 {
    width: 8px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5588_13147 .Pixso-symbol-5489_8978 {
    width: 8px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5588_13894 .Pixso-symbol-5489_8978 {
    width: 8px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5588_13153 .Pixso-symbol-5489_8978 {
    width: 8px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5588_11355 .Pixso-symbol-5489_8978 {
    width: 8px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5588_13159 .Pixso-symbol-5489_8978 {
    width: 8px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5588_13900 .Pixso-symbol-5489_8978 {
    width: 8px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5588_13165 .Pixso-symbol-5489_8978 {
    width: 8px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5588_11418 .Pixso-symbol-5489_8978 {
    width: 8px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5588_13171 .Pixso-symbol-5489_8978 {
    width: 8px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5588_13906 .Pixso-symbol-5489_8978 {
    width: 8px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5588_13177 .Pixso-symbol-5489_8978 {
    width: 8px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5588_11520 .Pixso-symbol-5489_8978 {
    width: 8px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5588_13183 .Pixso-symbol-5489_8978 {
    width: 8px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5588_13912 .Pixso-symbol-5489_8978 {
    width: 8px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5588_13189 .Pixso-symbol-5489_8978 {
    width: 8px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5588_11538 .Pixso-symbol-5489_8978 {
    width: 8px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5588_13195 .Pixso-symbol-5489_8978 {
    width: 8px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5588_13918 .Pixso-symbol-5489_8978 {
    width: 8px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5588_13201 .Pixso-symbol-5489_8978 {
    width: 8px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5588_11544 .Pixso-symbol-5489_8978 {
    width: 8px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5588_13207 .Pixso-symbol-5489_8978 {
    width: 8px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5588_13924 .Pixso-symbol-5489_8978 {
    width: 8px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5588_13213 .Pixso-symbol-5489_8978 {
    width: 8px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5586_11117 .Pixso-symbol-5489_8978 {
    width: 8px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5588_13219 .Pixso-symbol-5489_8978 {
    width: 8px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5588_13930 .Pixso-symbol-5489_8978 {
    width: 8px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5588_13225 .Pixso-symbol-5489_8978 {
    width: 8px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5588_11361 .Pixso-symbol-5489_8978 {
    width: 8px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5588_13231 .Pixso-symbol-5489_8978 {
    width: 8px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5588_13936 .Pixso-symbol-5489_8978 {
    width: 8px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5588_13237 .Pixso-symbol-5489_8978 {
    width: 8px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5588_11424 .Pixso-symbol-5489_8978 {
    width: 8px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5588_13243 .Pixso-symbol-5489_8978 {
    width: 8px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5588_13942 .Pixso-symbol-5489_8978 {
    width: 8px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5588_13249 .Pixso-symbol-5489_8978 {
    width: 8px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5588_11862 .Pixso-symbol-5489_8978 {
    width: 8px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5588_13255 .Pixso-symbol-5489_8978 {
    width: 8px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5588_13948 .Pixso-symbol-5489_8978 {
    width: 8px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5588_13261 .Pixso-symbol-5489_8978 {
    width: 8px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5588_12033 .Pixso-symbol-5489_8978 {
    width: 8px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5588_13267 .Pixso-symbol-5489_8978 {
    width: 8px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5588_13954 .Pixso-symbol-5489_8978 {
    width: 8px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5588_12195 .Pixso-symbol-5489_8978 {
    width: 8px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5588_13960 .Pixso-symbol-5489_8978 {
    width: 8px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5588_11868 .Pixso-symbol-5489_8978 {
    width: 8px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5588_13966 .Pixso-symbol-5489_8978 {
    width: 8px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5588_12039 .Pixso-symbol-5489_8978 {
    width: 8px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5588_13972 .Pixso-symbol-5489_8978 {
    width: 8px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5588_12201 .Pixso-symbol-5489_8978 {
    width: 8px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5588_13978 .Pixso-symbol-5489_8978 {
    width: 8px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5588_11874 .Pixso-symbol-5489_8978 {
    width: 8px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5588_13984 .Pixso-symbol-5489_8978 {
    width: 8px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5588_12045 .Pixso-symbol-5489_8978 {
    width: 8px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5588_13990 .Pixso-symbol-5489_8978 {
    width: 8px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5588_12207 .Pixso-symbol-5489_8978 {
    width: 8px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5588_13996 .Pixso-symbol-5489_8978 {
    width: 8px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5588_11526 .Pixso-symbol-5489_8978 {
    width: 8px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5588_14002 .Pixso-symbol-5489_8978 {
    width: 8px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5588_11550 .Pixso-symbol-5489_8978 {
    width: 8px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5588_14008 .Pixso-symbol-5489_8978 {
    width: 8px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5588_11556 .Pixso-symbol-5489_8978 {
    width: 8px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5588_14014 .Pixso-symbol-5489_8978 {
    width: 8px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5588_11880 .Pixso-symbol-5489_8978 {
    width: 8px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5588_14020 .Pixso-symbol-5489_8978 {
    width: 8px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5588_12051 .Pixso-symbol-5489_8978 {
    width: 8px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5588_14026 .Pixso-symbol-5489_8978 {
    width: 8px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5588_12213 .Pixso-symbol-5489_8978 {
    width: 8px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5588_14032 .Pixso-symbol-5489_8978 {
    width: 8px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5588_11886 .Pixso-symbol-5489_8978 {
    width: 8px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5588_14038 .Pixso-symbol-5489_8978 {
    width: 8px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5588_12057 .Pixso-symbol-5489_8978 {
    width: 8px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5588_14044 .Pixso-symbol-5489_8978 {
    width: 8px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5588_12219 .Pixso-symbol-5489_8978 {
    width: 8px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5588_14050 .Pixso-symbol-5489_8978 {
    width: 8px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5588_11892 .Pixso-symbol-5489_8978 {
    width: 8px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5588_14056 .Pixso-symbol-5489_8978 {
    width: 8px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5588_12063 .Pixso-symbol-5489_8978 {
    width: 8px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5588_14062 .Pixso-symbol-5489_8978 {
    width: 8px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5588_12225 .Pixso-symbol-5489_8978 {
    width: 8px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5588_14068 .Pixso-symbol-5489_8978 {
    width: 8px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5588_11532 .Pixso-symbol-5489_8978 {
    width: 8px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5588_14074 .Pixso-symbol-5489_8978 {
    width: 8px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5588_11562 .Pixso-symbol-5489_8978 {
    width: 8px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5588_14080 .Pixso-symbol-5489_8978 {
    width: 8px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5588_11568 .Pixso-symbol-5489_8978 {
    width: 8px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5588_14086 .Pixso-symbol-5489_8978 {
    width: 8px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5588_11192 .Pixso-frame-5490_8987 {
    width: 75%;
    height: 75%;
    overflow: hidden;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 12.5%;
    bottom: 12.5%;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5588_13003 .Pixso-frame-5490_8987 {
    width: 75%;
    height: 75%;
    overflow: hidden;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 12.5%;
    bottom: 12.5%;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5588_13822 .Pixso-frame-5490_8987 {
    width: 75%;
    height: 75%;
    overflow: hidden;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 12.5%;
    bottom: 12.5%;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5588_13009 .Pixso-frame-5490_8987 {
    width: 75%;
    height: 75%;
    overflow: hidden;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 12.5%;
    bottom: 12.5%;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5588_11349 .Pixso-frame-5490_8987 {
    width: 75%;
    height: 75%;
    overflow: hidden;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 12.5%;
    bottom: 12.5%;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5588_13015 .Pixso-frame-5490_8987 {
    width: 75%;
    height: 75%;
    overflow: hidden;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 12.5%;
    bottom: 12.5%;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5588_13828 .Pixso-frame-5490_8987 {
    width: 75%;
    height: 75%;
    overflow: hidden;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 12.5%;
    bottom: 12.5%;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5588_13021 .Pixso-frame-5490_8987 {
    width: 75%;
    height: 75%;
    overflow: hidden;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 12.5%;
    bottom: 12.5%;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5588_11412 .Pixso-frame-5490_8987 {
    width: 75%;
    height: 75%;
    overflow: hidden;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 12.5%;
    bottom: 12.5%;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5588_13027 .Pixso-frame-5490_8987 {
    width: 75%;
    height: 75%;
    overflow: hidden;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 12.5%;
    bottom: 12.5%;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5588_13834 .Pixso-frame-5490_8987 {
    width: 75%;
    height: 75%;
    overflow: hidden;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 12.5%;
    bottom: 12.5%;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5588_13033 .Pixso-frame-5490_8987 {
    width: 75%;
    height: 75%;
    overflow: hidden;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 12.5%;
    bottom: 12.5%;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5588_11844 .Pixso-frame-5490_8987 {
    width: 75%;
    height: 75%;
    overflow: hidden;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 12.5%;
    bottom: 12.5%;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5588_13039 .Pixso-frame-5490_8987 {
    width: 75%;
    height: 75%;
    overflow: hidden;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 12.5%;
    bottom: 12.5%;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5588_13840 .Pixso-frame-5490_8987 {
    width: 75%;
    height: 75%;
    overflow: hidden;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 12.5%;
    bottom: 12.5%;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5588_13045 .Pixso-frame-5490_8987 {
    width: 75%;
    height: 75%;
    overflow: hidden;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 12.5%;
    bottom: 12.5%;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5588_12015 .Pixso-frame-5490_8987 {
    width: 75%;
    height: 75%;
    overflow: hidden;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 12.5%;
    bottom: 12.5%;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5588_13051 .Pixso-frame-5490_8987 {
    width: 75%;
    height: 75%;
    overflow: hidden;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 12.5%;
    bottom: 12.5%;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5588_13846 .Pixso-frame-5490_8987 {
    width: 75%;
    height: 75%;
    overflow: hidden;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 12.5%;
    bottom: 12.5%;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5588_13057 .Pixso-frame-5490_8987 {
    width: 75%;
    height: 75%;
    overflow: hidden;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 12.5%;
    bottom: 12.5%;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5588_12177 .Pixso-frame-5490_8987 {
    width: 75%;
    height: 75%;
    overflow: hidden;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 12.5%;
    bottom: 12.5%;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5588_13063 .Pixso-frame-5490_8987 {
    width: 75%;
    height: 75%;
    overflow: hidden;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 12.5%;
    bottom: 12.5%;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5588_13852 .Pixso-frame-5490_8987 {
    width: 75%;
    height: 75%;
    overflow: hidden;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 12.5%;
    bottom: 12.5%;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5588_13069 .Pixso-frame-5490_8987 {
    width: 75%;
    height: 75%;
    overflow: hidden;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 12.5%;
    bottom: 12.5%;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5588_11850 .Pixso-frame-5490_8987 {
    width: 75%;
    height: 75%;
    overflow: hidden;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 12.5%;
    bottom: 12.5%;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5588_13075 .Pixso-frame-5490_8987 {
    width: 75%;
    height: 75%;
    overflow: hidden;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 12.5%;
    bottom: 12.5%;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5588_13858 .Pixso-frame-5490_8987 {
    width: 75%;
    height: 75%;
    overflow: hidden;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 12.5%;
    bottom: 12.5%;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5588_13081 .Pixso-frame-5490_8987 {
    width: 75%;
    height: 75%;
    overflow: hidden;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 12.5%;
    bottom: 12.5%;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5588_12021 .Pixso-frame-5490_8987 {
    width: 75%;
    height: 75%;
    overflow: hidden;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 12.5%;
    bottom: 12.5%;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5588_13087 .Pixso-frame-5490_8987 {
    width: 75%;
    height: 75%;
    overflow: hidden;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 12.5%;
    bottom: 12.5%;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5588_13864 .Pixso-frame-5490_8987 {
    width: 75%;
    height: 75%;
    overflow: hidden;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 12.5%;
    bottom: 12.5%;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5588_13093 .Pixso-frame-5490_8987 {
    width: 75%;
    height: 75%;
    overflow: hidden;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 12.5%;
    bottom: 12.5%;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5588_12183 .Pixso-frame-5490_8987 {
    width: 75%;
    height: 75%;
    overflow: hidden;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 12.5%;
    bottom: 12.5%;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5588_13099 .Pixso-frame-5490_8987 {
    width: 75%;
    height: 75%;
    overflow: hidden;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 12.5%;
    bottom: 12.5%;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5588_13870 .Pixso-frame-5490_8987 {
    width: 75%;
    height: 75%;
    overflow: hidden;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 12.5%;
    bottom: 12.5%;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5588_13105 .Pixso-frame-5490_8987 {
    width: 75%;
    height: 75%;
    overflow: hidden;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 12.5%;
    bottom: 12.5%;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5588_11856 .Pixso-frame-5490_8987 {
    width: 75%;
    height: 75%;
    overflow: hidden;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 12.5%;
    bottom: 12.5%;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5588_13111 .Pixso-frame-5490_8987 {
    width: 75%;
    height: 75%;
    overflow: hidden;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 12.5%;
    bottom: 12.5%;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5588_13876 .Pixso-frame-5490_8987 {
    width: 75%;
    height: 75%;
    overflow: hidden;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 12.5%;
    bottom: 12.5%;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5588_13117 .Pixso-frame-5490_8987 {
    width: 75%;
    height: 75%;
    overflow: hidden;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 12.5%;
    bottom: 12.5%;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5588_12027 .Pixso-frame-5490_8987 {
    width: 75%;
    height: 75%;
    overflow: hidden;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 12.5%;
    bottom: 12.5%;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5588_13123 .Pixso-frame-5490_8987 {
    width: 75%;
    height: 75%;
    overflow: hidden;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 12.5%;
    bottom: 12.5%;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5588_13882 .Pixso-frame-5490_8987 {
    width: 75%;
    height: 75%;
    overflow: hidden;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 12.5%;
    bottom: 12.5%;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5588_13129 .Pixso-frame-5490_8987 {
    width: 75%;
    height: 75%;
    overflow: hidden;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 12.5%;
    bottom: 12.5%;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5588_12189 .Pixso-frame-5490_8987 {
    width: 75%;
    height: 75%;
    overflow: hidden;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 12.5%;
    bottom: 12.5%;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5588_13135 .Pixso-frame-5490_8987 {
    width: 75%;
    height: 75%;
    overflow: hidden;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 12.5%;
    bottom: 12.5%;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5588_13888 .Pixso-frame-5490_8987 {
    width: 75%;
    height: 75%;
    overflow: hidden;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 12.5%;
    bottom: 12.5%;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5588_13141 .Pixso-frame-5490_8987 {
    width: 75%;
    height: 75%;
    overflow: hidden;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 12.5%;
    bottom: 12.5%;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5588_11165 .Pixso-frame-5490_8987 {
    width: 75%;
    height: 75%;
    overflow: hidden;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 12.5%;
    bottom: 12.5%;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5588_13147 .Pixso-frame-5490_8987 {
    width: 75%;
    height: 75%;
    overflow: hidden;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 12.5%;
    bottom: 12.5%;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5588_13894 .Pixso-frame-5490_8987 {
    width: 75%;
    height: 75%;
    overflow: hidden;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 12.5%;
    bottom: 12.5%;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5588_13153 .Pixso-frame-5490_8987 {
    width: 75%;
    height: 75%;
    overflow: hidden;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 12.5%;
    bottom: 12.5%;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5588_11355 .Pixso-frame-5490_8987 {
    width: 75%;
    height: 75%;
    overflow: hidden;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 12.5%;
    bottom: 12.5%;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5588_13159 .Pixso-frame-5490_8987 {
    width: 75%;
    height: 75%;
    overflow: hidden;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 12.5%;
    bottom: 12.5%;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5588_13900 .Pixso-frame-5490_8987 {
    width: 75%;
    height: 75%;
    overflow: hidden;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 12.5%;
    bottom: 12.5%;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5588_13165 .Pixso-frame-5490_8987 {
    width: 75%;
    height: 75%;
    overflow: hidden;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 12.5%;
    bottom: 12.5%;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5588_11418 .Pixso-frame-5490_8987 {
    width: 75%;
    height: 75%;
    overflow: hidden;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 12.5%;
    bottom: 12.5%;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5588_13171 .Pixso-frame-5490_8987 {
    width: 75%;
    height: 75%;
    overflow: hidden;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 12.5%;
    bottom: 12.5%;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5588_13906 .Pixso-frame-5490_8987 {
    width: 75%;
    height: 75%;
    overflow: hidden;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 12.5%;
    bottom: 12.5%;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5588_13177 .Pixso-frame-5490_8987 {
    width: 75%;
    height: 75%;
    overflow: hidden;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 12.5%;
    bottom: 12.5%;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5588_11520 .Pixso-frame-5490_8987 {
    width: 75%;
    height: 75%;
    overflow: hidden;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 12.5%;
    bottom: 12.5%;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5588_13183 .Pixso-frame-5490_8987 {
    width: 75%;
    height: 75%;
    overflow: hidden;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 12.5%;
    bottom: 12.5%;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5588_13912 .Pixso-frame-5490_8987 {
    width: 75%;
    height: 75%;
    overflow: hidden;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 12.5%;
    bottom: 12.5%;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5588_13189 .Pixso-frame-5490_8987 {
    width: 75%;
    height: 75%;
    overflow: hidden;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 12.5%;
    bottom: 12.5%;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5588_11538 .Pixso-frame-5490_8987 {
    width: 75%;
    height: 75%;
    overflow: hidden;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 12.5%;
    bottom: 12.5%;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5588_13195 .Pixso-frame-5490_8987 {
    width: 75%;
    height: 75%;
    overflow: hidden;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 12.5%;
    bottom: 12.5%;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5588_13918 .Pixso-frame-5490_8987 {
    width: 75%;
    height: 75%;
    overflow: hidden;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 12.5%;
    bottom: 12.5%;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5588_13201 .Pixso-frame-5490_8987 {
    width: 75%;
    height: 75%;
    overflow: hidden;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 12.5%;
    bottom: 12.5%;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5588_11544 .Pixso-frame-5490_8987 {
    width: 75%;
    height: 75%;
    overflow: hidden;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 12.5%;
    bottom: 12.5%;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5588_13207 .Pixso-frame-5490_8987 {
    width: 75%;
    height: 75%;
    overflow: hidden;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 12.5%;
    bottom: 12.5%;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5588_13924 .Pixso-frame-5490_8987 {
    width: 75%;
    height: 75%;
    overflow: hidden;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 12.5%;
    bottom: 12.5%;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5588_13213 .Pixso-frame-5490_8987 {
    width: 75%;
    height: 75%;
    overflow: hidden;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 12.5%;
    bottom: 12.5%;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5586_11117 .Pixso-frame-5490_8987 {
    width: 75%;
    height: 75%;
    overflow: hidden;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 12.5%;
    bottom: 12.5%;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5588_13219 .Pixso-frame-5490_8987 {
    width: 75%;
    height: 75%;
    overflow: hidden;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 12.5%;
    bottom: 12.5%;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5588_13930 .Pixso-frame-5490_8987 {
    width: 75%;
    height: 75%;
    overflow: hidden;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 12.5%;
    bottom: 12.5%;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5588_13225 .Pixso-frame-5490_8987 {
    width: 75%;
    height: 75%;
    overflow: hidden;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 12.5%;
    bottom: 12.5%;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5588_11361 .Pixso-frame-5490_8987 {
    width: 75%;
    height: 75%;
    overflow: hidden;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 12.5%;
    bottom: 12.5%;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5588_13231 .Pixso-frame-5490_8987 {
    width: 75%;
    height: 75%;
    overflow: hidden;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 12.5%;
    bottom: 12.5%;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5588_13936 .Pixso-frame-5490_8987 {
    width: 75%;
    height: 75%;
    overflow: hidden;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 12.5%;
    bottom: 12.5%;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5588_13237 .Pixso-frame-5490_8987 {
    width: 75%;
    height: 75%;
    overflow: hidden;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 12.5%;
    bottom: 12.5%;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5588_11424 .Pixso-frame-5490_8987 {
    width: 75%;
    height: 75%;
    overflow: hidden;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 12.5%;
    bottom: 12.5%;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5588_13243 .Pixso-frame-5490_8987 {
    width: 75%;
    height: 75%;
    overflow: hidden;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 12.5%;
    bottom: 12.5%;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5588_13942 .Pixso-frame-5490_8987 {
    width: 75%;
    height: 75%;
    overflow: hidden;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 12.5%;
    bottom: 12.5%;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5588_13249 .Pixso-frame-5490_8987 {
    width: 75%;
    height: 75%;
    overflow: hidden;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 12.5%;
    bottom: 12.5%;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5588_11862 .Pixso-frame-5490_8987 {
    width: 75%;
    height: 75%;
    overflow: hidden;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 12.5%;
    bottom: 12.5%;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5588_13255 .Pixso-frame-5490_8987 {
    width: 75%;
    height: 75%;
    overflow: hidden;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 12.5%;
    bottom: 12.5%;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5588_13948 .Pixso-frame-5490_8987 {
    width: 75%;
    height: 75%;
    overflow: hidden;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 12.5%;
    bottom: 12.5%;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5588_13261 .Pixso-frame-5490_8987 {
    width: 75%;
    height: 75%;
    overflow: hidden;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 12.5%;
    bottom: 12.5%;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5588_12033 .Pixso-frame-5490_8987 {
    width: 75%;
    height: 75%;
    overflow: hidden;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 12.5%;
    bottom: 12.5%;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5588_13267 .Pixso-frame-5490_8987 {
    width: 75%;
    height: 75%;
    overflow: hidden;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 12.5%;
    bottom: 12.5%;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5588_13954 .Pixso-frame-5490_8987 {
    width: 75%;
    height: 75%;
    overflow: hidden;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 12.5%;
    bottom: 12.5%;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5588_12195 .Pixso-frame-5490_8987 {
    width: 75%;
    height: 75%;
    overflow: hidden;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 12.5%;
    bottom: 12.5%;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5588_13960 .Pixso-frame-5490_8987 {
    width: 75%;
    height: 75%;
    overflow: hidden;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 12.5%;
    bottom: 12.5%;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5588_11868 .Pixso-frame-5490_8987 {
    width: 75%;
    height: 75%;
    overflow: hidden;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 12.5%;
    bottom: 12.5%;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5588_13966 .Pixso-frame-5490_8987 {
    width: 75%;
    height: 75%;
    overflow: hidden;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 12.5%;
    bottom: 12.5%;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5588_12039 .Pixso-frame-5490_8987 {
    width: 75%;
    height: 75%;
    overflow: hidden;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 12.5%;
    bottom: 12.5%;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5588_13972 .Pixso-frame-5490_8987 {
    width: 75%;
    height: 75%;
    overflow: hidden;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 12.5%;
    bottom: 12.5%;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5588_12201 .Pixso-frame-5490_8987 {
    width: 75%;
    height: 75%;
    overflow: hidden;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 12.5%;
    bottom: 12.5%;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5588_13978 .Pixso-frame-5490_8987 {
    width: 75%;
    height: 75%;
    overflow: hidden;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 12.5%;
    bottom: 12.5%;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5588_11874 .Pixso-frame-5490_8987 {
    width: 75%;
    height: 75%;
    overflow: hidden;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 12.5%;
    bottom: 12.5%;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5588_13984 .Pixso-frame-5490_8987 {
    width: 75%;
    height: 75%;
    overflow: hidden;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 12.5%;
    bottom: 12.5%;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5588_12045 .Pixso-frame-5490_8987 {
    width: 75%;
    height: 75%;
    overflow: hidden;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 12.5%;
    bottom: 12.5%;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5588_13990 .Pixso-frame-5490_8987 {
    width: 75%;
    height: 75%;
    overflow: hidden;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 12.5%;
    bottom: 12.5%;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5588_12207 .Pixso-frame-5490_8987 {
    width: 75%;
    height: 75%;
    overflow: hidden;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 12.5%;
    bottom: 12.5%;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5588_13996 .Pixso-frame-5490_8987 {
    width: 75%;
    height: 75%;
    overflow: hidden;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 12.5%;
    bottom: 12.5%;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5588_11526 .Pixso-frame-5490_8987 {
    width: 75%;
    height: 75%;
    overflow: hidden;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 12.5%;
    bottom: 12.5%;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5588_14002 .Pixso-frame-5490_8987 {
    width: 75%;
    height: 75%;
    overflow: hidden;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 12.5%;
    bottom: 12.5%;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5588_11550 .Pixso-frame-5490_8987 {
    width: 75%;
    height: 75%;
    overflow: hidden;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 12.5%;
    bottom: 12.5%;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5588_14008 .Pixso-frame-5490_8987 {
    width: 75%;
    height: 75%;
    overflow: hidden;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 12.5%;
    bottom: 12.5%;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5588_11556 .Pixso-frame-5490_8987 {
    width: 75%;
    height: 75%;
    overflow: hidden;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 12.5%;
    bottom: 12.5%;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5588_14014 .Pixso-frame-5490_8987 {
    width: 75%;
    height: 75%;
    overflow: hidden;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 12.5%;
    bottom: 12.5%;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5588_11880 .Pixso-frame-5490_8987 {
    width: 75%;
    height: 75%;
    overflow: hidden;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 12.5%;
    bottom: 12.5%;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5588_14020 .Pixso-frame-5490_8987 {
    width: 75%;
    height: 75%;
    overflow: hidden;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 12.5%;
    bottom: 12.5%;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5588_12051 .Pixso-frame-5490_8987 {
    width: 75%;
    height: 75%;
    overflow: hidden;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 12.5%;
    bottom: 12.5%;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5588_14026 .Pixso-frame-5490_8987 {
    width: 75%;
    height: 75%;
    overflow: hidden;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 12.5%;
    bottom: 12.5%;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5588_12213 .Pixso-frame-5490_8987 {
    width: 75%;
    height: 75%;
    overflow: hidden;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 12.5%;
    bottom: 12.5%;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5588_14032 .Pixso-frame-5490_8987 {
    width: 75%;
    height: 75%;
    overflow: hidden;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 12.5%;
    bottom: 12.5%;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5588_11886 .Pixso-frame-5490_8987 {
    width: 75%;
    height: 75%;
    overflow: hidden;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 12.5%;
    bottom: 12.5%;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5588_14038 .Pixso-frame-5490_8987 {
    width: 75%;
    height: 75%;
    overflow: hidden;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 12.5%;
    bottom: 12.5%;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5588_12057 .Pixso-frame-5490_8987 {
    width: 75%;
    height: 75%;
    overflow: hidden;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 12.5%;
    bottom: 12.5%;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5588_14044 .Pixso-frame-5490_8987 {
    width: 75%;
    height: 75%;
    overflow: hidden;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 12.5%;
    bottom: 12.5%;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5588_12219 .Pixso-frame-5490_8987 {
    width: 75%;
    height: 75%;
    overflow: hidden;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 12.5%;
    bottom: 12.5%;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5588_14050 .Pixso-frame-5490_8987 {
    width: 75%;
    height: 75%;
    overflow: hidden;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 12.5%;
    bottom: 12.5%;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5588_11892 .Pixso-frame-5490_8987 {
    width: 75%;
    height: 75%;
    overflow: hidden;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 12.5%;
    bottom: 12.5%;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5588_14056 .Pixso-frame-5490_8987 {
    width: 75%;
    height: 75%;
    overflow: hidden;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 12.5%;
    bottom: 12.5%;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5588_12063 .Pixso-frame-5490_8987 {
    width: 75%;
    height: 75%;
    overflow: hidden;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 12.5%;
    bottom: 12.5%;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5588_14062 .Pixso-frame-5490_8987 {
    width: 75%;
    height: 75%;
    overflow: hidden;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 12.5%;
    bottom: 12.5%;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5588_12225 .Pixso-frame-5490_8987 {
    width: 75%;
    height: 75%;
    overflow: hidden;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 12.5%;
    bottom: 12.5%;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5588_14068 .Pixso-frame-5490_8987 {
    width: 75%;
    height: 75%;
    overflow: hidden;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 12.5%;
    bottom: 12.5%;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5588_11532 .Pixso-frame-5490_8987 {
    width: 75%;
    height: 75%;
    overflow: hidden;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 12.5%;
    bottom: 12.5%;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5588_14074 .Pixso-frame-5490_8987 {
    width: 75%;
    height: 75%;
    overflow: hidden;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 12.5%;
    bottom: 12.5%;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5588_11562 .Pixso-frame-5490_8987 {
    width: 75%;
    height: 75%;
    overflow: hidden;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 12.5%;
    bottom: 12.5%;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5588_14080 .Pixso-frame-5490_8987 {
    width: 75%;
    height: 75%;
    overflow: hidden;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 12.5%;
    bottom: 12.5%;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5588_11568 .Pixso-frame-5490_8987 {
    width: 75%;
    height: 75%;
    overflow: hidden;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 12.5%;
    bottom: 12.5%;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5588_14086 .Pixso-frame-5490_8987 {
    width: 75%;
    height: 75%;
    overflow: hidden;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 12.5%;
    bottom: 12.5%;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5588_11191 .Pixso-symbol-5578_148941 .Pixso-symbol-5578_148908 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13001 .Pixso-symbol-5578_148941 .Pixso-symbol-5578_148908 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13820 .Pixso-symbol-5578_148941 .Pixso-symbol-5578_148908 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13007 .Pixso-symbol-5578_148941 .Pixso-symbol-5578_148908 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_11347 .Pixso-symbol-5578_148941 .Pixso-symbol-5578_148908 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13013 .Pixso-symbol-5578_148941 .Pixso-symbol-5578_148908 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13826 .Pixso-symbol-5578_148941 .Pixso-symbol-5578_148908 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13019 .Pixso-symbol-5578_148941 .Pixso-symbol-5578_148908 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_11410 .Pixso-symbol-5578_148941 .Pixso-symbol-5578_148908 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13025 .Pixso-symbol-5578_148941 .Pixso-symbol-5578_148908 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13832 .Pixso-symbol-5578_148941 .Pixso-symbol-5578_148908 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13031 .Pixso-symbol-5578_148941 .Pixso-symbol-5578_148908 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_11842 .Pixso-symbol-5578_148941 .Pixso-symbol-5578_148908 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13037 .Pixso-symbol-5578_148941 .Pixso-symbol-5578_148908 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13838 .Pixso-symbol-5578_148941 .Pixso-symbol-5578_148908 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13043 .Pixso-symbol-5578_148941 .Pixso-symbol-5578_148908 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_12013 .Pixso-symbol-5578_148941 .Pixso-symbol-5578_148908 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13049 .Pixso-symbol-5578_148941 .Pixso-symbol-5578_148908 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13844 .Pixso-symbol-5578_148941 .Pixso-symbol-5578_148908 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13055 .Pixso-symbol-5578_148941 .Pixso-symbol-5578_148908 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_12175 .Pixso-symbol-5578_148941 .Pixso-symbol-5578_148908 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13061 .Pixso-symbol-5578_148941 .Pixso-symbol-5578_148908 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13850 .Pixso-symbol-5578_148941 .Pixso-symbol-5578_148908 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13067 .Pixso-symbol-5578_148941 .Pixso-symbol-5578_148908 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_11848 .Pixso-symbol-5578_148941 .Pixso-symbol-5578_148908 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13073 .Pixso-symbol-5578_148941 .Pixso-symbol-5578_148908 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13856 .Pixso-symbol-5578_148941 .Pixso-symbol-5578_148908 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13079 .Pixso-symbol-5578_148941 .Pixso-symbol-5578_148908 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_12019 .Pixso-symbol-5578_148941 .Pixso-symbol-5578_148908 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13085 .Pixso-symbol-5578_148941 .Pixso-symbol-5578_148908 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13862 .Pixso-symbol-5578_148941 .Pixso-symbol-5578_148908 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13091 .Pixso-symbol-5578_148941 .Pixso-symbol-5578_148908 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_12181 .Pixso-symbol-5578_148941 .Pixso-symbol-5578_148908 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13097 .Pixso-symbol-5578_148941 .Pixso-symbol-5578_148908 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13868 .Pixso-symbol-5578_148941 .Pixso-symbol-5578_148908 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13103 .Pixso-symbol-5578_148941 .Pixso-symbol-5578_148908 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_11854 .Pixso-symbol-5578_148941 .Pixso-symbol-5578_148908 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13109 .Pixso-symbol-5578_148941 .Pixso-symbol-5578_148908 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13874 .Pixso-symbol-5578_148941 .Pixso-symbol-5578_148908 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13115 .Pixso-symbol-5578_148941 .Pixso-symbol-5578_148908 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_12025 .Pixso-symbol-5578_148941 .Pixso-symbol-5578_148908 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13121 .Pixso-symbol-5578_148941 .Pixso-symbol-5578_148908 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13880 .Pixso-symbol-5578_148941 .Pixso-symbol-5578_148908 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13127 .Pixso-symbol-5578_148941 .Pixso-symbol-5578_148908 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_12187 .Pixso-symbol-5578_148941 .Pixso-symbol-5578_148908 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13133 .Pixso-symbol-5578_148941 .Pixso-symbol-5578_148908 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13886 .Pixso-symbol-5578_148941 .Pixso-symbol-5578_148908 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13139 .Pixso-symbol-5578_148941 .Pixso-symbol-5578_148908 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_11164 .Pixso-symbol-5578_148941 .Pixso-symbol-5578_148908 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13145 .Pixso-symbol-5578_148941 .Pixso-symbol-5578_148908 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13892 .Pixso-symbol-5578_148941 .Pixso-symbol-5578_148908 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13151 .Pixso-symbol-5578_148941 .Pixso-symbol-5578_148908 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_11353 .Pixso-symbol-5578_148941 .Pixso-symbol-5578_148908 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13157 .Pixso-symbol-5578_148941 .Pixso-symbol-5578_148908 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13898 .Pixso-symbol-5578_148941 .Pixso-symbol-5578_148908 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13163 .Pixso-symbol-5578_148941 .Pixso-symbol-5578_148908 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_11416 .Pixso-symbol-5578_148941 .Pixso-symbol-5578_148908 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13169 .Pixso-symbol-5578_148941 .Pixso-symbol-5578_148908 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13904 .Pixso-symbol-5578_148941 .Pixso-symbol-5578_148908 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13175 .Pixso-symbol-5578_148941 .Pixso-symbol-5578_148908 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_11518 .Pixso-symbol-5578_148941 .Pixso-symbol-5578_148908 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13181 .Pixso-symbol-5578_148941 .Pixso-symbol-5578_148908 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13910 .Pixso-symbol-5578_148941 .Pixso-symbol-5578_148908 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13187 .Pixso-symbol-5578_148941 .Pixso-symbol-5578_148908 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_11536 .Pixso-symbol-5578_148941 .Pixso-symbol-5578_148908 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13193 .Pixso-symbol-5578_148941 .Pixso-symbol-5578_148908 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13916 .Pixso-symbol-5578_148941 .Pixso-symbol-5578_148908 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13199 .Pixso-symbol-5578_148941 .Pixso-symbol-5578_148908 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_11542 .Pixso-symbol-5578_148941 .Pixso-symbol-5578_148908 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13205 .Pixso-symbol-5578_148941 .Pixso-symbol-5578_148908 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13922 .Pixso-symbol-5578_148941 .Pixso-symbol-5578_148908 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5588_13211 .Pixso-symbol-5578_148941 .Pixso-symbol-5578_148908 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5494_4828 .Pixso-symbol-5578_148941 .Pixso-symbol-5578_148908 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13217 .Pixso-symbol-5578_148941 .Pixso-symbol-5578_148908 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13928 .Pixso-symbol-5578_148941 .Pixso-symbol-5578_148908 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13223 .Pixso-symbol-5578_148941 .Pixso-symbol-5578_148908 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_11359 .Pixso-symbol-5578_148941 .Pixso-symbol-5578_148908 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13229 .Pixso-symbol-5578_148941 .Pixso-symbol-5578_148908 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13934 .Pixso-symbol-5578_148941 .Pixso-symbol-5578_148908 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13235 .Pixso-symbol-5578_148941 .Pixso-symbol-5578_148908 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_11422 .Pixso-symbol-5578_148941 .Pixso-symbol-5578_148908 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13241 .Pixso-symbol-5578_148941 .Pixso-symbol-5578_148908 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13940 .Pixso-symbol-5578_148941 .Pixso-symbol-5578_148908 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13247 .Pixso-symbol-5578_148941 .Pixso-symbol-5578_148908 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_11860 .Pixso-symbol-5578_148941 .Pixso-symbol-5578_148908 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13253 .Pixso-symbol-5578_148941 .Pixso-symbol-5578_148908 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13946 .Pixso-symbol-5578_148941 .Pixso-symbol-5578_148908 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13259 .Pixso-symbol-5578_148941 .Pixso-symbol-5578_148908 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_12031 .Pixso-symbol-5578_148941 .Pixso-symbol-5578_148908 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13265 .Pixso-symbol-5578_148941 .Pixso-symbol-5578_148908 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13952 .Pixso-symbol-5578_148941 .Pixso-symbol-5578_148908 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_12193 .Pixso-symbol-5578_148941 .Pixso-symbol-5578_148908 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13958 .Pixso-symbol-5578_148941 .Pixso-symbol-5578_148908 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_11866 .Pixso-symbol-5578_148941 .Pixso-symbol-5578_148908 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13964 .Pixso-symbol-5578_148941 .Pixso-symbol-5578_148908 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_12037 .Pixso-symbol-5578_148941 .Pixso-symbol-5578_148908 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13970 .Pixso-symbol-5578_148941 .Pixso-symbol-5578_148908 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_12199 .Pixso-symbol-5578_148941 .Pixso-symbol-5578_148908 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13976 .Pixso-symbol-5578_148941 .Pixso-symbol-5578_148908 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_11872 .Pixso-symbol-5578_148941 .Pixso-symbol-5578_148908 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13982 .Pixso-symbol-5578_148941 .Pixso-symbol-5578_148908 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_12043 .Pixso-symbol-5578_148941 .Pixso-symbol-5578_148908 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13988 .Pixso-symbol-5578_148941 .Pixso-symbol-5578_148908 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_12205 .Pixso-symbol-5578_148941 .Pixso-symbol-5578_148908 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_13994 .Pixso-symbol-5578_148941 .Pixso-symbol-5578_148908 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_11524 .Pixso-symbol-5578_148941 .Pixso-symbol-5578_148908 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_14000 .Pixso-symbol-5578_148941 .Pixso-symbol-5578_148908 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_11548 .Pixso-symbol-5578_148941 .Pixso-symbol-5578_148908 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_14006 .Pixso-symbol-5578_148941 .Pixso-symbol-5578_148908 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_11554 .Pixso-symbol-5578_148941 .Pixso-symbol-5578_148908 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_14012 .Pixso-symbol-5578_148941 .Pixso-symbol-5578_148908 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 10px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_11878 .Pixso-symbol-5578_148941 .Pixso-symbol-5578_148908 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_14018 .Pixso-symbol-5578_148941 .Pixso-symbol-5578_148908 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_12049 .Pixso-symbol-5578_148941 .Pixso-symbol-5578_148908 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_14024 .Pixso-symbol-5578_148941 .Pixso-symbol-5578_148908 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_12211 .Pixso-symbol-5578_148941 .Pixso-symbol-5578_148908 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_14030 .Pixso-symbol-5578_148941 .Pixso-symbol-5578_148908 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_11884 .Pixso-symbol-5578_148941 .Pixso-symbol-5578_148908 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_14036 .Pixso-symbol-5578_148941 .Pixso-symbol-5578_148908 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_12055 .Pixso-symbol-5578_148941 .Pixso-symbol-5578_148908 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_14042 .Pixso-symbol-5578_148941 .Pixso-symbol-5578_148908 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_12217 .Pixso-symbol-5578_148941 .Pixso-symbol-5578_148908 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_14048 .Pixso-symbol-5578_148941 .Pixso-symbol-5578_148908 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_11890 .Pixso-symbol-5578_148941 .Pixso-symbol-5578_148908 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_14054 .Pixso-symbol-5578_148941 .Pixso-symbol-5578_148908 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_12061 .Pixso-symbol-5578_148941 .Pixso-symbol-5578_148908 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_14060 .Pixso-symbol-5578_148941 .Pixso-symbol-5578_148908 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_12223 .Pixso-symbol-5578_148941 .Pixso-symbol-5578_148908 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_14066 .Pixso-symbol-5578_148941 .Pixso-symbol-5578_148908 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_11530 .Pixso-symbol-5578_148941 .Pixso-symbol-5578_148908 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_14072 .Pixso-symbol-5578_148941 .Pixso-symbol-5578_148908 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_11560 .Pixso-symbol-5578_148941 .Pixso-symbol-5578_148908 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_14078 .Pixso-symbol-5578_148941 .Pixso-symbol-5578_148908 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_11566 .Pixso-symbol-5578_148941 .Pixso-symbol-5578_148908 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5588_14084 .Pixso-symbol-5578_148941 .Pixso-symbol-5578_148908 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 8px;
    top: 6px;
    background-color: transparent;
}
</style>
