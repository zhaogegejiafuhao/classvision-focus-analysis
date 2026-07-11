<template>
    <div class="component-5607_19608">
        <div id="5607_19608" class="Pixso-symbol-5607_19608">
            <div
                id="5607_19585"
                class="Pixso-symbol-5607_19585"
                v-if="
                    State === 'Default' && Type === 'Default' && Size === 'lg'
                "
            >
                <div id="5607_19584" class="Pixso-frame-5607_19584">
                    <div class="frame-content-5607_19584">
                        <slot name="slot_5607_19582" v-if="visible_5607_114">
                            <p
                                id="5607_19582"
                                class="Pixso-paragraph-5607_19582 fill-gray80-32_4123-paragraph text-text-smbold-423_3208"
                            >
                                {{ text_5607_120 ?? "Label" }}
                            </p>
                        </slot>
                        <slot name="slot_5607_19554">
                            <InputTextBase
                                id="5607_19554"
                                class="Pixso-instance-5607_19554"
                                Type="Default"
                                Size="lg"
                            />
                        </slot>
                    </div>
                </div>
                <slot name="slot_5607_19581" v-if="visible_5607_117">
                    <p
                        id="5607_19581"
                        class="Pixso-paragraph-5607_19581 fill-gray60-83_2722-paragraph text-text-smmedium-5454_21607"
                    >
                        {{ text_5607_123 ?? "This is an input helper text." }}
                    </p>
                </slot>
            </div>
            <div
                id="5608_19697"
                class="Pixso-symbol-5608_19697"
                v-if="State === 'Hover' && Type === 'Default' && Size === 'lg'"
            >
                <div id="5608_19698" class="Pixso-frame-5608_19698">
                    <div class="frame-content-5608_19698">
                        <slot name="slot_5608_19699" v-if="visible_5607_114">
                            <p
                                id="5608_19699"
                                class="Pixso-paragraph-5608_19699 fill-gray80-32_4123-paragraph text-text-smbold-423_3208"
                            >
                                {{ text_5607_120 ?? "Label" }}
                            </p>
                        </slot>
                        <slot name="slot_5608_19700">
                            <InputTextBase
                                id="5608_19700"
                                class="Pixso-instance-5608_19700"
                                Type="Default"
                                Size="lg"
                            />
                        </slot>
                    </div>
                </div>
                <slot name="slot_5608_19701" v-if="visible_5607_117">
                    <p
                        id="5608_19701"
                        class="Pixso-paragraph-5608_19701 fill-gray60-83_2722-paragraph text-text-smmedium-5454_21607"
                    >
                        {{ text_5607_123 ?? "This is an input helper text." }}
                    </p>
                </slot>
            </div>
            <div
                id="5607_19609"
                class="Pixso-symbol-5607_19609"
                v-if="State === 'Filled' && Type === 'Default' && Size === 'lg'"
            >
                <div id="5607_19610" class="Pixso-frame-5607_19610">
                    <div class="frame-content-5607_19610">
                        <slot name="slot_5607_19611" v-if="visible_5607_114">
                            <p
                                id="5607_19611"
                                class="Pixso-paragraph-5607_19611 fill-gray80-32_4123-paragraph text-text-smbold-423_3208"
                            >
                                {{ text_5607_120 ?? "Label" }}
                            </p>
                        </slot>
                        <slot name="slot_5607_19612">
                            <InputTextBase
                                id="5607_19612"
                                class="Pixso-instance-5607_19612"
                                Type="Default"
                                Size="lg"
                            />
                        </slot>
                    </div>
                </div>
                <slot name="slot_5607_19613" v-if="visible_5607_117">
                    <p
                        id="5607_19613"
                        class="Pixso-paragraph-5607_19613 fill-gray60-83_2722-paragraph text-text-smmedium-5454_21607"
                    >
                        {{ text_5607_123 ?? "This is an input helper text." }}
                    </p>
                </slot>
            </div>
            <div
                id="5608_19653"
                class="Pixso-symbol-5608_19653"
                v-if="
                    State === 'Focused' && Type === 'Default' && Size === 'lg'
                "
            >
                <div id="5608_19654" class="Pixso-frame-5608_19654">
                    <div class="frame-content-5608_19654">
                        <slot name="slot_5608_19655" v-if="visible_5607_114">
                            <p
                                id="5608_19655"
                                class="Pixso-paragraph-5608_19655 fill-gray80-32_4123-paragraph text-text-smbold-423_3208"
                            >
                                {{ text_5607_120 ?? "Label" }}
                            </p>
                        </slot>
                        <slot name="slot_5608_19656">
                            <InputTextBase
                                id="5608_19656"
                                class="Pixso-instance-5608_19656"
                                Type="Default"
                                Size="lg"
                            />
                        </slot>
                    </div>
                </div>
                <slot name="slot_5608_19657" v-if="visible_5607_117">
                    <p
                        id="5608_19657"
                        class="Pixso-paragraph-5608_19657 fill-gray60-83_2722-paragraph text-text-smmedium-5454_21607"
                    >
                        {{ text_5607_123 ?? "This is an input helper text." }}
                    </p>
                </slot>
            </div>
            <div
                id="5608_19675"
                class="Pixso-symbol-5608_19675"
                v-if="
                    State === 'Disabled' && Type === 'Default' && Size === 'lg'
                "
            >
                <div id="5608_19676" class="Pixso-frame-5608_19676">
                    <div class="frame-content-5608_19676">
                        <slot name="slot_5608_19677" v-if="visible_5607_114">
                            <p
                                id="5608_19677"
                                class="Pixso-paragraph-5608_19677 fill-gray80-32_4123-paragraph text-text-smbold-423_3208"
                            >
                                {{ text_5607_120 ?? "Label" }}
                            </p>
                        </slot>
                        <slot name="slot_5608_19678">
                            <InputTextBase
                                id="5608_19678"
                                class="Pixso-instance-5608_19678"
                                Type="Default"
                                Size="lg"
                            >
                                <template #slot_5606_19068>
                                    <User
                                        id="5606_19068"
                                        class="Pixso-instance-5606_19068"
                                        Format="Outline"
                                        Weight="Bold"
                                    />
                                </template>
                                <template #slot_5606_19072>
                                    <Question
                                        id="5606_19072"
                                        class="Pixso-instance-5606_19072"
                                        Format="Outline"
                                        Weight="Bold"
                                    />
                                </template>
                            </InputTextBase>
                        </slot>
                    </div>
                </div>
                <slot name="slot_5608_19679" v-if="visible_5607_117">
                    <p
                        id="5608_19679"
                        class="Pixso-paragraph-5608_19679 fill-gray60-83_2722-paragraph text-text-smmedium-5454_21607"
                    >
                        {{ text_5607_123 ?? "This is an input helper text." }}
                    </p>
                </slot>
            </div>
            <div
                id="5609_20111"
                class="Pixso-symbol-5609_20111"
                v-if="State === 'Error' && Type === 'Default' && Size === 'lg'"
            >
                <div id="5609_20112" class="Pixso-frame-5609_20112">
                    <div class="frame-content-5609_20112">
                        <slot name="slot_5609_20113" v-if="visible_5607_114">
                            <p
                                id="5609_20113"
                                class="Pixso-paragraph-5609_20113 fill-gray80-32_4123-paragraph text-text-smbold-423_3208"
                            >
                                {{ text_5607_120 ?? "Label" }}
                            </p>
                        </slot>
                        <slot name="slot_5609_20114">
                            <InputTextBase
                                id="5609_20114"
                                class="Pixso-instance-5609_20114"
                                Type="Default"
                                Size="lg"
                            />
                        </slot>
                    </div>
                </div>
                <slot name="slot_5609_20115" v-if="visible_5607_117">
                    <p
                        id="5609_20115"
                        class="Pixso-paragraph-5609_20115 fill-destructive50-423_3219-paragraph text-text-smmedium-5454_21607"
                    >
                        {{ text_5607_123 ?? "This is an input helper text." }}
                    </p>
                </slot>
            </div>
            <div
                id="5608_19763"
                class="Pixso-symbol-5608_19763"
                v-if="State === 'Default' && Type === 'Action' && Size === 'lg'"
            >
                <div id="5608_19764" class="Pixso-frame-5608_19764">
                    <div class="frame-content-5608_19764">
                        <slot name="slot_5608_19765" v-if="visible_5607_114">
                            <p
                                id="5608_19765"
                                class="Pixso-paragraph-5608_19765 fill-gray80-32_4123-paragraph text-text-smbold-423_3208"
                            >
                                {{ text_5607_120 ?? "Label" }}
                            </p>
                        </slot>
                        <slot name="slot_5608_19766">
                            <InputTextBase
                                id="5608_19766"
                                class="Pixso-instance-5608_19766"
                                Type="Action"
                                Size="lg"
                            />
                        </slot>
                    </div>
                </div>
                <slot name="slot_5608_19767" v-if="visible_5607_117">
                    <p
                        id="5608_19767"
                        class="Pixso-paragraph-5608_19767 fill-gray60-83_2722-paragraph text-text-smmedium-5454_21607"
                    >
                        {{ text_5607_123 ?? "This is an input helper text." }}
                    </p>
                </slot>
            </div>
            <div
                id="5608_19768"
                class="Pixso-symbol-5608_19768"
                v-if="State === 'Hover' && Type === 'Action' && Size === 'lg'"
            >
                <div id="5608_19769" class="Pixso-frame-5608_19769">
                    <div class="frame-content-5608_19769">
                        <slot name="slot_5608_19770" v-if="visible_5607_114">
                            <p
                                id="5608_19770"
                                class="Pixso-paragraph-5608_19770 fill-gray80-32_4123-paragraph text-text-smbold-423_3208"
                            >
                                {{ text_5607_120 ?? "Label" }}
                            </p>
                        </slot>
                        <slot name="slot_5608_19771">
                            <InputTextBase
                                id="5608_19771"
                                class="Pixso-instance-5608_19771"
                                Type="Action"
                                Size="lg"
                            />
                        </slot>
                    </div>
                </div>
                <slot name="slot_5608_19772" v-if="visible_5607_117">
                    <p
                        id="5608_19772"
                        class="Pixso-paragraph-5608_19772 fill-gray60-83_2722-paragraph text-text-smmedium-5454_21607"
                    >
                        {{ text_5607_123 ?? "This is an input helper text." }}
                    </p>
                </slot>
            </div>
            <div
                id="5608_19773"
                class="Pixso-symbol-5608_19773"
                v-if="State === 'Filled' && Type === 'Action' && Size === 'lg'"
            >
                <div id="5608_19774" class="Pixso-frame-5608_19774">
                    <div class="frame-content-5608_19774">
                        <slot name="slot_5608_19775" v-if="visible_5607_114">
                            <p
                                id="5608_19775"
                                class="Pixso-paragraph-5608_19775 fill-gray80-32_4123-paragraph text-text-smbold-423_3208"
                            >
                                {{ text_5607_120 ?? "Label" }}
                            </p>
                        </slot>
                        <slot name="slot_5608_19776">
                            <InputTextBase
                                id="5608_19776"
                                class="Pixso-instance-5608_19776"
                                Type="Action"
                                Size="lg"
                            />
                        </slot>
                    </div>
                </div>
                <slot name="slot_5608_19777" v-if="visible_5607_117">
                    <p
                        id="5608_19777"
                        class="Pixso-paragraph-5608_19777 fill-gray60-83_2722-paragraph text-text-smmedium-5454_21607"
                    >
                        {{ text_5607_123 ?? "This is an input helper text." }}
                    </p>
                </slot>
            </div>
            <div
                id="5608_19778"
                class="Pixso-symbol-5608_19778"
                v-if="State === 'Focused' && Type === 'Action' && Size === 'lg'"
            >
                <div id="5608_19779" class="Pixso-frame-5608_19779">
                    <div class="frame-content-5608_19779">
                        <slot name="slot_5608_19780" v-if="visible_5607_114">
                            <p
                                id="5608_19780"
                                class="Pixso-paragraph-5608_19780 fill-gray80-32_4123-paragraph text-text-smbold-423_3208"
                            >
                                {{ text_5607_120 ?? "Label" }}
                            </p>
                        </slot>
                        <slot name="slot_5608_19781">
                            <InputTextBase
                                id="5608_19781"
                                class="Pixso-instance-5608_19781"
                                Type="Action"
                                Size="lg"
                            />
                        </slot>
                    </div>
                </div>
                <slot name="slot_5608_19782" v-if="visible_5607_117">
                    <p
                        id="5608_19782"
                        class="Pixso-paragraph-5608_19782 fill-gray60-83_2722-paragraph text-text-smmedium-5454_21607"
                    >
                        {{ text_5607_123 ?? "This is an input helper text." }}
                    </p>
                </slot>
            </div>
            <div
                id="5608_19783"
                class="Pixso-symbol-5608_19783"
                v-if="
                    State === 'Disabled' && Type === 'Action' && Size === 'lg'
                "
            >
                <div id="5608_19784" class="Pixso-frame-5608_19784">
                    <div class="frame-content-5608_19784">
                        <slot name="slot_5608_19785" v-if="visible_5607_114">
                            <p
                                id="5608_19785"
                                class="Pixso-paragraph-5608_19785 fill-gray80-32_4123-paragraph text-text-smbold-423_3208"
                            >
                                {{ text_5607_120 ?? "Label" }}
                            </p>
                        </slot>
                        <slot name="slot_5608_19786">
                            <InputTextBase
                                id="5608_19786"
                                class="Pixso-instance-5608_19786"
                                Type="Action"
                                Size="lg"
                            >
                                <template #slot_5606_19157>
                                    <CopySimple
                                        id="5606_19157"
                                        class="Pixso-instance-5606_19157"
                                        Format="Outline"
                                        Weight="Bold"
                                    />
                                </template>
                            </InputTextBase>
                        </slot>
                    </div>
                </div>
                <slot name="slot_5608_19787" v-if="visible_5607_117">
                    <p
                        id="5608_19787"
                        class="Pixso-paragraph-5608_19787 fill-gray60-83_2722-paragraph text-text-smmedium-5454_21607"
                    >
                        {{ text_5607_123 ?? "This is an input helper text." }}
                    </p>
                </slot>
            </div>
            <div
                id="5609_20116"
                class="Pixso-symbol-5609_20116"
                v-if="State === 'Error' && Type === 'Action' && Size === 'lg'"
            >
                <div id="5609_20117" class="Pixso-frame-5609_20117">
                    <div class="frame-content-5609_20117">
                        <slot name="slot_5609_20118" v-if="visible_5607_114">
                            <p
                                id="5609_20118"
                                class="Pixso-paragraph-5609_20118 fill-gray80-32_4123-paragraph text-text-smbold-423_3208"
                            >
                                {{ text_5607_120 ?? "Label" }}
                            </p>
                        </slot>
                        <slot name="slot_5609_20119">
                            <InputTextBase
                                id="5609_20119"
                                class="Pixso-instance-5609_20119"
                                Type="Action"
                                Size="lg"
                            />
                        </slot>
                    </div>
                </div>
                <slot name="slot_5609_20120" v-if="visible_5607_117">
                    <p
                        id="5609_20120"
                        class="Pixso-paragraph-5609_20120 fill-destructive50-423_3219-paragraph text-text-smmedium-5454_21607"
                    >
                        {{ text_5607_123 ?? "This is an input helper text." }}
                    </p>
                </slot>
            </div>
            <div
                id="5608_19953"
                class="Pixso-symbol-5608_19953"
                v-if="
                    State === 'Default' && Type === 'Currency' && Size === 'lg'
                "
            >
                <div id="5608_19954" class="Pixso-frame-5608_19954">
                    <div class="frame-content-5608_19954">
                        <slot name="slot_5608_19955" v-if="visible_5607_114">
                            <p
                                id="5608_19955"
                                class="Pixso-paragraph-5608_19955 fill-gray80-32_4123-paragraph text-text-smbold-423_3208"
                            >
                                {{ text_5607_120 ?? "Label" }}
                            </p>
                        </slot>
                        <slot name="slot_5608_19956">
                            <InputTextBase
                                id="5608_19956"
                                class="Pixso-instance-5608_19956"
                                Type="Currency"
                                Size="lg"
                            />
                        </slot>
                    </div>
                </div>
                <slot name="slot_5608_19957" v-if="visible_5607_117">
                    <p
                        id="5608_19957"
                        class="Pixso-paragraph-5608_19957 fill-gray60-83_2722-paragraph text-text-smmedium-5454_21607"
                    >
                        {{ text_5607_123 ?? "This is an input helper text." }}
                    </p>
                </slot>
            </div>
            <div
                id="5608_19958"
                class="Pixso-symbol-5608_19958"
                v-if="State === 'Hover' && Type === 'Currency' && Size === 'lg'"
            >
                <div id="5608_19959" class="Pixso-frame-5608_19959">
                    <div class="frame-content-5608_19959">
                        <slot name="slot_5608_19960" v-if="visible_5607_114">
                            <p
                                id="5608_19960"
                                class="Pixso-paragraph-5608_19960 fill-gray80-32_4123-paragraph text-text-smbold-423_3208"
                            >
                                {{ text_5607_120 ?? "Label" }}
                            </p>
                        </slot>
                        <slot name="slot_5608_19961">
                            <InputTextBase
                                id="5608_19961"
                                class="Pixso-instance-5608_19961"
                                Type="Currency"
                                Size="lg"
                            />
                        </slot>
                    </div>
                </div>
                <slot name="slot_5608_19962" v-if="visible_5607_117">
                    <p
                        id="5608_19962"
                        class="Pixso-paragraph-5608_19962 fill-gray60-83_2722-paragraph text-text-smmedium-5454_21607"
                    >
                        {{ text_5607_123 ?? "This is an input helper text." }}
                    </p>
                </slot>
            </div>
            <div
                id="5608_19963"
                class="Pixso-symbol-5608_19963"
                v-if="
                    State === 'Filled' && Type === 'Currency' && Size === 'lg'
                "
            >
                <div id="5608_19964" class="Pixso-frame-5608_19964">
                    <div class="frame-content-5608_19964">
                        <slot name="slot_5608_19965" v-if="visible_5607_114">
                            <p
                                id="5608_19965"
                                class="Pixso-paragraph-5608_19965 fill-gray80-32_4123-paragraph text-text-smbold-423_3208"
                            >
                                {{ text_5607_120 ?? "Label" }}
                            </p>
                        </slot>
                        <slot name="slot_5608_19966">
                            <InputTextBase
                                id="5608_19966"
                                class="Pixso-instance-5608_19966"
                                Type="Currency"
                                Size="lg"
                            />
                        </slot>
                    </div>
                </div>
                <slot name="slot_5608_19967" v-if="visible_5607_117">
                    <p
                        id="5608_19967"
                        class="Pixso-paragraph-5608_19967 fill-gray60-83_2722-paragraph text-text-smmedium-5454_21607"
                    >
                        {{ text_5607_123 ?? "This is an input helper text." }}
                    </p>
                </slot>
            </div>
            <div
                id="5608_19968"
                class="Pixso-symbol-5608_19968"
                v-if="
                    State === 'Focused' && Type === 'Currency' && Size === 'lg'
                "
            >
                <div id="5608_19969" class="Pixso-frame-5608_19969">
                    <div class="frame-content-5608_19969">
                        <slot name="slot_5608_19970" v-if="visible_5607_114">
                            <p
                                id="5608_19970"
                                class="Pixso-paragraph-5608_19970 fill-gray80-32_4123-paragraph text-text-smbold-423_3208"
                            >
                                {{ text_5607_120 ?? "Label" }}
                            </p>
                        </slot>
                        <slot name="slot_5608_19971">
                            <InputTextBase
                                id="5608_19971"
                                class="Pixso-instance-5608_19971"
                                Type="Currency"
                                Size="lg"
                            />
                        </slot>
                    </div>
                </div>
                <slot name="slot_5608_19972" v-if="visible_5607_117">
                    <p
                        id="5608_19972"
                        class="Pixso-paragraph-5608_19972 fill-gray60-83_2722-paragraph text-text-smmedium-5454_21607"
                    >
                        {{ text_5607_123 ?? "This is an input helper text." }}
                    </p>
                </slot>
            </div>
            <div
                id="5608_19973"
                class="Pixso-symbol-5608_19973"
                v-if="
                    State === 'Disabled' && Type === 'Currency' && Size === 'lg'
                "
            >
                <div id="5608_19974" class="Pixso-frame-5608_19974">
                    <div class="frame-content-5608_19974">
                        <slot name="slot_5608_19975" v-if="visible_5607_114">
                            <p
                                id="5608_19975"
                                class="Pixso-paragraph-5608_19975 fill-gray80-32_4123-paragraph text-text-smbold-423_3208"
                            >
                                {{ text_5607_120 ?? "Label" }}
                            </p>
                        </slot>
                        <slot name="slot_5608_19976">
                            <InputTextBase
                                id="5608_19976"
                                class="Pixso-instance-5608_19976"
                                Type="Currency"
                                Size="lg"
                            >
                                <template #slot_5606_19176>
                                    <CaretDown
                                        id="5606_19176"
                                        class="Pixso-instance-5606_19176"
                                        Format="Outline"
                                        Weight="Bold"
                                    />
                                </template>
                                <template #slot_5606_19174>
                                    <CurrencyDollarSimple
                                        id="5606_19174"
                                        class="Pixso-instance-5606_19174"
                                        Format="Outline"
                                        Weight="Bold"
                                    />
                                </template>
                            </InputTextBase>
                        </slot>
                    </div>
                </div>
                <slot name="slot_5608_19977" v-if="visible_5607_117">
                    <p
                        id="5608_19977"
                        class="Pixso-paragraph-5608_19977 fill-gray60-83_2722-paragraph text-text-smmedium-5454_21607"
                    >
                        {{ text_5607_123 ?? "This is an input helper text." }}
                    </p>
                </slot>
            </div>
            <div
                id="5609_20121"
                class="Pixso-symbol-5609_20121"
                v-if="State === 'Error' && Type === 'Currency' && Size === 'lg'"
            >
                <div id="5609_20122" class="Pixso-frame-5609_20122">
                    <div class="frame-content-5609_20122">
                        <slot name="slot_5609_20123" v-if="visible_5607_114">
                            <p
                                id="5609_20123"
                                class="Pixso-paragraph-5609_20123 fill-gray80-32_4123-paragraph text-text-smbold-423_3208"
                            >
                                {{ text_5607_120 ?? "Label" }}
                            </p>
                        </slot>
                        <slot name="slot_5609_20124">
                            <InputTextBase
                                id="5609_20124"
                                class="Pixso-instance-5609_20124"
                                Type="Currency"
                                Size="lg"
                            />
                        </slot>
                    </div>
                </div>
                <slot name="slot_5609_20125" v-if="visible_5607_117">
                    <p
                        id="5609_20125"
                        class="Pixso-paragraph-5609_20125 fill-destructive50-423_3219-paragraph text-text-smmedium-5454_21607"
                    >
                        {{ text_5607_123 ?? "This is an input helper text." }}
                    </p>
                </slot>
            </div>
            <div
                id="5609_20232"
                class="Pixso-symbol-5609_20232"
                v-if="
                    State === 'Default' &&
                    Type === 'Credit Card' &&
                    Size === 'lg'
                "
            >
                <div id="5609_20233" class="Pixso-frame-5609_20233">
                    <div class="frame-content-5609_20233">
                        <slot name="slot_5609_20234" v-if="visible_5607_114">
                            <p
                                id="5609_20234"
                                class="Pixso-paragraph-5609_20234 fill-gray80-32_4123-paragraph text-text-smbold-423_3208"
                            >
                                {{ text_5607_120 ?? "Label" }}
                            </p>
                        </slot>
                        <slot name="slot_5609_20235">
                            <InputTextBase
                                id="5609_20235"
                                class="Pixso-instance-5609_20235"
                                Type="Credit Card"
                                Size="lg"
                            />
                        </slot>
                    </div>
                </div>
                <slot name="slot_5609_20236" v-if="visible_5607_117">
                    <p
                        id="5609_20236"
                        class="Pixso-paragraph-5609_20236 fill-gray60-83_2722-paragraph text-text-smmedium-5454_21607"
                    >
                        {{ text_5607_123 ?? "This is an input helper text." }}
                    </p>
                </slot>
            </div>
            <div
                id="5609_20242"
                class="Pixso-symbol-5609_20242"
                v-if="
                    State === 'Hover' && Type === 'Credit Card' && Size === 'lg'
                "
            >
                <div id="5609_20243" class="Pixso-frame-5609_20243">
                    <div class="frame-content-5609_20243">
                        <slot name="slot_5609_20244" v-if="visible_5607_114">
                            <p
                                id="5609_20244"
                                class="Pixso-paragraph-5609_20244 fill-gray80-32_4123-paragraph text-text-smbold-423_3208"
                            >
                                {{ text_5607_120 ?? "Label" }}
                            </p>
                        </slot>
                        <slot name="slot_5609_20245">
                            <InputTextBase
                                id="5609_20245"
                                class="Pixso-instance-5609_20245"
                                Type="Credit Card"
                                Size="lg"
                            />
                        </slot>
                    </div>
                </div>
                <slot name="slot_5609_20246" v-if="visible_5607_117">
                    <p
                        id="5609_20246"
                        class="Pixso-paragraph-5609_20246 fill-gray60-83_2722-paragraph text-text-smmedium-5454_21607"
                    >
                        {{ text_5607_123 ?? "This is an input helper text." }}
                    </p>
                </slot>
            </div>
            <div
                id="5609_20247"
                class="Pixso-symbol-5609_20247"
                v-if="
                    State === 'Filled' &&
                    Type === 'Credit Card' &&
                    Size === 'lg'
                "
            >
                <div id="5609_20248" class="Pixso-frame-5609_20248">
                    <div class="frame-content-5609_20248">
                        <slot name="slot_5609_20249" v-if="visible_5607_114">
                            <p
                                id="5609_20249"
                                class="Pixso-paragraph-5609_20249 fill-gray80-32_4123-paragraph text-text-smbold-423_3208"
                            >
                                {{ text_5607_120 ?? "Label" }}
                            </p>
                        </slot>
                        <slot name="slot_5609_20250">
                            <InputTextBase
                                id="5609_20250"
                                class="Pixso-instance-5609_20250"
                                Type="Credit Card"
                                Size="lg"
                            />
                        </slot>
                    </div>
                </div>
                <slot name="slot_5609_20251" v-if="visible_5607_117">
                    <p
                        id="5609_20251"
                        class="Pixso-paragraph-5609_20251 fill-gray60-83_2722-paragraph text-text-smmedium-5454_21607"
                    >
                        {{ text_5607_123 ?? "This is an input helper text." }}
                    </p>
                </slot>
            </div>
            <div
                id="5609_20252"
                class="Pixso-symbol-5609_20252"
                v-if="
                    State === 'Focused' &&
                    Type === 'Credit Card' &&
                    Size === 'lg'
                "
            >
                <div id="5609_20253" class="Pixso-frame-5609_20253">
                    <div class="frame-content-5609_20253">
                        <slot name="slot_5609_20254" v-if="visible_5607_114">
                            <p
                                id="5609_20254"
                                class="Pixso-paragraph-5609_20254 fill-gray80-32_4123-paragraph text-text-smbold-423_3208"
                            >
                                {{ text_5607_120 ?? "Label" }}
                            </p>
                        </slot>
                        <slot name="slot_5609_20255">
                            <InputTextBase
                                id="5609_20255"
                                class="Pixso-instance-5609_20255"
                                Type="Credit Card"
                                Size="lg"
                            />
                        </slot>
                    </div>
                </div>
                <slot name="slot_5609_20256" v-if="visible_5607_117">
                    <p
                        id="5609_20256"
                        class="Pixso-paragraph-5609_20256 fill-gray60-83_2722-paragraph text-text-smmedium-5454_21607"
                    >
                        {{ text_5607_123 ?? "This is an input helper text." }}
                    </p>
                </slot>
            </div>
            <div
                id="5609_20257"
                class="Pixso-symbol-5609_20257"
                v-if="
                    State === 'Disabled' &&
                    Type === 'Credit Card' &&
                    Size === 'lg'
                "
            >
                <div id="5609_20258" class="Pixso-frame-5609_20258">
                    <div class="frame-content-5609_20258">
                        <slot name="slot_5609_20259" v-if="visible_5607_114">
                            <p
                                id="5609_20259"
                                class="Pixso-paragraph-5609_20259 fill-gray80-32_4123-paragraph text-text-smbold-423_3208"
                            >
                                {{ text_5607_120 ?? "Label" }}
                            </p>
                        </slot>
                        <slot name="slot_5609_20260">
                            <InputTextBase
                                id="5609_20260"
                                class="Pixso-instance-5609_20260"
                                Type="Credit Card"
                                Size="lg"
                            />
                        </slot>
                    </div>
                </div>
                <slot name="slot_5609_20261" v-if="visible_5607_117">
                    <p
                        id="5609_20261"
                        class="Pixso-paragraph-5609_20261 fill-gray60-83_2722-paragraph text-text-smmedium-5454_21607"
                    >
                        {{ text_5607_123 ?? "This is an input helper text." }}
                    </p>
                </slot>
            </div>
            <div
                id="5609_20237"
                class="Pixso-symbol-5609_20237"
                v-if="
                    State === 'Error' && Type === 'Credit Card' && Size === 'lg'
                "
            >
                <div id="5609_20238" class="Pixso-frame-5609_20238">
                    <div class="frame-content-5609_20238">
                        <slot name="slot_5609_20239" v-if="visible_5607_114">
                            <p
                                id="5609_20239"
                                class="Pixso-paragraph-5609_20239 fill-gray80-32_4123-paragraph text-text-smbold-423_3208"
                            >
                                {{ text_5607_120 ?? "Label" }}
                            </p>
                        </slot>
                        <slot name="slot_5609_20240">
                            <InputTextBase
                                id="5609_20240"
                                class="Pixso-instance-5609_20240"
                                Type="Credit Card"
                                Size="lg"
                            />
                        </slot>
                    </div>
                </div>
                <slot name="slot_5609_20241" v-if="visible_5607_117">
                    <p
                        id="5609_20241"
                        class="Pixso-paragraph-5609_20241 fill-destructive50-423_3219-paragraph text-text-smmedium-5454_21607"
                    >
                        {{ text_5607_123 ?? "This is an input helper text." }}
                    </p>
                </slot>
            </div>
            <div
                id="5609_20496"
                class="Pixso-symbol-5609_20496"
                v-if="State === 'Default' && Type === 'Date' && Size === 'lg'"
            >
                <div id="5609_20497" class="Pixso-frame-5609_20497">
                    <div class="frame-content-5609_20497">
                        <slot name="slot_5609_20498" v-if="visible_5607_114">
                            <p
                                id="5609_20498"
                                class="Pixso-paragraph-5609_20498 fill-gray80-32_4123-paragraph text-text-smbold-423_3208"
                            >
                                {{ text_5607_120 ?? "Label" }}
                            </p>
                        </slot>
                        <slot name="slot_5609_20499">
                            <InputTextBase
                                id="5609_20499"
                                class="Pixso-instance-5609_20499"
                                Type="Date"
                                Size="lg"
                            />
                        </slot>
                    </div>
                </div>
                <slot name="slot_5609_20500" v-if="visible_5607_117">
                    <p
                        id="5609_20500"
                        class="Pixso-paragraph-5609_20500 fill-gray60-83_2722-paragraph text-text-smmedium-5454_21607"
                    >
                        {{ text_5607_123 ?? "This is an input helper text." }}
                    </p>
                </slot>
            </div>
            <div
                id="5609_20506"
                class="Pixso-symbol-5609_20506"
                v-if="State === 'Hover' && Type === 'Date' && Size === 'lg'"
            >
                <div id="5609_20507" class="Pixso-frame-5609_20507">
                    <div class="frame-content-5609_20507">
                        <slot name="slot_5609_20508" v-if="visible_5607_114">
                            <p
                                id="5609_20508"
                                class="Pixso-paragraph-5609_20508 fill-gray80-32_4123-paragraph text-text-smbold-423_3208"
                            >
                                {{ text_5607_120 ?? "Label" }}
                            </p>
                        </slot>
                        <slot name="slot_5609_20509">
                            <InputTextBase
                                id="5609_20509"
                                class="Pixso-instance-5609_20509"
                                Type="Date"
                                Size="lg"
                            />
                        </slot>
                    </div>
                </div>
                <slot name="slot_5609_20510" v-if="visible_5607_117">
                    <p
                        id="5609_20510"
                        class="Pixso-paragraph-5609_20510 fill-gray60-83_2722-paragraph text-text-smmedium-5454_21607"
                    >
                        {{ text_5607_123 ?? "This is an input helper text." }}
                    </p>
                </slot>
            </div>
            <div
                id="5609_20511"
                class="Pixso-symbol-5609_20511"
                v-if="State === 'Filled' && Type === 'Date' && Size === 'lg'"
            >
                <div id="5609_20512" class="Pixso-frame-5609_20512">
                    <div class="frame-content-5609_20512">
                        <slot name="slot_5609_20513" v-if="visible_5607_114">
                            <p
                                id="5609_20513"
                                class="Pixso-paragraph-5609_20513 fill-gray80-32_4123-paragraph text-text-smbold-423_3208"
                            >
                                {{ text_5607_120 ?? "Label" }}
                            </p>
                        </slot>
                        <slot name="slot_5609_20514">
                            <InputTextBase
                                id="5609_20514"
                                class="Pixso-instance-5609_20514"
                                Type="Date"
                                Size="lg"
                            />
                        </slot>
                    </div>
                </div>
                <slot name="slot_5609_20515" v-if="visible_5607_117">
                    <p
                        id="5609_20515"
                        class="Pixso-paragraph-5609_20515 fill-gray60-83_2722-paragraph text-text-smmedium-5454_21607"
                    >
                        {{ text_5607_123 ?? "This is an input helper text." }}
                    </p>
                </slot>
            </div>
            <div
                id="5609_20516"
                class="Pixso-symbol-5609_20516"
                v-if="State === 'Focused' && Type === 'Date' && Size === 'lg'"
            >
                <div id="5609_20517" class="Pixso-frame-5609_20517">
                    <div class="frame-content-5609_20517">
                        <slot name="slot_5609_20518" v-if="visible_5607_114">
                            <p
                                id="5609_20518"
                                class="Pixso-paragraph-5609_20518 fill-gray80-32_4123-paragraph text-text-smbold-423_3208"
                            >
                                {{ text_5607_120 ?? "Label" }}
                            </p>
                        </slot>
                        <slot name="slot_5609_20519">
                            <InputTextBase
                                id="5609_20519"
                                class="Pixso-instance-5609_20519"
                                Type="Date"
                                Size="lg"
                            />
                        </slot>
                    </div>
                </div>
                <slot name="slot_5609_20520" v-if="visible_5607_117">
                    <p
                        id="5609_20520"
                        class="Pixso-paragraph-5609_20520 fill-gray60-83_2722-paragraph text-text-smmedium-5454_21607"
                    >
                        {{ text_5607_123 ?? "This is an input helper text." }}
                    </p>
                </slot>
            </div>
            <div
                id="5609_20521"
                class="Pixso-symbol-5609_20521"
                v-if="State === 'Disabled' && Type === 'Date' && Size === 'lg'"
            >
                <div id="5609_20522" class="Pixso-frame-5609_20522">
                    <div class="frame-content-5609_20522">
                        <slot name="slot_5609_20523" v-if="visible_5607_114">
                            <p
                                id="5609_20523"
                                class="Pixso-paragraph-5609_20523 fill-gray80-32_4123-paragraph text-text-smbold-423_3208"
                            >
                                {{ text_5607_120 ?? "Label" }}
                            </p>
                        </slot>
                        <slot name="slot_5609_20524">
                            <InputTextBase
                                id="5609_20524"
                                class="Pixso-instance-5609_20524"
                                Type="Date"
                                Size="lg"
                            >
                                <template #slot_5607_19365>
                                    <CalendarBlank
                                        id="5607_19365"
                                        class="Pixso-instance-5607_19365"
                                        Format="Outline"
                                        Weight="Bold"
                                    />
                                </template>
                            </InputTextBase>
                        </slot>
                    </div>
                </div>
                <slot name="slot_5609_20525" v-if="visible_5607_117">
                    <p
                        id="5609_20525"
                        class="Pixso-paragraph-5609_20525 fill-gray60-83_2722-paragraph text-text-smmedium-5454_21607"
                    >
                        {{ text_5607_123 ?? "This is an input helper text." }}
                    </p>
                </slot>
            </div>
            <div
                id="5609_20501"
                class="Pixso-symbol-5609_20501"
                v-if="State === 'Error' && Type === 'Date' && Size === 'lg'"
            >
                <div id="5609_20502" class="Pixso-frame-5609_20502">
                    <div class="frame-content-5609_20502">
                        <slot name="slot_5609_20503" v-if="visible_5607_114">
                            <p
                                id="5609_20503"
                                class="Pixso-paragraph-5609_20503 fill-gray80-32_4123-paragraph text-text-smbold-423_3208"
                            >
                                {{ text_5607_120 ?? "Label" }}
                            </p>
                        </slot>
                        <slot name="slot_5609_20504">
                            <InputTextBase
                                id="5609_20504"
                                class="Pixso-instance-5609_20504"
                                Type="Date"
                                Size="lg"
                            />
                        </slot>
                    </div>
                </div>
                <slot name="slot_5609_20505" v-if="visible_5607_117">
                    <p
                        id="5609_20505"
                        class="Pixso-paragraph-5609_20505 fill-destructive50-423_3219-paragraph text-text-smmedium-5454_21607"
                    >
                        {{ text_5607_123 ?? "This is an input helper text." }}
                    </p>
                </slot>
            </div>
            <div
                id="5609_20658"
                class="Pixso-symbol-5609_20658"
                v-if="State === 'Default' && Type === 'Link' && Size === 'lg'"
            >
                <div id="5609_20659" class="Pixso-frame-5609_20659">
                    <div class="frame-content-5609_20659">
                        <slot name="slot_5609_20660" v-if="visible_5607_114">
                            <p
                                id="5609_20660"
                                class="Pixso-paragraph-5609_20660 fill-gray80-32_4123-paragraph text-text-smbold-423_3208"
                            >
                                {{ text_5607_120 ?? "Label" }}
                            </p>
                        </slot>
                        <slot name="slot_5609_20661">
                            <InputTextBase
                                id="5609_20661"
                                class="Pixso-instance-5609_20661"
                                Type="Link"
                                Size="lg"
                            />
                        </slot>
                    </div>
                </div>
                <slot name="slot_5609_20662" v-if="visible_5607_117">
                    <p
                        id="5609_20662"
                        class="Pixso-paragraph-5609_20662 fill-gray60-83_2722-paragraph text-text-smmedium-5454_21607"
                    >
                        {{ text_5607_123 ?? "This is an input helper text." }}
                    </p>
                </slot>
            </div>
            <div
                id="5609_20668"
                class="Pixso-symbol-5609_20668"
                v-if="State === 'Hover' && Type === 'Link' && Size === 'lg'"
            >
                <div id="5609_20669" class="Pixso-frame-5609_20669">
                    <div class="frame-content-5609_20669">
                        <slot name="slot_5609_20670" v-if="visible_5607_114">
                            <p
                                id="5609_20670"
                                class="Pixso-paragraph-5609_20670 fill-gray80-32_4123-paragraph text-text-smbold-423_3208"
                            >
                                {{ text_5607_120 ?? "Label" }}
                            </p>
                        </slot>
                        <slot name="slot_5609_20671">
                            <InputTextBase
                                id="5609_20671"
                                class="Pixso-instance-5609_20671"
                                Type="Link"
                                Size="lg"
                            />
                        </slot>
                    </div>
                </div>
                <slot name="slot_5609_20672" v-if="visible_5607_117">
                    <p
                        id="5609_20672"
                        class="Pixso-paragraph-5609_20672 fill-gray60-83_2722-paragraph text-text-smmedium-5454_21607"
                    >
                        {{ text_5607_123 ?? "This is an input helper text." }}
                    </p>
                </slot>
            </div>
            <div
                id="5609_20673"
                class="Pixso-symbol-5609_20673"
                v-if="State === 'Filled' && Type === 'Link' && Size === 'lg'"
            >
                <div id="5609_20674" class="Pixso-frame-5609_20674">
                    <div class="frame-content-5609_20674">
                        <slot name="slot_5609_20675" v-if="visible_5607_114">
                            <p
                                id="5609_20675"
                                class="Pixso-paragraph-5609_20675 fill-gray80-32_4123-paragraph text-text-smbold-423_3208"
                            >
                                {{ text_5607_120 ?? "Label" }}
                            </p>
                        </slot>
                        <slot name="slot_5609_20676">
                            <InputTextBase
                                id="5609_20676"
                                class="Pixso-instance-5609_20676"
                                Type="Link"
                                Size="lg"
                            />
                        </slot>
                    </div>
                </div>
                <slot name="slot_5609_20677" v-if="visible_5607_117">
                    <p
                        id="5609_20677"
                        class="Pixso-paragraph-5609_20677 fill-gray60-83_2722-paragraph text-text-smmedium-5454_21607"
                    >
                        {{ text_5607_123 ?? "This is an input helper text." }}
                    </p>
                </slot>
            </div>
            <div
                id="5609_20678"
                class="Pixso-symbol-5609_20678"
                v-if="State === 'Focused' && Type === 'Link' && Size === 'lg'"
            >
                <div id="5609_20679" class="Pixso-frame-5609_20679">
                    <div class="frame-content-5609_20679">
                        <slot name="slot_5609_20680" v-if="visible_5607_114">
                            <p
                                id="5609_20680"
                                class="Pixso-paragraph-5609_20680 fill-gray80-32_4123-paragraph text-text-smbold-423_3208"
                            >
                                {{ text_5607_120 ?? "Label" }}
                            </p>
                        </slot>
                        <slot name="slot_5609_20681">
                            <InputTextBase
                                id="5609_20681"
                                class="Pixso-instance-5609_20681"
                                Type="Link"
                                Size="lg"
                            />
                        </slot>
                    </div>
                </div>
                <slot name="slot_5609_20682" v-if="visible_5607_117">
                    <p
                        id="5609_20682"
                        class="Pixso-paragraph-5609_20682 fill-gray60-83_2722-paragraph text-text-smmedium-5454_21607"
                    >
                        {{ text_5607_123 ?? "This is an input helper text." }}
                    </p>
                </slot>
            </div>
            <div
                id="5609_20683"
                class="Pixso-symbol-5609_20683"
                v-if="State === 'Disabled' && Type === 'Link' && Size === 'lg'"
            >
                <div id="5609_20684" class="Pixso-frame-5609_20684">
                    <div class="frame-content-5609_20684">
                        <slot name="slot_5609_20685" v-if="visible_5607_114">
                            <p
                                id="5609_20685"
                                class="Pixso-paragraph-5609_20685 fill-gray80-32_4123-paragraph text-text-smbold-423_3208"
                            >
                                {{ text_5607_120 ?? "Label" }}
                            </p>
                        </slot>
                        <slot name="slot_5609_20686">
                            <InputTextBase
                                id="5609_20686"
                                class="Pixso-instance-5609_20686"
                                Type="Link"
                                Size="lg"
                            />
                        </slot>
                    </div>
                </div>
                <slot name="slot_5609_20687" v-if="visible_5607_117">
                    <p
                        id="5609_20687"
                        class="Pixso-paragraph-5609_20687 fill-gray60-83_2722-paragraph text-text-smmedium-5454_21607"
                    >
                        {{ text_5607_123 ?? "This is an input helper text." }}
                    </p>
                </slot>
            </div>
            <div
                id="5609_20663"
                class="Pixso-symbol-5609_20663"
                v-if="State === 'Error' && Type === 'Link' && Size === 'lg'"
            >
                <div id="5609_20664" class="Pixso-frame-5609_20664">
                    <div class="frame-content-5609_20664">
                        <slot name="slot_5609_20665" v-if="visible_5607_114">
                            <p
                                id="5609_20665"
                                class="Pixso-paragraph-5609_20665 fill-gray80-32_4123-paragraph text-text-smbold-423_3208"
                            >
                                {{ text_5607_120 ?? "Label" }}
                            </p>
                        </slot>
                        <slot name="slot_5609_20666">
                            <InputTextBase
                                id="5609_20666"
                                class="Pixso-instance-5609_20666"
                                Type="Link"
                                Size="lg"
                            />
                        </slot>
                    </div>
                </div>
                <slot name="slot_5609_20667" v-if="visible_5607_117">
                    <p
                        id="5609_20667"
                        class="Pixso-paragraph-5609_20667 fill-destructive50-423_3219-paragraph text-text-smmedium-5454_21607"
                    >
                        {{ text_5607_123 ?? "This is an input helper text." }}
                    </p>
                </slot>
            </div>
            <div
                id="5609_20808"
                class="Pixso-symbol-5609_20808"
                v-if="
                    State === 'Default' && Type === 'Password' && Size === 'lg'
                "
            >
                <div id="5609_20809" class="Pixso-frame-5609_20809">
                    <div class="frame-content-5609_20809">
                        <slot name="slot_5609_20810" v-if="visible_5607_114">
                            <p
                                id="5609_20810"
                                class="Pixso-paragraph-5609_20810 fill-gray80-32_4123-paragraph text-text-smbold-423_3208"
                            >
                                {{ text_5607_120 ?? "Label" }}
                            </p>
                        </slot>
                        <slot name="slot_5609_20811">
                            <InputTextBase
                                id="5609_20811"
                                class="Pixso-instance-5609_20811"
                                Type="Password"
                                Size="lg"
                            />
                        </slot>
                    </div>
                </div>
                <div
                    id="5612_2169"
                    class="Pixso-frame-5612_2169"
                    v-if="visible_5612_159"
                >
                    <div class="frame-content-5612_2169">
                        <slot name="slot_5612_2159">
                            <ProgressBarAtom
                                id="5612_2159"
                                class="Pixso-instance-5612_2159"
                                Size="sm"
                                Style="Fill"
                            />
                        </slot>
                        <slot name="slot_5612_2166">
                            <ProgressBarAtom
                                id="5612_2166"
                                class="Pixso-instance-5612_2166"
                                Size="sm"
                                Style="Fill"
                            />
                        </slot>
                        <slot name="slot_5612_2167">
                            <ProgressBarAtom
                                id="5612_2167"
                                class="Pixso-instance-5612_2167"
                                Size="sm"
                                Style="Fill"
                            />
                        </slot>
                        <slot name="slot_5612_2168">
                            <ProgressBarAtom
                                id="5612_2168"
                                class="Pixso-instance-5612_2168"
                                Size="sm"
                                Style="Fill"
                            />
                        </slot>
                    </div>
                </div>
                <slot name="slot_5609_20812" v-if="visible_5612_104">
                    <p
                        id="5609_20812"
                        class="Pixso-paragraph-5609_20812 fill-gray60-83_2722-paragraph text-text-smmedium-5454_21607"
                    >
                        {{ text_5612_49 ?? "This is a validation text." }}
                    </p>
                </slot>
            </div>
            <div
                id="5609_20818"
                class="Pixso-symbol-5609_20818"
                v-if="State === 'Hover' && Type === 'Password' && Size === 'lg'"
            >
                <div id="5609_20819" class="Pixso-frame-5609_20819">
                    <div class="frame-content-5609_20819">
                        <slot name="slot_5609_20820" v-if="visible_5607_114">
                            <p
                                id="5609_20820"
                                class="Pixso-paragraph-5609_20820 fill-gray80-32_4123-paragraph text-text-smbold-423_3208"
                            >
                                {{ text_5607_120 ?? "Label" }}
                            </p>
                        </slot>
                        <slot name="slot_5609_20821">
                            <InputTextBase
                                id="5609_20821"
                                class="Pixso-instance-5609_20821"
                                Type="Password"
                                Size="lg"
                            />
                        </slot>
                    </div>
                </div>
                <div
                    id="5612_2170"
                    class="Pixso-frame-5612_2170"
                    v-if="visible_5612_159"
                >
                    <div class="frame-content-5612_2170">
                        <slot name="slot_5612_2171">
                            <ProgressBarAtom
                                id="5612_2171"
                                class="Pixso-instance-5612_2171"
                                Size="sm"
                                Style="Fill"
                            />
                        </slot>
                        <slot name="slot_5612_2172">
                            <ProgressBarAtom
                                id="5612_2172"
                                class="Pixso-instance-5612_2172"
                                Size="sm"
                                Style="Fill"
                            />
                        </slot>
                        <slot name="slot_5612_2173">
                            <ProgressBarAtom
                                id="5612_2173"
                                class="Pixso-instance-5612_2173"
                                Size="sm"
                                Style="Fill"
                            />
                        </slot>
                        <slot name="slot_5612_2174">
                            <ProgressBarAtom
                                id="5612_2174"
                                class="Pixso-instance-5612_2174"
                                Size="sm"
                                Style="Fill"
                            />
                        </slot>
                    </div>
                </div>
                <slot name="slot_5609_20822" v-if="visible_5612_104">
                    <p
                        id="5609_20822"
                        class="Pixso-paragraph-5609_20822 fill-gray60-83_2722-paragraph text-text-smmedium-5454_21607"
                    >
                        {{ text_5612_49 ?? "This is a validation text." }}
                    </p>
                </slot>
            </div>
            <div
                id="5609_20823"
                class="Pixso-symbol-5609_20823"
                v-if="
                    State === 'Filled' && Type === 'Password' && Size === 'lg'
                "
            >
                <div id="5609_20824" class="Pixso-frame-5609_20824">
                    <div class="frame-content-5609_20824">
                        <slot name="slot_5609_20825" v-if="visible_5607_114">
                            <p
                                id="5609_20825"
                                class="Pixso-paragraph-5609_20825 fill-gray80-32_4123-paragraph text-text-smbold-423_3208"
                            >
                                {{ text_5607_120 ?? "Label" }}
                            </p>
                        </slot>
                        <slot name="slot_5609_20826">
                            <InputTextBase
                                id="5609_20826"
                                class="Pixso-instance-5609_20826"
                                Type="Password"
                                Size="lg"
                            />
                        </slot>
                    </div>
                </div>
                <div
                    id="5612_2175"
                    class="Pixso-frame-5612_2175"
                    v-if="visible_5612_159"
                >
                    <div class="frame-content-5612_2175">
                        <slot name="slot_5612_2176">
                            <ProgressBarAtom
                                id="5612_2176"
                                class="Pixso-instance-5612_2176"
                                Size="sm"
                                Style="Fill"
                            />
                        </slot>
                        <slot name="slot_5612_2177">
                            <ProgressBarAtom
                                id="5612_2177"
                                class="Pixso-instance-5612_2177"
                                Size="sm"
                                Style="Fill"
                            />
                        </slot>
                        <slot name="slot_5612_2178">
                            <ProgressBarAtom
                                id="5612_2178"
                                class="Pixso-instance-5612_2178"
                                Size="sm"
                                Style="Fill"
                            />
                        </slot>
                        <slot name="slot_5612_2179">
                            <ProgressBarAtom
                                id="5612_2179"
                                class="Pixso-instance-5612_2179"
                                Size="sm"
                                Style="Fill"
                            />
                        </slot>
                    </div>
                </div>
                <slot name="slot_5609_20827" v-if="visible_5612_104">
                    <p
                        id="5609_20827"
                        class="Pixso-paragraph-5609_20827 fill-gray60-83_2722-paragraph text-text-smmedium-5454_21607"
                    >
                        {{ text_5612_49 ?? "This is a validation text." }}
                    </p>
                </slot>
            </div>
            <div
                id="5609_20828"
                class="Pixso-symbol-5609_20828"
                v-if="
                    State === 'Focused' && Type === 'Password' && Size === 'lg'
                "
            >
                <div id="5609_20829" class="Pixso-frame-5609_20829">
                    <div class="frame-content-5609_20829">
                        <slot name="slot_5609_20830" v-if="visible_5607_114">
                            <p
                                id="5609_20830"
                                class="Pixso-paragraph-5609_20830 fill-gray80-32_4123-paragraph text-text-smbold-423_3208"
                            >
                                {{ text_5607_120 ?? "Label" }}
                            </p>
                        </slot>
                        <slot name="slot_5609_20831">
                            <InputTextBase
                                id="5609_20831"
                                class="Pixso-instance-5609_20831"
                                Type="Password"
                                Size="lg"
                            />
                        </slot>
                    </div>
                </div>
                <div
                    id="5612_2180"
                    class="Pixso-frame-5612_2180"
                    v-if="visible_5612_159"
                >
                    <div class="frame-content-5612_2180">
                        <slot name="slot_5612_2181">
                            <ProgressBarAtom
                                id="5612_2181"
                                class="Pixso-instance-5612_2181"
                                Size="sm"
                                Style="Fill"
                            />
                        </slot>
                        <slot name="slot_5612_2182">
                            <ProgressBarAtom
                                id="5612_2182"
                                class="Pixso-instance-5612_2182"
                                Size="sm"
                                Style="Fill"
                            />
                        </slot>
                        <slot name="slot_5612_2183">
                            <ProgressBarAtom
                                id="5612_2183"
                                class="Pixso-instance-5612_2183"
                                Size="sm"
                                Style="Fill"
                            />
                        </slot>
                        <slot name="slot_5612_2184">
                            <ProgressBarAtom
                                id="5612_2184"
                                class="Pixso-instance-5612_2184"
                                Size="sm"
                                Style="Fill"
                            />
                        </slot>
                    </div>
                </div>
                <slot name="slot_5609_20832" v-if="visible_5612_104">
                    <p
                        id="5609_20832"
                        class="Pixso-paragraph-5609_20832 fill-gray60-83_2722-paragraph text-text-smmedium-5454_21607"
                    >
                        {{ text_5612_49 ?? "This is a validation text." }}
                    </p>
                </slot>
            </div>
            <div
                id="5609_20833"
                class="Pixso-symbol-5609_20833"
                v-if="
                    State === 'Disabled' && Type === 'Password' && Size === 'lg'
                "
            >
                <div id="5609_20834" class="Pixso-frame-5609_20834">
                    <div class="frame-content-5609_20834">
                        <slot name="slot_5609_20835" v-if="visible_5607_114">
                            <p
                                id="5609_20835"
                                class="Pixso-paragraph-5609_20835 fill-gray80-32_4123-paragraph text-text-smbold-423_3208"
                            >
                                {{ text_5607_120 ?? "Label" }}
                            </p>
                        </slot>
                        <slot name="slot_5609_20836">
                            <InputTextBase
                                id="5609_20836"
                                class="Pixso-instance-5609_20836"
                                Type="Password"
                                Size="lg"
                            >
                                <template #slot_5607_19417>
                                    <LockSimple
                                        id="5607_19417"
                                        class="Pixso-instance-5607_19417"
                                        Format="Outline"
                                        Weight="Bold"
                                    />
                                </template>
                            </InputTextBase>
                        </slot>
                    </div>
                </div>
                <div
                    id="5612_2185"
                    class="Pixso-frame-5612_2185"
                    v-if="visible_5612_159"
                >
                    <div class="frame-content-5612_2185">
                        <slot name="slot_5612_2186">
                            <ProgressBarAtom
                                id="5612_2186"
                                class="Pixso-instance-5612_2186"
                                Size="sm"
                                Style="Fill"
                            />
                        </slot>
                        <slot name="slot_5612_2187">
                            <ProgressBarAtom
                                id="5612_2187"
                                class="Pixso-instance-5612_2187"
                                Size="sm"
                                Style="Fill"
                            />
                        </slot>
                        <slot name="slot_5612_2188">
                            <ProgressBarAtom
                                id="5612_2188"
                                class="Pixso-instance-5612_2188"
                                Size="sm"
                                Style="Fill"
                            />
                        </slot>
                        <slot name="slot_5612_2189">
                            <ProgressBarAtom
                                id="5612_2189"
                                class="Pixso-instance-5612_2189"
                                Size="sm"
                                Style="Fill"
                            />
                        </slot>
                    </div>
                </div>
                <slot name="slot_5609_20837" v-if="visible_5612_104">
                    <p
                        id="5609_20837"
                        class="Pixso-paragraph-5609_20837 fill-gray60-83_2722-paragraph text-text-smmedium-5454_21607"
                    >
                        {{ text_5612_49 ?? "This is a validation text." }}
                    </p>
                </slot>
            </div>
            <div
                id="5609_20813"
                class="Pixso-symbol-5609_20813"
                v-if="State === 'Error' && Type === 'Password' && Size === 'lg'"
            >
                <div id="5609_20814" class="Pixso-frame-5609_20814">
                    <div class="frame-content-5609_20814">
                        <slot name="slot_5609_20815" v-if="visible_5607_114">
                            <p
                                id="5609_20815"
                                class="Pixso-paragraph-5609_20815 fill-gray80-32_4123-paragraph text-text-smbold-423_3208"
                            >
                                {{ text_5607_120 ?? "Label" }}
                            </p>
                        </slot>
                        <slot name="slot_5609_20816">
                            <InputTextBase
                                id="5609_20816"
                                class="Pixso-instance-5609_20816"
                                Type="Password"
                                Size="lg"
                            />
                        </slot>
                    </div>
                </div>
                <div
                    id="5612_2190"
                    class="Pixso-frame-5612_2190"
                    v-if="visible_5612_159"
                >
                    <div class="frame-content-5612_2190">
                        <slot name="slot_5612_2191">
                            <ProgressBarAtom
                                id="5612_2191"
                                class="Pixso-instance-5612_2191"
                                Size="sm"
                                Style="Fill"
                            />
                        </slot>
                        <slot name="slot_5612_2192">
                            <ProgressBarAtom
                                id="5612_2192"
                                class="Pixso-instance-5612_2192"
                                Size="sm"
                                Style="Fill"
                            />
                        </slot>
                        <slot name="slot_5612_2193">
                            <ProgressBarAtom
                                id="5612_2193"
                                class="Pixso-instance-5612_2193"
                                Size="sm"
                                Style="Fill"
                            />
                        </slot>
                        <slot name="slot_5612_2194">
                            <ProgressBarAtom
                                id="5612_2194"
                                class="Pixso-instance-5612_2194"
                                Size="sm"
                                Style="Fill"
                            />
                        </slot>
                    </div>
                </div>
                <slot name="slot_5609_20817" v-if="visible_5612_104">
                    <p
                        id="5609_20817"
                        class="Pixso-paragraph-5609_20817 fill-destructive50-423_3219-paragraph text-text-smmedium-5454_21607"
                    >
                        {{ text_5612_49 ?? "This is a validation text." }}
                    </p>
                </slot>
            </div>
            <div
                id="5609_21048"
                class="Pixso-symbol-5609_21048"
                v-if="
                    State === 'Default' &&
                    Type === 'Phone Number/Country' &&
                    Size === 'lg'
                "
            >
                <div id="5609_21049" class="Pixso-frame-5609_21049">
                    <div class="frame-content-5609_21049">
                        <slot name="slot_5609_21050" v-if="visible_5607_114">
                            <p
                                id="5609_21050"
                                class="Pixso-paragraph-5609_21050 fill-gray80-32_4123-paragraph text-text-smbold-423_3208"
                            >
                                {{ text_5607_120 ?? "Label" }}
                            </p>
                        </slot>
                        <slot name="slot_5609_21051">
                            <InputTextBase
                                id="5609_21051"
                                class="Pixso-instance-5609_21051"
                                Type="Phone Number/Country"
                                Size="lg"
                            />
                        </slot>
                    </div>
                </div>
                <slot name="slot_5609_21052" v-if="visible_5607_117">
                    <p
                        id="5609_21052"
                        class="Pixso-paragraph-5609_21052 fill-gray60-83_2722-paragraph text-text-smmedium-5454_21607"
                    >
                        {{ text_5607_123 ?? "This is an input helper text." }}
                    </p>
                </slot>
            </div>
            <div
                id="5609_21058"
                class="Pixso-symbol-5609_21058"
                v-if="
                    State === 'Hover' &&
                    Type === 'Phone Number/Country' &&
                    Size === 'lg'
                "
            >
                <div id="5609_21059" class="Pixso-frame-5609_21059">
                    <div class="frame-content-5609_21059">
                        <slot name="slot_5609_21060" v-if="visible_5607_114">
                            <p
                                id="5609_21060"
                                class="Pixso-paragraph-5609_21060 fill-gray80-32_4123-paragraph text-text-smbold-423_3208"
                            >
                                {{ text_5607_120 ?? "Label" }}
                            </p>
                        </slot>
                        <slot name="slot_5609_21061">
                            <InputTextBase
                                id="5609_21061"
                                class="Pixso-instance-5609_21061"
                                Type="Phone Number/Country"
                                Size="lg"
                            />
                        </slot>
                    </div>
                </div>
                <slot name="slot_5609_21062" v-if="visible_5607_117">
                    <p
                        id="5609_21062"
                        class="Pixso-paragraph-5609_21062 fill-gray60-83_2722-paragraph text-text-smmedium-5454_21607"
                    >
                        {{ text_5607_123 ?? "This is an input helper text." }}
                    </p>
                </slot>
            </div>
            <div
                id="5609_21063"
                class="Pixso-symbol-5609_21063"
                v-if="
                    State === 'Filled' &&
                    Type === 'Phone Number/Country' &&
                    Size === 'lg'
                "
            >
                <div id="5609_21064" class="Pixso-frame-5609_21064">
                    <div class="frame-content-5609_21064">
                        <slot name="slot_5609_21065" v-if="visible_5607_114">
                            <p
                                id="5609_21065"
                                class="Pixso-paragraph-5609_21065 fill-gray80-32_4123-paragraph text-text-smbold-423_3208"
                            >
                                {{ text_5607_120 ?? "Label" }}
                            </p>
                        </slot>
                        <slot name="slot_5609_21066">
                            <InputTextBase
                                id="5609_21066"
                                class="Pixso-instance-5609_21066"
                                Type="Phone Number/Country"
                                Size="lg"
                            />
                        </slot>
                    </div>
                </div>
                <slot name="slot_5609_21067" v-if="visible_5607_117">
                    <p
                        id="5609_21067"
                        class="Pixso-paragraph-5609_21067 fill-gray60-83_2722-paragraph text-text-smmedium-5454_21607"
                    >
                        {{ text_5607_123 ?? "This is an input helper text." }}
                    </p>
                </slot>
            </div>
            <div
                id="5609_21068"
                class="Pixso-symbol-5609_21068"
                v-if="
                    State === 'Focused' &&
                    Type === 'Phone Number/Country' &&
                    Size === 'lg'
                "
            >
                <div id="5609_21069" class="Pixso-frame-5609_21069">
                    <div class="frame-content-5609_21069">
                        <slot name="slot_5609_21070" v-if="visible_5607_114">
                            <p
                                id="5609_21070"
                                class="Pixso-paragraph-5609_21070 fill-gray80-32_4123-paragraph text-text-smbold-423_3208"
                            >
                                {{ text_5607_120 ?? "Label" }}
                            </p>
                        </slot>
                        <slot name="slot_5609_21071">
                            <InputTextBase
                                id="5609_21071"
                                class="Pixso-instance-5609_21071"
                                Type="Phone Number/Country"
                                Size="lg"
                            />
                        </slot>
                    </div>
                </div>
                <slot name="slot_5609_21072" v-if="visible_5607_117">
                    <p
                        id="5609_21072"
                        class="Pixso-paragraph-5609_21072 fill-gray60-83_2722-paragraph text-text-smmedium-5454_21607"
                    >
                        {{ text_5607_123 ?? "This is an input helper text." }}
                    </p>
                </slot>
            </div>
            <div
                id="5609_21073"
                class="Pixso-symbol-5609_21073"
                v-if="
                    State === 'Disabled' &&
                    Type === 'Phone Number/Country' &&
                    Size === 'lg'
                "
            >
                <div id="5609_21074" class="Pixso-frame-5609_21074">
                    <div class="frame-content-5609_21074">
                        <slot name="slot_5609_21075" v-if="visible_5607_114">
                            <p
                                id="5609_21075"
                                class="Pixso-paragraph-5609_21075 fill-gray80-32_4123-paragraph text-text-smbold-423_3208"
                            >
                                {{ text_5607_120 ?? "Label" }}
                            </p>
                        </slot>
                        <slot name="slot_5609_21076">
                            <InputTextBase
                                id="5609_21076"
                                class="Pixso-instance-5609_21076"
                                Type="Phone Number/Country"
                                Size="lg"
                            />
                        </slot>
                    </div>
                </div>
                <slot name="slot_5609_21077" v-if="visible_5607_117">
                    <p
                        id="5609_21077"
                        class="Pixso-paragraph-5609_21077 fill-gray60-83_2722-paragraph text-text-smmedium-5454_21607"
                    >
                        {{ text_5607_123 ?? "This is an input helper text." }}
                    </p>
                </slot>
            </div>
            <div
                id="5609_21053"
                class="Pixso-symbol-5609_21053"
                v-if="
                    State === 'Error' &&
                    Type === 'Phone Number/Country' &&
                    Size === 'lg'
                "
            >
                <div id="5609_21054" class="Pixso-frame-5609_21054">
                    <div class="frame-content-5609_21054">
                        <slot name="slot_5609_21055" v-if="visible_5607_114">
                            <p
                                id="5609_21055"
                                class="Pixso-paragraph-5609_21055 fill-gray80-32_4123-paragraph text-text-smbold-423_3208"
                            >
                                {{ text_5607_120 ?? "Label" }}
                            </p>
                        </slot>
                        <slot name="slot_5609_21056">
                            <InputTextBase
                                id="5609_21056"
                                class="Pixso-instance-5609_21056"
                                Type="Phone Number/Country"
                                Size="lg"
                            />
                        </slot>
                    </div>
                </div>
                <slot name="slot_5609_21057" v-if="visible_5607_117">
                    <p
                        id="5609_21057"
                        class="Pixso-paragraph-5609_21057 fill-destructive50-423_3219-paragraph text-text-smmedium-5454_21607"
                    >
                        {{ text_5607_123 ?? "This is an input helper text." }}
                    </p>
                </slot>
            </div>
            <div
                id="5609_22109"
                class="Pixso-symbol-5609_22109"
                v-if="State === 'Default' && Type === 'Number' && Size === 'lg'"
            >
                <div id="5609_22110" class="Pixso-frame-5609_22110">
                    <div class="frame-content-5609_22110">
                        <slot name="slot_5609_22111" v-if="visible_5607_114">
                            <p
                                id="5609_22111"
                                class="Pixso-paragraph-5609_22111 fill-gray80-32_4123-paragraph text-text-smbold-423_3208"
                            >
                                {{ text_5607_120 ?? "Label" }}
                            </p>
                        </slot>
                        <slot name="slot_5609_22112">
                            <InputTextBase
                                id="5609_22112"
                                class="Pixso-instance-5609_22112"
                                Type="Number"
                                Size="lg"
                            />
                        </slot>
                    </div>
                </div>
                <slot name="slot_5609_22113" v-if="visible_5607_117">
                    <p
                        id="5609_22113"
                        class="Pixso-paragraph-5609_22113 fill-gray60-83_2722-paragraph text-text-smmedium-5454_21607"
                    >
                        {{ text_5607_123 ?? "This is an input helper text." }}
                    </p>
                </slot>
            </div>
            <div
                id="5609_22114"
                class="Pixso-symbol-5609_22114"
                v-if="State === 'Hover' && Type === 'Number' && Size === 'lg'"
            >
                <div id="5609_22115" class="Pixso-frame-5609_22115">
                    <div class="frame-content-5609_22115">
                        <slot name="slot_5609_22116" v-if="visible_5607_114">
                            <p
                                id="5609_22116"
                                class="Pixso-paragraph-5609_22116 fill-gray80-32_4123-paragraph text-text-smbold-423_3208"
                            >
                                {{ text_5607_120 ?? "Label" }}
                            </p>
                        </slot>
                        <slot name="slot_5609_22117">
                            <InputTextBase
                                id="5609_22117"
                                class="Pixso-instance-5609_22117"
                                Type="Number"
                                Size="lg"
                            />
                        </slot>
                    </div>
                </div>
                <slot name="slot_5609_22118" v-if="visible_5607_117">
                    <p
                        id="5609_22118"
                        class="Pixso-paragraph-5609_22118 fill-gray60-83_2722-paragraph text-text-smmedium-5454_21607"
                    >
                        {{ text_5607_123 ?? "This is an input helper text." }}
                    </p>
                </slot>
            </div>
            <div
                id="5609_22119"
                class="Pixso-symbol-5609_22119"
                v-if="State === 'Filled' && Type === 'Number' && Size === 'lg'"
            >
                <div id="5609_22120" class="Pixso-frame-5609_22120">
                    <div class="frame-content-5609_22120">
                        <slot name="slot_5609_22121" v-if="visible_5607_114">
                            <p
                                id="5609_22121"
                                class="Pixso-paragraph-5609_22121 fill-gray80-32_4123-paragraph text-text-smbold-423_3208"
                            >
                                {{ text_5607_120 ?? "Label" }}
                            </p>
                        </slot>
                        <slot name="slot_5609_22122">
                            <InputTextBase
                                id="5609_22122"
                                class="Pixso-instance-5609_22122"
                                Type="Number"
                                Size="lg"
                            />
                        </slot>
                    </div>
                </div>
                <slot name="slot_5609_22123" v-if="visible_5607_117">
                    <p
                        id="5609_22123"
                        class="Pixso-paragraph-5609_22123 fill-gray60-83_2722-paragraph text-text-smmedium-5454_21607"
                    >
                        {{ text_5607_123 ?? "This is an input helper text." }}
                    </p>
                </slot>
            </div>
            <div
                id="5609_22124"
                class="Pixso-symbol-5609_22124"
                v-if="State === 'Focused' && Type === 'Number' && Size === 'lg'"
            >
                <div id="5609_22125" class="Pixso-frame-5609_22125">
                    <div class="frame-content-5609_22125">
                        <slot name="slot_5609_22126" v-if="visible_5607_114">
                            <p
                                id="5609_22126"
                                class="Pixso-paragraph-5609_22126 fill-gray80-32_4123-paragraph text-text-smbold-423_3208"
                            >
                                {{ text_5607_120 ?? "Label" }}
                            </p>
                        </slot>
                        <slot name="slot_5609_22127">
                            <InputTextBase
                                id="5609_22127"
                                class="Pixso-instance-5609_22127"
                                Type="Number"
                                Size="lg"
                            />
                        </slot>
                    </div>
                </div>
                <slot name="slot_5609_22128" v-if="visible_5607_117">
                    <p
                        id="5609_22128"
                        class="Pixso-paragraph-5609_22128 fill-gray60-83_2722-paragraph text-text-smmedium-5454_21607"
                    >
                        {{ text_5607_123 ?? "This is an input helper text." }}
                    </p>
                </slot>
            </div>
            <div
                id="5609_22129"
                class="Pixso-symbol-5609_22129"
                v-if="
                    State === 'Disabled' && Type === 'Number' && Size === 'lg'
                "
            >
                <div id="5609_22130" class="Pixso-frame-5609_22130">
                    <div class="frame-content-5609_22130">
                        <slot name="slot_5609_22131" v-if="visible_5607_114">
                            <p
                                id="5609_22131"
                                class="Pixso-paragraph-5609_22131 fill-gray80-32_4123-paragraph text-text-smbold-423_3208"
                            >
                                {{ text_5607_120 ?? "Label" }}
                            </p>
                        </slot>
                        <slot name="slot_5609_22132">
                            <InputTextBase
                                id="5609_22132"
                                class="Pixso-instance-5609_22132"
                                Type="Number"
                                Size="lg"
                            />
                        </slot>
                    </div>
                </div>
                <slot name="slot_5609_22133" v-if="visible_5607_117">
                    <p
                        id="5609_22133"
                        class="Pixso-paragraph-5609_22133 fill-gray60-83_2722-paragraph text-text-smmedium-5454_21607"
                    >
                        {{ text_5607_123 ?? "This is an input helper text." }}
                    </p>
                </slot>
            </div>
            <div
                id="5609_22134"
                class="Pixso-symbol-5609_22134"
                v-if="State === 'Error' && Type === 'Number' && Size === 'lg'"
            >
                <div id="5609_22135" class="Pixso-frame-5609_22135">
                    <div class="frame-content-5609_22135">
                        <slot name="slot_5609_22136" v-if="visible_5607_114">
                            <p
                                id="5609_22136"
                                class="Pixso-paragraph-5609_22136 fill-gray80-32_4123-paragraph text-text-smbold-423_3208"
                            >
                                {{ text_5607_120 ?? "Label" }}
                            </p>
                        </slot>
                        <slot name="slot_5609_22137">
                            <InputTextBase
                                id="5609_22137"
                                class="Pixso-instance-5609_22137"
                                Type="Number"
                                Size="lg"
                            />
                        </slot>
                    </div>
                </div>
                <slot name="slot_5609_22138" v-if="visible_5607_117">
                    <p
                        id="5609_22138"
                        class="Pixso-paragraph-5609_22138 fill-destructive50-423_3219-paragraph text-text-smmedium-5454_21607"
                    >
                        {{ text_5607_123 ?? "This is an input helper text." }}
                    </p>
                </slot>
            </div>
            <div
                id="5976_53791"
                class="Pixso-symbol-5976_53791"
                v-if="
                    State === 'Default' && Type === 'Default' && Size === 'md'
                "
            >
                <div id="5976_53792" class="Pixso-frame-5976_53792">
                    <div class="frame-content-5976_53792">
                        <slot name="slot_5976_53793" v-if="visible_5607_114">
                            <p
                                id="5976_53793"
                                class="Pixso-paragraph-5976_53793 fill-gray80-32_4123-paragraph text-text-smbold-423_3208"
                            >
                                {{ text_5607_120 ?? "Label" }}
                            </p>
                        </slot>
                        <slot name="slot_5976_53794">
                            <InputTextBase
                                id="5976_53794"
                                class="Pixso-instance-5976_53794"
                                Type="Default"
                                Size="md"
                            />
                        </slot>
                    </div>
                </div>
                <slot name="slot_5976_53795" v-if="visible_5607_117">
                    <p
                        id="5976_53795"
                        class="Pixso-paragraph-5976_53795 fill-gray60-83_2722-paragraph text-text-smmedium-5454_21607"
                    >
                        {{ text_5607_123 ?? "This is an input helper text." }}
                    </p>
                </slot>
            </div>
            <div
                id="5976_53796"
                class="Pixso-symbol-5976_53796"
                v-if="State === 'Hover' && Type === 'Default' && Size === 'md'"
            >
                <div id="5976_53797" class="Pixso-frame-5976_53797">
                    <div class="frame-content-5976_53797">
                        <slot name="slot_5976_53798" v-if="visible_5607_114">
                            <p
                                id="5976_53798"
                                class="Pixso-paragraph-5976_53798 fill-gray80-32_4123-paragraph text-text-smbold-423_3208"
                            >
                                {{ text_5607_120 ?? "Label" }}
                            </p>
                        </slot>
                        <slot name="slot_5976_53799">
                            <InputTextBase
                                id="5976_53799"
                                class="Pixso-instance-5976_53799"
                                Type="Default"
                                Size="md"
                            />
                        </slot>
                    </div>
                </div>
                <slot name="slot_5976_53800" v-if="visible_5607_117">
                    <p
                        id="5976_53800"
                        class="Pixso-paragraph-5976_53800 fill-gray60-83_2722-paragraph text-text-smmedium-5454_21607"
                    >
                        {{ text_5607_123 ?? "This is an input helper text." }}
                    </p>
                </slot>
            </div>
            <div
                id="5976_53801"
                class="Pixso-symbol-5976_53801"
                v-if="State === 'Filled' && Type === 'Default' && Size === 'md'"
            >
                <div id="5976_53802" class="Pixso-frame-5976_53802">
                    <div class="frame-content-5976_53802">
                        <slot name="slot_5976_53803" v-if="visible_5607_114">
                            <p
                                id="5976_53803"
                                class="Pixso-paragraph-5976_53803 fill-gray80-32_4123-paragraph text-text-smbold-423_3208"
                            >
                                {{ text_5607_120 ?? "Label" }}
                            </p>
                        </slot>
                        <slot name="slot_5976_53804">
                            <InputTextBase
                                id="5976_53804"
                                class="Pixso-instance-5976_53804"
                                Type="Default"
                                Size="md"
                            />
                        </slot>
                    </div>
                </div>
                <slot name="slot_5976_53805" v-if="visible_5607_117">
                    <p
                        id="5976_53805"
                        class="Pixso-paragraph-5976_53805 fill-gray60-83_2722-paragraph text-text-smmedium-5454_21607"
                    >
                        {{ text_5607_123 ?? "This is an input helper text." }}
                    </p>
                </slot>
            </div>
            <div
                id="5976_53806"
                class="Pixso-symbol-5976_53806"
                v-if="
                    State === 'Focused' && Type === 'Default' && Size === 'md'
                "
            >
                <div id="5976_53807" class="Pixso-frame-5976_53807">
                    <div class="frame-content-5976_53807">
                        <slot name="slot_5976_53808" v-if="visible_5607_114">
                            <p
                                id="5976_53808"
                                class="Pixso-paragraph-5976_53808 fill-gray80-32_4123-paragraph text-text-smbold-423_3208"
                            >
                                {{ text_5607_120 ?? "Label" }}
                            </p>
                        </slot>
                        <slot name="slot_5976_53809">
                            <InputTextBase
                                id="5976_53809"
                                class="Pixso-instance-5976_53809"
                                Type="Default"
                                Size="md"
                            />
                        </slot>
                    </div>
                </div>
                <slot name="slot_5976_53810" v-if="visible_5607_117">
                    <p
                        id="5976_53810"
                        class="Pixso-paragraph-5976_53810 fill-gray60-83_2722-paragraph text-text-smmedium-5454_21607"
                    >
                        {{ text_5607_123 ?? "This is an input helper text." }}
                    </p>
                </slot>
            </div>
            <div
                id="5976_53811"
                class="Pixso-symbol-5976_53811"
                v-if="
                    State === 'Disabled' && Type === 'Default' && Size === 'md'
                "
            >
                <div id="5976_53812" class="Pixso-frame-5976_53812">
                    <div class="frame-content-5976_53812">
                        <slot name="slot_5976_53813" v-if="visible_5607_114">
                            <p
                                id="5976_53813"
                                class="Pixso-paragraph-5976_53813 fill-gray80-32_4123-paragraph text-text-smbold-423_3208"
                            >
                                {{ text_5607_120 ?? "Label" }}
                            </p>
                        </slot>
                        <slot name="slot_5976_53814">
                            <InputTextBase
                                id="5976_53814"
                                class="Pixso-instance-5976_53814"
                                Type="Default"
                                Size="md"
                            >
                                <template #slot_5976_52049>
                                    <User
                                        id="5976_52049"
                                        class="Pixso-instance-5976_52049"
                                        Format="Outline"
                                        Weight="Bold"
                                    />
                                </template>
                                <template #slot_5976_52051>
                                    <Question
                                        id="5976_52051"
                                        class="Pixso-instance-5976_52051"
                                        Format="Outline"
                                        Weight="Bold"
                                    />
                                </template>
                            </InputTextBase>
                        </slot>
                    </div>
                </div>
                <slot name="slot_5976_53815" v-if="visible_5607_117">
                    <p
                        id="5976_53815"
                        class="Pixso-paragraph-5976_53815 fill-gray60-83_2722-paragraph text-text-smmedium-5454_21607"
                    >
                        {{ text_5607_123 ?? "This is an input helper text." }}
                    </p>
                </slot>
            </div>
            <div
                id="5976_53816"
                class="Pixso-symbol-5976_53816"
                v-if="State === 'Error' && Type === 'Default' && Size === 'md'"
            >
                <div id="5976_53817" class="Pixso-frame-5976_53817">
                    <div class="frame-content-5976_53817">
                        <slot name="slot_5976_53818" v-if="visible_5607_114">
                            <p
                                id="5976_53818"
                                class="Pixso-paragraph-5976_53818 fill-gray80-32_4123-paragraph text-text-smbold-423_3208"
                            >
                                {{ text_5607_120 ?? "Label" }}
                            </p>
                        </slot>
                        <slot name="slot_5976_53819">
                            <InputTextBase
                                id="5976_53819"
                                class="Pixso-instance-5976_53819"
                                Type="Default"
                                Size="md"
                            />
                        </slot>
                    </div>
                </div>
                <slot name="slot_5976_53820" v-if="visible_5607_117">
                    <p
                        id="5976_53820"
                        class="Pixso-paragraph-5976_53820 fill-destructive50-423_3219-paragraph text-text-smmedium-5454_21607"
                    >
                        {{ text_5607_123 ?? "This is an input helper text." }}
                    </p>
                </slot>
            </div>
            <div
                id="5976_53821"
                class="Pixso-symbol-5976_53821"
                v-if="State === 'Default' && Type === 'Action' && Size === 'md'"
            >
                <div id="5976_53822" class="Pixso-frame-5976_53822">
                    <div class="frame-content-5976_53822">
                        <slot name="slot_5976_53823" v-if="visible_5607_114">
                            <p
                                id="5976_53823"
                                class="Pixso-paragraph-5976_53823 fill-gray80-32_4123-paragraph text-text-smbold-423_3208"
                            >
                                {{ text_5607_120 ?? "Label" }}
                            </p>
                        </slot>
                        <slot name="slot_5976_53824">
                            <InputTextBase
                                id="5976_53824"
                                class="Pixso-instance-5976_53824"
                                Type="Action"
                                Size="md"
                            />
                        </slot>
                    </div>
                </div>
                <slot name="slot_5976_53825" v-if="visible_5607_117">
                    <p
                        id="5976_53825"
                        class="Pixso-paragraph-5976_53825 fill-gray60-83_2722-paragraph text-text-smmedium-5454_21607"
                    >
                        {{ text_5607_123 ?? "This is an input helper text." }}
                    </p>
                </slot>
            </div>
            <div
                id="5976_53826"
                class="Pixso-symbol-5976_53826"
                v-if="State === 'Hover' && Type === 'Action' && Size === 'md'"
            >
                <div id="5976_53827" class="Pixso-frame-5976_53827">
                    <div class="frame-content-5976_53827">
                        <slot name="slot_5976_53828" v-if="visible_5607_114">
                            <p
                                id="5976_53828"
                                class="Pixso-paragraph-5976_53828 fill-gray80-32_4123-paragraph text-text-smbold-423_3208"
                            >
                                {{ text_5607_120 ?? "Label" }}
                            </p>
                        </slot>
                        <slot name="slot_5976_53829">
                            <InputTextBase
                                id="5976_53829"
                                class="Pixso-instance-5976_53829"
                                Type="Action"
                                Size="md"
                            />
                        </slot>
                    </div>
                </div>
                <slot name="slot_5976_53830" v-if="visible_5607_117">
                    <p
                        id="5976_53830"
                        class="Pixso-paragraph-5976_53830 fill-gray60-83_2722-paragraph text-text-smmedium-5454_21607"
                    >
                        {{ text_5607_123 ?? "This is an input helper text." }}
                    </p>
                </slot>
            </div>
            <div
                id="5976_53831"
                class="Pixso-symbol-5976_53831"
                v-if="State === 'Filled' && Type === 'Action' && Size === 'md'"
            >
                <div id="5976_53832" class="Pixso-frame-5976_53832">
                    <div class="frame-content-5976_53832">
                        <slot name="slot_5976_53833" v-if="visible_5607_114">
                            <p
                                id="5976_53833"
                                class="Pixso-paragraph-5976_53833 fill-gray80-32_4123-paragraph text-text-smbold-423_3208"
                            >
                                {{ text_5607_120 ?? "Label" }}
                            </p>
                        </slot>
                        <slot name="slot_5976_53834">
                            <InputTextBase
                                id="5976_53834"
                                class="Pixso-instance-5976_53834"
                                Type="Action"
                                Size="md"
                            />
                        </slot>
                    </div>
                </div>
                <slot name="slot_5976_53835" v-if="visible_5607_117">
                    <p
                        id="5976_53835"
                        class="Pixso-paragraph-5976_53835 fill-gray60-83_2722-paragraph text-text-smmedium-5454_21607"
                    >
                        {{ text_5607_123 ?? "This is an input helper text." }}
                    </p>
                </slot>
            </div>
            <div
                id="5976_53836"
                class="Pixso-symbol-5976_53836"
                v-if="State === 'Focused' && Type === 'Action' && Size === 'md'"
            >
                <div id="5976_53837" class="Pixso-frame-5976_53837">
                    <div class="frame-content-5976_53837">
                        <slot name="slot_5976_53838" v-if="visible_5607_114">
                            <p
                                id="5976_53838"
                                class="Pixso-paragraph-5976_53838 fill-gray80-32_4123-paragraph text-text-smbold-423_3208"
                            >
                                {{ text_5607_120 ?? "Label" }}
                            </p>
                        </slot>
                        <slot name="slot_5976_53839">
                            <InputTextBase
                                id="5976_53839"
                                class="Pixso-instance-5976_53839"
                                Type="Action"
                                Size="md"
                            />
                        </slot>
                    </div>
                </div>
                <slot name="slot_5976_53840" v-if="visible_5607_117">
                    <p
                        id="5976_53840"
                        class="Pixso-paragraph-5976_53840 fill-gray60-83_2722-paragraph text-text-smmedium-5454_21607"
                    >
                        {{ text_5607_123 ?? "This is an input helper text." }}
                    </p>
                </slot>
            </div>
            <div
                id="5976_53841"
                class="Pixso-symbol-5976_53841"
                v-if="
                    State === 'Disabled' && Type === 'Action' && Size === 'md'
                "
            >
                <div id="5976_53842" class="Pixso-frame-5976_53842">
                    <div class="frame-content-5976_53842">
                        <slot name="slot_5976_53843" v-if="visible_5607_114">
                            <p
                                id="5976_53843"
                                class="Pixso-paragraph-5976_53843 fill-gray80-32_4123-paragraph text-text-smbold-423_3208"
                            >
                                {{ text_5607_120 ?? "Label" }}
                            </p>
                        </slot>
                        <slot name="slot_5976_53844">
                            <InputTextBase
                                id="5976_53844"
                                class="Pixso-instance-5976_53844"
                                Type="Action"
                                Size="md"
                            >
                                <template #slot_5976_52057>
                                    <CopySimple
                                        id="5976_52057"
                                        class="Pixso-instance-5976_52057"
                                        Format="Outline"
                                        Weight="Bold"
                                    />
                                </template>
                            </InputTextBase>
                        </slot>
                    </div>
                </div>
                <slot name="slot_5976_53845" v-if="visible_5607_117">
                    <p
                        id="5976_53845"
                        class="Pixso-paragraph-5976_53845 fill-gray60-83_2722-paragraph text-text-smmedium-5454_21607"
                    >
                        {{ text_5607_123 ?? "This is an input helper text." }}
                    </p>
                </slot>
            </div>
            <div
                id="5976_53846"
                class="Pixso-symbol-5976_53846"
                v-if="State === 'Error' && Type === 'Action' && Size === 'md'"
            >
                <div id="5976_53847" class="Pixso-frame-5976_53847">
                    <div class="frame-content-5976_53847">
                        <slot name="slot_5976_53848" v-if="visible_5607_114">
                            <p
                                id="5976_53848"
                                class="Pixso-paragraph-5976_53848 fill-gray80-32_4123-paragraph text-text-smbold-423_3208"
                            >
                                {{ text_5607_120 ?? "Label" }}
                            </p>
                        </slot>
                        <slot name="slot_5976_53849">
                            <InputTextBase
                                id="5976_53849"
                                class="Pixso-instance-5976_53849"
                                Type="Action"
                                Size="md"
                            />
                        </slot>
                    </div>
                </div>
                <slot name="slot_5976_53850" v-if="visible_5607_117">
                    <p
                        id="5976_53850"
                        class="Pixso-paragraph-5976_53850 fill-destructive50-423_3219-paragraph text-text-smmedium-5454_21607"
                    >
                        {{ text_5607_123 ?? "This is an input helper text." }}
                    </p>
                </slot>
            </div>
            <div
                id="5976_53851"
                class="Pixso-symbol-5976_53851"
                v-if="
                    State === 'Default' && Type === 'Currency' && Size === 'md'
                "
            >
                <div id="5976_53852" class="Pixso-frame-5976_53852">
                    <div class="frame-content-5976_53852">
                        <slot name="slot_5976_53853" v-if="visible_5607_114">
                            <p
                                id="5976_53853"
                                class="Pixso-paragraph-5976_53853 fill-gray80-32_4123-paragraph text-text-smbold-423_3208"
                            >
                                {{ text_5607_120 ?? "Label" }}
                            </p>
                        </slot>
                        <slot name="slot_5976_53854">
                            <InputTextBase
                                id="5976_53854"
                                class="Pixso-instance-5976_53854"
                                Type="Currency"
                                Size="md"
                            />
                        </slot>
                    </div>
                </div>
                <slot name="slot_5976_53855" v-if="visible_5607_117">
                    <p
                        id="5976_53855"
                        class="Pixso-paragraph-5976_53855 fill-gray60-83_2722-paragraph text-text-smmedium-5454_21607"
                    >
                        {{ text_5607_123 ?? "This is an input helper text." }}
                    </p>
                </slot>
            </div>
            <div
                id="5976_53856"
                class="Pixso-symbol-5976_53856"
                v-if="State === 'Hover' && Type === 'Currency' && Size === 'md'"
            >
                <div id="5976_53857" class="Pixso-frame-5976_53857">
                    <div class="frame-content-5976_53857">
                        <slot name="slot_5976_53858" v-if="visible_5607_114">
                            <p
                                id="5976_53858"
                                class="Pixso-paragraph-5976_53858 fill-gray80-32_4123-paragraph text-text-smbold-423_3208"
                            >
                                {{ text_5607_120 ?? "Label" }}
                            </p>
                        </slot>
                        <slot name="slot_5976_53859">
                            <InputTextBase
                                id="5976_53859"
                                class="Pixso-instance-5976_53859"
                                Type="Currency"
                                Size="md"
                            />
                        </slot>
                    </div>
                </div>
                <slot name="slot_5976_53860" v-if="visible_5607_117">
                    <p
                        id="5976_53860"
                        class="Pixso-paragraph-5976_53860 fill-gray60-83_2722-paragraph text-text-smmedium-5454_21607"
                    >
                        {{ text_5607_123 ?? "This is an input helper text." }}
                    </p>
                </slot>
            </div>
            <div
                id="5976_53861"
                class="Pixso-symbol-5976_53861"
                v-if="
                    State === 'Filled' && Type === 'Currency' && Size === 'md'
                "
            >
                <div id="5976_53862" class="Pixso-frame-5976_53862">
                    <div class="frame-content-5976_53862">
                        <slot name="slot_5976_53863" v-if="visible_5607_114">
                            <p
                                id="5976_53863"
                                class="Pixso-paragraph-5976_53863 fill-gray80-32_4123-paragraph text-text-smbold-423_3208"
                            >
                                {{ text_5607_120 ?? "Label" }}
                            </p>
                        </slot>
                        <slot name="slot_5976_53864">
                            <InputTextBase
                                id="5976_53864"
                                class="Pixso-instance-5976_53864"
                                Type="Currency"
                                Size="md"
                            />
                        </slot>
                    </div>
                </div>
                <slot name="slot_5976_53865" v-if="visible_5607_117">
                    <p
                        id="5976_53865"
                        class="Pixso-paragraph-5976_53865 fill-gray60-83_2722-paragraph text-text-smmedium-5454_21607"
                    >
                        {{ text_5607_123 ?? "This is an input helper text." }}
                    </p>
                </slot>
            </div>
            <div
                id="5976_53866"
                class="Pixso-symbol-5976_53866"
                v-if="
                    State === 'Focused' && Type === 'Currency' && Size === 'md'
                "
            >
                <div id="5976_53867" class="Pixso-frame-5976_53867">
                    <div class="frame-content-5976_53867">
                        <slot name="slot_5976_53868" v-if="visible_5607_114">
                            <p
                                id="5976_53868"
                                class="Pixso-paragraph-5976_53868 fill-gray80-32_4123-paragraph text-text-smbold-423_3208"
                            >
                                {{ text_5607_120 ?? "Label" }}
                            </p>
                        </slot>
                        <slot name="slot_5976_53869">
                            <InputTextBase
                                id="5976_53869"
                                class="Pixso-instance-5976_53869"
                                Type="Currency"
                                Size="md"
                            />
                        </slot>
                    </div>
                </div>
                <slot name="slot_5976_53870" v-if="visible_5607_117">
                    <p
                        id="5976_53870"
                        class="Pixso-paragraph-5976_53870 fill-gray60-83_2722-paragraph text-text-smmedium-5454_21607"
                    >
                        {{ text_5607_123 ?? "This is an input helper text." }}
                    </p>
                </slot>
            </div>
            <div
                id="5976_53871"
                class="Pixso-symbol-5976_53871"
                v-if="
                    State === 'Disabled' && Type === 'Currency' && Size === 'md'
                "
            >
                <div id="5976_53872" class="Pixso-frame-5976_53872">
                    <div class="frame-content-5976_53872">
                        <slot name="slot_5976_53873" v-if="visible_5607_114">
                            <p
                                id="5976_53873"
                                class="Pixso-paragraph-5976_53873 fill-gray80-32_4123-paragraph text-text-smbold-423_3208"
                            >
                                {{ text_5607_120 ?? "Label" }}
                            </p>
                        </slot>
                        <slot name="slot_5976_53874">
                            <InputTextBase
                                id="5976_53874"
                                class="Pixso-instance-5976_53874"
                                Type="Currency"
                                Size="md"
                            >
                                <template #slot_5976_52065>
                                    <CaretDown
                                        id="5976_52065"
                                        class="Pixso-instance-5976_52065"
                                        Format="Outline"
                                        Weight="Bold"
                                    />
                                </template>
                                <template #slot_5976_52060>
                                    <CurrencyDollarSimple
                                        id="5976_52060"
                                        class="Pixso-instance-5976_52060"
                                        Format="Outline"
                                        Weight="Bold"
                                    />
                                </template>
                            </InputTextBase>
                        </slot>
                    </div>
                </div>
                <slot name="slot_5976_53875" v-if="visible_5607_117">
                    <p
                        id="5976_53875"
                        class="Pixso-paragraph-5976_53875 fill-gray60-83_2722-paragraph text-text-smmedium-5454_21607"
                    >
                        {{ text_5607_123 ?? "This is an input helper text." }}
                    </p>
                </slot>
            </div>
            <div
                id="5976_53876"
                class="Pixso-symbol-5976_53876"
                v-if="State === 'Error' && Type === 'Currency' && Size === 'md'"
            >
                <div id="5976_53877" class="Pixso-frame-5976_53877">
                    <div class="frame-content-5976_53877">
                        <slot name="slot_5976_53878" v-if="visible_5607_114">
                            <p
                                id="5976_53878"
                                class="Pixso-paragraph-5976_53878 fill-gray80-32_4123-paragraph text-text-smbold-423_3208"
                            >
                                {{ text_5607_120 ?? "Label" }}
                            </p>
                        </slot>
                        <slot name="slot_5976_53879">
                            <InputTextBase
                                id="5976_53879"
                                class="Pixso-instance-5976_53879"
                                Type="Currency"
                                Size="md"
                            />
                        </slot>
                    </div>
                </div>
                <slot name="slot_5976_53880" v-if="visible_5607_117">
                    <p
                        id="5976_53880"
                        class="Pixso-paragraph-5976_53880 fill-destructive50-423_3219-paragraph text-text-smmedium-5454_21607"
                    >
                        {{ text_5607_123 ?? "This is an input helper text." }}
                    </p>
                </slot>
            </div>
            <div
                id="5976_53881"
                class="Pixso-symbol-5976_53881"
                v-if="
                    State === 'Default' &&
                    Type === 'Credit Card' &&
                    Size === 'md'
                "
            >
                <div id="5976_53882" class="Pixso-frame-5976_53882">
                    <div class="frame-content-5976_53882">
                        <slot name="slot_5976_53883" v-if="visible_5607_114">
                            <p
                                id="5976_53883"
                                class="Pixso-paragraph-5976_53883 fill-gray80-32_4123-paragraph text-text-smbold-423_3208"
                            >
                                {{ text_5607_120 ?? "Label" }}
                            </p>
                        </slot>
                        <slot name="slot_5976_53884">
                            <InputTextBase
                                id="5976_53884"
                                class="Pixso-instance-5976_53884"
                                Type="Credit Card"
                                Size="md"
                            />
                        </slot>
                    </div>
                </div>
                <slot name="slot_5976_53885" v-if="visible_5607_117">
                    <p
                        id="5976_53885"
                        class="Pixso-paragraph-5976_53885 fill-gray60-83_2722-paragraph text-text-smmedium-5454_21607"
                    >
                        {{ text_5607_123 ?? "This is an input helper text." }}
                    </p>
                </slot>
            </div>
            <div
                id="5976_53886"
                class="Pixso-symbol-5976_53886"
                v-if="
                    State === 'Hover' && Type === 'Credit Card' && Size === 'md'
                "
            >
                <div id="5976_53887" class="Pixso-frame-5976_53887">
                    <div class="frame-content-5976_53887">
                        <slot name="slot_5976_53888" v-if="visible_5607_114">
                            <p
                                id="5976_53888"
                                class="Pixso-paragraph-5976_53888 fill-gray80-32_4123-paragraph text-text-smbold-423_3208"
                            >
                                {{ text_5607_120 ?? "Label" }}
                            </p>
                        </slot>
                        <slot name="slot_5976_53889">
                            <InputTextBase
                                id="5976_53889"
                                class="Pixso-instance-5976_53889"
                                Type="Credit Card"
                                Size="md"
                            />
                        </slot>
                    </div>
                </div>
                <slot name="slot_5976_53890" v-if="visible_5607_117">
                    <p
                        id="5976_53890"
                        class="Pixso-paragraph-5976_53890 fill-gray60-83_2722-paragraph text-text-smmedium-5454_21607"
                    >
                        {{ text_5607_123 ?? "This is an input helper text." }}
                    </p>
                </slot>
            </div>
            <div
                id="5976_53891"
                class="Pixso-symbol-5976_53891"
                v-if="
                    State === 'Filled' &&
                    Type === 'Credit Card' &&
                    Size === 'md'
                "
            >
                <div id="5976_53892" class="Pixso-frame-5976_53892">
                    <div class="frame-content-5976_53892">
                        <slot name="slot_5976_53893" v-if="visible_5607_114">
                            <p
                                id="5976_53893"
                                class="Pixso-paragraph-5976_53893 fill-gray80-32_4123-paragraph text-text-smbold-423_3208"
                            >
                                {{ text_5607_120 ?? "Label" }}
                            </p>
                        </slot>
                        <slot name="slot_5976_53894">
                            <InputTextBase
                                id="5976_53894"
                                class="Pixso-instance-5976_53894"
                                Type="Credit Card"
                                Size="md"
                            />
                        </slot>
                    </div>
                </div>
                <slot name="slot_5976_53895" v-if="visible_5607_117">
                    <p
                        id="5976_53895"
                        class="Pixso-paragraph-5976_53895 fill-gray60-83_2722-paragraph text-text-smmedium-5454_21607"
                    >
                        {{ text_5607_123 ?? "This is an input helper text." }}
                    </p>
                </slot>
            </div>
            <div
                id="5976_53896"
                class="Pixso-symbol-5976_53896"
                v-if="
                    State === 'Focused' &&
                    Type === 'Credit Card' &&
                    Size === 'md'
                "
            >
                <div id="5976_53897" class="Pixso-frame-5976_53897">
                    <div class="frame-content-5976_53897">
                        <slot name="slot_5976_53898" v-if="visible_5607_114">
                            <p
                                id="5976_53898"
                                class="Pixso-paragraph-5976_53898 fill-gray80-32_4123-paragraph text-text-smbold-423_3208"
                            >
                                {{ text_5607_120 ?? "Label" }}
                            </p>
                        </slot>
                        <slot name="slot_5976_53899">
                            <InputTextBase
                                id="5976_53899"
                                class="Pixso-instance-5976_53899"
                                Type="Credit Card"
                                Size="md"
                            />
                        </slot>
                    </div>
                </div>
                <slot name="slot_5976_53900" v-if="visible_5607_117">
                    <p
                        id="5976_53900"
                        class="Pixso-paragraph-5976_53900 fill-gray60-83_2722-paragraph text-text-smmedium-5454_21607"
                    >
                        {{ text_5607_123 ?? "This is an input helper text." }}
                    </p>
                </slot>
            </div>
            <div
                id="5976_53901"
                class="Pixso-symbol-5976_53901"
                v-if="
                    State === 'Disabled' &&
                    Type === 'Credit Card' &&
                    Size === 'md'
                "
            >
                <div id="5976_53902" class="Pixso-frame-5976_53902">
                    <div class="frame-content-5976_53902">
                        <slot name="slot_5976_53903" v-if="visible_5607_114">
                            <p
                                id="5976_53903"
                                class="Pixso-paragraph-5976_53903 fill-gray80-32_4123-paragraph text-text-smbold-423_3208"
                            >
                                {{ text_5607_120 ?? "Label" }}
                            </p>
                        </slot>
                        <slot name="slot_5976_53904">
                            <InputTextBase
                                id="5976_53904"
                                class="Pixso-instance-5976_53904"
                                Type="Credit Card"
                                Size="md"
                            />
                        </slot>
                    </div>
                </div>
                <slot name="slot_5976_53905" v-if="visible_5607_117">
                    <p
                        id="5976_53905"
                        class="Pixso-paragraph-5976_53905 fill-gray60-83_2722-paragraph text-text-smmedium-5454_21607"
                    >
                        {{ text_5607_123 ?? "This is an input helper text." }}
                    </p>
                </slot>
            </div>
            <div
                id="5976_53906"
                class="Pixso-symbol-5976_53906"
                v-if="
                    State === 'Error' && Type === 'Credit Card' && Size === 'md'
                "
            >
                <div id="5976_53907" class="Pixso-frame-5976_53907">
                    <div class="frame-content-5976_53907">
                        <slot name="slot_5976_53908" v-if="visible_5607_114">
                            <p
                                id="5976_53908"
                                class="Pixso-paragraph-5976_53908 fill-gray80-32_4123-paragraph text-text-smbold-423_3208"
                            >
                                {{ text_5607_120 ?? "Label" }}
                            </p>
                        </slot>
                        <slot name="slot_5976_53909">
                            <InputTextBase
                                id="5976_53909"
                                class="Pixso-instance-5976_53909"
                                Type="Credit Card"
                                Size="md"
                            />
                        </slot>
                    </div>
                </div>
                <slot name="slot_5976_53910" v-if="visible_5607_117">
                    <p
                        id="5976_53910"
                        class="Pixso-paragraph-5976_53910 fill-destructive50-423_3219-paragraph text-text-smmedium-5454_21607"
                    >
                        {{ text_5607_123 ?? "This is an input helper text." }}
                    </p>
                </slot>
            </div>
            <div
                id="5976_53911"
                class="Pixso-symbol-5976_53911"
                v-if="State === 'Default' && Type === 'Date' && Size === 'md'"
            >
                <div id="5976_53912" class="Pixso-frame-5976_53912">
                    <div class="frame-content-5976_53912">
                        <slot name="slot_5976_53913" v-if="visible_5607_114">
                            <p
                                id="5976_53913"
                                class="Pixso-paragraph-5976_53913 fill-gray80-32_4123-paragraph text-text-smbold-423_3208"
                            >
                                {{ text_5607_120 ?? "Label" }}
                            </p>
                        </slot>
                        <slot name="slot_5976_53914">
                            <InputTextBase
                                id="5976_53914"
                                class="Pixso-instance-5976_53914"
                                Type="Date"
                                Size="md"
                            />
                        </slot>
                    </div>
                </div>
                <slot name="slot_5976_53915" v-if="visible_5607_117">
                    <p
                        id="5976_53915"
                        class="Pixso-paragraph-5976_53915 fill-gray60-83_2722-paragraph text-text-smmedium-5454_21607"
                    >
                        {{ text_5607_123 ?? "This is an input helper text." }}
                    </p>
                </slot>
            </div>
            <div
                id="5976_53916"
                class="Pixso-symbol-5976_53916"
                v-if="State === 'Hover' && Type === 'Date' && Size === 'md'"
            >
                <div id="5976_53917" class="Pixso-frame-5976_53917">
                    <div class="frame-content-5976_53917">
                        <slot name="slot_5976_53918" v-if="visible_5607_114">
                            <p
                                id="5976_53918"
                                class="Pixso-paragraph-5976_53918 fill-gray80-32_4123-paragraph text-text-smbold-423_3208"
                            >
                                {{ text_5607_120 ?? "Label" }}
                            </p>
                        </slot>
                        <slot name="slot_5976_53919">
                            <InputTextBase
                                id="5976_53919"
                                class="Pixso-instance-5976_53919"
                                Type="Date"
                                Size="md"
                            />
                        </slot>
                    </div>
                </div>
                <slot name="slot_5976_53920" v-if="visible_5607_117">
                    <p
                        id="5976_53920"
                        class="Pixso-paragraph-5976_53920 fill-gray60-83_2722-paragraph text-text-smmedium-5454_21607"
                    >
                        {{ text_5607_123 ?? "This is an input helper text." }}
                    </p>
                </slot>
            </div>
            <div
                id="5976_53921"
                class="Pixso-symbol-5976_53921"
                v-if="State === 'Filled' && Type === 'Date' && Size === 'md'"
            >
                <div id="5976_53922" class="Pixso-frame-5976_53922">
                    <div class="frame-content-5976_53922">
                        <slot name="slot_5976_53923" v-if="visible_5607_114">
                            <p
                                id="5976_53923"
                                class="Pixso-paragraph-5976_53923 fill-gray80-32_4123-paragraph text-text-smbold-423_3208"
                            >
                                {{ text_5607_120 ?? "Label" }}
                            </p>
                        </slot>
                        <slot name="slot_5976_53924">
                            <InputTextBase
                                id="5976_53924"
                                class="Pixso-instance-5976_53924"
                                Type="Date"
                                Size="md"
                            />
                        </slot>
                    </div>
                </div>
                <slot name="slot_5976_53925" v-if="visible_5607_117">
                    <p
                        id="5976_53925"
                        class="Pixso-paragraph-5976_53925 fill-gray60-83_2722-paragraph text-text-smmedium-5454_21607"
                    >
                        {{ text_5607_123 ?? "This is an input helper text." }}
                    </p>
                </slot>
            </div>
            <div
                id="5976_53926"
                class="Pixso-symbol-5976_53926"
                v-if="State === 'Focused' && Type === 'Date' && Size === 'md'"
            >
                <div id="5976_53927" class="Pixso-frame-5976_53927">
                    <div class="frame-content-5976_53927">
                        <slot name="slot_5976_53928" v-if="visible_5607_114">
                            <p
                                id="5976_53928"
                                class="Pixso-paragraph-5976_53928 fill-gray80-32_4123-paragraph text-text-smbold-423_3208"
                            >
                                {{ text_5607_120 ?? "Label" }}
                            </p>
                        </slot>
                        <slot name="slot_5976_53929">
                            <InputTextBase
                                id="5976_53929"
                                class="Pixso-instance-5976_53929"
                                Type="Date"
                                Size="md"
                            />
                        </slot>
                    </div>
                </div>
                <slot name="slot_5976_53930" v-if="visible_5607_117">
                    <p
                        id="5976_53930"
                        class="Pixso-paragraph-5976_53930 fill-gray60-83_2722-paragraph text-text-smmedium-5454_21607"
                    >
                        {{ text_5607_123 ?? "This is an input helper text." }}
                    </p>
                </slot>
            </div>
            <div
                id="5976_53931"
                class="Pixso-symbol-5976_53931"
                v-if="State === 'Disabled' && Type === 'Date' && Size === 'md'"
            >
                <div id="5976_53932" class="Pixso-frame-5976_53932">
                    <div class="frame-content-5976_53932">
                        <slot name="slot_5976_53933" v-if="visible_5607_114">
                            <p
                                id="5976_53933"
                                class="Pixso-paragraph-5976_53933 fill-gray80-32_4123-paragraph text-text-smbold-423_3208"
                            >
                                {{ text_5607_120 ?? "Label" }}
                            </p>
                        </slot>
                        <slot name="slot_5976_53934">
                            <InputTextBase
                                id="5976_53934"
                                class="Pixso-instance-5976_53934"
                                Type="Date"
                                Size="md"
                            >
                                <template #slot_5976_52073>
                                    <CalendarBlank
                                        id="5976_52073"
                                        class="Pixso-instance-5976_52073"
                                        Format="Outline"
                                        Weight="Bold"
                                    />
                                </template>
                            </InputTextBase>
                        </slot>
                    </div>
                </div>
                <slot name="slot_5976_53935" v-if="visible_5607_117">
                    <p
                        id="5976_53935"
                        class="Pixso-paragraph-5976_53935 fill-gray60-83_2722-paragraph text-text-smmedium-5454_21607"
                    >
                        {{ text_5607_123 ?? "This is an input helper text." }}
                    </p>
                </slot>
            </div>
            <div
                id="5976_53936"
                class="Pixso-symbol-5976_53936"
                v-if="State === 'Error' && Type === 'Date' && Size === 'md'"
            >
                <div id="5976_53937" class="Pixso-frame-5976_53937">
                    <div class="frame-content-5976_53937">
                        <slot name="slot_5976_53938" v-if="visible_5607_114">
                            <p
                                id="5976_53938"
                                class="Pixso-paragraph-5976_53938 fill-gray80-32_4123-paragraph text-text-smbold-423_3208"
                            >
                                {{ text_5607_120 ?? "Label" }}
                            </p>
                        </slot>
                        <slot name="slot_5976_53939">
                            <InputTextBase
                                id="5976_53939"
                                class="Pixso-instance-5976_53939"
                                Type="Date"
                                Size="md"
                            />
                        </slot>
                    </div>
                </div>
                <slot name="slot_5976_53940" v-if="visible_5607_117">
                    <p
                        id="5976_53940"
                        class="Pixso-paragraph-5976_53940 fill-destructive50-423_3219-paragraph text-text-smmedium-5454_21607"
                    >
                        {{ text_5607_123 ?? "This is an input helper text." }}
                    </p>
                </slot>
            </div>
            <div
                id="5976_53941"
                class="Pixso-symbol-5976_53941"
                v-if="State === 'Default' && Type === 'Link' && Size === 'md'"
            >
                <div id="5976_53942" class="Pixso-frame-5976_53942">
                    <div class="frame-content-5976_53942">
                        <slot name="slot_5976_53943" v-if="visible_5607_114">
                            <p
                                id="5976_53943"
                                class="Pixso-paragraph-5976_53943 fill-gray80-32_4123-paragraph text-text-smbold-423_3208"
                            >
                                {{ text_5607_120 ?? "Label" }}
                            </p>
                        </slot>
                        <slot name="slot_5976_53944">
                            <InputTextBase
                                id="5976_53944"
                                class="Pixso-instance-5976_53944"
                                Type="Link"
                                Size="md"
                            />
                        </slot>
                    </div>
                </div>
                <slot name="slot_5976_53945" v-if="visible_5607_117">
                    <p
                        id="5976_53945"
                        class="Pixso-paragraph-5976_53945 fill-gray60-83_2722-paragraph text-text-smmedium-5454_21607"
                    >
                        {{ text_5607_123 ?? "This is an input helper text." }}
                    </p>
                </slot>
            </div>
            <div
                id="5976_53946"
                class="Pixso-symbol-5976_53946"
                v-if="State === 'Hover' && Type === 'Link' && Size === 'md'"
            >
                <div id="5976_53947" class="Pixso-frame-5976_53947">
                    <div class="frame-content-5976_53947">
                        <slot name="slot_5976_53948" v-if="visible_5607_114">
                            <p
                                id="5976_53948"
                                class="Pixso-paragraph-5976_53948 fill-gray80-32_4123-paragraph text-text-smbold-423_3208"
                            >
                                {{ text_5607_120 ?? "Label" }}
                            </p>
                        </slot>
                        <slot name="slot_5976_53949">
                            <InputTextBase
                                id="5976_53949"
                                class="Pixso-instance-5976_53949"
                                Type="Link"
                                Size="md"
                            />
                        </slot>
                    </div>
                </div>
                <slot name="slot_5976_53950" v-if="visible_5607_117">
                    <p
                        id="5976_53950"
                        class="Pixso-paragraph-5976_53950 fill-gray60-83_2722-paragraph text-text-smmedium-5454_21607"
                    >
                        {{ text_5607_123 ?? "This is an input helper text." }}
                    </p>
                </slot>
            </div>
            <div
                id="5976_53951"
                class="Pixso-symbol-5976_53951"
                v-if="State === 'Filled' && Type === 'Link' && Size === 'md'"
            >
                <div id="5976_53952" class="Pixso-frame-5976_53952">
                    <div class="frame-content-5976_53952">
                        <slot name="slot_5976_53953" v-if="visible_5607_114">
                            <p
                                id="5976_53953"
                                class="Pixso-paragraph-5976_53953 fill-gray80-32_4123-paragraph text-text-smbold-423_3208"
                            >
                                {{ text_5607_120 ?? "Label" }}
                            </p>
                        </slot>
                        <slot name="slot_5976_53954">
                            <InputTextBase
                                id="5976_53954"
                                class="Pixso-instance-5976_53954"
                                Type="Link"
                                Size="md"
                            />
                        </slot>
                    </div>
                </div>
                <slot name="slot_5976_53955" v-if="visible_5607_117">
                    <p
                        id="5976_53955"
                        class="Pixso-paragraph-5976_53955 fill-gray60-83_2722-paragraph text-text-smmedium-5454_21607"
                    >
                        {{ text_5607_123 ?? "This is an input helper text." }}
                    </p>
                </slot>
            </div>
            <div
                id="5976_53956"
                class="Pixso-symbol-5976_53956"
                v-if="State === 'Focused' && Type === 'Link' && Size === 'md'"
            >
                <div id="5976_53957" class="Pixso-frame-5976_53957">
                    <div class="frame-content-5976_53957">
                        <slot name="slot_5976_53958" v-if="visible_5607_114">
                            <p
                                id="5976_53958"
                                class="Pixso-paragraph-5976_53958 fill-gray80-32_4123-paragraph text-text-smbold-423_3208"
                            >
                                {{ text_5607_120 ?? "Label" }}
                            </p>
                        </slot>
                        <slot name="slot_5976_53959">
                            <InputTextBase
                                id="5976_53959"
                                class="Pixso-instance-5976_53959"
                                Type="Link"
                                Size="md"
                            />
                        </slot>
                    </div>
                </div>
                <slot name="slot_5976_53960" v-if="visible_5607_117">
                    <p
                        id="5976_53960"
                        class="Pixso-paragraph-5976_53960 fill-gray60-83_2722-paragraph text-text-smmedium-5454_21607"
                    >
                        {{ text_5607_123 ?? "This is an input helper text." }}
                    </p>
                </slot>
            </div>
            <div
                id="5976_53961"
                class="Pixso-symbol-5976_53961"
                v-if="State === 'Disabled' && Type === 'Link' && Size === 'md'"
            >
                <div id="5976_53962" class="Pixso-frame-5976_53962">
                    <div class="frame-content-5976_53962">
                        <slot name="slot_5976_53963" v-if="visible_5607_114">
                            <p
                                id="5976_53963"
                                class="Pixso-paragraph-5976_53963 fill-gray80-32_4123-paragraph text-text-smbold-423_3208"
                            >
                                {{ text_5607_120 ?? "Label" }}
                            </p>
                        </slot>
                        <slot name="slot_5976_53964">
                            <InputTextBase
                                id="5976_53964"
                                class="Pixso-instance-5976_53964"
                                Type="Link"
                                Size="md"
                            />
                        </slot>
                    </div>
                </div>
                <slot name="slot_5976_53965" v-if="visible_5607_117">
                    <p
                        id="5976_53965"
                        class="Pixso-paragraph-5976_53965 fill-gray60-83_2722-paragraph text-text-smmedium-5454_21607"
                    >
                        {{ text_5607_123 ?? "This is an input helper text." }}
                    </p>
                </slot>
            </div>
            <div
                id="5976_53966"
                class="Pixso-symbol-5976_53966"
                v-if="State === 'Error' && Type === 'Link' && Size === 'md'"
            >
                <div id="5976_53967" class="Pixso-frame-5976_53967">
                    <div class="frame-content-5976_53967">
                        <slot name="slot_5976_53968" v-if="visible_5607_114">
                            <p
                                id="5976_53968"
                                class="Pixso-paragraph-5976_53968 fill-gray80-32_4123-paragraph text-text-smbold-423_3208"
                            >
                                {{ text_5607_120 ?? "Label" }}
                            </p>
                        </slot>
                        <slot name="slot_5976_53969">
                            <InputTextBase
                                id="5976_53969"
                                class="Pixso-instance-5976_53969"
                                Type="Link"
                                Size="md"
                            />
                        </slot>
                    </div>
                </div>
                <slot name="slot_5976_53970" v-if="visible_5607_117">
                    <p
                        id="5976_53970"
                        class="Pixso-paragraph-5976_53970 fill-destructive50-423_3219-paragraph text-text-smmedium-5454_21607"
                    >
                        {{ text_5607_123 ?? "This is an input helper text." }}
                    </p>
                </slot>
            </div>
            <div
                id="5976_53971"
                class="Pixso-symbol-5976_53971"
                v-if="
                    State === 'Default' && Type === 'Password' && Size === 'md'
                "
            >
                <div id="5976_53972" class="Pixso-frame-5976_53972">
                    <div class="frame-content-5976_53972">
                        <slot name="slot_5976_53973" v-if="visible_5607_114">
                            <p
                                id="5976_53973"
                                class="Pixso-paragraph-5976_53973 fill-gray80-32_4123-paragraph text-text-smbold-423_3208"
                            >
                                {{ text_5607_120 ?? "Label" }}
                            </p>
                        </slot>
                        <slot name="slot_5976_53974">
                            <InputTextBase
                                id="5976_53974"
                                class="Pixso-instance-5976_53974"
                                Type="Password"
                                Size="md"
                            />
                        </slot>
                    </div>
                </div>
                <div
                    id="5976_53975"
                    class="Pixso-frame-5976_53975"
                    v-if="visible_5612_159"
                >
                    <div class="frame-content-5976_53975">
                        <slot name="slot_5976_53976">
                            <ProgressBarAtom
                                id="5976_53976"
                                class="Pixso-instance-5976_53976"
                                Size="sm"
                                Style="Fill"
                            />
                        </slot>
                        <slot name="slot_5976_53977">
                            <ProgressBarAtom
                                id="5976_53977"
                                class="Pixso-instance-5976_53977"
                                Size="sm"
                                Style="Fill"
                            />
                        </slot>
                        <slot name="slot_5976_53978">
                            <ProgressBarAtom
                                id="5976_53978"
                                class="Pixso-instance-5976_53978"
                                Size="sm"
                                Style="Fill"
                            />
                        </slot>
                        <slot name="slot_5976_53979">
                            <ProgressBarAtom
                                id="5976_53979"
                                class="Pixso-instance-5976_53979"
                                Size="sm"
                                Style="Fill"
                            />
                        </slot>
                    </div>
                </div>
                <slot name="slot_5976_53980" v-if="visible_5612_104">
                    <p
                        id="5976_53980"
                        class="Pixso-paragraph-5976_53980 fill-gray60-83_2722-paragraph text-text-smmedium-5454_21607"
                    >
                        {{ text_5612_49 ?? "This is a validation text." }}
                    </p>
                </slot>
            </div>
            <div
                id="5976_53981"
                class="Pixso-symbol-5976_53981"
                v-if="State === 'Hover' && Type === 'Password' && Size === 'md'"
            >
                <div id="5976_53982" class="Pixso-frame-5976_53982">
                    <div class="frame-content-5976_53982">
                        <slot name="slot_5976_53983" v-if="visible_5607_114">
                            <p
                                id="5976_53983"
                                class="Pixso-paragraph-5976_53983 fill-gray80-32_4123-paragraph text-text-smbold-423_3208"
                            >
                                {{ text_5607_120 ?? "Label" }}
                            </p>
                        </slot>
                        <slot name="slot_5976_53984">
                            <InputTextBase
                                id="5976_53984"
                                class="Pixso-instance-5976_53984"
                                Type="Password"
                                Size="md"
                            />
                        </slot>
                    </div>
                </div>
                <div
                    id="5976_53985"
                    class="Pixso-frame-5976_53985"
                    v-if="visible_5612_159"
                >
                    <div class="frame-content-5976_53985">
                        <slot name="slot_5976_53986">
                            <ProgressBarAtom
                                id="5976_53986"
                                class="Pixso-instance-5976_53986"
                                Size="sm"
                                Style="Fill"
                            />
                        </slot>
                        <slot name="slot_5976_53987">
                            <ProgressBarAtom
                                id="5976_53987"
                                class="Pixso-instance-5976_53987"
                                Size="sm"
                                Style="Fill"
                            />
                        </slot>
                        <slot name="slot_5976_53988">
                            <ProgressBarAtom
                                id="5976_53988"
                                class="Pixso-instance-5976_53988"
                                Size="sm"
                                Style="Fill"
                            />
                        </slot>
                        <slot name="slot_5976_53989">
                            <ProgressBarAtom
                                id="5976_53989"
                                class="Pixso-instance-5976_53989"
                                Size="sm"
                                Style="Fill"
                            />
                        </slot>
                    </div>
                </div>
                <slot name="slot_5976_53990" v-if="visible_5612_104">
                    <p
                        id="5976_53990"
                        class="Pixso-paragraph-5976_53990 fill-gray60-83_2722-paragraph text-text-smmedium-5454_21607"
                    >
                        {{ text_5612_49 ?? "This is a validation text." }}
                    </p>
                </slot>
            </div>
            <div
                id="5976_53991"
                class="Pixso-symbol-5976_53991"
                v-if="
                    State === 'Filled' && Type === 'Password' && Size === 'md'
                "
            >
                <div id="5976_53992" class="Pixso-frame-5976_53992">
                    <div class="frame-content-5976_53992">
                        <slot name="slot_5976_53993" v-if="visible_5607_114">
                            <p
                                id="5976_53993"
                                class="Pixso-paragraph-5976_53993 fill-gray80-32_4123-paragraph text-text-smbold-423_3208"
                            >
                                {{ text_5607_120 ?? "Label" }}
                            </p>
                        </slot>
                        <slot name="slot_5976_53994">
                            <InputTextBase
                                id="5976_53994"
                                class="Pixso-instance-5976_53994"
                                Type="Password"
                                Size="md"
                            />
                        </slot>
                    </div>
                </div>
                <div
                    id="5976_53995"
                    class="Pixso-frame-5976_53995"
                    v-if="visible_5612_159"
                >
                    <div class="frame-content-5976_53995">
                        <slot name="slot_5976_53996">
                            <ProgressBarAtom
                                id="5976_53996"
                                class="Pixso-instance-5976_53996"
                                Size="sm"
                                Style="Fill"
                            />
                        </slot>
                        <slot name="slot_5976_53997">
                            <ProgressBarAtom
                                id="5976_53997"
                                class="Pixso-instance-5976_53997"
                                Size="sm"
                                Style="Fill"
                            />
                        </slot>
                        <slot name="slot_5976_53998">
                            <ProgressBarAtom
                                id="5976_53998"
                                class="Pixso-instance-5976_53998"
                                Size="sm"
                                Style="Fill"
                            />
                        </slot>
                        <slot name="slot_5976_53999">
                            <ProgressBarAtom
                                id="5976_53999"
                                class="Pixso-instance-5976_53999"
                                Size="sm"
                                Style="Fill"
                            />
                        </slot>
                    </div>
                </div>
                <slot name="slot_5976_54000" v-if="visible_5612_104">
                    <p
                        id="5976_54000"
                        class="Pixso-paragraph-5976_54000 fill-gray60-83_2722-paragraph text-text-smmedium-5454_21607"
                    >
                        {{ text_5612_49 ?? "This is a validation text." }}
                    </p>
                </slot>
            </div>
            <div
                id="5976_54001"
                class="Pixso-symbol-5976_54001"
                v-if="
                    State === 'Focused' && Type === 'Password' && Size === 'md'
                "
            >
                <div id="5976_54002" class="Pixso-frame-5976_54002">
                    <div class="frame-content-5976_54002">
                        <slot name="slot_5976_54003" v-if="visible_5607_114">
                            <p
                                id="5976_54003"
                                class="Pixso-paragraph-5976_54003 fill-gray80-32_4123-paragraph text-text-smbold-423_3208"
                            >
                                {{ text_5607_120 ?? "Label" }}
                            </p>
                        </slot>
                        <slot name="slot_5976_54004">
                            <InputTextBase
                                id="5976_54004"
                                class="Pixso-instance-5976_54004"
                                Type="Password"
                                Size="md"
                            />
                        </slot>
                    </div>
                </div>
                <div
                    id="5976_54005"
                    class="Pixso-frame-5976_54005"
                    v-if="visible_5612_159"
                >
                    <div class="frame-content-5976_54005">
                        <slot name="slot_5976_54006">
                            <ProgressBarAtom
                                id="5976_54006"
                                class="Pixso-instance-5976_54006"
                                Size="sm"
                                Style="Fill"
                            />
                        </slot>
                        <slot name="slot_5976_54007">
                            <ProgressBarAtom
                                id="5976_54007"
                                class="Pixso-instance-5976_54007"
                                Size="sm"
                                Style="Fill"
                            />
                        </slot>
                        <slot name="slot_5976_54008">
                            <ProgressBarAtom
                                id="5976_54008"
                                class="Pixso-instance-5976_54008"
                                Size="sm"
                                Style="Fill"
                            />
                        </slot>
                        <slot name="slot_5976_54009">
                            <ProgressBarAtom
                                id="5976_54009"
                                class="Pixso-instance-5976_54009"
                                Size="sm"
                                Style="Fill"
                            />
                        </slot>
                    </div>
                </div>
                <slot name="slot_5976_54010" v-if="visible_5612_104">
                    <p
                        id="5976_54010"
                        class="Pixso-paragraph-5976_54010 fill-gray60-83_2722-paragraph text-text-smmedium-5454_21607"
                    >
                        {{ text_5612_49 ?? "This is a validation text." }}
                    </p>
                </slot>
            </div>
            <div
                id="5976_54011"
                class="Pixso-symbol-5976_54011"
                v-if="
                    State === 'Disabled' && Type === 'Password' && Size === 'md'
                "
            >
                <div id="5976_54012" class="Pixso-frame-5976_54012">
                    <div class="frame-content-5976_54012">
                        <slot name="slot_5976_54013" v-if="visible_5607_114">
                            <p
                                id="5976_54013"
                                class="Pixso-paragraph-5976_54013 fill-gray80-32_4123-paragraph text-text-smbold-423_3208"
                            >
                                {{ text_5607_120 ?? "Label" }}
                            </p>
                        </slot>
                        <slot name="slot_5976_54014">
                            <InputTextBase
                                id="5976_54014"
                                class="Pixso-instance-5976_54014"
                                Type="Password"
                                Size="md"
                            >
                                <template #slot_5976_52082>
                                    <LockSimple
                                        id="5976_52082"
                                        class="Pixso-instance-5976_52082"
                                        Format="Outline"
                                        Weight="Bold"
                                    />
                                </template>
                            </InputTextBase>
                        </slot>
                    </div>
                </div>
                <div
                    id="5976_54015"
                    class="Pixso-frame-5976_54015"
                    v-if="visible_5612_159"
                >
                    <div class="frame-content-5976_54015">
                        <slot name="slot_5976_54016">
                            <ProgressBarAtom
                                id="5976_54016"
                                class="Pixso-instance-5976_54016"
                                Size="sm"
                                Style="Fill"
                            />
                        </slot>
                        <slot name="slot_5976_54017">
                            <ProgressBarAtom
                                id="5976_54017"
                                class="Pixso-instance-5976_54017"
                                Size="sm"
                                Style="Fill"
                            />
                        </slot>
                        <slot name="slot_5976_54018">
                            <ProgressBarAtom
                                id="5976_54018"
                                class="Pixso-instance-5976_54018"
                                Size="sm"
                                Style="Fill"
                            />
                        </slot>
                        <slot name="slot_5976_54019">
                            <ProgressBarAtom
                                id="5976_54019"
                                class="Pixso-instance-5976_54019"
                                Size="sm"
                                Style="Fill"
                            />
                        </slot>
                    </div>
                </div>
                <slot name="slot_5976_54020" v-if="visible_5612_104">
                    <p
                        id="5976_54020"
                        class="Pixso-paragraph-5976_54020 fill-gray60-83_2722-paragraph text-text-smmedium-5454_21607"
                    >
                        {{ text_5612_49 ?? "This is a validation text." }}
                    </p>
                </slot>
            </div>
            <div
                id="5976_54021"
                class="Pixso-symbol-5976_54021"
                v-if="State === 'Error' && Type === 'Password' && Size === 'md'"
            >
                <div id="5976_54022" class="Pixso-frame-5976_54022">
                    <div class="frame-content-5976_54022">
                        <slot name="slot_5976_54023" v-if="visible_5607_114">
                            <p
                                id="5976_54023"
                                class="Pixso-paragraph-5976_54023 fill-gray80-32_4123-paragraph text-text-smbold-423_3208"
                            >
                                {{ text_5607_120 ?? "Label" }}
                            </p>
                        </slot>
                        <slot name="slot_5976_54024">
                            <InputTextBase
                                id="5976_54024"
                                class="Pixso-instance-5976_54024"
                                Type="Password"
                                Size="md"
                            />
                        </slot>
                    </div>
                </div>
                <div
                    id="5976_54025"
                    class="Pixso-frame-5976_54025"
                    v-if="visible_5612_159"
                >
                    <div class="frame-content-5976_54025">
                        <slot name="slot_5976_54026">
                            <ProgressBarAtom
                                id="5976_54026"
                                class="Pixso-instance-5976_54026"
                                Size="sm"
                                Style="Fill"
                            />
                        </slot>
                        <slot name="slot_5976_54027">
                            <ProgressBarAtom
                                id="5976_54027"
                                class="Pixso-instance-5976_54027"
                                Size="sm"
                                Style="Fill"
                            />
                        </slot>
                        <slot name="slot_5976_54028">
                            <ProgressBarAtom
                                id="5976_54028"
                                class="Pixso-instance-5976_54028"
                                Size="sm"
                                Style="Fill"
                            />
                        </slot>
                        <slot name="slot_5976_54029">
                            <ProgressBarAtom
                                id="5976_54029"
                                class="Pixso-instance-5976_54029"
                                Size="sm"
                                Style="Fill"
                            />
                        </slot>
                    </div>
                </div>
                <slot name="slot_5976_54030" v-if="visible_5612_104">
                    <p
                        id="5976_54030"
                        class="Pixso-paragraph-5976_54030 fill-destructive50-423_3219-paragraph text-text-smmedium-5454_21607"
                    >
                        {{ text_5612_49 ?? "This is a validation text." }}
                    </p>
                </slot>
            </div>
            <div
                id="5976_54031"
                class="Pixso-symbol-5976_54031"
                v-if="
                    State === 'Default' &&
                    Type === 'Phone Number/Country' &&
                    Size === 'md'
                "
            >
                <div id="5976_54032" class="Pixso-frame-5976_54032">
                    <div class="frame-content-5976_54032">
                        <slot name="slot_5976_54033" v-if="visible_5607_114">
                            <p
                                id="5976_54033"
                                class="Pixso-paragraph-5976_54033 fill-gray80-32_4123-paragraph text-text-smbold-423_3208"
                            >
                                {{ text_5607_120 ?? "Label" }}
                            </p>
                        </slot>
                        <slot name="slot_5976_54034">
                            <InputTextBase
                                id="5976_54034"
                                class="Pixso-instance-5976_54034"
                                Type="Phone Number/Country"
                                Size="md"
                            />
                        </slot>
                    </div>
                </div>
                <slot name="slot_5976_54035" v-if="visible_5607_117">
                    <p
                        id="5976_54035"
                        class="Pixso-paragraph-5976_54035 fill-gray60-83_2722-paragraph text-text-smmedium-5454_21607"
                    >
                        {{ text_5607_123 ?? "This is an input helper text." }}
                    </p>
                </slot>
            </div>
            <div
                id="5976_54036"
                class="Pixso-symbol-5976_54036"
                v-if="
                    State === 'Hover' &&
                    Type === 'Phone Number/Country' &&
                    Size === 'md'
                "
            >
                <div id="5976_54037" class="Pixso-frame-5976_54037">
                    <div class="frame-content-5976_54037">
                        <slot name="slot_5976_54038" v-if="visible_5607_114">
                            <p
                                id="5976_54038"
                                class="Pixso-paragraph-5976_54038 fill-gray80-32_4123-paragraph text-text-smbold-423_3208"
                            >
                                {{ text_5607_120 ?? "Label" }}
                            </p>
                        </slot>
                        <slot name="slot_5976_54039">
                            <InputTextBase
                                id="5976_54039"
                                class="Pixso-instance-5976_54039"
                                Type="Phone Number/Country"
                                Size="md"
                            />
                        </slot>
                    </div>
                </div>
                <slot name="slot_5976_54040" v-if="visible_5607_117">
                    <p
                        id="5976_54040"
                        class="Pixso-paragraph-5976_54040 fill-gray60-83_2722-paragraph text-text-smmedium-5454_21607"
                    >
                        {{ text_5607_123 ?? "This is an input helper text." }}
                    </p>
                </slot>
            </div>
            <div
                id="5976_54041"
                class="Pixso-symbol-5976_54041"
                v-if="
                    State === 'Filled' &&
                    Type === 'Phone Number/Country' &&
                    Size === 'md'
                "
            >
                <div id="5976_54042" class="Pixso-frame-5976_54042">
                    <div class="frame-content-5976_54042">
                        <slot name="slot_5976_54043" v-if="visible_5607_114">
                            <p
                                id="5976_54043"
                                class="Pixso-paragraph-5976_54043 fill-gray80-32_4123-paragraph text-text-smbold-423_3208"
                            >
                                {{ text_5607_120 ?? "Label" }}
                            </p>
                        </slot>
                        <slot name="slot_5976_54044">
                            <InputTextBase
                                id="5976_54044"
                                class="Pixso-instance-5976_54044"
                                Type="Phone Number/Country"
                                Size="md"
                            />
                        </slot>
                    </div>
                </div>
                <slot name="slot_5976_54045" v-if="visible_5607_117">
                    <p
                        id="5976_54045"
                        class="Pixso-paragraph-5976_54045 fill-gray60-83_2722-paragraph text-text-smmedium-5454_21607"
                    >
                        {{ text_5607_123 ?? "This is an input helper text." }}
                    </p>
                </slot>
            </div>
            <div
                id="5976_54046"
                class="Pixso-symbol-5976_54046"
                v-if="
                    State === 'Focused' &&
                    Type === 'Phone Number/Country' &&
                    Size === 'md'
                "
            >
                <div id="5976_54047" class="Pixso-frame-5976_54047">
                    <div class="frame-content-5976_54047">
                        <slot name="slot_5976_54048" v-if="visible_5607_114">
                            <p
                                id="5976_54048"
                                class="Pixso-paragraph-5976_54048 fill-gray80-32_4123-paragraph text-text-smbold-423_3208"
                            >
                                {{ text_5607_120 ?? "Label" }}
                            </p>
                        </slot>
                        <slot name="slot_5976_54049">
                            <InputTextBase
                                id="5976_54049"
                                class="Pixso-instance-5976_54049"
                                Type="Phone Number/Country"
                                Size="md"
                            />
                        </slot>
                    </div>
                </div>
                <slot name="slot_5976_54050" v-if="visible_5607_117">
                    <p
                        id="5976_54050"
                        class="Pixso-paragraph-5976_54050 fill-gray60-83_2722-paragraph text-text-smmedium-5454_21607"
                    >
                        {{ text_5607_123 ?? "This is an input helper text." }}
                    </p>
                </slot>
            </div>
            <div
                id="5976_54051"
                class="Pixso-symbol-5976_54051"
                v-if="
                    State === 'Disabled' &&
                    Type === 'Phone Number/Country' &&
                    Size === 'md'
                "
            >
                <div id="5976_54052" class="Pixso-frame-5976_54052">
                    <div class="frame-content-5976_54052">
                        <slot name="slot_5976_54053" v-if="visible_5607_114">
                            <p
                                id="5976_54053"
                                class="Pixso-paragraph-5976_54053 fill-gray80-32_4123-paragraph text-text-smbold-423_3208"
                            >
                                {{ text_5607_120 ?? "Label" }}
                            </p>
                        </slot>
                        <slot name="slot_5976_54054">
                            <InputTextBase
                                id="5976_54054"
                                class="Pixso-instance-5976_54054"
                                Type="Phone Number/Country"
                                Size="md"
                            />
                        </slot>
                    </div>
                </div>
                <slot name="slot_5976_54055" v-if="visible_5607_117">
                    <p
                        id="5976_54055"
                        class="Pixso-paragraph-5976_54055 fill-gray60-83_2722-paragraph text-text-smmedium-5454_21607"
                    >
                        {{ text_5607_123 ?? "This is an input helper text." }}
                    </p>
                </slot>
            </div>
            <div
                id="5976_54056"
                class="Pixso-symbol-5976_54056"
                v-if="
                    State === 'Error' &&
                    Type === 'Phone Number/Country' &&
                    Size === 'md'
                "
            >
                <div id="5976_54057" class="Pixso-frame-5976_54057">
                    <div class="frame-content-5976_54057">
                        <slot name="slot_5976_54058" v-if="visible_5607_114">
                            <p
                                id="5976_54058"
                                class="Pixso-paragraph-5976_54058 fill-gray80-32_4123-paragraph text-text-smbold-423_3208"
                            >
                                {{ text_5607_120 ?? "Label" }}
                            </p>
                        </slot>
                        <slot name="slot_5976_54059">
                            <InputTextBase
                                id="5976_54059"
                                class="Pixso-instance-5976_54059"
                                Type="Phone Number/Country"
                                Size="md"
                            />
                        </slot>
                    </div>
                </div>
                <slot name="slot_5976_54060" v-if="visible_5607_117">
                    <p
                        id="5976_54060"
                        class="Pixso-paragraph-5976_54060 fill-destructive50-423_3219-paragraph text-text-smmedium-5454_21607"
                    >
                        {{ text_5607_123 ?? "This is an input helper text." }}
                    </p>
                </slot>
            </div>
            <div
                id="5976_54061"
                class="Pixso-symbol-5976_54061"
                v-if="State === 'Default' && Type === 'Number' && Size === 'md'"
            >
                <div id="5976_54062" class="Pixso-frame-5976_54062">
                    <div class="frame-content-5976_54062">
                        <slot name="slot_5976_54063" v-if="visible_5607_114">
                            <p
                                id="5976_54063"
                                class="Pixso-paragraph-5976_54063 fill-gray80-32_4123-paragraph text-text-smbold-423_3208"
                            >
                                {{ text_5607_120 ?? "Label" }}
                            </p>
                        </slot>
                        <slot name="slot_5976_54064">
                            <InputTextBase
                                id="5976_54064"
                                class="Pixso-instance-5976_54064"
                                Type="Number"
                                Size="md"
                            />
                        </slot>
                    </div>
                </div>
                <slot name="slot_5976_54065" v-if="visible_5607_117">
                    <p
                        id="5976_54065"
                        class="Pixso-paragraph-5976_54065 fill-gray60-83_2722-paragraph text-text-smmedium-5454_21607"
                    >
                        {{ text_5607_123 ?? "This is an input helper text." }}
                    </p>
                </slot>
            </div>
            <div
                id="5976_54066"
                class="Pixso-symbol-5976_54066"
                v-if="State === 'Hover' && Type === 'Number' && Size === 'md'"
            >
                <div id="5976_54067" class="Pixso-frame-5976_54067">
                    <div class="frame-content-5976_54067">
                        <slot name="slot_5976_54068" v-if="visible_5607_114">
                            <p
                                id="5976_54068"
                                class="Pixso-paragraph-5976_54068 fill-gray80-32_4123-paragraph text-text-smbold-423_3208"
                            >
                                {{ text_5607_120 ?? "Label" }}
                            </p>
                        </slot>
                        <slot name="slot_5976_54069">
                            <InputTextBase
                                id="5976_54069"
                                class="Pixso-instance-5976_54069"
                                Type="Number"
                                Size="md"
                            />
                        </slot>
                    </div>
                </div>
                <slot name="slot_5976_54070" v-if="visible_5607_117">
                    <p
                        id="5976_54070"
                        class="Pixso-paragraph-5976_54070 fill-gray60-83_2722-paragraph text-text-smmedium-5454_21607"
                    >
                        {{ text_5607_123 ?? "This is an input helper text." }}
                    </p>
                </slot>
            </div>
            <div
                id="5976_54071"
                class="Pixso-symbol-5976_54071"
                v-if="State === 'Filled' && Type === 'Number' && Size === 'md'"
            >
                <div id="5976_54072" class="Pixso-frame-5976_54072">
                    <div class="frame-content-5976_54072">
                        <slot name="slot_5976_54073" v-if="visible_5607_114">
                            <p
                                id="5976_54073"
                                class="Pixso-paragraph-5976_54073 fill-gray80-32_4123-paragraph text-text-smbold-423_3208"
                            >
                                {{ text_5607_120 ?? "Label" }}
                            </p>
                        </slot>
                        <slot name="slot_5976_54074">
                            <InputTextBase
                                id="5976_54074"
                                class="Pixso-instance-5976_54074"
                                Type="Number"
                                Size="md"
                            />
                        </slot>
                    </div>
                </div>
                <slot name="slot_5976_54075" v-if="visible_5607_117">
                    <p
                        id="5976_54075"
                        class="Pixso-paragraph-5976_54075 fill-gray60-83_2722-paragraph text-text-smmedium-5454_21607"
                    >
                        {{ text_5607_123 ?? "This is an input helper text." }}
                    </p>
                </slot>
            </div>
            <div
                id="5976_54076"
                class="Pixso-symbol-5976_54076"
                v-if="State === 'Focused' && Type === 'Number' && Size === 'md'"
            >
                <div id="5976_54077" class="Pixso-frame-5976_54077">
                    <div class="frame-content-5976_54077">
                        <slot name="slot_5976_54078" v-if="visible_5607_114">
                            <p
                                id="5976_54078"
                                class="Pixso-paragraph-5976_54078 fill-gray80-32_4123-paragraph text-text-smbold-423_3208"
                            >
                                {{ text_5607_120 ?? "Label" }}
                            </p>
                        </slot>
                        <slot name="slot_5976_54079">
                            <InputTextBase
                                id="5976_54079"
                                class="Pixso-instance-5976_54079"
                                Type="Number"
                                Size="md"
                            />
                        </slot>
                    </div>
                </div>
                <slot name="slot_5976_54080" v-if="visible_5607_117">
                    <p
                        id="5976_54080"
                        class="Pixso-paragraph-5976_54080 fill-gray60-83_2722-paragraph text-text-smmedium-5454_21607"
                    >
                        {{ text_5607_123 ?? "This is an input helper text." }}
                    </p>
                </slot>
            </div>
            <div
                id="5976_54081"
                class="Pixso-symbol-5976_54081"
                v-if="
                    State === 'Disabled' && Type === 'Number' && Size === 'md'
                "
            >
                <div id="5976_54082" class="Pixso-frame-5976_54082">
                    <div class="frame-content-5976_54082">
                        <slot name="slot_5976_54083" v-if="visible_5607_114">
                            <p
                                id="5976_54083"
                                class="Pixso-paragraph-5976_54083 fill-gray80-32_4123-paragraph text-text-smbold-423_3208"
                            >
                                {{ text_5607_120 ?? "Label" }}
                            </p>
                        </slot>
                        <slot name="slot_5976_54084">
                            <InputTextBase
                                id="5976_54084"
                                class="Pixso-instance-5976_54084"
                                Type="Number"
                                Size="md"
                            />
                        </slot>
                    </div>
                </div>
                <slot name="slot_5976_54085" v-if="visible_5607_117">
                    <p
                        id="5976_54085"
                        class="Pixso-paragraph-5976_54085 fill-gray60-83_2722-paragraph text-text-smmedium-5454_21607"
                    >
                        {{ text_5607_123 ?? "This is an input helper text." }}
                    </p>
                </slot>
            </div>
            <div
                id="5976_54086"
                class="Pixso-symbol-5976_54086"
                v-if="State === 'Error' && Type === 'Number' && Size === 'md'"
            >
                <div id="5976_54087" class="Pixso-frame-5976_54087">
                    <div class="frame-content-5976_54087">
                        <slot name="slot_5976_54088" v-if="visible_5607_114">
                            <p
                                id="5976_54088"
                                class="Pixso-paragraph-5976_54088 fill-gray80-32_4123-paragraph text-text-smbold-423_3208"
                            >
                                {{ text_5607_120 ?? "Label" }}
                            </p>
                        </slot>
                        <slot name="slot_5976_54089">
                            <InputTextBase
                                id="5976_54089"
                                class="Pixso-instance-5976_54089"
                                Type="Number"
                                Size="md"
                            />
                        </slot>
                    </div>
                </div>
                <slot name="slot_5976_54090" v-if="visible_5607_117">
                    <p
                        id="5976_54090"
                        class="Pixso-paragraph-5976_54090 fill-destructive50-423_3219-paragraph text-text-smmedium-5454_21607"
                    >
                        {{ text_5607_123 ?? "This is an input helper text." }}
                    </p>
                </slot>
            </div>
        </div>
    </div>
</template>
<script lang="ts" setup>
import InputTextBase from "@/components/Inputtextbase.vue";
import User from "@/components/User.vue";
import Question from "@/components/Question.vue";
import CopySimple from "@/components/Copysimple.vue";
import CaretDown from "@/components/Caretdown.vue";
import CurrencyDollarSimple from "@/components/Currencydollarsimple.vue";
import CalendarBlank from "@/components/Calendarblank.vue";
import ProgressBarAtom from "@/components/Progressbaratom.vue";
import LockSimple from "@/components/Locksimple.vue";
const props = defineProps({
    visible_5607_114: { type: Boolean, default: true },
    visible_5607_117: { type: Boolean, default: true },
    text_5607_120: { type: String, default: "Label" },
    text_5607_123: { type: String, default: "This is an input helper text." },
    text_5612_49: { type: String, default: "This is a validation text." },
    visible_5612_104: { type: Boolean, default: true },
    visible_5612_159: { type: Boolean, default: true },
    State: { type: String },
    Type: { type: String },
    Size: { type: String }
});
</script>
<style>
.Pixso-symbol-5607_19608 {
}
.Pixso-symbol-5607_19585 {
    width: 320px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 8px;
    align-items: flex-end;
}
.Pixso-frame-5607_19584 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
}
.frame-content-5607_19584 {
    display: flex;
    flex-direction: column;
    gap: 8px;
    align-items: flex-end;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5607_19582 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5607_19554 {
    width: 320px;
    height: 48px;
}
.Pixso-paragraph-5607_19581 {
    width: 100%;
    height: 18px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-symbol-5608_19697 {
    width: 320px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 8px;
    align-items: flex-end;
}
.Pixso-frame-5608_19698 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
}
.frame-content-5608_19698 {
    display: flex;
    flex-direction: column;
    gap: 8px;
    align-items: flex-end;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5608_19699 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5608_19700 {
    width: 320px;
    height: 48px;
}
.Pixso-paragraph-5608_19701 {
    width: 100%;
    height: 18px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-symbol-5607_19609 {
    width: 320px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 8px;
    align-items: flex-end;
}
.Pixso-frame-5607_19610 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
}
.frame-content-5607_19610 {
    display: flex;
    flex-direction: column;
    gap: 8px;
    align-items: flex-end;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5607_19611 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5607_19612 {
    width: 320px;
    height: 48px;
}
.Pixso-paragraph-5607_19613 {
    width: 100%;
    height: 18px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-symbol-5608_19653 {
    width: 320px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 8px;
    align-items: flex-end;
}
.Pixso-frame-5608_19654 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
}
.frame-content-5608_19654 {
    display: flex;
    flex-direction: column;
    gap: 8px;
    align-items: flex-end;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5608_19655 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5608_19656 {
    width: 320px;
    height: 48px;
}
.Pixso-paragraph-5608_19657 {
    width: 100%;
    height: 18px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-symbol-5608_19675 {
    width: 320px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 8px;
    align-items: flex-end;
}
.Pixso-frame-5608_19676 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
}
.frame-content-5608_19676 {
    display: flex;
    flex-direction: column;
    gap: 8px;
    align-items: flex-end;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5608_19677 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5608_19678 {
    width: 320px;
    height: 48px;
}
.Pixso-instance-5606_19068 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5606_19072 {
    width: 20px;
    height: 20px;
}
.Pixso-paragraph-5608_19679 {
    width: 100%;
    height: 18px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-symbol-5609_20111 {
    width: 320px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 8px;
    align-items: flex-end;
}
.Pixso-frame-5609_20112 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
}
.frame-content-5609_20112 {
    display: flex;
    flex-direction: column;
    gap: 8px;
    align-items: flex-end;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5609_20113 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5609_20114 {
    width: 320px;
    height: 48px;
}
.Pixso-paragraph-5609_20115 {
    width: 100%;
    height: 18px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-symbol-5608_19763 {
    width: 320px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 8px;
    align-items: flex-end;
}
.Pixso-frame-5608_19764 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
}
.frame-content-5608_19764 {
    display: flex;
    flex-direction: column;
    gap: 8px;
    align-items: flex-end;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5608_19765 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5608_19766 {
    width: 320px;
    height: 48px;
}
.Pixso-paragraph-5608_19767 {
    width: 100%;
    height: 18px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-symbol-5608_19768 {
    width: 320px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 8px;
    align-items: flex-end;
}
.Pixso-frame-5608_19769 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
}
.frame-content-5608_19769 {
    display: flex;
    flex-direction: column;
    gap: 8px;
    align-items: flex-end;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5608_19770 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5608_19771 {
    width: 320px;
    height: 48px;
}
.Pixso-paragraph-5608_19772 {
    width: 100%;
    height: 18px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-symbol-5608_19773 {
    width: 320px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 8px;
    align-items: flex-end;
}
.Pixso-frame-5608_19774 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
}
.frame-content-5608_19774 {
    display: flex;
    flex-direction: column;
    gap: 8px;
    align-items: flex-end;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5608_19775 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5608_19776 {
    width: 320px;
    height: 48px;
}
.Pixso-paragraph-5608_19777 {
    width: 100%;
    height: 18px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-symbol-5608_19778 {
    width: 320px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 8px;
    align-items: flex-end;
}
.Pixso-frame-5608_19779 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
}
.frame-content-5608_19779 {
    display: flex;
    flex-direction: column;
    gap: 8px;
    align-items: flex-end;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5608_19780 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5608_19781 {
    width: 320px;
    height: 48px;
}
.Pixso-paragraph-5608_19782 {
    width: 100%;
    height: 18px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-symbol-5608_19783 {
    width: 320px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 8px;
    align-items: flex-end;
}
.Pixso-frame-5608_19784 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
}
.frame-content-5608_19784 {
    display: flex;
    flex-direction: column;
    gap: 8px;
    align-items: flex-end;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5608_19785 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5608_19786 {
    width: 320px;
    height: 48px;
}
.Pixso-instance-5606_19157 {
    width: 20px;
    height: 20px;
}
.Pixso-paragraph-5608_19787 {
    width: 100%;
    height: 18px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-symbol-5609_20116 {
    width: 320px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 8px;
    align-items: flex-end;
}
.Pixso-frame-5609_20117 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
}
.frame-content-5609_20117 {
    display: flex;
    flex-direction: column;
    gap: 8px;
    align-items: flex-end;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5609_20118 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5609_20119 {
    width: 320px;
    height: 48px;
}
.Pixso-paragraph-5609_20120 {
    width: 100%;
    height: 18px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-symbol-5608_19953 {
    width: 320px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 8px;
    align-items: flex-end;
}
.Pixso-frame-5608_19954 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
}
.frame-content-5608_19954 {
    display: flex;
    flex-direction: column;
    gap: 8px;
    align-items: flex-end;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5608_19955 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5608_19956 {
    width: 320px;
    height: 48px;
}
.Pixso-paragraph-5608_19957 {
    width: 100%;
    height: 18px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-symbol-5608_19958 {
    width: 320px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 8px;
    align-items: flex-end;
}
.Pixso-frame-5608_19959 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
}
.frame-content-5608_19959 {
    display: flex;
    flex-direction: column;
    gap: 8px;
    align-items: flex-end;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5608_19960 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5608_19961 {
    width: 320px;
    height: 48px;
}
.Pixso-paragraph-5608_19962 {
    width: 100%;
    height: 18px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-symbol-5608_19963 {
    width: 320px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 8px;
    align-items: flex-end;
}
.Pixso-frame-5608_19964 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
}
.frame-content-5608_19964 {
    display: flex;
    flex-direction: column;
    gap: 8px;
    align-items: flex-end;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5608_19965 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5608_19966 {
    width: 320px;
    height: 48px;
}
.Pixso-paragraph-5608_19967 {
    width: 100%;
    height: 18px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-symbol-5608_19968 {
    width: 320px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 8px;
    align-items: flex-end;
}
.Pixso-frame-5608_19969 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
}
.frame-content-5608_19969 {
    display: flex;
    flex-direction: column;
    gap: 8px;
    align-items: flex-end;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5608_19970 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5608_19971 {
    width: 320px;
    height: 48px;
}
.Pixso-paragraph-5608_19972 {
    width: 100%;
    height: 18px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-symbol-5608_19973 {
    width: 320px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 8px;
    align-items: flex-end;
}
.Pixso-frame-5608_19974 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
}
.frame-content-5608_19974 {
    display: flex;
    flex-direction: column;
    gap: 8px;
    align-items: flex-end;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5608_19975 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5608_19976 {
    width: 320px;
    height: 48px;
}
.Pixso-instance-5606_19176 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5606_19174 {
    width: 20px;
    height: 20px;
}
.Pixso-paragraph-5608_19977 {
    width: 100%;
    height: 18px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-symbol-5609_20121 {
    width: 320px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 8px;
    align-items: flex-end;
}
.Pixso-frame-5609_20122 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
}
.frame-content-5609_20122 {
    display: flex;
    flex-direction: column;
    gap: 8px;
    align-items: flex-end;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5609_20123 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5609_20124 {
    width: 320px;
    height: 48px;
}
.Pixso-paragraph-5609_20125 {
    width: 100%;
    height: 18px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-symbol-5609_20232 {
    width: 320px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 8px;
    align-items: flex-end;
}
.Pixso-frame-5609_20233 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
}
.frame-content-5609_20233 {
    display: flex;
    flex-direction: column;
    gap: 8px;
    align-items: flex-end;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5609_20234 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5609_20235 {
    width: 320px;
    height: 48px;
}
.Pixso-paragraph-5609_20236 {
    width: 100%;
    height: 18px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-symbol-5609_20242 {
    width: 320px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 8px;
    align-items: flex-end;
}
.Pixso-frame-5609_20243 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
}
.frame-content-5609_20243 {
    display: flex;
    flex-direction: column;
    gap: 8px;
    align-items: flex-end;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5609_20244 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5609_20245 {
    width: 320px;
    height: 48px;
}
.Pixso-paragraph-5609_20246 {
    width: 100%;
    height: 18px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-symbol-5609_20247 {
    width: 320px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 8px;
    align-items: flex-end;
}
.Pixso-frame-5609_20248 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
}
.frame-content-5609_20248 {
    display: flex;
    flex-direction: column;
    gap: 8px;
    align-items: flex-end;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5609_20249 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5609_20250 {
    width: 320px;
    height: 48px;
}
.Pixso-paragraph-5609_20251 {
    width: 100%;
    height: 18px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-symbol-5609_20252 {
    width: 320px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 8px;
    align-items: flex-end;
}
.Pixso-frame-5609_20253 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
}
.frame-content-5609_20253 {
    display: flex;
    flex-direction: column;
    gap: 8px;
    align-items: flex-end;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5609_20254 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5609_20255 {
    width: 320px;
    height: 48px;
}
.Pixso-paragraph-5609_20256 {
    width: 100%;
    height: 18px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-symbol-5609_20257 {
    width: 320px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 8px;
    align-items: flex-end;
}
.Pixso-frame-5609_20258 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
}
.frame-content-5609_20258 {
    display: flex;
    flex-direction: column;
    gap: 8px;
    align-items: flex-end;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5609_20259 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5609_20260 {
    width: 320px;
    height: 48px;
}
.Pixso-paragraph-5609_20261 {
    width: 100%;
    height: 18px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-symbol-5609_20237 {
    width: 320px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 8px;
    align-items: flex-end;
}
.Pixso-frame-5609_20238 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
}
.frame-content-5609_20238 {
    display: flex;
    flex-direction: column;
    gap: 8px;
    align-items: flex-end;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5609_20239 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5609_20240 {
    width: 320px;
    height: 48px;
}
.Pixso-paragraph-5609_20241 {
    width: 100%;
    height: 18px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-symbol-5609_20496 {
    width: 320px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 8px;
    align-items: flex-end;
}
.Pixso-frame-5609_20497 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
}
.frame-content-5609_20497 {
    display: flex;
    flex-direction: column;
    gap: 8px;
    align-items: flex-end;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5609_20498 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5609_20499 {
    width: 320px;
    height: 48px;
}
.Pixso-paragraph-5609_20500 {
    width: 100%;
    height: 18px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-symbol-5609_20506 {
    width: 320px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 8px;
    align-items: flex-end;
}
.Pixso-frame-5609_20507 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
}
.frame-content-5609_20507 {
    display: flex;
    flex-direction: column;
    gap: 8px;
    align-items: flex-end;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5609_20508 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5609_20509 {
    width: 320px;
    height: 48px;
}
.Pixso-paragraph-5609_20510 {
    width: 100%;
    height: 18px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-symbol-5609_20511 {
    width: 320px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 8px;
    align-items: flex-end;
}
.Pixso-frame-5609_20512 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
}
.frame-content-5609_20512 {
    display: flex;
    flex-direction: column;
    gap: 8px;
    align-items: flex-end;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5609_20513 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5609_20514 {
    width: 320px;
    height: 48px;
}
.Pixso-paragraph-5609_20515 {
    width: 100%;
    height: 18px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-symbol-5609_20516 {
    width: 320px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 8px;
    align-items: flex-end;
}
.Pixso-frame-5609_20517 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
}
.frame-content-5609_20517 {
    display: flex;
    flex-direction: column;
    gap: 8px;
    align-items: flex-end;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5609_20518 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5609_20519 {
    width: 320px;
    height: 48px;
}
.Pixso-paragraph-5609_20520 {
    width: 100%;
    height: 18px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-symbol-5609_20521 {
    width: 320px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 8px;
    align-items: flex-end;
}
.Pixso-frame-5609_20522 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
}
.frame-content-5609_20522 {
    display: flex;
    flex-direction: column;
    gap: 8px;
    align-items: flex-end;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5609_20523 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5609_20524 {
    width: 320px;
    height: 48px;
}
.Pixso-instance-5607_19365 {
    width: 20px;
    height: 20px;
}
.Pixso-paragraph-5609_20525 {
    width: 100%;
    height: 18px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-symbol-5609_20501 {
    width: 320px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 8px;
    align-items: flex-end;
}
.Pixso-frame-5609_20502 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
}
.frame-content-5609_20502 {
    display: flex;
    flex-direction: column;
    gap: 8px;
    align-items: flex-end;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5609_20503 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5609_20504 {
    width: 320px;
    height: 48px;
}
.Pixso-paragraph-5609_20505 {
    width: 100%;
    height: 18px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-symbol-5609_20658 {
    width: 320px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 8px;
    align-items: flex-end;
}
.Pixso-frame-5609_20659 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
}
.frame-content-5609_20659 {
    display: flex;
    flex-direction: column;
    gap: 8px;
    align-items: flex-end;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5609_20660 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5609_20661 {
    width: 320px;
    height: 48px;
}
.Pixso-paragraph-5609_20662 {
    width: 100%;
    height: 18px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-symbol-5609_20668 {
    width: 320px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 8px;
    align-items: flex-end;
}
.Pixso-frame-5609_20669 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
}
.frame-content-5609_20669 {
    display: flex;
    flex-direction: column;
    gap: 8px;
    align-items: flex-end;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5609_20670 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5609_20671 {
    width: 320px;
    height: 48px;
}
.Pixso-paragraph-5609_20672 {
    width: 100%;
    height: 18px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-symbol-5609_20673 {
    width: 320px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 8px;
    align-items: flex-end;
}
.Pixso-frame-5609_20674 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
}
.frame-content-5609_20674 {
    display: flex;
    flex-direction: column;
    gap: 8px;
    align-items: flex-end;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5609_20675 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5609_20676 {
    width: 320px;
    height: 48px;
}
.Pixso-paragraph-5609_20677 {
    width: 100%;
    height: 18px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-symbol-5609_20678 {
    width: 320px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 8px;
    align-items: flex-end;
}
.Pixso-frame-5609_20679 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
}
.frame-content-5609_20679 {
    display: flex;
    flex-direction: column;
    gap: 8px;
    align-items: flex-end;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5609_20680 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5609_20681 {
    width: 320px;
    height: 48px;
}
.Pixso-paragraph-5609_20682 {
    width: 100%;
    height: 18px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-symbol-5609_20683 {
    width: 320px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 8px;
    align-items: flex-end;
}
.Pixso-frame-5609_20684 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
}
.frame-content-5609_20684 {
    display: flex;
    flex-direction: column;
    gap: 8px;
    align-items: flex-end;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5609_20685 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5609_20686 {
    width: 320px;
    height: 48px;
}
.Pixso-paragraph-5609_20687 {
    width: 100%;
    height: 18px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-symbol-5609_20663 {
    width: 320px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 8px;
    align-items: flex-end;
}
.Pixso-frame-5609_20664 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
}
.frame-content-5609_20664 {
    display: flex;
    flex-direction: column;
    gap: 8px;
    align-items: flex-end;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5609_20665 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5609_20666 {
    width: 320px;
    height: 48px;
}
.Pixso-paragraph-5609_20667 {
    width: 100%;
    height: 18px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-symbol-5609_20808 {
    width: 320px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 8px;
    align-items: flex-end;
}
.Pixso-frame-5609_20809 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
}
.frame-content-5609_20809 {
    display: flex;
    flex-direction: column;
    gap: 8px;
    align-items: flex-end;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5609_20810 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5609_20811 {
    width: 320px;
    height: 48px;
}
.Pixso-frame-5612_2169 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    justify-content: flex-end;
    align-items: flex-start;
}
.frame-content-5612_2169 {
    display: flex;
    flex-direction: row;
    gap: 4px;
    align-items: flex-start;
    justify-content: flex-end;
    width: 100%;
    position: relative;
}
.Pixso-instance-5612_2159 {
    width: 77px;
    height: 4px;
}
.Pixso-instance-5612_2166 {
    width: 77px;
    height: 4px;
}
.Pixso-instance-5612_2167 {
    width: 77px;
    height: 4px;
}
.Pixso-instance-5612_2168 {
    width: 77px;
    height: 4px;
}
.Pixso-paragraph-5609_20812 {
    width: 100%;
    height: 18px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-symbol-5609_20818 {
    width: 320px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 8px;
    align-items: flex-end;
}
.Pixso-frame-5609_20819 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
}
.frame-content-5609_20819 {
    display: flex;
    flex-direction: column;
    gap: 8px;
    align-items: flex-end;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5609_20820 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5609_20821 {
    width: 320px;
    height: 48px;
}
.Pixso-frame-5612_2170 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    justify-content: flex-end;
    align-items: flex-start;
}
.frame-content-5612_2170 {
    display: flex;
    flex-direction: row;
    gap: 4px;
    align-items: flex-start;
    justify-content: flex-end;
    width: 100%;
    position: relative;
}
.Pixso-instance-5612_2171 {
    width: 77px;
    height: 4px;
}
.Pixso-instance-5612_2172 {
    width: 77px;
    height: 4px;
}
.Pixso-instance-5612_2173 {
    width: 77px;
    height: 4px;
}
.Pixso-instance-5612_2174 {
    width: 77px;
    height: 4px;
}
.Pixso-paragraph-5609_20822 {
    width: 100%;
    height: 18px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-symbol-5609_20823 {
    width: 320px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 8px;
    align-items: flex-end;
}
.Pixso-frame-5609_20824 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
}
.frame-content-5609_20824 {
    display: flex;
    flex-direction: column;
    gap: 8px;
    align-items: flex-end;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5609_20825 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5609_20826 {
    width: 320px;
    height: 48px;
}
.Pixso-frame-5612_2175 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    justify-content: flex-end;
    align-items: flex-start;
}
.frame-content-5612_2175 {
    display: flex;
    flex-direction: row;
    gap: 4px;
    align-items: flex-start;
    justify-content: flex-end;
    width: 100%;
    position: relative;
}
.Pixso-instance-5612_2176 {
    width: 77px;
    height: 4px;
}
.Pixso-instance-5612_2177 {
    width: 77px;
    height: 4px;
}
.Pixso-instance-5612_2178 {
    width: 77px;
    height: 4px;
}
.Pixso-instance-5612_2179 {
    width: 77px;
    height: 4px;
}
.Pixso-paragraph-5609_20827 {
    width: 100%;
    height: 18px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-symbol-5609_20828 {
    width: 320px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 8px;
    align-items: flex-end;
}
.Pixso-frame-5609_20829 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
}
.frame-content-5609_20829 {
    display: flex;
    flex-direction: column;
    gap: 8px;
    align-items: flex-end;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5609_20830 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5609_20831 {
    width: 320px;
    height: 48px;
}
.Pixso-frame-5612_2180 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    justify-content: flex-end;
    align-items: flex-start;
}
.frame-content-5612_2180 {
    display: flex;
    flex-direction: row;
    gap: 4px;
    align-items: flex-start;
    justify-content: flex-end;
    width: 100%;
    position: relative;
}
.Pixso-instance-5612_2181 {
    width: 77px;
    height: 4px;
}
.Pixso-instance-5612_2182 {
    width: 77px;
    height: 4px;
}
.Pixso-instance-5612_2183 {
    width: 77px;
    height: 4px;
}
.Pixso-instance-5612_2184 {
    width: 77px;
    height: 4px;
}
.Pixso-paragraph-5609_20832 {
    width: 100%;
    height: 18px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-symbol-5609_20833 {
    width: 320px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 8px;
    align-items: flex-end;
}
.Pixso-frame-5609_20834 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
}
.frame-content-5609_20834 {
    display: flex;
    flex-direction: column;
    gap: 8px;
    align-items: flex-end;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5609_20835 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5609_20836 {
    width: 320px;
    height: 48px;
}
.Pixso-instance-5607_19417 {
    width: 20px;
    height: 20px;
}
.Pixso-frame-5612_2185 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    justify-content: flex-end;
    align-items: flex-start;
}
.frame-content-5612_2185 {
    display: flex;
    flex-direction: row;
    gap: 4px;
    align-items: flex-start;
    justify-content: flex-end;
    width: 100%;
    position: relative;
}
.Pixso-instance-5612_2186 {
    width: 77px;
    height: 4px;
}
.Pixso-instance-5612_2187 {
    width: 77px;
    height: 4px;
}
.Pixso-instance-5612_2188 {
    width: 77px;
    height: 4px;
}
.Pixso-instance-5612_2189 {
    width: 77px;
    height: 4px;
}
.Pixso-paragraph-5609_20837 {
    width: 100%;
    height: 18px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-symbol-5609_20813 {
    width: 320px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 8px;
    align-items: flex-end;
}
.Pixso-frame-5609_20814 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
}
.frame-content-5609_20814 {
    display: flex;
    flex-direction: column;
    gap: 8px;
    align-items: flex-end;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5609_20815 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5609_20816 {
    width: 320px;
    height: 48px;
}
.Pixso-frame-5612_2190 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    justify-content: flex-end;
    align-items: flex-start;
}
.frame-content-5612_2190 {
    display: flex;
    flex-direction: row;
    gap: 4px;
    align-items: flex-start;
    justify-content: flex-end;
    width: 100%;
    position: relative;
}
.Pixso-instance-5612_2191 {
    width: 77px;
    height: 4px;
}
.Pixso-instance-5612_2192 {
    width: 77px;
    height: 4px;
}
.Pixso-instance-5612_2193 {
    width: 77px;
    height: 4px;
}
.Pixso-instance-5612_2194 {
    width: 77px;
    height: 4px;
}
.Pixso-paragraph-5609_20817 {
    width: 100%;
    height: 18px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-symbol-5609_21048 {
    width: 320px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 8px;
    align-items: flex-end;
}
.Pixso-frame-5609_21049 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
}
.frame-content-5609_21049 {
    display: flex;
    flex-direction: column;
    gap: 8px;
    align-items: flex-end;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5609_21050 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5609_21051 {
    width: 320px;
    height: 48px;
}
.Pixso-paragraph-5609_21052 {
    width: 100%;
    height: 18px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-symbol-5609_21058 {
    width: 320px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 8px;
    align-items: flex-end;
}
.Pixso-frame-5609_21059 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
}
.frame-content-5609_21059 {
    display: flex;
    flex-direction: column;
    gap: 8px;
    align-items: flex-end;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5609_21060 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5609_21061 {
    width: 320px;
    height: 48px;
}
.Pixso-paragraph-5609_21062 {
    width: 100%;
    height: 18px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-symbol-5609_21063 {
    width: 320px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 8px;
    align-items: flex-end;
}
.Pixso-frame-5609_21064 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
}
.frame-content-5609_21064 {
    display: flex;
    flex-direction: column;
    gap: 8px;
    align-items: flex-end;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5609_21065 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5609_21066 {
    width: 320px;
    height: 48px;
}
.Pixso-paragraph-5609_21067 {
    width: 100%;
    height: 18px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-symbol-5609_21068 {
    width: 320px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 8px;
    align-items: flex-end;
}
.Pixso-frame-5609_21069 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
}
.frame-content-5609_21069 {
    display: flex;
    flex-direction: column;
    gap: 8px;
    align-items: flex-end;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5609_21070 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5609_21071 {
    width: 320px;
    height: 48px;
}
.Pixso-paragraph-5609_21072 {
    width: 100%;
    height: 18px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-symbol-5609_21073 {
    width: 320px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 8px;
    align-items: flex-end;
}
.Pixso-frame-5609_21074 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
}
.frame-content-5609_21074 {
    display: flex;
    flex-direction: column;
    gap: 8px;
    align-items: flex-end;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5609_21075 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5609_21076 {
    width: 320px;
    height: 48px;
}
.Pixso-paragraph-5609_21077 {
    width: 100%;
    height: 18px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-symbol-5609_21053 {
    width: 320px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 8px;
    align-items: flex-end;
}
.Pixso-frame-5609_21054 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
}
.frame-content-5609_21054 {
    display: flex;
    flex-direction: column;
    gap: 8px;
    align-items: flex-end;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5609_21055 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5609_21056 {
    width: 320px;
    height: 48px;
}
.Pixso-paragraph-5609_21057 {
    width: 100%;
    height: 18px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-symbol-5609_22109 {
    width: 320px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 8px;
    align-items: flex-end;
}
.Pixso-frame-5609_22110 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
}
.frame-content-5609_22110 {
    display: flex;
    flex-direction: column;
    gap: 8px;
    align-items: flex-end;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5609_22111 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5609_22112 {
    width: 320px;
    height: 48px;
}
.Pixso-paragraph-5609_22113 {
    width: 100%;
    height: 18px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-symbol-5609_22114 {
    width: 320px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 8px;
    align-items: flex-end;
}
.Pixso-frame-5609_22115 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
}
.frame-content-5609_22115 {
    display: flex;
    flex-direction: column;
    gap: 8px;
    align-items: flex-end;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5609_22116 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5609_22117 {
    width: 320px;
    height: 48px;
}
.Pixso-paragraph-5609_22118 {
    width: 100%;
    height: 18px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-symbol-5609_22119 {
    width: 320px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 8px;
    align-items: flex-end;
}
.Pixso-frame-5609_22120 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
}
.frame-content-5609_22120 {
    display: flex;
    flex-direction: column;
    gap: 8px;
    align-items: flex-end;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5609_22121 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5609_22122 {
    width: 320px;
    height: 48px;
}
.Pixso-paragraph-5609_22123 {
    width: 100%;
    height: 18px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-symbol-5609_22124 {
    width: 320px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 8px;
    align-items: flex-end;
}
.Pixso-frame-5609_22125 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
}
.frame-content-5609_22125 {
    display: flex;
    flex-direction: column;
    gap: 8px;
    align-items: flex-end;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5609_22126 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5609_22127 {
    width: 320px;
    height: 48px;
}
.Pixso-paragraph-5609_22128 {
    width: 100%;
    height: 18px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-symbol-5609_22129 {
    width: 320px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 8px;
    align-items: flex-end;
}
.Pixso-frame-5609_22130 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
}
.frame-content-5609_22130 {
    display: flex;
    flex-direction: column;
    gap: 8px;
    align-items: flex-end;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5609_22131 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5609_22132 {
    width: 320px;
    height: 48px;
}
.Pixso-paragraph-5609_22133 {
    width: 100%;
    height: 18px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-symbol-5609_22134 {
    width: 320px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 8px;
    align-items: flex-end;
}
.Pixso-frame-5609_22135 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
}
.frame-content-5609_22135 {
    display: flex;
    flex-direction: column;
    gap: 8px;
    align-items: flex-end;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5609_22136 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5609_22137 {
    width: 320px;
    height: 48px;
}
.Pixso-paragraph-5609_22138 {
    width: 100%;
    height: 18px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-symbol-5976_53791 {
    width: 320px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 6px;
    align-items: flex-end;
}
.Pixso-frame-5976_53792 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
}
.frame-content-5976_53792 {
    display: flex;
    flex-direction: column;
    gap: 6px;
    align-items: flex-end;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5976_53793 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5976_53794 {
    width: 320px;
    height: 40px;
}
.Pixso-paragraph-5976_53795 {
    width: 100%;
    height: 18px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-symbol-5976_53796 {
    width: 320px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 6px;
    align-items: flex-end;
}
.Pixso-frame-5976_53797 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
}
.frame-content-5976_53797 {
    display: flex;
    flex-direction: column;
    gap: 6px;
    align-items: flex-end;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5976_53798 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5976_53799 {
    width: 320px;
    height: 40px;
}
.Pixso-paragraph-5976_53800 {
    width: 100%;
    height: 18px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-symbol-5976_53801 {
    width: 320px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 6px;
    align-items: flex-end;
}
.Pixso-frame-5976_53802 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
}
.frame-content-5976_53802 {
    display: flex;
    flex-direction: column;
    gap: 6px;
    align-items: flex-end;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5976_53803 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5976_53804 {
    width: 320px;
    height: 40px;
}
.Pixso-paragraph-5976_53805 {
    width: 100%;
    height: 18px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-symbol-5976_53806 {
    width: 320px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 6px;
    align-items: flex-end;
}
.Pixso-frame-5976_53807 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
}
.frame-content-5976_53807 {
    display: flex;
    flex-direction: column;
    gap: 6px;
    align-items: flex-end;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5976_53808 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5976_53809 {
    width: 320px;
    height: 40px;
}
.Pixso-paragraph-5976_53810 {
    width: 100%;
    height: 18px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-symbol-5976_53811 {
    width: 320px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 6px;
    align-items: flex-end;
}
.Pixso-frame-5976_53812 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
}
.frame-content-5976_53812 {
    display: flex;
    flex-direction: column;
    gap: 6px;
    align-items: flex-end;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5976_53813 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5976_53814 {
    width: 320px;
    height: 40px;
}
.Pixso-instance-5976_52049 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5976_52051 {
    width: 20px;
    height: 20px;
}
.Pixso-paragraph-5976_53815 {
    width: 100%;
    height: 18px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-symbol-5976_53816 {
    width: 320px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 6px;
    align-items: flex-end;
}
.Pixso-frame-5976_53817 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
}
.frame-content-5976_53817 {
    display: flex;
    flex-direction: column;
    gap: 6px;
    align-items: flex-end;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5976_53818 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5976_53819 {
    width: 320px;
    height: 40px;
}
.Pixso-paragraph-5976_53820 {
    width: 100%;
    height: 18px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-symbol-5976_53821 {
    width: 320px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 6px;
    align-items: flex-end;
}
.Pixso-frame-5976_53822 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
}
.frame-content-5976_53822 {
    display: flex;
    flex-direction: column;
    gap: 6px;
    align-items: flex-end;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5976_53823 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5976_53824 {
    width: 320px;
    height: 40px;
}
.Pixso-paragraph-5976_53825 {
    width: 100%;
    height: 18px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-symbol-5976_53826 {
    width: 320px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 6px;
    align-items: flex-end;
}
.Pixso-frame-5976_53827 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
}
.frame-content-5976_53827 {
    display: flex;
    flex-direction: column;
    gap: 6px;
    align-items: flex-end;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5976_53828 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5976_53829 {
    width: 320px;
    height: 40px;
}
.Pixso-paragraph-5976_53830 {
    width: 100%;
    height: 18px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-symbol-5976_53831 {
    width: 320px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 6px;
    align-items: flex-end;
}
.Pixso-frame-5976_53832 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
}
.frame-content-5976_53832 {
    display: flex;
    flex-direction: column;
    gap: 6px;
    align-items: flex-end;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5976_53833 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5976_53834 {
    width: 320px;
    height: 40px;
}
.Pixso-paragraph-5976_53835 {
    width: 100%;
    height: 18px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-symbol-5976_53836 {
    width: 320px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 6px;
    align-items: flex-end;
}
.Pixso-frame-5976_53837 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
}
.frame-content-5976_53837 {
    display: flex;
    flex-direction: column;
    gap: 6px;
    align-items: flex-end;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5976_53838 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5976_53839 {
    width: 320px;
    height: 40px;
}
.Pixso-paragraph-5976_53840 {
    width: 100%;
    height: 18px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-symbol-5976_53841 {
    width: 320px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 6px;
    align-items: flex-end;
}
.Pixso-frame-5976_53842 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
}
.frame-content-5976_53842 {
    display: flex;
    flex-direction: column;
    gap: 6px;
    align-items: flex-end;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5976_53843 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5976_53844 {
    width: 320px;
    height: 40px;
}
.Pixso-instance-5976_52057 {
    width: 20px;
    height: 20px;
}
.Pixso-paragraph-5976_53845 {
    width: 100%;
    height: 18px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-symbol-5976_53846 {
    width: 320px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 6px;
    align-items: flex-end;
}
.Pixso-frame-5976_53847 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
}
.frame-content-5976_53847 {
    display: flex;
    flex-direction: column;
    gap: 6px;
    align-items: flex-end;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5976_53848 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5976_53849 {
    width: 320px;
    height: 40px;
}
.Pixso-paragraph-5976_53850 {
    width: 100%;
    height: 18px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-symbol-5976_53851 {
    width: 320px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 6px;
    align-items: flex-end;
}
.Pixso-frame-5976_53852 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
}
.frame-content-5976_53852 {
    display: flex;
    flex-direction: column;
    gap: 6px;
    align-items: flex-end;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5976_53853 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5976_53854 {
    width: 320px;
    height: 40px;
}
.Pixso-paragraph-5976_53855 {
    width: 100%;
    height: 18px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-symbol-5976_53856 {
    width: 320px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 6px;
    align-items: flex-end;
}
.Pixso-frame-5976_53857 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
}
.frame-content-5976_53857 {
    display: flex;
    flex-direction: column;
    gap: 6px;
    align-items: flex-end;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5976_53858 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5976_53859 {
    width: 320px;
    height: 40px;
}
.Pixso-paragraph-5976_53860 {
    width: 100%;
    height: 18px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-symbol-5976_53861 {
    width: 320px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 6px;
    align-items: flex-end;
}
.Pixso-frame-5976_53862 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
}
.frame-content-5976_53862 {
    display: flex;
    flex-direction: column;
    gap: 6px;
    align-items: flex-end;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5976_53863 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5976_53864 {
    width: 320px;
    height: 40px;
}
.Pixso-paragraph-5976_53865 {
    width: 100%;
    height: 18px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-symbol-5976_53866 {
    width: 320px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 6px;
    align-items: flex-end;
}
.Pixso-frame-5976_53867 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
}
.frame-content-5976_53867 {
    display: flex;
    flex-direction: column;
    gap: 6px;
    align-items: flex-end;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5976_53868 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5976_53869 {
    width: 320px;
    height: 40px;
}
.Pixso-paragraph-5976_53870 {
    width: 100%;
    height: 18px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-symbol-5976_53871 {
    width: 320px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 6px;
    align-items: flex-end;
}
.Pixso-frame-5976_53872 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
}
.frame-content-5976_53872 {
    display: flex;
    flex-direction: column;
    gap: 6px;
    align-items: flex-end;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5976_53873 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5976_53874 {
    width: 320px;
    height: 40px;
}
.Pixso-instance-5976_52065 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5976_52060 {
    width: 20px;
    height: 20px;
}
.Pixso-paragraph-5976_53875 {
    width: 100%;
    height: 18px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-symbol-5976_53876 {
    width: 320px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 6px;
    align-items: flex-end;
}
.Pixso-frame-5976_53877 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
}
.frame-content-5976_53877 {
    display: flex;
    flex-direction: column;
    gap: 6px;
    align-items: flex-end;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5976_53878 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5976_53879 {
    width: 320px;
    height: 40px;
}
.Pixso-paragraph-5976_53880 {
    width: 100%;
    height: 18px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-symbol-5976_53881 {
    width: 320px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 6px;
    align-items: flex-end;
}
.Pixso-frame-5976_53882 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
}
.frame-content-5976_53882 {
    display: flex;
    flex-direction: column;
    gap: 6px;
    align-items: flex-end;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5976_53883 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5976_53884 {
    width: 320px;
    height: 40px;
}
.Pixso-paragraph-5976_53885 {
    width: 100%;
    height: 18px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-symbol-5976_53886 {
    width: 320px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 6px;
    align-items: flex-end;
}
.Pixso-frame-5976_53887 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
}
.frame-content-5976_53887 {
    display: flex;
    flex-direction: column;
    gap: 6px;
    align-items: flex-end;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5976_53888 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5976_53889 {
    width: 320px;
    height: 40px;
}
.Pixso-paragraph-5976_53890 {
    width: 100%;
    height: 18px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-symbol-5976_53891 {
    width: 320px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 6px;
    align-items: flex-end;
}
.Pixso-frame-5976_53892 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
}
.frame-content-5976_53892 {
    display: flex;
    flex-direction: column;
    gap: 6px;
    align-items: flex-end;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5976_53893 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5976_53894 {
    width: 320px;
    height: 40px;
}
.Pixso-paragraph-5976_53895 {
    width: 100%;
    height: 18px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-symbol-5976_53896 {
    width: 320px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 6px;
    align-items: flex-end;
}
.Pixso-frame-5976_53897 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
}
.frame-content-5976_53897 {
    display: flex;
    flex-direction: column;
    gap: 6px;
    align-items: flex-end;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5976_53898 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5976_53899 {
    width: 320px;
    height: 40px;
}
.Pixso-paragraph-5976_53900 {
    width: 100%;
    height: 18px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-symbol-5976_53901 {
    width: 320px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 6px;
    align-items: flex-end;
}
.Pixso-frame-5976_53902 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
}
.frame-content-5976_53902 {
    display: flex;
    flex-direction: column;
    gap: 6px;
    align-items: flex-end;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5976_53903 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5976_53904 {
    width: 320px;
    height: 40px;
}
.Pixso-paragraph-5976_53905 {
    width: 100%;
    height: 18px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-symbol-5976_53906 {
    width: 320px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 6px;
    align-items: flex-end;
}
.Pixso-frame-5976_53907 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
}
.frame-content-5976_53907 {
    display: flex;
    flex-direction: column;
    gap: 6px;
    align-items: flex-end;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5976_53908 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5976_53909 {
    width: 320px;
    height: 40px;
}
.Pixso-paragraph-5976_53910 {
    width: 100%;
    height: 18px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-symbol-5976_53911 {
    width: 320px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 6px;
    align-items: flex-end;
}
.Pixso-frame-5976_53912 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
}
.frame-content-5976_53912 {
    display: flex;
    flex-direction: column;
    gap: 6px;
    align-items: flex-end;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5976_53913 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5976_53914 {
    width: 320px;
    height: 40px;
}
.Pixso-paragraph-5976_53915 {
    width: 100%;
    height: 18px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-symbol-5976_53916 {
    width: 320px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 6px;
    align-items: flex-end;
}
.Pixso-frame-5976_53917 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
}
.frame-content-5976_53917 {
    display: flex;
    flex-direction: column;
    gap: 6px;
    align-items: flex-end;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5976_53918 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5976_53919 {
    width: 320px;
    height: 40px;
}
.Pixso-paragraph-5976_53920 {
    width: 100%;
    height: 18px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-symbol-5976_53921 {
    width: 320px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 6px;
    align-items: flex-end;
}
.Pixso-frame-5976_53922 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
}
.frame-content-5976_53922 {
    display: flex;
    flex-direction: column;
    gap: 6px;
    align-items: flex-end;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5976_53923 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5976_53924 {
    width: 320px;
    height: 40px;
}
.Pixso-paragraph-5976_53925 {
    width: 100%;
    height: 18px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-symbol-5976_53926 {
    width: 320px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 6px;
    align-items: flex-end;
}
.Pixso-frame-5976_53927 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
}
.frame-content-5976_53927 {
    display: flex;
    flex-direction: column;
    gap: 6px;
    align-items: flex-end;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5976_53928 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5976_53929 {
    width: 320px;
    height: 40px;
}
.Pixso-paragraph-5976_53930 {
    width: 100%;
    height: 18px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-symbol-5976_53931 {
    width: 320px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 6px;
    align-items: flex-end;
}
.Pixso-frame-5976_53932 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
}
.frame-content-5976_53932 {
    display: flex;
    flex-direction: column;
    gap: 6px;
    align-items: flex-end;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5976_53933 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5976_53934 {
    width: 320px;
    height: 40px;
}
.Pixso-instance-5976_52073 {
    width: 20px;
    height: 20px;
}
.Pixso-paragraph-5976_53935 {
    width: 100%;
    height: 18px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-symbol-5976_53936 {
    width: 320px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 6px;
    align-items: flex-end;
}
.Pixso-frame-5976_53937 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
}
.frame-content-5976_53937 {
    display: flex;
    flex-direction: column;
    gap: 6px;
    align-items: flex-end;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5976_53938 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5976_53939 {
    width: 320px;
    height: 40px;
}
.Pixso-paragraph-5976_53940 {
    width: 100%;
    height: 18px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-symbol-5976_53941 {
    width: 320px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 6px;
    align-items: flex-end;
}
.Pixso-frame-5976_53942 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
}
.frame-content-5976_53942 {
    display: flex;
    flex-direction: column;
    gap: 6px;
    align-items: flex-end;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5976_53943 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5976_53944 {
    width: 320px;
    height: 40px;
}
.Pixso-paragraph-5976_53945 {
    width: 100%;
    height: 18px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-symbol-5976_53946 {
    width: 320px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 6px;
    align-items: flex-end;
}
.Pixso-frame-5976_53947 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
}
.frame-content-5976_53947 {
    display: flex;
    flex-direction: column;
    gap: 6px;
    align-items: flex-end;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5976_53948 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5976_53949 {
    width: 320px;
    height: 40px;
}
.Pixso-paragraph-5976_53950 {
    width: 100%;
    height: 18px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-symbol-5976_53951 {
    width: 320px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 6px;
    align-items: flex-end;
}
.Pixso-frame-5976_53952 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
}
.frame-content-5976_53952 {
    display: flex;
    flex-direction: column;
    gap: 6px;
    align-items: flex-end;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5976_53953 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5976_53954 {
    width: 320px;
    height: 40px;
}
.Pixso-paragraph-5976_53955 {
    width: 100%;
    height: 18px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-symbol-5976_53956 {
    width: 320px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 6px;
    align-items: flex-end;
}
.Pixso-frame-5976_53957 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
}
.frame-content-5976_53957 {
    display: flex;
    flex-direction: column;
    gap: 6px;
    align-items: flex-end;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5976_53958 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5976_53959 {
    width: 320px;
    height: 40px;
}
.Pixso-paragraph-5976_53960 {
    width: 100%;
    height: 18px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-symbol-5976_53961 {
    width: 320px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 6px;
    align-items: flex-end;
}
.Pixso-frame-5976_53962 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
}
.frame-content-5976_53962 {
    display: flex;
    flex-direction: column;
    gap: 6px;
    align-items: flex-end;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5976_53963 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5976_53964 {
    width: 320px;
    height: 40px;
}
.Pixso-paragraph-5976_53965 {
    width: 100%;
    height: 18px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-symbol-5976_53966 {
    width: 320px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 6px;
    align-items: flex-end;
}
.Pixso-frame-5976_53967 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
}
.frame-content-5976_53967 {
    display: flex;
    flex-direction: column;
    gap: 6px;
    align-items: flex-end;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5976_53968 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5976_53969 {
    width: 320px;
    height: 40px;
}
.Pixso-paragraph-5976_53970 {
    width: 100%;
    height: 18px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-symbol-5976_53971 {
    width: 320px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 6px;
    align-items: flex-end;
}
.Pixso-frame-5976_53972 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
}
.frame-content-5976_53972 {
    display: flex;
    flex-direction: column;
    gap: 6px;
    align-items: flex-end;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5976_53973 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5976_53974 {
    width: 320px;
    height: 40px;
}
.Pixso-frame-5976_53975 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    justify-content: flex-end;
    align-items: flex-start;
}
.frame-content-5976_53975 {
    display: flex;
    flex-direction: row;
    gap: 4px;
    align-items: flex-start;
    justify-content: flex-end;
    width: 100%;
    position: relative;
}
.Pixso-instance-5976_53976 {
    width: 77px;
    height: 4px;
}
.Pixso-instance-5976_53977 {
    width: 77px;
    height: 4px;
}
.Pixso-instance-5976_53978 {
    width: 77px;
    height: 4px;
}
.Pixso-instance-5976_53979 {
    width: 77px;
    height: 4px;
}
.Pixso-paragraph-5976_53980 {
    width: 100%;
    height: 18px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-symbol-5976_53981 {
    width: 320px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 6px;
    align-items: flex-end;
}
.Pixso-frame-5976_53982 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
}
.frame-content-5976_53982 {
    display: flex;
    flex-direction: column;
    gap: 6px;
    align-items: flex-end;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5976_53983 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5976_53984 {
    width: 320px;
    height: 40px;
}
.Pixso-frame-5976_53985 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    justify-content: flex-end;
    align-items: flex-start;
}
.frame-content-5976_53985 {
    display: flex;
    flex-direction: row;
    gap: 4px;
    align-items: flex-start;
    justify-content: flex-end;
    width: 100%;
    position: relative;
}
.Pixso-instance-5976_53986 {
    width: 77px;
    height: 4px;
}
.Pixso-instance-5976_53987 {
    width: 77px;
    height: 4px;
}
.Pixso-instance-5976_53988 {
    width: 77px;
    height: 4px;
}
.Pixso-instance-5976_53989 {
    width: 77px;
    height: 4px;
}
.Pixso-paragraph-5976_53990 {
    width: 100%;
    height: 18px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-symbol-5976_53991 {
    width: 320px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 6px;
    align-items: flex-end;
}
.Pixso-frame-5976_53992 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
}
.frame-content-5976_53992 {
    display: flex;
    flex-direction: column;
    gap: 6px;
    align-items: flex-end;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5976_53993 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5976_53994 {
    width: 320px;
    height: 40px;
}
.Pixso-frame-5976_53995 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    justify-content: flex-end;
    align-items: flex-start;
}
.frame-content-5976_53995 {
    display: flex;
    flex-direction: row;
    gap: 4px;
    align-items: flex-start;
    justify-content: flex-end;
    width: 100%;
    position: relative;
}
.Pixso-instance-5976_53996 {
    width: 77px;
    height: 4px;
}
.Pixso-instance-5976_53997 {
    width: 77px;
    height: 4px;
}
.Pixso-instance-5976_53998 {
    width: 77px;
    height: 4px;
}
.Pixso-instance-5976_53999 {
    width: 77px;
    height: 4px;
}
.Pixso-paragraph-5976_54000 {
    width: 100%;
    height: 18px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-symbol-5976_54001 {
    width: 320px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 6px;
    align-items: flex-end;
}
.Pixso-frame-5976_54002 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
}
.frame-content-5976_54002 {
    display: flex;
    flex-direction: column;
    gap: 6px;
    align-items: flex-end;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5976_54003 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5976_54004 {
    width: 320px;
    height: 40px;
}
.Pixso-frame-5976_54005 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    justify-content: flex-end;
    align-items: flex-start;
}
.frame-content-5976_54005 {
    display: flex;
    flex-direction: row;
    gap: 4px;
    align-items: flex-start;
    justify-content: flex-end;
    width: 100%;
    position: relative;
}
.Pixso-instance-5976_54006 {
    width: 77px;
    height: 4px;
}
.Pixso-instance-5976_54007 {
    width: 77px;
    height: 4px;
}
.Pixso-instance-5976_54008 {
    width: 77px;
    height: 4px;
}
.Pixso-instance-5976_54009 {
    width: 77px;
    height: 4px;
}
.Pixso-paragraph-5976_54010 {
    width: 100%;
    height: 18px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-symbol-5976_54011 {
    width: 320px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 6px;
    align-items: flex-end;
}
.Pixso-frame-5976_54012 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
}
.frame-content-5976_54012 {
    display: flex;
    flex-direction: column;
    gap: 6px;
    align-items: flex-end;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5976_54013 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5976_54014 {
    width: 320px;
    height: 40px;
}
.Pixso-instance-5976_52082 {
    width: 20px;
    height: 20px;
}
.Pixso-frame-5976_54015 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    justify-content: flex-end;
    align-items: flex-start;
}
.frame-content-5976_54015 {
    display: flex;
    flex-direction: row;
    gap: 4px;
    align-items: flex-start;
    justify-content: flex-end;
    width: 100%;
    position: relative;
}
.Pixso-instance-5976_54016 {
    width: 77px;
    height: 4px;
}
.Pixso-instance-5976_54017 {
    width: 77px;
    height: 4px;
}
.Pixso-instance-5976_54018 {
    width: 77px;
    height: 4px;
}
.Pixso-instance-5976_54019 {
    width: 77px;
    height: 4px;
}
.Pixso-paragraph-5976_54020 {
    width: 100%;
    height: 18px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-symbol-5976_54021 {
    width: 320px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 6px;
    align-items: flex-end;
}
.Pixso-frame-5976_54022 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
}
.frame-content-5976_54022 {
    display: flex;
    flex-direction: column;
    gap: 6px;
    align-items: flex-end;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5976_54023 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5976_54024 {
    width: 320px;
    height: 40px;
}
.Pixso-frame-5976_54025 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    justify-content: flex-end;
    align-items: flex-start;
}
.frame-content-5976_54025 {
    display: flex;
    flex-direction: row;
    gap: 4px;
    align-items: flex-start;
    justify-content: flex-end;
    width: 100%;
    position: relative;
}
.Pixso-instance-5976_54026 {
    width: 77px;
    height: 4px;
}
.Pixso-instance-5976_54027 {
    width: 77px;
    height: 4px;
}
.Pixso-instance-5976_54028 {
    width: 77px;
    height: 4px;
}
.Pixso-instance-5976_54029 {
    width: 77px;
    height: 4px;
}
.Pixso-paragraph-5976_54030 {
    width: 100%;
    height: 18px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-symbol-5976_54031 {
    width: 320px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 6px;
    align-items: flex-end;
}
.Pixso-frame-5976_54032 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
}
.frame-content-5976_54032 {
    display: flex;
    flex-direction: column;
    gap: 6px;
    align-items: flex-end;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5976_54033 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5976_54034 {
    width: 320px;
    height: 40px;
}
.Pixso-paragraph-5976_54035 {
    width: 100%;
    height: 18px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-symbol-5976_54036 {
    width: 320px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 6px;
    align-items: flex-end;
}
.Pixso-frame-5976_54037 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
}
.frame-content-5976_54037 {
    display: flex;
    flex-direction: column;
    gap: 6px;
    align-items: flex-end;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5976_54038 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5976_54039 {
    width: 320px;
    height: 40px;
}
.Pixso-paragraph-5976_54040 {
    width: 100%;
    height: 18px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-symbol-5976_54041 {
    width: 320px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 6px;
    align-items: flex-end;
}
.Pixso-frame-5976_54042 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
}
.frame-content-5976_54042 {
    display: flex;
    flex-direction: column;
    gap: 6px;
    align-items: flex-end;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5976_54043 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5976_54044 {
    width: 320px;
    height: 40px;
}
.Pixso-paragraph-5976_54045 {
    width: 100%;
    height: 18px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-symbol-5976_54046 {
    width: 320px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 6px;
    align-items: flex-end;
}
.Pixso-frame-5976_54047 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
}
.frame-content-5976_54047 {
    display: flex;
    flex-direction: column;
    gap: 6px;
    align-items: flex-end;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5976_54048 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5976_54049 {
    width: 320px;
    height: 40px;
}
.Pixso-paragraph-5976_54050 {
    width: 100%;
    height: 18px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-symbol-5976_54051 {
    width: 320px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 6px;
    align-items: flex-end;
}
.Pixso-frame-5976_54052 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
}
.frame-content-5976_54052 {
    display: flex;
    flex-direction: column;
    gap: 6px;
    align-items: flex-end;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5976_54053 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5976_54054 {
    width: 320px;
    height: 40px;
}
.Pixso-paragraph-5976_54055 {
    width: 100%;
    height: 18px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-symbol-5976_54056 {
    width: 320px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 6px;
    align-items: flex-end;
}
.Pixso-frame-5976_54057 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
}
.frame-content-5976_54057 {
    display: flex;
    flex-direction: column;
    gap: 6px;
    align-items: flex-end;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5976_54058 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5976_54059 {
    width: 320px;
    height: 40px;
}
.Pixso-paragraph-5976_54060 {
    width: 100%;
    height: 18px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-symbol-5976_54061 {
    width: 320px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 6px;
    align-items: flex-end;
}
.Pixso-frame-5976_54062 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
}
.frame-content-5976_54062 {
    display: flex;
    flex-direction: column;
    gap: 6px;
    align-items: flex-end;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5976_54063 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5976_54064 {
    width: 320px;
    height: 40px;
}
.Pixso-paragraph-5976_54065 {
    width: 100%;
    height: 18px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-symbol-5976_54066 {
    width: 320px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 6px;
    align-items: flex-end;
}
.Pixso-frame-5976_54067 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
}
.frame-content-5976_54067 {
    display: flex;
    flex-direction: column;
    gap: 6px;
    align-items: flex-end;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5976_54068 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5976_54069 {
    width: 320px;
    height: 40px;
}
.Pixso-paragraph-5976_54070 {
    width: 100%;
    height: 18px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-symbol-5976_54071 {
    width: 320px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 6px;
    align-items: flex-end;
}
.Pixso-frame-5976_54072 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
}
.frame-content-5976_54072 {
    display: flex;
    flex-direction: column;
    gap: 6px;
    align-items: flex-end;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5976_54073 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5976_54074 {
    width: 320px;
    height: 40px;
}
.Pixso-paragraph-5976_54075 {
    width: 100%;
    height: 18px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-symbol-5976_54076 {
    width: 320px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 6px;
    align-items: flex-end;
}
.Pixso-frame-5976_54077 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
}
.frame-content-5976_54077 {
    display: flex;
    flex-direction: column;
    gap: 6px;
    align-items: flex-end;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5976_54078 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5976_54079 {
    width: 320px;
    height: 40px;
}
.Pixso-paragraph-5976_54080 {
    width: 100%;
    height: 18px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-symbol-5976_54081 {
    width: 320px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 6px;
    align-items: flex-end;
}
.Pixso-frame-5976_54082 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
}
.frame-content-5976_54082 {
    display: flex;
    flex-direction: column;
    gap: 6px;
    align-items: flex-end;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5976_54083 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5976_54084 {
    width: 320px;
    height: 40px;
}
.Pixso-paragraph-5976_54085 {
    width: 100%;
    height: 18px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-symbol-5976_54086 {
    width: 320px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 6px;
    align-items: flex-end;
}
.Pixso-frame-5976_54087 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
}
.frame-content-5976_54087 {
    display: flex;
    flex-direction: column;
    gap: 6px;
    align-items: flex-end;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5976_54088 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5976_54089 {
    width: 320px;
    height: 40px;
}
.Pixso-paragraph-5976_54090 {
    width: 100%;
    height: 18px;
    position: relative;
    flex-shrink: 0;
}

.Pixso-instance-5608_19678
    .Pixso-instance-5606_19068
    .Pixso-vector-5579_152456 {
    width: 84.37%;
    height: 81.39%;
    background-image: url(@/assets/images/Vector48.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 7.74%;
    right: 7.89%;
    top: 7.8%;
    bottom: 10.81%;
}
.Pixso-instance-5608_19678
    .Pixso-instance-5606_19072
    .Pixso-vector-5579_153183 {
    width: 84.38%;
    height: 84.38%;
    background-image: url(@/assets/images/Vector72.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5606_19068 .Pixso-symbol-5579_152455 .Pixso-symbol-5578_150578 {
    width: 20px;
    height: 20px;
    position: absolute;
    left: 0px;
    top: 1px;
    background-color: transparent;
}
.Pixso-instance-5606_19068 .Pixso-vector-5579_152456 {
    width: 84.37%;
    height: 81.39%;
    position: absolute;
    left: 7.74%;
    right: 7.89%;
    top: 7.8%;
    bottom: 10.81%;
}
.Pixso-instance-5606_19068 .Pixso-symbol-5579_152455 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5607_19554 .Pixso-instance-5606_19068 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5608_19700 .Pixso-instance-5606_19068 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5607_19612 .Pixso-instance-5606_19068 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5608_19656 .Pixso-instance-5606_19068 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5608_19678 .Pixso-instance-5606_19068 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5606_19068 .Pixso-instance-5606_19068 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5606_19072 .Pixso-symbol-5579_153182 .Pixso-symbol-5578_150578 {
    width: 20px;
    height: 20px;
    position: absolute;
    left: 288px;
    top: 14px;
    background-color: transparent;
}
.Pixso-instance-5606_19072 .Pixso-vector-5579_153183 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5606_19072 .Pixso-symbol-5579_153182 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5607_19554 .Pixso-instance-5606_19072 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5608_19700 .Pixso-instance-5606_19072 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5607_19612 .Pixso-instance-5606_19072 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5608_19656 .Pixso-instance-5606_19072 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5608_19678 .Pixso-instance-5606_19072 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5606_19072 .Pixso-instance-5606_19072 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5609_20114 .Pixso-instance-5606_19068 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5609_20114 .Pixso-instance-5606_19072 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5608_19786
    .Pixso-instance-5606_19157
    .Pixso-vector-5579_151287 {
    width: 78.12%;
    height: 78.12%;
    background-image: url(@/assets/images/Vector295.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 10.94%;
    right: 10.94%;
    top: 10.94%;
    bottom: 10.94%;
}
.Pixso-instance-5606_19157 .Pixso-symbol-5579_151286 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5606_19157 .Pixso-vector-5579_151287 {
    width: 78.12%;
    height: 78.12%;
    position: absolute;
    left: 10.94%;
    right: 10.94%;
    top: 10.94%;
    bottom: 10.94%;
}
.Pixso-instance-5608_19976
    .Pixso-instance-5606_19176
    .Pixso-vector-5577_144009 {
    width: 71.9%;
    height: 40.64%;
    background-image: url(@/assets/images/Vector19.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 14.05%;
    right: 14.05%;
    top: 32.8%;
    bottom: 26.56%;
}
.Pixso-instance-5608_19976
    .Pixso-instance-5606_19174
    .Pixso-vector-5579_152191 {
    width: 59.38%;
    height: 90.62%;
    background-image: url(@/assets/images/Vector2043.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 20.31%;
    right: 20.31%;
    top: 4.69%;
    bottom: 4.69%;
}
.Pixso-instance-5606_19176 .Pixso-symbol-5577_144008 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5606_19176 .Pixso-vector-5577_144009 {
    width: 71.9%;
    height: 40.64%;
    position: absolute;
    left: 14.05%;
    right: 14.05%;
    top: 32.8%;
    bottom: 26.56%;
}
.Pixso-instance-5606_19174 .Pixso-symbol-5579_152190 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5606_19174 .Pixso-vector-5579_152191 {
    width: 59.38%;
    height: 90.62%;
    position: absolute;
    left: 20.31%;
    right: 20.31%;
    top: 4.69%;
    bottom: 4.69%;
}
.Pixso-instance-5609_20524
    .Pixso-instance-5607_19365
    .Pixso-vector-5578_148823 {
    width: 78.12%;
    height: 84.37%;
    background-image: url(@/assets/images/Vector375.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 10.94%;
    right: 10.94%;
    top: 4.69%;
    bottom: 10.94%;
}
.Pixso-instance-5607_19365 .Pixso-symbol-5578_148822 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5607_19365 .Pixso-vector-5578_148823 {
    width: 78.12%;
    height: 84.37%;
    position: absolute;
    left: 10.94%;
    right: 10.94%;
    top: 4.69%;
    bottom: 10.94%;
}
.Pixso-instance-5609_20499 .Pixso-instance-5607_19365 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5609_20509 .Pixso-instance-5607_19365 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5609_20514 .Pixso-instance-5607_19365 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5609_20519 .Pixso-instance-5607_19365 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5609_20524 .Pixso-instance-5607_19365 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5607_19365 .Pixso-instance-5607_19365 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5609_20504 .Pixso-instance-5607_19365 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5612_2159 .Pixso-symbol-1264_9827 {
    width: 77px;
    height: 4px;
    position: relative;
    flex-shrink: 0;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5612_2166 .Pixso-symbol-1264_9827 {
    width: 77px;
    height: 4px;
    position: relative;
    flex-shrink: 0;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5612_2167 .Pixso-symbol-1264_9827 {
    width: 77px;
    height: 4px;
    position: relative;
    flex-shrink: 0;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5612_2168 .Pixso-symbol-1264_9827 {
    width: 77px;
    height: 4px;
    position: relative;
    flex-shrink: 0;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5612_2171 .Pixso-symbol-1264_9827 {
    width: 77px;
    height: 4px;
    position: relative;
    flex-shrink: 0;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5612_2172 .Pixso-symbol-1264_9827 {
    width: 77px;
    height: 4px;
    position: relative;
    flex-shrink: 0;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5612_2173 .Pixso-symbol-1264_9827 {
    width: 77px;
    height: 4px;
    position: relative;
    flex-shrink: 0;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5612_2174 .Pixso-symbol-1264_9827 {
    width: 77px;
    height: 4px;
    position: relative;
    flex-shrink: 0;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5612_2176 .Pixso-symbol-1264_9827 {
    width: 77px;
    height: 4px;
    position: relative;
    flex-shrink: 0;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5612_2177 .Pixso-symbol-1264_9827 {
    width: 77px;
    height: 4px;
    position: relative;
    flex-shrink: 0;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5612_2178 .Pixso-symbol-1264_9827 {
    width: 77px;
    height: 4px;
    position: relative;
    flex-shrink: 0;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5612_2179 .Pixso-symbol-1264_9827 {
    width: 77px;
    height: 4px;
    position: relative;
    flex-shrink: 0;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5612_2181 .Pixso-symbol-1264_9827 {
    width: 77px;
    height: 4px;
    position: relative;
    flex-shrink: 0;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5612_2182 .Pixso-symbol-1264_9827 {
    width: 77px;
    height: 4px;
    position: relative;
    flex-shrink: 0;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5612_2183 .Pixso-symbol-1264_9827 {
    width: 77px;
    height: 4px;
    position: relative;
    flex-shrink: 0;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5612_2184 .Pixso-symbol-1264_9827 {
    width: 77px;
    height: 4px;
    position: relative;
    flex-shrink: 0;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5609_20836
    .Pixso-instance-5607_19417
    .Pixso-vector-5579_153024 {
    width: 78.12%;
    height: 87.5%;
    background-image: url(@/assets/images/Vector66.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 10.94%;
    right: 10.94%;
    top: 1.56%;
    bottom: 10.94%;
}
.Pixso-instance-5607_19417 .Pixso-symbol-5579_153023 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5607_19417 .Pixso-vector-5579_153024 {
    width: 78.12%;
    height: 87.5%;
    position: absolute;
    left: 10.94%;
    right: 10.94%;
    top: 1.56%;
    bottom: 10.94%;
}
.Pixso-instance-5609_20811 .Pixso-instance-5607_19417 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5609_20821 .Pixso-instance-5607_19417 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5609_20826 .Pixso-instance-5607_19417 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5609_20831 .Pixso-instance-5607_19417 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5609_20836 .Pixso-instance-5607_19417 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5607_19417 .Pixso-instance-5607_19417 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5612_2186 .Pixso-symbol-1264_9827 {
    width: 77px;
    height: 4px;
    position: relative;
    flex-shrink: 0;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5612_2187 .Pixso-symbol-1264_9827 {
    width: 77px;
    height: 4px;
    position: relative;
    flex-shrink: 0;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5612_2188 .Pixso-symbol-1264_9827 {
    width: 77px;
    height: 4px;
    position: relative;
    flex-shrink: 0;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5612_2189 .Pixso-symbol-1264_9827 {
    width: 77px;
    height: 4px;
    position: relative;
    flex-shrink: 0;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5609_20816 .Pixso-instance-5607_19417 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5612_2191 .Pixso-symbol-1264_9827 {
    width: 77px;
    height: 4px;
    position: relative;
    flex-shrink: 0;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5612_2192 .Pixso-symbol-1264_9827 {
    width: 77px;
    height: 4px;
    position: relative;
    flex-shrink: 0;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5612_2193 .Pixso-symbol-1264_9827 {
    width: 77px;
    height: 4px;
    position: relative;
    flex-shrink: 0;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5612_2194 .Pixso-symbol-1264_9827 {
    width: 77px;
    height: 4px;
    position: relative;
    flex-shrink: 0;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5976_53794 .Pixso-instance-5976_52049 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5976_53799 .Pixso-instance-5976_52049 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5976_53804 .Pixso-instance-5976_52049 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5976_53809 .Pixso-instance-5976_52049 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5976_53814 .Pixso-instance-5976_52049 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5976_53814
    .Pixso-instance-5976_52049
    .Pixso-vector-5579_152456 {
    width: 84.37%;
    height: 81.39%;
    background-image: url(@/assets/images/Vector48.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 7.74%;
    right: 7.89%;
    top: 7.8%;
    bottom: 10.81%;
}
.Pixso-instance-5976_53814
    .Pixso-instance-5976_52051
    .Pixso-vector-5579_153183 {
    width: 84.38%;
    height: 84.38%;
    background-image: url(@/assets/images/Vector72.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5976_52049 .Pixso-symbol-5579_152455 .Pixso-symbol-5578_150578 {
    width: 20px;
    height: 20px;
    position: absolute;
    left: 0px;
    top: 1px;
    background-color: transparent;
}
.Pixso-instance-5976_52049 .Pixso-vector-5579_152456 {
    width: 84.37%;
    height: 81.39%;
    position: absolute;
    left: 7.74%;
    right: 7.89%;
    top: 7.8%;
    bottom: 10.81%;
}
.Pixso-instance-5976_52049 .Pixso-symbol-5579_152455 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5976_52049 .Pixso-instance-5976_52049 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5976_52051 .Pixso-symbol-5579_153182 .Pixso-symbol-5578_150578 {
    width: 20px;
    height: 20px;
    position: absolute;
    left: 288px;
    top: 10px;
    background-color: transparent;
}
.Pixso-instance-5976_52051 .Pixso-vector-5579_153183 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5976_52051 .Pixso-symbol-5579_153182 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5976_53794 .Pixso-instance-5976_52051 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5976_53799 .Pixso-instance-5976_52051 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5976_53804 .Pixso-instance-5976_52051 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5976_53809 .Pixso-instance-5976_52051 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5976_53814 .Pixso-instance-5976_52051 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5976_52051 .Pixso-instance-5976_52051 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5976_53819 .Pixso-instance-5976_52049 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5976_53819 .Pixso-instance-5976_52051 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5976_53844
    .Pixso-instance-5976_52057
    .Pixso-vector-5579_151287 {
    width: 78.12%;
    height: 78.12%;
    background-image: url(@/assets/images/Vector295.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 10.94%;
    right: 10.94%;
    top: 10.94%;
    bottom: 10.94%;
}
.Pixso-instance-5976_52057 .Pixso-symbol-5579_151286 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5976_52057 .Pixso-vector-5579_151287 {
    width: 78.12%;
    height: 78.12%;
    position: absolute;
    left: 10.94%;
    right: 10.94%;
    top: 10.94%;
    bottom: 10.94%;
}
.Pixso-instance-5976_53874
    .Pixso-instance-5976_52065
    .Pixso-vector-5577_144009 {
    width: 71.9%;
    height: 40.64%;
    background-image: url(@/assets/images/Vector19.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 14.05%;
    right: 14.05%;
    top: 32.8%;
    bottom: 26.56%;
}
.Pixso-instance-5976_53874
    .Pixso-instance-5976_52060
    .Pixso-vector-5579_152191 {
    width: 59.38%;
    height: 90.62%;
    background-image: url(@/assets/images/Vector2043.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 20.31%;
    right: 20.31%;
    top: 4.69%;
    bottom: 4.69%;
}
.Pixso-instance-5976_52065 .Pixso-symbol-5577_144008 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5976_52065 .Pixso-vector-5577_144009 {
    width: 71.9%;
    height: 40.64%;
    position: absolute;
    left: 14.05%;
    right: 14.05%;
    top: 32.8%;
    bottom: 26.56%;
}
.Pixso-instance-5976_52060 .Pixso-symbol-5579_152190 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5976_52060 .Pixso-vector-5579_152191 {
    width: 59.38%;
    height: 90.62%;
    position: absolute;
    left: 20.31%;
    right: 20.31%;
    top: 4.69%;
    bottom: 4.69%;
}
.Pixso-instance-5976_53934
    .Pixso-instance-5976_52073
    .Pixso-vector-5578_148823 {
    width: 78.12%;
    height: 84.37%;
    background-image: url(@/assets/images/Vector375.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 10.94%;
    right: 10.94%;
    top: 4.69%;
    bottom: 10.94%;
}
.Pixso-instance-5976_52073 .Pixso-symbol-5578_148822 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5976_52073 .Pixso-vector-5578_148823 {
    width: 78.12%;
    height: 84.37%;
    position: absolute;
    left: 10.94%;
    right: 10.94%;
    top: 4.69%;
    bottom: 10.94%;
}
.Pixso-instance-5976_53914 .Pixso-instance-5976_52073 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5976_53919 .Pixso-instance-5976_52073 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5976_53924 .Pixso-instance-5976_52073 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5976_53929 .Pixso-instance-5976_52073 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5976_53934 .Pixso-instance-5976_52073 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5976_52073 .Pixso-instance-5976_52073 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5976_53939 .Pixso-instance-5976_52073 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5976_53976 .Pixso-symbol-1264_9827 {
    width: 77px;
    height: 4px;
    position: relative;
    flex-shrink: 0;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5976_53977 .Pixso-symbol-1264_9827 {
    width: 77px;
    height: 4px;
    position: relative;
    flex-shrink: 0;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5976_53978 .Pixso-symbol-1264_9827 {
    width: 77px;
    height: 4px;
    position: relative;
    flex-shrink: 0;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5976_53979 .Pixso-symbol-1264_9827 {
    width: 77px;
    height: 4px;
    position: relative;
    flex-shrink: 0;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5976_53986 .Pixso-symbol-1264_9827 {
    width: 77px;
    height: 4px;
    position: relative;
    flex-shrink: 0;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5976_53987 .Pixso-symbol-1264_9827 {
    width: 77px;
    height: 4px;
    position: relative;
    flex-shrink: 0;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5976_53988 .Pixso-symbol-1264_9827 {
    width: 77px;
    height: 4px;
    position: relative;
    flex-shrink: 0;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5976_53989 .Pixso-symbol-1264_9827 {
    width: 77px;
    height: 4px;
    position: relative;
    flex-shrink: 0;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5976_53996 .Pixso-symbol-1264_9827 {
    width: 77px;
    height: 4px;
    position: relative;
    flex-shrink: 0;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5976_53997 .Pixso-symbol-1264_9827 {
    width: 77px;
    height: 4px;
    position: relative;
    flex-shrink: 0;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5976_53998 .Pixso-symbol-1264_9827 {
    width: 77px;
    height: 4px;
    position: relative;
    flex-shrink: 0;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5976_53999 .Pixso-symbol-1264_9827 {
    width: 77px;
    height: 4px;
    position: relative;
    flex-shrink: 0;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5976_54006 .Pixso-symbol-1264_9827 {
    width: 77px;
    height: 4px;
    position: relative;
    flex-shrink: 0;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5976_54007 .Pixso-symbol-1264_9827 {
    width: 77px;
    height: 4px;
    position: relative;
    flex-shrink: 0;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5976_54008 .Pixso-symbol-1264_9827 {
    width: 77px;
    height: 4px;
    position: relative;
    flex-shrink: 0;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5976_54009 .Pixso-symbol-1264_9827 {
    width: 77px;
    height: 4px;
    position: relative;
    flex-shrink: 0;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5976_54014
    .Pixso-instance-5976_52082
    .Pixso-vector-5579_153024 {
    width: 78.12%;
    height: 87.5%;
    background-image: url(@/assets/images/Vector66.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 10.94%;
    right: 10.94%;
    top: 1.56%;
    bottom: 10.94%;
}
.Pixso-instance-5976_52082 .Pixso-symbol-5579_153023 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5976_52082 .Pixso-vector-5579_153024 {
    width: 78.12%;
    height: 87.5%;
    position: absolute;
    left: 10.94%;
    right: 10.94%;
    top: 1.56%;
    bottom: 10.94%;
}
.Pixso-instance-5976_53974 .Pixso-instance-5976_52082 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5976_53984 .Pixso-instance-5976_52082 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5976_53994 .Pixso-instance-5976_52082 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5976_54004 .Pixso-instance-5976_52082 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5976_54014 .Pixso-instance-5976_52082 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5976_52082 .Pixso-instance-5976_52082 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5976_54016 .Pixso-symbol-1264_9827 {
    width: 77px;
    height: 4px;
    position: relative;
    flex-shrink: 0;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5976_54017 .Pixso-symbol-1264_9827 {
    width: 77px;
    height: 4px;
    position: relative;
    flex-shrink: 0;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5976_54018 .Pixso-symbol-1264_9827 {
    width: 77px;
    height: 4px;
    position: relative;
    flex-shrink: 0;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5976_54019 .Pixso-symbol-1264_9827 {
    width: 77px;
    height: 4px;
    position: relative;
    flex-shrink: 0;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5976_54024 .Pixso-instance-5976_52082 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5976_54026 .Pixso-symbol-1264_9827 {
    width: 77px;
    height: 4px;
    position: relative;
    flex-shrink: 0;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5976_54027 .Pixso-symbol-1264_9827 {
    width: 77px;
    height: 4px;
    position: relative;
    flex-shrink: 0;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5976_54028 .Pixso-symbol-1264_9827 {
    width: 77px;
    height: 4px;
    position: relative;
    flex-shrink: 0;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5976_54029 .Pixso-symbol-1264_9827 {
    width: 77px;
    height: 4px;
    position: relative;
    flex-shrink: 0;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5607_19554 .Pixso-symbol-5606_19081 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 12px 12px 12px 12px;
    min-height: 48px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5607_19554 .stroke-wrapper-5606_19081 {
    width: 320px;
    height: 48px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5607_19554 .stroke-5606_19081 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5608_19700 .Pixso-symbol-5606_19081 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 12px 12px 12px 12px;
    min-height: 48px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5608_19700 .stroke-wrapper-5606_19081 {
    width: 320px;
    height: 48px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5608_19700 .stroke-5606_19081 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5607_19612 .Pixso-symbol-5606_19081 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 12px 12px 12px 12px;
    min-height: 48px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5607_19612 .stroke-wrapper-5606_19081 {
    width: 320px;
    height: 48px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5607_19612 .stroke-5606_19081 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5608_19656 .Pixso-symbol-5606_19081 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 12px 12px 12px 12px;
    min-height: 48px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5608_19656 .stroke-wrapper-5606_19081 {
    width: 320px;
    height: 48px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5608_19656 .stroke-5606_19081 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5608_19678 .Pixso-symbol-5606_19081 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 12px 12px 12px 12px;
    min-height: 48px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5608_19678 .stroke-wrapper-5606_19081 {
    width: 320px;
    height: 48px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5608_19678 .stroke-5606_19081 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5609_20114 .Pixso-symbol-5606_19081 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 12px 12px 12px 12px;
    min-height: 48px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5609_20114 .stroke-wrapper-5606_19081 {
    width: 320px;
    height: 48px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5609_20114 .stroke-5606_19081 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5607_19554 .Pixso-frame-5606_19162 {
    width: 100%;
    height: 22px;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5608_19700 .Pixso-frame-5606_19162 {
    width: 100%;
    height: 22px;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5607_19612 .Pixso-frame-5606_19162 {
    width: 100%;
    height: 22px;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5608_19656 .Pixso-frame-5606_19162 {
    width: 100%;
    height: 22px;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5608_19678 .Pixso-frame-5606_19162 {
    width: 100%;
    height: 22px;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5609_20114 .Pixso-frame-5606_19162 {
    width: 100%;
    height: 22px;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5607_19554 .Pixso-paragraph-5606_19069 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5608_19700 .Pixso-paragraph-5606_19069 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5607_19612 .Pixso-paragraph-5606_19069 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5608_19656 .Pixso-paragraph-5606_19069 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5608_19678 .Pixso-paragraph-5606_19069 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5609_20114 .Pixso-paragraph-5606_19069 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5976_53794 .Pixso-symbol-5976_52047 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 8px 12px 8px 12px;
    min-height: 40px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5976_53794 .stroke-wrapper-5976_52047 {
    width: 320px;
    height: 40px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5976_53794 .stroke-5976_52047 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5976_53799 .Pixso-symbol-5976_52047 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 8px 12px 8px 12px;
    min-height: 40px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5976_53799 .stroke-wrapper-5976_52047 {
    width: 320px;
    height: 40px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5976_53799 .stroke-5976_52047 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5976_53804 .Pixso-symbol-5976_52047 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 8px 12px 8px 12px;
    min-height: 40px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5976_53804 .stroke-wrapper-5976_52047 {
    width: 320px;
    height: 40px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5976_53804 .stroke-5976_52047 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5976_53809 .Pixso-symbol-5976_52047 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 8px 12px 8px 12px;
    min-height: 40px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5976_53809 .stroke-wrapper-5976_52047 {
    width: 320px;
    height: 40px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5976_53809 .stroke-5976_52047 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5976_53814 .Pixso-symbol-5976_52047 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 8px 12px 8px 12px;
    min-height: 40px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5976_53814 .stroke-wrapper-5976_52047 {
    width: 320px;
    height: 40px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5976_53814 .stroke-5976_52047 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5976_53819 .Pixso-symbol-5976_52047 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 8px 12px 8px 12px;
    min-height: 40px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5976_53819 .stroke-wrapper-5976_52047 {
    width: 320px;
    height: 40px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5976_53819 .stroke-5976_52047 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5976_53794 .Pixso-frame-5976_52048 {
    width: 100%;
    height: 22px;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5976_53799 .Pixso-frame-5976_52048 {
    width: 100%;
    height: 22px;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5976_53804 .Pixso-frame-5976_52048 {
    width: 100%;
    height: 22px;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5976_53809 .Pixso-frame-5976_52048 {
    width: 100%;
    height: 22px;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5976_53814 .Pixso-frame-5976_52048 {
    width: 100%;
    height: 22px;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5976_53819 .Pixso-frame-5976_52048 {
    width: 100%;
    height: 22px;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5976_53794 .Pixso-paragraph-5976_52050 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5976_53799 .Pixso-paragraph-5976_52050 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5976_53804 .Pixso-paragraph-5976_52050 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5976_53809 .Pixso-paragraph-5976_52050 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5976_53814 .Pixso-paragraph-5976_52050 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5976_53819 .Pixso-paragraph-5976_52050 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5608_19766 .Pixso-symbol-5606_19148 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    align-items: center;
    min-height: 48px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5608_19766 .stroke-wrapper-5606_19148 {
    width: 320px;
    height: 48px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5608_19766 .stroke-5606_19148 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5608_19771 .Pixso-symbol-5606_19148 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    align-items: center;
    min-height: 48px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5608_19771 .stroke-wrapper-5606_19148 {
    width: 320px;
    height: 48px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5608_19771 .stroke-5606_19148 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5608_19776 .Pixso-symbol-5606_19148 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    align-items: center;
    min-height: 48px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5608_19776 .stroke-wrapper-5606_19148 {
    width: 320px;
    height: 48px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5608_19776 .stroke-5606_19148 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5608_19781 .Pixso-symbol-5606_19148 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    align-items: center;
    min-height: 48px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5608_19781 .stroke-wrapper-5606_19148 {
    width: 320px;
    height: 48px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5608_19781 .stroke-5606_19148 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5608_19786 .Pixso-symbol-5606_19148 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    align-items: center;
    min-height: 48px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5608_19786 .stroke-wrapper-5606_19148 {
    width: 320px;
    height: 48px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5608_19786 .stroke-5606_19148 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5609_20119 .Pixso-symbol-5606_19148 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    align-items: center;
    min-height: 48px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5609_20119 .stroke-wrapper-5606_19148 {
    width: 320px;
    height: 48px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5609_20119 .stroke-5606_19148 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5608_19766 .Pixso-frame-5606_19163 .frame-content-5606_19163 {
    padding: 12px 12px 12px 12px;
}
.Pixso-instance-5608_19766 .Pixso-frame-5606_19163 {
    width: 100%;
    height: 46px;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: row;
    gap: 6px;
    align-items: center;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5608_19771 .Pixso-frame-5606_19163 .frame-content-5606_19163 {
    padding: 12px 12px 12px 12px;
}
.Pixso-instance-5608_19771 .Pixso-frame-5606_19163 {
    width: 100%;
    height: 46px;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: row;
    gap: 6px;
    align-items: center;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5608_19776 .Pixso-frame-5606_19163 .frame-content-5606_19163 {
    padding: 12px 12px 12px 12px;
}
.Pixso-instance-5608_19776 .Pixso-frame-5606_19163 {
    width: 100%;
    height: 46px;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: row;
    gap: 6px;
    align-items: center;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5608_19781 .Pixso-frame-5606_19163 .frame-content-5606_19163 {
    padding: 12px 12px 12px 12px;
}
.Pixso-instance-5608_19781 .Pixso-frame-5606_19163 {
    width: 100%;
    height: 46px;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: row;
    gap: 6px;
    align-items: center;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5608_19786 .Pixso-frame-5606_19163 .frame-content-5606_19163 {
    padding: 12px 12px 12px 12px;
}
.Pixso-instance-5608_19786 .Pixso-frame-5606_19163 {
    width: 100%;
    height: 46px;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: row;
    gap: 6px;
    align-items: center;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5609_20119 .Pixso-frame-5606_19163 .frame-content-5606_19163 {
    padding: 12px 12px 12px 12px;
}
.Pixso-instance-5609_20119 .Pixso-frame-5606_19163 {
    width: 100%;
    height: 46px;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: row;
    gap: 6px;
    align-items: center;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5608_19766 .Pixso-paragraph-5606_19143 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5608_19771 .Pixso-paragraph-5606_19143 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5608_19776 .Pixso-paragraph-5606_19143 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5608_19781 .Pixso-paragraph-5606_19143 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5608_19786 .Pixso-paragraph-5606_19143 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5609_20119 .Pixso-paragraph-5606_19143 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5608_19766 .Pixso-frame-5606_19161 {
    width: 100%;
    height: 100%;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 6px;
    align-items: center;
}
.Pixso-instance-5608_19766 .stroke-wrapper-5606_19161 {
    width: 92px;
    height: 48px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5608_19766 .stroke-5606_19161 {
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 0px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5608_19771 .Pixso-frame-5606_19161 {
    width: 100%;
    height: 100%;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 6px;
    align-items: center;
}
.Pixso-instance-5608_19771 .stroke-wrapper-5606_19161 {
    width: 92px;
    height: 48px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5608_19771 .stroke-5606_19161 {
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 0px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5608_19776 .Pixso-frame-5606_19161 {
    width: 100%;
    height: 100%;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 6px;
    align-items: center;
}
.Pixso-instance-5608_19776 .stroke-wrapper-5606_19161 {
    width: 92px;
    height: 48px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5608_19776 .stroke-5606_19161 {
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 0px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5608_19781 .Pixso-frame-5606_19161 {
    width: 100%;
    height: 100%;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 6px;
    align-items: center;
}
.Pixso-instance-5608_19781 .stroke-wrapper-5606_19161 {
    width: 92px;
    height: 48px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5608_19781 .stroke-5606_19161 {
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 0px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5608_19786 .Pixso-frame-5606_19161 .frame-content-5606_19161 {
    padding: 12px 12px 12px 12px;
}
.Pixso-instance-5608_19786 .Pixso-frame-5606_19161 {
    width: 100%;
    height: 100%;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 6px;
    align-items: center;
}
.Pixso-instance-5608_19786 .stroke-wrapper-5606_19161 {
    width: 92px;
    height: 48px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5608_19786 .stroke-5606_19161 {
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 0px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5609_20119 .Pixso-frame-5606_19161 {
    width: 100%;
    height: 100%;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 6px;
    align-items: center;
}
.Pixso-instance-5609_20119 .stroke-wrapper-5606_19161 {
    width: 92px;
    height: 48px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5609_20119 .stroke-5606_19161 {
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 0px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5608_19786 .Pixso-paragraph-5606_19152 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5976_53824 .Pixso-symbol-5976_52052 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    align-items: center;
    min-height: 40px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5976_53824 .stroke-wrapper-5976_52052 {
    width: 320px;
    height: 40px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5976_53824 .stroke-5976_52052 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5976_53829 .Pixso-symbol-5976_52052 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    align-items: center;
    min-height: 40px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5976_53829 .stroke-wrapper-5976_52052 {
    width: 320px;
    height: 40px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5976_53829 .stroke-5976_52052 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5976_53834 .Pixso-symbol-5976_52052 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    align-items: center;
    min-height: 40px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5976_53834 .stroke-wrapper-5976_52052 {
    width: 320px;
    height: 40px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5976_53834 .stroke-5976_52052 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5976_53839 .Pixso-symbol-5976_52052 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    align-items: center;
    min-height: 40px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5976_53839 .stroke-wrapper-5976_52052 {
    width: 320px;
    height: 40px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5976_53839 .stroke-5976_52052 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5976_53844 .Pixso-symbol-5976_52052 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    align-items: center;
    min-height: 40px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5976_53844 .stroke-wrapper-5976_52052 {
    width: 320px;
    height: 40px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5976_53844 .stroke-5976_52052 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5976_53849 .Pixso-symbol-5976_52052 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    align-items: center;
    min-height: 40px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5976_53849 .stroke-wrapper-5976_52052 {
    width: 320px;
    height: 40px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5976_53849 .stroke-5976_52052 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5976_53824 .Pixso-frame-5976_52053 {
    width: 100%;
    height: 38px;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: row;
    gap: 6px;
    align-items: center;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5976_53829 .Pixso-frame-5976_52053 {
    width: 100%;
    height: 38px;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: row;
    gap: 6px;
    align-items: center;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5976_53834 .Pixso-frame-5976_52053 {
    width: 100%;
    height: 38px;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: row;
    gap: 6px;
    align-items: center;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5976_53839 .Pixso-frame-5976_52053 {
    width: 100%;
    height: 38px;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: row;
    gap: 6px;
    align-items: center;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5976_53844 .Pixso-frame-5976_52053 {
    width: 100%;
    height: 38px;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: row;
    gap: 6px;
    align-items: center;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5976_53849 .Pixso-frame-5976_52053 {
    width: 100%;
    height: 38px;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: row;
    gap: 6px;
    align-items: center;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5976_53824 .Pixso-paragraph-5976_52054 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5976_53829 .Pixso-paragraph-5976_52054 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5976_53834 .Pixso-paragraph-5976_52054 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5976_53839 .Pixso-paragraph-5976_52054 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5976_53844 .Pixso-paragraph-5976_52054 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5976_53849 .Pixso-paragraph-5976_52054 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5976_53824 .Pixso-frame-5976_52055 {
    width: 100%;
    height: 100%;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 6px;
    align-items: center;
}
.Pixso-instance-5976_53824 .stroke-wrapper-5976_52055 {
    width: 92px;
    height: 40px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5976_53824 .stroke-5976_52055 {
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 0px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5976_53829 .Pixso-frame-5976_52055 {
    width: 100%;
    height: 100%;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 6px;
    align-items: center;
}
.Pixso-instance-5976_53829 .stroke-wrapper-5976_52055 {
    width: 92px;
    height: 40px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5976_53829 .stroke-5976_52055 {
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 0px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5976_53834 .Pixso-frame-5976_52055 {
    width: 100%;
    height: 100%;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 6px;
    align-items: center;
}
.Pixso-instance-5976_53834 .stroke-wrapper-5976_52055 {
    width: 92px;
    height: 40px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5976_53834 .stroke-5976_52055 {
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 0px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5976_53839 .Pixso-frame-5976_52055 {
    width: 100%;
    height: 100%;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 6px;
    align-items: center;
}
.Pixso-instance-5976_53839 .stroke-wrapper-5976_52055 {
    width: 92px;
    height: 40px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5976_53839 .stroke-5976_52055 {
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 0px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5976_53844 .Pixso-frame-5976_52055 {
    width: 100%;
    height: 100%;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 6px;
    align-items: center;
}
.Pixso-instance-5976_53844 .stroke-wrapper-5976_52055 {
    width: 92px;
    height: 40px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5976_53844 .stroke-5976_52055 {
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 0px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5976_53849 .Pixso-frame-5976_52055 {
    width: 100%;
    height: 100%;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 6px;
    align-items: center;
}
.Pixso-instance-5976_53849 .stroke-wrapper-5976_52055 {
    width: 92px;
    height: 40px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5976_53849 .stroke-5976_52055 {
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 0px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5976_53844 .Pixso-paragraph-5976_52056 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5608_19956 .Pixso-symbol-5606_19172 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    align-items: center;
    min-height: 48px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5608_19956 .stroke-wrapper-5606_19172 {
    width: 320px;
    height: 48px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5608_19956 .stroke-5606_19172 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5608_19961 .Pixso-symbol-5606_19172 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    align-items: center;
    min-height: 48px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5608_19961 .stroke-wrapper-5606_19172 {
    width: 320px;
    height: 48px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5608_19961 .stroke-5606_19172 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5608_19966 .Pixso-symbol-5606_19172 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    align-items: center;
    min-height: 48px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5608_19966 .stroke-wrapper-5606_19172 {
    width: 320px;
    height: 48px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5608_19966 .stroke-5606_19172 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5608_19971 .Pixso-symbol-5606_19172 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    align-items: center;
    min-height: 48px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5608_19971 .stroke-wrapper-5606_19172 {
    width: 320px;
    height: 48px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5608_19971 .stroke-5606_19172 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5608_19976 .Pixso-symbol-5606_19172 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    align-items: center;
    min-height: 48px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5608_19976 .stroke-wrapper-5606_19172 {
    width: 320px;
    height: 48px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5608_19976 .stroke-5606_19172 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5609_20124 .Pixso-symbol-5606_19172 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    align-items: center;
    min-height: 48px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5609_20124 .stroke-wrapper-5606_19172 {
    width: 320px;
    height: 48px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5609_20124 .stroke-5606_19172 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5608_19956 .Pixso-frame-5607_19244 {
    width: 100%;
    height: 100%;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 6px;
    align-items: center;
}
.Pixso-instance-5608_19956 .stroke-wrapper-5607_19244 {
    width: 44px;
    height: 48px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5608_19956 .stroke-5607_19244 {
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 1px 0px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5608_19961 .Pixso-frame-5607_19244 {
    width: 100%;
    height: 100%;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 6px;
    align-items: center;
}
.Pixso-instance-5608_19961 .stroke-wrapper-5607_19244 {
    width: 44px;
    height: 48px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5608_19961 .stroke-5607_19244 {
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 1px 0px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5608_19966 .Pixso-frame-5607_19244 {
    width: 100%;
    height: 100%;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 6px;
    align-items: center;
}
.Pixso-instance-5608_19966 .stroke-wrapper-5607_19244 {
    width: 44px;
    height: 48px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5608_19966 .stroke-5607_19244 {
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 1px 0px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5608_19971 .Pixso-frame-5607_19244 {
    width: 100%;
    height: 100%;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 6px;
    align-items: center;
}
.Pixso-instance-5608_19971 .stroke-wrapper-5607_19244 {
    width: 44px;
    height: 48px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5608_19971 .stroke-5607_19244 {
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 1px 0px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5608_19976 .Pixso-frame-5607_19244 {
    width: 100%;
    height: 100%;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 6px;
    align-items: center;
}
.Pixso-instance-5608_19976 .stroke-wrapper-5607_19244 {
    width: 44px;
    height: 48px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5608_19976 .stroke-5607_19244 {
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 1px 0px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5609_20124 .Pixso-frame-5607_19244 {
    width: 100%;
    height: 100%;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 6px;
    align-items: center;
}
.Pixso-instance-5609_20124 .stroke-wrapper-5607_19244 {
    width: 44px;
    height: 48px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5609_20124 .stroke-5607_19244 {
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 1px 0px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5608_19956 .Pixso-frame-5607_19390 .frame-content-5607_19390 {
    padding: 12px 12px 12px 12px;
}
.Pixso-instance-5608_19956 .Pixso-frame-5607_19390 {
    width: 100%;
    height: 46px;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: row;
    gap: 6px;
    align-items: center;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5608_19961 .Pixso-frame-5607_19390 .frame-content-5607_19390 {
    padding: 12px 12px 12px 12px;
}
.Pixso-instance-5608_19961 .Pixso-frame-5607_19390 {
    width: 100%;
    height: 46px;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: row;
    gap: 6px;
    align-items: center;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5608_19966 .Pixso-frame-5607_19390 .frame-content-5607_19390 {
    padding: 12px 12px 12px 12px;
}
.Pixso-instance-5608_19966 .Pixso-frame-5607_19390 {
    width: 100%;
    height: 46px;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: row;
    gap: 6px;
    align-items: center;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5608_19971 .Pixso-frame-5607_19390 .frame-content-5607_19390 {
    padding: 12px 12px 12px 12px;
}
.Pixso-instance-5608_19971 .Pixso-frame-5607_19390 {
    width: 100%;
    height: 46px;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: row;
    gap: 6px;
    align-items: center;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5608_19976 .Pixso-frame-5607_19390 .frame-content-5607_19390 {
    padding: 12px 12px 12px 12px;
}
.Pixso-instance-5608_19976 .Pixso-frame-5607_19390 {
    width: 100%;
    height: 46px;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: row;
    gap: 6px;
    align-items: center;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5609_20124 .Pixso-frame-5607_19390 .frame-content-5607_19390 {
    padding: 12px 12px 12px 12px;
}
.Pixso-instance-5609_20124 .Pixso-frame-5607_19390 {
    width: 100%;
    height: 46px;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: row;
    gap: 6px;
    align-items: center;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5608_19956 .Pixso-paragraph-5606_19175 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5608_19961 .Pixso-paragraph-5606_19175 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5608_19966 .Pixso-paragraph-5606_19175 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5608_19971 .Pixso-paragraph-5606_19175 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5608_19976 .Pixso-paragraph-5606_19175 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5609_20124 .Pixso-paragraph-5606_19175 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5608_19956 .Pixso-frame-5606_19240 {
    width: 100%;
    height: 100%;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 6px;
    align-items: center;
}
.Pixso-instance-5608_19956 .stroke-wrapper-5606_19240 {
    width: 84px;
    height: 48px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5608_19956 .stroke-5606_19240 {
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 0px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5608_19961 .Pixso-frame-5606_19240 {
    width: 100%;
    height: 100%;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 6px;
    align-items: center;
}
.Pixso-instance-5608_19961 .stroke-wrapper-5606_19240 {
    width: 84px;
    height: 48px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5608_19961 .stroke-5606_19240 {
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 0px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5608_19966 .Pixso-frame-5606_19240 {
    width: 100%;
    height: 100%;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 6px;
    align-items: center;
}
.Pixso-instance-5608_19966 .stroke-wrapper-5606_19240 {
    width: 84px;
    height: 48px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5608_19966 .stroke-5606_19240 {
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 0px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5608_19971 .Pixso-frame-5606_19240 {
    width: 100%;
    height: 100%;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 6px;
    align-items: center;
}
.Pixso-instance-5608_19971 .stroke-wrapper-5606_19240 {
    width: 84px;
    height: 48px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5608_19971 .stroke-5606_19240 {
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 0px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5608_19976 .Pixso-frame-5606_19240 .frame-content-5606_19240 {
    padding: 12px 12px 12px 12px;
}
.Pixso-instance-5608_19976 .Pixso-frame-5606_19240 {
    width: 100%;
    height: 100%;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 6px;
    align-items: center;
}
.Pixso-instance-5608_19976 .stroke-wrapper-5606_19240 {
    width: 84px;
    height: 48px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5608_19976 .stroke-5606_19240 {
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 0px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5609_20124 .Pixso-frame-5606_19240 {
    width: 100%;
    height: 100%;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 6px;
    align-items: center;
}
.Pixso-instance-5609_20124 .stroke-wrapper-5606_19240 {
    width: 84px;
    height: 48px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5609_20124 .stroke-5606_19240 {
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 0px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5608_19976 .Pixso-paragraph-5606_19193 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5976_53854 .Pixso-symbol-5976_52058 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    align-items: center;
    min-height: 40px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5976_53854 .stroke-wrapper-5976_52058 {
    width: 320px;
    height: 40px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5976_53854 .stroke-5976_52058 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5976_53859 .Pixso-symbol-5976_52058 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    align-items: center;
    min-height: 40px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5976_53859 .stroke-wrapper-5976_52058 {
    width: 320px;
    height: 40px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5976_53859 .stroke-5976_52058 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5976_53864 .Pixso-symbol-5976_52058 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    align-items: center;
    min-height: 40px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5976_53864 .stroke-wrapper-5976_52058 {
    width: 320px;
    height: 40px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5976_53864 .stroke-5976_52058 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5976_53869 .Pixso-symbol-5976_52058 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    align-items: center;
    min-height: 40px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5976_53869 .stroke-wrapper-5976_52058 {
    width: 320px;
    height: 40px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5976_53869 .stroke-5976_52058 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5976_53874 .Pixso-symbol-5976_52058 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    align-items: center;
    min-height: 40px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5976_53874 .stroke-wrapper-5976_52058 {
    width: 320px;
    height: 40px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5976_53874 .stroke-5976_52058 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5976_53879 .Pixso-symbol-5976_52058 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    align-items: center;
    min-height: 40px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5976_53879 .stroke-wrapper-5976_52058 {
    width: 320px;
    height: 40px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5976_53879 .stroke-5976_52058 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5976_53854 .Pixso-frame-5976_52059 {
    width: 100%;
    height: 100%;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 6px;
    align-items: center;
}
.Pixso-instance-5976_53854 .stroke-wrapper-5976_52059 {
    width: 44px;
    height: 40px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5976_53854 .stroke-5976_52059 {
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 1px 0px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5976_53859 .Pixso-frame-5976_52059 {
    width: 100%;
    height: 100%;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 6px;
    align-items: center;
}
.Pixso-instance-5976_53859 .stroke-wrapper-5976_52059 {
    width: 44px;
    height: 40px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5976_53859 .stroke-5976_52059 {
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 1px 0px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5976_53864 .Pixso-frame-5976_52059 {
    width: 100%;
    height: 100%;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 6px;
    align-items: center;
}
.Pixso-instance-5976_53864 .stroke-wrapper-5976_52059 {
    width: 44px;
    height: 40px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5976_53864 .stroke-5976_52059 {
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 1px 0px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5976_53869 .Pixso-frame-5976_52059 {
    width: 100%;
    height: 100%;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 6px;
    align-items: center;
}
.Pixso-instance-5976_53869 .stroke-wrapper-5976_52059 {
    width: 44px;
    height: 40px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5976_53869 .stroke-5976_52059 {
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 1px 0px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5976_53874 .Pixso-frame-5976_52059 {
    width: 100%;
    height: 100%;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 6px;
    align-items: center;
}
.Pixso-instance-5976_53874 .stroke-wrapper-5976_52059 {
    width: 44px;
    height: 40px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5976_53874 .stroke-5976_52059 {
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 1px 0px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5976_53879 .Pixso-frame-5976_52059 {
    width: 100%;
    height: 100%;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 6px;
    align-items: center;
}
.Pixso-instance-5976_53879 .stroke-wrapper-5976_52059 {
    width: 44px;
    height: 40px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5976_53879 .stroke-5976_52059 {
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 1px 0px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5976_53854 .Pixso-frame-5976_52061 {
    width: 100%;
    height: 38px;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: row;
    gap: 6px;
    align-items: center;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5976_53859 .Pixso-frame-5976_52061 {
    width: 100%;
    height: 38px;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: row;
    gap: 6px;
    align-items: center;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5976_53864 .Pixso-frame-5976_52061 {
    width: 100%;
    height: 38px;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: row;
    gap: 6px;
    align-items: center;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5976_53869 .Pixso-frame-5976_52061 {
    width: 100%;
    height: 38px;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: row;
    gap: 6px;
    align-items: center;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5976_53874 .Pixso-frame-5976_52061 {
    width: 100%;
    height: 38px;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: row;
    gap: 6px;
    align-items: center;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5976_53879 .Pixso-frame-5976_52061 {
    width: 100%;
    height: 38px;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: row;
    gap: 6px;
    align-items: center;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5976_53854 .Pixso-paragraph-5976_52062 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5976_53859 .Pixso-paragraph-5976_52062 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5976_53864 .Pixso-paragraph-5976_52062 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5976_53869 .Pixso-paragraph-5976_52062 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5976_53874 .Pixso-paragraph-5976_52062 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5976_53879 .Pixso-paragraph-5976_52062 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5976_53854 .Pixso-frame-5976_52063 {
    width: 100%;
    height: 100%;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 6px;
    align-items: center;
}
.Pixso-instance-5976_53854 .stroke-wrapper-5976_52063 {
    width: 84px;
    height: 40px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5976_53854 .stroke-5976_52063 {
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 0px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5976_53859 .Pixso-frame-5976_52063 {
    width: 100%;
    height: 100%;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 6px;
    align-items: center;
}
.Pixso-instance-5976_53859 .stroke-wrapper-5976_52063 {
    width: 84px;
    height: 40px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5976_53859 .stroke-5976_52063 {
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 0px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5976_53864 .Pixso-frame-5976_52063 {
    width: 100%;
    height: 100%;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 6px;
    align-items: center;
}
.Pixso-instance-5976_53864 .stroke-wrapper-5976_52063 {
    width: 84px;
    height: 40px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5976_53864 .stroke-5976_52063 {
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 0px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5976_53869 .Pixso-frame-5976_52063 {
    width: 100%;
    height: 100%;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 6px;
    align-items: center;
}
.Pixso-instance-5976_53869 .stroke-wrapper-5976_52063 {
    width: 84px;
    height: 40px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5976_53869 .stroke-5976_52063 {
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 0px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5976_53874 .Pixso-frame-5976_52063 {
    width: 100%;
    height: 100%;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 6px;
    align-items: center;
}
.Pixso-instance-5976_53874 .stroke-wrapper-5976_52063 {
    width: 84px;
    height: 40px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5976_53874 .stroke-5976_52063 {
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 0px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5976_53879 .Pixso-frame-5976_52063 {
    width: 100%;
    height: 100%;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 6px;
    align-items: center;
}
.Pixso-instance-5976_53879 .stroke-wrapper-5976_52063 {
    width: 84px;
    height: 40px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5976_53879 .stroke-5976_52063 {
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 0px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5976_53874 .Pixso-paragraph-5976_52064 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5609_20235 .Pixso-symbol-5607_19283 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 10px 12px 10px 12px;
    min-height: 48px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5609_20235 .stroke-wrapper-5607_19283 {
    width: 320px;
    height: 48px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5609_20235 .stroke-5607_19283 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5609_20245 .Pixso-symbol-5607_19283 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 10px 12px 10px 12px;
    min-height: 48px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5609_20245 .stroke-wrapper-5607_19283 {
    width: 320px;
    height: 48px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5609_20245 .stroke-5607_19283 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5609_20250 .Pixso-symbol-5607_19283 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 10px 12px 10px 12px;
    min-height: 48px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5609_20250 .stroke-wrapper-5607_19283 {
    width: 320px;
    height: 48px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5609_20250 .stroke-5607_19283 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5609_20255 .Pixso-symbol-5607_19283 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 10px 12px 10px 12px;
    min-height: 48px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5609_20255 .stroke-wrapper-5607_19283 {
    width: 320px;
    height: 48px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5609_20255 .stroke-5607_19283 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5609_20260 .Pixso-symbol-5607_19283 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 10px 12px 10px 12px;
    min-height: 48px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5609_20260 .stroke-wrapper-5607_19283 {
    width: 320px;
    height: 48px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5609_20260 .stroke-5607_19283 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5609_20240 .Pixso-symbol-5607_19283 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 10px 12px 10px 12px;
    min-height: 48px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5609_20240 .stroke-wrapper-5607_19283 {
    width: 320px;
    height: 48px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5609_20240 .stroke-5607_19283 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5609_20235 .Pixso-paragraph-5607_19286 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5609_20245 .Pixso-paragraph-5607_19286 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5609_20250 .Pixso-paragraph-5607_19286 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5609_20255 .Pixso-paragraph-5607_19286 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5609_20260 .Pixso-paragraph-5607_19286 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5609_20240 .Pixso-paragraph-5607_19286 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5609_20235 .Pixso-frame-5607_19315 {
    width: 64px;
    height: 24px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
}
.Pixso-instance-5609_20245 .Pixso-frame-5607_19315 {
    width: 64px;
    height: 24px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
}
.Pixso-instance-5609_20250 .Pixso-frame-5607_19315 {
    width: 64px;
    height: 24px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
}
.Pixso-instance-5609_20255 .Pixso-frame-5607_19315 {
    width: 64px;
    height: 24px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
}
.Pixso-instance-5609_20260 .Pixso-frame-5607_19315 {
    width: 64px;
    height: 24px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
}
.Pixso-instance-5609_20240 .Pixso-frame-5607_19315 {
    width: 64px;
    height: 24px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
}
.Pixso-instance-5609_20235 .Pixso-instance-5607_19306 {
    width: 36px;
    height: 24px;
}
.Pixso-instance-5609_20245 .Pixso-instance-5607_19306 {
    width: 36px;
    height: 24px;
}
.Pixso-instance-5609_20250 .Pixso-instance-5607_19306 {
    width: 36px;
    height: 24px;
}
.Pixso-instance-5609_20255 .Pixso-instance-5607_19306 {
    width: 36px;
    height: 24px;
}
.Pixso-instance-5609_20260 .Pixso-instance-5607_19306 {
    width: 36px;
    height: 24px;
}
.Pixso-instance-5609_20240 .Pixso-instance-5607_19306 {
    width: 36px;
    height: 24px;
}
.Pixso-instance-5609_20235 .Pixso-instance-5607_19313 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5609_20245 .Pixso-instance-5607_19313 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5609_20250 .Pixso-instance-5607_19313 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5609_20255 .Pixso-instance-5607_19313 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5609_20260 .Pixso-instance-5607_19313 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5609_20240 .Pixso-instance-5607_19313 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5976_53884 .Pixso-symbol-5976_52066 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 8px 12px 8px 12px;
    min-height: 40px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5976_53884 .stroke-wrapper-5976_52066 {
    width: 320px;
    height: 40px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5976_53884 .stroke-5976_52066 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5976_53889 .Pixso-symbol-5976_52066 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 8px 12px 8px 12px;
    min-height: 40px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5976_53889 .stroke-wrapper-5976_52066 {
    width: 320px;
    height: 40px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5976_53889 .stroke-5976_52066 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5976_53894 .Pixso-symbol-5976_52066 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 8px 12px 8px 12px;
    min-height: 40px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5976_53894 .stroke-wrapper-5976_52066 {
    width: 320px;
    height: 40px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5976_53894 .stroke-5976_52066 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5976_53899 .Pixso-symbol-5976_52066 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 8px 12px 8px 12px;
    min-height: 40px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5976_53899 .stroke-wrapper-5976_52066 {
    width: 320px;
    height: 40px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5976_53899 .stroke-5976_52066 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5976_53904 .Pixso-symbol-5976_52066 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 8px 12px 8px 12px;
    min-height: 40px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5976_53904 .stroke-wrapper-5976_52066 {
    width: 320px;
    height: 40px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5976_53904 .stroke-5976_52066 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5976_53909 .Pixso-symbol-5976_52066 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 8px 12px 8px 12px;
    min-height: 40px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5976_53909 .stroke-wrapper-5976_52066 {
    width: 320px;
    height: 40px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5976_53909 .stroke-5976_52066 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5976_53884 .Pixso-paragraph-5976_52067 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5976_53889 .Pixso-paragraph-5976_52067 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5976_53894 .Pixso-paragraph-5976_52067 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5976_53899 .Pixso-paragraph-5976_52067 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5976_53904 .Pixso-paragraph-5976_52067 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5976_53909 .Pixso-paragraph-5976_52067 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5976_53884 .Pixso-frame-5976_52068 {
    width: 64px;
    height: 24px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
}
.Pixso-instance-5976_53889 .Pixso-frame-5976_52068 {
    width: 64px;
    height: 24px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
}
.Pixso-instance-5976_53894 .Pixso-frame-5976_52068 {
    width: 64px;
    height: 24px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
}
.Pixso-instance-5976_53899 .Pixso-frame-5976_52068 {
    width: 64px;
    height: 24px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
}
.Pixso-instance-5976_53904 .Pixso-frame-5976_52068 {
    width: 64px;
    height: 24px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
}
.Pixso-instance-5976_53909 .Pixso-frame-5976_52068 {
    width: 64px;
    height: 24px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
}
.Pixso-instance-5976_53884 .Pixso-instance-5976_52069 {
    width: 36px;
    height: 24px;
}
.Pixso-instance-5976_53889 .Pixso-instance-5976_52069 {
    width: 36px;
    height: 24px;
}
.Pixso-instance-5976_53894 .Pixso-instance-5976_52069 {
    width: 36px;
    height: 24px;
}
.Pixso-instance-5976_53899 .Pixso-instance-5976_52069 {
    width: 36px;
    height: 24px;
}
.Pixso-instance-5976_53904 .Pixso-instance-5976_52069 {
    width: 36px;
    height: 24px;
}
.Pixso-instance-5976_53909 .Pixso-instance-5976_52069 {
    width: 36px;
    height: 24px;
}
.Pixso-instance-5976_53884 .Pixso-instance-5976_52070 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5976_53889 .Pixso-instance-5976_52070 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5976_53894 .Pixso-instance-5976_52070 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5976_53899 .Pixso-instance-5976_52070 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5976_53904 .Pixso-instance-5976_52070 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5976_53909 .Pixso-instance-5976_52070 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5609_20499 .Pixso-symbol-5607_19353 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 10px 12px 10px 12px;
    min-height: 48px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5609_20499 .stroke-wrapper-5607_19353 {
    width: 320px;
    height: 48px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5609_20499 .stroke-5607_19353 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5609_20509 .Pixso-symbol-5607_19353 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 10px 12px 10px 12px;
    min-height: 48px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5609_20509 .stroke-wrapper-5607_19353 {
    width: 320px;
    height: 48px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5609_20509 .stroke-5607_19353 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5609_20514 .Pixso-symbol-5607_19353 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 10px 12px 10px 12px;
    min-height: 48px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5609_20514 .stroke-wrapper-5607_19353 {
    width: 320px;
    height: 48px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5609_20514 .stroke-5607_19353 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5609_20519 .Pixso-symbol-5607_19353 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 10px 12px 10px 12px;
    min-height: 48px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5609_20519 .stroke-wrapper-5607_19353 {
    width: 320px;
    height: 48px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5609_20519 .stroke-5607_19353 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5609_20524 .Pixso-symbol-5607_19353 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 10px 12px 10px 12px;
    min-height: 48px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5609_20524 .stroke-wrapper-5607_19353 {
    width: 320px;
    height: 48px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5609_20524 .stroke-5607_19353 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5609_20504 .Pixso-symbol-5607_19353 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 10px 12px 10px 12px;
    min-height: 48px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5609_20504 .stroke-wrapper-5607_19353 {
    width: 320px;
    height: 48px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5609_20504 .stroke-5607_19353 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5609_20499 .Pixso-paragraph-5607_19354 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5609_20509 .Pixso-paragraph-5607_19354 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5609_20514 .Pixso-paragraph-5607_19354 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5609_20519 .Pixso-paragraph-5607_19354 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5609_20524 .Pixso-paragraph-5607_19354 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5609_20504 .Pixso-paragraph-5607_19354 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5976_53914 .Pixso-symbol-5976_52071 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 8px 12px 8px 12px;
    min-height: 40px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5976_53914 .stroke-wrapper-5976_52071 {
    width: 320px;
    height: 40px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5976_53914 .stroke-5976_52071 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5976_53919 .Pixso-symbol-5976_52071 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 8px 12px 8px 12px;
    min-height: 40px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5976_53919 .stroke-wrapper-5976_52071 {
    width: 320px;
    height: 40px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5976_53919 .stroke-5976_52071 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5976_53924 .Pixso-symbol-5976_52071 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 8px 12px 8px 12px;
    min-height: 40px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5976_53924 .stroke-wrapper-5976_52071 {
    width: 320px;
    height: 40px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5976_53924 .stroke-5976_52071 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5976_53929 .Pixso-symbol-5976_52071 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 8px 12px 8px 12px;
    min-height: 40px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5976_53929 .stroke-wrapper-5976_52071 {
    width: 320px;
    height: 40px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5976_53929 .stroke-5976_52071 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5976_53934 .Pixso-symbol-5976_52071 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 8px 12px 8px 12px;
    min-height: 40px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5976_53934 .stroke-wrapper-5976_52071 {
    width: 320px;
    height: 40px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5976_53934 .stroke-5976_52071 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5976_53939 .Pixso-symbol-5976_52071 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 8px 12px 8px 12px;
    min-height: 40px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5976_53939 .stroke-wrapper-5976_52071 {
    width: 320px;
    height: 40px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5976_53939 .stroke-5976_52071 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5976_53914 .Pixso-paragraph-5976_52072 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5976_53919 .Pixso-paragraph-5976_52072 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5976_53924 .Pixso-paragraph-5976_52072 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5976_53929 .Pixso-paragraph-5976_52072 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5976_53934 .Pixso-paragraph-5976_52072 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5976_53939 .Pixso-paragraph-5976_52072 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5609_20661 .Pixso-symbol-5607_19379 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    align-items: center;
    min-height: 48px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5609_20661 .stroke-wrapper-5607_19379 {
    width: 320px;
    height: 48px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5609_20661 .stroke-5607_19379 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5609_20671 .Pixso-symbol-5607_19379 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    align-items: center;
    min-height: 48px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5609_20671 .stroke-wrapper-5607_19379 {
    width: 320px;
    height: 48px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5609_20671 .stroke-5607_19379 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5609_20676 .Pixso-symbol-5607_19379 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    align-items: center;
    min-height: 48px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5609_20676 .stroke-wrapper-5607_19379 {
    width: 320px;
    height: 48px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5609_20676 .stroke-5607_19379 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5609_20681 .Pixso-symbol-5607_19379 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    align-items: center;
    min-height: 48px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5609_20681 .stroke-wrapper-5607_19379 {
    width: 320px;
    height: 48px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5609_20681 .stroke-5607_19379 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5609_20686 .Pixso-symbol-5607_19379 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    align-items: center;
    min-height: 48px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5609_20686 .stroke-wrapper-5607_19379 {
    width: 320px;
    height: 48px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5609_20686 .stroke-5607_19379 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5609_20666 .Pixso-symbol-5607_19379 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    align-items: center;
    min-height: 48px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5609_20666 .stroke-wrapper-5607_19379 {
    width: 320px;
    height: 48px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5609_20666 .stroke-5607_19379 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5609_20661 .Pixso-frame-5607_19383 {
    width: 100%;
    height: 100%;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 6px;
    align-items: center;
}
.Pixso-instance-5609_20661 .stroke-wrapper-5607_19383 {
    width: 84px;
    height: 48px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5609_20661 .stroke-5607_19383 {
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 1px 0px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5609_20671 .Pixso-frame-5607_19383 {
    width: 100%;
    height: 100%;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 6px;
    align-items: center;
}
.Pixso-instance-5609_20671 .stroke-wrapper-5607_19383 {
    width: 84px;
    height: 48px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5609_20671 .stroke-5607_19383 {
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 1px 0px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5609_20676 .Pixso-frame-5607_19383 {
    width: 100%;
    height: 100%;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 6px;
    align-items: center;
}
.Pixso-instance-5609_20676 .stroke-wrapper-5607_19383 {
    width: 84px;
    height: 48px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5609_20676 .stroke-5607_19383 {
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 1px 0px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5609_20681 .Pixso-frame-5607_19383 {
    width: 100%;
    height: 100%;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 6px;
    align-items: center;
}
.Pixso-instance-5609_20681 .stroke-wrapper-5607_19383 {
    width: 84px;
    height: 48px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5609_20681 .stroke-5607_19383 {
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 1px 0px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5609_20686 .Pixso-frame-5607_19383 {
    width: 100%;
    height: 100%;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 6px;
    align-items: center;
}
.Pixso-instance-5609_20686 .stroke-wrapper-5607_19383 {
    width: 84px;
    height: 48px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5609_20686 .stroke-5607_19383 {
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 1px 0px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5609_20666 .Pixso-frame-5607_19383 {
    width: 100%;
    height: 100%;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 6px;
    align-items: center;
}
.Pixso-instance-5609_20666 .stroke-wrapper-5607_19383 {
    width: 84px;
    height: 48px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5609_20666 .stroke-5607_19383 {
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 1px 0px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5609_20686 .Pixso-paragraph-5607_19384 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5609_20661 .Pixso-frame-5607_19389 .frame-content-5607_19389 {
    padding: 12px 12px 12px 12px;
}
.Pixso-instance-5609_20661 .Pixso-frame-5607_19389 {
    width: 100%;
    height: 100%;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: row;
    gap: 6px;
    align-items: center;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5609_20661 .stroke-wrapper-5607_19389 {
    width: 100%;
    height: 46px;
    display: flex;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5609_20661 .stroke-5607_19389 {
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 1px 0px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5609_20671 .Pixso-frame-5607_19389 .frame-content-5607_19389 {
    padding: 12px 12px 12px 12px;
}
.Pixso-instance-5609_20671 .Pixso-frame-5607_19389 {
    width: 100%;
    height: 100%;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: row;
    gap: 6px;
    align-items: center;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5609_20671 .stroke-wrapper-5607_19389 {
    width: 100%;
    height: 46px;
    display: flex;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5609_20671 .stroke-5607_19389 {
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 1px 0px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5609_20676 .Pixso-frame-5607_19389 .frame-content-5607_19389 {
    padding: 12px 12px 12px 12px;
}
.Pixso-instance-5609_20676 .Pixso-frame-5607_19389 {
    width: 100%;
    height: 100%;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: row;
    gap: 6px;
    align-items: center;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5609_20676 .stroke-wrapper-5607_19389 {
    width: 100%;
    height: 46px;
    display: flex;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5609_20676 .stroke-5607_19389 {
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 1px 0px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5609_20681 .Pixso-frame-5607_19389 .frame-content-5607_19389 {
    padding: 12px 12px 12px 12px;
}
.Pixso-instance-5609_20681 .Pixso-frame-5607_19389 {
    width: 100%;
    height: 100%;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: row;
    gap: 6px;
    align-items: center;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5609_20681 .stroke-wrapper-5607_19389 {
    width: 100%;
    height: 46px;
    display: flex;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5609_20681 .stroke-5607_19389 {
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 1px 0px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5609_20686 .Pixso-frame-5607_19389 .frame-content-5607_19389 {
    padding: 12px 12px 12px 12px;
}
.Pixso-instance-5609_20686 .Pixso-frame-5607_19389 {
    width: 100%;
    height: 100%;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: row;
    gap: 6px;
    align-items: center;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5609_20686 .stroke-wrapper-5607_19389 {
    width: 100%;
    height: 46px;
    display: flex;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5609_20686 .stroke-5607_19389 {
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 1px 0px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5609_20666 .Pixso-frame-5607_19389 .frame-content-5607_19389 {
    padding: 12px 12px 12px 12px;
}
.Pixso-instance-5609_20666 .Pixso-frame-5607_19389 {
    width: 100%;
    height: 100%;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: row;
    gap: 6px;
    align-items: center;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5609_20666 .stroke-wrapper-5607_19389 {
    width: 100%;
    height: 46px;
    display: flex;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5609_20666 .stroke-5607_19389 {
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 1px 0px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5609_20661 .Pixso-paragraph-5607_19380 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5609_20671 .Pixso-paragraph-5607_19380 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5609_20676 .Pixso-paragraph-5607_19380 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5609_20681 .Pixso-paragraph-5607_19380 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5609_20686 .Pixso-paragraph-5607_19380 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5609_20666 .Pixso-paragraph-5607_19380 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5609_20661 .Pixso-instance-5607_19387 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5609_20671 .Pixso-instance-5607_19387 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5609_20676 .Pixso-instance-5607_19387 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5609_20681 .Pixso-instance-5607_19387 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5609_20686 .Pixso-instance-5607_19387 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5609_20666 .Pixso-instance-5607_19387 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5976_53944 .Pixso-symbol-5976_52074 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    align-items: center;
    min-height: 40px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5976_53944 .stroke-wrapper-5976_52074 {
    width: 320px;
    height: 40px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5976_53944 .stroke-5976_52074 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5976_53949 .Pixso-symbol-5976_52074 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    align-items: center;
    min-height: 40px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5976_53949 .stroke-wrapper-5976_52074 {
    width: 320px;
    height: 40px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5976_53949 .stroke-5976_52074 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5976_53954 .Pixso-symbol-5976_52074 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    align-items: center;
    min-height: 40px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5976_53954 .stroke-wrapper-5976_52074 {
    width: 320px;
    height: 40px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5976_53954 .stroke-5976_52074 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5976_53959 .Pixso-symbol-5976_52074 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    align-items: center;
    min-height: 40px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5976_53959 .stroke-wrapper-5976_52074 {
    width: 320px;
    height: 40px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5976_53959 .stroke-5976_52074 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5976_53964 .Pixso-symbol-5976_52074 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    align-items: center;
    min-height: 40px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5976_53964 .stroke-wrapper-5976_52074 {
    width: 320px;
    height: 40px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5976_53964 .stroke-5976_52074 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5976_53969 .Pixso-symbol-5976_52074 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    align-items: center;
    min-height: 40px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5976_53969 .stroke-wrapper-5976_52074 {
    width: 320px;
    height: 40px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5976_53969 .stroke-5976_52074 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5976_53944 .Pixso-frame-5976_52075 {
    width: 100%;
    height: 100%;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 6px;
    align-items: center;
}
.Pixso-instance-5976_53944 .stroke-wrapper-5976_52075 {
    width: 84px;
    height: 40px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5976_53944 .stroke-5976_52075 {
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 1px 0px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5976_53949 .Pixso-frame-5976_52075 {
    width: 100%;
    height: 100%;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 6px;
    align-items: center;
}
.Pixso-instance-5976_53949 .stroke-wrapper-5976_52075 {
    width: 84px;
    height: 40px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5976_53949 .stroke-5976_52075 {
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 1px 0px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5976_53954 .Pixso-frame-5976_52075 {
    width: 100%;
    height: 100%;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 6px;
    align-items: center;
}
.Pixso-instance-5976_53954 .stroke-wrapper-5976_52075 {
    width: 84px;
    height: 40px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5976_53954 .stroke-5976_52075 {
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 1px 0px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5976_53959 .Pixso-frame-5976_52075 {
    width: 100%;
    height: 100%;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 6px;
    align-items: center;
}
.Pixso-instance-5976_53959 .stroke-wrapper-5976_52075 {
    width: 84px;
    height: 40px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5976_53959 .stroke-5976_52075 {
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 1px 0px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5976_53964 .Pixso-frame-5976_52075 {
    width: 100%;
    height: 100%;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 6px;
    align-items: center;
}
.Pixso-instance-5976_53964 .stroke-wrapper-5976_52075 {
    width: 84px;
    height: 40px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5976_53964 .stroke-5976_52075 {
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 1px 0px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5976_53969 .Pixso-frame-5976_52075 {
    width: 100%;
    height: 100%;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 6px;
    align-items: center;
}
.Pixso-instance-5976_53969 .stroke-wrapper-5976_52075 {
    width: 84px;
    height: 40px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5976_53969 .stroke-5976_52075 {
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 1px 0px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5976_53964 .Pixso-paragraph-5976_52076 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5976_53944 .Pixso-frame-5976_52077 {
    width: 100%;
    height: 100%;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: row;
    gap: 6px;
    align-items: center;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5976_53944 .stroke-wrapper-5976_52077 {
    width: 100%;
    height: 38px;
    display: flex;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5976_53944 .stroke-5976_52077 {
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 1px 0px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5976_53949 .Pixso-frame-5976_52077 {
    width: 100%;
    height: 100%;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: row;
    gap: 6px;
    align-items: center;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5976_53949 .stroke-wrapper-5976_52077 {
    width: 100%;
    height: 38px;
    display: flex;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5976_53949 .stroke-5976_52077 {
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 1px 0px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5976_53954 .Pixso-frame-5976_52077 {
    width: 100%;
    height: 100%;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: row;
    gap: 6px;
    align-items: center;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5976_53954 .stroke-wrapper-5976_52077 {
    width: 100%;
    height: 38px;
    display: flex;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5976_53954 .stroke-5976_52077 {
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 1px 0px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5976_53959 .Pixso-frame-5976_52077 {
    width: 100%;
    height: 100%;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: row;
    gap: 6px;
    align-items: center;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5976_53959 .stroke-wrapper-5976_52077 {
    width: 100%;
    height: 38px;
    display: flex;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5976_53959 .stroke-5976_52077 {
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 1px 0px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5976_53964 .Pixso-frame-5976_52077 {
    width: 100%;
    height: 100%;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: row;
    gap: 6px;
    align-items: center;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5976_53964 .stroke-wrapper-5976_52077 {
    width: 100%;
    height: 38px;
    display: flex;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5976_53964 .stroke-5976_52077 {
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 1px 0px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5976_53969 .Pixso-frame-5976_52077 {
    width: 100%;
    height: 100%;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: row;
    gap: 6px;
    align-items: center;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5976_53969 .stroke-wrapper-5976_52077 {
    width: 100%;
    height: 38px;
    display: flex;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5976_53969 .stroke-5976_52077 {
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 1px 0px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5976_53944 .Pixso-paragraph-5976_52078 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5976_53949 .Pixso-paragraph-5976_52078 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5976_53954 .Pixso-paragraph-5976_52078 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5976_53959 .Pixso-paragraph-5976_52078 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5976_53964 .Pixso-paragraph-5976_52078 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5976_53969 .Pixso-paragraph-5976_52078 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5976_53944 .Pixso-instance-5976_52079 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5976_53949 .Pixso-instance-5976_52079 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5976_53954 .Pixso-instance-5976_52079 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5976_53959 .Pixso-instance-5976_52079 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5976_53964 .Pixso-instance-5976_52079 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5976_53969 .Pixso-instance-5976_52079 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5609_20811 .Pixso-symbol-5607_19415 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 12px 12px 12px 12px;
    min-height: 48px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5609_20811 .stroke-wrapper-5607_19415 {
    width: 320px;
    height: 48px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5609_20811 .stroke-5607_19415 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5609_20821 .Pixso-symbol-5607_19415 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 12px 12px 12px 12px;
    min-height: 48px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5609_20821 .stroke-wrapper-5607_19415 {
    width: 320px;
    height: 48px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5609_20821 .stroke-5607_19415 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5609_20826 .Pixso-symbol-5607_19415 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 12px 12px 12px 12px;
    min-height: 48px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5609_20826 .stroke-wrapper-5607_19415 {
    width: 320px;
    height: 48px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5609_20826 .stroke-5607_19415 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5609_20831 .Pixso-symbol-5607_19415 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 12px 12px 12px 12px;
    min-height: 48px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5609_20831 .stroke-wrapper-5607_19415 {
    width: 320px;
    height: 48px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5609_20831 .stroke-5607_19415 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5609_20836 .Pixso-symbol-5607_19415 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 12px 12px 12px 12px;
    min-height: 48px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5609_20836 .stroke-wrapper-5607_19415 {
    width: 320px;
    height: 48px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5609_20836 .stroke-5607_19415 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5609_20816 .Pixso-symbol-5607_19415 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 12px 12px 12px 12px;
    min-height: 48px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5609_20816 .stroke-wrapper-5607_19415 {
    width: 320px;
    height: 48px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5609_20816 .stroke-5607_19415 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5609_20811 .Pixso-frame-5607_19416 {
    width: 100%;
    height: 22px;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5609_20821 .Pixso-frame-5607_19416 {
    width: 100%;
    height: 22px;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5609_20826 .Pixso-frame-5607_19416 {
    width: 100%;
    height: 22px;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5609_20831 .Pixso-frame-5607_19416 {
    width: 100%;
    height: 22px;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5609_20836 .Pixso-frame-5607_19416 {
    width: 100%;
    height: 22px;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5609_20816 .Pixso-frame-5607_19416 {
    width: 100%;
    height: 22px;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5609_20811 .Pixso-paragraph-5607_19418 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5609_20821 .Pixso-paragraph-5607_19418 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5609_20826 .Pixso-paragraph-5607_19418 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5609_20831 .Pixso-paragraph-5607_19418 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5609_20836 .Pixso-paragraph-5607_19418 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5609_20816 .Pixso-paragraph-5607_19418 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5609_20811 .Pixso-instance-5607_19419 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5609_20821 .Pixso-instance-5607_19419 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5609_20826 .Pixso-instance-5607_19419 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5609_20831 .Pixso-instance-5607_19419 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5609_20836 .Pixso-instance-5607_19419 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5609_20816 .Pixso-instance-5607_19419 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5976_53974 .Pixso-symbol-5976_52080 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 8px 12px 8px 12px;
    min-height: 40px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5976_53974 .stroke-wrapper-5976_52080 {
    width: 320px;
    height: 40px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5976_53974 .stroke-5976_52080 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5976_53984 .Pixso-symbol-5976_52080 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 8px 12px 8px 12px;
    min-height: 40px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5976_53984 .stroke-wrapper-5976_52080 {
    width: 320px;
    height: 40px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5976_53984 .stroke-5976_52080 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5976_53994 .Pixso-symbol-5976_52080 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 8px 12px 8px 12px;
    min-height: 40px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5976_53994 .stroke-wrapper-5976_52080 {
    width: 320px;
    height: 40px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5976_53994 .stroke-5976_52080 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5976_54004 .Pixso-symbol-5976_52080 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 8px 12px 8px 12px;
    min-height: 40px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5976_54004 .stroke-wrapper-5976_52080 {
    width: 320px;
    height: 40px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5976_54004 .stroke-5976_52080 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5976_54014 .Pixso-symbol-5976_52080 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 8px 12px 8px 12px;
    min-height: 40px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5976_54014 .stroke-wrapper-5976_52080 {
    width: 320px;
    height: 40px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5976_54014 .stroke-5976_52080 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5976_54024 .Pixso-symbol-5976_52080 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 8px 12px 8px 12px;
    min-height: 40px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5976_54024 .stroke-wrapper-5976_52080 {
    width: 320px;
    height: 40px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5976_54024 .stroke-5976_52080 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5976_53974 .Pixso-frame-5976_52081 {
    width: 100%;
    height: 22px;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5976_53984 .Pixso-frame-5976_52081 {
    width: 100%;
    height: 22px;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5976_53994 .Pixso-frame-5976_52081 {
    width: 100%;
    height: 22px;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5976_54004 .Pixso-frame-5976_52081 {
    width: 100%;
    height: 22px;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5976_54014 .Pixso-frame-5976_52081 {
    width: 100%;
    height: 22px;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5976_54024 .Pixso-frame-5976_52081 {
    width: 100%;
    height: 22px;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5976_53974 .Pixso-paragraph-5976_52083 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5976_53984 .Pixso-paragraph-5976_52083 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5976_53994 .Pixso-paragraph-5976_52083 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5976_54004 .Pixso-paragraph-5976_52083 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5976_54014 .Pixso-paragraph-5976_52083 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5976_54024 .Pixso-paragraph-5976_52083 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5976_53974 .Pixso-instance-5976_52084 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5976_53984 .Pixso-instance-5976_52084 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5976_53994 .Pixso-instance-5976_52084 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5976_54004 .Pixso-instance-5976_52084 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5976_54014 .Pixso-instance-5976_52084 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5976_54024 .Pixso-instance-5976_52084 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5609_21051 .Pixso-symbol-5607_19447 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    align-items: center;
    min-height: 48px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5609_21051 .stroke-wrapper-5607_19447 {
    width: 320px;
    height: 48px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5609_21051 .stroke-5607_19447 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5609_21061 .Pixso-symbol-5607_19447 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    align-items: center;
    min-height: 48px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5609_21061 .stroke-wrapper-5607_19447 {
    width: 320px;
    height: 48px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5609_21061 .stroke-5607_19447 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5609_21066 .Pixso-symbol-5607_19447 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    align-items: center;
    min-height: 48px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5609_21066 .stroke-wrapper-5607_19447 {
    width: 320px;
    height: 48px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5609_21066 .stroke-5607_19447 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5609_21071 .Pixso-symbol-5607_19447 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    align-items: center;
    min-height: 48px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5609_21071 .stroke-wrapper-5607_19447 {
    width: 320px;
    height: 48px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5609_21071 .stroke-5607_19447 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5609_21076 .Pixso-symbol-5607_19447 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    align-items: center;
    min-height: 48px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5609_21076 .stroke-wrapper-5607_19447 {
    width: 320px;
    height: 48px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5609_21076 .stroke-5607_19447 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5609_21056 .Pixso-symbol-5607_19447 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    align-items: center;
    min-height: 48px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5609_21056 .stroke-wrapper-5607_19447 {
    width: 320px;
    height: 48px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5609_21056 .stroke-5607_19447 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5609_21051 .Pixso-frame-5607_19473 {
    width: 100%;
    height: 100%;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 6px;
    align-items: center;
}
.Pixso-instance-5609_21051 .stroke-wrapper-5607_19473 {
    width: 70px;
    height: 48px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5609_21051 .stroke-5607_19473 {
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 1px 0px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5609_21061 .Pixso-frame-5607_19473 {
    width: 100%;
    height: 100%;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 6px;
    align-items: center;
}
.Pixso-instance-5609_21061 .stroke-wrapper-5607_19473 {
    width: 70px;
    height: 48px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5609_21061 .stroke-5607_19473 {
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 1px 0px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5609_21066 .Pixso-frame-5607_19473 {
    width: 100%;
    height: 100%;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 6px;
    align-items: center;
}
.Pixso-instance-5609_21066 .stroke-wrapper-5607_19473 {
    width: 70px;
    height: 48px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5609_21066 .stroke-5607_19473 {
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 1px 0px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5609_21071 .Pixso-frame-5607_19473 {
    width: 100%;
    height: 100%;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 6px;
    align-items: center;
}
.Pixso-instance-5609_21071 .stroke-wrapper-5607_19473 {
    width: 70px;
    height: 48px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5609_21071 .stroke-5607_19473 {
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 1px 0px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5609_21076 .Pixso-frame-5607_19473 {
    width: 100%;
    height: 100%;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 6px;
    align-items: center;
}
.Pixso-instance-5609_21076 .stroke-wrapper-5607_19473 {
    width: 70px;
    height: 48px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5609_21076 .stroke-5607_19473 {
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 1px 0px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5609_21056 .Pixso-frame-5607_19473 {
    width: 100%;
    height: 100%;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 6px;
    align-items: center;
}
.Pixso-instance-5609_21056 .stroke-wrapper-5607_19473 {
    width: 70px;
    height: 48px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5609_21056 .stroke-5607_19473 {
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 1px 0px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5609_21051 .Pixso-frame-5607_19474 .frame-content-5607_19474 {
    padding: 12px 12px 12px 12px;
}
.Pixso-instance-5609_21051 .Pixso-frame-5607_19474 {
    width: 100%;
    height: 46px;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: row;
    gap: 6px;
    align-items: center;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5609_21061 .Pixso-frame-5607_19474 .frame-content-5607_19474 {
    padding: 12px 12px 12px 12px;
}
.Pixso-instance-5609_21061 .Pixso-frame-5607_19474 {
    width: 100%;
    height: 46px;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: row;
    gap: 6px;
    align-items: center;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5609_21066 .Pixso-frame-5607_19474 .frame-content-5607_19474 {
    padding: 12px 12px 12px 12px;
}
.Pixso-instance-5609_21066 .Pixso-frame-5607_19474 {
    width: 100%;
    height: 46px;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: row;
    gap: 6px;
    align-items: center;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5609_21071 .Pixso-frame-5607_19474 .frame-content-5607_19474 {
    padding: 12px 12px 12px 12px;
}
.Pixso-instance-5609_21071 .Pixso-frame-5607_19474 {
    width: 100%;
    height: 46px;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: row;
    gap: 6px;
    align-items: center;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5609_21076 .Pixso-frame-5607_19474 .frame-content-5607_19474 {
    padding: 12px 12px 12px 12px;
}
.Pixso-instance-5609_21076 .Pixso-frame-5607_19474 {
    width: 100%;
    height: 46px;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: row;
    gap: 6px;
    align-items: center;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5609_21056 .Pixso-frame-5607_19474 .frame-content-5607_19474 {
    padding: 12px 12px 12px 12px;
}
.Pixso-instance-5609_21056 .Pixso-frame-5607_19474 {
    width: 100%;
    height: 46px;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: row;
    gap: 6px;
    align-items: center;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5609_21051 .Pixso-paragraph-5607_19450 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5609_21061 .Pixso-paragraph-5607_19450 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5609_21066 .Pixso-paragraph-5607_19450 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5609_21071 .Pixso-paragraph-5607_19450 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5609_21076 .Pixso-paragraph-5607_19450 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5609_21056 .Pixso-paragraph-5607_19450 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5609_21051 .Pixso-paragraph-5607_19477 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5609_21061 .Pixso-paragraph-5607_19477 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5609_21066 .Pixso-paragraph-5607_19477 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5609_21071 .Pixso-paragraph-5607_19477 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5609_21076 .Pixso-paragraph-5607_19477 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5609_21056 .Pixso-paragraph-5607_19477 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5609_21051 .Pixso-instance-5607_19475 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5609_21061 .Pixso-instance-5607_19475 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5609_21066 .Pixso-instance-5607_19475 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5609_21071 .Pixso-instance-5607_19475 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5609_21076 .Pixso-instance-5607_19475 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5609_21056 .Pixso-instance-5607_19475 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5976_54034 .Pixso-symbol-5976_52085 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    align-items: center;
    min-height: 40px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5976_54034 .stroke-wrapper-5976_52085 {
    width: 320px;
    height: 40px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5976_54034 .stroke-5976_52085 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5976_54039 .Pixso-symbol-5976_52085 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    align-items: center;
    min-height: 40px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5976_54039 .stroke-wrapper-5976_52085 {
    width: 320px;
    height: 40px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5976_54039 .stroke-5976_52085 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5976_54044 .Pixso-symbol-5976_52085 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    align-items: center;
    min-height: 40px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5976_54044 .stroke-wrapper-5976_52085 {
    width: 320px;
    height: 40px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5976_54044 .stroke-5976_52085 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5976_54049 .Pixso-symbol-5976_52085 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    align-items: center;
    min-height: 40px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5976_54049 .stroke-wrapper-5976_52085 {
    width: 320px;
    height: 40px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5976_54049 .stroke-5976_52085 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5976_54054 .Pixso-symbol-5976_52085 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    align-items: center;
    min-height: 40px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5976_54054 .stroke-wrapper-5976_52085 {
    width: 320px;
    height: 40px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5976_54054 .stroke-5976_52085 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5976_54059 .Pixso-symbol-5976_52085 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    align-items: center;
    min-height: 40px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5976_54059 .stroke-wrapper-5976_52085 {
    width: 320px;
    height: 40px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5976_54059 .stroke-5976_52085 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5976_54034 .Pixso-frame-5976_52086 {
    width: 100%;
    height: 100%;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 6px;
    align-items: center;
}
.Pixso-instance-5976_54034 .stroke-wrapper-5976_52086 {
    width: 70px;
    height: 40px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5976_54034 .stroke-5976_52086 {
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 1px 0px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5976_54039 .Pixso-frame-5976_52086 {
    width: 100%;
    height: 100%;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 6px;
    align-items: center;
}
.Pixso-instance-5976_54039 .stroke-wrapper-5976_52086 {
    width: 70px;
    height: 40px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5976_54039 .stroke-5976_52086 {
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 1px 0px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5976_54044 .Pixso-frame-5976_52086 {
    width: 100%;
    height: 100%;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 6px;
    align-items: center;
}
.Pixso-instance-5976_54044 .stroke-wrapper-5976_52086 {
    width: 70px;
    height: 40px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5976_54044 .stroke-5976_52086 {
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 1px 0px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5976_54049 .Pixso-frame-5976_52086 {
    width: 100%;
    height: 100%;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 6px;
    align-items: center;
}
.Pixso-instance-5976_54049 .stroke-wrapper-5976_52086 {
    width: 70px;
    height: 40px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5976_54049 .stroke-5976_52086 {
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 1px 0px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5976_54054 .Pixso-frame-5976_52086 {
    width: 100%;
    height: 100%;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 6px;
    align-items: center;
}
.Pixso-instance-5976_54054 .stroke-wrapper-5976_52086 {
    width: 70px;
    height: 40px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5976_54054 .stroke-5976_52086 {
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 1px 0px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5976_54059 .Pixso-frame-5976_52086 {
    width: 100%;
    height: 100%;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 6px;
    align-items: center;
}
.Pixso-instance-5976_54059 .stroke-wrapper-5976_52086 {
    width: 70px;
    height: 40px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5976_54059 .stroke-5976_52086 {
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 1px 0px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5976_54034 .Pixso-frame-5976_52089 {
    width: 100%;
    height: 38px;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: row;
    gap: 6px;
    align-items: center;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5976_54039 .Pixso-frame-5976_52089 {
    width: 100%;
    height: 38px;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: row;
    gap: 6px;
    align-items: center;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5976_54044 .Pixso-frame-5976_52089 {
    width: 100%;
    height: 38px;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: row;
    gap: 6px;
    align-items: center;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5976_54049 .Pixso-frame-5976_52089 {
    width: 100%;
    height: 38px;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: row;
    gap: 6px;
    align-items: center;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5976_54054 .Pixso-frame-5976_52089 {
    width: 100%;
    height: 38px;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: row;
    gap: 6px;
    align-items: center;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5976_54059 .Pixso-frame-5976_52089 {
    width: 100%;
    height: 38px;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: row;
    gap: 6px;
    align-items: center;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5976_54034 .Pixso-paragraph-5976_52090 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5976_54039 .Pixso-paragraph-5976_52090 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5976_54044 .Pixso-paragraph-5976_52090 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5976_54049 .Pixso-paragraph-5976_52090 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5976_54054 .Pixso-paragraph-5976_52090 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5976_54059 .Pixso-paragraph-5976_52090 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5976_54034 .Pixso-paragraph-5976_52091 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5976_54039 .Pixso-paragraph-5976_52091 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5976_54044 .Pixso-paragraph-5976_52091 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5976_54049 .Pixso-paragraph-5976_52091 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5976_54054 .Pixso-paragraph-5976_52091 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5976_54059 .Pixso-paragraph-5976_52091 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5976_54034 .Pixso-instance-5976_52092 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5976_54039 .Pixso-instance-5976_52092 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5976_54044 .Pixso-instance-5976_52092 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5976_54049 .Pixso-instance-5976_52092 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5976_54054 .Pixso-instance-5976_52092 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5976_54059 .Pixso-instance-5976_52092 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5609_22112 .Pixso-symbol-5609_21323 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 12px 12px 12px 12px;
    min-height: 48px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5609_22112 .stroke-wrapper-5609_21323 {
    width: 320px;
    height: 48px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5609_22112 .stroke-5609_21323 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5609_22117 .Pixso-symbol-5609_21323 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 12px 12px 12px 12px;
    min-height: 48px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5609_22117 .stroke-wrapper-5609_21323 {
    width: 320px;
    height: 48px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5609_22117 .stroke-5609_21323 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5609_22122 .Pixso-symbol-5609_21323 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 12px 12px 12px 12px;
    min-height: 48px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5609_22122 .stroke-wrapper-5609_21323 {
    width: 320px;
    height: 48px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5609_22122 .stroke-5609_21323 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5609_22127 .Pixso-symbol-5609_21323 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 12px 12px 12px 12px;
    min-height: 48px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5609_22127 .stroke-wrapper-5609_21323 {
    width: 320px;
    height: 48px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5609_22127 .stroke-5609_21323 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5609_22132 .Pixso-symbol-5609_21323 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 12px 12px 12px 12px;
    min-height: 48px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5609_22132 .stroke-wrapper-5609_21323 {
    width: 320px;
    height: 48px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5609_22132 .stroke-5609_21323 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5609_22137 .Pixso-symbol-5609_21323 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 12px 12px 12px 12px;
    min-height: 48px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5609_22137 .stroke-wrapper-5609_21323 {
    width: 320px;
    height: 48px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5609_22137 .stroke-5609_21323 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5609_22112 .Pixso-frame-5609_21324 {
    width: 100%;
    height: 22px;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5609_22117 .Pixso-frame-5609_21324 {
    width: 100%;
    height: 22px;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5609_22122 .Pixso-frame-5609_21324 {
    width: 100%;
    height: 22px;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5609_22127 .Pixso-frame-5609_21324 {
    width: 100%;
    height: 22px;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5609_22132 .Pixso-frame-5609_21324 {
    width: 100%;
    height: 22px;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5609_22137 .Pixso-frame-5609_21324 {
    width: 100%;
    height: 22px;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5609_22112 .Pixso-instance-5609_21325 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5609_22117 .Pixso-instance-5609_21325 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5609_22122 .Pixso-instance-5609_21325 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5609_22127 .Pixso-instance-5609_21325 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5609_22132 .Pixso-instance-5609_21325 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5609_22137 .Pixso-instance-5609_21325 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5609_22112 .Pixso-paragraph-5609_21326 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5609_22117 .Pixso-paragraph-5609_21326 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5609_22122 .Pixso-paragraph-5609_21326 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5609_22127 .Pixso-paragraph-5609_21326 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5609_22132 .Pixso-paragraph-5609_21326 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5609_22137 .Pixso-paragraph-5609_21326 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5609_22112 .Pixso-instance-5609_21330 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5609_22117 .Pixso-instance-5609_21330 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5609_22122 .Pixso-instance-5609_21330 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5609_22127 .Pixso-instance-5609_21330 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5609_22132 .Pixso-instance-5609_21330 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5609_22137 .Pixso-instance-5609_21330 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5976_54064 .Pixso-symbol-5976_52093 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 8px 12px 8px 12px;
    min-height: 40px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5976_54064 .stroke-wrapper-5976_52093 {
    width: 320px;
    height: 40px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5976_54064 .stroke-5976_52093 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5976_54069 .Pixso-symbol-5976_52093 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 8px 12px 8px 12px;
    min-height: 40px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5976_54069 .stroke-wrapper-5976_52093 {
    width: 320px;
    height: 40px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5976_54069 .stroke-5976_52093 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5976_54074 .Pixso-symbol-5976_52093 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 8px 12px 8px 12px;
    min-height: 40px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5976_54074 .stroke-wrapper-5976_52093 {
    width: 320px;
    height: 40px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5976_54074 .stroke-5976_52093 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5976_54079 .Pixso-symbol-5976_52093 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 8px 12px 8px 12px;
    min-height: 40px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5976_54079 .stroke-wrapper-5976_52093 {
    width: 320px;
    height: 40px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5976_54079 .stroke-5976_52093 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5976_54084 .Pixso-symbol-5976_52093 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 8px 12px 8px 12px;
    min-height: 40px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5976_54084 .stroke-wrapper-5976_52093 {
    width: 320px;
    height: 40px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5976_54084 .stroke-5976_52093 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5976_54089 .Pixso-symbol-5976_52093 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 8px 12px 8px 12px;
    min-height: 40px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5976_54089 .stroke-wrapper-5976_52093 {
    width: 320px;
    height: 40px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5976_54089 .stroke-5976_52093 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5976_54064 .Pixso-frame-5976_52094 {
    width: 100%;
    height: 22px;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5976_54069 .Pixso-frame-5976_52094 {
    width: 100%;
    height: 22px;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5976_54074 .Pixso-frame-5976_52094 {
    width: 100%;
    height: 22px;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5976_54079 .Pixso-frame-5976_52094 {
    width: 100%;
    height: 22px;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5976_54084 .Pixso-frame-5976_52094 {
    width: 100%;
    height: 22px;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5976_54089 .Pixso-frame-5976_52094 {
    width: 100%;
    height: 22px;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5976_54064 .Pixso-instance-5976_52095 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5976_54069 .Pixso-instance-5976_52095 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5976_54074 .Pixso-instance-5976_52095 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5976_54079 .Pixso-instance-5976_52095 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5976_54084 .Pixso-instance-5976_52095 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5976_54089 .Pixso-instance-5976_52095 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5976_54064 .Pixso-paragraph-5976_52096 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5976_54069 .Pixso-paragraph-5976_52096 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5976_54074 .Pixso-paragraph-5976_52096 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5976_54079 .Pixso-paragraph-5976_52096 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5976_54084 .Pixso-paragraph-5976_52096 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5976_54089 .Pixso-paragraph-5976_52096 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5976_54064 .Pixso-instance-5976_52097 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5976_54069 .Pixso-instance-5976_52097 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5976_54074 .Pixso-instance-5976_52097 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5976_54079 .Pixso-instance-5976_52097 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5976_54084 .Pixso-instance-5976_52097 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5976_54089 .Pixso-instance-5976_52097 {
    width: 20px;
    height: 20px;
}
</style>
