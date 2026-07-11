<template>
    <div class="component-5558_51607">
        <div id="5558_51607" class="Pixso-symbol-5558_51607">
            <div
                id="5629_43319"
                class="Pixso-symbol-5629_43319"
                v-if="
                    State === 'Default' &&
                    Style === 'Default' &&
                    Size === 'sm' &&
                    Width === 'Hug'
                "
            >
                <slot name="slot_5629_43320" v-if="visible_5629_708">
                    <User
                        id="5629_43320"
                        class="Pixso-instance-5629_43320"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <slot name="slot_5629_43321">
                    <p
                        id="5629_43321"
                        class="Pixso-paragraph-5629_43321 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                    >
                        {{ text_5629_714 ?? "Tab Text" }}
                    </p>
                </slot>
                <slot name="slot_5629_43322" v-if="visible_5560_235">
                    <BadgeText
                        id="5629_43322"
                        class="Pixso-instance-5629_43322"
                        :visible_5586_119="false"
                        :visible_5586_121="false"
                        :visible_5586_123="false"
                        text_5588_129="12"
                        Size="sm"
                        Color="Brand"
                        Hierarchy="Secondary"
                        State="Default"
                    >
                        <template #slot_5588_11362>
                            <p
                                id="5588_11362"
                                class="Pixso-paragraph-5588_11362 fill-brand60-1257_33467-paragraph text-text-xssemibold-439_9521"
                            >
                                {{ "12" }}
                            </p>
                        </template>
                    </BadgeText>
                </slot>
            </div>
            <div
                id="5629_43810"
                class="Pixso-symbol-5629_43810"
                v-if="
                    State === 'Default' &&
                    Style === 'Outlined' &&
                    Size === 'sm' &&
                    Width === 'Hug'
                "
            >
                <slot name="slot_5629_43811" v-if="visible_5629_708">
                    <User
                        id="5629_43811"
                        class="Pixso-instance-5629_43811"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <slot name="slot_5629_43812">
                    <p
                        id="5629_43812"
                        class="Pixso-paragraph-5629_43812 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                    >
                        {{ text_5629_714 ?? "Tab Text" }}
                    </p>
                </slot>
                <slot name="slot_5629_43813" v-if="visible_5560_235">
                    <BadgeText
                        id="5629_43813"
                        class="Pixso-instance-5629_43813"
                        :visible_5586_119="false"
                        :visible_5586_121="false"
                        :visible_5586_123="false"
                        text_5588_129="12"
                        Size="sm"
                        Color="Brand"
                        Hierarchy="Secondary"
                        State="Default"
                    >
                        <template #slot_5588_11362>
                            <p
                                id="5588_11362"
                                class="Pixso-paragraph-5588_11362 fill-brand60-1257_33467-paragraph text-text-xssemibold-439_9521"
                            >
                                {{ "12" }}
                            </p>
                        </template>
                    </BadgeText>
                </slot>
            </div>
            <div
                id="5629_43902"
                class="stroke-wrapper-5629_43902"
                v-if="
                    State === 'Default' &&
                    Style === 'Bottom Border' &&
                    Size === 'sm' &&
                    Width === 'Hug'
                "
            >
                <div class="Pixso-symbol-5629_43902">
                    <slot name="slot_5629_43903" v-if="visible_5629_708">
                        <User
                            id="5629_43903"
                            class="Pixso-instance-5629_43903"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                    <slot name="slot_5629_43904">
                        <p
                            id="5629_43904"
                            class="Pixso-paragraph-5629_43904 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                        >
                            {{ text_5629_714 ?? "Tab Text" }}
                        </p>
                    </slot>
                    <slot name="slot_5629_43905" v-if="visible_5560_235">
                        <BadgeText
                            id="5629_43905"
                            class="Pixso-instance-5629_43905"
                            :visible_5586_119="false"
                            :visible_5586_121="false"
                            :visible_5586_123="false"
                            text_5588_129="12"
                            Size="sm"
                            Color="Brand"
                            Hierarchy="Secondary"
                            State="Default"
                        >
                            <template #slot_5588_11362>
                                <p
                                    id="5588_11362"
                                    class="Pixso-paragraph-5588_11362 fill-brand60-1257_33467-paragraph text-text-xssemibold-439_9521"
                                >
                                    {{ "12" }}
                                </p>
                            </template>
                        </BadgeText>
                    </slot>
                </div>
                <div class="stroke-5629_43902 stroke-gray30-35_1481"></div>
            </div>
            <div
                id="5629_44270"
                class="stroke-wrapper-5629_44270"
                v-if="
                    State === 'Default' &&
                    Style === 'Left Border' &&
                    Size === 'sm' &&
                    Width === 'Hug'
                "
            >
                <div class="Pixso-symbol-5629_44270">
                    <slot name="slot_5629_44271" v-if="visible_5629_708">
                        <User
                            id="5629_44271"
                            class="Pixso-instance-5629_44271"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                    <slot name="slot_5629_44272">
                        <p
                            id="5629_44272"
                            class="Pixso-paragraph-5629_44272 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                        >
                            {{ text_5629_714 ?? "Tab Text" }}
                        </p>
                    </slot>
                    <slot name="slot_5629_44273" v-if="visible_5560_235">
                        <BadgeText
                            id="5629_44273"
                            class="Pixso-instance-5629_44273"
                            :visible_5586_119="false"
                            :visible_5586_121="false"
                            :visible_5586_123="false"
                            text_5588_129="12"
                            Size="sm"
                            Color="Brand"
                            Hierarchy="Secondary"
                            State="Default"
                        >
                            <template #slot_5588_11362>
                                <p
                                    id="5588_11362"
                                    class="Pixso-paragraph-5588_11362 fill-brand60-1257_33467-paragraph text-text-xssemibold-439_9521"
                                >
                                    {{ "12" }}
                                </p>
                            </template>
                        </BadgeText>
                    </slot>
                </div>
                <div class="stroke-5629_44270 stroke-gray30-35_1481"></div>
            </div>
            <div
                id="5629_44074"
                class="Pixso-symbol-5629_44074"
                v-if="
                    State === 'Default' &&
                    Style === 'Default' &&
                    Size === 'sm' &&
                    Width === 'Fixed'
                "
            >
                <slot name="slot_5629_44075" v-if="visible_5629_708">
                    <User
                        id="5629_44075"
                        class="Pixso-instance-5629_44075"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <slot name="slot_5629_44076">
                    <p
                        id="5629_44076"
                        class="Pixso-paragraph-5629_44076 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                    >
                        {{ text_5629_714 ?? "Tab Text" }}
                    </p>
                </slot>
                <slot name="slot_5629_44077" v-if="visible_5560_235">
                    <BadgeText
                        id="5629_44077"
                        class="Pixso-instance-5629_44077"
                        :visible_5586_119="false"
                        :visible_5586_121="false"
                        :visible_5586_123="false"
                        text_5588_129="12"
                        Size="sm"
                        Color="Brand"
                        Hierarchy="Secondary"
                        State="Default"
                    >
                        <template #slot_5588_11362>
                            <p
                                id="5588_11362"
                                class="Pixso-paragraph-5588_11362 fill-brand60-1257_33467-paragraph text-text-xssemibold-439_9521"
                            >
                                {{ "12" }}
                            </p>
                        </template>
                    </BadgeText>
                </slot>
            </div>
            <div
                id="5629_44078"
                class="Pixso-symbol-5629_44078"
                v-if="
                    State === 'Default' &&
                    Style === 'Outlined' &&
                    Size === 'sm' &&
                    Width === 'Fixed'
                "
            >
                <slot name="slot_5629_44079" v-if="visible_5629_708">
                    <User
                        id="5629_44079"
                        class="Pixso-instance-5629_44079"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <slot name="slot_5629_44080">
                    <p
                        id="5629_44080"
                        class="Pixso-paragraph-5629_44080 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                    >
                        {{ text_5629_714 ?? "Tab Text" }}
                    </p>
                </slot>
                <slot name="slot_5629_44081" v-if="visible_5560_235">
                    <BadgeText
                        id="5629_44081"
                        class="Pixso-instance-5629_44081"
                        :visible_5586_119="false"
                        :visible_5586_121="false"
                        :visible_5586_123="false"
                        text_5588_129="12"
                        Size="sm"
                        Color="Brand"
                        Hierarchy="Secondary"
                        State="Default"
                    >
                        <template #slot_5588_11362>
                            <p
                                id="5588_11362"
                                class="Pixso-paragraph-5588_11362 fill-brand60-1257_33467-paragraph text-text-xssemibold-439_9521"
                            >
                                {{ "12" }}
                            </p>
                        </template>
                    </BadgeText>
                </slot>
            </div>
            <div
                id="5629_44082"
                class="stroke-wrapper-5629_44082"
                v-if="
                    State === 'Default' &&
                    Style === 'Bottom Border' &&
                    Size === 'sm' &&
                    Width === 'Fixed'
                "
            >
                <div class="Pixso-symbol-5629_44082">
                    <slot name="slot_5629_44083" v-if="visible_5629_708">
                        <User
                            id="5629_44083"
                            class="Pixso-instance-5629_44083"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                    <slot name="slot_5629_44084">
                        <p
                            id="5629_44084"
                            class="Pixso-paragraph-5629_44084 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                        >
                            {{ text_5629_714 ?? "Tab Text" }}
                        </p>
                    </slot>
                    <slot name="slot_5629_44085" v-if="visible_5560_235">
                        <BadgeText
                            id="5629_44085"
                            class="Pixso-instance-5629_44085"
                            :visible_5586_119="false"
                            :visible_5586_121="false"
                            :visible_5586_123="false"
                            text_5588_129="12"
                            Size="sm"
                            Color="Brand"
                            Hierarchy="Secondary"
                            State="Default"
                        >
                            <template #slot_5588_11362>
                                <p
                                    id="5588_11362"
                                    class="Pixso-paragraph-5588_11362 fill-brand60-1257_33467-paragraph text-text-xssemibold-439_9521"
                                >
                                    {{ "12" }}
                                </p>
                            </template>
                        </BadgeText>
                    </slot>
                </div>
                <div class="stroke-5629_44082 stroke-gray30-35_1481"></div>
            </div>
            <div
                id="5629_44626"
                class="stroke-wrapper-5629_44626"
                v-if="
                    State === 'Default' &&
                    Style === 'Left Border' &&
                    Size === 'sm' &&
                    Width === 'Fixed'
                "
            >
                <div class="Pixso-symbol-5629_44626">
                    <slot name="slot_5629_44627" v-if="visible_5629_708">
                        <User
                            id="5629_44627"
                            class="Pixso-instance-5629_44627"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                    <slot name="slot_5629_44628">
                        <p
                            id="5629_44628"
                            class="Pixso-paragraph-5629_44628 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                        >
                            {{ text_5629_714 ?? "Tab Text" }}
                        </p>
                    </slot>
                    <slot name="slot_5629_44629" v-if="visible_5560_235">
                        <BadgeText
                            id="5629_44629"
                            class="Pixso-instance-5629_44629"
                            :visible_5586_119="false"
                            :visible_5586_121="false"
                            :visible_5586_123="false"
                            text_5588_129="12"
                            Size="sm"
                            Color="Brand"
                            Hierarchy="Secondary"
                            State="Default"
                        >
                            <template #slot_5588_11362>
                                <p
                                    id="5588_11362"
                                    class="Pixso-paragraph-5588_11362 fill-brand60-1257_33467-paragraph text-text-xssemibold-439_9521"
                                >
                                    {{ "12" }}
                                </p>
                            </template>
                        </BadgeText>
                    </slot>
                </div>
                <div class="stroke-5629_44626 stroke-gray30-35_1481"></div>
            </div>
            <div
                id="5629_43687"
                class="Pixso-symbol-5629_43687 fill-gray5-32_4120"
                v-if="
                    State === 'Hover' &&
                    Style === 'Default' &&
                    Size === 'sm' &&
                    Width === 'Hug'
                "
            >
                <slot name="slot_5629_43688" v-if="visible_5629_708">
                    <User
                        id="5629_43688"
                        class="Pixso-instance-5629_43688"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <slot name="slot_5629_43689">
                    <p
                        id="5629_43689"
                        class="Pixso-paragraph-5629_43689 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                    >
                        {{ text_5629_714 ?? "Tab Text" }}
                    </p>
                </slot>
                <slot name="slot_5629_43690" v-if="visible_5560_235">
                    <BadgeText
                        id="5629_43690"
                        class="Pixso-instance-5629_43690"
                        :visible_5586_119="false"
                        :visible_5586_121="false"
                        :visible_5586_123="false"
                        text_5588_129="12"
                        Size="sm"
                        Color="Brand"
                        Hierarchy="Secondary"
                        State="Hover"
                    >
                        <template #slot_5588_13118>
                            <p
                                id="5588_13118"
                                class="Pixso-paragraph-5588_13118 fill-brand60-1257_33467-paragraph text-text-xssemibold-439_9521"
                            >
                                {{ "12" }}
                            </p>
                        </template>
                    </BadgeText>
                </slot>
            </div>
            <div
                id="5629_43910"
                class="stroke-wrapper-5629_43910"
                v-if="
                    State === 'Hover' &&
                    Style === 'Bottom Border' &&
                    Size === 'sm' &&
                    Width === 'Hug'
                "
            >
                <div class="Pixso-symbol-5629_43910 fill-gray5-32_4120">
                    <slot name="slot_5629_43911" v-if="visible_5629_708">
                        <User
                            id="5629_43911"
                            class="Pixso-instance-5629_43911"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                    <slot name="slot_5629_43912">
                        <p
                            id="5629_43912"
                            class="Pixso-paragraph-5629_43912 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                        >
                            {{ text_5629_714 ?? "Tab Text" }}
                        </p>
                    </slot>
                    <slot name="slot_5629_43913" v-if="visible_5560_235">
                        <BadgeText
                            id="5629_43913"
                            class="Pixso-instance-5629_43913"
                            :visible_5586_119="false"
                            :visible_5586_121="false"
                            :visible_5586_123="false"
                            text_5588_129="12"
                            Size="sm"
                            Color="Brand"
                            Hierarchy="Secondary"
                            State="Hover"
                        >
                            <template #slot_5588_13118>
                                <p
                                    id="5588_13118"
                                    class="Pixso-paragraph-5588_13118 fill-brand60-1257_33467-paragraph text-text-xssemibold-439_9521"
                                >
                                    {{ "12" }}
                                </p>
                            </template>
                        </BadgeText>
                    </slot>
                </div>
                <div class="stroke-5629_43910 stroke-gray30-35_1481"></div>
            </div>
            <div
                id="5629_43818"
                class="Pixso-symbol-5629_43818 fill-gray5-32_4120"
                v-if="
                    State === 'Hover' &&
                    Style === 'Outlined' &&
                    Size === 'sm' &&
                    Width === 'Hug'
                "
            >
                <slot name="slot_5629_43819" v-if="visible_5629_708">
                    <User
                        id="5629_43819"
                        class="Pixso-instance-5629_43819"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <slot name="slot_5629_43820">
                    <p
                        id="5629_43820"
                        class="Pixso-paragraph-5629_43820 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                    >
                        {{ text_5629_714 ?? "Tab Text" }}
                    </p>
                </slot>
                <slot name="slot_5629_43821" v-if="visible_5560_235">
                    <BadgeText
                        id="5629_43821"
                        class="Pixso-instance-5629_43821"
                        :visible_5586_119="false"
                        :visible_5586_121="false"
                        :visible_5586_123="false"
                        text_5588_129="12"
                        Size="sm"
                        Color="Brand"
                        Hierarchy="Secondary"
                        State="Hover"
                    >
                        <template #slot_5588_13118>
                            <p
                                id="5588_13118"
                                class="Pixso-paragraph-5588_13118 fill-brand60-1257_33467-paragraph text-text-xssemibold-439_9521"
                            >
                                {{ "12" }}
                            </p>
                        </template>
                    </BadgeText>
                </slot>
            </div>
            <div
                id="5629_44274"
                class="stroke-wrapper-5629_44274"
                v-if="
                    State === 'Hover' &&
                    Style === 'Left Border' &&
                    Size === 'sm' &&
                    Width === 'Hug'
                "
            >
                <div class="Pixso-symbol-5629_44274 fill-gray5-32_4120">
                    <slot name="slot_5629_44275" v-if="visible_5629_708">
                        <User
                            id="5629_44275"
                            class="Pixso-instance-5629_44275"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                    <slot name="slot_5629_44276">
                        <p
                            id="5629_44276"
                            class="Pixso-paragraph-5629_44276 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                        >
                            {{ text_5629_714 ?? "Tab Text" }}
                        </p>
                    </slot>
                    <slot name="slot_5629_44277" v-if="visible_5560_235">
                        <BadgeText
                            id="5629_44277"
                            class="Pixso-instance-5629_44277"
                            :visible_5586_119="false"
                            :visible_5586_121="false"
                            :visible_5586_123="false"
                            text_5588_129="12"
                            Size="sm"
                            Color="Brand"
                            Hierarchy="Secondary"
                            State="Hover"
                        >
                            <template #slot_5588_13118>
                                <p
                                    id="5588_13118"
                                    class="Pixso-paragraph-5588_13118 fill-brand60-1257_33467-paragraph text-text-xssemibold-439_9521"
                                >
                                    {{ "12" }}
                                </p>
                            </template>
                        </BadgeText>
                    </slot>
                </div>
                <div class="stroke-5629_44274 stroke-gray30-35_1481"></div>
            </div>
            <div
                id="5629_44098"
                class="Pixso-symbol-5629_44098 fill-gray5-32_4120"
                v-if="
                    State === 'Hover' &&
                    Style === 'Default' &&
                    Size === 'sm' &&
                    Width === 'Fixed'
                "
            >
                <slot name="slot_5629_44099" v-if="visible_5629_708">
                    <User
                        id="5629_44099"
                        class="Pixso-instance-5629_44099"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <slot name="slot_5629_44100">
                    <p
                        id="5629_44100"
                        class="Pixso-paragraph-5629_44100 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                    >
                        {{ text_5629_714 ?? "Tab Text" }}
                    </p>
                </slot>
                <slot name="slot_5629_44101" v-if="visible_5560_235">
                    <BadgeText
                        id="5629_44101"
                        class="Pixso-instance-5629_44101"
                        :visible_5586_119="false"
                        :visible_5586_121="false"
                        :visible_5586_123="false"
                        text_5588_129="12"
                        Size="sm"
                        Color="Brand"
                        Hierarchy="Secondary"
                        State="Hover"
                    >
                        <template #slot_5588_13118>
                            <p
                                id="5588_13118"
                                class="Pixso-paragraph-5588_13118 fill-brand60-1257_33467-paragraph text-text-xssemibold-439_9521"
                            >
                                {{ "12" }}
                            </p>
                        </template>
                    </BadgeText>
                </slot>
            </div>
            <div
                id="5629_44106"
                class="stroke-wrapper-5629_44106"
                v-if="
                    State === 'Hover' &&
                    Style === 'Bottom Border' &&
                    Size === 'sm' &&
                    Width === 'Fixed'
                "
            >
                <div class="Pixso-symbol-5629_44106 fill-gray5-32_4120">
                    <slot name="slot_5629_44107" v-if="visible_5629_708">
                        <User
                            id="5629_44107"
                            class="Pixso-instance-5629_44107"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                    <slot name="slot_5629_44108">
                        <p
                            id="5629_44108"
                            class="Pixso-paragraph-5629_44108 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                        >
                            {{ text_5629_714 ?? "Tab Text" }}
                        </p>
                    </slot>
                    <slot name="slot_5629_44109" v-if="visible_5560_235">
                        <BadgeText
                            id="5629_44109"
                            class="Pixso-instance-5629_44109"
                            :visible_5586_119="false"
                            :visible_5586_121="false"
                            :visible_5586_123="false"
                            text_5588_129="12"
                            Size="sm"
                            Color="Brand"
                            Hierarchy="Secondary"
                            State="Hover"
                        >
                            <template #slot_5588_13118>
                                <p
                                    id="5588_13118"
                                    class="Pixso-paragraph-5588_13118 fill-brand60-1257_33467-paragraph text-text-xssemibold-439_9521"
                                >
                                    {{ "12" }}
                                </p>
                            </template>
                        </BadgeText>
                    </slot>
                </div>
                <div class="stroke-5629_44106 stroke-gray30-35_1481"></div>
            </div>
            <div
                id="5629_44102"
                class="Pixso-symbol-5629_44102 fill-gray5-32_4120"
                v-if="
                    State === 'Hover' &&
                    Style === 'Outlined' &&
                    Size === 'sm' &&
                    Width === 'Fixed'
                "
            >
                <slot name="slot_5629_44103" v-if="visible_5629_708">
                    <User
                        id="5629_44103"
                        class="Pixso-instance-5629_44103"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <slot name="slot_5629_44104">
                    <p
                        id="5629_44104"
                        class="Pixso-paragraph-5629_44104 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                    >
                        {{ text_5629_714 ?? "Tab Text" }}
                    </p>
                </slot>
                <slot name="slot_5629_44105" v-if="visible_5560_235">
                    <BadgeText
                        id="5629_44105"
                        class="Pixso-instance-5629_44105"
                        :visible_5586_119="false"
                        :visible_5586_121="false"
                        :visible_5586_123="false"
                        text_5588_129="12"
                        Size="sm"
                        Color="Brand"
                        Hierarchy="Secondary"
                        State="Hover"
                    >
                        <template #slot_5588_13118>
                            <p
                                id="5588_13118"
                                class="Pixso-paragraph-5588_13118 fill-brand60-1257_33467-paragraph text-text-xssemibold-439_9521"
                            >
                                {{ "12" }}
                            </p>
                        </template>
                    </BadgeText>
                </slot>
            </div>
            <div
                id="5629_44630"
                class="stroke-wrapper-5629_44630"
                v-if="
                    State === 'Hover' &&
                    Style === 'Left Border' &&
                    Size === 'sm' &&
                    Width === 'Fixed'
                "
            >
                <div class="Pixso-symbol-5629_44630 fill-gray5-32_4120">
                    <slot name="slot_5629_44631" v-if="visible_5629_708">
                        <User
                            id="5629_44631"
                            class="Pixso-instance-5629_44631"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                    <slot name="slot_5629_44632">
                        <p
                            id="5629_44632"
                            class="Pixso-paragraph-5629_44632 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                        >
                            {{ text_5629_714 ?? "Tab Text" }}
                        </p>
                    </slot>
                    <slot name="slot_5629_44633" v-if="visible_5560_235">
                        <BadgeText
                            id="5629_44633"
                            class="Pixso-instance-5629_44633"
                            :visible_5586_119="false"
                            :visible_5586_121="false"
                            :visible_5586_123="false"
                            text_5588_129="12"
                            Size="sm"
                            Color="Brand"
                            Hierarchy="Secondary"
                            State="Hover"
                        >
                            <template #slot_5588_13118>
                                <p
                                    id="5588_13118"
                                    class="Pixso-paragraph-5588_13118 fill-brand60-1257_33467-paragraph text-text-xssemibold-439_9521"
                                >
                                    {{ "12" }}
                                </p>
                            </template>
                        </BadgeText>
                    </slot>
                </div>
                <div class="stroke-5629_44630 stroke-gray30-35_1481"></div>
            </div>
            <div
                id="5629_43914"
                class="stroke-wrapper-5629_43914"
                v-if="
                    State === 'Active' &&
                    Style === 'Bottom Border' &&
                    Size === 'sm' &&
                    Width === 'Hug'
                "
            >
                <div class="Pixso-symbol-5629_43914">
                    <slot name="slot_5629_43915" v-if="visible_5629_708">
                        <User
                            id="5629_43915"
                            class="Pixso-instance-5629_43915"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                    <slot name="slot_5629_43916">
                        <p
                            id="5629_43916"
                            class="Pixso-paragraph-5629_43916 fill-gray80-32_4123-paragraph text-text-smbold-423_3208"
                        >
                            {{ text_5629_714 ?? "Tab Text" }}
                        </p>
                    </slot>
                    <slot name="slot_5629_43917" v-if="visible_5560_235">
                        <BadgeText
                            id="5629_43917"
                            class="Pixso-instance-5629_43917"
                            :visible_5586_119="false"
                            :visible_5586_121="false"
                            :visible_5586_123="false"
                            text_5588_129="12"
                            Size="sm"
                            Color="Brand"
                            Hierarchy="Secondary"
                            State="Default"
                        >
                            <template #slot_5588_11362>
                                <p
                                    id="5588_11362"
                                    class="Pixso-paragraph-5588_11362 fill-brand60-1257_33467-paragraph text-text-xssemibold-439_9521"
                                >
                                    {{ "12" }}
                                </p>
                            </template>
                        </BadgeText>
                    </slot>
                </div>
                <div class="stroke-5629_43914 stroke-brand60-1257_33467"></div>
            </div>
            <div
                id="5629_43710"
                class="Pixso-symbol-5629_43710 fill-gray0-white-67_3285 effect-shadowmd-5457_24364"
                v-if="
                    State === 'Active' &&
                    Style === 'Default' &&
                    Size === 'sm' &&
                    Width === 'Hug'
                "
            >
                <slot name="slot_5629_43711" v-if="visible_5629_708">
                    <User
                        id="5629_43711"
                        class="Pixso-instance-5629_43711"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <slot name="slot_5629_43712">
                    <p
                        id="5629_43712"
                        class="Pixso-paragraph-5629_43712 fill-gray80-32_4123-paragraph text-text-smbold-423_3208"
                    >
                        {{ text_5629_714 ?? "Tab Text" }}
                    </p>
                </slot>
                <slot name="slot_5629_43713" v-if="visible_5560_235">
                    <BadgeText
                        id="5629_43713"
                        class="Pixso-instance-5629_43713"
                        :visible_5586_119="false"
                        :visible_5586_121="false"
                        :visible_5586_123="false"
                        text_5588_129="12"
                        Size="sm"
                        Color="Brand"
                        Hierarchy="Secondary"
                        State="Default"
                    >
                        <template #slot_5588_11362>
                            <p
                                id="5588_11362"
                                class="Pixso-paragraph-5588_11362 fill-brand60-1257_33467-paragraph text-text-xssemibold-439_9521"
                            >
                                {{ "12" }}
                            </p>
                        </template>
                    </BadgeText>
                </slot>
            </div>
            <div
                id="5629_43822"
                class="stroke-wrapper-5629_43822"
                v-if="
                    State === 'Active' &&
                    Style === 'Outlined' &&
                    Size === 'sm' &&
                    Width === 'Hug'
                "
            >
                <div class="Pixso-symbol-5629_43822">
                    <slot name="slot_5629_43823" v-if="visible_5629_708">
                        <User
                            id="5629_43823"
                            class="Pixso-instance-5629_43823"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                    <slot name="slot_5629_43824">
                        <p
                            id="5629_43824"
                            class="Pixso-paragraph-5629_43824 fill-gray80-32_4123-paragraph text-text-smbold-423_3208"
                        >
                            {{ text_5629_714 ?? "Tab Text" }}
                        </p>
                    </slot>
                    <slot name="slot_5629_43825" v-if="visible_5560_235">
                        <BadgeText
                            id="5629_43825"
                            class="Pixso-instance-5629_43825"
                            :visible_5586_119="false"
                            :visible_5586_121="false"
                            :visible_5586_123="false"
                            text_5588_129="12"
                            Size="sm"
                            Color="Brand"
                            Hierarchy="Secondary"
                            State="Default"
                        >
                            <template #slot_5588_11362>
                                <p
                                    id="5588_11362"
                                    class="Pixso-paragraph-5588_11362 fill-brand60-1257_33467-paragraph text-text-xssemibold-439_9521"
                                >
                                    {{ "12" }}
                                </p>
                            </template>
                        </BadgeText>
                    </slot>
                </div>
                <div class="stroke-5629_43822 stroke-brand60-1257_33467"></div>
            </div>
            <div
                id="5629_44278"
                class="stroke-wrapper-5629_44278"
                v-if="
                    State === 'Active' &&
                    Style === 'Left Border' &&
                    Size === 'sm' &&
                    Width === 'Hug'
                "
            >
                <div class="Pixso-symbol-5629_44278 fill-gray0-white-67_3285">
                    <slot name="slot_5629_44279" v-if="visible_5629_708">
                        <User
                            id="5629_44279"
                            class="Pixso-instance-5629_44279"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                    <slot name="slot_5629_44280">
                        <p
                            id="5629_44280"
                            class="Pixso-paragraph-5629_44280 fill-gray80-32_4123-paragraph text-text-smbold-423_3208"
                        >
                            {{ text_5629_714 ?? "Tab Text" }}
                        </p>
                    </slot>
                    <slot name="slot_5629_44281" v-if="visible_5560_235">
                        <BadgeText
                            id="5629_44281"
                            class="Pixso-instance-5629_44281"
                            :visible_5586_119="false"
                            :visible_5586_121="false"
                            :visible_5586_123="false"
                            text_5588_129="12"
                            Size="sm"
                            Color="Brand"
                            Hierarchy="Secondary"
                            State="Default"
                        >
                            <template #slot_5588_11362>
                                <p
                                    id="5588_11362"
                                    class="Pixso-paragraph-5588_11362 fill-brand60-1257_33467-paragraph text-text-xssemibold-439_9521"
                                >
                                    {{ "12" }}
                                </p>
                            </template>
                        </BadgeText>
                    </slot>
                </div>
                <div class="stroke-5629_44278 stroke-brand60-1257_33467"></div>
            </div>
            <div
                id="5629_44110"
                class="Pixso-symbol-5629_44110 fill-gray0-white-67_3285 effect-shadowmd-5457_24364"
                v-if="
                    State === 'Active' &&
                    Style === 'Default' &&
                    Size === 'sm' &&
                    Width === 'Fixed'
                "
            >
                <slot name="slot_5629_44111" v-if="visible_5629_708">
                    <User
                        id="5629_44111"
                        class="Pixso-instance-5629_44111"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <slot name="slot_5629_44112">
                    <p
                        id="5629_44112"
                        class="Pixso-paragraph-5629_44112 fill-gray80-32_4123-paragraph text-text-smbold-423_3208"
                    >
                        {{ text_5629_714 ?? "Tab Text" }}
                    </p>
                </slot>
                <slot name="slot_5629_44113" v-if="visible_5560_235">
                    <BadgeText
                        id="5629_44113"
                        class="Pixso-instance-5629_44113"
                        :visible_5586_119="false"
                        :visible_5586_121="false"
                        :visible_5586_123="false"
                        text_5588_129="12"
                        Size="sm"
                        Color="Brand"
                        Hierarchy="Secondary"
                        State="Default"
                    >
                        <template #slot_5588_11362>
                            <p
                                id="5588_11362"
                                class="Pixso-paragraph-5588_11362 fill-brand60-1257_33467-paragraph text-text-xssemibold-439_9521"
                            >
                                {{ "12" }}
                            </p>
                        </template>
                    </BadgeText>
                </slot>
            </div>
            <div
                id="5629_44118"
                class="stroke-wrapper-5629_44118"
                v-if="
                    State === 'Active' &&
                    Style === 'Bottom Border' &&
                    Size === 'sm' &&
                    Width === 'Fixed'
                "
            >
                <div class="Pixso-symbol-5629_44118">
                    <slot name="slot_5629_44119" v-if="visible_5629_708">
                        <User
                            id="5629_44119"
                            class="Pixso-instance-5629_44119"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                    <slot name="slot_5629_44120">
                        <p
                            id="5629_44120"
                            class="Pixso-paragraph-5629_44120 fill-gray80-32_4123-paragraph text-text-smbold-423_3208"
                        >
                            {{ text_5629_714 ?? "Tab Text" }}
                        </p>
                    </slot>
                    <slot name="slot_5629_44121" v-if="visible_5560_235">
                        <BadgeText
                            id="5629_44121"
                            class="Pixso-instance-5629_44121"
                            :visible_5586_119="false"
                            :visible_5586_121="false"
                            :visible_5586_123="false"
                            text_5588_129="12"
                            Size="sm"
                            Color="Brand"
                            Hierarchy="Secondary"
                            State="Default"
                        >
                            <template #slot_5588_11362>
                                <p
                                    id="5588_11362"
                                    class="Pixso-paragraph-5588_11362 fill-brand60-1257_33467-paragraph text-text-xssemibold-439_9521"
                                >
                                    {{ "12" }}
                                </p>
                            </template>
                        </BadgeText>
                    </slot>
                </div>
                <div class="stroke-5629_44118 stroke-brand60-1257_33467"></div>
            </div>
            <div
                id="5629_44114"
                class="stroke-wrapper-5629_44114"
                v-if="
                    State === 'Active' &&
                    Style === 'Outlined' &&
                    Size === 'sm' &&
                    Width === 'Fixed'
                "
            >
                <div class="Pixso-symbol-5629_44114">
                    <slot name="slot_5629_44115" v-if="visible_5629_708">
                        <User
                            id="5629_44115"
                            class="Pixso-instance-5629_44115"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                    <slot name="slot_5629_44116">
                        <p
                            id="5629_44116"
                            class="Pixso-paragraph-5629_44116 fill-gray80-32_4123-paragraph text-text-smbold-423_3208"
                        >
                            {{ text_5629_714 ?? "Tab Text" }}
                        </p>
                    </slot>
                    <slot name="slot_5629_44117" v-if="visible_5560_235">
                        <BadgeText
                            id="5629_44117"
                            class="Pixso-instance-5629_44117"
                            :visible_5586_119="false"
                            :visible_5586_121="false"
                            :visible_5586_123="false"
                            text_5588_129="12"
                            Size="sm"
                            Color="Brand"
                            Hierarchy="Secondary"
                            State="Default"
                        >
                            <template #slot_5588_11362>
                                <p
                                    id="5588_11362"
                                    class="Pixso-paragraph-5588_11362 fill-brand60-1257_33467-paragraph text-text-xssemibold-439_9521"
                                >
                                    {{ "12" }}
                                </p>
                            </template>
                        </BadgeText>
                    </slot>
                </div>
                <div class="stroke-5629_44114 stroke-brand60-1257_33467"></div>
            </div>
            <div
                id="5629_43906"
                class="stroke-wrapper-5629_43906"
                v-if="
                    State === 'Disabled' &&
                    Style === 'Bottom Border' &&
                    Size === 'sm' &&
                    Width === 'Hug'
                "
            >
                <div class="Pixso-symbol-5629_43906">
                    <slot name="slot_5629_43907" v-if="visible_5629_708">
                        <User
                            id="5629_43907"
                            class="Pixso-instance-5629_43907"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                    <slot name="slot_5629_43908">
                        <p
                            id="5629_43908"
                            class="Pixso-paragraph-5629_43908 fill-gray30-35_1481-paragraph text-text-smbold-423_3208"
                        >
                            {{ text_5629_714 ?? "Tab Text" }}
                        </p>
                    </slot>
                    <slot name="slot_5629_43909" v-if="visible_5560_235">
                        <BadgeText
                            id="5629_43909"
                            class="Pixso-instance-5629_43909"
                            :visible_5586_119="false"
                            :visible_5586_121="false"
                            :visible_5586_123="false"
                            text_5588_129="12"
                            Size="sm"
                            Color="Brand"
                            Hierarchy="Secondary"
                            State="Disabled"
                        >
                            <template #slot_5588_13937>
                                <p
                                    id="5588_13937"
                                    class="Pixso-paragraph-5588_13937 fill-brand30-1257_33463-paragraph text-text-xssemibold-439_9521"
                                >
                                    {{ "12" }}
                                </p>
                            </template>
                        </BadgeText>
                    </slot>
                </div>
                <div class="stroke-5629_43906 stroke-gray30-35_1481"></div>
            </div>
            <div
                id="5629_44634"
                class="stroke-wrapper-5629_44634"
                v-if="
                    State === 'Active' &&
                    Style === 'Left Border' &&
                    Size === 'sm' &&
                    Width === 'Fixed'
                "
            >
                <div class="Pixso-symbol-5629_44634 fill-gray0-white-67_3285">
                    <slot name="slot_5629_44635" v-if="visible_5629_708">
                        <User
                            id="5629_44635"
                            class="Pixso-instance-5629_44635"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                    <slot name="slot_5629_44636">
                        <p
                            id="5629_44636"
                            class="Pixso-paragraph-5629_44636 fill-gray80-32_4123-paragraph text-text-smbold-423_3208"
                        >
                            {{ text_5629_714 ?? "Tab Text" }}
                        </p>
                    </slot>
                    <slot name="slot_5629_44637" v-if="visible_5560_235">
                        <BadgeText
                            id="5629_44637"
                            class="Pixso-instance-5629_44637"
                            :visible_5586_119="false"
                            :visible_5586_121="false"
                            :visible_5586_123="false"
                            text_5588_129="12"
                            Size="sm"
                            Color="Brand"
                            Hierarchy="Secondary"
                            State="Default"
                        >
                            <template #slot_5588_11362>
                                <p
                                    id="5588_11362"
                                    class="Pixso-paragraph-5588_11362 fill-brand60-1257_33467-paragraph text-text-xssemibold-439_9521"
                                >
                                    {{ "12" }}
                                </p>
                            </template>
                        </BadgeText>
                    </slot>
                </div>
                <div class="stroke-5629_44634 stroke-brand60-1257_33467"></div>
            </div>
            <div
                id="5629_43749"
                class="Pixso-symbol-5629_43749"
                v-if="
                    State === 'Disabled' &&
                    Style === 'Default' &&
                    Size === 'sm' &&
                    Width === 'Hug'
                "
            >
                <slot name="slot_5629_43750" v-if="visible_5629_708">
                    <User
                        id="5629_43750"
                        class="Pixso-instance-5629_43750"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <slot name="slot_5629_43751">
                    <p
                        id="5629_43751"
                        class="Pixso-paragraph-5629_43751 fill-gray30-35_1481-paragraph text-text-smbold-423_3208"
                    >
                        {{ text_5629_714 ?? "Tab Text" }}
                    </p>
                </slot>
                <slot name="slot_5629_43752" v-if="visible_5560_235">
                    <BadgeText
                        id="5629_43752"
                        class="Pixso-instance-5629_43752"
                        :visible_5586_119="false"
                        :visible_5586_121="false"
                        :visible_5586_123="false"
                        text_5588_129="12"
                        Size="sm"
                        Color="Brand"
                        Hierarchy="Secondary"
                        State="Disabled"
                    >
                        <template #slot_5588_13937>
                            <p
                                id="5588_13937"
                                class="Pixso-paragraph-5588_13937 fill-brand30-1257_33463-paragraph text-text-xssemibold-439_9521"
                            >
                                {{ "12" }}
                            </p>
                        </template>
                    </BadgeText>
                </slot>
            </div>
            <div
                id="5629_43814"
                class="stroke-wrapper-5629_43814"
                v-if="
                    State === 'Disabled' &&
                    Style === 'Outlined' &&
                    Size === 'sm' &&
                    Width === 'Hug'
                "
            >
                <div class="Pixso-symbol-5629_43814">
                    <slot name="slot_5629_43815" v-if="visible_5629_708">
                        <User
                            id="5629_43815"
                            class="Pixso-instance-5629_43815"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                    <slot name="slot_5629_43816">
                        <p
                            id="5629_43816"
                            class="Pixso-paragraph-5629_43816 fill-gray30-35_1481-paragraph text-text-smbold-423_3208"
                        >
                            {{ text_5629_714 ?? "Tab Text" }}
                        </p>
                    </slot>
                    <slot name="slot_5629_43817" v-if="visible_5560_235">
                        <BadgeText
                            id="5629_43817"
                            class="Pixso-instance-5629_43817"
                            :visible_5586_119="false"
                            :visible_5586_121="false"
                            :visible_5586_123="false"
                            text_5588_129="12"
                            Size="sm"
                            Color="Brand"
                            Hierarchy="Secondary"
                            State="Disabled"
                        >
                            <template #slot_5588_13937>
                                <p
                                    id="5588_13937"
                                    class="Pixso-paragraph-5588_13937 fill-brand30-1257_33463-paragraph text-text-xssemibold-439_9521"
                                >
                                    {{ "12" }}
                                </p>
                            </template>
                        </BadgeText>
                    </slot>
                </div>
                <div class="stroke-5629_43814 stroke-gray30-35_1481"></div>
            </div>
            <div
                id="5629_44094"
                class="stroke-wrapper-5629_44094"
                v-if="
                    State === 'Disabled' &&
                    Style === 'Bottom Border' &&
                    Size === 'sm' &&
                    Width === 'Fixed'
                "
            >
                <div class="Pixso-symbol-5629_44094">
                    <slot name="slot_5629_44095" v-if="visible_5629_708">
                        <User
                            id="5629_44095"
                            class="Pixso-instance-5629_44095"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                    <slot name="slot_5629_44096">
                        <p
                            id="5629_44096"
                            class="Pixso-paragraph-5629_44096 fill-gray30-35_1481-paragraph text-text-smbold-423_3208"
                        >
                            {{ text_5629_714 ?? "Tab Text" }}
                        </p>
                    </slot>
                    <slot name="slot_5629_44097" v-if="visible_5560_235">
                        <BadgeText
                            id="5629_44097"
                            class="Pixso-instance-5629_44097"
                            :visible_5586_119="false"
                            :visible_5586_121="false"
                            :visible_5586_123="false"
                            text_5588_129="12"
                            Size="sm"
                            Color="Brand"
                            Hierarchy="Secondary"
                            State="Disabled"
                        >
                            <template #slot_5588_13937>
                                <p
                                    id="5588_13937"
                                    class="Pixso-paragraph-5588_13937 fill-brand30-1257_33463-paragraph text-text-xssemibold-439_9521"
                                >
                                    {{ "12" }}
                                </p>
                            </template>
                        </BadgeText>
                    </slot>
                </div>
                <div class="stroke-5629_44094 stroke-gray30-35_1481"></div>
            </div>
            <div
                id="5629_44282"
                class="stroke-wrapper-5629_44282"
                v-if="
                    State === 'Disabled' &&
                    Style === 'Left Border' &&
                    Size === 'sm' &&
                    Width === 'Hug'
                "
            >
                <div class="Pixso-symbol-5629_44282">
                    <slot name="slot_5629_44283" v-if="visible_5629_708">
                        <User
                            id="5629_44283"
                            class="Pixso-instance-5629_44283"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                    <slot name="slot_5629_44284">
                        <p
                            id="5629_44284"
                            class="Pixso-paragraph-5629_44284 fill-gray30-35_1481-paragraph text-text-smbold-423_3208"
                        >
                            {{ text_5629_714 ?? "Tab Text" }}
                        </p>
                    </slot>
                    <slot name="slot_5629_44285" v-if="visible_5560_235">
                        <BadgeText
                            id="5629_44285"
                            class="Pixso-instance-5629_44285"
                            :visible_5586_119="false"
                            :visible_5586_121="false"
                            :visible_5586_123="false"
                            text_5588_129="12"
                            Size="sm"
                            Color="Brand"
                            Hierarchy="Secondary"
                            State="Disabled"
                        >
                            <template #slot_5588_13937>
                                <p
                                    id="5588_13937"
                                    class="Pixso-paragraph-5588_13937 fill-brand30-1257_33463-paragraph text-text-xssemibold-439_9521"
                                >
                                    {{ "12" }}
                                </p>
                            </template>
                        </BadgeText>
                    </slot>
                </div>
                <div class="stroke-5629_44282 stroke-gray30-35_1481"></div>
            </div>
            <div
                id="5629_44086"
                class="Pixso-symbol-5629_44086"
                v-if="
                    State === 'Disabled' &&
                    Style === 'Default' &&
                    Size === 'sm' &&
                    Width === 'Fixed'
                "
            >
                <slot name="slot_5629_44087" v-if="visible_5629_708">
                    <User
                        id="5629_44087"
                        class="Pixso-instance-5629_44087"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <slot name="slot_5629_44088">
                    <p
                        id="5629_44088"
                        class="Pixso-paragraph-5629_44088 fill-gray30-35_1481-paragraph text-text-smbold-423_3208"
                    >
                        {{ text_5629_714 ?? "Tab Text" }}
                    </p>
                </slot>
                <slot name="slot_5629_44089" v-if="visible_5560_235">
                    <BadgeText
                        id="5629_44089"
                        class="Pixso-instance-5629_44089"
                        :visible_5586_119="false"
                        :visible_5586_121="false"
                        :visible_5586_123="false"
                        text_5588_129="12"
                        Size="sm"
                        Color="Brand"
                        Hierarchy="Secondary"
                        State="Disabled"
                    >
                        <template #slot_5588_13937>
                            <p
                                id="5588_13937"
                                class="Pixso-paragraph-5588_13937 fill-brand30-1257_33463-paragraph text-text-xssemibold-439_9521"
                            >
                                {{ "12" }}
                            </p>
                        </template>
                    </BadgeText>
                </slot>
            </div>
            <div
                id="5629_44090"
                class="stroke-wrapper-5629_44090"
                v-if="
                    State === 'Disabled' &&
                    Style === 'Outlined' &&
                    Size === 'sm' &&
                    Width === 'Fixed'
                "
            >
                <div class="Pixso-symbol-5629_44090">
                    <slot name="slot_5629_44091" v-if="visible_5629_708">
                        <User
                            id="5629_44091"
                            class="Pixso-instance-5629_44091"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                    <slot name="slot_5629_44092">
                        <p
                            id="5629_44092"
                            class="Pixso-paragraph-5629_44092 fill-gray30-35_1481-paragraph text-text-smbold-423_3208"
                        >
                            {{ text_5629_714 ?? "Tab Text" }}
                        </p>
                    </slot>
                    <slot name="slot_5629_44093" v-if="visible_5560_235">
                        <BadgeText
                            id="5629_44093"
                            class="Pixso-instance-5629_44093"
                            :visible_5586_119="false"
                            :visible_5586_121="false"
                            :visible_5586_123="false"
                            text_5588_129="12"
                            Size="sm"
                            Color="Brand"
                            Hierarchy="Secondary"
                            State="Disabled"
                        >
                            <template #slot_5588_13937>
                                <p
                                    id="5588_13937"
                                    class="Pixso-paragraph-5588_13937 fill-brand30-1257_33463-paragraph text-text-xssemibold-439_9521"
                                >
                                    {{ "12" }}
                                </p>
                            </template>
                        </BadgeText>
                    </slot>
                </div>
                <div class="stroke-5629_44090 stroke-gray30-35_1481"></div>
            </div>
            <div
                id="5629_44638"
                class="stroke-wrapper-5629_44638"
                v-if="
                    State === 'Disabled' &&
                    Style === 'Left Border' &&
                    Size === 'sm' &&
                    Width === 'Fixed'
                "
            >
                <div class="Pixso-symbol-5629_44638">
                    <slot name="slot_5629_44639" v-if="visible_5629_708">
                        <User
                            id="5629_44639"
                            class="Pixso-instance-5629_44639"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                    <slot name="slot_5629_44640">
                        <p
                            id="5629_44640"
                            class="Pixso-paragraph-5629_44640 fill-gray30-35_1481-paragraph text-text-smbold-423_3208"
                        >
                            {{ text_5629_714 ?? "Tab Text" }}
                        </p>
                    </slot>
                    <slot name="slot_5629_44641" v-if="visible_5560_235">
                        <BadgeText
                            id="5629_44641"
                            class="Pixso-instance-5629_44641"
                            :visible_5586_119="false"
                            :visible_5586_121="false"
                            :visible_5586_123="false"
                            text_5588_129="12"
                            Size="sm"
                            Color="Brand"
                            Hierarchy="Secondary"
                            State="Disabled"
                        >
                            <template #slot_5588_13937>
                                <p
                                    id="5588_13937"
                                    class="Pixso-paragraph-5588_13937 fill-brand30-1257_33463-paragraph text-text-xssemibold-439_9521"
                                >
                                    {{ "12" }}
                                </p>
                            </template>
                        </BadgeText>
                    </slot>
                </div>
                <div class="stroke-5629_44638 stroke-gray30-35_1481"></div>
            </div>
            <div
                id="5558_51587"
                class="Pixso-symbol-5558_51587"
                v-if="
                    State === 'Default' &&
                    Style === 'Default' &&
                    Size === 'md' &&
                    Width === 'Hug'
                "
            >
                <slot name="slot_5629_41189" v-if="visible_5629_708">
                    <User
                        id="5629_41189"
                        class="Pixso-instance-5629_41189"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <slot name="slot_5558_51586">
                    <p
                        id="5558_51586"
                        class="Pixso-paragraph-5558_51586 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                    >
                        {{ text_5629_714 ?? "Tab Text" }}
                    </p>
                </slot>
                <slot name="slot_5629_41092" v-if="visible_5560_235">
                    <BadgeText
                        id="5629_41092"
                        class="Pixso-instance-5629_41092"
                        :visible_5586_119="false"
                        :visible_5586_121="false"
                        :visible_5586_123="false"
                        text_5588_129="12"
                        Size="sm"
                        Color="Brand"
                        Hierarchy="Secondary"
                        State="Default"
                    >
                        <template #slot_5588_11362>
                            <p
                                id="5588_11362"
                                class="Pixso-paragraph-5588_11362 fill-brand60-1257_33467-paragraph text-text-xssemibold-439_9521"
                            >
                                {{ "12" }}
                            </p>
                        </template>
                    </BadgeText>
                </slot>
            </div>
            <div
                id="5629_41545"
                class="Pixso-symbol-5629_41545 fill-gray0-white-67_3285"
                v-if="
                    State === 'Default' &&
                    Style === 'Outlined' &&
                    Size === 'md' &&
                    Width === 'Hug'
                "
            >
                <slot name="slot_5629_41546" v-if="visible_5629_708">
                    <User
                        id="5629_41546"
                        class="Pixso-instance-5629_41546"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <slot name="slot_5629_41547">
                    <p
                        id="5629_41547"
                        class="Pixso-paragraph-5629_41547 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                    >
                        {{ text_5629_714 ?? "Tab Text" }}
                    </p>
                </slot>
                <slot name="slot_5629_41548" v-if="visible_5560_235">
                    <BadgeText
                        id="5629_41548"
                        class="Pixso-instance-5629_41548"
                        :visible_5586_119="false"
                        :visible_5586_121="false"
                        :visible_5586_123="false"
                        text_5588_129="12"
                        Size="sm"
                        Color="Brand"
                        Hierarchy="Secondary"
                        State="Default"
                    >
                        <template #slot_5588_11362>
                            <p
                                id="5588_11362"
                                class="Pixso-paragraph-5588_11362 fill-brand60-1257_33467-paragraph text-text-xssemibold-439_9521"
                            >
                                {{ "12" }}
                            </p>
                        </template>
                    </BadgeText>
                </slot>
            </div>
            <div
                id="5629_41725"
                class="stroke-wrapper-5629_41725"
                v-if="
                    State === 'Default' &&
                    Style === 'Bottom Border' &&
                    Size === 'md' &&
                    Width === 'Fixed'
                "
            >
                <div class="Pixso-symbol-5629_41725">
                    <slot name="slot_5629_41726" v-if="visible_5629_708">
                        <User
                            id="5629_41726"
                            class="Pixso-instance-5629_41726"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                    <slot name="slot_5629_41727">
                        <p
                            id="5629_41727"
                            class="Pixso-paragraph-5629_41727 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                        >
                            {{ text_5629_714 ?? "Tab Text" }}
                        </p>
                    </slot>
                    <slot name="slot_5629_41728" v-if="visible_5560_235">
                        <BadgeText
                            id="5629_41728"
                            class="Pixso-instance-5629_41728"
                            :visible_5586_119="false"
                            :visible_5586_121="false"
                            :visible_5586_123="false"
                            text_5588_129="12"
                            Size="sm"
                            Color="Brand"
                            Hierarchy="Secondary"
                            State="Default"
                        >
                            <template #slot_5588_11362>
                                <p
                                    id="5588_11362"
                                    class="Pixso-paragraph-5588_11362 fill-brand60-1257_33467-paragraph text-text-xssemibold-439_9521"
                                >
                                    {{ "12" }}
                                </p>
                            </template>
                        </BadgeText>
                    </slot>
                </div>
                <div class="stroke-5629_41725 stroke-gray30-35_1481"></div>
            </div>
            <div
                id="5629_41453"
                class="stroke-wrapper-5629_41453"
                v-if="
                    State === 'Default' &&
                    Style === 'Bottom Border' &&
                    Size === 'md' &&
                    Width === 'Hug'
                "
            >
                <div class="Pixso-symbol-5629_41453">
                    <slot name="slot_5629_41454" v-if="visible_5629_708">
                        <User
                            id="5629_41454"
                            class="Pixso-instance-5629_41454"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                    <slot name="slot_5629_41455">
                        <p
                            id="5629_41455"
                            class="Pixso-paragraph-5629_41455 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                        >
                            {{ text_5629_714 ?? "Tab Text" }}
                        </p>
                    </slot>
                    <slot name="slot_5629_41456" v-if="visible_5560_235">
                        <BadgeText
                            id="5629_41456"
                            class="Pixso-instance-5629_41456"
                            :visible_5586_119="false"
                            :visible_5586_121="false"
                            :visible_5586_123="false"
                            text_5588_129="12"
                            Size="sm"
                            Color="Brand"
                            Hierarchy="Secondary"
                            State="Default"
                        >
                            <template #slot_5588_11362>
                                <p
                                    id="5588_11362"
                                    class="Pixso-paragraph-5588_11362 fill-brand60-1257_33467-paragraph text-text-xssemibold-439_9521"
                                >
                                    {{ "12" }}
                                </p>
                            </template>
                        </BadgeText>
                    </slot>
                </div>
                <div class="stroke-5629_41453 stroke-gray30-35_1481"></div>
            </div>
            <div
                id="5629_44352"
                class="stroke-wrapper-5629_44352"
                v-if="
                    State === 'Default' &&
                    Style === 'Left Border' &&
                    Size === 'md' &&
                    Width === 'Hug'
                "
            >
                <div class="Pixso-symbol-5629_44352 fill-gray0-white-67_3285">
                    <slot name="slot_5629_44353" v-if="visible_5629_708">
                        <User
                            id="5629_44353"
                            class="Pixso-instance-5629_44353"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                    <slot name="slot_5629_44354">
                        <p
                            id="5629_44354"
                            class="Pixso-paragraph-5629_44354 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                        >
                            {{ text_5629_714 ?? "Tab Text" }}
                        </p>
                    </slot>
                    <slot name="slot_5629_44355" v-if="visible_5560_235">
                        <BadgeText
                            id="5629_44355"
                            class="Pixso-instance-5629_44355"
                            :visible_5586_119="false"
                            :visible_5586_121="false"
                            :visible_5586_123="false"
                            text_5588_129="12"
                            Size="sm"
                            Color="Brand"
                            Hierarchy="Secondary"
                            State="Default"
                        >
                            <template #slot_5588_11362>
                                <p
                                    id="5588_11362"
                                    class="Pixso-paragraph-5588_11362 fill-brand60-1257_33467-paragraph text-text-xssemibold-439_9521"
                                >
                                    {{ "12" }}
                                </p>
                            </template>
                        </BadgeText>
                    </slot>
                </div>
                <div class="stroke-5629_44352 stroke-gray30-35_1481"></div>
            </div>
            <div
                id="5629_41717"
                class="Pixso-symbol-5629_41717"
                v-if="
                    State === 'Default' &&
                    Style === 'Default' &&
                    Size === 'md' &&
                    Width === 'Fixed'
                "
            >
                <slot name="slot_5629_41718" v-if="visible_5629_708">
                    <User
                        id="5629_41718"
                        class="Pixso-instance-5629_41718"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <slot name="slot_5629_41719">
                    <p
                        id="5629_41719"
                        class="Pixso-paragraph-5629_41719 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                    >
                        {{ text_5629_714 ?? "Tab Text" }}
                    </p>
                </slot>
                <slot name="slot_5629_41720" v-if="visible_5560_235">
                    <BadgeText
                        id="5629_41720"
                        class="Pixso-instance-5629_41720"
                        :visible_5586_119="false"
                        :visible_5586_121="false"
                        :visible_5586_123="false"
                        text_5588_129="12"
                        Size="sm"
                        Color="Brand"
                        Hierarchy="Secondary"
                        State="Default"
                    >
                        <template #slot_5588_11362>
                            <p
                                id="5588_11362"
                                class="Pixso-paragraph-5588_11362 fill-brand60-1257_33467-paragraph text-text-xssemibold-439_9521"
                            >
                                {{ "12" }}
                            </p>
                        </template>
                    </BadgeText>
                </slot>
            </div>
            <div
                id="5629_41721"
                class="Pixso-symbol-5629_41721 fill-gray0-white-67_3285"
                v-if="
                    State === 'Default' &&
                    Style === 'Outlined' &&
                    Size === 'md' &&
                    Width === 'Fixed'
                "
            >
                <slot name="slot_5629_41722" v-if="visible_5629_708">
                    <User
                        id="5629_41722"
                        class="Pixso-instance-5629_41722"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <slot name="slot_5629_41723">
                    <p
                        id="5629_41723"
                        class="Pixso-paragraph-5629_41723 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                    >
                        {{ text_5629_714 ?? "Tab Text" }}
                    </p>
                </slot>
                <slot name="slot_5629_41724" v-if="visible_5560_235">
                    <BadgeText
                        id="5629_41724"
                        class="Pixso-instance-5629_41724"
                        :visible_5586_119="false"
                        :visible_5586_121="false"
                        :visible_5586_123="false"
                        text_5588_129="12"
                        Size="sm"
                        Color="Brand"
                        Hierarchy="Secondary"
                        State="Default"
                    >
                        <template #slot_5588_11362>
                            <p
                                id="5588_11362"
                                class="Pixso-paragraph-5588_11362 fill-brand60-1257_33467-paragraph text-text-xssemibold-439_9521"
                            >
                                {{ "12" }}
                            </p>
                        </template>
                    </BadgeText>
                </slot>
            </div>
            <div
                id="5629_44642"
                class="stroke-wrapper-5629_44642"
                v-if="
                    State === 'Default' &&
                    Style === 'Left Border' &&
                    Size === 'md' &&
                    Width === 'Fixed'
                "
            >
                <div class="Pixso-symbol-5629_44642 fill-gray0-white-67_3285">
                    <slot name="slot_5629_44643" v-if="visible_5629_708">
                        <User
                            id="5629_44643"
                            class="Pixso-instance-5629_44643"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                    <slot name="slot_5629_44644">
                        <p
                            id="5629_44644"
                            class="Pixso-paragraph-5629_44644 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                        >
                            {{ text_5629_714 ?? "Tab Text" }}
                        </p>
                    </slot>
                    <slot name="slot_5629_44645" v-if="visible_5560_235">
                        <BadgeText
                            id="5629_44645"
                            class="Pixso-instance-5629_44645"
                            :visible_5586_119="false"
                            :visible_5586_121="false"
                            :visible_5586_123="false"
                            text_5588_129="12"
                            Size="sm"
                            Color="Brand"
                            Hierarchy="Secondary"
                            State="Default"
                        >
                            <template #slot_5588_11362>
                                <p
                                    id="5588_11362"
                                    class="Pixso-paragraph-5588_11362 fill-brand60-1257_33467-paragraph text-text-xssemibold-439_9521"
                                >
                                    {{ "12" }}
                                </p>
                            </template>
                        </BadgeText>
                    </slot>
                </div>
                <div class="stroke-5629_44642 stroke-gray30-35_1481"></div>
            </div>
            <div
                id="5629_41223"
                class="Pixso-symbol-5629_41223 fill-gray5-32_4120"
                v-if="
                    State === 'Hover' &&
                    Style === 'Default' &&
                    Size === 'md' &&
                    Width === 'Hug'
                "
            >
                <slot name="slot_5629_41224" v-if="visible_5629_708">
                    <User
                        id="5629_41224"
                        class="Pixso-instance-5629_41224"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <slot name="slot_5629_41225">
                    <p
                        id="5629_41225"
                        class="Pixso-paragraph-5629_41225 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                    >
                        {{ text_5629_714 ?? "Tab Text" }}
                    </p>
                </slot>
                <slot name="slot_5629_41226" v-if="visible_5560_235">
                    <BadgeText
                        id="5629_41226"
                        class="Pixso-instance-5629_41226"
                        :visible_5586_119="false"
                        :visible_5586_121="false"
                        :visible_5586_123="false"
                        text_5588_129="12"
                        Size="sm"
                        Color="Brand"
                        Hierarchy="Secondary"
                        State="Hover"
                    >
                        <template #slot_5588_13118>
                            <p
                                id="5588_13118"
                                class="Pixso-paragraph-5588_13118 fill-brand60-1257_33467-paragraph text-text-xssemibold-439_9521"
                            >
                                {{ "12" }}
                            </p>
                        </template>
                    </BadgeText>
                </slot>
            </div>
            <div
                id="5629_41737"
                class="stroke-wrapper-5629_41737"
                v-if="
                    State === 'Hover' &&
                    Style === 'Bottom Border' &&
                    Size === 'md' &&
                    Width === 'Fixed'
                "
            >
                <div class="Pixso-symbol-5629_41737 fill-gray5-32_4120">
                    <slot name="slot_5629_41738" v-if="visible_5629_708">
                        <User
                            id="5629_41738"
                            class="Pixso-instance-5629_41738"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                    <slot name="slot_5629_41739">
                        <p
                            id="5629_41739"
                            class="Pixso-paragraph-5629_41739 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                        >
                            {{ text_5629_714 ?? "Tab Text" }}
                        </p>
                    </slot>
                    <slot name="slot_5629_41740" v-if="visible_5560_235">
                        <BadgeText
                            id="5629_41740"
                            class="Pixso-instance-5629_41740"
                            :visible_5586_119="false"
                            :visible_5586_121="false"
                            :visible_5586_123="false"
                            text_5588_129="12"
                            Size="sm"
                            Color="Brand"
                            Hierarchy="Secondary"
                            State="Hover"
                        >
                            <template #slot_5588_13118>
                                <p
                                    id="5588_13118"
                                    class="Pixso-paragraph-5588_13118 fill-brand60-1257_33467-paragraph text-text-xssemibold-439_9521"
                                >
                                    {{ "12" }}
                                </p>
                            </template>
                        </BadgeText>
                    </slot>
                </div>
                <div class="stroke-5629_41737 stroke-gray30-35_1481"></div>
            </div>
            <div
                id="5629_41549"
                class="stroke-wrapper-5629_41549"
                v-if="
                    State === 'Hover' &&
                    Style === 'Outlined' &&
                    Size === 'md' &&
                    Width === 'Hug'
                "
            >
                <div class="Pixso-symbol-5629_41549">
                    <slot name="slot_5629_41550" v-if="visible_5629_708">
                        <User
                            id="5629_41550"
                            class="Pixso-instance-5629_41550"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                    <slot name="slot_5629_41551">
                        <p
                            id="5629_41551"
                            class="Pixso-paragraph-5629_41551 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                        >
                            {{ text_5629_714 ?? "Tab Text" }}
                        </p>
                    </slot>
                    <slot name="slot_5629_41552" v-if="visible_5560_235">
                        <BadgeText
                            id="5629_41552"
                            class="Pixso-instance-5629_41552"
                            :visible_5586_119="false"
                            :visible_5586_121="false"
                            :visible_5586_123="false"
                            text_5588_129="12"
                            Size="sm"
                            Color="Brand"
                            Hierarchy="Secondary"
                            State="Hover"
                        >
                            <template #slot_5588_13118>
                                <p
                                    id="5588_13118"
                                    class="Pixso-paragraph-5588_13118 fill-brand60-1257_33467-paragraph text-text-xssemibold-439_9521"
                                >
                                    {{ "12" }}
                                </p>
                            </template>
                        </BadgeText>
                    </slot>
                </div>
                <div class="stroke-5629_41549 stroke-gray30-35_1481"></div>
            </div>
            <div
                id="5629_41457"
                class="stroke-wrapper-5629_41457"
                v-if="
                    State === 'Hover' &&
                    Style === 'Bottom Border' &&
                    Size === 'md' &&
                    Width === 'Hug'
                "
            >
                <div class="Pixso-symbol-5629_41457 fill-gray5-32_4120">
                    <slot name="slot_5629_41458" v-if="visible_5629_708">
                        <User
                            id="5629_41458"
                            class="Pixso-instance-5629_41458"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                    <slot name="slot_5629_41459">
                        <p
                            id="5629_41459"
                            class="Pixso-paragraph-5629_41459 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                        >
                            {{ text_5629_714 ?? "Tab Text" }}
                        </p>
                    </slot>
                    <slot name="slot_5629_41460" v-if="visible_5560_235">
                        <BadgeText
                            id="5629_41460"
                            class="Pixso-instance-5629_41460"
                            :visible_5586_119="false"
                            :visible_5586_121="false"
                            :visible_5586_123="false"
                            text_5588_129="12"
                            Size="sm"
                            Color="Brand"
                            Hierarchy="Secondary"
                            State="Hover"
                        >
                            <template #slot_5588_13118>
                                <p
                                    id="5588_13118"
                                    class="Pixso-paragraph-5588_13118 fill-brand60-1257_33467-paragraph text-text-xssemibold-439_9521"
                                >
                                    {{ "12" }}
                                </p>
                            </template>
                        </BadgeText>
                    </slot>
                </div>
                <div class="stroke-5629_41457 stroke-gray30-35_1481"></div>
            </div>
            <div
                id="5629_44356"
                class="stroke-wrapper-5629_44356"
                v-if="
                    State === 'Hover' &&
                    Style === 'Left Border' &&
                    Size === 'md' &&
                    Width === 'Hug'
                "
            >
                <div class="Pixso-symbol-5629_44356 fill-gray5-32_4120">
                    <slot name="slot_5629_44357" v-if="visible_5629_708">
                        <User
                            id="5629_44357"
                            class="Pixso-instance-5629_44357"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                    <slot name="slot_5629_44358">
                        <p
                            id="5629_44358"
                            class="Pixso-paragraph-5629_44358 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                        >
                            {{ text_5629_714 ?? "Tab Text" }}
                        </p>
                    </slot>
                    <slot name="slot_5629_44359" v-if="visible_5560_235">
                        <BadgeText
                            id="5629_44359"
                            class="Pixso-instance-5629_44359"
                            :visible_5586_119="false"
                            :visible_5586_121="false"
                            :visible_5586_123="false"
                            text_5588_129="12"
                            Size="sm"
                            Color="Brand"
                            Hierarchy="Secondary"
                            State="Hover"
                        >
                            <template #slot_5588_13118>
                                <p
                                    id="5588_13118"
                                    class="Pixso-paragraph-5588_13118 fill-brand60-1257_33467-paragraph text-text-xssemibold-439_9521"
                                >
                                    {{ "12" }}
                                </p>
                            </template>
                        </BadgeText>
                    </slot>
                </div>
                <div class="stroke-5629_44356 stroke-gray30-35_1481"></div>
            </div>
            <div
                id="5629_41729"
                class="Pixso-symbol-5629_41729 fill-gray5-32_4120"
                v-if="
                    State === 'Hover' &&
                    Style === 'Default' &&
                    Size === 'md' &&
                    Width === 'Fixed'
                "
            >
                <slot name="slot_5629_41730" v-if="visible_5629_708">
                    <User
                        id="5629_41730"
                        class="Pixso-instance-5629_41730"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <slot name="slot_5629_41731">
                    <p
                        id="5629_41731"
                        class="Pixso-paragraph-5629_41731 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                    >
                        {{ text_5629_714 ?? "Tab Text" }}
                    </p>
                </slot>
                <slot name="slot_5629_41732" v-if="visible_5560_235">
                    <BadgeText
                        id="5629_41732"
                        class="Pixso-instance-5629_41732"
                        :visible_5586_119="false"
                        :visible_5586_121="false"
                        :visible_5586_123="false"
                        text_5588_129="12"
                        Size="sm"
                        Color="Brand"
                        Hierarchy="Secondary"
                        State="Hover"
                    >
                        <template #slot_5588_13118>
                            <p
                                id="5588_13118"
                                class="Pixso-paragraph-5588_13118 fill-brand60-1257_33467-paragraph text-text-xssemibold-439_9521"
                            >
                                {{ "12" }}
                            </p>
                        </template>
                    </BadgeText>
                </slot>
            </div>
            <div
                id="5629_41733"
                class="stroke-wrapper-5629_41733"
                v-if="
                    State === 'Hover' &&
                    Style === 'Outlined' &&
                    Size === 'md' &&
                    Width === 'Fixed'
                "
            >
                <div class="Pixso-symbol-5629_41733">
                    <slot name="slot_5629_41734" v-if="visible_5629_708">
                        <User
                            id="5629_41734"
                            class="Pixso-instance-5629_41734"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                    <slot name="slot_5629_41735">
                        <p
                            id="5629_41735"
                            class="Pixso-paragraph-5629_41735 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                        >
                            {{ text_5629_714 ?? "Tab Text" }}
                        </p>
                    </slot>
                    <slot name="slot_5629_41736" v-if="visible_5560_235">
                        <BadgeText
                            id="5629_41736"
                            class="Pixso-instance-5629_41736"
                            :visible_5586_119="false"
                            :visible_5586_121="false"
                            :visible_5586_123="false"
                            text_5588_129="12"
                            Size="sm"
                            Color="Brand"
                            Hierarchy="Secondary"
                            State="Hover"
                        >
                            <template #slot_5588_13118>
                                <p
                                    id="5588_13118"
                                    class="Pixso-paragraph-5588_13118 fill-brand60-1257_33467-paragraph text-text-xssemibold-439_9521"
                                >
                                    {{ "12" }}
                                </p>
                            </template>
                        </BadgeText>
                    </slot>
                </div>
                <div class="stroke-5629_41733 stroke-gray30-35_1481"></div>
            </div>
            <div
                id="5629_44646"
                class="stroke-wrapper-5629_44646"
                v-if="
                    State === 'Hover' &&
                    Style === 'Left Border' &&
                    Size === 'md' &&
                    Width === 'Fixed'
                "
            >
                <div class="Pixso-symbol-5629_44646 fill-gray5-32_4120">
                    <slot name="slot_5629_44647" v-if="visible_5629_708">
                        <User
                            id="5629_44647"
                            class="Pixso-instance-5629_44647"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                    <slot name="slot_5629_44648">
                        <p
                            id="5629_44648"
                            class="Pixso-paragraph-5629_44648 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                        >
                            {{ text_5629_714 ?? "Tab Text" }}
                        </p>
                    </slot>
                    <slot name="slot_5629_44649" v-if="visible_5560_235">
                        <BadgeText
                            id="5629_44649"
                            class="Pixso-instance-5629_44649"
                            :visible_5586_119="false"
                            :visible_5586_121="false"
                            :visible_5586_123="false"
                            text_5588_129="12"
                            Size="sm"
                            Color="Brand"
                            Hierarchy="Secondary"
                            State="Hover"
                        >
                            <template #slot_5588_13118>
                                <p
                                    id="5588_13118"
                                    class="Pixso-paragraph-5588_13118 fill-brand60-1257_33467-paragraph text-text-xssemibold-439_9521"
                                >
                                    {{ "12" }}
                                </p>
                            </template>
                        </BadgeText>
                    </slot>
                </div>
                <div class="stroke-5629_44646 stroke-gray30-35_1481"></div>
            </div>
            <div
                id="5629_41749"
                class="stroke-wrapper-5629_41749"
                v-if="
                    State === 'Active' &&
                    Style === 'Bottom Border' &&
                    Size === 'md' &&
                    Width === 'Fixed'
                "
            >
                <div class="Pixso-symbol-5629_41749">
                    <slot name="slot_5629_41750" v-if="visible_5629_708">
                        <User
                            id="5629_41750"
                            class="Pixso-instance-5629_41750"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                    <slot name="slot_5629_41751">
                        <p
                            id="5629_41751"
                            class="Pixso-paragraph-5629_41751 fill-gray80-32_4123-paragraph text-text-smbold-423_3208"
                        >
                            {{ text_5629_714 ?? "Tab Text" }}
                        </p>
                    </slot>
                    <slot name="slot_5629_41752" v-if="visible_5560_235">
                        <BadgeText
                            id="5629_41752"
                            class="Pixso-instance-5629_41752"
                            :visible_5586_119="false"
                            :visible_5586_121="false"
                            :visible_5586_123="false"
                            text_5588_129="12"
                            Size="sm"
                            Color="Brand"
                            Hierarchy="Secondary"
                            State="Default"
                        >
                            <template #slot_5588_11362>
                                <p
                                    id="5588_11362"
                                    class="Pixso-paragraph-5588_11362 fill-brand60-1257_33467-paragraph text-text-xssemibold-439_9521"
                                >
                                    {{ "12" }}
                                </p>
                            </template>
                        </BadgeText>
                    </slot>
                </div>
                <div class="stroke-5629_41749 stroke-brand60-1257_33467"></div>
            </div>
            <div
                id="5629_41260"
                class="Pixso-symbol-5629_41260 fill-gray0-white-67_3285 effect-shadowmd-5457_24364"
                v-if="
                    State === 'Active' &&
                    Style === 'Default' &&
                    Size === 'md' &&
                    Width === 'Hug'
                "
            >
                <slot name="slot_5629_41261" v-if="visible_5629_708">
                    <User
                        id="5629_41261"
                        class="Pixso-instance-5629_41261"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <slot name="slot_5629_41262">
                    <p
                        id="5629_41262"
                        class="Pixso-paragraph-5629_41262 fill-gray80-32_4123-paragraph text-text-smbold-423_3208"
                    >
                        {{ text_5629_714 ?? "Tab Text" }}
                    </p>
                </slot>
                <slot name="slot_5629_41263" v-if="visible_5560_235">
                    <BadgeText
                        id="5629_41263"
                        class="Pixso-instance-5629_41263"
                        :visible_5586_119="false"
                        :visible_5586_121="false"
                        :visible_5586_123="false"
                        text_5588_129="12"
                        Size="sm"
                        Color="Brand"
                        Hierarchy="Secondary"
                        State="Default"
                    >
                        <template #slot_5588_11362>
                            <p
                                id="5588_11362"
                                class="Pixso-paragraph-5588_11362 fill-brand60-1257_33467-paragraph text-text-xssemibold-439_9521"
                            >
                                {{ "12" }}
                            </p>
                        </template>
                    </BadgeText>
                </slot>
            </div>
            <div
                id="5629_41553"
                class="stroke-wrapper-5629_41553"
                v-if="
                    State === 'Active' &&
                    Style === 'Outlined' &&
                    Size === 'md' &&
                    Width === 'Hug'
                "
            >
                <div class="Pixso-symbol-5629_41553">
                    <slot name="slot_5629_41554" v-if="visible_5629_708">
                        <User
                            id="5629_41554"
                            class="Pixso-instance-5629_41554"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                    <slot name="slot_5629_41555">
                        <p
                            id="5629_41555"
                            class="Pixso-paragraph-5629_41555 fill-gray80-32_4123-paragraph text-text-smbold-423_3208"
                        >
                            {{ text_5629_714 ?? "Tab Text" }}
                        </p>
                    </slot>
                    <slot name="slot_5629_41556" v-if="visible_5560_235">
                        <BadgeText
                            id="5629_41556"
                            class="Pixso-instance-5629_41556"
                            :visible_5586_119="false"
                            :visible_5586_121="false"
                            :visible_5586_123="false"
                            text_5588_129="12"
                            Size="sm"
                            Color="Brand"
                            Hierarchy="Secondary"
                            State="Default"
                        >
                            <template #slot_5588_11362>
                                <p
                                    id="5588_11362"
                                    class="Pixso-paragraph-5588_11362 fill-brand60-1257_33467-paragraph text-text-xssemibold-439_9521"
                                >
                                    {{ "12" }}
                                </p>
                            </template>
                        </BadgeText>
                    </slot>
                </div>
                <div class="stroke-5629_41553 stroke-brand60-1257_33467"></div>
            </div>
            <div
                id="5629_41461"
                class="stroke-wrapper-5629_41461"
                v-if="
                    State === 'Active' &&
                    Style === 'Bottom Border' &&
                    Size === 'md' &&
                    Width === 'Hug'
                "
            >
                <div class="Pixso-symbol-5629_41461">
                    <slot name="slot_5629_41462" v-if="visible_5629_708">
                        <User
                            id="5629_41462"
                            class="Pixso-instance-5629_41462"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                    <slot name="slot_5629_41463">
                        <p
                            id="5629_41463"
                            class="Pixso-paragraph-5629_41463 fill-gray80-32_4123-paragraph text-text-smbold-423_3208"
                        >
                            {{ text_5629_714 ?? "Tab Text" }}
                        </p>
                    </slot>
                    <slot name="slot_5629_41464" v-if="visible_5560_235">
                        <BadgeText
                            id="5629_41464"
                            class="Pixso-instance-5629_41464"
                            :visible_5586_119="false"
                            :visible_5586_121="false"
                            :visible_5586_123="false"
                            text_5588_129="12"
                            Size="sm"
                            Color="Brand"
                            Hierarchy="Secondary"
                            State="Default"
                        >
                            <template #slot_5588_11362>
                                <p
                                    id="5588_11362"
                                    class="Pixso-paragraph-5588_11362 fill-brand60-1257_33467-paragraph text-text-xssemibold-439_9521"
                                >
                                    {{ "12" }}
                                </p>
                            </template>
                        </BadgeText>
                    </slot>
                </div>
                <div class="stroke-5629_41461 stroke-brand60-1257_33467"></div>
            </div>
            <div
                id="5629_44360"
                class="stroke-wrapper-5629_44360"
                v-if="
                    State === 'Active' &&
                    Style === 'Left Border' &&
                    Size === 'md' &&
                    Width === 'Hug'
                "
            >
                <div class="Pixso-symbol-5629_44360 fill-gray0-white-67_3285">
                    <slot name="slot_5629_44361" v-if="visible_5629_708">
                        <User
                            id="5629_44361"
                            class="Pixso-instance-5629_44361"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                    <slot name="slot_5629_44362">
                        <p
                            id="5629_44362"
                            class="Pixso-paragraph-5629_44362 fill-gray80-32_4123-paragraph text-text-smbold-423_3208"
                        >
                            {{ text_5629_714 ?? "Tab Text" }}
                        </p>
                    </slot>
                    <slot name="slot_5629_44363" v-if="visible_5560_235">
                        <BadgeText
                            id="5629_44363"
                            class="Pixso-instance-5629_44363"
                            :visible_5586_119="false"
                            :visible_5586_121="false"
                            :visible_5586_123="false"
                            text_5588_129="12"
                            Size="sm"
                            Color="Brand"
                            Hierarchy="Secondary"
                            State="Default"
                        >
                            <template #slot_5588_11362>
                                <p
                                    id="5588_11362"
                                    class="Pixso-paragraph-5588_11362 fill-brand60-1257_33467-paragraph text-text-xssemibold-439_9521"
                                >
                                    {{ "12" }}
                                </p>
                            </template>
                        </BadgeText>
                    </slot>
                </div>
                <div class="stroke-5629_44360 stroke-brand60-1257_33467"></div>
            </div>
            <div
                id="5629_41741"
                class="Pixso-symbol-5629_41741 fill-brand5-1257_33460"
                v-if="
                    State === 'Active' &&
                    Style === 'Default' &&
                    Size === 'md' &&
                    Width === 'Fixed'
                "
            >
                <slot name="slot_5629_41742" v-if="visible_5629_708">
                    <User
                        id="5629_41742"
                        class="Pixso-instance-5629_41742"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <slot name="slot_5629_41743">
                    <p
                        id="5629_41743"
                        class="Pixso-paragraph-5629_41743 fill-gray80-32_4123-paragraph text-text-smbold-423_3208"
                    >
                        {{ text_5629_714 ?? "Tab Text" }}
                    </p>
                </slot>
                <slot name="slot_5629_41744" v-if="visible_5560_235">
                    <BadgeText
                        id="5629_41744"
                        class="Pixso-instance-5629_41744"
                        :visible_5586_119="false"
                        :visible_5586_121="false"
                        :visible_5586_123="false"
                        text_5588_129="12"
                        Size="sm"
                        Color="Brand"
                        Hierarchy="Secondary"
                        State="Default"
                    >
                        <template #slot_5588_11362>
                            <p
                                id="5588_11362"
                                class="Pixso-paragraph-5588_11362 fill-brand60-1257_33467-paragraph text-text-xssemibold-439_9521"
                            >
                                {{ "12" }}
                            </p>
                        </template>
                    </BadgeText>
                </slot>
            </div>
            <div
                id="5629_41745"
                class="stroke-wrapper-5629_41745"
                v-if="
                    State === 'Active' &&
                    Style === 'Outlined' &&
                    Size === 'md' &&
                    Width === 'Fixed'
                "
            >
                <div class="Pixso-symbol-5629_41745">
                    <slot name="slot_5629_41746" v-if="visible_5629_708">
                        <User
                            id="5629_41746"
                            class="Pixso-instance-5629_41746"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                    <slot name="slot_5629_41747">
                        <p
                            id="5629_41747"
                            class="Pixso-paragraph-5629_41747 fill-gray80-32_4123-paragraph text-text-smbold-423_3208"
                        >
                            {{ text_5629_714 ?? "Tab Text" }}
                        </p>
                    </slot>
                    <slot name="slot_5629_41748" v-if="visible_5560_235">
                        <BadgeText
                            id="5629_41748"
                            class="Pixso-instance-5629_41748"
                            :visible_5586_119="false"
                            :visible_5586_121="false"
                            :visible_5586_123="false"
                            text_5588_129="12"
                            Size="sm"
                            Color="Brand"
                            Hierarchy="Secondary"
                            State="Default"
                        >
                            <template #slot_5588_11362>
                                <p
                                    id="5588_11362"
                                    class="Pixso-paragraph-5588_11362 fill-brand60-1257_33467-paragraph text-text-xssemibold-439_9521"
                                >
                                    {{ "12" }}
                                </p>
                            </template>
                        </BadgeText>
                    </slot>
                </div>
                <div class="stroke-5629_41745 stroke-brand60-1257_33467"></div>
            </div>
            <div
                id="5629_41761"
                class="stroke-wrapper-5629_41761"
                v-if="
                    State === 'Disabled' &&
                    Style === 'Bottom Border' &&
                    Size === 'md' &&
                    Width === 'Fixed'
                "
            >
                <div class="Pixso-symbol-5629_41761 fill-gray0-white-67_3285">
                    <slot name="slot_5629_41762" v-if="visible_5629_708">
                        <User
                            id="5629_41762"
                            class="Pixso-instance-5629_41762"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                    <slot name="slot_5629_41763">
                        <p
                            id="5629_41763"
                            class="Pixso-paragraph-5629_41763 fill-gray30-35_1481-paragraph text-text-smbold-423_3208"
                        >
                            {{ text_5629_714 ?? "Tab Text" }}
                        </p>
                    </slot>
                    <slot name="slot_5629_41764" v-if="visible_5560_235">
                        <BadgeText
                            id="5629_41764"
                            class="Pixso-instance-5629_41764"
                            :visible_5586_119="false"
                            :visible_5586_121="false"
                            :visible_5586_123="false"
                            text_5588_129="12"
                            Size="sm"
                            Color="Brand"
                            Hierarchy="Secondary"
                            State="Disabled"
                        >
                            <template #slot_5588_13937>
                                <p
                                    id="5588_13937"
                                    class="Pixso-paragraph-5588_13937 fill-brand30-1257_33463-paragraph text-text-xssemibold-439_9521"
                                >
                                    {{ "12" }}
                                </p>
                            </template>
                        </BadgeText>
                    </slot>
                </div>
                <div class="stroke-5629_41761 stroke-gray30-35_1481"></div>
            </div>
            <div
                id="5629_44650"
                class="stroke-wrapper-5629_44650"
                v-if="
                    State === 'Active' &&
                    Style === 'Left Border' &&
                    Size === 'md' &&
                    Width === 'Fixed'
                "
            >
                <div class="Pixso-symbol-5629_44650 fill-gray0-white-67_3285">
                    <slot name="slot_5629_44651" v-if="visible_5629_708">
                        <User
                            id="5629_44651"
                            class="Pixso-instance-5629_44651"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                    <slot name="slot_5629_44652">
                        <p
                            id="5629_44652"
                            class="Pixso-paragraph-5629_44652 fill-gray80-32_4123-paragraph text-text-smbold-423_3208"
                        >
                            {{ text_5629_714 ?? "Tab Text" }}
                        </p>
                    </slot>
                    <slot name="slot_5629_44653" v-if="visible_5560_235">
                        <BadgeText
                            id="5629_44653"
                            class="Pixso-instance-5629_44653"
                            :visible_5586_119="false"
                            :visible_5586_121="false"
                            :visible_5586_123="false"
                            text_5588_129="12"
                            Size="sm"
                            Color="Brand"
                            Hierarchy="Secondary"
                            State="Default"
                        >
                            <template #slot_5588_11362>
                                <p
                                    id="5588_11362"
                                    class="Pixso-paragraph-5588_11362 fill-brand60-1257_33467-paragraph text-text-xssemibold-439_9521"
                                >
                                    {{ "12" }}
                                </p>
                            </template>
                        </BadgeText>
                    </slot>
                </div>
                <div class="stroke-5629_44650 stroke-brand60-1257_33467"></div>
            </div>
            <div
                id="5629_41299"
                class="Pixso-symbol-5629_41299"
                v-if="
                    State === 'Disabled' &&
                    Style === 'Default' &&
                    Size === 'md' &&
                    Width === 'Hug'
                "
            >
                <slot name="slot_5629_41300" v-if="visible_5629_708">
                    <User
                        id="5629_41300"
                        class="Pixso-instance-5629_41300"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <slot name="slot_5629_41301">
                    <p
                        id="5629_41301"
                        class="Pixso-paragraph-5629_41301 fill-gray30-35_1481-paragraph text-text-smbold-423_3208"
                    >
                        {{ text_5629_714 ?? "Tab Text" }}
                    </p>
                </slot>
                <slot name="slot_5629_41302" v-if="visible_5560_235">
                    <BadgeText
                        id="5629_41302"
                        class="Pixso-instance-5629_41302"
                        :visible_5586_119="false"
                        :visible_5586_121="false"
                        :visible_5586_123="false"
                        text_5588_129="12"
                        Size="sm"
                        Color="Brand"
                        Hierarchy="Secondary"
                        State="Disabled"
                    >
                        <template #slot_5588_13937>
                            <p
                                id="5588_13937"
                                class="Pixso-paragraph-5588_13937 fill-brand30-1257_33463-paragraph text-text-xssemibold-439_9521"
                            >
                                {{ "12" }}
                            </p>
                        </template>
                    </BadgeText>
                </slot>
            </div>
            <div
                id="5629_41557"
                class="stroke-wrapper-5629_41557"
                v-if="
                    State === 'Disabled' &&
                    Style === 'Outlined' &&
                    Size === 'md' &&
                    Width === 'Hug'
                "
            >
                <div class="Pixso-symbol-5629_41557">
                    <slot name="slot_5629_41558" v-if="visible_5629_708">
                        <User
                            id="5629_41558"
                            class="Pixso-instance-5629_41558"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                    <slot name="slot_5629_41559">
                        <p
                            id="5629_41559"
                            class="Pixso-paragraph-5629_41559 fill-gray30-35_1481-paragraph text-text-smbold-423_3208"
                        >
                            {{ text_5629_714 ?? "Tab Text" }}
                        </p>
                    </slot>
                    <slot name="slot_5629_41560" v-if="visible_5560_235">
                        <BadgeText
                            id="5629_41560"
                            class="Pixso-instance-5629_41560"
                            :visible_5586_119="false"
                            :visible_5586_121="false"
                            :visible_5586_123="false"
                            text_5588_129="12"
                            Size="sm"
                            Color="Brand"
                            Hierarchy="Secondary"
                            State="Disabled"
                        >
                            <template #slot_5588_13937>
                                <p
                                    id="5588_13937"
                                    class="Pixso-paragraph-5588_13937 fill-brand30-1257_33463-paragraph text-text-xssemibold-439_9521"
                                >
                                    {{ "12" }}
                                </p>
                            </template>
                        </BadgeText>
                    </slot>
                </div>
                <div class="stroke-5629_41557 stroke-gray30-35_1481"></div>
            </div>
            <div
                id="5629_41465"
                class="stroke-wrapper-5629_41465"
                v-if="
                    State === 'Disabled' &&
                    Style === 'Bottom Border' &&
                    Size === 'md' &&
                    Width === 'Hug'
                "
            >
                <div class="Pixso-symbol-5629_41465 fill-gray0-white-67_3285">
                    <slot name="slot_5629_41466" v-if="visible_5629_708">
                        <User
                            id="5629_41466"
                            class="Pixso-instance-5629_41466"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                    <slot name="slot_5629_41467">
                        <p
                            id="5629_41467"
                            class="Pixso-paragraph-5629_41467 fill-gray30-35_1481-paragraph text-text-smbold-423_3208"
                        >
                            {{ text_5629_714 ?? "Tab Text" }}
                        </p>
                    </slot>
                    <slot name="slot_5629_41468" v-if="visible_5560_235">
                        <BadgeText
                            id="5629_41468"
                            class="Pixso-instance-5629_41468"
                            :visible_5586_119="false"
                            :visible_5586_121="false"
                            :visible_5586_123="false"
                            text_5588_129="12"
                            Size="sm"
                            Color="Brand"
                            Hierarchy="Secondary"
                            State="Disabled"
                        >
                            <template #slot_5588_13937>
                                <p
                                    id="5588_13937"
                                    class="Pixso-paragraph-5588_13937 fill-brand30-1257_33463-paragraph text-text-xssemibold-439_9521"
                                >
                                    {{ "12" }}
                                </p>
                            </template>
                        </BadgeText>
                    </slot>
                </div>
                <div class="stroke-5629_41465 stroke-gray30-35_1481"></div>
            </div>
            <div
                id="5629_44401"
                class="stroke-wrapper-5629_44401"
                v-if="
                    State === 'Disabled' &&
                    Style === 'Left Border' &&
                    Size === 'md' &&
                    Width === 'Hug'
                "
            >
                <div class="Pixso-symbol-5629_44401 fill-gray0-white-67_3285">
                    <slot name="slot_5629_44402" v-if="visible_5629_708">
                        <User
                            id="5629_44402"
                            class="Pixso-instance-5629_44402"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                    <slot name="slot_5629_44403">
                        <p
                            id="5629_44403"
                            class="Pixso-paragraph-5629_44403 fill-gray30-35_1481-paragraph text-text-smbold-423_3208"
                        >
                            {{ text_5629_714 ?? "Tab Text" }}
                        </p>
                    </slot>
                    <slot name="slot_5629_44404" v-if="visible_5560_235">
                        <BadgeText
                            id="5629_44404"
                            class="Pixso-instance-5629_44404"
                            :visible_5586_119="false"
                            :visible_5586_121="false"
                            :visible_5586_123="false"
                            text_5588_129="12"
                            Size="sm"
                            Color="Brand"
                            Hierarchy="Secondary"
                            State="Disabled"
                        >
                            <template #slot_5588_13937>
                                <p
                                    id="5588_13937"
                                    class="Pixso-paragraph-5588_13937 fill-brand30-1257_33463-paragraph text-text-xssemibold-439_9521"
                                >
                                    {{ "12" }}
                                </p>
                            </template>
                        </BadgeText>
                    </slot>
                </div>
                <div class="stroke-5629_44401 stroke-gray30-35_1481"></div>
            </div>
            <div
                id="5629_41753"
                class="Pixso-symbol-5629_41753"
                v-if="
                    State === 'Disabled' &&
                    Style === 'Default' &&
                    Size === 'md' &&
                    Width === 'Fixed'
                "
            >
                <slot name="slot_5629_41754" v-if="visible_5629_708">
                    <User
                        id="5629_41754"
                        class="Pixso-instance-5629_41754"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <slot name="slot_5629_41755">
                    <p
                        id="5629_41755"
                        class="Pixso-paragraph-5629_41755 fill-gray30-35_1481-paragraph text-text-smbold-423_3208"
                    >
                        {{ text_5629_714 ?? "Tab Text" }}
                    </p>
                </slot>
                <slot name="slot_5629_41756" v-if="visible_5560_235">
                    <BadgeText
                        id="5629_41756"
                        class="Pixso-instance-5629_41756"
                        :visible_5586_119="false"
                        :visible_5586_121="false"
                        :visible_5586_123="false"
                        text_5588_129="12"
                        Size="sm"
                        Color="Brand"
                        Hierarchy="Secondary"
                        State="Disabled"
                    >
                        <template #slot_5588_13937>
                            <p
                                id="5588_13937"
                                class="Pixso-paragraph-5588_13937 fill-brand30-1257_33463-paragraph text-text-xssemibold-439_9521"
                            >
                                {{ "12" }}
                            </p>
                        </template>
                    </BadgeText>
                </slot>
            </div>
            <div
                id="5629_42871"
                class="stroke-wrapper-5629_42871"
                v-if="
                    State === 'Default' &&
                    Style === 'Bottom Border' &&
                    Size === 'lg' &&
                    Width === 'Fixed'
                "
            >
                <div class="Pixso-symbol-5629_42871">
                    <slot name="slot_5629_42872" v-if="visible_5629_708">
                        <User
                            id="5629_42872"
                            class="Pixso-instance-5629_42872"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                    <slot name="slot_5629_42873">
                        <p
                            id="5629_42873"
                            class="Pixso-paragraph-5629_42873 fill-gray60-83_2722-paragraph text-text-mdbold-423_3205"
                        >
                            {{ text_5629_714 ?? "Tab Text" }}
                        </p>
                    </slot>
                    <slot name="slot_5629_42874" v-if="visible_5560_235">
                        <BadgeText
                            id="5629_42874"
                            class="Pixso-instance-5629_42874"
                            :visible_5586_119="false"
                            :visible_5586_121="false"
                            :visible_5586_123="false"
                            text_5588_129="12"
                            Size="sm"
                            Color="Brand"
                            Hierarchy="Secondary"
                            State="Default"
                        >
                            <template #slot_5588_11362>
                                <p
                                    id="5588_11362"
                                    class="Pixso-paragraph-5588_11362 fill-brand60-1257_33467-paragraph text-text-xssemibold-439_9521"
                                >
                                    {{ "12" }}
                                </p>
                            </template>
                        </BadgeText>
                    </slot>
                </div>
                <div class="stroke-5629_42871 stroke-gray30-35_1481"></div>
            </div>
            <div
                id="5629_41757"
                class="stroke-wrapper-5629_41757"
                v-if="
                    State === 'Disabled' &&
                    Style === 'Outlined' &&
                    Size === 'md' &&
                    Width === 'Fixed'
                "
            >
                <div class="Pixso-symbol-5629_41757">
                    <slot name="slot_5629_41758" v-if="visible_5629_708">
                        <User
                            id="5629_41758"
                            class="Pixso-instance-5629_41758"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                    <slot name="slot_5629_41759">
                        <p
                            id="5629_41759"
                            class="Pixso-paragraph-5629_41759 fill-gray30-35_1481-paragraph text-text-smbold-423_3208"
                        >
                            {{ text_5629_714 ?? "Tab Text" }}
                        </p>
                    </slot>
                    <slot name="slot_5629_41760" v-if="visible_5560_235">
                        <BadgeText
                            id="5629_41760"
                            class="Pixso-instance-5629_41760"
                            :visible_5586_119="false"
                            :visible_5586_121="false"
                            :visible_5586_123="false"
                            text_5588_129="12"
                            Size="sm"
                            Color="Brand"
                            Hierarchy="Secondary"
                            State="Disabled"
                        >
                            <template #slot_5588_13937>
                                <p
                                    id="5588_13937"
                                    class="Pixso-paragraph-5588_13937 fill-brand30-1257_33463-paragraph text-text-xssemibold-439_9521"
                                >
                                    {{ "12" }}
                                </p>
                            </template>
                        </BadgeText>
                    </slot>
                </div>
                <div class="stroke-5629_41757 stroke-gray30-35_1481"></div>
            </div>
            <div
                id="5629_44654"
                class="stroke-wrapper-5629_44654"
                v-if="
                    State === 'Disabled' &&
                    Style === 'Left Border' &&
                    Size === 'md' &&
                    Width === 'Fixed'
                "
            >
                <div class="Pixso-symbol-5629_44654 fill-gray0-white-67_3285">
                    <slot name="slot_5629_44655" v-if="visible_5629_708">
                        <User
                            id="5629_44655"
                            class="Pixso-instance-5629_44655"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                    <slot name="slot_5629_44656">
                        <p
                            id="5629_44656"
                            class="Pixso-paragraph-5629_44656 fill-gray30-35_1481-paragraph text-text-smbold-423_3208"
                        >
                            {{ text_5629_714 ?? "Tab Text" }}
                        </p>
                    </slot>
                    <slot name="slot_5629_44657" v-if="visible_5560_235">
                        <BadgeText
                            id="5629_44657"
                            class="Pixso-instance-5629_44657"
                            :visible_5586_119="false"
                            :visible_5586_121="false"
                            :visible_5586_123="false"
                            text_5588_129="12"
                            Size="sm"
                            Color="Brand"
                            Hierarchy="Secondary"
                            State="Disabled"
                        >
                            <template #slot_5588_13937>
                                <p
                                    id="5588_13937"
                                    class="Pixso-paragraph-5588_13937 fill-brand30-1257_33463-paragraph text-text-xssemibold-439_9521"
                                >
                                    {{ "12" }}
                                </p>
                            </template>
                        </BadgeText>
                    </slot>
                </div>
                <div class="stroke-5629_44654 stroke-gray30-35_1481"></div>
            </div>
            <div
                id="5629_42113"
                class="Pixso-symbol-5629_42113"
                v-if="
                    State === 'Default' &&
                    Style === 'Default' &&
                    Size === 'lg' &&
                    Width === 'Hug'
                "
            >
                <slot name="slot_5629_42114" v-if="visible_5629_708">
                    <User
                        id="5629_42114"
                        class="Pixso-instance-5629_42114"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <slot name="slot_5629_42115">
                    <p
                        id="5629_42115"
                        class="Pixso-paragraph-5629_42115 fill-gray60-83_2722-paragraph text-text-mdbold-423_3205"
                    >
                        {{ text_5629_714 ?? "Tab Text" }}
                    </p>
                </slot>
                <slot name="slot_5629_42116" v-if="visible_5560_235">
                    <BadgeText
                        id="5629_42116"
                        class="Pixso-instance-5629_42116"
                        :visible_5586_119="false"
                        :visible_5586_121="false"
                        :visible_5586_123="false"
                        text_5588_129="12"
                        Size="sm"
                        Color="Brand"
                        Hierarchy="Secondary"
                        State="Default"
                    >
                        <template #slot_5588_11362>
                            <p
                                id="5588_11362"
                                class="Pixso-paragraph-5588_11362 fill-brand60-1257_33467-paragraph text-text-xssemibold-439_9521"
                            >
                                {{ "12" }}
                            </p>
                        </template>
                    </BadgeText>
                </slot>
            </div>
            <div
                id="5629_42599"
                class="Pixso-symbol-5629_42599 fill-gray0-white-67_3285"
                v-if="
                    State === 'Default' &&
                    Style === 'Outlined' &&
                    Size === 'lg' &&
                    Width === 'Hug'
                "
            >
                <slot name="slot_5629_42600" v-if="visible_5629_708">
                    <User
                        id="5629_42600"
                        class="Pixso-instance-5629_42600"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <slot name="slot_5629_42601">
                    <p
                        id="5629_42601"
                        class="Pixso-paragraph-5629_42601 fill-gray60-83_2722-paragraph text-text-mdbold-423_3205"
                    >
                        {{ text_5629_714 ?? "Tab Text" }}
                    </p>
                </slot>
                <slot name="slot_5629_42602" v-if="visible_5560_235">
                    <BadgeText
                        id="5629_42602"
                        class="Pixso-instance-5629_42602"
                        :visible_5586_119="false"
                        :visible_5586_121="false"
                        :visible_5586_123="false"
                        text_5588_129="12"
                        Size="sm"
                        Color="Brand"
                        Hierarchy="Secondary"
                        State="Default"
                    >
                        <template #slot_5588_11362>
                            <p
                                id="5588_11362"
                                class="Pixso-paragraph-5588_11362 fill-brand60-1257_33467-paragraph text-text-xssemibold-439_9521"
                            >
                                {{ "12" }}
                            </p>
                        </template>
                    </BadgeText>
                </slot>
            </div>
            <div
                id="5629_42691"
                class="stroke-wrapper-5629_42691"
                v-if="
                    State === 'Default' &&
                    Style === 'Bottom Border' &&
                    Size === 'lg' &&
                    Width === 'Hug'
                "
            >
                <div class="Pixso-symbol-5629_42691">
                    <slot name="slot_5629_42692" v-if="visible_5629_708">
                        <User
                            id="5629_42692"
                            class="Pixso-instance-5629_42692"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                    <slot name="slot_5629_42693">
                        <p
                            id="5629_42693"
                            class="Pixso-paragraph-5629_42693 fill-gray60-83_2722-paragraph text-text-mdbold-423_3205"
                        >
                            {{ text_5629_714 ?? "Tab Text" }}
                        </p>
                    </slot>
                    <slot name="slot_5629_42694" v-if="visible_5560_235">
                        <BadgeText
                            id="5629_42694"
                            class="Pixso-instance-5629_42694"
                            :visible_5586_119="false"
                            :visible_5586_121="false"
                            :visible_5586_123="false"
                            text_5588_129="12"
                            Size="sm"
                            Color="Brand"
                            Hierarchy="Secondary"
                            State="Default"
                        >
                            <template #slot_5588_11362>
                                <p
                                    id="5588_11362"
                                    class="Pixso-paragraph-5588_11362 fill-brand60-1257_33467-paragraph text-text-xssemibold-439_9521"
                                >
                                    {{ "12" }}
                                </p>
                            </template>
                        </BadgeText>
                    </slot>
                </div>
                <div class="stroke-5629_42691 stroke-gray30-35_1481"></div>
            </div>
            <div
                id="5629_44454"
                class="stroke-wrapper-5629_44454"
                v-if="
                    State === 'Default' &&
                    Style === 'Left Border' &&
                    Size === 'lg' &&
                    Width === 'Hug'
                "
            >
                <div class="Pixso-symbol-5629_44454 fill-gray0-white-67_3285">
                    <slot name="slot_5629_44455" v-if="visible_5629_708">
                        <User
                            id="5629_44455"
                            class="Pixso-instance-5629_44455"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                    <slot name="slot_5629_44456">
                        <p
                            id="5629_44456"
                            class="Pixso-paragraph-5629_44456 fill-gray60-83_2722-paragraph text-text-mdbold-423_3205"
                        >
                            {{ text_5629_714 ?? "Tab Text" }}
                        </p>
                    </slot>
                    <slot name="slot_5629_44457" v-if="visible_5560_235">
                        <BadgeText
                            id="5629_44457"
                            class="Pixso-instance-5629_44457"
                            :visible_5586_119="false"
                            :visible_5586_121="false"
                            :visible_5586_123="false"
                            text_5588_129="12"
                            Size="sm"
                            Color="Brand"
                            Hierarchy="Secondary"
                            State="Default"
                        >
                            <template #slot_5588_11362>
                                <p
                                    id="5588_11362"
                                    class="Pixso-paragraph-5588_11362 fill-brand60-1257_33467-paragraph text-text-xssemibold-439_9521"
                                >
                                    {{ "12" }}
                                </p>
                            </template>
                        </BadgeText>
                    </slot>
                </div>
                <div class="stroke-5629_44454 stroke-gray30-35_1481"></div>
            </div>
            <div
                id="5629_42899"
                class="stroke-wrapper-5629_42899"
                v-if="
                    State === 'Hover' &&
                    Style === 'Bottom Border' &&
                    Size === 'lg' &&
                    Width === 'Fixed'
                "
            >
                <div class="Pixso-symbol-5629_42899 fill-gray5-32_4120">
                    <slot name="slot_5629_42900" v-if="visible_5629_708">
                        <User
                            id="5629_42900"
                            class="Pixso-instance-5629_42900"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                    <slot name="slot_5629_42901">
                        <p
                            id="5629_42901"
                            class="Pixso-paragraph-5629_42901 fill-gray60-83_2722-paragraph text-text-mdbold-423_3205"
                        >
                            {{ text_5629_714 ?? "Tab Text" }}
                        </p>
                    </slot>
                    <slot name="slot_5629_42902" v-if="visible_5560_235">
                        <BadgeText
                            id="5629_42902"
                            class="Pixso-instance-5629_42902"
                            :visible_5586_119="false"
                            :visible_5586_121="false"
                            :visible_5586_123="false"
                            text_5588_129="12"
                            Size="sm"
                            Color="Brand"
                            Hierarchy="Secondary"
                            State="Hover"
                        >
                            <template #slot_5588_13118>
                                <p
                                    id="5588_13118"
                                    class="Pixso-paragraph-5588_13118 fill-brand60-1257_33467-paragraph text-text-xssemibold-439_9521"
                                >
                                    {{ "12" }}
                                </p>
                            </template>
                        </BadgeText>
                    </slot>
                </div>
                <div class="stroke-5629_42899 stroke-gray40-83_2714"></div>
            </div>
            <div
                id="5629_42863"
                class="Pixso-symbol-5629_42863"
                v-if="
                    State === 'Default' &&
                    Style === 'Default' &&
                    Size === 'lg' &&
                    Width === 'Fixed'
                "
            >
                <slot name="slot_5629_42864" v-if="visible_5629_708">
                    <User
                        id="5629_42864"
                        class="Pixso-instance-5629_42864"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <slot name="slot_5629_42865">
                    <p
                        id="5629_42865"
                        class="Pixso-paragraph-5629_42865 fill-gray60-83_2722-paragraph text-text-mdbold-423_3205"
                    >
                        {{ text_5629_714 ?? "Tab Text" }}
                    </p>
                </slot>
                <slot name="slot_5629_42866" v-if="visible_5560_235">
                    <BadgeText
                        id="5629_42866"
                        class="Pixso-instance-5629_42866"
                        :visible_5586_119="false"
                        :visible_5586_121="false"
                        :visible_5586_123="false"
                        text_5588_129="12"
                        Size="sm"
                        Color="Brand"
                        Hierarchy="Secondary"
                        State="Default"
                    >
                        <template #slot_5588_11362>
                            <p
                                id="5588_11362"
                                class="Pixso-paragraph-5588_11362 fill-brand60-1257_33467-paragraph text-text-xssemibold-439_9521"
                            >
                                {{ "12" }}
                            </p>
                        </template>
                    </BadgeText>
                </slot>
            </div>
            <div
                id="5629_42867"
                class="Pixso-symbol-5629_42867 fill-gray0-white-67_3285"
                v-if="
                    State === 'Default' &&
                    Style === 'Outlined' &&
                    Size === 'lg' &&
                    Width === 'Fixed'
                "
            >
                <slot name="slot_5629_42868" v-if="visible_5629_708">
                    <User
                        id="5629_42868"
                        class="Pixso-instance-5629_42868"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <slot name="slot_5629_42869">
                    <p
                        id="5629_42869"
                        class="Pixso-paragraph-5629_42869 fill-gray60-83_2722-paragraph text-text-mdbold-423_3205"
                    >
                        {{ text_5629_714 ?? "Tab Text" }}
                    </p>
                </slot>
                <slot name="slot_5629_42870" v-if="visible_5560_235">
                    <BadgeText
                        id="5629_42870"
                        class="Pixso-instance-5629_42870"
                        :visible_5586_119="false"
                        :visible_5586_121="false"
                        :visible_5586_123="false"
                        text_5588_129="12"
                        Size="sm"
                        Color="Brand"
                        Hierarchy="Secondary"
                        State="Default"
                    >
                        <template #slot_5588_11362>
                            <p
                                id="5588_11362"
                                class="Pixso-paragraph-5588_11362 fill-brand60-1257_33467-paragraph text-text-xssemibold-439_9521"
                            >
                                {{ "12" }}
                            </p>
                        </template>
                    </BadgeText>
                </slot>
            </div>
            <div
                id="5629_44658"
                class="stroke-wrapper-5629_44658"
                v-if="
                    State === 'Default' &&
                    Style === 'Left Border' &&
                    Size === 'lg' &&
                    Width === 'Fixed'
                "
            >
                <div class="Pixso-symbol-5629_44658 fill-gray0-white-67_3285">
                    <slot name="slot_5629_44659" v-if="visible_5629_708">
                        <User
                            id="5629_44659"
                            class="Pixso-instance-5629_44659"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                    <slot name="slot_5629_44660">
                        <p
                            id="5629_44660"
                            class="Pixso-paragraph-5629_44660 fill-gray60-83_2722-paragraph text-text-mdbold-423_3205"
                        >
                            {{ text_5629_714 ?? "Tab Text" }}
                        </p>
                    </slot>
                    <slot name="slot_5629_44661" v-if="visible_5560_235">
                        <BadgeText
                            id="5629_44661"
                            class="Pixso-instance-5629_44661"
                            :visible_5586_119="false"
                            :visible_5586_121="false"
                            :visible_5586_123="false"
                            text_5588_129="12"
                            Size="sm"
                            Color="Brand"
                            Hierarchy="Secondary"
                            State="Default"
                        >
                            <template #slot_5588_11362>
                                <p
                                    id="5588_11362"
                                    class="Pixso-paragraph-5588_11362 fill-brand60-1257_33467-paragraph text-text-xssemibold-439_9521"
                                >
                                    {{ "12" }}
                                </p>
                            </template>
                        </BadgeText>
                    </slot>
                </div>
                <div class="stroke-5629_44658 stroke-gray30-35_1481"></div>
            </div>
            <div
                id="5629_42468"
                class="Pixso-symbol-5629_42468 fill-gray5-32_4120"
                v-if="
                    State === 'Hover' &&
                    Style === 'Default' &&
                    Size === 'lg' &&
                    Width === 'Hug'
                "
            >
                <slot name="slot_5629_42469" v-if="visible_5629_708">
                    <User
                        id="5629_42469"
                        class="Pixso-instance-5629_42469"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <slot name="slot_5629_42470">
                    <p
                        id="5629_42470"
                        class="Pixso-paragraph-5629_42470 fill-gray60-83_2722-paragraph text-text-mdbold-423_3205"
                    >
                        {{ text_5629_714 ?? "Tab Text" }}
                    </p>
                </slot>
                <slot name="slot_5629_42471" v-if="visible_5560_235">
                    <BadgeText
                        id="5629_42471"
                        class="Pixso-instance-5629_42471"
                        :visible_5586_119="false"
                        :visible_5586_121="false"
                        :visible_5586_123="false"
                        text_5588_129="12"
                        Size="sm"
                        Color="Brand"
                        Hierarchy="Secondary"
                        State="Hover"
                    >
                        <template #slot_5588_13118>
                            <p
                                id="5588_13118"
                                class="Pixso-paragraph-5588_13118 fill-brand60-1257_33467-paragraph text-text-xssemibold-439_9521"
                            >
                                {{ "12" }}
                            </p>
                        </template>
                    </BadgeText>
                </slot>
            </div>
            <div
                id="5629_42699"
                class="stroke-wrapper-5629_42699"
                v-if="
                    State === 'Hover' &&
                    Style === 'Bottom Border' &&
                    Size === 'lg' &&
                    Width === 'Hug'
                "
            >
                <div class="Pixso-symbol-5629_42699 fill-gray5-32_4120">
                    <slot name="slot_5629_42700" v-if="visible_5629_708">
                        <User
                            id="5629_42700"
                            class="Pixso-instance-5629_42700"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                    <slot name="slot_5629_42701">
                        <p
                            id="5629_42701"
                            class="Pixso-paragraph-5629_42701 fill-gray60-83_2722-paragraph text-text-mdbold-423_3205"
                        >
                            {{ text_5629_714 ?? "Tab Text" }}
                        </p>
                    </slot>
                    <slot name="slot_5629_42702" v-if="visible_5560_235">
                        <BadgeText
                            id="5629_42702"
                            class="Pixso-instance-5629_42702"
                            :visible_5586_119="false"
                            :visible_5586_121="false"
                            :visible_5586_123="false"
                            text_5588_129="12"
                            Size="sm"
                            Color="Brand"
                            Hierarchy="Secondary"
                            State="Hover"
                        >
                            <template #slot_5588_13118>
                                <p
                                    id="5588_13118"
                                    class="Pixso-paragraph-5588_13118 fill-brand60-1257_33467-paragraph text-text-xssemibold-439_9521"
                                >
                                    {{ "12" }}
                                </p>
                            </template>
                        </BadgeText>
                    </slot>
                </div>
                <div class="stroke-5629_42699 stroke-gray40-83_2714"></div>
            </div>
            <div
                id="5629_42607"
                class="stroke-wrapper-5629_42607"
                v-if="
                    State === 'Hover' &&
                    Style === 'Outlined' &&
                    Size === 'lg' &&
                    Width === 'Hug'
                "
            >
                <div class="Pixso-symbol-5629_42607">
                    <slot name="slot_5629_42608" v-if="visible_5629_708">
                        <User
                            id="5629_42608"
                            class="Pixso-instance-5629_42608"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                    <slot name="slot_5629_42609">
                        <p
                            id="5629_42609"
                            class="Pixso-paragraph-5629_42609 fill-gray60-83_2722-paragraph text-text-mdbold-423_3205"
                        >
                            {{ text_5629_714 ?? "Tab Text" }}
                        </p>
                    </slot>
                    <slot name="slot_5629_42610" v-if="visible_5560_235">
                        <BadgeText
                            id="5629_42610"
                            class="Pixso-instance-5629_42610"
                            :visible_5586_119="false"
                            :visible_5586_121="false"
                            :visible_5586_123="false"
                            text_5588_129="12"
                            Size="sm"
                            Color="Brand"
                            Hierarchy="Secondary"
                            State="Hover"
                        >
                            <template #slot_5588_13118>
                                <p
                                    id="5588_13118"
                                    class="Pixso-paragraph-5588_13118 fill-brand60-1257_33467-paragraph text-text-xssemibold-439_9521"
                                >
                                    {{ "12" }}
                                </p>
                            </template>
                        </BadgeText>
                    </slot>
                </div>
                <div class="stroke-5629_42607 stroke-gray30-35_1481"></div>
            </div>
            <div
                id="5629_44458"
                class="stroke-wrapper-5629_44458"
                v-if="
                    State === 'Hover' &&
                    Style === 'Left Border' &&
                    Size === 'lg' &&
                    Width === 'Hug'
                "
            >
                <div class="Pixso-symbol-5629_44458 fill-gray5-32_4120">
                    <slot name="slot_5629_44459" v-if="visible_5629_708">
                        <User
                            id="5629_44459"
                            class="Pixso-instance-5629_44459"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                    <slot name="slot_5629_44460">
                        <p
                            id="5629_44460"
                            class="Pixso-paragraph-5629_44460 fill-gray60-83_2722-paragraph text-text-mdbold-423_3205"
                        >
                            {{ text_5629_714 ?? "Tab Text" }}
                        </p>
                    </slot>
                    <slot name="slot_5629_44461" v-if="visible_5560_235">
                        <BadgeText
                            id="5629_44461"
                            class="Pixso-instance-5629_44461"
                            :visible_5586_119="false"
                            :visible_5586_121="false"
                            :visible_5586_123="false"
                            text_5588_129="12"
                            Size="sm"
                            Color="Brand"
                            Hierarchy="Secondary"
                            State="Hover"
                        >
                            <template #slot_5588_13118>
                                <p
                                    id="5588_13118"
                                    class="Pixso-paragraph-5588_13118 fill-brand60-1257_33467-paragraph text-text-xssemibold-439_9521"
                                >
                                    {{ "12" }}
                                </p>
                            </template>
                        </BadgeText>
                    </slot>
                </div>
                <div class="stroke-5629_44458 stroke-gray40-83_2714"></div>
            </div>
            <div
                id="5629_42907"
                class="stroke-wrapper-5629_42907"
                v-if="
                    State === 'Active' &&
                    Style === 'Bottom Border' &&
                    Size === 'lg' &&
                    Width === 'Fixed'
                "
            >
                <div class="Pixso-symbol-5629_42907">
                    <slot name="slot_5629_42908" v-if="visible_5629_708">
                        <User
                            id="5629_42908"
                            class="Pixso-instance-5629_42908"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                    <slot name="slot_5629_42909">
                        <p
                            id="5629_42909"
                            class="Pixso-paragraph-5629_42909 fill-gray80-32_4123-paragraph text-text-mdbold-423_3205"
                        >
                            {{ text_5629_714 ?? "Tab Text" }}
                        </p>
                    </slot>
                    <slot name="slot_5629_42910" v-if="visible_5560_235">
                        <BadgeText
                            id="5629_42910"
                            class="Pixso-instance-5629_42910"
                            :visible_5586_119="false"
                            :visible_5586_121="false"
                            :visible_5586_123="false"
                            text_5588_129="12"
                            Size="sm"
                            Color="Brand"
                            Hierarchy="Secondary"
                            State="Default"
                        >
                            <template #slot_5588_11362>
                                <p
                                    id="5588_11362"
                                    class="Pixso-paragraph-5588_11362 fill-brand60-1257_33467-paragraph text-text-xssemibold-439_9521"
                                >
                                    {{ "12" }}
                                </p>
                            </template>
                        </BadgeText>
                    </slot>
                </div>
                <div class="stroke-5629_42907 stroke-brand60-1257_33467"></div>
            </div>
            <div
                id="5629_42895"
                class="Pixso-symbol-5629_42895 fill-gray5-32_4120"
                v-if="
                    State === 'Hover' &&
                    Style === 'Default' &&
                    Size === 'lg' &&
                    Width === 'Fixed'
                "
            >
                <slot name="slot_5629_42896" v-if="visible_5629_708">
                    <User
                        id="5629_42896"
                        class="Pixso-instance-5629_42896"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <slot name="slot_5629_42897">
                    <p
                        id="5629_42897"
                        class="Pixso-paragraph-5629_42897 fill-gray60-83_2722-paragraph text-text-mdbold-423_3205"
                    >
                        {{ text_5629_714 ?? "Tab Text" }}
                    </p>
                </slot>
                <slot name="slot_5629_42898" v-if="visible_5560_235">
                    <BadgeText
                        id="5629_42898"
                        class="Pixso-instance-5629_42898"
                        :visible_5586_119="false"
                        :visible_5586_121="false"
                        :visible_5586_123="false"
                        text_5588_129="12"
                        Size="sm"
                        Color="Brand"
                        Hierarchy="Secondary"
                        State="Hover"
                    >
                        <template #slot_5588_13118>
                            <p
                                id="5588_13118"
                                class="Pixso-paragraph-5588_13118 fill-brand60-1257_33467-paragraph text-text-xssemibold-439_9521"
                            >
                                {{ "12" }}
                            </p>
                        </template>
                    </BadgeText>
                </slot>
            </div>
            <div
                id="5629_42883"
                class="stroke-wrapper-5629_42883"
                v-if="
                    State === 'Hover' &&
                    Style === 'Outlined' &&
                    Size === 'lg' &&
                    Width === 'Fixed'
                "
            >
                <div class="Pixso-symbol-5629_42883">
                    <slot name="slot_5629_42884" v-if="visible_5629_708">
                        <User
                            id="5629_42884"
                            class="Pixso-instance-5629_42884"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                    <slot name="slot_5629_42885">
                        <p
                            id="5629_42885"
                            class="Pixso-paragraph-5629_42885 fill-gray60-83_2722-paragraph text-text-mdbold-423_3205"
                        >
                            {{ text_5629_714 ?? "Tab Text" }}
                        </p>
                    </slot>
                    <slot name="slot_5629_42886" v-if="visible_5560_235">
                        <BadgeText
                            id="5629_42886"
                            class="Pixso-instance-5629_42886"
                            :visible_5586_119="false"
                            :visible_5586_121="false"
                            :visible_5586_123="false"
                            text_5588_129="12"
                            Size="sm"
                            Color="Brand"
                            Hierarchy="Secondary"
                            State="Hover"
                        >
                            <template #slot_5588_13118>
                                <p
                                    id="5588_13118"
                                    class="Pixso-paragraph-5588_13118 fill-brand60-1257_33467-paragraph text-text-xssemibold-439_9521"
                                >
                                    {{ "12" }}
                                </p>
                            </template>
                        </BadgeText>
                    </slot>
                </div>
                <div class="stroke-5629_42883 stroke-gray30-35_1481"></div>
            </div>
            <div
                id="5629_44662"
                class="stroke-wrapper-5629_44662"
                v-if="
                    State === 'Hover' &&
                    Style === 'Left Border' &&
                    Size === 'lg' &&
                    Width === 'Fixed'
                "
            >
                <div class="Pixso-symbol-5629_44662 fill-gray5-32_4120">
                    <slot name="slot_5629_44663" v-if="visible_5629_708">
                        <User
                            id="5629_44663"
                            class="Pixso-instance-5629_44663"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                    <slot name="slot_5629_44664">
                        <p
                            id="5629_44664"
                            class="Pixso-paragraph-5629_44664 fill-gray60-83_2722-paragraph text-text-mdbold-423_3205"
                        >
                            {{ text_5629_714 ?? "Tab Text" }}
                        </p>
                    </slot>
                    <slot name="slot_5629_44665" v-if="visible_5560_235">
                        <BadgeText
                            id="5629_44665"
                            class="Pixso-instance-5629_44665"
                            :visible_5586_119="false"
                            :visible_5586_121="false"
                            :visible_5586_123="false"
                            text_5588_129="12"
                            Size="sm"
                            Color="Brand"
                            Hierarchy="Secondary"
                            State="Hover"
                        >
                            <template #slot_5588_13118>
                                <p
                                    id="5588_13118"
                                    class="Pixso-paragraph-5588_13118 fill-brand60-1257_33467-paragraph text-text-xssemibold-439_9521"
                                >
                                    {{ "12" }}
                                </p>
                            </template>
                        </BadgeText>
                    </slot>
                </div>
                <div class="stroke-5629_44662 stroke-gray40-83_2714"></div>
            </div>
            <div
                id="5629_42703"
                class="stroke-wrapper-5629_42703"
                v-if="
                    State === 'Active' &&
                    Style === 'Bottom Border' &&
                    Size === 'lg' &&
                    Width === 'Hug'
                "
            >
                <div class="Pixso-symbol-5629_42703">
                    <slot name="slot_5629_42704" v-if="visible_5629_708">
                        <User
                            id="5629_42704"
                            class="Pixso-instance-5629_42704"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                    <slot name="slot_5629_42705">
                        <p
                            id="5629_42705"
                            class="Pixso-paragraph-5629_42705 fill-gray80-32_4123-paragraph text-text-mdbold-423_3205"
                        >
                            {{ text_5629_714 ?? "Tab Text" }}
                        </p>
                    </slot>
                    <slot name="slot_5629_42706" v-if="visible_5560_235">
                        <BadgeText
                            id="5629_42706"
                            class="Pixso-instance-5629_42706"
                            :visible_5586_119="false"
                            :visible_5586_121="false"
                            :visible_5586_123="false"
                            text_5588_129="12"
                            Size="sm"
                            Color="Brand"
                            Hierarchy="Secondary"
                            State="Default"
                        >
                            <template #slot_5588_11362>
                                <p
                                    id="5588_11362"
                                    class="Pixso-paragraph-5588_11362 fill-brand60-1257_33467-paragraph text-text-xssemibold-439_9521"
                                >
                                    {{ "12" }}
                                </p>
                            </template>
                        </BadgeText>
                    </slot>
                </div>
                <div class="stroke-5629_42703 stroke-brand60-1257_33467"></div>
            </div>
            <div
                id="5629_42499"
                class="Pixso-symbol-5629_42499 fill-gray0-white-67_3285 effect-shadowmd-5457_24364"
                v-if="
                    State === 'Active' &&
                    Style === 'Default' &&
                    Size === 'lg' &&
                    Width === 'Hug'
                "
            >
                <slot name="slot_5629_42500" v-if="visible_5629_708">
                    <User
                        id="5629_42500"
                        class="Pixso-instance-5629_42500"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <slot name="slot_5629_42501">
                    <p
                        id="5629_42501"
                        class="Pixso-paragraph-5629_42501 fill-gray80-32_4123-paragraph text-text-mdbold-423_3205"
                    >
                        {{ text_5629_714 ?? "Tab Text" }}
                    </p>
                </slot>
                <slot name="slot_5629_42502" v-if="visible_5560_235">
                    <BadgeText
                        id="5629_42502"
                        class="Pixso-instance-5629_42502"
                        :visible_5586_119="false"
                        :visible_5586_121="false"
                        :visible_5586_123="false"
                        text_5588_129="12"
                        Size="sm"
                        Color="Brand"
                        Hierarchy="Secondary"
                        State="Default"
                    >
                        <template #slot_5588_11362>
                            <p
                                id="5588_11362"
                                class="Pixso-paragraph-5588_11362 fill-brand60-1257_33467-paragraph text-text-xssemibold-439_9521"
                            >
                                {{ "12" }}
                            </p>
                        </template>
                    </BadgeText>
                </slot>
            </div>
            <div
                id="5629_42887"
                class="stroke-wrapper-5629_42887"
                v-if="
                    State === 'Disabled' &&
                    Style === 'Bottom Border' &&
                    Size === 'lg' &&
                    Width === 'Fixed'
                "
            >
                <div class="Pixso-symbol-5629_42887 fill-gray0-white-67_3285">
                    <slot name="slot_5629_42888" v-if="visible_5629_708">
                        <User
                            id="5629_42888"
                            class="Pixso-instance-5629_42888"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                    <slot name="slot_5629_42889">
                        <p
                            id="5629_42889"
                            class="Pixso-paragraph-5629_42889 fill-gray30-35_1481-paragraph text-text-mdbold-423_3205"
                        >
                            {{ text_5629_714 ?? "Tab Text" }}
                        </p>
                    </slot>
                    <slot name="slot_5629_42890" v-if="visible_5560_235">
                        <BadgeText
                            id="5629_42890"
                            class="Pixso-instance-5629_42890"
                            :visible_5586_119="false"
                            :visible_5586_121="false"
                            :visible_5586_123="false"
                            text_5588_129="12"
                            Size="sm"
                            Color="Brand"
                            Hierarchy="Secondary"
                            State="Disabled"
                        >
                            <template #slot_5588_13937>
                                <p
                                    id="5588_13937"
                                    class="Pixso-paragraph-5588_13937 fill-brand30-1257_33463-paragraph text-text-xssemibold-439_9521"
                                >
                                    {{ "12" }}
                                </p>
                            </template>
                        </BadgeText>
                    </slot>
                </div>
                <div class="stroke-5629_42887 stroke-gray30-35_1481"></div>
            </div>
            <div
                id="5629_42611"
                class="stroke-wrapper-5629_42611"
                v-if="
                    State === 'Active' &&
                    Style === 'Outlined' &&
                    Size === 'lg' &&
                    Width === 'Hug'
                "
            >
                <div class="Pixso-symbol-5629_42611">
                    <slot name="slot_5629_42612" v-if="visible_5629_708">
                        <User
                            id="5629_42612"
                            class="Pixso-instance-5629_42612"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                    <slot name="slot_5629_42613">
                        <p
                            id="5629_42613"
                            class="Pixso-paragraph-5629_42613 fill-gray80-32_4123-paragraph text-text-mdbold-423_3205"
                        >
                            {{ text_5629_714 ?? "Tab Text" }}
                        </p>
                    </slot>
                    <slot name="slot_5629_42614" v-if="visible_5560_235">
                        <BadgeText
                            id="5629_42614"
                            class="Pixso-instance-5629_42614"
                            :visible_5586_119="false"
                            :visible_5586_121="false"
                            :visible_5586_123="false"
                            text_5588_129="12"
                            Size="sm"
                            Color="Brand"
                            Hierarchy="Secondary"
                            State="Default"
                        >
                            <template #slot_5588_11362>
                                <p
                                    id="5588_11362"
                                    class="Pixso-paragraph-5588_11362 fill-brand60-1257_33467-paragraph text-text-xssemibold-439_9521"
                                >
                                    {{ "12" }}
                                </p>
                            </template>
                        </BadgeText>
                    </slot>
                </div>
                <div class="stroke-5629_42611 stroke-brand60-1257_33467"></div>
            </div>
            <div
                id="5629_44462"
                class="stroke-wrapper-5629_44462"
                v-if="
                    State === 'Active' &&
                    Style === 'Left Border' &&
                    Size === 'lg' &&
                    Width === 'Hug'
                "
            >
                <div class="Pixso-symbol-5629_44462 fill-gray0-white-67_3285">
                    <slot name="slot_5629_44463" v-if="visible_5629_708">
                        <User
                            id="5629_44463"
                            class="Pixso-instance-5629_44463"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                    <slot name="slot_5629_44464">
                        <p
                            id="5629_44464"
                            class="Pixso-paragraph-5629_44464 fill-gray80-32_4123-paragraph text-text-mdbold-423_3205"
                        >
                            {{ text_5629_714 ?? "Tab Text" }}
                        </p>
                    </slot>
                    <slot name="slot_5629_44465" v-if="visible_5560_235">
                        <BadgeText
                            id="5629_44465"
                            class="Pixso-instance-5629_44465"
                            :visible_5586_119="false"
                            :visible_5586_121="false"
                            :visible_5586_123="false"
                            text_5588_129="12"
                            Size="sm"
                            Color="Brand"
                            Hierarchy="Secondary"
                            State="Default"
                        >
                            <template #slot_5588_11362>
                                <p
                                    id="5588_11362"
                                    class="Pixso-paragraph-5588_11362 fill-brand60-1257_33467-paragraph text-text-xssemibold-439_9521"
                                >
                                    {{ "12" }}
                                </p>
                            </template>
                        </BadgeText>
                    </slot>
                </div>
                <div class="stroke-5629_44462 stroke-brand60-1257_33467"></div>
            </div>
            <div
                id="5629_42903"
                class="Pixso-symbol-5629_42903 fill-gray0-white-67_3285 effect-shadowmd-5457_24364"
                v-if="
                    State === 'Active' &&
                    Style === 'Default' &&
                    Size === 'lg' &&
                    Width === 'Fixed'
                "
            >
                <slot name="slot_5629_42904" v-if="visible_5629_708">
                    <User
                        id="5629_42904"
                        class="Pixso-instance-5629_42904"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <slot name="slot_5629_42905">
                    <p
                        id="5629_42905"
                        class="Pixso-paragraph-5629_42905 fill-gray80-32_4123-paragraph text-text-mdbold-423_3205"
                    >
                        {{ text_5629_714 ?? "Tab Text" }}
                    </p>
                </slot>
                <slot name="slot_5629_42906" v-if="visible_5560_235">
                    <BadgeText
                        id="5629_42906"
                        class="Pixso-instance-5629_42906"
                        :visible_5586_119="false"
                        :visible_5586_121="false"
                        :visible_5586_123="false"
                        text_5588_129="12"
                        Size="sm"
                        Color="Brand"
                        Hierarchy="Secondary"
                        State="Default"
                    >
                        <template #slot_5588_11362>
                            <p
                                id="5588_11362"
                                class="Pixso-paragraph-5588_11362 fill-brand60-1257_33467-paragraph text-text-xssemibold-439_9521"
                            >
                                {{ "12" }}
                            </p>
                        </template>
                    </BadgeText>
                </slot>
            </div>
            <div
                id="5629_42891"
                class="stroke-wrapper-5629_42891"
                v-if="
                    State === 'Active' &&
                    Style === 'Outlined' &&
                    Size === 'lg' &&
                    Width === 'Fixed'
                "
            >
                <div class="Pixso-symbol-5629_42891">
                    <slot name="slot_5629_42892" v-if="visible_5629_708">
                        <User
                            id="5629_42892"
                            class="Pixso-instance-5629_42892"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                    <slot name="slot_5629_42893">
                        <p
                            id="5629_42893"
                            class="Pixso-paragraph-5629_42893 fill-gray80-32_4123-paragraph text-text-mdbold-423_3205"
                        >
                            {{ text_5629_714 ?? "Tab Text" }}
                        </p>
                    </slot>
                    <slot name="slot_5629_42894" v-if="visible_5560_235">
                        <BadgeText
                            id="5629_42894"
                            class="Pixso-instance-5629_42894"
                            :visible_5586_119="false"
                            :visible_5586_121="false"
                            :visible_5586_123="false"
                            text_5588_129="12"
                            Size="sm"
                            Color="Brand"
                            Hierarchy="Secondary"
                            State="Default"
                        >
                            <template #slot_5588_11362>
                                <p
                                    id="5588_11362"
                                    class="Pixso-paragraph-5588_11362 fill-brand60-1257_33467-paragraph text-text-xssemibold-439_9521"
                                >
                                    {{ "12" }}
                                </p>
                            </template>
                        </BadgeText>
                    </slot>
                </div>
                <div class="stroke-5629_42891 stroke-brand60-1257_33467"></div>
            </div>
            <div
                id="5629_42695"
                class="stroke-wrapper-5629_42695"
                v-if="
                    State === 'Disabled' &&
                    Style === 'Bottom Border' &&
                    Size === 'lg' &&
                    Width === 'Hug'
                "
            >
                <div class="Pixso-symbol-5629_42695 fill-gray0-white-67_3285">
                    <slot name="slot_5629_42696" v-if="visible_5629_708">
                        <User
                            id="5629_42696"
                            class="Pixso-instance-5629_42696"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                    <slot name="slot_5629_42697">
                        <p
                            id="5629_42697"
                            class="Pixso-paragraph-5629_42697 fill-gray30-35_1481-paragraph text-text-mdbold-423_3205"
                        >
                            {{ text_5629_714 ?? "Tab Text" }}
                        </p>
                    </slot>
                    <slot name="slot_5629_42698" v-if="visible_5560_235">
                        <BadgeText
                            id="5629_42698"
                            class="Pixso-instance-5629_42698"
                            :visible_5586_119="false"
                            :visible_5586_121="false"
                            :visible_5586_123="false"
                            text_5588_129="12"
                            Size="sm"
                            Color="Brand"
                            Hierarchy="Secondary"
                            State="Disabled"
                        >
                            <template #slot_5588_13937>
                                <p
                                    id="5588_13937"
                                    class="Pixso-paragraph-5588_13937 fill-brand30-1257_33463-paragraph text-text-xssemibold-439_9521"
                                >
                                    {{ "12" }}
                                </p>
                            </template>
                        </BadgeText>
                    </slot>
                </div>
                <div class="stroke-5629_42695 stroke-gray30-35_1481"></div>
            </div>
            <div
                id="5629_44666"
                class="stroke-wrapper-5629_44666"
                v-if="
                    State === 'Active' &&
                    Style === 'Left Border' &&
                    Size === 'lg' &&
                    Width === 'Fixed'
                "
            >
                <div class="Pixso-symbol-5629_44666 fill-gray0-white-67_3285">
                    <slot name="slot_5629_44667" v-if="visible_5629_708">
                        <User
                            id="5629_44667"
                            class="Pixso-instance-5629_44667"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                    <slot name="slot_5629_44668">
                        <p
                            id="5629_44668"
                            class="Pixso-paragraph-5629_44668 fill-gray80-32_4123-paragraph text-text-mdbold-423_3205"
                        >
                            {{ text_5629_714 ?? "Tab Text" }}
                        </p>
                    </slot>
                    <slot name="slot_5629_44669" v-if="visible_5560_235">
                        <BadgeText
                            id="5629_44669"
                            class="Pixso-instance-5629_44669"
                            :visible_5586_119="false"
                            :visible_5586_121="false"
                            :visible_5586_123="false"
                            text_5588_129="12"
                            Size="sm"
                            Color="Brand"
                            Hierarchy="Secondary"
                            State="Default"
                        >
                            <template #slot_5588_11362>
                                <p
                                    id="5588_11362"
                                    class="Pixso-paragraph-5588_11362 fill-brand60-1257_33467-paragraph text-text-xssemibold-439_9521"
                                >
                                    {{ "12" }}
                                </p>
                            </template>
                        </BadgeText>
                    </slot>
                </div>
                <div class="stroke-5629_44666 stroke-brand60-1257_33467"></div>
            </div>
            <div
                id="5629_42538"
                class="Pixso-symbol-5629_42538"
                v-if="
                    State === 'Disabled' &&
                    Style === 'Default' &&
                    Size === 'lg' &&
                    Width === 'Hug'
                "
            >
                <slot name="slot_5629_42539" v-if="visible_5629_708">
                    <User
                        id="5629_42539"
                        class="Pixso-instance-5629_42539"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <slot name="slot_5629_42540">
                    <p
                        id="5629_42540"
                        class="Pixso-paragraph-5629_42540 fill-gray30-35_1481-paragraph text-text-mdbold-423_3205"
                    >
                        {{ text_5629_714 ?? "Tab Text" }}
                    </p>
                </slot>
                <slot name="slot_5629_42541" v-if="visible_5560_235">
                    <BadgeText
                        id="5629_42541"
                        class="Pixso-instance-5629_42541"
                        :visible_5586_119="false"
                        :visible_5586_121="false"
                        :visible_5586_123="false"
                        text_5588_129="12"
                        Size="sm"
                        Color="Brand"
                        Hierarchy="Secondary"
                        State="Disabled"
                    >
                        <template #slot_5588_13937>
                            <p
                                id="5588_13937"
                                class="Pixso-paragraph-5588_13937 fill-brand30-1257_33463-paragraph text-text-xssemibold-439_9521"
                            >
                                {{ "12" }}
                            </p>
                        </template>
                    </BadgeText>
                </slot>
            </div>
            <div
                id="5629_42603"
                class="stroke-wrapper-5629_42603"
                v-if="
                    State === 'Disabled' &&
                    Style === 'Outlined' &&
                    Size === 'lg' &&
                    Width === 'Hug'
                "
            >
                <div class="Pixso-symbol-5629_42603 fill-gray0-white-67_3285">
                    <slot name="slot_5629_42604" v-if="visible_5629_708">
                        <User
                            id="5629_42604"
                            class="Pixso-instance-5629_42604"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                    <slot name="slot_5629_42605">
                        <p
                            id="5629_42605"
                            class="Pixso-paragraph-5629_42605 fill-gray30-35_1481-paragraph text-text-mdbold-423_3205"
                        >
                            {{ text_5629_714 ?? "Tab Text" }}
                        </p>
                    </slot>
                    <slot name="slot_5629_42606" v-if="visible_5560_235">
                        <BadgeText
                            id="5629_42606"
                            class="Pixso-instance-5629_42606"
                            :visible_5586_119="false"
                            :visible_5586_121="false"
                            :visible_5586_123="false"
                            text_5588_129="12"
                            Size="sm"
                            Color="Brand"
                            Hierarchy="Secondary"
                            State="Disabled"
                        >
                            <template #slot_5588_13937>
                                <p
                                    id="5588_13937"
                                    class="Pixso-paragraph-5588_13937 fill-brand30-1257_33463-paragraph text-text-xssemibold-439_9521"
                                >
                                    {{ "12" }}
                                </p>
                            </template>
                        </BadgeText>
                    </slot>
                </div>
                <div class="stroke-5629_42603 stroke-gray30-35_1481"></div>
            </div>
            <div
                id="5629_44466"
                class="stroke-wrapper-5629_44466"
                v-if="
                    State === 'Disabled' &&
                    Style === 'Left Border' &&
                    Size === 'lg' &&
                    Width === 'Hug'
                "
            >
                <div class="Pixso-symbol-5629_44466 fill-gray0-white-67_3285">
                    <slot name="slot_5629_44467" v-if="visible_5629_708">
                        <User
                            id="5629_44467"
                            class="Pixso-instance-5629_44467"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                    <slot name="slot_5629_44468">
                        <p
                            id="5629_44468"
                            class="Pixso-paragraph-5629_44468 fill-gray30-35_1481-paragraph text-text-mdbold-423_3205"
                        >
                            {{ text_5629_714 ?? "Tab Text" }}
                        </p>
                    </slot>
                    <slot name="slot_5629_44469" v-if="visible_5560_235">
                        <BadgeText
                            id="5629_44469"
                            class="Pixso-instance-5629_44469"
                            :visible_5586_119="false"
                            :visible_5586_121="false"
                            :visible_5586_123="false"
                            text_5588_129="12"
                            Size="sm"
                            Color="Brand"
                            Hierarchy="Secondary"
                            State="Disabled"
                        >
                            <template #slot_5588_13937>
                                <p
                                    id="5588_13937"
                                    class="Pixso-paragraph-5588_13937 fill-brand30-1257_33463-paragraph text-text-xssemibold-439_9521"
                                >
                                    {{ "12" }}
                                </p>
                            </template>
                        </BadgeText>
                    </slot>
                </div>
                <div class="stroke-5629_44466 stroke-gray30-35_1481"></div>
            </div>
            <div
                id="5629_42879"
                class="Pixso-symbol-5629_42879"
                v-if="
                    State === 'Disabled' &&
                    Style === 'Default' &&
                    Size === 'lg' &&
                    Width === 'Fixed'
                "
            >
                <slot name="slot_5629_42880" v-if="visible_5629_708">
                    <User
                        id="5629_42880"
                        class="Pixso-instance-5629_42880"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <slot name="slot_5629_42881">
                    <p
                        id="5629_42881"
                        class="Pixso-paragraph-5629_42881 fill-gray30-35_1481-paragraph text-text-mdbold-423_3205"
                    >
                        {{ text_5629_714 ?? "Tab Text" }}
                    </p>
                </slot>
                <slot name="slot_5629_42882" v-if="visible_5560_235">
                    <BadgeText
                        id="5629_42882"
                        class="Pixso-instance-5629_42882"
                        :visible_5586_119="false"
                        :visible_5586_121="false"
                        :visible_5586_123="false"
                        text_5588_129="12"
                        Size="sm"
                        Color="Brand"
                        Hierarchy="Secondary"
                        State="Disabled"
                    >
                        <template #slot_5588_13937>
                            <p
                                id="5588_13937"
                                class="Pixso-paragraph-5588_13937 fill-brand30-1257_33463-paragraph text-text-xssemibold-439_9521"
                            >
                                {{ "12" }}
                            </p>
                        </template>
                    </BadgeText>
                </slot>
            </div>
            <div
                id="5629_42875"
                class="stroke-wrapper-5629_42875"
                v-if="
                    State === 'Disabled' &&
                    Style === 'Outlined' &&
                    Size === 'lg' &&
                    Width === 'Fixed'
                "
            >
                <div class="Pixso-symbol-5629_42875 fill-gray0-white-67_3285">
                    <slot name="slot_5629_42876" v-if="visible_5629_708">
                        <User
                            id="5629_42876"
                            class="Pixso-instance-5629_42876"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                    <slot name="slot_5629_42877">
                        <p
                            id="5629_42877"
                            class="Pixso-paragraph-5629_42877 fill-gray30-35_1481-paragraph text-text-mdbold-423_3205"
                        >
                            {{ text_5629_714 ?? "Tab Text" }}
                        </p>
                    </slot>
                    <slot name="slot_5629_42878" v-if="visible_5560_235">
                        <BadgeText
                            id="5629_42878"
                            class="Pixso-instance-5629_42878"
                            :visible_5586_119="false"
                            :visible_5586_121="false"
                            :visible_5586_123="false"
                            text_5588_129="12"
                            Size="sm"
                            Color="Brand"
                            Hierarchy="Secondary"
                            State="Disabled"
                        >
                            <template #slot_5588_13937>
                                <p
                                    id="5588_13937"
                                    class="Pixso-paragraph-5588_13937 fill-brand30-1257_33463-paragraph text-text-xssemibold-439_9521"
                                >
                                    {{ "12" }}
                                </p>
                            </template>
                        </BadgeText>
                    </slot>
                </div>
                <div class="stroke-5629_42875 stroke-gray30-35_1481"></div>
            </div>
            <div
                id="5629_44670"
                class="stroke-wrapper-5629_44670"
                v-if="
                    State === 'Disabled' &&
                    Style === 'Left Border' &&
                    Size === 'lg' &&
                    Width === 'Fixed'
                "
            >
                <div class="Pixso-symbol-5629_44670 fill-gray0-white-67_3285">
                    <slot name="slot_5629_44671" v-if="visible_5629_708">
                        <User
                            id="5629_44671"
                            class="Pixso-instance-5629_44671"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                    <slot name="slot_5629_44672">
                        <p
                            id="5629_44672"
                            class="Pixso-paragraph-5629_44672 fill-gray30-35_1481-paragraph text-text-mdbold-423_3205"
                        >
                            {{ text_5629_714 ?? "Tab Text" }}
                        </p>
                    </slot>
                    <slot name="slot_5629_44673" v-if="visible_5560_235">
                        <BadgeText
                            id="5629_44673"
                            class="Pixso-instance-5629_44673"
                            :visible_5586_119="false"
                            :visible_5586_121="false"
                            :visible_5586_123="false"
                            text_5588_129="12"
                            Size="sm"
                            Color="Brand"
                            Hierarchy="Secondary"
                            State="Disabled"
                        >
                            <template #slot_5588_13937>
                                <p
                                    id="5588_13937"
                                    class="Pixso-paragraph-5588_13937 fill-brand30-1257_33463-paragraph text-text-xssemibold-439_9521"
                                >
                                    {{ "12" }}
                                </p>
                            </template>
                        </BadgeText>
                    </slot>
                </div>
                <div class="stroke-5629_44670 stroke-gray30-35_1481"></div>
            </div>
        </div>
    </div>
</template>
<script lang="ts" setup>
import User from "@/components/User.vue";
import BadgeText from "@/components/Badgetext.vue";
const props = defineProps({
    visible_5560_235: { type: Boolean, default: true },
    visible_5629_708: { type: Boolean, default: true },
    instance_5629_711: { type: String, default: "Component_5579_152455" },
    text_5629_714: { type: String, default: "Tab Text" },
    State: { type: String },
    Style: { type: String },
    Size: { type: String },
    Width: { type: String }
});
</script>
<style>
.Pixso-symbol-5558_51607 {
}
.Pixso-symbol-5629_43319 {
    width: auto;
    height: auto;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 8px 12px 8px 12px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_43320 {
    width: 16px;
    height: 16px;
}
.Pixso-paragraph-5629_43321 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_43322 {
    width: 24px;
    height: 20px;
}
.Pixso-paragraph-5588_11362 {
    text-align: center;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    width: auto;
    height: auto;
    flex-grow: 0;
}
.Pixso-symbol-5629_43810 {
    width: auto;
    height: auto;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 8px 12px 8px 12px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_43811 {
    width: 16px;
    height: 16px;
}
.Pixso-paragraph-5629_43812 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_43813 {
    width: 24px;
    height: 20px;
}
.Pixso-symbol-5629_43902 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 8px 12px 8px 12px;
}
.stroke-wrapper-5629_43902 {
    position: relative;
    width: auto;
    height: auto;
    display: flex;
}
.stroke-5629_43902 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 2px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5629_43903 {
    width: 16px;
    height: 16px;
}
.Pixso-paragraph-5629_43904 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_43905 {
    width: 24px;
    height: 20px;
}
.Pixso-symbol-5629_44270 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 8px 12px 8px 12px;
}
.stroke-wrapper-5629_44270 {
    position: relative;
    width: auto;
    height: auto;
    display: flex;
}
.stroke-5629_44270 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 0px 2px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5629_44271 {
    width: 16px;
    height: 16px;
}
.Pixso-paragraph-5629_44272 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_44273 {
    width: 24px;
    height: 20px;
}
.Pixso-symbol-5629_44074 {
    width: 240px;
    height: auto;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 8px 12px 8px 12px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_44075 {
    width: 16px;
    height: 16px;
}
.Pixso-paragraph-5629_44076 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_44077 {
    width: 24px;
    height: 20px;
}
.Pixso-symbol-5629_44078 {
    width: 240px;
    height: auto;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 8px 12px 8px 12px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_44079 {
    width: 16px;
    height: 16px;
}
.Pixso-paragraph-5629_44080 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_44081 {
    width: 24px;
    height: 20px;
}
.Pixso-symbol-5629_44082 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 8px 12px 8px 12px;
}
.stroke-wrapper-5629_44082 {
    position: relative;
    width: 240px;
    height: auto;
    display: flex;
}
.stroke-5629_44082 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 2px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5629_44083 {
    width: 16px;
    height: 16px;
}
.Pixso-paragraph-5629_44084 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_44085 {
    width: 24px;
    height: 20px;
}
.Pixso-symbol-5629_44626 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 8px 12px 8px 12px;
}
.stroke-wrapper-5629_44626 {
    position: relative;
    width: 240px;
    height: auto;
    display: flex;
}
.stroke-5629_44626 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 0px 2px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5629_44627 {
    width: 16px;
    height: 16px;
}
.Pixso-paragraph-5629_44628 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_44629 {
    width: 24px;
    height: 20px;
}
.Pixso-symbol-5629_43687 {
    width: auto;
    height: auto;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 8px 12px 8px 12px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_43688 {
    width: 16px;
    height: 16px;
}
.Pixso-paragraph-5629_43689 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_43690 {
    width: 24px;
    height: 20px;
}
.Pixso-paragraph-5588_13118 {
    text-align: center;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    width: auto;
    height: auto;
    flex-grow: 0;
}
.Pixso-symbol-5629_43910 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 8px 12px 8px 12px;
}
.stroke-wrapper-5629_43910 {
    position: relative;
    width: auto;
    height: auto;
    display: flex;
}
.stroke-5629_43910 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 2px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5629_43911 {
    width: 16px;
    height: 16px;
}
.Pixso-paragraph-5629_43912 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_43913 {
    width: 24px;
    height: 20px;
}
.Pixso-symbol-5629_43818 {
    width: auto;
    height: auto;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 8px 12px 8px 12px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_43819 {
    width: 16px;
    height: 16px;
}
.Pixso-paragraph-5629_43820 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_43821 {
    width: 24px;
    height: 20px;
}
.Pixso-symbol-5629_44274 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 8px 12px 8px 12px;
}
.stroke-wrapper-5629_44274 {
    position: relative;
    width: auto;
    height: auto;
    display: flex;
}
.stroke-5629_44274 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 0px 2px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5629_44275 {
    width: 16px;
    height: 16px;
}
.Pixso-paragraph-5629_44276 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_44277 {
    width: 24px;
    height: 20px;
}
.Pixso-symbol-5629_44098 {
    width: 240px;
    height: auto;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 8px 12px 8px 12px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_44099 {
    width: 16px;
    height: 16px;
}
.Pixso-paragraph-5629_44100 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_44101 {
    width: 24px;
    height: 20px;
}
.Pixso-symbol-5629_44106 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 8px 12px 8px 12px;
}
.stroke-wrapper-5629_44106 {
    position: relative;
    width: 240px;
    height: auto;
    display: flex;
}
.stroke-5629_44106 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 2px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5629_44107 {
    width: 16px;
    height: 16px;
}
.Pixso-paragraph-5629_44108 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_44109 {
    width: 24px;
    height: 20px;
}
.Pixso-symbol-5629_44102 {
    width: 240px;
    height: auto;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 8px 12px 8px 12px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_44103 {
    width: 16px;
    height: 16px;
}
.Pixso-paragraph-5629_44104 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_44105 {
    width: 24px;
    height: 20px;
}
.Pixso-symbol-5629_44630 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 8px 12px 8px 12px;
}
.stroke-wrapper-5629_44630 {
    position: relative;
    width: 240px;
    height: auto;
    display: flex;
}
.stroke-5629_44630 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 0px 2px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5629_44631 {
    width: 16px;
    height: 16px;
}
.Pixso-paragraph-5629_44632 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_44633 {
    width: 24px;
    height: 20px;
}
.Pixso-symbol-5629_43914 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 8px 12px 8px 12px;
}
.stroke-wrapper-5629_43914 {
    position: relative;
    width: auto;
    height: auto;
    display: flex;
}
.stroke-5629_43914 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 2px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5629_43915 {
    width: 16px;
    height: 16px;
}
.Pixso-paragraph-5629_43916 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_43917 {
    width: 24px;
    height: 20px;
}
.Pixso-symbol-5629_43710 {
    width: auto;
    height: auto;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 8px 12px 8px 12px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_43711 {
    width: 16px;
    height: 16px;
}
.Pixso-paragraph-5629_43712 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_43713 {
    width: 24px;
    height: 20px;
}
.Pixso-symbol-5629_43822 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 8px 12px 8px 12px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.stroke-wrapper-5629_43822 {
    position: relative;
    width: auto;
    height: auto;
    display: flex;
}
.stroke-5629_43822 {
    position: absolute;
    inset: 0px;
    border-radius: 1234px 1234px 1234px 1234px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5629_43823 {
    width: 16px;
    height: 16px;
}
.Pixso-paragraph-5629_43824 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_43825 {
    width: 24px;
    height: 20px;
}
.Pixso-symbol-5629_44278 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 8px 12px 8px 12px;
}
.stroke-wrapper-5629_44278 {
    position: relative;
    width: auto;
    height: auto;
    display: flex;
}
.stroke-5629_44278 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 0px 2px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5629_44279 {
    width: 16px;
    height: 16px;
}
.Pixso-paragraph-5629_44280 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_44281 {
    width: 24px;
    height: 20px;
}
.Pixso-symbol-5629_44110 {
    width: 240px;
    height: auto;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 8px 12px 8px 12px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_44111 {
    width: 16px;
    height: 16px;
}
.Pixso-paragraph-5629_44112 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_44113 {
    width: 24px;
    height: 20px;
}
.Pixso-symbol-5629_44118 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 8px 12px 8px 12px;
}
.stroke-wrapper-5629_44118 {
    position: relative;
    width: 240px;
    height: auto;
    display: flex;
}
.stroke-5629_44118 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 2px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5629_44119 {
    width: 16px;
    height: 16px;
}
.Pixso-paragraph-5629_44120 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_44121 {
    width: 24px;
    height: 20px;
}
.Pixso-symbol-5629_44114 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 8px 12px 8px 12px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.stroke-wrapper-5629_44114 {
    position: relative;
    width: 240px;
    height: auto;
    display: flex;
}
.stroke-5629_44114 {
    position: absolute;
    inset: 0px;
    border-radius: 1234px 1234px 1234px 1234px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5629_44115 {
    width: 16px;
    height: 16px;
}
.Pixso-paragraph-5629_44116 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_44117 {
    width: 24px;
    height: 20px;
}
.Pixso-symbol-5629_43906 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 8px 12px 8px 12px;
}
.stroke-wrapper-5629_43906 {
    position: relative;
    width: auto;
    height: auto;
    display: flex;
}
.stroke-5629_43906 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 2px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5629_43907 {
    width: 16px;
    height: 16px;
}
.Pixso-paragraph-5629_43908 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_43909 {
    width: 24px;
    height: 20px;
}
.Pixso-paragraph-5588_13937 {
    text-align: center;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    width: auto;
    height: auto;
    flex-grow: 0;
}
.Pixso-symbol-5629_44634 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 8px 12px 8px 12px;
}
.stroke-wrapper-5629_44634 {
    position: relative;
    width: 240px;
    height: auto;
    display: flex;
}
.stroke-5629_44634 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 0px 2px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5629_44635 {
    width: 16px;
    height: 16px;
}
.Pixso-paragraph-5629_44636 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_44637 {
    width: 24px;
    height: 20px;
}
.Pixso-symbol-5629_43749 {
    width: auto;
    height: auto;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 8px 12px 8px 12px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_43750 {
    width: 16px;
    height: 16px;
}
.Pixso-paragraph-5629_43751 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_43752 {
    width: 24px;
    height: 20px;
}
.Pixso-symbol-5629_43814 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 8px 12px 8px 12px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.stroke-wrapper-5629_43814 {
    position: relative;
    width: auto;
    height: auto;
    display: flex;
}
.stroke-5629_43814 {
    position: absolute;
    inset: 0px;
    border-radius: 1234px 1234px 1234px 1234px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5629_43815 {
    width: 16px;
    height: 16px;
}
.Pixso-paragraph-5629_43816 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_43817 {
    width: 24px;
    height: 20px;
}
.Pixso-symbol-5629_44094 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 8px 12px 8px 12px;
}
.stroke-wrapper-5629_44094 {
    position: relative;
    width: 240px;
    height: auto;
    display: flex;
}
.stroke-5629_44094 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 2px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5629_44095 {
    width: 16px;
    height: 16px;
}
.Pixso-paragraph-5629_44096 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_44097 {
    width: 24px;
    height: 20px;
}
.Pixso-symbol-5629_44282 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 8px 12px 8px 12px;
}
.stroke-wrapper-5629_44282 {
    position: relative;
    width: auto;
    height: auto;
    display: flex;
}
.stroke-5629_44282 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 0px 2px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5629_44283 {
    width: 16px;
    height: 16px;
}
.Pixso-paragraph-5629_44284 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_44285 {
    width: 24px;
    height: 20px;
}
.Pixso-symbol-5629_44086 {
    width: 240px;
    height: auto;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 8px 12px 8px 12px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_44087 {
    width: 16px;
    height: 16px;
}
.Pixso-paragraph-5629_44088 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_44089 {
    width: 24px;
    height: 20px;
}
.Pixso-symbol-5629_44090 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 8px 12px 8px 12px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.stroke-wrapper-5629_44090 {
    position: relative;
    width: 240px;
    height: auto;
    display: flex;
}
.stroke-5629_44090 {
    position: absolute;
    inset: 0px;
    border-radius: 1234px 1234px 1234px 1234px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5629_44091 {
    width: 16px;
    height: 16px;
}
.Pixso-paragraph-5629_44092 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_44093 {
    width: 24px;
    height: 20px;
}
.Pixso-symbol-5629_44638 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 8px 12px 8px 12px;
}
.stroke-wrapper-5629_44638 {
    position: relative;
    width: 240px;
    height: auto;
    display: flex;
}
.stroke-5629_44638 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 0px 2px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5629_44639 {
    width: 16px;
    height: 16px;
}
.Pixso-paragraph-5629_44640 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_44641 {
    width: 24px;
    height: 20px;
}
.Pixso-symbol-5558_51587 {
    width: auto;
    height: 40px;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 8px 16px 8px 16px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_41189 {
    width: 20px;
    height: 20px;
}
.Pixso-paragraph-5558_51586 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_41092 {
    width: 28px;
    height: 24px;
}
.Pixso-symbol-5629_41545 {
    width: auto;
    height: 40px;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 8px 16px 8px 16px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_41546 {
    width: 20px;
    height: 20px;
}
.Pixso-paragraph-5629_41547 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_41548 {
    width: 28px;
    height: 24px;
}
.Pixso-symbol-5629_41725 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 8px 16px 8px 16px;
}
.stroke-wrapper-5629_41725 {
    position: relative;
    width: 240px;
    height: 40px;
    display: flex;
}
.stroke-5629_41725 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 2px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5629_41726 {
    width: 20px;
    height: 20px;
}
.Pixso-paragraph-5629_41727 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_41728 {
    width: 28px;
    height: 24px;
}
.Pixso-symbol-5629_41453 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 8px 16px 8px 16px;
}
.stroke-wrapper-5629_41453 {
    position: relative;
    width: auto;
    height: 40px;
    display: flex;
}
.stroke-5629_41453 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 2px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5629_41454 {
    width: 20px;
    height: 20px;
}
.Pixso-paragraph-5629_41455 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_41456 {
    width: 28px;
    height: 24px;
}
.Pixso-symbol-5629_44352 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 8px 16px 8px 16px;
}
.stroke-wrapper-5629_44352 {
    position: relative;
    width: auto;
    height: 40px;
    display: flex;
}
.stroke-5629_44352 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 0px 2px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5629_44353 {
    width: 20px;
    height: 20px;
}
.Pixso-paragraph-5629_44354 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_44355 {
    width: 28px;
    height: 24px;
}
.Pixso-symbol-5629_41717 {
    width: 240px;
    height: 40px;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 8px 16px 8px 16px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_41718 {
    width: 20px;
    height: 20px;
}
.Pixso-paragraph-5629_41719 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_41720 {
    width: 28px;
    height: 24px;
}
.Pixso-symbol-5629_41721 {
    width: 240px;
    height: 40px;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 8px 16px 8px 16px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_41722 {
    width: 20px;
    height: 20px;
}
.Pixso-paragraph-5629_41723 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_41724 {
    width: 28px;
    height: 24px;
}
.Pixso-symbol-5629_44642 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 8px 16px 8px 16px;
}
.stroke-wrapper-5629_44642 {
    position: relative;
    width: 240px;
    height: 40px;
    display: flex;
}
.stroke-5629_44642 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 0px 2px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5629_44643 {
    width: 20px;
    height: 20px;
}
.Pixso-paragraph-5629_44644 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_44645 {
    width: 28px;
    height: 24px;
}
.Pixso-symbol-5629_41223 {
    width: auto;
    height: 40px;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 8px 16px 8px 16px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_41224 {
    width: 20px;
    height: 20px;
}
.Pixso-paragraph-5629_41225 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_41226 {
    width: 28px;
    height: 24px;
}
.Pixso-symbol-5629_41737 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 8px 16px 8px 16px;
}
.stroke-wrapper-5629_41737 {
    position: relative;
    width: 240px;
    height: 40px;
    display: flex;
}
.stroke-5629_41737 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 2px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5629_41738 {
    width: 20px;
    height: 20px;
}
.Pixso-paragraph-5629_41739 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_41740 {
    width: 28px;
    height: 24px;
}
.Pixso-symbol-5629_41549 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 8px 16px 8px 16px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.stroke-wrapper-5629_41549 {
    position: relative;
    width: auto;
    height: 40px;
    display: flex;
}
.stroke-5629_41549 {
    position: absolute;
    inset: 0px;
    border-radius: 1234px 1234px 1234px 1234px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5629_41550 {
    width: 20px;
    height: 20px;
}
.Pixso-paragraph-5629_41551 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_41552 {
    width: 28px;
    height: 24px;
}
.Pixso-symbol-5629_41457 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 8px 16px 8px 16px;
}
.stroke-wrapper-5629_41457 {
    position: relative;
    width: auto;
    height: 40px;
    display: flex;
}
.stroke-5629_41457 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 2px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5629_41458 {
    width: 20px;
    height: 20px;
}
.Pixso-paragraph-5629_41459 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_41460 {
    width: 28px;
    height: 24px;
}
.Pixso-symbol-5629_44356 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 8px 16px 8px 16px;
}
.stroke-wrapper-5629_44356 {
    position: relative;
    width: auto;
    height: 40px;
    display: flex;
}
.stroke-5629_44356 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 0px 2px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5629_44357 {
    width: 20px;
    height: 20px;
}
.Pixso-paragraph-5629_44358 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_44359 {
    width: 28px;
    height: 24px;
}
.Pixso-symbol-5629_41729 {
    width: 240px;
    height: 40px;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 8px 16px 8px 16px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_41730 {
    width: 20px;
    height: 20px;
}
.Pixso-paragraph-5629_41731 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_41732 {
    width: 28px;
    height: 24px;
}
.Pixso-symbol-5629_41733 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 8px 16px 8px 16px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.stroke-wrapper-5629_41733 {
    position: relative;
    width: 240px;
    height: 40px;
    display: flex;
}
.stroke-5629_41733 {
    position: absolute;
    inset: 0px;
    border-radius: 1234px 1234px 1234px 1234px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5629_41734 {
    width: 20px;
    height: 20px;
}
.Pixso-paragraph-5629_41735 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_41736 {
    width: 28px;
    height: 24px;
}
.Pixso-symbol-5629_44646 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 8px 16px 8px 16px;
}
.stroke-wrapper-5629_44646 {
    position: relative;
    width: 240px;
    height: 40px;
    display: flex;
}
.stroke-5629_44646 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 0px 2px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5629_44647 {
    width: 20px;
    height: 20px;
}
.Pixso-paragraph-5629_44648 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_44649 {
    width: 28px;
    height: 24px;
}
.Pixso-symbol-5629_41749 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 8px 16px 8px 16px;
}
.stroke-wrapper-5629_41749 {
    position: relative;
    width: 240px;
    height: 40px;
    display: flex;
}
.stroke-5629_41749 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 2px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5629_41750 {
    width: 20px;
    height: 20px;
}
.Pixso-paragraph-5629_41751 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_41752 {
    width: 28px;
    height: 24px;
}
.Pixso-symbol-5629_41260 {
    width: auto;
    height: 40px;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 8px 16px 8px 16px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_41261 {
    width: 20px;
    height: 20px;
}
.Pixso-paragraph-5629_41262 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_41263 {
    width: 28px;
    height: 24px;
}
.Pixso-symbol-5629_41553 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 8px 16px 8px 16px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.stroke-wrapper-5629_41553 {
    position: relative;
    width: auto;
    height: 40px;
    display: flex;
}
.stroke-5629_41553 {
    position: absolute;
    inset: 0px;
    border-radius: 1234px 1234px 1234px 1234px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5629_41554 {
    width: 20px;
    height: 20px;
}
.Pixso-paragraph-5629_41555 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_41556 {
    width: 28px;
    height: 24px;
}
.Pixso-symbol-5629_41461 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 8px 16px 8px 16px;
}
.stroke-wrapper-5629_41461 {
    position: relative;
    width: auto;
    height: 40px;
    display: flex;
}
.stroke-5629_41461 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 2px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5629_41462 {
    width: 20px;
    height: 20px;
}
.Pixso-paragraph-5629_41463 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_41464 {
    width: 28px;
    height: 24px;
}
.Pixso-symbol-5629_44360 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 8px 16px 8px 16px;
}
.stroke-wrapper-5629_44360 {
    position: relative;
    width: auto;
    height: 40px;
    display: flex;
}
.stroke-5629_44360 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 0px 2px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5629_44361 {
    width: 20px;
    height: 20px;
}
.Pixso-paragraph-5629_44362 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_44363 {
    width: 28px;
    height: 24px;
}
.Pixso-symbol-5629_41741 {
    width: 240px;
    height: 40px;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 8px 16px 8px 16px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_41742 {
    width: 20px;
    height: 20px;
}
.Pixso-paragraph-5629_41743 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_41744 {
    width: 28px;
    height: 24px;
}
.Pixso-symbol-5629_41745 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 8px 16px 8px 16px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.stroke-wrapper-5629_41745 {
    position: relative;
    width: 240px;
    height: 40px;
    display: flex;
}
.stroke-5629_41745 {
    position: absolute;
    inset: 0px;
    border-radius: 1234px 1234px 1234px 1234px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5629_41746 {
    width: 20px;
    height: 20px;
}
.Pixso-paragraph-5629_41747 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_41748 {
    width: 28px;
    height: 24px;
}
.Pixso-symbol-5629_41761 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 8px 16px 8px 16px;
}
.stroke-wrapper-5629_41761 {
    position: relative;
    width: 240px;
    height: 40px;
    display: flex;
}
.stroke-5629_41761 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 2px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5629_41762 {
    width: 20px;
    height: 20px;
}
.Pixso-paragraph-5629_41763 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_41764 {
    width: 28px;
    height: 24px;
}
.Pixso-symbol-5629_44650 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 8px 16px 8px 16px;
}
.stroke-wrapper-5629_44650 {
    position: relative;
    width: 240px;
    height: 40px;
    display: flex;
}
.stroke-5629_44650 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 0px 2px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5629_44651 {
    width: 20px;
    height: 20px;
}
.Pixso-paragraph-5629_44652 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_44653 {
    width: 28px;
    height: 24px;
}
.Pixso-symbol-5629_41299 {
    width: auto;
    height: 40px;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 8px 16px 8px 16px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_41300 {
    width: 20px;
    height: 20px;
}
.Pixso-paragraph-5629_41301 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_41302 {
    width: 28px;
    height: 24px;
}
.Pixso-symbol-5629_41557 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 8px 16px 8px 16px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.stroke-wrapper-5629_41557 {
    position: relative;
    width: auto;
    height: 40px;
    display: flex;
}
.stroke-5629_41557 {
    position: absolute;
    inset: 0px;
    border-radius: 1234px 1234px 1234px 1234px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5629_41558 {
    width: 20px;
    height: 20px;
}
.Pixso-paragraph-5629_41559 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_41560 {
    width: 28px;
    height: 24px;
}
.Pixso-symbol-5629_41465 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 8px 16px 8px 16px;
}
.stroke-wrapper-5629_41465 {
    position: relative;
    width: auto;
    height: 40px;
    display: flex;
}
.stroke-5629_41465 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 2px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5629_41466 {
    width: 20px;
    height: 20px;
}
.Pixso-paragraph-5629_41467 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_41468 {
    width: 28px;
    height: 24px;
}
.Pixso-symbol-5629_44401 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 8px 16px 8px 16px;
}
.stroke-wrapper-5629_44401 {
    position: relative;
    width: auto;
    height: 40px;
    display: flex;
}
.stroke-5629_44401 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 0px 2px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5629_44402 {
    width: 20px;
    height: 20px;
}
.Pixso-paragraph-5629_44403 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_44404 {
    width: 28px;
    height: 24px;
}
.Pixso-symbol-5629_41753 {
    width: 240px;
    height: 40px;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 8px 16px 8px 16px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_41754 {
    width: 20px;
    height: 20px;
}
.Pixso-paragraph-5629_41755 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_41756 {
    width: 28px;
    height: 24px;
}
.Pixso-symbol-5629_42871 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 10px;
    justify-content: center;
    align-items: center;
    padding: 12px 16px 12px 16px;
    min-height: 48px;
}
.stroke-wrapper-5629_42871 {
    position: relative;
    width: 240px;
    height: auto;
    display: flex;
}
.stroke-5629_42871 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 2px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5629_42872 {
    width: 20px;
    height: 20px;
}
.Pixso-paragraph-5629_42873 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_42874 {
    width: 28px;
    height: 24px;
}
.Pixso-symbol-5629_41757 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 8px 16px 8px 16px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.stroke-wrapper-5629_41757 {
    position: relative;
    width: 240px;
    height: 40px;
    display: flex;
}
.stroke-5629_41757 {
    position: absolute;
    inset: 0px;
    border-radius: 1234px 1234px 1234px 1234px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5629_41758 {
    width: 20px;
    height: 20px;
}
.Pixso-paragraph-5629_41759 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_41760 {
    width: 28px;
    height: 24px;
}
.Pixso-symbol-5629_44654 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 8px 16px 8px 16px;
}
.stroke-wrapper-5629_44654 {
    position: relative;
    width: 240px;
    height: 40px;
    display: flex;
}
.stroke-5629_44654 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 0px 2px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5629_44655 {
    width: 20px;
    height: 20px;
}
.Pixso-paragraph-5629_44656 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_44657 {
    width: 28px;
    height: 24px;
}
.Pixso-symbol-5629_42113 {
    width: auto;
    height: auto;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 10px;
    justify-content: center;
    align-items: center;
    padding: 12px 16px 12px 16px;
    min-height: 48px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_42114 {
    width: 20px;
    height: 20px;
}
.Pixso-paragraph-5629_42115 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_42116 {
    width: 28px;
    height: 24px;
}
.Pixso-symbol-5629_42599 {
    width: auto;
    height: auto;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 10px;
    justify-content: center;
    align-items: center;
    padding: 12px 16px 12px 16px;
    min-height: 48px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_42600 {
    width: 20px;
    height: 20px;
}
.Pixso-paragraph-5629_42601 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_42602 {
    width: 28px;
    height: 24px;
}
.Pixso-symbol-5629_42691 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 10px;
    justify-content: center;
    align-items: center;
    padding: 12px 16px 12px 16px;
    min-height: 48px;
}
.stroke-wrapper-5629_42691 {
    position: relative;
    width: auto;
    height: auto;
    display: flex;
}
.stroke-5629_42691 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 2px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5629_42692 {
    width: 20px;
    height: 20px;
}
.Pixso-paragraph-5629_42693 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_42694 {
    width: 28px;
    height: 24px;
}
.Pixso-symbol-5629_44454 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 10px;
    justify-content: center;
    align-items: center;
    padding: 12px 16px 12px 16px;
    min-height: 48px;
}
.stroke-wrapper-5629_44454 {
    position: relative;
    width: auto;
    height: auto;
    display: flex;
}
.stroke-5629_44454 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 0px 2px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5629_44455 {
    width: 20px;
    height: 20px;
}
.Pixso-paragraph-5629_44456 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_44457 {
    width: 28px;
    height: 24px;
}
.Pixso-symbol-5629_42899 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 10px;
    justify-content: center;
    align-items: center;
    padding: 12px 16px 12px 16px;
    min-height: 48px;
}
.stroke-wrapper-5629_42899 {
    position: relative;
    width: 240px;
    height: auto;
    display: flex;
}
.stroke-5629_42899 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 2px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5629_42900 {
    width: 20px;
    height: 20px;
}
.Pixso-paragraph-5629_42901 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_42902 {
    width: 28px;
    height: 24px;
}
.Pixso-symbol-5629_42863 {
    width: 240px;
    height: auto;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 10px;
    justify-content: center;
    align-items: center;
    padding: 12px 16px 12px 16px;
    min-height: 48px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_42864 {
    width: 20px;
    height: 20px;
}
.Pixso-paragraph-5629_42865 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_42866 {
    width: 28px;
    height: 24px;
}
.Pixso-symbol-5629_42867 {
    width: 240px;
    height: auto;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 10px;
    justify-content: center;
    align-items: center;
    padding: 12px 16px 12px 16px;
    min-height: 48px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_42868 {
    width: 20px;
    height: 20px;
}
.Pixso-paragraph-5629_42869 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_42870 {
    width: 28px;
    height: 24px;
}
.Pixso-symbol-5629_44658 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 10px;
    justify-content: center;
    align-items: center;
    padding: 12px 16px 12px 16px;
    min-height: 48px;
}
.stroke-wrapper-5629_44658 {
    position: relative;
    width: 240px;
    height: auto;
    display: flex;
}
.stroke-5629_44658 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 0px 2px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5629_44659 {
    width: 20px;
    height: 20px;
}
.Pixso-paragraph-5629_44660 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_44661 {
    width: 28px;
    height: 24px;
}
.Pixso-symbol-5629_42468 {
    width: auto;
    height: auto;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 10px;
    justify-content: center;
    align-items: center;
    padding: 12px 16px 12px 16px;
    min-height: 48px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_42469 {
    width: 20px;
    height: 20px;
}
.Pixso-paragraph-5629_42470 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_42471 {
    width: 28px;
    height: 24px;
}
.Pixso-symbol-5629_42699 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 10px;
    justify-content: center;
    align-items: center;
    padding: 12px 16px 12px 16px;
    min-height: 48px;
}
.stroke-wrapper-5629_42699 {
    position: relative;
    width: auto;
    height: auto;
    display: flex;
}
.stroke-5629_42699 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 2px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5629_42700 {
    width: 20px;
    height: 20px;
}
.Pixso-paragraph-5629_42701 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_42702 {
    width: 28px;
    height: 24px;
}
.Pixso-symbol-5629_42607 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 10px;
    justify-content: center;
    align-items: center;
    padding: 12px 16px 12px 16px;
    min-height: 48px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.stroke-wrapper-5629_42607 {
    position: relative;
    width: auto;
    height: auto;
    display: flex;
}
.stroke-5629_42607 {
    position: absolute;
    inset: 0px;
    border-radius: 1234px 1234px 1234px 1234px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5629_42608 {
    width: 20px;
    height: 20px;
}
.Pixso-paragraph-5629_42609 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_42610 {
    width: 28px;
    height: 24px;
}
.Pixso-symbol-5629_44458 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 10px;
    justify-content: center;
    align-items: center;
    padding: 12px 16px 12px 16px;
    min-height: 48px;
}
.stroke-wrapper-5629_44458 {
    position: relative;
    width: auto;
    height: auto;
    display: flex;
}
.stroke-5629_44458 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 0px 2px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5629_44459 {
    width: 20px;
    height: 20px;
}
.Pixso-paragraph-5629_44460 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_44461 {
    width: 28px;
    height: 24px;
}
.Pixso-symbol-5629_42907 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 10px;
    justify-content: center;
    align-items: center;
    padding: 12px 16px 12px 16px;
    min-height: 48px;
}
.stroke-wrapper-5629_42907 {
    position: relative;
    width: 240px;
    height: auto;
    display: flex;
}
.stroke-5629_42907 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 2px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5629_42908 {
    width: 20px;
    height: 20px;
}
.Pixso-paragraph-5629_42909 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_42910 {
    width: 28px;
    height: 24px;
}
.Pixso-symbol-5629_42895 {
    width: 240px;
    height: auto;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 10px;
    justify-content: center;
    align-items: center;
    padding: 12px 16px 12px 16px;
    min-height: 48px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_42896 {
    width: 20px;
    height: 20px;
}
.Pixso-paragraph-5629_42897 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_42898 {
    width: 28px;
    height: 24px;
}
.Pixso-symbol-5629_42883 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 10px;
    justify-content: center;
    align-items: center;
    padding: 12px 16px 12px 16px;
    min-height: 48px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.stroke-wrapper-5629_42883 {
    position: relative;
    width: 240px;
    height: auto;
    display: flex;
}
.stroke-5629_42883 {
    position: absolute;
    inset: 0px;
    border-radius: 1234px 1234px 1234px 1234px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5629_42884 {
    width: 20px;
    height: 20px;
}
.Pixso-paragraph-5629_42885 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_42886 {
    width: 28px;
    height: 24px;
}
.Pixso-symbol-5629_44662 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 10px;
    justify-content: center;
    align-items: center;
    padding: 12px 16px 12px 16px;
    min-height: 48px;
}
.stroke-wrapper-5629_44662 {
    position: relative;
    width: 240px;
    height: auto;
    display: flex;
}
.stroke-5629_44662 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 0px 2px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5629_44663 {
    width: 20px;
    height: 20px;
}
.Pixso-paragraph-5629_44664 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_44665 {
    width: 28px;
    height: 24px;
}
.Pixso-symbol-5629_42703 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 10px;
    justify-content: center;
    align-items: center;
    padding: 12px 16px 12px 16px;
    min-height: 48px;
}
.stroke-wrapper-5629_42703 {
    position: relative;
    width: auto;
    height: auto;
    display: flex;
}
.stroke-5629_42703 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 2px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5629_42704 {
    width: 20px;
    height: 20px;
}
.Pixso-paragraph-5629_42705 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_42706 {
    width: 28px;
    height: 24px;
}
.Pixso-symbol-5629_42499 {
    width: auto;
    height: auto;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 10px;
    justify-content: center;
    align-items: center;
    padding: 12px 16px 12px 16px;
    min-height: 48px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_42500 {
    width: 20px;
    height: 20px;
}
.Pixso-paragraph-5629_42501 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_42502 {
    width: 28px;
    height: 24px;
}
.Pixso-symbol-5629_42887 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 10px;
    justify-content: center;
    align-items: center;
    padding: 12px 16px 12px 16px;
    min-height: 48px;
}
.stroke-wrapper-5629_42887 {
    position: relative;
    width: 240px;
    height: auto;
    display: flex;
}
.stroke-5629_42887 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 2px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5629_42888 {
    width: 20px;
    height: 20px;
}
.Pixso-paragraph-5629_42889 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_42890 {
    width: 28px;
    height: 24px;
}
.Pixso-symbol-5629_42611 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 10px;
    justify-content: center;
    align-items: center;
    padding: 12px 16px 12px 16px;
    min-height: 48px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.stroke-wrapper-5629_42611 {
    position: relative;
    width: auto;
    height: auto;
    display: flex;
}
.stroke-5629_42611 {
    position: absolute;
    inset: 0px;
    border-radius: 1234px 1234px 1234px 1234px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5629_42612 {
    width: 20px;
    height: 20px;
}
.Pixso-paragraph-5629_42613 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_42614 {
    width: 28px;
    height: 24px;
}
.Pixso-symbol-5629_44462 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 10px;
    justify-content: center;
    align-items: center;
    padding: 12px 16px 12px 16px;
    min-height: 48px;
}
.stroke-wrapper-5629_44462 {
    position: relative;
    width: auto;
    height: auto;
    display: flex;
}
.stroke-5629_44462 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 0px 2px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5629_44463 {
    width: 20px;
    height: 20px;
}
.Pixso-paragraph-5629_44464 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_44465 {
    width: 28px;
    height: 24px;
}
.Pixso-symbol-5629_42903 {
    width: 240px;
    height: auto;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 10px;
    justify-content: center;
    align-items: center;
    padding: 12px 16px 12px 16px;
    min-height: 48px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_42904 {
    width: 20px;
    height: 20px;
}
.Pixso-paragraph-5629_42905 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_42906 {
    width: 28px;
    height: 24px;
}
.Pixso-symbol-5629_42891 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 10px;
    justify-content: center;
    align-items: center;
    padding: 12px 16px 12px 16px;
    min-height: 48px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.stroke-wrapper-5629_42891 {
    position: relative;
    width: 240px;
    height: auto;
    display: flex;
}
.stroke-5629_42891 {
    position: absolute;
    inset: 0px;
    border-radius: 1234px 1234px 1234px 1234px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5629_42892 {
    width: 20px;
    height: 20px;
}
.Pixso-paragraph-5629_42893 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_42894 {
    width: 28px;
    height: 24px;
}
.Pixso-symbol-5629_42695 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 10px;
    justify-content: center;
    align-items: center;
    padding: 12px 16px 12px 16px;
    min-height: 48px;
}
.stroke-wrapper-5629_42695 {
    position: relative;
    width: auto;
    height: auto;
    display: flex;
}
.stroke-5629_42695 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 2px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5629_42696 {
    width: 20px;
    height: 20px;
}
.Pixso-paragraph-5629_42697 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_42698 {
    width: 28px;
    height: 24px;
}
.Pixso-symbol-5629_44666 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 10px;
    justify-content: center;
    align-items: center;
    padding: 12px 16px 12px 16px;
    min-height: 48px;
}
.stroke-wrapper-5629_44666 {
    position: relative;
    width: 240px;
    height: auto;
    display: flex;
}
.stroke-5629_44666 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 0px 2px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5629_44667 {
    width: 20px;
    height: 20px;
}
.Pixso-paragraph-5629_44668 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_44669 {
    width: 28px;
    height: 24px;
}
.Pixso-symbol-5629_42538 {
    width: auto;
    height: auto;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 10px;
    justify-content: center;
    align-items: center;
    padding: 12px 16px 12px 16px;
    min-height: 48px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_42539 {
    width: 20px;
    height: 20px;
}
.Pixso-paragraph-5629_42540 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_42541 {
    width: 28px;
    height: 24px;
}
.Pixso-symbol-5629_42603 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 10px;
    justify-content: center;
    align-items: center;
    padding: 12px 16px 12px 16px;
    min-height: 48px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.stroke-wrapper-5629_42603 {
    position: relative;
    width: auto;
    height: auto;
    display: flex;
}
.stroke-5629_42603 {
    position: absolute;
    inset: 0px;
    border-radius: 1234px 1234px 1234px 1234px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5629_42604 {
    width: 20px;
    height: 20px;
}
.Pixso-paragraph-5629_42605 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_42606 {
    width: 28px;
    height: 24px;
}
.Pixso-symbol-5629_44466 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 10px;
    justify-content: center;
    align-items: center;
    padding: 12px 16px 12px 16px;
    min-height: 48px;
}
.stroke-wrapper-5629_44466 {
    position: relative;
    width: auto;
    height: auto;
    display: flex;
}
.stroke-5629_44466 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 0px 2px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5629_44467 {
    width: 20px;
    height: 20px;
}
.Pixso-paragraph-5629_44468 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_44469 {
    width: 28px;
    height: 24px;
}
.Pixso-symbol-5629_42879 {
    width: 240px;
    height: auto;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 10px;
    justify-content: center;
    align-items: center;
    padding: 12px 16px 12px 16px;
    min-height: 48px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_42880 {
    width: 20px;
    height: 20px;
}
.Pixso-paragraph-5629_42881 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_42882 {
    width: 28px;
    height: 24px;
}
.Pixso-symbol-5629_42875 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 10px;
    justify-content: center;
    align-items: center;
    padding: 12px 16px 12px 16px;
    min-height: 48px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.stroke-wrapper-5629_42875 {
    position: relative;
    width: 240px;
    height: auto;
    display: flex;
}
.stroke-5629_42875 {
    position: absolute;
    inset: 0px;
    border-radius: 1234px 1234px 1234px 1234px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5629_42876 {
    width: 20px;
    height: 20px;
}
.Pixso-paragraph-5629_42877 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_42878 {
    width: 28px;
    height: 24px;
}
.Pixso-symbol-5629_44670 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 10px;
    justify-content: center;
    align-items: center;
    padding: 12px 16px 12px 16px;
    min-height: 48px;
}
.stroke-wrapper-5629_44670 {
    position: relative;
    width: 240px;
    height: auto;
    display: flex;
}
.stroke-5629_44670 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 0px 2px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5629_44671 {
    width: 20px;
    height: 20px;
}
.Pixso-paragraph-5629_44672 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_44673 {
    width: 28px;
    height: 24px;
}

.Pixso-instance-5629_43320 .Pixso-symbol-5579_152455 .Pixso-symbol-5578_150578 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 10px;
    background-color: transparent;
}
.Pixso-instance-5629_43320 .Pixso-vector-5579_152456 {
    width: 84.37%;
    height: 81.39%;
    position: absolute;
    left: 7.74%;
    right: 7.89%;
    top: 7.8%;
    bottom: 10.81%;
}
.Pixso-instance-5629_43320 .Pixso-symbol-5579_152455 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5629_43322 .Pixso-symbol-5588_11358 {
    width: 24px;
    height: 20px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
    padding: 4px 8px 4px 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_43322 .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_43322 .Pixso-frame-5588_11360 {
    width: 12px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_43322 .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_43322 .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_43322 .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_43811 .Pixso-symbol-5579_152455 .Pixso-symbol-5578_150578 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 10px;
    background-color: transparent;
}
.Pixso-instance-5629_43811 .Pixso-vector-5579_152456 {
    width: 84.37%;
    height: 81.39%;
    position: absolute;
    left: 7.74%;
    right: 7.89%;
    top: 7.8%;
    bottom: 10.81%;
}
.Pixso-instance-5629_43811 .Pixso-symbol-5579_152455 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5629_43813 .Pixso-symbol-5588_11358 {
    width: 24px;
    height: 20px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
    padding: 4px 8px 4px 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_43813 .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_43813 .Pixso-frame-5588_11360 {
    width: 12px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_43813 .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_43813 .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_43813 .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_43903 .Pixso-symbol-5579_152455 .Pixso-symbol-5578_150578 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 10px;
    background-color: transparent;
}
.Pixso-instance-5629_43903 .Pixso-vector-5579_152456 {
    width: 84.37%;
    height: 81.39%;
    position: absolute;
    left: 7.74%;
    right: 7.89%;
    top: 7.8%;
    bottom: 10.81%;
}
.Pixso-instance-5629_43903 .Pixso-symbol-5579_152455 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5629_43905 .Pixso-symbol-5588_11358 {
    width: 24px;
    height: 20px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
    padding: 4px 8px 4px 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_43905 .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_43905 .Pixso-frame-5588_11360 {
    width: 12px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_43905 .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_43905 .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_43905 .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_44271 .Pixso-symbol-5579_152455 .Pixso-symbol-5578_150578 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 10px;
    background-color: transparent;
}
.Pixso-instance-5629_44271 .Pixso-vector-5579_152456 {
    width: 84.37%;
    height: 81.39%;
    position: absolute;
    left: 7.74%;
    right: 7.89%;
    top: 7.8%;
    bottom: 10.81%;
}
.Pixso-instance-5629_44271 .Pixso-symbol-5579_152455 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5629_44273 .Pixso-symbol-5588_11358 {
    width: 24px;
    height: 20px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
    padding: 4px 8px 4px 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_44273 .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_44273 .Pixso-frame-5588_11360 {
    width: 12px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_44273 .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_44273 .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_44273 .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_44075 .Pixso-symbol-5579_152455 .Pixso-symbol-5578_150578 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 64.5px;
    top: 10px;
    background-color: transparent;
}
.Pixso-instance-5629_44075 .Pixso-vector-5579_152456 {
    width: 84.37%;
    height: 81.39%;
    position: absolute;
    left: 7.74%;
    right: 7.89%;
    top: 7.8%;
    bottom: 10.81%;
}
.Pixso-instance-5629_44075 .Pixso-symbol-5579_152455 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5629_44077 .Pixso-symbol-5588_11358 {
    width: 24px;
    height: 20px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
    padding: 4px 8px 4px 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_44077 .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_44077 .Pixso-frame-5588_11360 {
    width: 12px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_44077 .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_44077 .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_44077 .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_44079 .Pixso-symbol-5579_152455 .Pixso-symbol-5578_150578 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 64.5px;
    top: 10px;
    background-color: transparent;
}
.Pixso-instance-5629_44079 .Pixso-vector-5579_152456 {
    width: 84.37%;
    height: 81.39%;
    position: absolute;
    left: 7.74%;
    right: 7.89%;
    top: 7.8%;
    bottom: 10.81%;
}
.Pixso-instance-5629_44079 .Pixso-symbol-5579_152455 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5629_44081 .Pixso-symbol-5588_11358 {
    width: 24px;
    height: 20px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
    padding: 4px 8px 4px 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_44081 .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_44081 .Pixso-frame-5588_11360 {
    width: 12px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_44081 .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_44081 .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_44081 .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_44083 .Pixso-symbol-5579_152455 .Pixso-symbol-5578_150578 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 64.5px;
    top: 10px;
    background-color: transparent;
}
.Pixso-instance-5629_44083 .Pixso-vector-5579_152456 {
    width: 84.37%;
    height: 81.39%;
    position: absolute;
    left: 7.74%;
    right: 7.89%;
    top: 7.8%;
    bottom: 10.81%;
}
.Pixso-instance-5629_44083 .Pixso-symbol-5579_152455 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5629_44085 .Pixso-symbol-5588_11358 {
    width: 24px;
    height: 20px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
    padding: 4px 8px 4px 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_44085 .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_44085 .Pixso-frame-5588_11360 {
    width: 12px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_44085 .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_44085 .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_44085 .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_44627 .Pixso-symbol-5579_152455 .Pixso-symbol-5578_150578 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 64.5px;
    top: 10px;
    background-color: transparent;
}
.Pixso-instance-5629_44627 .Pixso-vector-5579_152456 {
    width: 84.37%;
    height: 81.39%;
    position: absolute;
    left: 7.74%;
    right: 7.89%;
    top: 7.8%;
    bottom: 10.81%;
}
.Pixso-instance-5629_44627 .Pixso-symbol-5579_152455 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5629_44629 .Pixso-symbol-5588_11358 {
    width: 24px;
    height: 20px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
    padding: 4px 8px 4px 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_44629 .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_44629 .Pixso-frame-5588_11360 {
    width: 12px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_44629 .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_44629 .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_44629 .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_43688 .Pixso-symbol-5579_152455 .Pixso-symbol-5578_150578 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 10px;
    background-color: transparent;
}
.Pixso-instance-5629_43688 .Pixso-vector-5579_152456 {
    width: 84.37%;
    height: 81.39%;
    position: absolute;
    left: 7.74%;
    right: 7.89%;
    top: 7.8%;
    bottom: 10.81%;
}
.Pixso-instance-5629_43688 .Pixso-symbol-5579_152455 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5629_43690 .Pixso-symbol-5588_13114 {
    width: 24px;
    height: 20px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
    padding: 4px 8px 4px 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_43690 .Pixso-instance-5588_13115 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_43690 .Pixso-frame-5588_13116 {
    width: 12px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_43690 .Pixso-instance-5588_13117 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_43690 .Pixso-paragraph-5588_13118 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_43690 .Pixso-instance-5588_13119 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_43911 .Pixso-symbol-5579_152455 .Pixso-symbol-5578_150578 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 10px;
    background-color: transparent;
}
.Pixso-instance-5629_43911 .Pixso-vector-5579_152456 {
    width: 84.37%;
    height: 81.39%;
    position: absolute;
    left: 7.74%;
    right: 7.89%;
    top: 7.8%;
    bottom: 10.81%;
}
.Pixso-instance-5629_43911 .Pixso-symbol-5579_152455 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5629_43913 .Pixso-symbol-5588_13114 {
    width: 24px;
    height: 20px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
    padding: 4px 8px 4px 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_43913 .Pixso-instance-5588_13115 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_43913 .Pixso-frame-5588_13116 {
    width: 12px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_43913 .Pixso-instance-5588_13117 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_43913 .Pixso-paragraph-5588_13118 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_43913 .Pixso-instance-5588_13119 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_43819 .Pixso-symbol-5579_152455 .Pixso-symbol-5578_150578 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 10px;
    background-color: transparent;
}
.Pixso-instance-5629_43819 .Pixso-vector-5579_152456 {
    width: 84.37%;
    height: 81.39%;
    position: absolute;
    left: 7.74%;
    right: 7.89%;
    top: 7.8%;
    bottom: 10.81%;
}
.Pixso-instance-5629_43819 .Pixso-symbol-5579_152455 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5629_43821 .Pixso-symbol-5588_13114 {
    width: 24px;
    height: 20px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
    padding: 4px 8px 4px 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_43821 .Pixso-instance-5588_13115 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_43821 .Pixso-frame-5588_13116 {
    width: 12px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_43821 .Pixso-instance-5588_13117 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_43821 .Pixso-paragraph-5588_13118 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_43821 .Pixso-instance-5588_13119 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_44275 .Pixso-symbol-5579_152455 .Pixso-symbol-5578_150578 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 10px;
    background-color: transparent;
}
.Pixso-instance-5629_44275 .Pixso-vector-5579_152456 {
    width: 84.37%;
    height: 81.39%;
    position: absolute;
    left: 7.74%;
    right: 7.89%;
    top: 7.8%;
    bottom: 10.81%;
}
.Pixso-instance-5629_44275 .Pixso-symbol-5579_152455 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5629_44277 .Pixso-symbol-5588_13114 {
    width: 24px;
    height: 20px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
    padding: 4px 8px 4px 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_44277 .Pixso-instance-5588_13115 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_44277 .Pixso-frame-5588_13116 {
    width: 12px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_44277 .Pixso-instance-5588_13117 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_44277 .Pixso-paragraph-5588_13118 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_44277 .Pixso-instance-5588_13119 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_44099 .Pixso-symbol-5579_152455 .Pixso-symbol-5578_150578 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 64.5px;
    top: 10px;
    background-color: transparent;
}
.Pixso-instance-5629_44099 .Pixso-vector-5579_152456 {
    width: 84.37%;
    height: 81.39%;
    position: absolute;
    left: 7.74%;
    right: 7.89%;
    top: 7.8%;
    bottom: 10.81%;
}
.Pixso-instance-5629_44099 .Pixso-symbol-5579_152455 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5629_44101 .Pixso-symbol-5588_13114 {
    width: 24px;
    height: 20px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
    padding: 4px 8px 4px 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_44101 .Pixso-instance-5588_13115 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_44101 .Pixso-frame-5588_13116 {
    width: 12px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_44101 .Pixso-instance-5588_13117 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_44101 .Pixso-paragraph-5588_13118 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_44101 .Pixso-instance-5588_13119 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_44107 .Pixso-symbol-5579_152455 .Pixso-symbol-5578_150578 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 64.5px;
    top: 10px;
    background-color: transparent;
}
.Pixso-instance-5629_44107 .Pixso-vector-5579_152456 {
    width: 84.37%;
    height: 81.39%;
    position: absolute;
    left: 7.74%;
    right: 7.89%;
    top: 7.8%;
    bottom: 10.81%;
}
.Pixso-instance-5629_44107 .Pixso-symbol-5579_152455 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5629_44109 .Pixso-symbol-5588_13114 {
    width: 24px;
    height: 20px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
    padding: 4px 8px 4px 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_44109 .Pixso-instance-5588_13115 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_44109 .Pixso-frame-5588_13116 {
    width: 12px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_44109 .Pixso-instance-5588_13117 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_44109 .Pixso-paragraph-5588_13118 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_44109 .Pixso-instance-5588_13119 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_44103 .Pixso-symbol-5579_152455 .Pixso-symbol-5578_150578 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 64.5px;
    top: 10px;
    background-color: transparent;
}
.Pixso-instance-5629_44103 .Pixso-vector-5579_152456 {
    width: 84.37%;
    height: 81.39%;
    position: absolute;
    left: 7.74%;
    right: 7.89%;
    top: 7.8%;
    bottom: 10.81%;
}
.Pixso-instance-5629_44103 .Pixso-symbol-5579_152455 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5629_44105 .Pixso-symbol-5588_13114 {
    width: 24px;
    height: 20px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
    padding: 4px 8px 4px 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_44105 .Pixso-instance-5588_13115 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_44105 .Pixso-frame-5588_13116 {
    width: 12px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_44105 .Pixso-instance-5588_13117 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_44105 .Pixso-paragraph-5588_13118 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_44105 .Pixso-instance-5588_13119 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_44631 .Pixso-symbol-5579_152455 .Pixso-symbol-5578_150578 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 64.5px;
    top: 10px;
    background-color: transparent;
}
.Pixso-instance-5629_44631 .Pixso-vector-5579_152456 {
    width: 84.37%;
    height: 81.39%;
    position: absolute;
    left: 7.74%;
    right: 7.89%;
    top: 7.8%;
    bottom: 10.81%;
}
.Pixso-instance-5629_44631 .Pixso-symbol-5579_152455 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5629_44633 .Pixso-symbol-5588_13114 {
    width: 24px;
    height: 20px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
    padding: 4px 8px 4px 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_44633 .Pixso-instance-5588_13115 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_44633 .Pixso-frame-5588_13116 {
    width: 12px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_44633 .Pixso-instance-5588_13117 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_44633 .Pixso-paragraph-5588_13118 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_44633 .Pixso-instance-5588_13119 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_43915 .Pixso-symbol-5579_152455 .Pixso-symbol-5578_150578 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 10px;
    background-color: transparent;
}
.Pixso-instance-5629_43915 .Pixso-vector-5579_152456 {
    width: 84.37%;
    height: 81.39%;
    position: absolute;
    left: 7.74%;
    right: 7.89%;
    top: 7.8%;
    bottom: 10.81%;
}
.Pixso-instance-5629_43915 .Pixso-symbol-5579_152455 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5629_43917 .Pixso-symbol-5588_11358 {
    width: 24px;
    height: 20px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
    padding: 4px 8px 4px 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_43917 .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_43917 .Pixso-frame-5588_11360 {
    width: 12px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_43917 .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_43917 .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_43917 .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_43711 .Pixso-symbol-5579_152455 .Pixso-symbol-5578_150578 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 10px;
    background-color: transparent;
}
.Pixso-instance-5629_43711 .Pixso-vector-5579_152456 {
    width: 84.37%;
    height: 81.39%;
    position: absolute;
    left: 7.74%;
    right: 7.89%;
    top: 7.8%;
    bottom: 10.81%;
}
.Pixso-instance-5629_43711 .Pixso-symbol-5579_152455 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5629_43713 .Pixso-symbol-5588_11358 {
    width: 24px;
    height: 20px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
    padding: 4px 8px 4px 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_43713 .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_43713 .Pixso-frame-5588_11360 {
    width: 12px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_43713 .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_43713 .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_43713 .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_43823 .Pixso-symbol-5579_152455 .Pixso-symbol-5578_150578 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 10px;
    background-color: transparent;
}
.Pixso-instance-5629_43823 .Pixso-vector-5579_152456 {
    width: 84.37%;
    height: 81.39%;
    position: absolute;
    left: 7.74%;
    right: 7.89%;
    top: 7.8%;
    bottom: 10.81%;
}
.Pixso-instance-5629_43823 .Pixso-symbol-5579_152455 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5629_43825 .Pixso-symbol-5588_11358 {
    width: 24px;
    height: 20px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
    padding: 4px 8px 4px 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_43825 .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_43825 .Pixso-frame-5588_11360 {
    width: 12px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_43825 .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_43825 .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_43825 .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_44279 .Pixso-symbol-5579_152455 .Pixso-symbol-5578_150578 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 10px;
    background-color: transparent;
}
.Pixso-instance-5629_44279 .Pixso-vector-5579_152456 {
    width: 84.37%;
    height: 81.39%;
    position: absolute;
    left: 7.74%;
    right: 7.89%;
    top: 7.8%;
    bottom: 10.81%;
}
.Pixso-instance-5629_44279 .Pixso-symbol-5579_152455 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5629_44281 .Pixso-symbol-5588_11358 {
    width: 24px;
    height: 20px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
    padding: 4px 8px 4px 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_44281 .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_44281 .Pixso-frame-5588_11360 {
    width: 12px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_44281 .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_44281 .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_44281 .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_44111 .Pixso-symbol-5579_152455 .Pixso-symbol-5578_150578 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 64.5px;
    top: 10px;
    background-color: transparent;
}
.Pixso-instance-5629_44111 .Pixso-vector-5579_152456 {
    width: 84.37%;
    height: 81.39%;
    position: absolute;
    left: 7.74%;
    right: 7.89%;
    top: 7.8%;
    bottom: 10.81%;
}
.Pixso-instance-5629_44111 .Pixso-symbol-5579_152455 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5629_44113 .Pixso-symbol-5588_11358 {
    width: 24px;
    height: 20px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
    padding: 4px 8px 4px 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_44113 .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_44113 .Pixso-frame-5588_11360 {
    width: 12px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_44113 .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_44113 .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_44113 .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_44119 .Pixso-symbol-5579_152455 .Pixso-symbol-5578_150578 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 64.5px;
    top: 10px;
    background-color: transparent;
}
.Pixso-instance-5629_44119 .Pixso-vector-5579_152456 {
    width: 84.37%;
    height: 81.39%;
    position: absolute;
    left: 7.74%;
    right: 7.89%;
    top: 7.8%;
    bottom: 10.81%;
}
.Pixso-instance-5629_44119 .Pixso-symbol-5579_152455 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5629_44121 .Pixso-symbol-5588_11358 {
    width: 24px;
    height: 20px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
    padding: 4px 8px 4px 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_44121 .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_44121 .Pixso-frame-5588_11360 {
    width: 12px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_44121 .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_44121 .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_44121 .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_44115 .Pixso-symbol-5579_152455 .Pixso-symbol-5578_150578 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 64.5px;
    top: 10px;
    background-color: transparent;
}
.Pixso-instance-5629_44115 .Pixso-vector-5579_152456 {
    width: 84.37%;
    height: 81.39%;
    position: absolute;
    left: 7.74%;
    right: 7.89%;
    top: 7.8%;
    bottom: 10.81%;
}
.Pixso-instance-5629_44115 .Pixso-symbol-5579_152455 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5629_44117 .Pixso-symbol-5588_11358 {
    width: 24px;
    height: 20px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
    padding: 4px 8px 4px 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_44117 .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_44117 .Pixso-frame-5588_11360 {
    width: 12px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_44117 .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_44117 .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_44117 .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_43907 .Pixso-symbol-5579_152455 .Pixso-symbol-5578_150578 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 10px;
    background-color: transparent;
}
.Pixso-instance-5629_43907 .Pixso-vector-5579_152456 {
    width: 84.37%;
    height: 81.39%;
    position: absolute;
    left: 7.74%;
    right: 7.89%;
    top: 7.8%;
    bottom: 10.81%;
}
.Pixso-instance-5629_43907 .Pixso-symbol-5579_152455 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5629_43909 .Pixso-symbol-5588_13933 {
    width: 24px;
    height: 20px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
    padding: 4px 8px 4px 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_43909 .Pixso-instance-5588_13934 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_43909 .Pixso-frame-5588_13935 {
    width: 12px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_43909 .Pixso-instance-5588_13936 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_43909 .Pixso-paragraph-5588_13937 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_43909 .Pixso-instance-5588_13938 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_44635 .Pixso-symbol-5579_152455 .Pixso-symbol-5578_150578 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 64.5px;
    top: 10px;
    background-color: transparent;
}
.Pixso-instance-5629_44635 .Pixso-vector-5579_152456 {
    width: 84.37%;
    height: 81.39%;
    position: absolute;
    left: 7.74%;
    right: 7.89%;
    top: 7.8%;
    bottom: 10.81%;
}
.Pixso-instance-5629_44635 .Pixso-symbol-5579_152455 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5629_44637 .Pixso-symbol-5588_11358 {
    width: 24px;
    height: 20px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
    padding: 4px 8px 4px 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_44637 .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_44637 .Pixso-frame-5588_11360 {
    width: 12px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_44637 .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_44637 .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_44637 .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_43750 .Pixso-symbol-5579_152455 .Pixso-symbol-5578_150578 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 10px;
    background-color: transparent;
}
.Pixso-instance-5629_43750 .Pixso-vector-5579_152456 {
    width: 84.37%;
    height: 81.39%;
    position: absolute;
    left: 7.74%;
    right: 7.89%;
    top: 7.8%;
    bottom: 10.81%;
}
.Pixso-instance-5629_43750 .Pixso-symbol-5579_152455 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5629_43752 .Pixso-symbol-5588_13933 {
    width: 24px;
    height: 20px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
    padding: 4px 8px 4px 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_43752 .Pixso-instance-5588_13934 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_43752 .Pixso-frame-5588_13935 {
    width: 12px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_43752 .Pixso-instance-5588_13936 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_43752 .Pixso-paragraph-5588_13937 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_43752 .Pixso-instance-5588_13938 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_43815 .Pixso-symbol-5579_152455 .Pixso-symbol-5578_150578 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 10px;
    background-color: transparent;
}
.Pixso-instance-5629_43815 .Pixso-vector-5579_152456 {
    width: 84.37%;
    height: 81.39%;
    position: absolute;
    left: 7.74%;
    right: 7.89%;
    top: 7.8%;
    bottom: 10.81%;
}
.Pixso-instance-5629_43815 .Pixso-symbol-5579_152455 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5629_43817 .Pixso-symbol-5588_13933 {
    width: 24px;
    height: 20px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
    padding: 4px 8px 4px 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_43817 .Pixso-instance-5588_13934 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_43817 .Pixso-frame-5588_13935 {
    width: 12px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_43817 .Pixso-instance-5588_13936 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_43817 .Pixso-paragraph-5588_13937 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_43817 .Pixso-instance-5588_13938 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_44095 .Pixso-symbol-5579_152455 .Pixso-symbol-5578_150578 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 64.5px;
    top: 10px;
    background-color: transparent;
}
.Pixso-instance-5629_44095 .Pixso-vector-5579_152456 {
    width: 84.37%;
    height: 81.39%;
    position: absolute;
    left: 7.74%;
    right: 7.89%;
    top: 7.8%;
    bottom: 10.81%;
}
.Pixso-instance-5629_44095 .Pixso-symbol-5579_152455 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5629_44097 .Pixso-symbol-5588_13933 {
    width: 24px;
    height: 20px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
    padding: 4px 8px 4px 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_44097 .Pixso-instance-5588_13934 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_44097 .Pixso-frame-5588_13935 {
    width: 12px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_44097 .Pixso-instance-5588_13936 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_44097 .Pixso-paragraph-5588_13937 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_44097 .Pixso-instance-5588_13938 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_44283 .Pixso-symbol-5579_152455 .Pixso-symbol-5578_150578 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 12px;
    top: 10px;
    background-color: transparent;
}
.Pixso-instance-5629_44283 .Pixso-vector-5579_152456 {
    width: 84.37%;
    height: 81.39%;
    position: absolute;
    left: 7.74%;
    right: 7.89%;
    top: 7.8%;
    bottom: 10.81%;
}
.Pixso-instance-5629_44283 .Pixso-symbol-5579_152455 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5629_44285 .Pixso-symbol-5588_13933 {
    width: 24px;
    height: 20px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
    padding: 4px 8px 4px 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_44285 .Pixso-instance-5588_13934 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_44285 .Pixso-frame-5588_13935 {
    width: 12px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_44285 .Pixso-instance-5588_13936 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_44285 .Pixso-paragraph-5588_13937 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_44285 .Pixso-instance-5588_13938 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_44087 .Pixso-symbol-5579_152455 .Pixso-symbol-5578_150578 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 64.5px;
    top: 10px;
    background-color: transparent;
}
.Pixso-instance-5629_44087 .Pixso-vector-5579_152456 {
    width: 84.37%;
    height: 81.39%;
    position: absolute;
    left: 7.74%;
    right: 7.89%;
    top: 7.8%;
    bottom: 10.81%;
}
.Pixso-instance-5629_44087 .Pixso-symbol-5579_152455 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5629_44089 .Pixso-symbol-5588_13933 {
    width: 24px;
    height: 20px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
    padding: 4px 8px 4px 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_44089 .Pixso-instance-5588_13934 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_44089 .Pixso-frame-5588_13935 {
    width: 12px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_44089 .Pixso-instance-5588_13936 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_44089 .Pixso-paragraph-5588_13937 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_44089 .Pixso-instance-5588_13938 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_44091 .Pixso-symbol-5579_152455 .Pixso-symbol-5578_150578 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 64.5px;
    top: 10px;
    background-color: transparent;
}
.Pixso-instance-5629_44091 .Pixso-vector-5579_152456 {
    width: 84.37%;
    height: 81.39%;
    position: absolute;
    left: 7.74%;
    right: 7.89%;
    top: 7.8%;
    bottom: 10.81%;
}
.Pixso-instance-5629_44091 .Pixso-symbol-5579_152455 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5629_44093 .Pixso-symbol-5588_13933 {
    width: 24px;
    height: 20px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
    padding: 4px 8px 4px 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_44093 .Pixso-instance-5588_13934 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_44093 .Pixso-frame-5588_13935 {
    width: 12px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_44093 .Pixso-instance-5588_13936 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_44093 .Pixso-paragraph-5588_13937 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_44093 .Pixso-instance-5588_13938 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_44639 .Pixso-symbol-5579_152455 .Pixso-symbol-5578_150578 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 64.5px;
    top: 10px;
    background-color: transparent;
}
.Pixso-instance-5629_44639 .Pixso-vector-5579_152456 {
    width: 84.37%;
    height: 81.39%;
    position: absolute;
    left: 7.74%;
    right: 7.89%;
    top: 7.8%;
    bottom: 10.81%;
}
.Pixso-instance-5629_44639 .Pixso-symbol-5579_152455 {
    width: 16px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5629_44641 .Pixso-symbol-5588_13933 {
    width: 24px;
    height: 20px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
    padding: 4px 8px 4px 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_44641 .Pixso-instance-5588_13934 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_44641 .Pixso-frame-5588_13935 {
    width: 12px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_44641 .Pixso-instance-5588_13936 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_44641 .Pixso-paragraph-5588_13937 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_44641 .Pixso-instance-5588_13938 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_41189 .Pixso-symbol-5579_152455 .Pixso-symbol-5578_150578 {
    width: 20px;
    height: 20px;
    position: absolute;
    left: 16px;
    top: 10px;
    background-color: transparent;
}
.Pixso-instance-5629_41189 .Pixso-vector-5579_152456 {
    width: 84.37%;
    height: 81.39%;
    position: absolute;
    left: 7.74%;
    right: 7.89%;
    top: 7.8%;
    bottom: 10.81%;
}
.Pixso-instance-5629_41189 .Pixso-symbol-5579_152455 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5629_41092 .Pixso-symbol-5588_11358 {
    width: 28px;
    height: 24px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
    padding: 4px 8px 4px 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_41092 .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_41092 .Pixso-frame-5588_11360 {
    width: 12px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_41092 .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_41092 .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_41092 .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_41546 .Pixso-symbol-5579_152455 .Pixso-symbol-5578_150578 {
    width: 20px;
    height: 20px;
    position: absolute;
    left: 16px;
    top: 10px;
    background-color: transparent;
}
.Pixso-instance-5629_41546 .Pixso-vector-5579_152456 {
    width: 84.37%;
    height: 81.39%;
    position: absolute;
    left: 7.74%;
    right: 7.89%;
    top: 7.8%;
    bottom: 10.81%;
}
.Pixso-instance-5629_41546 .Pixso-symbol-5579_152455 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5629_41548 .Pixso-symbol-5588_11358 {
    width: 28px;
    height: 24px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
    padding: 4px 8px 4px 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_41548 .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_41548 .Pixso-frame-5588_11360 {
    width: 12px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_41548 .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_41548 .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_41548 .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_41726 .Pixso-symbol-5579_152455 .Pixso-symbol-5578_150578 {
    width: 20px;
    height: 20px;
    position: absolute;
    left: 60.5px;
    top: 10px;
    background-color: transparent;
}
.Pixso-instance-5629_41726 .Pixso-vector-5579_152456 {
    width: 84.37%;
    height: 81.39%;
    position: absolute;
    left: 7.74%;
    right: 7.89%;
    top: 7.8%;
    bottom: 10.81%;
}
.Pixso-instance-5629_41726 .Pixso-symbol-5579_152455 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5629_41728 .Pixso-symbol-5588_11358 {
    width: 28px;
    height: 24px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
    padding: 4px 8px 4px 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_41728 .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_41728 .Pixso-frame-5588_11360 {
    width: 12px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_41728 .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_41728 .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_41728 .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_41454 .Pixso-symbol-5579_152455 .Pixso-symbol-5578_150578 {
    width: 20px;
    height: 20px;
    position: absolute;
    left: 16px;
    top: 10px;
    background-color: transparent;
}
.Pixso-instance-5629_41454 .Pixso-vector-5579_152456 {
    width: 84.37%;
    height: 81.39%;
    position: absolute;
    left: 7.74%;
    right: 7.89%;
    top: 7.8%;
    bottom: 10.81%;
}
.Pixso-instance-5629_41454 .Pixso-symbol-5579_152455 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5629_41456 .Pixso-symbol-5588_11358 {
    width: 28px;
    height: 24px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
    padding: 4px 8px 4px 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_41456 .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_41456 .Pixso-frame-5588_11360 {
    width: 12px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_41456 .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_41456 .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_41456 .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_44353 .Pixso-symbol-5579_152455 .Pixso-symbol-5578_150578 {
    width: 20px;
    height: 20px;
    position: absolute;
    left: 16px;
    top: 10px;
    background-color: transparent;
}
.Pixso-instance-5629_44353 .Pixso-vector-5579_152456 {
    width: 84.37%;
    height: 81.39%;
    position: absolute;
    left: 7.74%;
    right: 7.89%;
    top: 7.8%;
    bottom: 10.81%;
}
.Pixso-instance-5629_44353 .Pixso-symbol-5579_152455 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5629_44355 .Pixso-symbol-5588_11358 {
    width: 28px;
    height: 24px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
    padding: 4px 8px 4px 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_44355 .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_44355 .Pixso-frame-5588_11360 {
    width: 12px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_44355 .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_44355 .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_44355 .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_41718 .Pixso-symbol-5579_152455 .Pixso-symbol-5578_150578 {
    width: 20px;
    height: 20px;
    position: absolute;
    left: 60.5px;
    top: 10px;
    background-color: transparent;
}
.Pixso-instance-5629_41718 .Pixso-vector-5579_152456 {
    width: 84.37%;
    height: 81.39%;
    position: absolute;
    left: 7.74%;
    right: 7.89%;
    top: 7.8%;
    bottom: 10.81%;
}
.Pixso-instance-5629_41718 .Pixso-symbol-5579_152455 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5629_41720 .Pixso-symbol-5588_11358 {
    width: 28px;
    height: 24px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
    padding: 4px 8px 4px 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_41720 .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_41720 .Pixso-frame-5588_11360 {
    width: 12px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_41720 .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_41720 .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_41720 .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_41722 .Pixso-symbol-5579_152455 .Pixso-symbol-5578_150578 {
    width: 20px;
    height: 20px;
    position: absolute;
    left: 60.5px;
    top: 10px;
    background-color: transparent;
}
.Pixso-instance-5629_41722 .Pixso-vector-5579_152456 {
    width: 84.37%;
    height: 81.39%;
    position: absolute;
    left: 7.74%;
    right: 7.89%;
    top: 7.8%;
    bottom: 10.81%;
}
.Pixso-instance-5629_41722 .Pixso-symbol-5579_152455 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5629_41724 .Pixso-symbol-5588_11358 {
    width: 28px;
    height: 24px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
    padding: 4px 8px 4px 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_41724 .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_41724 .Pixso-frame-5588_11360 {
    width: 12px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_41724 .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_41724 .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_41724 .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_44643 .Pixso-symbol-5579_152455 .Pixso-symbol-5578_150578 {
    width: 20px;
    height: 20px;
    position: absolute;
    left: 60.5px;
    top: 10px;
    background-color: transparent;
}
.Pixso-instance-5629_44643 .Pixso-vector-5579_152456 {
    width: 84.37%;
    height: 81.39%;
    position: absolute;
    left: 7.74%;
    right: 7.89%;
    top: 7.8%;
    bottom: 10.81%;
}
.Pixso-instance-5629_44643 .Pixso-symbol-5579_152455 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5629_44645 .Pixso-symbol-5588_11358 {
    width: 28px;
    height: 24px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
    padding: 4px 8px 4px 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_44645 .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_44645 .Pixso-frame-5588_11360 {
    width: 12px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_44645 .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_44645 .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_44645 .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_41224 .Pixso-symbol-5579_152455 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5629_41224 .Pixso-vector-5579_152456 {
    width: 84.37%;
    height: 81.39%;
    position: absolute;
    left: 7.74%;
    right: 7.89%;
    top: 7.8%;
    bottom: 10.81%;
}
.Pixso-instance-5629_41226 .Pixso-symbol-5588_13114 {
    width: 28px;
    height: 24px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
    padding: 4px 8px 4px 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_41226 .Pixso-instance-5588_13115 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_41226 .Pixso-frame-5588_13116 {
    width: 12px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_41226 .Pixso-instance-5588_13117 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_41226 .Pixso-paragraph-5588_13118 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_41226 .Pixso-instance-5588_13119 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_41738 .Pixso-symbol-5579_152455 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5629_41738 .Pixso-vector-5579_152456 {
    width: 84.37%;
    height: 81.39%;
    position: absolute;
    left: 7.74%;
    right: 7.89%;
    top: 7.8%;
    bottom: 10.81%;
}
.Pixso-instance-5629_41740 .Pixso-symbol-5588_13114 {
    width: 28px;
    height: 24px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
    padding: 4px 8px 4px 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_41740 .Pixso-instance-5588_13115 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_41740 .Pixso-frame-5588_13116 {
    width: 12px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_41740 .Pixso-instance-5588_13117 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_41740 .Pixso-paragraph-5588_13118 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_41740 .Pixso-instance-5588_13119 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_41550 .Pixso-symbol-5579_152455 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5629_41550 .Pixso-vector-5579_152456 {
    width: 84.37%;
    height: 81.39%;
    position: absolute;
    left: 7.74%;
    right: 7.89%;
    top: 7.8%;
    bottom: 10.81%;
}
.Pixso-instance-5629_41552 .Pixso-symbol-5588_13114 {
    width: 28px;
    height: 24px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
    padding: 4px 8px 4px 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_41552 .Pixso-instance-5588_13115 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_41552 .Pixso-frame-5588_13116 {
    width: 12px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_41552 .Pixso-instance-5588_13117 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_41552 .Pixso-paragraph-5588_13118 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_41552 .Pixso-instance-5588_13119 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_41458 .Pixso-symbol-5579_152455 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5629_41458 .Pixso-vector-5579_152456 {
    width: 84.37%;
    height: 81.39%;
    position: absolute;
    left: 7.74%;
    right: 7.89%;
    top: 7.8%;
    bottom: 10.81%;
}
.Pixso-instance-5629_41460 .Pixso-symbol-5588_13114 {
    width: 28px;
    height: 24px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
    padding: 4px 8px 4px 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_41460 .Pixso-instance-5588_13115 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_41460 .Pixso-frame-5588_13116 {
    width: 12px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_41460 .Pixso-instance-5588_13117 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_41460 .Pixso-paragraph-5588_13118 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_41460 .Pixso-instance-5588_13119 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_44357 .Pixso-symbol-5579_152455 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5629_44357 .Pixso-vector-5579_152456 {
    width: 84.37%;
    height: 81.39%;
    position: absolute;
    left: 7.74%;
    right: 7.89%;
    top: 7.8%;
    bottom: 10.81%;
}
.Pixso-instance-5629_44359 .Pixso-symbol-5588_13114 {
    width: 28px;
    height: 24px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
    padding: 4px 8px 4px 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_44359 .Pixso-instance-5588_13115 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_44359 .Pixso-frame-5588_13116 {
    width: 12px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_44359 .Pixso-instance-5588_13117 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_44359 .Pixso-paragraph-5588_13118 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_44359 .Pixso-instance-5588_13119 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_41730 .Pixso-symbol-5579_152455 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5629_41730 .Pixso-vector-5579_152456 {
    width: 84.37%;
    height: 81.39%;
    position: absolute;
    left: 7.74%;
    right: 7.89%;
    top: 7.8%;
    bottom: 10.81%;
}
.Pixso-instance-5629_41732 .Pixso-symbol-5588_13114 {
    width: 28px;
    height: 24px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
    padding: 4px 8px 4px 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_41732 .Pixso-instance-5588_13115 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_41732 .Pixso-frame-5588_13116 {
    width: 12px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_41732 .Pixso-instance-5588_13117 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_41732 .Pixso-paragraph-5588_13118 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_41732 .Pixso-instance-5588_13119 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_41734 .Pixso-symbol-5579_152455 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5629_41734 .Pixso-vector-5579_152456 {
    width: 84.37%;
    height: 81.39%;
    position: absolute;
    left: 7.74%;
    right: 7.89%;
    top: 7.8%;
    bottom: 10.81%;
}
.Pixso-instance-5629_41736 .Pixso-symbol-5588_13114 {
    width: 28px;
    height: 24px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
    padding: 4px 8px 4px 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_41736 .Pixso-instance-5588_13115 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_41736 .Pixso-frame-5588_13116 {
    width: 12px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_41736 .Pixso-instance-5588_13117 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_41736 .Pixso-paragraph-5588_13118 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_41736 .Pixso-instance-5588_13119 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_44647 .Pixso-symbol-5579_152455 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5629_44647 .Pixso-vector-5579_152456 {
    width: 84.37%;
    height: 81.39%;
    position: absolute;
    left: 7.74%;
    right: 7.89%;
    top: 7.8%;
    bottom: 10.81%;
}
.Pixso-instance-5629_44649 .Pixso-symbol-5588_13114 {
    width: 28px;
    height: 24px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
    padding: 4px 8px 4px 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_44649 .Pixso-instance-5588_13115 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_44649 .Pixso-frame-5588_13116 {
    width: 12px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_44649 .Pixso-instance-5588_13117 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_44649 .Pixso-paragraph-5588_13118 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_44649 .Pixso-instance-5588_13119 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_41750 .Pixso-symbol-5579_152455 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5629_41750 .Pixso-vector-5579_152456 {
    width: 84.37%;
    height: 81.39%;
    position: absolute;
    left: 7.74%;
    right: 7.89%;
    top: 7.8%;
    bottom: 10.81%;
}
.Pixso-instance-5629_41752 .Pixso-symbol-5588_11358 {
    width: 28px;
    height: 24px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
    padding: 4px 8px 4px 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_41752 .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_41752 .Pixso-frame-5588_11360 {
    width: 12px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_41752 .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_41752 .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_41752 .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_41261 .Pixso-symbol-5579_152455 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5629_41261 .Pixso-vector-5579_152456 {
    width: 84.37%;
    height: 81.39%;
    position: absolute;
    left: 7.74%;
    right: 7.89%;
    top: 7.8%;
    bottom: 10.81%;
}
.Pixso-instance-5629_41263 .Pixso-symbol-5588_11358 {
    width: 28px;
    height: 24px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
    padding: 4px 8px 4px 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_41263 .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_41263 .Pixso-frame-5588_11360 {
    width: 12px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_41263 .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_41263 .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_41263 .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_41554 .Pixso-symbol-5579_152455 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5629_41554 .Pixso-vector-5579_152456 {
    width: 84.37%;
    height: 81.39%;
    position: absolute;
    left: 7.74%;
    right: 7.89%;
    top: 7.8%;
    bottom: 10.81%;
}
.Pixso-instance-5629_41556 .Pixso-symbol-5588_11358 {
    width: 28px;
    height: 24px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
    padding: 4px 8px 4px 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_41556 .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_41556 .Pixso-frame-5588_11360 {
    width: 12px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_41556 .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_41556 .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_41556 .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_41462 .Pixso-symbol-5579_152455 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5629_41462 .Pixso-vector-5579_152456 {
    width: 84.37%;
    height: 81.39%;
    position: absolute;
    left: 7.74%;
    right: 7.89%;
    top: 7.8%;
    bottom: 10.81%;
}
.Pixso-instance-5629_41464 .Pixso-symbol-5588_11358 {
    width: 28px;
    height: 24px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
    padding: 4px 8px 4px 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_41464 .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_41464 .Pixso-frame-5588_11360 {
    width: 12px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_41464 .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_41464 .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_41464 .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_44361 .Pixso-symbol-5579_152455 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5629_44361 .Pixso-vector-5579_152456 {
    width: 84.37%;
    height: 81.39%;
    position: absolute;
    left: 7.74%;
    right: 7.89%;
    top: 7.8%;
    bottom: 10.81%;
}
.Pixso-instance-5629_44363 .Pixso-symbol-5588_11358 {
    width: 28px;
    height: 24px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
    padding: 4px 8px 4px 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_44363 .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_44363 .Pixso-frame-5588_11360 {
    width: 12px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_44363 .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_44363 .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_44363 .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_41742 .Pixso-symbol-5579_152455 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5629_41742 .Pixso-vector-5579_152456 {
    width: 84.37%;
    height: 81.39%;
    position: absolute;
    left: 7.74%;
    right: 7.89%;
    top: 7.8%;
    bottom: 10.81%;
}
.Pixso-instance-5629_41744 .Pixso-symbol-5588_11358 {
    width: 28px;
    height: 24px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
    padding: 4px 8px 4px 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_41744 .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_41744 .Pixso-frame-5588_11360 {
    width: 12px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_41744 .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_41744 .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_41744 .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_41746 .Pixso-symbol-5579_152455 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5629_41746 .Pixso-vector-5579_152456 {
    width: 84.37%;
    height: 81.39%;
    position: absolute;
    left: 7.74%;
    right: 7.89%;
    top: 7.8%;
    bottom: 10.81%;
}
.Pixso-instance-5629_41748 .Pixso-symbol-5588_11358 {
    width: 28px;
    height: 24px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
    padding: 4px 8px 4px 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_41748 .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_41748 .Pixso-frame-5588_11360 {
    width: 12px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_41748 .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_41748 .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_41748 .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_41762 .Pixso-symbol-5579_152455 .Pixso-symbol-5578_150578 {
    width: 20px;
    height: 20px;
    position: absolute;
    left: 60.5px;
    top: 10px;
    background-color: transparent;
}
.Pixso-instance-5629_41762 .Pixso-vector-5579_152456 {
    width: 84.37%;
    height: 81.39%;
    position: absolute;
    left: 7.74%;
    right: 7.89%;
    top: 7.8%;
    bottom: 10.81%;
}
.Pixso-instance-5629_41762 .Pixso-symbol-5579_152455 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5629_41764 .Pixso-symbol-5588_13933 {
    width: 28px;
    height: 24px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
    padding: 4px 8px 4px 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_41764 .Pixso-instance-5588_13934 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_41764 .Pixso-frame-5588_13935 {
    width: 12px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_41764 .Pixso-instance-5588_13936 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_41764 .Pixso-paragraph-5588_13937 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_41764 .Pixso-instance-5588_13938 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_44651 .Pixso-symbol-5579_152455 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5629_44651 .Pixso-vector-5579_152456 {
    width: 84.37%;
    height: 81.39%;
    position: absolute;
    left: 7.74%;
    right: 7.89%;
    top: 7.8%;
    bottom: 10.81%;
}
.Pixso-instance-5629_44653 .Pixso-symbol-5588_11358 {
    width: 28px;
    height: 24px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
    padding: 4px 8px 4px 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_44653 .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_44653 .Pixso-frame-5588_11360 {
    width: 12px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_44653 .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_44653 .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_44653 .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_41300 .Pixso-symbol-5579_152455 .Pixso-symbol-5578_150578 {
    width: 20px;
    height: 20px;
    position: absolute;
    left: 16px;
    top: 10px;
    background-color: transparent;
}
.Pixso-instance-5629_41300 .Pixso-vector-5579_152456 {
    width: 84.37%;
    height: 81.39%;
    position: absolute;
    left: 7.74%;
    right: 7.89%;
    top: 7.8%;
    bottom: 10.81%;
}
.Pixso-instance-5629_41300 .Pixso-symbol-5579_152455 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5629_41302 .Pixso-symbol-5588_13933 {
    width: 28px;
    height: 24px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
    padding: 4px 8px 4px 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_41302 .Pixso-instance-5588_13934 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_41302 .Pixso-frame-5588_13935 {
    width: 12px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_41302 .Pixso-instance-5588_13936 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_41302 .Pixso-paragraph-5588_13937 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_41302 .Pixso-instance-5588_13938 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_41558 .Pixso-symbol-5579_152455 .Pixso-symbol-5578_150578 {
    width: 20px;
    height: 20px;
    position: absolute;
    left: 16px;
    top: 10px;
    background-color: transparent;
}
.Pixso-instance-5629_41558 .Pixso-vector-5579_152456 {
    width: 84.37%;
    height: 81.39%;
    position: absolute;
    left: 7.74%;
    right: 7.89%;
    top: 7.8%;
    bottom: 10.81%;
}
.Pixso-instance-5629_41558 .Pixso-symbol-5579_152455 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5629_41560 .Pixso-symbol-5588_13933 {
    width: 28px;
    height: 24px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
    padding: 4px 8px 4px 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_41560 .Pixso-instance-5588_13934 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_41560 .Pixso-frame-5588_13935 {
    width: 12px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_41560 .Pixso-instance-5588_13936 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_41560 .Pixso-paragraph-5588_13937 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_41560 .Pixso-instance-5588_13938 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_41466 .Pixso-symbol-5579_152455 .Pixso-symbol-5578_150578 {
    width: 20px;
    height: 20px;
    position: absolute;
    left: 16px;
    top: 10px;
    background-color: transparent;
}
.Pixso-instance-5629_41466 .Pixso-vector-5579_152456 {
    width: 84.37%;
    height: 81.39%;
    position: absolute;
    left: 7.74%;
    right: 7.89%;
    top: 7.8%;
    bottom: 10.81%;
}
.Pixso-instance-5629_41466 .Pixso-symbol-5579_152455 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5629_41468 .Pixso-symbol-5588_13933 {
    width: 28px;
    height: 24px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
    padding: 4px 8px 4px 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_41468 .Pixso-instance-5588_13934 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_41468 .Pixso-frame-5588_13935 {
    width: 12px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_41468 .Pixso-instance-5588_13936 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_41468 .Pixso-paragraph-5588_13937 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_41468 .Pixso-instance-5588_13938 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_44402 .Pixso-symbol-5579_152455 .Pixso-symbol-5578_150578 {
    width: 20px;
    height: 20px;
    position: absolute;
    left: 16px;
    top: 10px;
    background-color: transparent;
}
.Pixso-instance-5629_44402 .Pixso-vector-5579_152456 {
    width: 84.37%;
    height: 81.39%;
    position: absolute;
    left: 7.74%;
    right: 7.89%;
    top: 7.8%;
    bottom: 10.81%;
}
.Pixso-instance-5629_44402 .Pixso-symbol-5579_152455 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5629_44404 .Pixso-symbol-5588_13933 {
    width: 28px;
    height: 24px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
    padding: 4px 8px 4px 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_44404 .Pixso-instance-5588_13934 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_44404 .Pixso-frame-5588_13935 {
    width: 12px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_44404 .Pixso-instance-5588_13936 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_44404 .Pixso-paragraph-5588_13937 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_44404 .Pixso-instance-5588_13938 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_41754 .Pixso-symbol-5579_152455 .Pixso-symbol-5578_150578 {
    width: 20px;
    height: 20px;
    position: absolute;
    left: 60.5px;
    top: 10px;
    background-color: transparent;
}
.Pixso-instance-5629_41754 .Pixso-vector-5579_152456 {
    width: 84.37%;
    height: 81.39%;
    position: absolute;
    left: 7.74%;
    right: 7.89%;
    top: 7.8%;
    bottom: 10.81%;
}
.Pixso-instance-5629_41754 .Pixso-symbol-5579_152455 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5629_41756 .Pixso-symbol-5588_13933 {
    width: 28px;
    height: 24px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
    padding: 4px 8px 4px 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_41756 .Pixso-instance-5588_13934 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_41756 .Pixso-frame-5588_13935 {
    width: 12px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_41756 .Pixso-instance-5588_13936 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_41756 .Pixso-paragraph-5588_13937 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_41756 .Pixso-instance-5588_13938 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_42872 .Pixso-symbol-5579_152455 .Pixso-symbol-5578_150578 {
    width: 20px;
    height: 20px;
    position: absolute;
    left: 54.5px;
    top: 14px;
    background-color: transparent;
}
.Pixso-instance-5629_42872 .Pixso-vector-5579_152456 {
    width: 84.37%;
    height: 81.39%;
    position: absolute;
    left: 7.74%;
    right: 7.89%;
    top: 7.8%;
    bottom: 10.81%;
}
.Pixso-instance-5629_42872 .Pixso-symbol-5579_152455 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5629_42874 .Pixso-symbol-5588_11358 {
    width: 28px;
    height: 24px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
    padding: 4px 8px 4px 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_42874 .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_42874 .Pixso-frame-5588_11360 {
    width: 12px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_42874 .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_42874 .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_42874 .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_41758 .Pixso-symbol-5579_152455 .Pixso-symbol-5578_150578 {
    width: 20px;
    height: 20px;
    position: absolute;
    left: 60.5px;
    top: 10px;
    background-color: transparent;
}
.Pixso-instance-5629_41758 .Pixso-vector-5579_152456 {
    width: 84.37%;
    height: 81.39%;
    position: absolute;
    left: 7.74%;
    right: 7.89%;
    top: 7.8%;
    bottom: 10.81%;
}
.Pixso-instance-5629_41758 .Pixso-symbol-5579_152455 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5629_41760 .Pixso-symbol-5588_13933 {
    width: 28px;
    height: 24px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
    padding: 4px 8px 4px 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_41760 .Pixso-instance-5588_13934 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_41760 .Pixso-frame-5588_13935 {
    width: 12px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_41760 .Pixso-instance-5588_13936 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_41760 .Pixso-paragraph-5588_13937 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_41760 .Pixso-instance-5588_13938 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_44655 .Pixso-symbol-5579_152455 .Pixso-symbol-5578_150578 {
    width: 20px;
    height: 20px;
    position: absolute;
    left: 60.5px;
    top: 10px;
    background-color: transparent;
}
.Pixso-instance-5629_44655 .Pixso-vector-5579_152456 {
    width: 84.37%;
    height: 81.39%;
    position: absolute;
    left: 7.74%;
    right: 7.89%;
    top: 7.8%;
    bottom: 10.81%;
}
.Pixso-instance-5629_44655 .Pixso-symbol-5579_152455 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5629_44657 .Pixso-symbol-5588_13933 {
    width: 28px;
    height: 24px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
    padding: 4px 8px 4px 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_44657 .Pixso-instance-5588_13934 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_44657 .Pixso-frame-5588_13935 {
    width: 12px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_44657 .Pixso-instance-5588_13936 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_44657 .Pixso-paragraph-5588_13937 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_44657 .Pixso-instance-5588_13938 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_42114 .Pixso-symbol-5579_152455 .Pixso-symbol-5578_150578 {
    width: 20px;
    height: 20px;
    position: absolute;
    left: 16px;
    top: 14px;
    background-color: transparent;
}
.Pixso-instance-5629_42114 .Pixso-vector-5579_152456 {
    width: 84.37%;
    height: 81.39%;
    position: absolute;
    left: 7.74%;
    right: 7.89%;
    top: 7.8%;
    bottom: 10.81%;
}
.Pixso-instance-5629_42114 .Pixso-symbol-5579_152455 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5629_42116 .Pixso-symbol-5588_11358 {
    width: 28px;
    height: 24px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
    padding: 4px 8px 4px 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_42116 .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_42116 .Pixso-frame-5588_11360 {
    width: 12px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_42116 .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_42116 .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_42116 .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_42600 .Pixso-symbol-5579_152455 .Pixso-symbol-5578_150578 {
    width: 20px;
    height: 20px;
    position: absolute;
    left: 16px;
    top: 14px;
    background-color: transparent;
}
.Pixso-instance-5629_42600 .Pixso-vector-5579_152456 {
    width: 84.37%;
    height: 81.39%;
    position: absolute;
    left: 7.74%;
    right: 7.89%;
    top: 7.8%;
    bottom: 10.81%;
}
.Pixso-instance-5629_42600 .Pixso-symbol-5579_152455 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5629_42602 .Pixso-symbol-5588_11358 {
    width: 28px;
    height: 24px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
    padding: 4px 8px 4px 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_42602 .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_42602 .Pixso-frame-5588_11360 {
    width: 12px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_42602 .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_42602 .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_42602 .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_42692 .Pixso-symbol-5579_152455 .Pixso-symbol-5578_150578 {
    width: 20px;
    height: 20px;
    position: absolute;
    left: 16px;
    top: 14px;
    background-color: transparent;
}
.Pixso-instance-5629_42692 .Pixso-vector-5579_152456 {
    width: 84.37%;
    height: 81.39%;
    position: absolute;
    left: 7.74%;
    right: 7.89%;
    top: 7.8%;
    bottom: 10.81%;
}
.Pixso-instance-5629_42692 .Pixso-symbol-5579_152455 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5629_42694 .Pixso-symbol-5588_11358 {
    width: 28px;
    height: 24px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
    padding: 4px 8px 4px 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_42694 .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_42694 .Pixso-frame-5588_11360 {
    width: 12px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_42694 .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_42694 .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_42694 .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_44455 .Pixso-symbol-5579_152455 .Pixso-symbol-5578_150578 {
    width: 20px;
    height: 20px;
    position: absolute;
    left: 16px;
    top: 14px;
    background-color: transparent;
}
.Pixso-instance-5629_44455 .Pixso-vector-5579_152456 {
    width: 84.37%;
    height: 81.39%;
    position: absolute;
    left: 7.74%;
    right: 7.89%;
    top: 7.8%;
    bottom: 10.81%;
}
.Pixso-instance-5629_44455 .Pixso-symbol-5579_152455 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5629_44457 .Pixso-symbol-5588_11358 {
    width: 28px;
    height: 24px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
    padding: 4px 8px 4px 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_44457 .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_44457 .Pixso-frame-5588_11360 {
    width: 12px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_44457 .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_44457 .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_44457 .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_42900 .Pixso-symbol-5579_152455 .Pixso-symbol-5578_150578 {
    width: 20px;
    height: 20px;
    position: absolute;
    left: 54.5px;
    top: 14px;
    background-color: transparent;
}
.Pixso-instance-5629_42900 .Pixso-vector-5579_152456 {
    width: 84.37%;
    height: 81.39%;
    position: absolute;
    left: 7.74%;
    right: 7.89%;
    top: 7.8%;
    bottom: 10.81%;
}
.Pixso-instance-5629_42900 .Pixso-symbol-5579_152455 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5629_42902 .Pixso-symbol-5588_13114 {
    width: 28px;
    height: 24px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
    padding: 4px 8px 4px 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_42902 .Pixso-instance-5588_13115 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_42902 .Pixso-frame-5588_13116 {
    width: 12px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_42902 .Pixso-instance-5588_13117 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_42902 .Pixso-paragraph-5588_13118 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_42902 .Pixso-instance-5588_13119 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_42864 .Pixso-symbol-5579_152455 .Pixso-symbol-5578_150578 {
    width: 20px;
    height: 20px;
    position: absolute;
    left: 54.5px;
    top: 14px;
    background-color: transparent;
}
.Pixso-instance-5629_42864 .Pixso-vector-5579_152456 {
    width: 84.37%;
    height: 81.39%;
    position: absolute;
    left: 7.74%;
    right: 7.89%;
    top: 7.8%;
    bottom: 10.81%;
}
.Pixso-instance-5629_42864 .Pixso-symbol-5579_152455 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5629_42866 .Pixso-symbol-5588_11358 {
    width: 28px;
    height: 24px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
    padding: 4px 8px 4px 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_42866 .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_42866 .Pixso-frame-5588_11360 {
    width: 12px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_42866 .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_42866 .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_42866 .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_42868 .Pixso-symbol-5579_152455 .Pixso-symbol-5578_150578 {
    width: 20px;
    height: 20px;
    position: absolute;
    left: 54.5px;
    top: 14px;
    background-color: transparent;
}
.Pixso-instance-5629_42868 .Pixso-vector-5579_152456 {
    width: 84.37%;
    height: 81.39%;
    position: absolute;
    left: 7.74%;
    right: 7.89%;
    top: 7.8%;
    bottom: 10.81%;
}
.Pixso-instance-5629_42868 .Pixso-symbol-5579_152455 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5629_42870 .Pixso-symbol-5588_11358 {
    width: 28px;
    height: 24px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
    padding: 4px 8px 4px 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_42870 .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_42870 .Pixso-frame-5588_11360 {
    width: 12px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_42870 .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_42870 .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_42870 .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_44659 .Pixso-symbol-5579_152455 .Pixso-symbol-5578_150578 {
    width: 20px;
    height: 20px;
    position: absolute;
    left: 54.5px;
    top: 14px;
    background-color: transparent;
}
.Pixso-instance-5629_44659 .Pixso-vector-5579_152456 {
    width: 84.37%;
    height: 81.39%;
    position: absolute;
    left: 7.74%;
    right: 7.89%;
    top: 7.8%;
    bottom: 10.81%;
}
.Pixso-instance-5629_44659 .Pixso-symbol-5579_152455 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5629_44661 .Pixso-symbol-5588_11358 {
    width: 28px;
    height: 24px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
    padding: 4px 8px 4px 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_44661 .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_44661 .Pixso-frame-5588_11360 {
    width: 12px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_44661 .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_44661 .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_44661 .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_42469 .Pixso-symbol-5579_152455 .Pixso-symbol-5578_150578 {
    width: 20px;
    height: 20px;
    position: absolute;
    left: 16px;
    top: 14px;
    background-color: transparent;
}
.Pixso-instance-5629_42469 .Pixso-vector-5579_152456 {
    width: 84.37%;
    height: 81.39%;
    position: absolute;
    left: 7.74%;
    right: 7.89%;
    top: 7.8%;
    bottom: 10.81%;
}
.Pixso-instance-5629_42469 .Pixso-symbol-5579_152455 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5629_42471 .Pixso-symbol-5588_13114 {
    width: 28px;
    height: 24px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
    padding: 4px 8px 4px 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_42471 .Pixso-instance-5588_13115 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_42471 .Pixso-frame-5588_13116 {
    width: 12px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_42471 .Pixso-instance-5588_13117 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_42471 .Pixso-paragraph-5588_13118 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_42471 .Pixso-instance-5588_13119 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_42700 .Pixso-symbol-5579_152455 .Pixso-symbol-5578_150578 {
    width: 20px;
    height: 20px;
    position: absolute;
    left: 16px;
    top: 14px;
    background-color: transparent;
}
.Pixso-instance-5629_42700 .Pixso-vector-5579_152456 {
    width: 84.37%;
    height: 81.39%;
    position: absolute;
    left: 7.74%;
    right: 7.89%;
    top: 7.8%;
    bottom: 10.81%;
}
.Pixso-instance-5629_42700 .Pixso-symbol-5579_152455 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5629_42702 .Pixso-symbol-5588_13114 {
    width: 28px;
    height: 24px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
    padding: 4px 8px 4px 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_42702 .Pixso-instance-5588_13115 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_42702 .Pixso-frame-5588_13116 {
    width: 12px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_42702 .Pixso-instance-5588_13117 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_42702 .Pixso-paragraph-5588_13118 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_42702 .Pixso-instance-5588_13119 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_42608 .Pixso-symbol-5579_152455 .Pixso-symbol-5578_150578 {
    width: 20px;
    height: 20px;
    position: absolute;
    left: 16px;
    top: 14px;
    background-color: transparent;
}
.Pixso-instance-5629_42608 .Pixso-vector-5579_152456 {
    width: 84.37%;
    height: 81.39%;
    position: absolute;
    left: 7.74%;
    right: 7.89%;
    top: 7.8%;
    bottom: 10.81%;
}
.Pixso-instance-5629_42608 .Pixso-symbol-5579_152455 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5629_42610 .Pixso-symbol-5588_13114 {
    width: 28px;
    height: 24px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
    padding: 4px 8px 4px 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_42610 .Pixso-instance-5588_13115 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_42610 .Pixso-frame-5588_13116 {
    width: 12px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_42610 .Pixso-instance-5588_13117 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_42610 .Pixso-paragraph-5588_13118 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_42610 .Pixso-instance-5588_13119 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_44459 .Pixso-symbol-5579_152455 .Pixso-symbol-5578_150578 {
    width: 20px;
    height: 20px;
    position: absolute;
    left: 16px;
    top: 14px;
    background-color: transparent;
}
.Pixso-instance-5629_44459 .Pixso-vector-5579_152456 {
    width: 84.37%;
    height: 81.39%;
    position: absolute;
    left: 7.74%;
    right: 7.89%;
    top: 7.8%;
    bottom: 10.81%;
}
.Pixso-instance-5629_44459 .Pixso-symbol-5579_152455 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5629_44461 .Pixso-symbol-5588_13114 {
    width: 28px;
    height: 24px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
    padding: 4px 8px 4px 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_44461 .Pixso-instance-5588_13115 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_44461 .Pixso-frame-5588_13116 {
    width: 12px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_44461 .Pixso-instance-5588_13117 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_44461 .Pixso-paragraph-5588_13118 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_44461 .Pixso-instance-5588_13119 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_42908 .Pixso-symbol-5579_152455 .Pixso-symbol-5578_150578 {
    width: 20px;
    height: 20px;
    position: absolute;
    left: 54.5px;
    top: 14px;
    background-color: transparent;
}
.Pixso-instance-5629_42908 .Pixso-vector-5579_152456 {
    width: 84.37%;
    height: 81.39%;
    position: absolute;
    left: 7.74%;
    right: 7.89%;
    top: 7.8%;
    bottom: 10.81%;
}
.Pixso-instance-5629_42908 .Pixso-symbol-5579_152455 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5629_42910 .Pixso-symbol-5588_11358 {
    width: 28px;
    height: 24px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
    padding: 4px 8px 4px 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_42910 .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_42910 .Pixso-frame-5588_11360 {
    width: 12px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_42910 .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_42910 .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_42910 .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_42896 .Pixso-symbol-5579_152455 .Pixso-symbol-5578_150578 {
    width: 20px;
    height: 20px;
    position: absolute;
    left: 54.5px;
    top: 14px;
    background-color: transparent;
}
.Pixso-instance-5629_42896 .Pixso-vector-5579_152456 {
    width: 84.37%;
    height: 81.39%;
    position: absolute;
    left: 7.74%;
    right: 7.89%;
    top: 7.8%;
    bottom: 10.81%;
}
.Pixso-instance-5629_42896 .Pixso-symbol-5579_152455 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5629_42898 .Pixso-symbol-5588_13114 {
    width: 28px;
    height: 24px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
    padding: 4px 8px 4px 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_42898 .Pixso-instance-5588_13115 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_42898 .Pixso-frame-5588_13116 {
    width: 12px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_42898 .Pixso-instance-5588_13117 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_42898 .Pixso-paragraph-5588_13118 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_42898 .Pixso-instance-5588_13119 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_42884 .Pixso-symbol-5579_152455 .Pixso-symbol-5578_150578 {
    width: 20px;
    height: 20px;
    position: absolute;
    left: 54.5px;
    top: 14px;
    background-color: transparent;
}
.Pixso-instance-5629_42884 .Pixso-vector-5579_152456 {
    width: 84.37%;
    height: 81.39%;
    position: absolute;
    left: 7.74%;
    right: 7.89%;
    top: 7.8%;
    bottom: 10.81%;
}
.Pixso-instance-5629_42884 .Pixso-symbol-5579_152455 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5629_42886 .Pixso-symbol-5588_13114 {
    width: 28px;
    height: 24px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
    padding: 4px 8px 4px 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_42886 .Pixso-instance-5588_13115 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_42886 .Pixso-frame-5588_13116 {
    width: 12px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_42886 .Pixso-instance-5588_13117 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_42886 .Pixso-paragraph-5588_13118 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_42886 .Pixso-instance-5588_13119 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_44663 .Pixso-symbol-5579_152455 .Pixso-symbol-5578_150578 {
    width: 20px;
    height: 20px;
    position: absolute;
    left: 54.5px;
    top: 14px;
    background-color: transparent;
}
.Pixso-instance-5629_44663 .Pixso-vector-5579_152456 {
    width: 84.37%;
    height: 81.39%;
    position: absolute;
    left: 7.74%;
    right: 7.89%;
    top: 7.8%;
    bottom: 10.81%;
}
.Pixso-instance-5629_44663 .Pixso-symbol-5579_152455 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5629_44665 .Pixso-symbol-5588_13114 {
    width: 28px;
    height: 24px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
    padding: 4px 8px 4px 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_44665 .Pixso-instance-5588_13115 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_44665 .Pixso-frame-5588_13116 {
    width: 12px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_44665 .Pixso-instance-5588_13117 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_44665 .Pixso-paragraph-5588_13118 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_44665 .Pixso-instance-5588_13119 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_42704 .Pixso-symbol-5579_152455 .Pixso-symbol-5578_150578 {
    width: 20px;
    height: 20px;
    position: absolute;
    left: 16px;
    top: 14px;
    background-color: transparent;
}
.Pixso-instance-5629_42704 .Pixso-vector-5579_152456 {
    width: 84.37%;
    height: 81.39%;
    position: absolute;
    left: 7.74%;
    right: 7.89%;
    top: 7.8%;
    bottom: 10.81%;
}
.Pixso-instance-5629_42704 .Pixso-symbol-5579_152455 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5629_42706 .Pixso-symbol-5588_11358 {
    width: 28px;
    height: 24px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
    padding: 4px 8px 4px 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_42706 .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_42706 .Pixso-frame-5588_11360 {
    width: 12px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_42706 .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_42706 .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_42706 .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_42500 .Pixso-symbol-5579_152455 .Pixso-symbol-5578_150578 {
    width: 20px;
    height: 20px;
    position: absolute;
    left: 16px;
    top: 14px;
    background-color: transparent;
}
.Pixso-instance-5629_42500 .Pixso-vector-5579_152456 {
    width: 84.37%;
    height: 81.39%;
    position: absolute;
    left: 7.74%;
    right: 7.89%;
    top: 7.8%;
    bottom: 10.81%;
}
.Pixso-instance-5629_42500 .Pixso-symbol-5579_152455 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5629_42502 .Pixso-symbol-5588_11358 {
    width: 28px;
    height: 24px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
    padding: 4px 8px 4px 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_42502 .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_42502 .Pixso-frame-5588_11360 {
    width: 12px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_42502 .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_42502 .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_42502 .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_42888 .Pixso-symbol-5579_152455 .Pixso-symbol-5578_150578 {
    width: 20px;
    height: 20px;
    position: absolute;
    left: 54.5px;
    top: 14px;
    background-color: transparent;
}
.Pixso-instance-5629_42888 .Pixso-vector-5579_152456 {
    width: 84.37%;
    height: 81.39%;
    position: absolute;
    left: 7.74%;
    right: 7.89%;
    top: 7.8%;
    bottom: 10.81%;
}
.Pixso-instance-5629_42888 .Pixso-symbol-5579_152455 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5629_42890 .Pixso-symbol-5588_13933 {
    width: 28px;
    height: 24px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
    padding: 4px 8px 4px 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_42890 .Pixso-instance-5588_13934 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_42890 .Pixso-frame-5588_13935 {
    width: 12px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_42890 .Pixso-instance-5588_13936 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_42890 .Pixso-paragraph-5588_13937 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_42890 .Pixso-instance-5588_13938 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_42612 .Pixso-symbol-5579_152455 .Pixso-symbol-5578_150578 {
    width: 20px;
    height: 20px;
    position: absolute;
    left: 16px;
    top: 14px;
    background-color: transparent;
}
.Pixso-instance-5629_42612 .Pixso-vector-5579_152456 {
    width: 84.37%;
    height: 81.39%;
    position: absolute;
    left: 7.74%;
    right: 7.89%;
    top: 7.8%;
    bottom: 10.81%;
}
.Pixso-instance-5629_42612 .Pixso-symbol-5579_152455 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5629_42614 .Pixso-symbol-5588_11358 {
    width: 28px;
    height: 24px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
    padding: 4px 8px 4px 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_42614 .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_42614 .Pixso-frame-5588_11360 {
    width: 12px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_42614 .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_42614 .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_42614 .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_44463 .Pixso-symbol-5579_152455 .Pixso-symbol-5578_150578 {
    width: 20px;
    height: 20px;
    position: absolute;
    left: 16px;
    top: 14px;
    background-color: transparent;
}
.Pixso-instance-5629_44463 .Pixso-vector-5579_152456 {
    width: 84.37%;
    height: 81.39%;
    position: absolute;
    left: 7.74%;
    right: 7.89%;
    top: 7.8%;
    bottom: 10.81%;
}
.Pixso-instance-5629_44463 .Pixso-symbol-5579_152455 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5629_44465 .Pixso-symbol-5588_11358 {
    width: 28px;
    height: 24px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
    padding: 4px 8px 4px 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_44465 .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_44465 .Pixso-frame-5588_11360 {
    width: 12px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_44465 .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_44465 .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_44465 .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_42904 .Pixso-symbol-5579_152455 .Pixso-symbol-5578_150578 {
    width: 20px;
    height: 20px;
    position: absolute;
    left: 54.5px;
    top: 14px;
    background-color: transparent;
}
.Pixso-instance-5629_42904 .Pixso-vector-5579_152456 {
    width: 84.37%;
    height: 81.39%;
    position: absolute;
    left: 7.74%;
    right: 7.89%;
    top: 7.8%;
    bottom: 10.81%;
}
.Pixso-instance-5629_42904 .Pixso-symbol-5579_152455 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5629_42906 .Pixso-symbol-5588_11358 {
    width: 28px;
    height: 24px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
    padding: 4px 8px 4px 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_42906 .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_42906 .Pixso-frame-5588_11360 {
    width: 12px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_42906 .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_42906 .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_42906 .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_42892 .Pixso-symbol-5579_152455 .Pixso-symbol-5578_150578 {
    width: 20px;
    height: 20px;
    position: absolute;
    left: 54.5px;
    top: 14px;
    background-color: transparent;
}
.Pixso-instance-5629_42892 .Pixso-vector-5579_152456 {
    width: 84.37%;
    height: 81.39%;
    position: absolute;
    left: 7.74%;
    right: 7.89%;
    top: 7.8%;
    bottom: 10.81%;
}
.Pixso-instance-5629_42892 .Pixso-symbol-5579_152455 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5629_42894 .Pixso-symbol-5588_11358 {
    width: 28px;
    height: 24px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
    padding: 4px 8px 4px 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_42894 .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_42894 .Pixso-frame-5588_11360 {
    width: 12px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_42894 .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_42894 .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_42894 .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_42696 .Pixso-symbol-5579_152455 .Pixso-symbol-5578_150578 {
    width: 20px;
    height: 20px;
    position: absolute;
    left: 16px;
    top: 14px;
    background-color: transparent;
}
.Pixso-instance-5629_42696 .Pixso-vector-5579_152456 {
    width: 84.37%;
    height: 81.39%;
    position: absolute;
    left: 7.74%;
    right: 7.89%;
    top: 7.8%;
    bottom: 10.81%;
}
.Pixso-instance-5629_42696 .Pixso-symbol-5579_152455 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5629_42698 .Pixso-symbol-5588_13933 {
    width: 28px;
    height: 24px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
    padding: 4px 8px 4px 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_42698 .Pixso-instance-5588_13934 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_42698 .Pixso-frame-5588_13935 {
    width: 12px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_42698 .Pixso-instance-5588_13936 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_42698 .Pixso-paragraph-5588_13937 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_42698 .Pixso-instance-5588_13938 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_44667 .Pixso-symbol-5579_152455 .Pixso-symbol-5578_150578 {
    width: 20px;
    height: 20px;
    position: absolute;
    left: 54.5px;
    top: 14px;
    background-color: transparent;
}
.Pixso-instance-5629_44667 .Pixso-vector-5579_152456 {
    width: 84.37%;
    height: 81.39%;
    position: absolute;
    left: 7.74%;
    right: 7.89%;
    top: 7.8%;
    bottom: 10.81%;
}
.Pixso-instance-5629_44667 .Pixso-symbol-5579_152455 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5629_44669 .Pixso-symbol-5588_11358 {
    width: 28px;
    height: 24px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
    padding: 4px 8px 4px 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_44669 .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_44669 .Pixso-frame-5588_11360 {
    width: 12px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_44669 .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_44669 .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_44669 .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_42539 .Pixso-symbol-5579_152455 .Pixso-symbol-5578_150578 {
    width: 20px;
    height: 20px;
    position: absolute;
    left: 16px;
    top: 14px;
    background-color: transparent;
}
.Pixso-instance-5629_42539 .Pixso-vector-5579_152456 {
    width: 84.37%;
    height: 81.39%;
    position: absolute;
    left: 7.74%;
    right: 7.89%;
    top: 7.8%;
    bottom: 10.81%;
}
.Pixso-instance-5629_42539 .Pixso-symbol-5579_152455 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5629_42541 .Pixso-symbol-5588_13933 {
    width: 28px;
    height: 24px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
    padding: 4px 8px 4px 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_42541 .Pixso-instance-5588_13934 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_42541 .Pixso-frame-5588_13935 {
    width: 12px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_42541 .Pixso-instance-5588_13936 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_42541 .Pixso-paragraph-5588_13937 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_42541 .Pixso-instance-5588_13938 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_42604 .Pixso-symbol-5579_152455 .Pixso-symbol-5578_150578 {
    width: 20px;
    height: 20px;
    position: absolute;
    left: 16px;
    top: 14px;
    background-color: transparent;
}
.Pixso-instance-5629_42604 .Pixso-vector-5579_152456 {
    width: 84.37%;
    height: 81.39%;
    position: absolute;
    left: 7.74%;
    right: 7.89%;
    top: 7.8%;
    bottom: 10.81%;
}
.Pixso-instance-5629_42604 .Pixso-symbol-5579_152455 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5629_42606 .Pixso-symbol-5588_13933 {
    width: 28px;
    height: 24px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
    padding: 4px 8px 4px 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_42606 .Pixso-instance-5588_13934 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_42606 .Pixso-frame-5588_13935 {
    width: 12px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_42606 .Pixso-instance-5588_13936 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_42606 .Pixso-paragraph-5588_13937 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_42606 .Pixso-instance-5588_13938 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_44467 .Pixso-symbol-5579_152455 .Pixso-symbol-5578_150578 {
    width: 20px;
    height: 20px;
    position: absolute;
    left: 16px;
    top: 14px;
    background-color: transparent;
}
.Pixso-instance-5629_44467 .Pixso-vector-5579_152456 {
    width: 84.37%;
    height: 81.39%;
    position: absolute;
    left: 7.74%;
    right: 7.89%;
    top: 7.8%;
    bottom: 10.81%;
}
.Pixso-instance-5629_44467 .Pixso-symbol-5579_152455 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5629_44469 .Pixso-symbol-5588_13933 {
    width: 28px;
    height: 24px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
    padding: 4px 8px 4px 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_44469 .Pixso-instance-5588_13934 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_44469 .Pixso-frame-5588_13935 {
    width: 12px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_44469 .Pixso-instance-5588_13936 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_44469 .Pixso-paragraph-5588_13937 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_44469 .Pixso-instance-5588_13938 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_42880 .Pixso-symbol-5579_152455 .Pixso-symbol-5578_150578 {
    width: 20px;
    height: 20px;
    position: absolute;
    left: 54.5px;
    top: 14px;
    background-color: transparent;
}
.Pixso-instance-5629_42880 .Pixso-vector-5579_152456 {
    width: 84.37%;
    height: 81.39%;
    position: absolute;
    left: 7.74%;
    right: 7.89%;
    top: 7.8%;
    bottom: 10.81%;
}
.Pixso-instance-5629_42880 .Pixso-symbol-5579_152455 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5629_42882 .Pixso-symbol-5588_13933 {
    width: 28px;
    height: 24px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
    padding: 4px 8px 4px 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_42882 .Pixso-instance-5588_13934 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_42882 .Pixso-frame-5588_13935 {
    width: 12px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_42882 .Pixso-instance-5588_13936 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_42882 .Pixso-paragraph-5588_13937 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_42882 .Pixso-instance-5588_13938 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_42876 .Pixso-symbol-5579_152455 .Pixso-symbol-5578_150578 {
    width: 20px;
    height: 20px;
    position: absolute;
    left: 54.5px;
    top: 14px;
    background-color: transparent;
}
.Pixso-instance-5629_42876 .Pixso-vector-5579_152456 {
    width: 84.37%;
    height: 81.39%;
    position: absolute;
    left: 7.74%;
    right: 7.89%;
    top: 7.8%;
    bottom: 10.81%;
}
.Pixso-instance-5629_42876 .Pixso-symbol-5579_152455 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5629_42878 .Pixso-symbol-5588_13933 {
    width: 28px;
    height: 24px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
    padding: 4px 8px 4px 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_42878 .Pixso-instance-5588_13934 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_42878 .Pixso-frame-5588_13935 {
    width: 12px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_42878 .Pixso-instance-5588_13936 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_42878 .Pixso-paragraph-5588_13937 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_42878 .Pixso-instance-5588_13938 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_44671 .Pixso-symbol-5579_152455 .Pixso-symbol-5578_150578 {
    width: 20px;
    height: 20px;
    position: absolute;
    left: 54.5px;
    top: 14px;
    background-color: transparent;
}
.Pixso-instance-5629_44671 .Pixso-vector-5579_152456 {
    width: 84.37%;
    height: 81.39%;
    position: absolute;
    left: 7.74%;
    right: 7.89%;
    top: 7.8%;
    bottom: 10.81%;
}
.Pixso-instance-5629_44671 .Pixso-symbol-5579_152455 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5629_44673 .Pixso-symbol-5588_13933 {
    width: 28px;
    height: 24px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
    padding: 4px 8px 4px 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_44673 .Pixso-instance-5588_13934 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_44673 .Pixso-frame-5588_13935 {
    width: 12px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_44673 .Pixso-instance-5588_13936 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_44673 .Pixso-paragraph-5588_13937 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_44673 .Pixso-instance-5588_13938 {
    width: 12px;
    height: 12px;
}
</style>
