<template>
    <div class="component-5629_52744">
        <div id="5629_52744" class="Pixso-symbol-5629_52744">
            <div
                id="5629_51807"
                class="Pixso-symbol-5629_51807 fill-gray10-83_2713"
                v-if="
                    Orientation === 'Horizontal' &&
                    Size === 'sm' &&
                    Style === 'Default'
                "
            >
                <slot name="slot_5629_47594" v-if="visible_6000_13">
                    <TabSingle
                        id="5629_47594"
                        class="Pixso-instance-5629_47594"
                        :visible_5560_235="false"
                        :visible_5629_708="false"
                        text_5629_714="Dashboard"
                        State="Default"
                        Style="Default"
                        Size="sm"
                        Width="Hug"
                    >
                        <template #slot_5629_43321>
                            <p
                                id="5629_43321"
                                class="Pixso-paragraph-5629_43321 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                            >
                                {{ "Dashboard" }}
                            </p>
                        </template>
                    </TabSingle>
                </slot>
                <slot name="slot_5629_47684" v-if="visible_6000_38">
                    <TabSingle
                        id="5629_47684"
                        class="Pixso-instance-5629_47684"
                        :visible_5560_235="false"
                        :visible_5629_708="false"
                        text_5629_714="Settings"
                        State="Default"
                        Style="Default"
                        Size="sm"
                        Width="Hug"
                    >
                        <template #slot_5629_43321>
                            <p
                                id="5629_43321"
                                class="Pixso-paragraph-5629_43321 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                            >
                                {{ "Settings" }}
                            </p>
                        </template>
                    </TabSingle>
                </slot>
                <slot name="slot_5629_47694" v-if="visible_6000_63">
                    <TabSingle
                        id="5629_47694"
                        class="Pixso-instance-5629_47694"
                        :visible_5560_235="false"
                        :visible_5629_708="false"
                        text_5629_714="Payment"
                        State="Default"
                        Style="Default"
                        Size="sm"
                        Width="Hug"
                    >
                        <template #slot_5629_43321>
                            <p
                                id="5629_43321"
                                class="Pixso-paragraph-5629_43321 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                            >
                                {{ "Payment" }}
                            </p>
                        </template>
                    </TabSingle>
                </slot>
                <slot name="slot_5629_47704" v-if="visible_6000_88">
                    <TabSingle
                        id="5629_47704"
                        class="Pixso-instance-5629_47704"
                        :visible_5560_235="false"
                        :visible_5629_708="false"
                        text_5629_714="Subscription"
                        State="Default"
                        Style="Default"
                        Size="sm"
                        Width="Hug"
                    >
                        <template #slot_5629_43321>
                            <p
                                id="5629_43321"
                                class="Pixso-paragraph-5629_43321 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                            >
                                {{ "Subscription" }}
                            </p>
                        </template>
                    </TabSingle>
                </slot>
                <slot name="slot_5629_47714" v-if="visible_6000_113">
                    <TabSingle
                        id="5629_47714"
                        class="Pixso-instance-5629_47714"
                        :visible_5629_708="false"
                        text_5629_714="Profile"
                        State="Active"
                        Style="Default"
                        Size="sm"
                        Width="Hug"
                    >
                        <template #slot_5629_43712>
                            <p
                                id="5629_43712"
                                class="Pixso-paragraph-5629_43712 fill-gray80-32_4123-paragraph text-text-smbold-423_3208"
                            >
                                {{ "Profile" }}
                            </p>
                        </template>
                        <template #slot_5629_43713>
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
                        </template>
                    </TabSingle>
                </slot>
            </div>
            <div
                id="5629_51795"
                class="Pixso-symbol-5629_51795 fill-gray10-83_2713"
                v-if="
                    Orientation === 'Horizontal' &&
                    Size === 'md' &&
                    Style === 'Default'
                "
            >
                <slot name="slot_5629_47760" v-if="visible_6000_13">
                    <TabSingle
                        id="5629_47760"
                        class="Pixso-instance-5629_47760"
                        :visible_5560_235="false"
                        :visible_5629_708="false"
                        text_5629_714="Dashboard"
                        State="Default"
                        Style="Default"
                        Size="md"
                        Width="Hug"
                    >
                        <template #slot_5558_51586>
                            <p
                                id="5558_51586"
                                class="Pixso-paragraph-5558_51586 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                            >
                                {{ "Dashboard" }}
                            </p>
                        </template>
                    </TabSingle>
                </slot>
                <slot name="slot_5629_47761" v-if="visible_6000_38">
                    <TabSingle
                        id="5629_47761"
                        class="Pixso-instance-5629_47761"
                        :visible_5560_235="false"
                        :visible_5629_708="false"
                        text_5629_714="Settings"
                        State="Default"
                        Style="Default"
                        Size="md"
                        Width="Hug"
                    >
                        <template #slot_5558_51586>
                            <p
                                id="5558_51586"
                                class="Pixso-paragraph-5558_51586 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                            >
                                {{ "Settings" }}
                            </p>
                        </template>
                    </TabSingle>
                </slot>
                <slot name="slot_5629_47762" v-if="visible_6000_63">
                    <TabSingle
                        id="5629_47762"
                        class="Pixso-instance-5629_47762"
                        :visible_5560_235="false"
                        :visible_5629_708="false"
                        text_5629_714="Payment"
                        State="Default"
                        Style="Default"
                        Size="md"
                        Width="Hug"
                    >
                        <template #slot_5558_51586>
                            <p
                                id="5558_51586"
                                class="Pixso-paragraph-5558_51586 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                            >
                                {{ "Payment" }}
                            </p>
                        </template>
                    </TabSingle>
                </slot>
                <slot name="slot_5629_47763" v-if="visible_6000_88">
                    <TabSingle
                        id="5629_47763"
                        class="Pixso-instance-5629_47763"
                        :visible_5560_235="false"
                        :visible_5629_708="false"
                        text_5629_714="Subscription"
                        State="Default"
                        Style="Default"
                        Size="md"
                        Width="Hug"
                    >
                        <template #slot_5558_51586>
                            <p
                                id="5558_51586"
                                class="Pixso-paragraph-5558_51586 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                            >
                                {{ "Subscription" }}
                            </p>
                        </template>
                    </TabSingle>
                </slot>
                <slot name="slot_5629_47764" v-if="visible_6000_113">
                    <TabSingle
                        id="5629_47764"
                        class="Pixso-instance-5629_47764"
                        :visible_5629_708="false"
                        text_5629_714="Profile"
                        State="Active"
                        Style="Default"
                        Size="md"
                        Width="Hug"
                    >
                        <template #slot_5629_41262>
                            <p
                                id="5629_41262"
                                class="Pixso-paragraph-5629_41262 fill-gray80-32_4123-paragraph text-text-smbold-423_3208"
                            >
                                {{ "Profile" }}
                            </p>
                        </template>
                        <template #slot_5629_41263>
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
                        </template>
                    </TabSingle>
                </slot>
            </div>
            <div
                id="5629_51806"
                class="Pixso-symbol-5629_51806 fill-gray10-83_2713"
                v-if="
                    Orientation === 'Horizontal' &&
                    Size === 'lg' &&
                    Style === 'Default'
                "
            >
                <slot name="slot_5629_47808" v-if="visible_6000_13">
                    <TabSingle
                        id="5629_47808"
                        class="Pixso-instance-5629_47808"
                        :visible_5560_235="false"
                        :visible_5629_708="false"
                        text_5629_714="Dashboard"
                        State="Default"
                        Style="Default"
                        Size="lg"
                        Width="Hug"
                    >
                        <template #slot_5629_42115>
                            <p
                                id="5629_42115"
                                class="Pixso-paragraph-5629_42115 fill-gray60-83_2722-paragraph text-text-mdbold-423_3205"
                            >
                                {{ "Dashboard" }}
                            </p>
                        </template>
                    </TabSingle>
                </slot>
                <slot name="slot_5629_47809" v-if="visible_6000_38">
                    <TabSingle
                        id="5629_47809"
                        class="Pixso-instance-5629_47809"
                        :visible_5560_235="false"
                        :visible_5629_708="false"
                        text_5629_714="Settings"
                        State="Default"
                        Style="Default"
                        Size="lg"
                        Width="Hug"
                    >
                        <template #slot_5629_42115>
                            <p
                                id="5629_42115"
                                class="Pixso-paragraph-5629_42115 fill-gray60-83_2722-paragraph text-text-mdbold-423_3205"
                            >
                                {{ "Settings" }}
                            </p>
                        </template>
                    </TabSingle>
                </slot>
                <slot name="slot_5629_47810" v-if="visible_6000_63">
                    <TabSingle
                        id="5629_47810"
                        class="Pixso-instance-5629_47810"
                        :visible_5560_235="false"
                        :visible_5629_708="false"
                        text_5629_714="Payment"
                        State="Default"
                        Style="Default"
                        Size="lg"
                        Width="Hug"
                    >
                        <template #slot_5629_42115>
                            <p
                                id="5629_42115"
                                class="Pixso-paragraph-5629_42115 fill-gray60-83_2722-paragraph text-text-mdbold-423_3205"
                            >
                                {{ "Payment" }}
                            </p>
                        </template>
                    </TabSingle>
                </slot>
                <slot name="slot_5629_47811" v-if="visible_6000_88">
                    <TabSingle
                        id="5629_47811"
                        class="Pixso-instance-5629_47811"
                        :visible_5560_235="false"
                        :visible_5629_708="false"
                        text_5629_714="Subscription"
                        State="Default"
                        Style="Default"
                        Size="lg"
                        Width="Hug"
                    >
                        <template #slot_5629_42115>
                            <p
                                id="5629_42115"
                                class="Pixso-paragraph-5629_42115 fill-gray60-83_2722-paragraph text-text-mdbold-423_3205"
                            >
                                {{ "Subscription" }}
                            </p>
                        </template>
                    </TabSingle>
                </slot>
                <slot name="slot_5629_47812" v-if="visible_6000_113">
                    <TabSingle
                        id="5629_47812"
                        class="Pixso-instance-5629_47812"
                        :visible_5629_708="false"
                        text_5629_714="Profile"
                        State="Active"
                        Style="Default"
                        Size="lg"
                        Width="Hug"
                    >
                        <template #slot_5629_42501>
                            <p
                                id="5629_42501"
                                class="Pixso-paragraph-5629_42501 fill-gray80-32_4123-paragraph text-text-mdbold-423_3205"
                            >
                                {{ "Profile" }}
                            </p>
                        </template>
                        <template #slot_5629_42502>
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
                        </template>
                    </TabSingle>
                </slot>
            </div>
            <div
                id="5629_51802"
                class="Pixso-symbol-5629_51802"
                v-if="
                    Orientation === 'Horizontal' &&
                    Size === 'sm' &&
                    Style === 'Outlined'
                "
            >
                <slot name="slot_5629_50493" v-if="visible_6000_13">
                    <TabSingle
                        id="5629_50493"
                        class="Pixso-instance-5629_50493"
                        :visible_5560_235="false"
                        :visible_5629_708="false"
                        text_5629_714="Dashboard"
                        State="Default"
                        Style="Outlined"
                        Size="sm"
                        Width="Hug"
                    >
                        <template #slot_5629_43812>
                            <p
                                id="5629_43812"
                                class="Pixso-paragraph-5629_43812 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                            >
                                {{ "Dashboard" }}
                            </p>
                        </template>
                    </TabSingle>
                </slot>
                <slot name="slot_5629_50494" v-if="visible_6000_38">
                    <TabSingle
                        id="5629_50494"
                        class="Pixso-instance-5629_50494"
                        :visible_5560_235="false"
                        :visible_5629_708="false"
                        text_5629_714="Settings"
                        State="Default"
                        Style="Outlined"
                        Size="sm"
                        Width="Hug"
                    >
                        <template #slot_5629_43812>
                            <p
                                id="5629_43812"
                                class="Pixso-paragraph-5629_43812 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                            >
                                {{ "Settings" }}
                            </p>
                        </template>
                    </TabSingle>
                </slot>
                <slot name="slot_5629_50495" v-if="visible_6000_63">
                    <TabSingle
                        id="5629_50495"
                        class="Pixso-instance-5629_50495"
                        :visible_5560_235="false"
                        :visible_5629_708="false"
                        text_5629_714="Payment"
                        State="Default"
                        Style="Outlined"
                        Size="sm"
                        Width="Hug"
                    >
                        <template #slot_5629_43812>
                            <p
                                id="5629_43812"
                                class="Pixso-paragraph-5629_43812 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                            >
                                {{ "Payment" }}
                            </p>
                        </template>
                    </TabSingle>
                </slot>
                <slot name="slot_5629_50496" v-if="visible_6000_88">
                    <TabSingle
                        id="5629_50496"
                        class="Pixso-instance-5629_50496"
                        :visible_5560_235="false"
                        :visible_5629_708="false"
                        text_5629_714="Subscription"
                        State="Default"
                        Style="Outlined"
                        Size="sm"
                        Width="Hug"
                    >
                        <template #slot_5629_43812>
                            <p
                                id="5629_43812"
                                class="Pixso-paragraph-5629_43812 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                            >
                                {{ "Subscription" }}
                            </p>
                        </template>
                    </TabSingle>
                </slot>
                <slot name="slot_5629_50497" v-if="visible_6000_113">
                    <TabSingle
                        id="5629_50497"
                        class="Pixso-instance-5629_50497"
                        :visible_5629_708="false"
                        text_5629_714="Profile"
                        State="Active"
                        Style="Outlined"
                        Size="sm"
                        Width="Hug"
                    >
                        <template #slot_5629_43824>
                            <p
                                id="5629_43824"
                                class="Pixso-paragraph-5629_43824 fill-gray80-32_4123-paragraph text-text-smbold-423_3208"
                            >
                                {{ "Profile" }}
                            </p>
                        </template>
                        <template #slot_5629_43825>
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
                        </template>
                    </TabSingle>
                </slot>
            </div>
            <div
                id="5629_51798"
                class="Pixso-symbol-5629_51798"
                v-if="
                    Orientation === 'Horizontal' &&
                    Size === 'sm' &&
                    Style === 'Bottom Border'
                "
            >
                <slot name="slot_5629_50679" v-if="visible_6000_13">
                    <TabSingle
                        id="5629_50679"
                        class="Pixso-instance-5629_50679"
                        :visible_5560_235="false"
                        :visible_5629_708="false"
                        text_5629_714="Dashboard"
                        State="Default"
                        Style="Bottom Border"
                        Size="sm"
                        Width="Hug"
                    >
                        <template #slot_5629_43904>
                            <p
                                id="5629_43904"
                                class="Pixso-paragraph-5629_43904 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                            >
                                {{ "Dashboard" }}
                            </p>
                        </template>
                    </TabSingle>
                </slot>
                <slot name="slot_5629_50680" v-if="visible_6000_38">
                    <TabSingle
                        id="5629_50680"
                        class="Pixso-instance-5629_50680"
                        :visible_5560_235="false"
                        :visible_5629_708="false"
                        text_5629_714="Settings"
                        State="Default"
                        Style="Bottom Border"
                        Size="sm"
                        Width="Hug"
                    >
                        <template #slot_5629_43904>
                            <p
                                id="5629_43904"
                                class="Pixso-paragraph-5629_43904 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                            >
                                {{ "Settings" }}
                            </p>
                        </template>
                    </TabSingle>
                </slot>
                <slot name="slot_5629_50681" v-if="visible_6000_63">
                    <TabSingle
                        id="5629_50681"
                        class="Pixso-instance-5629_50681"
                        :visible_5560_235="false"
                        :visible_5629_708="false"
                        text_5629_714="Payment"
                        State="Default"
                        Style="Bottom Border"
                        Size="sm"
                        Width="Hug"
                    >
                        <template #slot_5629_43904>
                            <p
                                id="5629_43904"
                                class="Pixso-paragraph-5629_43904 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                            >
                                {{ "Payment" }}
                            </p>
                        </template>
                    </TabSingle>
                </slot>
                <slot name="slot_5629_50682" v-if="visible_6000_88">
                    <TabSingle
                        id="5629_50682"
                        class="Pixso-instance-5629_50682"
                        :visible_5560_235="false"
                        :visible_5629_708="false"
                        text_5629_714="Subscription"
                        State="Default"
                        Style="Bottom Border"
                        Size="sm"
                        Width="Hug"
                    >
                        <template #slot_5629_43904>
                            <p
                                id="5629_43904"
                                class="Pixso-paragraph-5629_43904 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                            >
                                {{ "Subscription" }}
                            </p>
                        </template>
                    </TabSingle>
                </slot>
                <slot name="slot_5629_50683" v-if="visible_6000_113">
                    <TabSingle
                        id="5629_50683"
                        class="Pixso-instance-5629_50683"
                        :visible_5629_708="false"
                        text_5629_714="Profile"
                        State="Active"
                        Style="Bottom Border"
                        Size="sm"
                        Width="Hug"
                    >
                        <template #slot_5629_43916>
                            <p
                                id="5629_43916"
                                class="Pixso-paragraph-5629_43916 fill-gray80-32_4123-paragraph text-text-smbold-423_3208"
                            >
                                {{ "Profile" }}
                            </p>
                        </template>
                        <template #slot_5629_43917>
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
                        </template>
                    </TabSingle>
                </slot>
            </div>
            <div
                id="5629_51803"
                class="Pixso-symbol-5629_51803"
                v-if="
                    Orientation === 'Horizontal' &&
                    Size === 'sm' &&
                    Style === 'Left Border'
                "
            >
                <slot name="slot_5629_51050" v-if="visible_6000_13">
                    <TabSingle
                        id="5629_51050"
                        class="Pixso-instance-5629_51050"
                        :visible_5560_235="false"
                        :visible_5629_708="false"
                        text_5629_714="Dashboard"
                        State="Default"
                        Style="Left Border"
                        Size="sm"
                        Width="Hug"
                    >
                        <template #slot_5629_44272>
                            <p
                                id="5629_44272"
                                class="Pixso-paragraph-5629_44272 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                            >
                                {{ "Dashboard" }}
                            </p>
                        </template>
                    </TabSingle>
                </slot>
                <slot name="slot_5629_51051" v-if="visible_6000_38">
                    <TabSingle
                        id="5629_51051"
                        class="Pixso-instance-5629_51051"
                        :visible_5560_235="false"
                        :visible_5629_708="false"
                        text_5629_714="Settings"
                        State="Default"
                        Style="Left Border"
                        Size="sm"
                        Width="Hug"
                    >
                        <template #slot_5629_44272>
                            <p
                                id="5629_44272"
                                class="Pixso-paragraph-5629_44272 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                            >
                                {{ "Settings" }}
                            </p>
                        </template>
                    </TabSingle>
                </slot>
                <slot name="slot_5629_51052" v-if="visible_6000_63">
                    <TabSingle
                        id="5629_51052"
                        class="Pixso-instance-5629_51052"
                        :visible_5560_235="false"
                        :visible_5629_708="false"
                        text_5629_714="Payment"
                        State="Default"
                        Style="Left Border"
                        Size="sm"
                        Width="Hug"
                    >
                        <template #slot_5629_44272>
                            <p
                                id="5629_44272"
                                class="Pixso-paragraph-5629_44272 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                            >
                                {{ "Payment" }}
                            </p>
                        </template>
                    </TabSingle>
                </slot>
                <slot name="slot_5629_51053" v-if="visible_6000_88">
                    <TabSingle
                        id="5629_51053"
                        class="Pixso-instance-5629_51053"
                        :visible_5560_235="false"
                        :visible_5629_708="false"
                        text_5629_714="Subscription"
                        State="Default"
                        Style="Left Border"
                        Size="sm"
                        Width="Hug"
                    >
                        <template #slot_5629_44272>
                            <p
                                id="5629_44272"
                                class="Pixso-paragraph-5629_44272 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                            >
                                {{ "Subscription" }}
                            </p>
                        </template>
                    </TabSingle>
                </slot>
                <slot name="slot_5629_51054" v-if="visible_6000_113">
                    <TabSingle
                        id="5629_51054"
                        class="Pixso-instance-5629_51054"
                        :visible_5629_708="false"
                        text_5629_714="Profile"
                        State="Active"
                        Style="Left Border"
                        Size="sm"
                        Width="Hug"
                    >
                        <template #slot_5629_44280>
                            <p
                                id="5629_44280"
                                class="Pixso-paragraph-5629_44280 fill-gray80-32_4123-paragraph text-text-smbold-423_3208"
                            >
                                {{ "Profile" }}
                            </p>
                        </template>
                        <template #slot_5629_44281>
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
                        </template>
                    </TabSingle>
                </slot>
            </div>
            <div
                id="5629_51805"
                class="Pixso-symbol-5629_51805"
                v-if="
                    Orientation === 'Horizontal' &&
                    Size === 'md' &&
                    Style === 'Bottom Border'
                "
            >
                <slot name="slot_5629_50685" v-if="visible_6000_13">
                    <TabSingle
                        id="5629_50685"
                        class="Pixso-instance-5629_50685"
                        :visible_5560_235="false"
                        :visible_5629_708="false"
                        text_5629_714="Dashboard"
                        State="Default"
                        Style="Bottom Border"
                        Size="md"
                        Width="Hug"
                    >
                        <template #slot_5629_41455>
                            <p
                                id="5629_41455"
                                class="Pixso-paragraph-5629_41455 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                            >
                                {{ "Dashboard" }}
                            </p>
                        </template>
                    </TabSingle>
                </slot>
                <slot name="slot_5629_50686" v-if="visible_6000_38">
                    <TabSingle
                        id="5629_50686"
                        class="Pixso-instance-5629_50686"
                        :visible_5560_235="false"
                        :visible_5629_708="false"
                        text_5629_714="Settings"
                        State="Default"
                        Style="Bottom Border"
                        Size="md"
                        Width="Hug"
                    >
                        <template #slot_5629_41455>
                            <p
                                id="5629_41455"
                                class="Pixso-paragraph-5629_41455 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                            >
                                {{ "Settings" }}
                            </p>
                        </template>
                    </TabSingle>
                </slot>
                <slot name="slot_5629_50687" v-if="visible_6000_63">
                    <TabSingle
                        id="5629_50687"
                        class="Pixso-instance-5629_50687"
                        :visible_5560_235="false"
                        :visible_5629_708="false"
                        text_5629_714="Payment"
                        State="Default"
                        Style="Bottom Border"
                        Size="md"
                        Width="Hug"
                    >
                        <template #slot_5629_41455>
                            <p
                                id="5629_41455"
                                class="Pixso-paragraph-5629_41455 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                            >
                                {{ "Payment" }}
                            </p>
                        </template>
                    </TabSingle>
                </slot>
                <slot name="slot_5629_50688" v-if="visible_6000_88">
                    <TabSingle
                        id="5629_50688"
                        class="Pixso-instance-5629_50688"
                        :visible_5560_235="false"
                        :visible_5629_708="false"
                        text_5629_714="Subscription"
                        State="Default"
                        Style="Bottom Border"
                        Size="md"
                        Width="Hug"
                    >
                        <template #slot_5629_41455>
                            <p
                                id="5629_41455"
                                class="Pixso-paragraph-5629_41455 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                            >
                                {{ "Subscription" }}
                            </p>
                        </template>
                    </TabSingle>
                </slot>
                <slot name="slot_5629_50689" v-if="visible_6000_113">
                    <TabSingle
                        id="5629_50689"
                        class="Pixso-instance-5629_50689"
                        :visible_5629_708="false"
                        text_5629_714="Profile"
                        State="Active"
                        Style="Bottom Border"
                        Size="md"
                        Width="Hug"
                    >
                        <template #slot_5629_41463>
                            <p
                                id="5629_41463"
                                class="Pixso-paragraph-5629_41463 fill-gray80-32_4123-paragraph text-text-smbold-423_3208"
                            >
                                {{ "Profile" }}
                            </p>
                        </template>
                        <template #slot_5629_41464>
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
                        </template>
                    </TabSingle>
                </slot>
            </div>
            <div
                id="5629_51804"
                class="Pixso-symbol-5629_51804"
                v-if="
                    Orientation === 'Horizontal' &&
                    Size === 'md' &&
                    Style === 'Outlined'
                "
            >
                <slot name="slot_5629_50499" v-if="visible_6000_13">
                    <TabSingle
                        id="5629_50499"
                        class="Pixso-instance-5629_50499"
                        :visible_5560_235="false"
                        :visible_5629_708="false"
                        text_5629_714="Dashboard"
                        State="Default"
                        Style="Outlined"
                        Size="md"
                        Width="Hug"
                    >
                        <template #slot_5629_41547>
                            <p
                                id="5629_41547"
                                class="Pixso-paragraph-5629_41547 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                            >
                                {{ "Dashboard" }}
                            </p>
                        </template>
                    </TabSingle>
                </slot>
                <slot name="slot_5629_50500" v-if="visible_6000_38">
                    <TabSingle
                        id="5629_50500"
                        class="Pixso-instance-5629_50500"
                        :visible_5560_235="false"
                        :visible_5629_708="false"
                        text_5629_714="Settings"
                        State="Default"
                        Style="Outlined"
                        Size="md"
                        Width="Hug"
                    >
                        <template #slot_5629_41547>
                            <p
                                id="5629_41547"
                                class="Pixso-paragraph-5629_41547 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                            >
                                {{ "Settings" }}
                            </p>
                        </template>
                    </TabSingle>
                </slot>
                <slot name="slot_5629_50501" v-if="visible_6000_63">
                    <TabSingle
                        id="5629_50501"
                        class="Pixso-instance-5629_50501"
                        :visible_5560_235="false"
                        :visible_5629_708="false"
                        text_5629_714="Payment"
                        State="Default"
                        Style="Outlined"
                        Size="md"
                        Width="Hug"
                    >
                        <template #slot_5629_41547>
                            <p
                                id="5629_41547"
                                class="Pixso-paragraph-5629_41547 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                            >
                                {{ "Payment" }}
                            </p>
                        </template>
                    </TabSingle>
                </slot>
                <slot name="slot_5629_50502" v-if="visible_6000_88">
                    <TabSingle
                        id="5629_50502"
                        class="Pixso-instance-5629_50502"
                        :visible_5560_235="false"
                        :visible_5629_708="false"
                        text_5629_714="Subscription"
                        State="Default"
                        Style="Outlined"
                        Size="md"
                        Width="Hug"
                    >
                        <template #slot_5629_41547>
                            <p
                                id="5629_41547"
                                class="Pixso-paragraph-5629_41547 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                            >
                                {{ "Subscription" }}
                            </p>
                        </template>
                    </TabSingle>
                </slot>
                <slot name="slot_5629_50503" v-if="visible_6000_113">
                    <TabSingle
                        id="5629_50503"
                        class="Pixso-instance-5629_50503"
                        :visible_5629_708="false"
                        text_5629_714="Profile"
                        State="Active"
                        Style="Outlined"
                        Size="md"
                        Width="Hug"
                    >
                        <template #slot_5629_41555>
                            <p
                                id="5629_41555"
                                class="Pixso-paragraph-5629_41555 fill-gray80-32_4123-paragraph text-text-smbold-423_3208"
                            >
                                {{ "Profile" }}
                            </p>
                        </template>
                        <template #slot_5629_41556>
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
                        </template>
                    </TabSingle>
                </slot>
            </div>
            <div
                id="5629_51794"
                class="Pixso-symbol-5629_51794"
                v-if="
                    Orientation === 'Horizontal' &&
                    Size === 'lg' &&
                    Style === 'Bottom Border'
                "
            >
                <slot name="slot_5629_50691" v-if="visible_6000_13">
                    <TabSingle
                        id="5629_50691"
                        class="Pixso-instance-5629_50691"
                        :visible_5560_235="false"
                        :visible_5629_708="false"
                        text_5629_714="Dashboard"
                        State="Default"
                        Style="Bottom Border"
                        Size="lg"
                        Width="Hug"
                    >
                        <template #slot_5629_42693>
                            <p
                                id="5629_42693"
                                class="Pixso-paragraph-5629_42693 fill-gray60-83_2722-paragraph text-text-mdbold-423_3205"
                            >
                                {{ "Dashboard" }}
                            </p>
                        </template>
                    </TabSingle>
                </slot>
                <slot name="slot_5629_50692" v-if="visible_6000_38">
                    <TabSingle
                        id="5629_50692"
                        class="Pixso-instance-5629_50692"
                        :visible_5560_235="false"
                        :visible_5629_708="false"
                        text_5629_714="Settings"
                        State="Default"
                        Style="Bottom Border"
                        Size="lg"
                        Width="Hug"
                    >
                        <template #slot_5629_42693>
                            <p
                                id="5629_42693"
                                class="Pixso-paragraph-5629_42693 fill-gray60-83_2722-paragraph text-text-mdbold-423_3205"
                            >
                                {{ "Settings" }}
                            </p>
                        </template>
                    </TabSingle>
                </slot>
                <slot name="slot_5629_50693" v-if="visible_6000_63">
                    <TabSingle
                        id="5629_50693"
                        class="Pixso-instance-5629_50693"
                        :visible_5560_235="false"
                        :visible_5629_708="false"
                        text_5629_714="Payment"
                        State="Default"
                        Style="Bottom Border"
                        Size="lg"
                        Width="Hug"
                    >
                        <template #slot_5629_42693>
                            <p
                                id="5629_42693"
                                class="Pixso-paragraph-5629_42693 fill-gray60-83_2722-paragraph text-text-mdbold-423_3205"
                            >
                                {{ "Payment" }}
                            </p>
                        </template>
                    </TabSingle>
                </slot>
                <slot name="slot_5629_50694" v-if="visible_6000_88">
                    <TabSingle
                        id="5629_50694"
                        class="Pixso-instance-5629_50694"
                        :visible_5560_235="false"
                        :visible_5629_708="false"
                        text_5629_714="Subscription"
                        State="Default"
                        Style="Bottom Border"
                        Size="lg"
                        Width="Hug"
                    >
                        <template #slot_5629_42693>
                            <p
                                id="5629_42693"
                                class="Pixso-paragraph-5629_42693 fill-gray60-83_2722-paragraph text-text-mdbold-423_3205"
                            >
                                {{ "Subscription" }}
                            </p>
                        </template>
                    </TabSingle>
                </slot>
                <slot name="slot_5629_50695" v-if="visible_6000_113">
                    <TabSingle
                        id="5629_50695"
                        class="Pixso-instance-5629_50695"
                        :visible_5629_708="false"
                        text_5629_714="Profile"
                        State="Active"
                        Style="Bottom Border"
                        Size="lg"
                        Width="Hug"
                    >
                        <template #slot_5629_42705>
                            <p
                                id="5629_42705"
                                class="Pixso-paragraph-5629_42705 fill-gray80-32_4123-paragraph text-text-mdbold-423_3205"
                            >
                                {{ "Profile" }}
                            </p>
                        </template>
                        <template #slot_5629_42706>
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
                        </template>
                    </TabSingle>
                </slot>
            </div>
            <div
                id="5629_51800"
                class="Pixso-symbol-5629_51800"
                v-if="
                    Orientation === 'Horizontal' &&
                    Size === 'md' &&
                    Style === 'Left Border'
                "
            >
                <slot name="slot_5629_51056" v-if="visible_6000_13">
                    <TabSingle
                        id="5629_51056"
                        class="Pixso-instance-5629_51056"
                        :visible_5560_235="false"
                        :visible_5629_708="false"
                        text_5629_714="Dashboard"
                        State="Default"
                        Style="Left Border"
                        Size="md"
                        Width="Hug"
                    >
                        <template #slot_5629_44354>
                            <p
                                id="5629_44354"
                                class="Pixso-paragraph-5629_44354 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                            >
                                {{ "Dashboard" }}
                            </p>
                        </template>
                    </TabSingle>
                </slot>
                <slot name="slot_5629_51057" v-if="visible_6000_38">
                    <TabSingle
                        id="5629_51057"
                        class="Pixso-instance-5629_51057"
                        :visible_5560_235="false"
                        :visible_5629_708="false"
                        text_5629_714="Settings"
                        State="Default"
                        Style="Left Border"
                        Size="md"
                        Width="Hug"
                    >
                        <template #slot_5629_44354>
                            <p
                                id="5629_44354"
                                class="Pixso-paragraph-5629_44354 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                            >
                                {{ "Settings" }}
                            </p>
                        </template>
                    </TabSingle>
                </slot>
                <slot name="slot_5629_51058" v-if="visible_6000_63">
                    <TabSingle
                        id="5629_51058"
                        class="Pixso-instance-5629_51058"
                        :visible_5560_235="false"
                        :visible_5629_708="false"
                        text_5629_714="Payment"
                        State="Default"
                        Style="Left Border"
                        Size="md"
                        Width="Hug"
                    >
                        <template #slot_5629_44354>
                            <p
                                id="5629_44354"
                                class="Pixso-paragraph-5629_44354 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                            >
                                {{ "Payment" }}
                            </p>
                        </template>
                    </TabSingle>
                </slot>
                <slot name="slot_5629_51059" v-if="visible_6000_88">
                    <TabSingle
                        id="5629_51059"
                        class="Pixso-instance-5629_51059"
                        :visible_5560_235="false"
                        :visible_5629_708="false"
                        text_5629_714="Subscription"
                        State="Default"
                        Style="Left Border"
                        Size="md"
                        Width="Hug"
                    >
                        <template #slot_5629_44354>
                            <p
                                id="5629_44354"
                                class="Pixso-paragraph-5629_44354 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                            >
                                {{ "Subscription" }}
                            </p>
                        </template>
                    </TabSingle>
                </slot>
                <slot name="slot_5629_51060" v-if="visible_6000_113">
                    <TabSingle
                        id="5629_51060"
                        class="Pixso-instance-5629_51060"
                        :visible_5629_708="false"
                        text_5629_714="Profile"
                        State="Active"
                        Style="Left Border"
                        Size="md"
                        Width="Hug"
                    >
                        <template #slot_5629_44362>
                            <p
                                id="5629_44362"
                                class="Pixso-paragraph-5629_44362 fill-gray80-32_4123-paragraph text-text-smbold-423_3208"
                            >
                                {{ "Profile" }}
                            </p>
                        </template>
                        <template #slot_5629_44363>
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
                        </template>
                    </TabSingle>
                </slot>
            </div>
            <div
                id="5629_51796"
                class="Pixso-symbol-5629_51796"
                v-if="
                    Orientation === 'Horizontal' &&
                    Size === 'lg' &&
                    Style === 'Outlined'
                "
            >
                <slot name="slot_5629_50505" v-if="visible_6000_13">
                    <TabSingle
                        id="5629_50505"
                        class="Pixso-instance-5629_50505"
                        :visible_5560_235="false"
                        :visible_5629_708="false"
                        text_5629_714="Dashboard"
                        State="Default"
                        Style="Outlined"
                        Size="lg"
                        Width="Hug"
                    >
                        <template #slot_5629_42601>
                            <p
                                id="5629_42601"
                                class="Pixso-paragraph-5629_42601 fill-gray60-83_2722-paragraph text-text-mdbold-423_3205"
                            >
                                {{ "Dashboard" }}
                            </p>
                        </template>
                    </TabSingle>
                </slot>
                <slot name="slot_5629_50506" v-if="visible_6000_38">
                    <TabSingle
                        id="5629_50506"
                        class="Pixso-instance-5629_50506"
                        :visible_5560_235="false"
                        :visible_5629_708="false"
                        text_5629_714="Settings"
                        State="Default"
                        Style="Outlined"
                        Size="lg"
                        Width="Hug"
                    >
                        <template #slot_5629_42601>
                            <p
                                id="5629_42601"
                                class="Pixso-paragraph-5629_42601 fill-gray60-83_2722-paragraph text-text-mdbold-423_3205"
                            >
                                {{ "Settings" }}
                            </p>
                        </template>
                    </TabSingle>
                </slot>
                <slot name="slot_5629_50507" v-if="visible_6000_63">
                    <TabSingle
                        id="5629_50507"
                        class="Pixso-instance-5629_50507"
                        :visible_5560_235="false"
                        :visible_5629_708="false"
                        text_5629_714="Payment"
                        State="Default"
                        Style="Outlined"
                        Size="lg"
                        Width="Hug"
                    >
                        <template #slot_5629_42601>
                            <p
                                id="5629_42601"
                                class="Pixso-paragraph-5629_42601 fill-gray60-83_2722-paragraph text-text-mdbold-423_3205"
                            >
                                {{ "Payment" }}
                            </p>
                        </template>
                    </TabSingle>
                </slot>
                <slot name="slot_5629_50508" v-if="visible_6000_88">
                    <TabSingle
                        id="5629_50508"
                        class="Pixso-instance-5629_50508"
                        :visible_5560_235="false"
                        :visible_5629_708="false"
                        text_5629_714="Subscription"
                        State="Default"
                        Style="Outlined"
                        Size="lg"
                        Width="Hug"
                    >
                        <template #slot_5629_42601>
                            <p
                                id="5629_42601"
                                class="Pixso-paragraph-5629_42601 fill-gray60-83_2722-paragraph text-text-mdbold-423_3205"
                            >
                                {{ "Subscription" }}
                            </p>
                        </template>
                    </TabSingle>
                </slot>
                <slot name="slot_5629_50509" v-if="visible_6000_113">
                    <TabSingle
                        id="5629_50509"
                        class="Pixso-instance-5629_50509"
                        :visible_5629_708="false"
                        text_5629_714="Profile"
                        State="Active"
                        Style="Outlined"
                        Size="lg"
                        Width="Hug"
                    >
                        <template #slot_5629_42613>
                            <p
                                id="5629_42613"
                                class="Pixso-paragraph-5629_42613 fill-gray80-32_4123-paragraph text-text-mdbold-423_3205"
                            >
                                {{ "Profile" }}
                            </p>
                        </template>
                        <template #slot_5629_42614>
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
                        </template>
                    </TabSingle>
                </slot>
            </div>
            <div
                id="5629_51793"
                class="Pixso-symbol-5629_51793"
                v-if="
                    Orientation === 'Horizontal' &&
                    Size === 'lg' &&
                    Style === 'Left Border'
                "
            >
                <slot name="slot_5629_51062" v-if="visible_6000_13">
                    <TabSingle
                        id="5629_51062"
                        class="Pixso-instance-5629_51062"
                        :visible_5560_235="false"
                        :visible_5629_708="false"
                        text_5629_714="Dashboard"
                        State="Default"
                        Style="Left Border"
                        Size="lg"
                        Width="Hug"
                    >
                        <template #slot_5629_44456>
                            <p
                                id="5629_44456"
                                class="Pixso-paragraph-5629_44456 fill-gray60-83_2722-paragraph text-text-mdbold-423_3205"
                            >
                                {{ "Dashboard" }}
                            </p>
                        </template>
                    </TabSingle>
                </slot>
                <slot name="slot_5629_51063" v-if="visible_6000_38">
                    <TabSingle
                        id="5629_51063"
                        class="Pixso-instance-5629_51063"
                        :visible_5560_235="false"
                        :visible_5629_708="false"
                        text_5629_714="Settings"
                        State="Default"
                        Style="Left Border"
                        Size="lg"
                        Width="Hug"
                    >
                        <template #slot_5629_44456>
                            <p
                                id="5629_44456"
                                class="Pixso-paragraph-5629_44456 fill-gray60-83_2722-paragraph text-text-mdbold-423_3205"
                            >
                                {{ "Settings" }}
                            </p>
                        </template>
                    </TabSingle>
                </slot>
                <slot name="slot_5629_51064" v-if="visible_6000_63">
                    <TabSingle
                        id="5629_51064"
                        class="Pixso-instance-5629_51064"
                        :visible_5560_235="false"
                        :visible_5629_708="false"
                        text_5629_714="Payment"
                        State="Default"
                        Style="Left Border"
                        Size="lg"
                        Width="Hug"
                    >
                        <template #slot_5629_44456>
                            <p
                                id="5629_44456"
                                class="Pixso-paragraph-5629_44456 fill-gray60-83_2722-paragraph text-text-mdbold-423_3205"
                            >
                                {{ "Payment" }}
                            </p>
                        </template>
                    </TabSingle>
                </slot>
                <slot name="slot_5629_51065" v-if="visible_6000_88">
                    <TabSingle
                        id="5629_51065"
                        class="Pixso-instance-5629_51065"
                        :visible_5560_235="false"
                        :visible_5629_708="false"
                        text_5629_714="Subscription"
                        State="Default"
                        Style="Left Border"
                        Size="lg"
                        Width="Hug"
                    >
                        <template #slot_5629_44456>
                            <p
                                id="5629_44456"
                                class="Pixso-paragraph-5629_44456 fill-gray60-83_2722-paragraph text-text-mdbold-423_3205"
                            >
                                {{ "Subscription" }}
                            </p>
                        </template>
                    </TabSingle>
                </slot>
                <slot name="slot_5629_51066" v-if="visible_6000_113">
                    <TabSingle
                        id="5629_51066"
                        class="Pixso-instance-5629_51066"
                        :visible_5629_708="false"
                        text_5629_714="Profile"
                        State="Active"
                        Style="Left Border"
                        Size="lg"
                        Width="Hug"
                    >
                        <template #slot_5629_44464>
                            <p
                                id="5629_44464"
                                class="Pixso-paragraph-5629_44464 fill-gray80-32_4123-paragraph text-text-mdbold-423_3205"
                            >
                                {{ "Profile" }}
                            </p>
                        </template>
                        <template #slot_5629_44465>
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
                        </template>
                    </TabSingle>
                </slot>
            </div>
            <div
                id="5629_51790"
                class="Pixso-symbol-5629_51790 fill-gray10-83_2713"
                v-if="
                    Orientation === 'Vertical' &&
                    Size === 'sm' &&
                    Style === 'Default'
                "
            >
                <slot name="slot_5629_51194" v-if="visible_6000_13">
                    <TabSingle
                        id="5629_51194"
                        class="Pixso-instance-5629_51194"
                        :visible_5560_235="false"
                        :visible_5629_708="false"
                        text_5629_714="Dashboard"
                        State="Default"
                        Style="Default"
                        Size="sm"
                        Width="Hug"
                    >
                        <template #slot_5629_43321>
                            <p
                                id="5629_43321"
                                class="Pixso-paragraph-5629_43321 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                            >
                                {{ "Dashboard" }}
                            </p>
                        </template>
                    </TabSingle>
                </slot>
                <slot name="slot_5629_51195" v-if="visible_6000_38">
                    <TabSingle
                        id="5629_51195"
                        class="Pixso-instance-5629_51195"
                        :visible_5560_235="false"
                        :visible_5629_708="false"
                        text_5629_714="Settings"
                        State="Default"
                        Style="Default"
                        Size="sm"
                        Width="Hug"
                    >
                        <template #slot_5629_43321>
                            <p
                                id="5629_43321"
                                class="Pixso-paragraph-5629_43321 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                            >
                                {{ "Settings" }}
                            </p>
                        </template>
                    </TabSingle>
                </slot>
                <slot name="slot_5629_51196" v-if="visible_6000_63">
                    <TabSingle
                        id="5629_51196"
                        class="Pixso-instance-5629_51196"
                        :visible_5560_235="false"
                        :visible_5629_708="false"
                        text_5629_714="Payment"
                        State="Default"
                        Style="Default"
                        Size="sm"
                        Width="Hug"
                    >
                        <template #slot_5629_43321>
                            <p
                                id="5629_43321"
                                class="Pixso-paragraph-5629_43321 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                            >
                                {{ "Payment" }}
                            </p>
                        </template>
                    </TabSingle>
                </slot>
                <slot name="slot_5629_51197" v-if="visible_6000_88">
                    <TabSingle
                        id="5629_51197"
                        class="Pixso-instance-5629_51197"
                        :visible_5560_235="false"
                        :visible_5629_708="false"
                        text_5629_714="Subscription"
                        State="Default"
                        Style="Default"
                        Size="sm"
                        Width="Hug"
                    >
                        <template #slot_5629_43321>
                            <p
                                id="5629_43321"
                                class="Pixso-paragraph-5629_43321 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                            >
                                {{ "Subscription" }}
                            </p>
                        </template>
                    </TabSingle>
                </slot>
                <slot name="slot_5629_51198" v-if="visible_6000_113">
                    <TabSingle
                        id="5629_51198"
                        class="Pixso-instance-5629_51198"
                        :visible_5629_708="false"
                        text_5629_714="Profile"
                        State="Active"
                        Style="Default"
                        Size="sm"
                        Width="Hug"
                    >
                        <template #slot_5629_43712>
                            <p
                                id="5629_43712"
                                class="Pixso-paragraph-5629_43712 fill-gray80-32_4123-paragraph text-text-smbold-423_3208"
                            >
                                {{ "Profile" }}
                            </p>
                        </template>
                        <template #slot_5629_43713>
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
                        </template>
                    </TabSingle>
                </slot>
            </div>
            <div
                id="5629_51788"
                class="Pixso-symbol-5629_51788 fill-gray10-83_2713"
                v-if="
                    Orientation === 'Vertical' &&
                    Size === 'md' &&
                    Style === 'Default'
                "
            >
                <slot name="slot_5629_51200" v-if="visible_6000_13">
                    <TabSingle
                        id="5629_51200"
                        class="Pixso-instance-5629_51200"
                        :visible_5560_235="false"
                        :visible_5629_708="false"
                        text_5629_714="Dashboard"
                        State="Default"
                        Style="Default"
                        Size="md"
                        Width="Hug"
                    >
                        <template #slot_5558_51586>
                            <p
                                id="5558_51586"
                                class="Pixso-paragraph-5558_51586 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                            >
                                {{ "Dashboard" }}
                            </p>
                        </template>
                    </TabSingle>
                </slot>
                <slot name="slot_5629_51201" v-if="visible_6000_38">
                    <TabSingle
                        id="5629_51201"
                        class="Pixso-instance-5629_51201"
                        :visible_5560_235="false"
                        :visible_5629_708="false"
                        text_5629_714="Settings"
                        State="Default"
                        Style="Default"
                        Size="md"
                        Width="Hug"
                    >
                        <template #slot_5558_51586>
                            <p
                                id="5558_51586"
                                class="Pixso-paragraph-5558_51586 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                            >
                                {{ "Settings" }}
                            </p>
                        </template>
                    </TabSingle>
                </slot>
                <slot name="slot_5629_51202" v-if="visible_6000_63">
                    <TabSingle
                        id="5629_51202"
                        class="Pixso-instance-5629_51202"
                        :visible_5560_235="false"
                        :visible_5629_708="false"
                        text_5629_714="Payment"
                        State="Default"
                        Style="Default"
                        Size="md"
                        Width="Hug"
                    >
                        <template #slot_5558_51586>
                            <p
                                id="5558_51586"
                                class="Pixso-paragraph-5558_51586 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                            >
                                {{ "Payment" }}
                            </p>
                        </template>
                    </TabSingle>
                </slot>
                <slot name="slot_5629_51203" v-if="visible_6000_88">
                    <TabSingle
                        id="5629_51203"
                        class="Pixso-instance-5629_51203"
                        :visible_5560_235="false"
                        :visible_5629_708="false"
                        text_5629_714="Subscription"
                        State="Default"
                        Style="Default"
                        Size="md"
                        Width="Hug"
                    >
                        <template #slot_5558_51586>
                            <p
                                id="5558_51586"
                                class="Pixso-paragraph-5558_51586 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                            >
                                {{ "Subscription" }}
                            </p>
                        </template>
                    </TabSingle>
                </slot>
                <slot name="slot_5629_51204" v-if="visible_6000_113">
                    <TabSingle
                        id="5629_51204"
                        class="Pixso-instance-5629_51204"
                        :visible_5629_708="false"
                        text_5629_714="Profile"
                        State="Active"
                        Style="Default"
                        Size="md"
                        Width="Hug"
                    >
                        <template #slot_5629_41262>
                            <p
                                id="5629_41262"
                                class="Pixso-paragraph-5629_41262 fill-gray80-32_4123-paragraph text-text-smbold-423_3208"
                            >
                                {{ "Profile" }}
                            </p>
                        </template>
                        <template #slot_5629_41263>
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
                        </template>
                    </TabSingle>
                </slot>
            </div>
            <div
                id="5629_51787"
                class="Pixso-symbol-5629_51787 fill-gray10-83_2713"
                v-if="
                    Orientation === 'Vertical' &&
                    Size === 'lg' &&
                    Style === 'Default'
                "
            >
                <slot name="slot_5629_51206" v-if="visible_6000_13">
                    <TabSingle
                        id="5629_51206"
                        class="Pixso-instance-5629_51206"
                        :visible_5560_235="false"
                        :visible_5629_708="false"
                        text_5629_714="Dashboard"
                        State="Default"
                        Style="Default"
                        Size="lg"
                        Width="Hug"
                    >
                        <template #slot_5629_42115>
                            <p
                                id="5629_42115"
                                class="Pixso-paragraph-5629_42115 fill-gray60-83_2722-paragraph text-text-mdbold-423_3205"
                            >
                                {{ "Dashboard" }}
                            </p>
                        </template>
                    </TabSingle>
                </slot>
                <slot name="slot_5629_51207" v-if="visible_6000_38">
                    <TabSingle
                        id="5629_51207"
                        class="Pixso-instance-5629_51207"
                        :visible_5560_235="false"
                        :visible_5629_708="false"
                        text_5629_714="Settings"
                        State="Default"
                        Style="Default"
                        Size="lg"
                        Width="Hug"
                    >
                        <template #slot_5629_42115>
                            <p
                                id="5629_42115"
                                class="Pixso-paragraph-5629_42115 fill-gray60-83_2722-paragraph text-text-mdbold-423_3205"
                            >
                                {{ "Settings" }}
                            </p>
                        </template>
                    </TabSingle>
                </slot>
                <slot name="slot_5629_51208" v-if="visible_6000_63">
                    <TabSingle
                        id="5629_51208"
                        class="Pixso-instance-5629_51208"
                        :visible_5560_235="false"
                        :visible_5629_708="false"
                        text_5629_714="Payment"
                        State="Default"
                        Style="Default"
                        Size="lg"
                        Width="Hug"
                    >
                        <template #slot_5629_42115>
                            <p
                                id="5629_42115"
                                class="Pixso-paragraph-5629_42115 fill-gray60-83_2722-paragraph text-text-mdbold-423_3205"
                            >
                                {{ "Payment" }}
                            </p>
                        </template>
                    </TabSingle>
                </slot>
                <slot name="slot_5629_51209" v-if="visible_6000_88">
                    <TabSingle
                        id="5629_51209"
                        class="Pixso-instance-5629_51209"
                        :visible_5560_235="false"
                        :visible_5629_708="false"
                        text_5629_714="Subscription"
                        State="Default"
                        Style="Default"
                        Size="lg"
                        Width="Hug"
                    >
                        <template #slot_5629_42115>
                            <p
                                id="5629_42115"
                                class="Pixso-paragraph-5629_42115 fill-gray60-83_2722-paragraph text-text-mdbold-423_3205"
                            >
                                {{ "Subscription" }}
                            </p>
                        </template>
                    </TabSingle>
                </slot>
                <slot name="slot_5629_51210" v-if="visible_6000_113">
                    <TabSingle
                        id="5629_51210"
                        class="Pixso-instance-5629_51210"
                        :visible_5629_708="false"
                        text_5629_714="Profile"
                        State="Active"
                        Style="Default"
                        Size="lg"
                        Width="Hug"
                    >
                        <template #slot_5629_42501>
                            <p
                                id="5629_42501"
                                class="Pixso-paragraph-5629_42501 fill-gray80-32_4123-paragraph text-text-mdbold-423_3205"
                            >
                                {{ "Profile" }}
                            </p>
                        </template>
                        <template #slot_5629_42502>
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
                        </template>
                    </TabSingle>
                </slot>
            </div>
            <div
                id="5629_51785"
                class="Pixso-symbol-5629_51785"
                v-if="
                    Orientation === 'Vertical' &&
                    Size === 'sm' &&
                    Style === 'Outlined'
                "
            >
                <slot name="slot_5629_51212" v-if="visible_6000_13">
                    <TabSingle
                        id="5629_51212"
                        class="Pixso-instance-5629_51212"
                        :visible_5560_235="false"
                        :visible_5629_708="false"
                        text_5629_714="Dashboard"
                        State="Default"
                        Style="Outlined"
                        Size="sm"
                        Width="Hug"
                    >
                        <template #slot_5629_43812>
                            <p
                                id="5629_43812"
                                class="Pixso-paragraph-5629_43812 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                            >
                                {{ "Dashboard" }}
                            </p>
                        </template>
                    </TabSingle>
                </slot>
                <slot name="slot_5629_51213" v-if="visible_6000_38">
                    <TabSingle
                        id="5629_51213"
                        class="Pixso-instance-5629_51213"
                        :visible_5560_235="false"
                        :visible_5629_708="false"
                        text_5629_714="Settings"
                        State="Default"
                        Style="Outlined"
                        Size="sm"
                        Width="Hug"
                    >
                        <template #slot_5629_43812>
                            <p
                                id="5629_43812"
                                class="Pixso-paragraph-5629_43812 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                            >
                                {{ "Settings" }}
                            </p>
                        </template>
                    </TabSingle>
                </slot>
                <slot name="slot_5629_51214" v-if="visible_6000_63">
                    <TabSingle
                        id="5629_51214"
                        class="Pixso-instance-5629_51214"
                        :visible_5560_235="false"
                        :visible_5629_708="false"
                        text_5629_714="Payment"
                        State="Default"
                        Style="Outlined"
                        Size="sm"
                        Width="Hug"
                    >
                        <template #slot_5629_43812>
                            <p
                                id="5629_43812"
                                class="Pixso-paragraph-5629_43812 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                            >
                                {{ "Payment" }}
                            </p>
                        </template>
                    </TabSingle>
                </slot>
                <slot name="slot_5629_51215" v-if="visible_6000_88">
                    <TabSingle
                        id="5629_51215"
                        class="Pixso-instance-5629_51215"
                        :visible_5560_235="false"
                        :visible_5629_708="false"
                        text_5629_714="Subscription"
                        State="Default"
                        Style="Outlined"
                        Size="sm"
                        Width="Hug"
                    >
                        <template #slot_5629_43812>
                            <p
                                id="5629_43812"
                                class="Pixso-paragraph-5629_43812 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                            >
                                {{ "Subscription" }}
                            </p>
                        </template>
                    </TabSingle>
                </slot>
                <slot name="slot_5629_51216" v-if="visible_6000_113">
                    <TabSingle
                        id="5629_51216"
                        class="Pixso-instance-5629_51216"
                        :visible_5629_708="false"
                        text_5629_714="Profile"
                        State="Active"
                        Style="Outlined"
                        Size="sm"
                        Width="Hug"
                    >
                        <template #slot_5629_43824>
                            <p
                                id="5629_43824"
                                class="Pixso-paragraph-5629_43824 fill-gray80-32_4123-paragraph text-text-smbold-423_3208"
                            >
                                {{ "Profile" }}
                            </p>
                        </template>
                        <template #slot_5629_43825>
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
                        </template>
                    </TabSingle>
                </slot>
            </div>
            <div
                id="5629_51801"
                class="Pixso-symbol-5629_51801"
                v-if="
                    Orientation === 'Vertical' &&
                    Size === 'sm' &&
                    Style === 'Bottom Border'
                "
            >
                <slot name="slot_5629_51218" v-if="visible_6000_13">
                    <TabSingle
                        id="5629_51218"
                        class="Pixso-instance-5629_51218"
                        :visible_5560_235="false"
                        :visible_5629_708="false"
                        text_5629_714="Dashboard"
                        State="Default"
                        Style="Bottom Border"
                        Size="sm"
                        Width="Hug"
                    >
                        <template #slot_5629_43904>
                            <p
                                id="5629_43904"
                                class="Pixso-paragraph-5629_43904 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                            >
                                {{ "Dashboard" }}
                            </p>
                        </template>
                    </TabSingle>
                </slot>
                <slot name="slot_5629_51219" v-if="visible_6000_38">
                    <TabSingle
                        id="5629_51219"
                        class="Pixso-instance-5629_51219"
                        :visible_5560_235="false"
                        :visible_5629_708="false"
                        text_5629_714="Settings"
                        State="Default"
                        Style="Bottom Border"
                        Size="sm"
                        Width="Hug"
                    >
                        <template #slot_5629_43904>
                            <p
                                id="5629_43904"
                                class="Pixso-paragraph-5629_43904 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                            >
                                {{ "Settings" }}
                            </p>
                        </template>
                    </TabSingle>
                </slot>
                <slot name="slot_5629_51220" v-if="visible_6000_63">
                    <TabSingle
                        id="5629_51220"
                        class="Pixso-instance-5629_51220"
                        :visible_5560_235="false"
                        :visible_5629_708="false"
                        text_5629_714="Payment"
                        State="Default"
                        Style="Bottom Border"
                        Size="sm"
                        Width="Hug"
                    >
                        <template #slot_5629_43904>
                            <p
                                id="5629_43904"
                                class="Pixso-paragraph-5629_43904 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                            >
                                {{ "Payment" }}
                            </p>
                        </template>
                    </TabSingle>
                </slot>
                <slot name="slot_5629_51221" v-if="visible_6000_88">
                    <TabSingle
                        id="5629_51221"
                        class="Pixso-instance-5629_51221"
                        :visible_5560_235="false"
                        :visible_5629_708="false"
                        text_5629_714="Subscription"
                        State="Default"
                        Style="Bottom Border"
                        Size="sm"
                        Width="Hug"
                    >
                        <template #slot_5629_43904>
                            <p
                                id="5629_43904"
                                class="Pixso-paragraph-5629_43904 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                            >
                                {{ "Subscription" }}
                            </p>
                        </template>
                    </TabSingle>
                </slot>
                <slot name="slot_5629_51222" v-if="visible_6000_113">
                    <TabSingle
                        id="5629_51222"
                        class="Pixso-instance-5629_51222"
                        :visible_5629_708="false"
                        text_5629_714="Profile"
                        State="Active"
                        Style="Bottom Border"
                        Size="sm"
                        Width="Hug"
                    >
                        <template #slot_5629_43916>
                            <p
                                id="5629_43916"
                                class="Pixso-paragraph-5629_43916 fill-gray80-32_4123-paragraph text-text-smbold-423_3208"
                            >
                                {{ "Profile" }}
                            </p>
                        </template>
                        <template #slot_5629_43917>
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
                        </template>
                    </TabSingle>
                </slot>
            </div>
            <div
                id="5629_51797"
                class="Pixso-symbol-5629_51797"
                v-if="
                    Orientation === 'Vertical' &&
                    Size === 'sm' &&
                    Style === 'Left Border'
                "
            >
                <slot name="slot_5629_51230" v-if="visible_6000_13">
                    <TabSingle
                        id="5629_51230"
                        class="Pixso-instance-5629_51230"
                        :visible_5560_235="false"
                        :visible_5629_708="false"
                        text_5629_714="Dashboard"
                        State="Default"
                        Style="Left Border"
                        Size="sm"
                        Width="Hug"
                    >
                        <template #slot_5629_44272>
                            <p
                                id="5629_44272"
                                class="Pixso-paragraph-5629_44272 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                            >
                                {{ "Dashboard" }}
                            </p>
                        </template>
                    </TabSingle>
                </slot>
                <slot name="slot_5629_51231" v-if="visible_6000_38">
                    <TabSingle
                        id="5629_51231"
                        class="Pixso-instance-5629_51231"
                        :visible_5560_235="false"
                        :visible_5629_708="false"
                        text_5629_714="Settings"
                        State="Default"
                        Style="Left Border"
                        Size="sm"
                        Width="Hug"
                    >
                        <template #slot_5629_44272>
                            <p
                                id="5629_44272"
                                class="Pixso-paragraph-5629_44272 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                            >
                                {{ "Settings" }}
                            </p>
                        </template>
                    </TabSingle>
                </slot>
                <slot name="slot_5629_51232" v-if="visible_6000_63">
                    <TabSingle
                        id="5629_51232"
                        class="Pixso-instance-5629_51232"
                        :visible_5560_235="false"
                        :visible_5629_708="false"
                        text_5629_714="Payment"
                        State="Default"
                        Style="Left Border"
                        Size="sm"
                        Width="Hug"
                    >
                        <template #slot_5629_44272>
                            <p
                                id="5629_44272"
                                class="Pixso-paragraph-5629_44272 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                            >
                                {{ "Payment" }}
                            </p>
                        </template>
                    </TabSingle>
                </slot>
                <slot name="slot_5629_51233" v-if="visible_6000_88">
                    <TabSingle
                        id="5629_51233"
                        class="Pixso-instance-5629_51233"
                        :visible_5560_235="false"
                        :visible_5629_708="false"
                        text_5629_714="Subscription"
                        State="Default"
                        Style="Left Border"
                        Size="sm"
                        Width="Hug"
                    >
                        <template #slot_5629_44272>
                            <p
                                id="5629_44272"
                                class="Pixso-paragraph-5629_44272 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                            >
                                {{ "Subscription" }}
                            </p>
                        </template>
                    </TabSingle>
                </slot>
                <slot name="slot_5629_51234" v-if="visible_6000_113">
                    <TabSingle
                        id="5629_51234"
                        class="Pixso-instance-5629_51234"
                        :visible_5629_708="false"
                        text_5629_714="Profile"
                        State="Active"
                        Style="Left Border"
                        Size="sm"
                        Width="Hug"
                    >
                        <template #slot_5629_44280>
                            <p
                                id="5629_44280"
                                class="Pixso-paragraph-5629_44280 fill-gray80-32_4123-paragraph text-text-smbold-423_3208"
                            >
                                {{ "Profile" }}
                            </p>
                        </template>
                        <template #slot_5629_44281>
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
                        </template>
                    </TabSingle>
                </slot>
            </div>
            <div
                id="5629_51792"
                class="Pixso-symbol-5629_51792"
                v-if="
                    Orientation === 'Vertical' &&
                    Size === 'md' &&
                    Style === 'Bottom Border'
                "
            >
                <slot name="slot_5629_51236" v-if="visible_6000_13">
                    <TabSingle
                        id="5629_51236"
                        class="Pixso-instance-5629_51236"
                        :visible_5560_235="false"
                        :visible_5629_708="false"
                        text_5629_714="Dashboard"
                        State="Default"
                        Style="Bottom Border"
                        Size="md"
                        Width="Hug"
                    >
                        <template #slot_5629_41455>
                            <p
                                id="5629_41455"
                                class="Pixso-paragraph-5629_41455 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                            >
                                {{ "Dashboard" }}
                            </p>
                        </template>
                    </TabSingle>
                </slot>
                <slot name="slot_5629_51237" v-if="visible_6000_38">
                    <TabSingle
                        id="5629_51237"
                        class="Pixso-instance-5629_51237"
                        :visible_5560_235="false"
                        :visible_5629_708="false"
                        text_5629_714="Settings"
                        State="Default"
                        Style="Bottom Border"
                        Size="md"
                        Width="Hug"
                    >
                        <template #slot_5629_41455>
                            <p
                                id="5629_41455"
                                class="Pixso-paragraph-5629_41455 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                            >
                                {{ "Settings" }}
                            </p>
                        </template>
                    </TabSingle>
                </slot>
                <slot name="slot_5629_51238" v-if="visible_6000_63">
                    <TabSingle
                        id="5629_51238"
                        class="Pixso-instance-5629_51238"
                        :visible_5560_235="false"
                        :visible_5629_708="false"
                        text_5629_714="Payment"
                        State="Default"
                        Style="Bottom Border"
                        Size="md"
                        Width="Hug"
                    >
                        <template #slot_5629_41455>
                            <p
                                id="5629_41455"
                                class="Pixso-paragraph-5629_41455 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                            >
                                {{ "Payment" }}
                            </p>
                        </template>
                    </TabSingle>
                </slot>
                <slot name="slot_5629_51239" v-if="visible_6000_88">
                    <TabSingle
                        id="5629_51239"
                        class="Pixso-instance-5629_51239"
                        :visible_5560_235="false"
                        :visible_5629_708="false"
                        text_5629_714="Subscription"
                        State="Default"
                        Style="Bottom Border"
                        Size="md"
                        Width="Hug"
                    >
                        <template #slot_5629_41455>
                            <p
                                id="5629_41455"
                                class="Pixso-paragraph-5629_41455 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                            >
                                {{ "Subscription" }}
                            </p>
                        </template>
                    </TabSingle>
                </slot>
                <slot name="slot_5629_51240" v-if="visible_6000_113">
                    <TabSingle
                        id="5629_51240"
                        class="Pixso-instance-5629_51240"
                        :visible_5629_708="false"
                        text_5629_714="Profile"
                        State="Active"
                        Style="Bottom Border"
                        Size="md"
                        Width="Hug"
                    >
                        <template #slot_5629_41463>
                            <p
                                id="5629_41463"
                                class="Pixso-paragraph-5629_41463 fill-gray80-32_4123-paragraph text-text-smbold-423_3208"
                            >
                                {{ "Profile" }}
                            </p>
                        </template>
                        <template #slot_5629_41464>
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
                        </template>
                    </TabSingle>
                </slot>
            </div>
            <div
                id="5629_51786"
                class="Pixso-symbol-5629_51786"
                v-if="
                    Orientation === 'Vertical' &&
                    Size === 'md' &&
                    Style === 'Outlined'
                "
            >
                <slot name="slot_5629_51242" v-if="visible_6000_13">
                    <TabSingle
                        id="5629_51242"
                        class="Pixso-instance-5629_51242"
                        :visible_5560_235="false"
                        :visible_5629_708="false"
                        text_5629_714="Dashboard"
                        State="Default"
                        Style="Outlined"
                        Size="md"
                        Width="Hug"
                    >
                        <template #slot_5629_41547>
                            <p
                                id="5629_41547"
                                class="Pixso-paragraph-5629_41547 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                            >
                                {{ "Dashboard" }}
                            </p>
                        </template>
                    </TabSingle>
                </slot>
                <slot name="slot_5629_51243" v-if="visible_6000_38">
                    <TabSingle
                        id="5629_51243"
                        class="Pixso-instance-5629_51243"
                        :visible_5560_235="false"
                        :visible_5629_708="false"
                        text_5629_714="Settings"
                        State="Default"
                        Style="Outlined"
                        Size="md"
                        Width="Hug"
                    >
                        <template #slot_5629_41547>
                            <p
                                id="5629_41547"
                                class="Pixso-paragraph-5629_41547 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                            >
                                {{ "Settings" }}
                            </p>
                        </template>
                    </TabSingle>
                </slot>
                <slot name="slot_5629_51244" v-if="visible_6000_63">
                    <TabSingle
                        id="5629_51244"
                        class="Pixso-instance-5629_51244"
                        :visible_5560_235="false"
                        :visible_5629_708="false"
                        text_5629_714="Payment"
                        State="Default"
                        Style="Outlined"
                        Size="md"
                        Width="Hug"
                    >
                        <template #slot_5629_41547>
                            <p
                                id="5629_41547"
                                class="Pixso-paragraph-5629_41547 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                            >
                                {{ "Payment" }}
                            </p>
                        </template>
                    </TabSingle>
                </slot>
                <slot name="slot_5629_51245" v-if="visible_6000_88">
                    <TabSingle
                        id="5629_51245"
                        class="Pixso-instance-5629_51245"
                        :visible_5560_235="false"
                        :visible_5629_708="false"
                        text_5629_714="Subscription"
                        State="Default"
                        Style="Outlined"
                        Size="md"
                        Width="Hug"
                    >
                        <template #slot_5629_41547>
                            <p
                                id="5629_41547"
                                class="Pixso-paragraph-5629_41547 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                            >
                                {{ "Subscription" }}
                            </p>
                        </template>
                    </TabSingle>
                </slot>
                <slot name="slot_5629_51246" v-if="visible_6000_113">
                    <TabSingle
                        id="5629_51246"
                        class="Pixso-instance-5629_51246"
                        :visible_5629_708="false"
                        text_5629_714="Profile"
                        State="Active"
                        Style="Outlined"
                        Size="md"
                        Width="Hug"
                    >
                        <template #slot_5629_41555>
                            <p
                                id="5629_41555"
                                class="Pixso-paragraph-5629_41555 fill-gray80-32_4123-paragraph text-text-smbold-423_3208"
                            >
                                {{ "Profile" }}
                            </p>
                        </template>
                        <template #slot_5629_41556>
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
                        </template>
                    </TabSingle>
                </slot>
            </div>
            <div
                id="5629_51784"
                class="Pixso-symbol-5629_51784"
                v-if="
                    Orientation === 'Vertical' &&
                    Size === 'lg' &&
                    Style === 'Bottom Border'
                "
            >
                <slot name="slot_5629_51248" v-if="visible_6000_13">
                    <TabSingle
                        id="5629_51248"
                        class="Pixso-instance-5629_51248"
                        :visible_5560_235="false"
                        :visible_5629_708="false"
                        text_5629_714="Dashboard"
                        State="Default"
                        Style="Bottom Border"
                        Size="lg"
                        Width="Hug"
                    >
                        <template #slot_5629_42693>
                            <p
                                id="5629_42693"
                                class="Pixso-paragraph-5629_42693 fill-gray60-83_2722-paragraph text-text-mdbold-423_3205"
                            >
                                {{ "Dashboard" }}
                            </p>
                        </template>
                    </TabSingle>
                </slot>
                <slot name="slot_5629_51249" v-if="visible_6000_38">
                    <TabSingle
                        id="5629_51249"
                        class="Pixso-instance-5629_51249"
                        :visible_5560_235="false"
                        :visible_5629_708="false"
                        text_5629_714="Settings"
                        State="Default"
                        Style="Bottom Border"
                        Size="lg"
                        Width="Hug"
                    >
                        <template #slot_5629_42693>
                            <p
                                id="5629_42693"
                                class="Pixso-paragraph-5629_42693 fill-gray60-83_2722-paragraph text-text-mdbold-423_3205"
                            >
                                {{ "Settings" }}
                            </p>
                        </template>
                    </TabSingle>
                </slot>
                <slot name="slot_5629_51250" v-if="visible_6000_63">
                    <TabSingle
                        id="5629_51250"
                        class="Pixso-instance-5629_51250"
                        :visible_5560_235="false"
                        :visible_5629_708="false"
                        text_5629_714="Payment"
                        State="Default"
                        Style="Bottom Border"
                        Size="lg"
                        Width="Hug"
                    >
                        <template #slot_5629_42693>
                            <p
                                id="5629_42693"
                                class="Pixso-paragraph-5629_42693 fill-gray60-83_2722-paragraph text-text-mdbold-423_3205"
                            >
                                {{ "Payment" }}
                            </p>
                        </template>
                    </TabSingle>
                </slot>
                <slot name="slot_5629_51251" v-if="visible_6000_88">
                    <TabSingle
                        id="5629_51251"
                        class="Pixso-instance-5629_51251"
                        :visible_5560_235="false"
                        :visible_5629_708="false"
                        text_5629_714="Subscription"
                        State="Default"
                        Style="Bottom Border"
                        Size="lg"
                        Width="Hug"
                    >
                        <template #slot_5629_42693>
                            <p
                                id="5629_42693"
                                class="Pixso-paragraph-5629_42693 fill-gray60-83_2722-paragraph text-text-mdbold-423_3205"
                            >
                                {{ "Subscription" }}
                            </p>
                        </template>
                    </TabSingle>
                </slot>
                <slot name="slot_5629_51252" v-if="visible_6000_113">
                    <TabSingle
                        id="5629_51252"
                        class="Pixso-instance-5629_51252"
                        :visible_5629_708="false"
                        text_5629_714="Profile"
                        State="Active"
                        Style="Bottom Border"
                        Size="lg"
                        Width="Hug"
                    >
                        <template #slot_5629_42705>
                            <p
                                id="5629_42705"
                                class="Pixso-paragraph-5629_42705 fill-gray80-32_4123-paragraph text-text-mdbold-423_3205"
                            >
                                {{ "Profile" }}
                            </p>
                        </template>
                        <template #slot_5629_42706>
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
                        </template>
                    </TabSingle>
                </slot>
            </div>
            <div
                id="5629_51789"
                class="Pixso-symbol-5629_51789"
                v-if="
                    Orientation === 'Vertical' &&
                    Size === 'md' &&
                    Style === 'Left Border'
                "
            >
                <slot name="slot_5629_51260" v-if="visible_6000_13">
                    <TabSingle
                        id="5629_51260"
                        class="Pixso-instance-5629_51260"
                        :visible_5560_235="false"
                        :visible_5629_708="false"
                        text_5629_714="Dashboard"
                        State="Default"
                        Style="Left Border"
                        Size="md"
                        Width="Hug"
                    >
                        <template #slot_5629_44354>
                            <p
                                id="5629_44354"
                                class="Pixso-paragraph-5629_44354 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                            >
                                {{ "Dashboard" }}
                            </p>
                        </template>
                    </TabSingle>
                </slot>
                <slot name="slot_5629_51261" v-if="visible_6000_38">
                    <TabSingle
                        id="5629_51261"
                        class="Pixso-instance-5629_51261"
                        :visible_5560_235="false"
                        :visible_5629_708="false"
                        text_5629_714="Settings"
                        State="Default"
                        Style="Left Border"
                        Size="md"
                        Width="Hug"
                    >
                        <template #slot_5629_44354>
                            <p
                                id="5629_44354"
                                class="Pixso-paragraph-5629_44354 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                            >
                                {{ "Settings" }}
                            </p>
                        </template>
                    </TabSingle>
                </slot>
                <slot name="slot_5629_51262" v-if="visible_6000_63">
                    <TabSingle
                        id="5629_51262"
                        class="Pixso-instance-5629_51262"
                        :visible_5560_235="false"
                        :visible_5629_708="false"
                        text_5629_714="Payment"
                        State="Default"
                        Style="Left Border"
                        Size="md"
                        Width="Hug"
                    >
                        <template #slot_5629_44354>
                            <p
                                id="5629_44354"
                                class="Pixso-paragraph-5629_44354 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                            >
                                {{ "Payment" }}
                            </p>
                        </template>
                    </TabSingle>
                </slot>
                <slot name="slot_5629_51263" v-if="visible_6000_88">
                    <TabSingle
                        id="5629_51263"
                        class="Pixso-instance-5629_51263"
                        :visible_5560_235="false"
                        :visible_5629_708="false"
                        text_5629_714="Subscription"
                        State="Default"
                        Style="Left Border"
                        Size="md"
                        Width="Hug"
                    >
                        <template #slot_5629_44354>
                            <p
                                id="5629_44354"
                                class="Pixso-paragraph-5629_44354 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                            >
                                {{ "Subscription" }}
                            </p>
                        </template>
                    </TabSingle>
                </slot>
                <slot name="slot_5629_51264" v-if="visible_6000_113">
                    <TabSingle
                        id="5629_51264"
                        class="Pixso-instance-5629_51264"
                        :visible_5629_708="false"
                        text_5629_714="Profile"
                        State="Active"
                        Style="Left Border"
                        Size="md"
                        Width="Hug"
                    >
                        <template #slot_5629_44362>
                            <p
                                id="5629_44362"
                                class="Pixso-paragraph-5629_44362 fill-gray80-32_4123-paragraph text-text-smbold-423_3208"
                            >
                                {{ "Profile" }}
                            </p>
                        </template>
                        <template #slot_5629_44363>
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
                        </template>
                    </TabSingle>
                </slot>
            </div>
            <div
                id="5629_51791"
                class="Pixso-symbol-5629_51791"
                v-if="
                    Orientation === 'Vertical' &&
                    Size === 'lg' &&
                    Style === 'Outlined'
                "
            >
                <slot name="slot_5629_51266" v-if="visible_6000_13">
                    <TabSingle
                        id="5629_51266"
                        class="Pixso-instance-5629_51266"
                        :visible_5560_235="false"
                        :visible_5629_708="false"
                        text_5629_714="Dashboard"
                        State="Default"
                        Style="Outlined"
                        Size="lg"
                        Width="Hug"
                    >
                        <template #slot_5629_42601>
                            <p
                                id="5629_42601"
                                class="Pixso-paragraph-5629_42601 fill-gray60-83_2722-paragraph text-text-mdbold-423_3205"
                            >
                                {{ "Dashboard" }}
                            </p>
                        </template>
                    </TabSingle>
                </slot>
                <slot name="slot_5629_51267" v-if="visible_6000_38">
                    <TabSingle
                        id="5629_51267"
                        class="Pixso-instance-5629_51267"
                        :visible_5560_235="false"
                        :visible_5629_708="false"
                        text_5629_714="Settings"
                        State="Default"
                        Style="Outlined"
                        Size="lg"
                        Width="Hug"
                    >
                        <template #slot_5629_42601>
                            <p
                                id="5629_42601"
                                class="Pixso-paragraph-5629_42601 fill-gray60-83_2722-paragraph text-text-mdbold-423_3205"
                            >
                                {{ "Settings" }}
                            </p>
                        </template>
                    </TabSingle>
                </slot>
                <slot name="slot_5629_51268" v-if="visible_6000_63">
                    <TabSingle
                        id="5629_51268"
                        class="Pixso-instance-5629_51268"
                        :visible_5560_235="false"
                        :visible_5629_708="false"
                        text_5629_714="Payment"
                        State="Default"
                        Style="Outlined"
                        Size="lg"
                        Width="Hug"
                    >
                        <template #slot_5629_42601>
                            <p
                                id="5629_42601"
                                class="Pixso-paragraph-5629_42601 fill-gray60-83_2722-paragraph text-text-mdbold-423_3205"
                            >
                                {{ "Payment" }}
                            </p>
                        </template>
                    </TabSingle>
                </slot>
                <slot name="slot_5629_51269" v-if="visible_6000_88">
                    <TabSingle
                        id="5629_51269"
                        class="Pixso-instance-5629_51269"
                        :visible_5560_235="false"
                        :visible_5629_708="false"
                        text_5629_714="Subscription"
                        State="Default"
                        Style="Outlined"
                        Size="lg"
                        Width="Hug"
                    >
                        <template #slot_5629_42601>
                            <p
                                id="5629_42601"
                                class="Pixso-paragraph-5629_42601 fill-gray60-83_2722-paragraph text-text-mdbold-423_3205"
                            >
                                {{ "Subscription" }}
                            </p>
                        </template>
                    </TabSingle>
                </slot>
                <slot name="slot_5629_51270" v-if="visible_6000_113">
                    <TabSingle
                        id="5629_51270"
                        class="Pixso-instance-5629_51270"
                        :visible_5629_708="false"
                        text_5629_714="Profile"
                        State="Active"
                        Style="Outlined"
                        Size="lg"
                        Width="Hug"
                    >
                        <template #slot_5629_42613>
                            <p
                                id="5629_42613"
                                class="Pixso-paragraph-5629_42613 fill-gray80-32_4123-paragraph text-text-mdbold-423_3205"
                            >
                                {{ "Profile" }}
                            </p>
                        </template>
                        <template #slot_5629_42614>
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
                        </template>
                    </TabSingle>
                </slot>
            </div>
            <div
                id="5629_51799"
                class="Pixso-symbol-5629_51799"
                v-if="
                    Orientation === 'Vertical' &&
                    Size === 'lg' &&
                    Style === 'Left Border'
                "
            >
                <slot name="slot_5629_51278" v-if="visible_6000_13">
                    <TabSingle
                        id="5629_51278"
                        class="Pixso-instance-5629_51278"
                        :visible_5560_235="false"
                        :visible_5629_708="false"
                        text_5629_714="Dashboard"
                        State="Default"
                        Style="Left Border"
                        Size="lg"
                        Width="Hug"
                    >
                        <template #slot_5629_44456>
                            <p
                                id="5629_44456"
                                class="Pixso-paragraph-5629_44456 fill-gray60-83_2722-paragraph text-text-mdbold-423_3205"
                            >
                                {{ "Dashboard" }}
                            </p>
                        </template>
                    </TabSingle>
                </slot>
                <slot name="slot_5629_51279" v-if="visible_6000_38">
                    <TabSingle
                        id="5629_51279"
                        class="Pixso-instance-5629_51279"
                        :visible_5560_235="false"
                        :visible_5629_708="false"
                        text_5629_714="Settings"
                        State="Default"
                        Style="Left Border"
                        Size="lg"
                        Width="Hug"
                    >
                        <template #slot_5629_44456>
                            <p
                                id="5629_44456"
                                class="Pixso-paragraph-5629_44456 fill-gray60-83_2722-paragraph text-text-mdbold-423_3205"
                            >
                                {{ "Settings" }}
                            </p>
                        </template>
                    </TabSingle>
                </slot>
                <slot name="slot_5629_51280" v-if="visible_6000_63">
                    <TabSingle
                        id="5629_51280"
                        class="Pixso-instance-5629_51280"
                        :visible_5560_235="false"
                        :visible_5629_708="false"
                        text_5629_714="Payment"
                        State="Default"
                        Style="Left Border"
                        Size="lg"
                        Width="Hug"
                    >
                        <template #slot_5629_44456>
                            <p
                                id="5629_44456"
                                class="Pixso-paragraph-5629_44456 fill-gray60-83_2722-paragraph text-text-mdbold-423_3205"
                            >
                                {{ "Payment" }}
                            </p>
                        </template>
                    </TabSingle>
                </slot>
                <slot name="slot_5629_51281" v-if="visible_6000_88">
                    <TabSingle
                        id="5629_51281"
                        class="Pixso-instance-5629_51281"
                        :visible_5560_235="false"
                        :visible_5629_708="false"
                        text_5629_714="Subscription"
                        State="Default"
                        Style="Left Border"
                        Size="lg"
                        Width="Hug"
                    >
                        <template #slot_5629_44456>
                            <p
                                id="5629_44456"
                                class="Pixso-paragraph-5629_44456 fill-gray60-83_2722-paragraph text-text-mdbold-423_3205"
                            >
                                {{ "Subscription" }}
                            </p>
                        </template>
                    </TabSingle>
                </slot>
                <slot name="slot_5629_51282" v-if="visible_6000_113">
                    <TabSingle
                        id="5629_51282"
                        class="Pixso-instance-5629_51282"
                        :visible_5629_708="false"
                        text_5629_714="Profile"
                        State="Active"
                        Style="Left Border"
                        Size="lg"
                        Width="Hug"
                    >
                        <template #slot_5629_44464>
                            <p
                                id="5629_44464"
                                class="Pixso-paragraph-5629_44464 fill-gray80-32_4123-paragraph text-text-mdbold-423_3205"
                            >
                                {{ "Profile" }}
                            </p>
                        </template>
                        <template #slot_5629_44465>
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
                        </template>
                    </TabSingle>
                </slot>
            </div>
        </div>
    </div>
</template>
<script lang="ts" setup>
import TabSingle from "@/components/Tabsingle.vue";
import BadgeText from "@/components/Badgetext.vue";
const props = defineProps({
    visible_6000_13: { type: Boolean, default: true },
    visible_6000_38: { type: Boolean, default: true },
    visible_6000_63: { type: Boolean, default: true },
    visible_6000_88: { type: Boolean, default: true },
    visible_6000_113: { type: Boolean, default: true },
    Orientation: { type: String },
    Size: { type: String },
    Style: { type: String }
});
</script>
<style>
.Pixso-symbol-5629_52744 {
}
.Pixso-symbol-5629_51807 {
    width: auto;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: row;
    align-items: flex-start;
    padding: 4px 4px 4px 4px;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5629_47594 {
    width: 99px;
    height: 36px;
}
.Pixso-paragraph-5629_43321 {
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    width: auto;
    height: auto;
    flex-grow: 0;
}
.Pixso-instance-5629_47684 {
    width: 81px;
    height: 36px;
}
.Pixso-instance-5629_47694 {
    width: 85px;
    height: 36px;
}
.Pixso-instance-5629_47704 {
    width: 111px;
    height: 36px;
}
.Pixso-instance-5629_47714 {
    width: 100px;
    height: 36px;
}
.Pixso-paragraph-5629_43712 {
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    width: auto;
    height: auto;
    flex-grow: 0;
}
.Pixso-instance-5629_43713 {
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
.Pixso-symbol-5629_51795 {
    width: auto;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: row;
    align-items: flex-start;
    padding: 4px 4px 4px 4px;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5629_47760 {
    width: 107px;
    height: 40px;
}
.Pixso-paragraph-5558_51586 {
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    width: auto;
    height: auto;
    flex-grow: 0;
}
.Pixso-instance-5629_47761 {
    width: 89px;
    height: 40px;
}
.Pixso-instance-5629_47762 {
    width: 93px;
    height: 40px;
}
.Pixso-instance-5629_47763 {
    width: 119px;
    height: 40px;
}
.Pixso-instance-5629_47764 {
    width: 112px;
    height: 40px;
}
.Pixso-paragraph-5629_41262 {
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    width: auto;
    height: auto;
    flex-grow: 0;
}
.Pixso-instance-5629_41263 {
    width: 28px;
    height: 24px;
}
.Pixso-symbol-5629_51806 {
    width: auto;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: row;
    align-items: flex-start;
    padding: 4px 4px 4px 4px;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5629_47808 {
    width: 118px;
    height: 48px;
}
.Pixso-paragraph-5629_42115 {
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    width: auto;
    height: auto;
    flex-grow: 0;
}
.Pixso-instance-5629_47809 {
    width: 97px;
    height: 48px;
}
.Pixso-instance-5629_47810 {
    width: 101px;
    height: 48px;
}
.Pixso-instance-5629_47811 {
    width: 131px;
    height: 48px;
}
.Pixso-instance-5629_47812 {
    width: 120px;
    height: 48px;
}
.Pixso-paragraph-5629_42501 {
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    width: auto;
    height: auto;
    flex-grow: 0;
}
.Pixso-instance-5629_42502 {
    width: 28px;
    height: 24px;
}
.Pixso-symbol-5629_51802 {
    width: auto;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: row;
    align-items: flex-start;
}
.Pixso-instance-5629_50493 {
    width: 99px;
    height: 36px;
}
.Pixso-paragraph-5629_43812 {
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    width: auto;
    height: auto;
    flex-grow: 0;
}
.Pixso-instance-5629_50494 {
    width: 81px;
    height: 36px;
}
.Pixso-instance-5629_50495 {
    width: 85px;
    height: 36px;
}
.Pixso-instance-5629_50496 {
    width: 111px;
    height: 36px;
}
.Pixso-instance-5629_50497 {
    width: 100px;
    height: 36px;
}
.Pixso-paragraph-5629_43824 {
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    width: auto;
    height: auto;
    flex-grow: 0;
}
.Pixso-instance-5629_43825 {
    width: 24px;
    height: 20px;
}
.Pixso-symbol-5629_51798 {
    width: auto;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: row;
    align-items: flex-start;
}
.Pixso-instance-5629_50679 {
    width: 99px;
    height: 36px;
}
.Pixso-paragraph-5629_43904 {
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    width: auto;
    height: auto;
    flex-grow: 0;
}
.Pixso-instance-5629_50680 {
    width: 81px;
    height: 36px;
}
.Pixso-instance-5629_50681 {
    width: 85px;
    height: 36px;
}
.Pixso-instance-5629_50682 {
    width: 111px;
    height: 36px;
}
.Pixso-instance-5629_50683 {
    width: 100px;
    height: 36px;
}
.Pixso-paragraph-5629_43916 {
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    width: auto;
    height: auto;
    flex-grow: 0;
}
.Pixso-instance-5629_43917 {
    width: 24px;
    height: 20px;
}
.Pixso-symbol-5629_51803 {
    width: auto;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: row;
    align-items: flex-start;
}
.Pixso-instance-5629_51050 {
    width: 99px;
    height: 36px;
}
.Pixso-paragraph-5629_44272 {
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    width: auto;
    height: auto;
    flex-grow: 0;
}
.Pixso-instance-5629_51051 {
    width: 81px;
    height: 36px;
}
.Pixso-instance-5629_51052 {
    width: 85px;
    height: 36px;
}
.Pixso-instance-5629_51053 {
    width: 111px;
    height: 36px;
}
.Pixso-instance-5629_51054 {
    width: 100px;
    height: 36px;
}
.Pixso-paragraph-5629_44280 {
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    width: auto;
    height: auto;
    flex-grow: 0;
}
.Pixso-instance-5629_44281 {
    width: 24px;
    height: 20px;
}
.Pixso-symbol-5629_51805 {
    width: auto;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: row;
    align-items: flex-start;
}
.Pixso-instance-5629_50685 {
    width: 107px;
    height: 40px;
}
.Pixso-paragraph-5629_41455 {
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    width: auto;
    height: auto;
    flex-grow: 0;
}
.Pixso-instance-5629_50686 {
    width: 89px;
    height: 40px;
}
.Pixso-instance-5629_50687 {
    width: 93px;
    height: 40px;
}
.Pixso-instance-5629_50688 {
    width: 119px;
    height: 40px;
}
.Pixso-instance-5629_50689 {
    width: 112px;
    height: 40px;
}
.Pixso-paragraph-5629_41463 {
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    width: auto;
    height: auto;
    flex-grow: 0;
}
.Pixso-instance-5629_41464 {
    width: 28px;
    height: 24px;
}
.Pixso-symbol-5629_51804 {
    width: auto;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: row;
    align-items: flex-start;
}
.Pixso-instance-5629_50499 {
    width: 107px;
    height: 40px;
}
.Pixso-paragraph-5629_41547 {
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    width: auto;
    height: auto;
    flex-grow: 0;
}
.Pixso-instance-5629_50500 {
    width: 89px;
    height: 40px;
}
.Pixso-instance-5629_50501 {
    width: 93px;
    height: 40px;
}
.Pixso-instance-5629_50502 {
    width: 119px;
    height: 40px;
}
.Pixso-instance-5629_50503 {
    width: 112px;
    height: 40px;
}
.Pixso-paragraph-5629_41555 {
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    width: auto;
    height: auto;
    flex-grow: 0;
}
.Pixso-instance-5629_41556 {
    width: 28px;
    height: 24px;
}
.Pixso-symbol-5629_51794 {
    width: auto;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: row;
    align-items: flex-start;
}
.Pixso-instance-5629_50691 {
    width: 118px;
    height: 48px;
}
.Pixso-paragraph-5629_42693 {
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    width: auto;
    height: auto;
    flex-grow: 0;
}
.Pixso-instance-5629_50692 {
    width: 97px;
    height: 48px;
}
.Pixso-instance-5629_50693 {
    width: 101px;
    height: 48px;
}
.Pixso-instance-5629_50694 {
    width: 131px;
    height: 48px;
}
.Pixso-instance-5629_50695 {
    width: 120px;
    height: 48px;
}
.Pixso-paragraph-5629_42705 {
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    width: auto;
    height: auto;
    flex-grow: 0;
}
.Pixso-instance-5629_42706 {
    width: 28px;
    height: 24px;
}
.Pixso-symbol-5629_51800 {
    width: auto;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: row;
    align-items: flex-start;
}
.Pixso-instance-5629_51056 {
    width: 107px;
    height: 40px;
}
.Pixso-paragraph-5629_44354 {
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    width: auto;
    height: auto;
    flex-grow: 0;
}
.Pixso-instance-5629_51057 {
    width: 89px;
    height: 40px;
}
.Pixso-instance-5629_51058 {
    width: 93px;
    height: 40px;
}
.Pixso-instance-5629_51059 {
    width: 119px;
    height: 40px;
}
.Pixso-instance-5629_51060 {
    width: 112px;
    height: 40px;
}
.Pixso-paragraph-5629_44362 {
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    width: auto;
    height: auto;
    flex-grow: 0;
}
.Pixso-instance-5629_44363 {
    width: 28px;
    height: 24px;
}
.Pixso-symbol-5629_51796 {
    width: auto;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: row;
    align-items: flex-start;
}
.Pixso-instance-5629_50505 {
    width: 118px;
    height: 48px;
}
.Pixso-paragraph-5629_42601 {
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    width: auto;
    height: auto;
    flex-grow: 0;
}
.Pixso-instance-5629_50506 {
    width: 97px;
    height: 48px;
}
.Pixso-instance-5629_50507 {
    width: 101px;
    height: 48px;
}
.Pixso-instance-5629_50508 {
    width: 131px;
    height: 48px;
}
.Pixso-instance-5629_50509 {
    width: 120px;
    height: 48px;
}
.Pixso-paragraph-5629_42613 {
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    width: auto;
    height: auto;
    flex-grow: 0;
}
.Pixso-instance-5629_42614 {
    width: 28px;
    height: 24px;
}
.Pixso-symbol-5629_51793 {
    width: auto;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: row;
    align-items: flex-start;
}
.Pixso-instance-5629_51062 {
    width: 118px;
    height: 48px;
}
.Pixso-paragraph-5629_44456 {
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    width: auto;
    height: auto;
    flex-grow: 0;
}
.Pixso-instance-5629_51063 {
    width: 97px;
    height: 48px;
}
.Pixso-instance-5629_51064 {
    width: 101px;
    height: 48px;
}
.Pixso-instance-5629_51065 {
    width: 131px;
    height: 48px;
}
.Pixso-instance-5629_51066 {
    width: 120px;
    height: 48px;
}
.Pixso-paragraph-5629_44464 {
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    width: auto;
    height: auto;
    flex-grow: 0;
}
.Pixso-instance-5629_44465 {
    width: 28px;
    height: 24px;
}
.Pixso-symbol-5629_51790 {
    width: auto;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 4px;
    align-items: flex-start;
    padding: 4px 4px 4px 4px;
    border-radius: 24px 24px 24px 24px;
}
.Pixso-instance-5629_51194 {
    width: 111px;
    height: 36px;
}
.Pixso-instance-5629_51195 {
    width: 111px;
    height: 36px;
}
.Pixso-instance-5629_51196 {
    width: 111px;
    height: 36px;
}
.Pixso-instance-5629_51197 {
    width: 111px;
    height: 36px;
}
.Pixso-instance-5629_51198 {
    width: 111px;
    height: 36px;
}
.Pixso-symbol-5629_51788 {
    width: auto;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 6px;
    align-items: flex-start;
    padding: 4px 4px 4px 4px;
    border-radius: 28px 28px 28px 28px;
}
.Pixso-instance-5629_51200 {
    width: 119px;
    height: 40px;
}
.Pixso-instance-5629_51201 {
    width: 119px;
    height: 40px;
}
.Pixso-instance-5629_51202 {
    width: 119px;
    height: 40px;
}
.Pixso-instance-5629_51203 {
    width: 119px;
    height: 40px;
}
.Pixso-instance-5629_51204 {
    width: 119px;
    height: 40px;
}
.Pixso-symbol-5629_51787 {
    width: auto;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 8px;
    align-items: flex-start;
    padding: 4px 4px 4px 4px;
    border-radius: 28px 28px 28px 28px;
}
.Pixso-instance-5629_51206 {
    width: 131px;
    height: 48px;
}
.Pixso-instance-5629_51207 {
    width: 131px;
    height: 48px;
}
.Pixso-instance-5629_51208 {
    width: 131px;
    height: 48px;
}
.Pixso-instance-5629_51209 {
    width: 131px;
    height: 48px;
}
.Pixso-instance-5629_51210 {
    width: 131px;
    height: 48px;
}
.Pixso-symbol-5629_51785 {
    width: auto;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 4px;
    align-items: flex-start;
}
.Pixso-instance-5629_51212 {
    width: 111px;
    height: 36px;
}
.Pixso-instance-5629_51213 {
    width: 111px;
    height: 36px;
}
.Pixso-instance-5629_51214 {
    width: 111px;
    height: 36px;
}
.Pixso-instance-5629_51215 {
    width: 111px;
    height: 36px;
}
.Pixso-instance-5629_51216 {
    width: 111px;
    height: 36px;
}
.Pixso-symbol-5629_51801 {
    width: auto;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 4px;
    align-items: flex-start;
}
.Pixso-instance-5629_51218 {
    width: 111px;
    height: 36px;
}
.Pixso-instance-5629_51219 {
    width: 111px;
    height: 36px;
}
.Pixso-instance-5629_51220 {
    width: 111px;
    height: 36px;
}
.Pixso-instance-5629_51221 {
    width: 111px;
    height: 36px;
}
.Pixso-instance-5629_51222 {
    width: 111px;
    height: 36px;
}
.Pixso-symbol-5629_51797 {
    width: auto;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
}
.Pixso-instance-5629_51230 {
    width: 111px;
    height: 36px;
}
.Pixso-instance-5629_51231 {
    width: 111px;
    height: 36px;
}
.Pixso-instance-5629_51232 {
    width: 111px;
    height: 36px;
}
.Pixso-instance-5629_51233 {
    width: 111px;
    height: 36px;
}
.Pixso-instance-5629_51234 {
    width: 111px;
    height: 36px;
}
.Pixso-symbol-5629_51792 {
    width: auto;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 6px;
    align-items: flex-start;
}
.Pixso-instance-5629_51236 {
    width: 119px;
    height: 40px;
}
.Pixso-instance-5629_51237 {
    width: 119px;
    height: 40px;
}
.Pixso-instance-5629_51238 {
    width: 119px;
    height: 40px;
}
.Pixso-instance-5629_51239 {
    width: 119px;
    height: 40px;
}
.Pixso-instance-5629_51240 {
    width: 119px;
    height: 40px;
}
.Pixso-symbol-5629_51786 {
    width: auto;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 6px;
    align-items: flex-start;
}
.Pixso-instance-5629_51242 {
    width: 119px;
    height: 40px;
}
.Pixso-instance-5629_51243 {
    width: 119px;
    height: 40px;
}
.Pixso-instance-5629_51244 {
    width: 119px;
    height: 40px;
}
.Pixso-instance-5629_51245 {
    width: 119px;
    height: 40px;
}
.Pixso-instance-5629_51246 {
    width: 119px;
    height: 40px;
}
.Pixso-symbol-5629_51784 {
    width: auto;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 8px;
    align-items: flex-start;
}
.Pixso-instance-5629_51248 {
    width: 131px;
    height: 48px;
}
.Pixso-instance-5629_51249 {
    width: 131px;
    height: 48px;
}
.Pixso-instance-5629_51250 {
    width: 131px;
    height: 48px;
}
.Pixso-instance-5629_51251 {
    width: 131px;
    height: 48px;
}
.Pixso-instance-5629_51252 {
    width: 131px;
    height: 48px;
}
.Pixso-symbol-5629_51789 {
    width: auto;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
}
.Pixso-instance-5629_51260 {
    width: 119px;
    height: 40px;
}
.Pixso-instance-5629_51261 {
    width: 119px;
    height: 40px;
}
.Pixso-instance-5629_51262 {
    width: 119px;
    height: 40px;
}
.Pixso-instance-5629_51263 {
    width: 119px;
    height: 40px;
}
.Pixso-instance-5629_51264 {
    width: 119px;
    height: 40px;
}
.Pixso-symbol-5629_51791 {
    width: auto;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 8px;
    align-items: flex-start;
}
.Pixso-instance-5629_51266 {
    width: 131px;
    height: 48px;
}
.Pixso-instance-5629_51267 {
    width: 131px;
    height: 48px;
}
.Pixso-instance-5629_51268 {
    width: 131px;
    height: 48px;
}
.Pixso-instance-5629_51269 {
    width: 131px;
    height: 48px;
}
.Pixso-instance-5629_51270 {
    width: 131px;
    height: 48px;
}
.Pixso-symbol-5629_51799 {
    width: auto;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
}
.Pixso-instance-5629_51278 {
    width: 131px;
    height: 48px;
}
.Pixso-instance-5629_51279 {
    width: 131px;
    height: 48px;
}
.Pixso-instance-5629_51280 {
    width: 131px;
    height: 48px;
}
.Pixso-instance-5629_51281 {
    width: 131px;
    height: 48px;
}
.Pixso-instance-5629_51282 {
    width: 131px;
    height: 48px;
}

.Pixso-instance-5629_47594
    .Pixso-instance-5629_43322
    .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_47594 .Pixso-instance-5629_43322 .Pixso-frame-5588_11360 {
    width: 44px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_47594
    .Pixso-instance-5629_43322
    .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_47594
    .Pixso-instance-5629_43322
    .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_47594
    .Pixso-instance-5629_43322
    .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_47594 .Pixso-paragraph-5629_43321 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_47684 .Pixso-paragraph-5629_43321 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_47684
    .Pixso-instance-5629_43322
    .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_47684 .Pixso-instance-5629_43322 .Pixso-frame-5588_11360 {
    width: 44px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_47684
    .Pixso-instance-5629_43322
    .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_47684
    .Pixso-instance-5629_43322
    .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_47684
    .Pixso-instance-5629_43322
    .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_47694 .Pixso-paragraph-5629_43321 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_47694
    .Pixso-instance-5629_43322
    .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_47694 .Pixso-instance-5629_43322 .Pixso-frame-5588_11360 {
    width: 44px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_47694
    .Pixso-instance-5629_43322
    .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_47694
    .Pixso-instance-5629_43322
    .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_47694
    .Pixso-instance-5629_43322
    .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_47704 .Pixso-paragraph-5629_43321 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_47704
    .Pixso-instance-5629_43322
    .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_47704 .Pixso-instance-5629_43322 .Pixso-frame-5588_11360 {
    width: 44px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_47704
    .Pixso-instance-5629_43322
    .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_47704
    .Pixso-instance-5629_43322
    .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_47704
    .Pixso-instance-5629_43322
    .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_47714
    .Pixso-instance-5629_43713
    .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_47714 .Pixso-instance-5629_43713 .Pixso-frame-5588_11360 {
    width: 44px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_47714
    .Pixso-instance-5629_43713
    .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_47714
    .Pixso-instance-5629_43713
    .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_47714
    .Pixso-instance-5629_43713
    .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_47714 .Pixso-paragraph-5629_43712 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
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
.Pixso-instance-5629_47714 .Pixso-instance-5629_43713 {
    width: 24px;
    height: 20px;
}
.Pixso-instance-5629_43713 .Pixso-instance-5629_43713 {
    width: 24px;
    height: 20px;
}
.Pixso-instance-5629_47760
    .Pixso-instance-5629_41092
    .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_47760 .Pixso-instance-5629_41092 .Pixso-frame-5588_11360 {
    width: 44px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_47760
    .Pixso-instance-5629_41092
    .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_47760
    .Pixso-instance-5629_41092
    .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_47760
    .Pixso-instance-5629_41092
    .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_47760 .Pixso-paragraph-5558_51586 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_47761
    .Pixso-instance-5629_41092
    .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_47761 .Pixso-instance-5629_41092 .Pixso-frame-5588_11360 {
    width: 44px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_47761
    .Pixso-instance-5629_41092
    .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_47761
    .Pixso-instance-5629_41092
    .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_47761
    .Pixso-instance-5629_41092
    .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_47761 .Pixso-paragraph-5558_51586 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_47762
    .Pixso-instance-5629_41092
    .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_47762 .Pixso-instance-5629_41092 .Pixso-frame-5588_11360 {
    width: 44px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_47762
    .Pixso-instance-5629_41092
    .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_47762
    .Pixso-instance-5629_41092
    .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_47762
    .Pixso-instance-5629_41092
    .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_47762 .Pixso-paragraph-5558_51586 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_47763
    .Pixso-instance-5629_41092
    .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_47763 .Pixso-instance-5629_41092 .Pixso-frame-5588_11360 {
    width: 44px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_47763
    .Pixso-instance-5629_41092
    .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_47763
    .Pixso-instance-5629_41092
    .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_47763
    .Pixso-instance-5629_41092
    .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_47763 .Pixso-paragraph-5558_51586 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_47764
    .Pixso-instance-5629_41263
    .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_47764 .Pixso-instance-5629_41263 .Pixso-frame-5588_11360 {
    width: 44px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_47764
    .Pixso-instance-5629_41263
    .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_47764
    .Pixso-instance-5629_41263
    .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_47764
    .Pixso-instance-5629_41263
    .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_47764 .Pixso-paragraph-5629_41262 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
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
.Pixso-instance-5629_47764 .Pixso-instance-5629_41263 {
    width: 28px;
    height: 24px;
}
.Pixso-instance-5629_41263 .Pixso-instance-5629_41263 {
    width: 28px;
    height: 24px;
}
.Pixso-instance-5629_47808
    .Pixso-instance-5629_42116
    .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_47808 .Pixso-instance-5629_42116 .Pixso-frame-5588_11360 {
    width: 44px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_47808
    .Pixso-instance-5629_42116
    .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_47808
    .Pixso-instance-5629_42116
    .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_47808
    .Pixso-instance-5629_42116
    .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_47808 .Pixso-paragraph-5629_42115 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_47809 .Pixso-paragraph-5629_42115 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_47809
    .Pixso-instance-5629_42116
    .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_47809 .Pixso-instance-5629_42116 .Pixso-frame-5588_11360 {
    width: 44px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_47809
    .Pixso-instance-5629_42116
    .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_47809
    .Pixso-instance-5629_42116
    .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_47809
    .Pixso-instance-5629_42116
    .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_47810 .Pixso-paragraph-5629_42115 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_47810
    .Pixso-instance-5629_42116
    .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_47810 .Pixso-instance-5629_42116 .Pixso-frame-5588_11360 {
    width: 44px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_47810
    .Pixso-instance-5629_42116
    .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_47810
    .Pixso-instance-5629_42116
    .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_47810
    .Pixso-instance-5629_42116
    .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_47811 .Pixso-paragraph-5629_42115 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_47811
    .Pixso-instance-5629_42116
    .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_47811 .Pixso-instance-5629_42116 .Pixso-frame-5588_11360 {
    width: 44px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_47811
    .Pixso-instance-5629_42116
    .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_47811
    .Pixso-instance-5629_42116
    .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_47811
    .Pixso-instance-5629_42116
    .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_47812
    .Pixso-instance-5629_42502
    .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_47812 .Pixso-instance-5629_42502 .Pixso-frame-5588_11360 {
    width: 44px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_47812
    .Pixso-instance-5629_42502
    .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_47812
    .Pixso-instance-5629_42502
    .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_47812
    .Pixso-instance-5629_42502
    .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_47812 .Pixso-paragraph-5629_42501 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
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
.Pixso-instance-5629_47812 .Pixso-instance-5629_42502 {
    width: 28px;
    height: 24px;
}
.Pixso-instance-5629_42502 .Pixso-instance-5629_42502 {
    width: 28px;
    height: 24px;
}
.Pixso-instance-5629_50493
    .Pixso-instance-5629_43813
    .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_50493 .Pixso-instance-5629_43813 .Pixso-frame-5588_11360 {
    width: 44px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_50493
    .Pixso-instance-5629_43813
    .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_50493
    .Pixso-instance-5629_43813
    .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_50493
    .Pixso-instance-5629_43813
    .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_50493 .Pixso-paragraph-5629_43812 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_50494 .Pixso-paragraph-5629_43812 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_50494
    .Pixso-instance-5629_43813
    .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_50494 .Pixso-instance-5629_43813 .Pixso-frame-5588_11360 {
    width: 44px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_50494
    .Pixso-instance-5629_43813
    .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_50494
    .Pixso-instance-5629_43813
    .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_50494
    .Pixso-instance-5629_43813
    .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_50495 .Pixso-paragraph-5629_43812 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_50495
    .Pixso-instance-5629_43813
    .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_50495 .Pixso-instance-5629_43813 .Pixso-frame-5588_11360 {
    width: 44px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_50495
    .Pixso-instance-5629_43813
    .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_50495
    .Pixso-instance-5629_43813
    .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_50495
    .Pixso-instance-5629_43813
    .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_50496 .Pixso-paragraph-5629_43812 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_50496
    .Pixso-instance-5629_43813
    .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_50496 .Pixso-instance-5629_43813 .Pixso-frame-5588_11360 {
    width: 44px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_50496
    .Pixso-instance-5629_43813
    .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_50496
    .Pixso-instance-5629_43813
    .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_50496
    .Pixso-instance-5629_43813
    .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_50497
    .Pixso-instance-5629_43825
    .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_50497 .Pixso-instance-5629_43825 .Pixso-frame-5588_11360 {
    width: 44px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_50497
    .Pixso-instance-5629_43825
    .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_50497
    .Pixso-instance-5629_43825
    .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_50497
    .Pixso-instance-5629_43825
    .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_50497
    .Pixso-instance-5629_43823
    .Pixso-vector-5579_152456 {
    width: 84.37%;
    height: 81.39%;
    background-image: url(@/assets/images/Vector48.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 5.16%;
    right: 10.47%;
    top: 5.2%;
    bottom: 13.41%;
}
.Pixso-instance-5629_50497 .Pixso-paragraph-5629_43824 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
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
.Pixso-instance-5629_50497 .Pixso-instance-5629_43825 {
    width: 24px;
    height: 20px;
}
.Pixso-instance-5629_43825 .Pixso-instance-5629_43825 {
    width: 24px;
    height: 20px;
}
.Pixso-instance-5629_50679
    .Pixso-instance-5629_43905
    .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_50679 .Pixso-instance-5629_43905 .Pixso-frame-5588_11360 {
    width: 44px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_50679
    .Pixso-instance-5629_43905
    .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_50679
    .Pixso-instance-5629_43905
    .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_50679
    .Pixso-instance-5629_43905
    .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_50679 .Pixso-paragraph-5629_43904 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_50680 .Pixso-paragraph-5629_43904 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_50680
    .Pixso-instance-5629_43905
    .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_50680 .Pixso-instance-5629_43905 .Pixso-frame-5588_11360 {
    width: 44px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_50680
    .Pixso-instance-5629_43905
    .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_50680
    .Pixso-instance-5629_43905
    .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_50680
    .Pixso-instance-5629_43905
    .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_50681 .Pixso-paragraph-5629_43904 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_50681
    .Pixso-instance-5629_43905
    .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_50681 .Pixso-instance-5629_43905 .Pixso-frame-5588_11360 {
    width: 44px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_50681
    .Pixso-instance-5629_43905
    .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_50681
    .Pixso-instance-5629_43905
    .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_50681
    .Pixso-instance-5629_43905
    .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_50682 .Pixso-paragraph-5629_43904 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_50682
    .Pixso-instance-5629_43905
    .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_50682 .Pixso-instance-5629_43905 .Pixso-frame-5588_11360 {
    width: 44px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_50682
    .Pixso-instance-5629_43905
    .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_50682
    .Pixso-instance-5629_43905
    .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_50682
    .Pixso-instance-5629_43905
    .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_50683
    .Pixso-instance-5629_43917
    .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_50683 .Pixso-instance-5629_43917 .Pixso-frame-5588_11360 {
    width: 44px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_50683
    .Pixso-instance-5629_43917
    .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_50683
    .Pixso-instance-5629_43917
    .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_50683
    .Pixso-instance-5629_43917
    .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_50683 .Pixso-paragraph-5629_43916 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
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
.Pixso-instance-5629_50683 .Pixso-instance-5629_43917 {
    width: 24px;
    height: 20px;
}
.Pixso-instance-5629_43917 .Pixso-instance-5629_43917 {
    width: 24px;
    height: 20px;
}
.Pixso-instance-5629_51050
    .Pixso-instance-5629_44273
    .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51050 .Pixso-instance-5629_44273 .Pixso-frame-5588_11360 {
    width: 44px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_51050
    .Pixso-instance-5629_44273
    .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_51050
    .Pixso-instance-5629_44273
    .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_51050
    .Pixso-instance-5629_44273
    .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51050 .Pixso-paragraph-5629_44272 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_51051 .Pixso-paragraph-5629_44272 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_51051
    .Pixso-instance-5629_44273
    .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51051 .Pixso-instance-5629_44273 .Pixso-frame-5588_11360 {
    width: 44px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_51051
    .Pixso-instance-5629_44273
    .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_51051
    .Pixso-instance-5629_44273
    .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_51051
    .Pixso-instance-5629_44273
    .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51052 .Pixso-paragraph-5629_44272 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_51052
    .Pixso-instance-5629_44273
    .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51052 .Pixso-instance-5629_44273 .Pixso-frame-5588_11360 {
    width: 44px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_51052
    .Pixso-instance-5629_44273
    .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_51052
    .Pixso-instance-5629_44273
    .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_51052
    .Pixso-instance-5629_44273
    .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51053 .Pixso-paragraph-5629_44272 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_51053
    .Pixso-instance-5629_44273
    .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51053 .Pixso-instance-5629_44273 .Pixso-frame-5588_11360 {
    width: 44px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_51053
    .Pixso-instance-5629_44273
    .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_51053
    .Pixso-instance-5629_44273
    .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_51053
    .Pixso-instance-5629_44273
    .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51054
    .Pixso-instance-5629_44281
    .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51054 .Pixso-instance-5629_44281 .Pixso-frame-5588_11360 {
    width: 44px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_51054
    .Pixso-instance-5629_44281
    .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_51054
    .Pixso-instance-5629_44281
    .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_51054
    .Pixso-instance-5629_44281
    .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51054 .Pixso-paragraph-5629_44280 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
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
.Pixso-instance-5629_51054 .Pixso-instance-5629_44281 {
    width: 24px;
    height: 20px;
}
.Pixso-instance-5629_44281 .Pixso-instance-5629_44281 {
    width: 24px;
    height: 20px;
}
.Pixso-instance-5629_50685
    .Pixso-instance-5629_41456
    .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_50685 .Pixso-instance-5629_41456 .Pixso-frame-5588_11360 {
    width: 44px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_50685
    .Pixso-instance-5629_41456
    .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_50685
    .Pixso-instance-5629_41456
    .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_50685
    .Pixso-instance-5629_41456
    .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_50685 .Pixso-paragraph-5629_41455 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_50686
    .Pixso-instance-5629_41456
    .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_50686 .Pixso-instance-5629_41456 .Pixso-frame-5588_11360 {
    width: 44px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_50686
    .Pixso-instance-5629_41456
    .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_50686
    .Pixso-instance-5629_41456
    .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_50686
    .Pixso-instance-5629_41456
    .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_50686 .Pixso-paragraph-5629_41455 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_50687
    .Pixso-instance-5629_41456
    .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_50687 .Pixso-instance-5629_41456 .Pixso-frame-5588_11360 {
    width: 44px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_50687
    .Pixso-instance-5629_41456
    .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_50687
    .Pixso-instance-5629_41456
    .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_50687
    .Pixso-instance-5629_41456
    .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_50687 .Pixso-paragraph-5629_41455 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_50688
    .Pixso-instance-5629_41456
    .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_50688 .Pixso-instance-5629_41456 .Pixso-frame-5588_11360 {
    width: 44px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_50688
    .Pixso-instance-5629_41456
    .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_50688
    .Pixso-instance-5629_41456
    .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_50688
    .Pixso-instance-5629_41456
    .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_50688 .Pixso-paragraph-5629_41455 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_50689
    .Pixso-instance-5629_41464
    .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_50689 .Pixso-instance-5629_41464 .Pixso-frame-5588_11360 {
    width: 44px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_50689
    .Pixso-instance-5629_41464
    .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_50689
    .Pixso-instance-5629_41464
    .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_50689
    .Pixso-instance-5629_41464
    .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_50689 .Pixso-instance-5629_41464 {
    width: 28px;
    height: 24px;
}
.Pixso-instance-5629_50689 .Pixso-paragraph-5629_41463 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
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
.Pixso-instance-5629_41464 .Pixso-instance-5629_41464 {
    width: 28px;
    height: 24px;
}
.Pixso-instance-5629_50499
    .Pixso-instance-5629_41548
    .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_50499 .Pixso-instance-5629_41548 .Pixso-frame-5588_11360 {
    width: 44px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_50499
    .Pixso-instance-5629_41548
    .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_50499
    .Pixso-instance-5629_41548
    .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_50499
    .Pixso-instance-5629_41548
    .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_50499 .Pixso-paragraph-5629_41547 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_50500
    .Pixso-instance-5629_41548
    .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_50500 .Pixso-instance-5629_41548 .Pixso-frame-5588_11360 {
    width: 44px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_50500
    .Pixso-instance-5629_41548
    .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_50500
    .Pixso-instance-5629_41548
    .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_50500
    .Pixso-instance-5629_41548
    .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_50500 .Pixso-paragraph-5629_41547 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_50501
    .Pixso-instance-5629_41548
    .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_50501 .Pixso-instance-5629_41548 .Pixso-frame-5588_11360 {
    width: 44px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_50501
    .Pixso-instance-5629_41548
    .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_50501
    .Pixso-instance-5629_41548
    .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_50501
    .Pixso-instance-5629_41548
    .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_50501 .Pixso-paragraph-5629_41547 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_50502
    .Pixso-instance-5629_41548
    .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_50502 .Pixso-instance-5629_41548 .Pixso-frame-5588_11360 {
    width: 44px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_50502
    .Pixso-instance-5629_41548
    .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_50502
    .Pixso-instance-5629_41548
    .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_50502
    .Pixso-instance-5629_41548
    .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_50502 .Pixso-paragraph-5629_41547 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_50503
    .Pixso-instance-5629_41556
    .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_50503 .Pixso-instance-5629_41556 .Pixso-frame-5588_11360 {
    width: 44px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_50503
    .Pixso-instance-5629_41556
    .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_50503
    .Pixso-instance-5629_41556
    .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_50503
    .Pixso-instance-5629_41556
    .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_50503 .Pixso-paragraph-5629_41555 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
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
.Pixso-instance-5629_50503 .Pixso-instance-5629_41556 {
    width: 28px;
    height: 24px;
}
.Pixso-instance-5629_41556 .Pixso-instance-5629_41556 {
    width: 28px;
    height: 24px;
}
.Pixso-instance-5629_50691
    .Pixso-instance-5629_42694
    .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_50691 .Pixso-instance-5629_42694 .Pixso-frame-5588_11360 {
    width: 44px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_50691
    .Pixso-instance-5629_42694
    .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_50691
    .Pixso-instance-5629_42694
    .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_50691
    .Pixso-instance-5629_42694
    .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_50691 .Pixso-paragraph-5629_42693 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_50692 .Pixso-paragraph-5629_42693 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_50692
    .Pixso-instance-5629_42694
    .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_50692 .Pixso-instance-5629_42694 .Pixso-frame-5588_11360 {
    width: 44px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_50692
    .Pixso-instance-5629_42694
    .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_50692
    .Pixso-instance-5629_42694
    .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_50692
    .Pixso-instance-5629_42694
    .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_50693 .Pixso-paragraph-5629_42693 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_50693
    .Pixso-instance-5629_42694
    .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_50693 .Pixso-instance-5629_42694 .Pixso-frame-5588_11360 {
    width: 44px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_50693
    .Pixso-instance-5629_42694
    .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_50693
    .Pixso-instance-5629_42694
    .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_50693
    .Pixso-instance-5629_42694
    .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_50694 .Pixso-paragraph-5629_42693 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_50694
    .Pixso-instance-5629_42694
    .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_50694 .Pixso-instance-5629_42694 .Pixso-frame-5588_11360 {
    width: 44px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_50694
    .Pixso-instance-5629_42694
    .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_50694
    .Pixso-instance-5629_42694
    .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_50694
    .Pixso-instance-5629_42694
    .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_50695
    .Pixso-instance-5629_42706
    .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_50695 .Pixso-instance-5629_42706 .Pixso-frame-5588_11360 {
    width: 44px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_50695
    .Pixso-instance-5629_42706
    .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_50695
    .Pixso-instance-5629_42706
    .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_50695
    .Pixso-instance-5629_42706
    .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_50695 .Pixso-paragraph-5629_42705 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
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
.Pixso-instance-5629_50695 .Pixso-instance-5629_42706 {
    width: 28px;
    height: 24px;
}
.Pixso-instance-5629_42706 .Pixso-instance-5629_42706 {
    width: 28px;
    height: 24px;
}
.Pixso-instance-5629_51056
    .Pixso-instance-5629_44355
    .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51056 .Pixso-instance-5629_44355 .Pixso-frame-5588_11360 {
    width: 44px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_51056
    .Pixso-instance-5629_44355
    .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_51056
    .Pixso-instance-5629_44355
    .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_51056
    .Pixso-instance-5629_44355
    .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51056 .Pixso-paragraph-5629_44354 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_51057
    .Pixso-instance-5629_44355
    .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51057 .Pixso-instance-5629_44355 .Pixso-frame-5588_11360 {
    width: 44px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_51057
    .Pixso-instance-5629_44355
    .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_51057
    .Pixso-instance-5629_44355
    .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_51057
    .Pixso-instance-5629_44355
    .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51057 .Pixso-paragraph-5629_44354 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_51058
    .Pixso-instance-5629_44355
    .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51058 .Pixso-instance-5629_44355 .Pixso-frame-5588_11360 {
    width: 44px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_51058
    .Pixso-instance-5629_44355
    .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_51058
    .Pixso-instance-5629_44355
    .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_51058
    .Pixso-instance-5629_44355
    .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51058 .Pixso-paragraph-5629_44354 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_51059
    .Pixso-instance-5629_44355
    .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51059 .Pixso-instance-5629_44355 .Pixso-frame-5588_11360 {
    width: 44px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_51059
    .Pixso-instance-5629_44355
    .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_51059
    .Pixso-instance-5629_44355
    .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_51059
    .Pixso-instance-5629_44355
    .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51059 .Pixso-paragraph-5629_44354 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_51060
    .Pixso-instance-5629_44363
    .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51060 .Pixso-instance-5629_44363 .Pixso-frame-5588_11360 {
    width: 44px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_51060
    .Pixso-instance-5629_44363
    .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_51060
    .Pixso-instance-5629_44363
    .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_51060
    .Pixso-instance-5629_44363
    .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51060 .Pixso-paragraph-5629_44362 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
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
.Pixso-instance-5629_51060 .Pixso-instance-5629_44363 {
    width: 28px;
    height: 24px;
}
.Pixso-instance-5629_44363 .Pixso-instance-5629_44363 {
    width: 28px;
    height: 24px;
}
.Pixso-instance-5629_50505
    .Pixso-instance-5629_42602
    .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_50505 .Pixso-instance-5629_42602 .Pixso-frame-5588_11360 {
    width: 44px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_50505
    .Pixso-instance-5629_42602
    .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_50505
    .Pixso-instance-5629_42602
    .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_50505
    .Pixso-instance-5629_42602
    .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_50505 .Pixso-paragraph-5629_42601 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_50506 .Pixso-paragraph-5629_42601 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_50506
    .Pixso-instance-5629_42602
    .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_50506 .Pixso-instance-5629_42602 .Pixso-frame-5588_11360 {
    width: 44px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_50506
    .Pixso-instance-5629_42602
    .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_50506
    .Pixso-instance-5629_42602
    .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_50506
    .Pixso-instance-5629_42602
    .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_50507 .Pixso-paragraph-5629_42601 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_50507
    .Pixso-instance-5629_42602
    .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_50507 .Pixso-instance-5629_42602 .Pixso-frame-5588_11360 {
    width: 44px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_50507
    .Pixso-instance-5629_42602
    .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_50507
    .Pixso-instance-5629_42602
    .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_50507
    .Pixso-instance-5629_42602
    .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_50508 .Pixso-paragraph-5629_42601 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_50508
    .Pixso-instance-5629_42602
    .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_50508 .Pixso-instance-5629_42602 .Pixso-frame-5588_11360 {
    width: 44px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_50508
    .Pixso-instance-5629_42602
    .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_50508
    .Pixso-instance-5629_42602
    .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_50508
    .Pixso-instance-5629_42602
    .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_50509
    .Pixso-instance-5629_42614
    .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_50509 .Pixso-instance-5629_42614 .Pixso-frame-5588_11360 {
    width: 44px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_50509
    .Pixso-instance-5629_42614
    .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_50509
    .Pixso-instance-5629_42614
    .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_50509
    .Pixso-instance-5629_42614
    .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_50509 .Pixso-paragraph-5629_42613 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
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
.Pixso-instance-5629_50509 .Pixso-instance-5629_42614 {
    width: 28px;
    height: 24px;
}
.Pixso-instance-5629_42614 .Pixso-instance-5629_42614 {
    width: 28px;
    height: 24px;
}
.Pixso-instance-5629_51062
    .Pixso-instance-5629_44457
    .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51062 .Pixso-instance-5629_44457 .Pixso-frame-5588_11360 {
    width: 44px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_51062
    .Pixso-instance-5629_44457
    .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_51062
    .Pixso-instance-5629_44457
    .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_51062
    .Pixso-instance-5629_44457
    .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51062 .Pixso-paragraph-5629_44456 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_51063 .Pixso-paragraph-5629_44456 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_51063
    .Pixso-instance-5629_44457
    .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51063 .Pixso-instance-5629_44457 .Pixso-frame-5588_11360 {
    width: 44px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_51063
    .Pixso-instance-5629_44457
    .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_51063
    .Pixso-instance-5629_44457
    .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_51063
    .Pixso-instance-5629_44457
    .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51064 .Pixso-paragraph-5629_44456 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_51064
    .Pixso-instance-5629_44457
    .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51064 .Pixso-instance-5629_44457 .Pixso-frame-5588_11360 {
    width: 44px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_51064
    .Pixso-instance-5629_44457
    .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_51064
    .Pixso-instance-5629_44457
    .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_51064
    .Pixso-instance-5629_44457
    .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51065 .Pixso-paragraph-5629_44456 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_51065
    .Pixso-instance-5629_44457
    .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51065 .Pixso-instance-5629_44457 .Pixso-frame-5588_11360 {
    width: 44px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_51065
    .Pixso-instance-5629_44457
    .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_51065
    .Pixso-instance-5629_44457
    .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_51065
    .Pixso-instance-5629_44457
    .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51066
    .Pixso-instance-5629_44465
    .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51066 .Pixso-instance-5629_44465 .Pixso-frame-5588_11360 {
    width: 44px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_51066
    .Pixso-instance-5629_44465
    .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_51066
    .Pixso-instance-5629_44465
    .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_51066
    .Pixso-instance-5629_44465
    .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51066 .Pixso-paragraph-5629_44464 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
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
.Pixso-instance-5629_51066 .Pixso-instance-5629_44465 {
    width: 28px;
    height: 24px;
}
.Pixso-instance-5629_44465 .Pixso-instance-5629_44465 {
    width: 28px;
    height: 24px;
}
.Pixso-instance-5629_51194 .Pixso-paragraph-5629_43321 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_51194
    .Pixso-instance-5629_43322
    .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51194 .Pixso-instance-5629_43322 .Pixso-frame-5588_11360 {
    width: 44px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_51194
    .Pixso-instance-5629_43322
    .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_51194
    .Pixso-instance-5629_43322
    .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_51194
    .Pixso-instance-5629_43322
    .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51195 .Pixso-paragraph-5629_43321 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_51195
    .Pixso-instance-5629_43322
    .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51195 .Pixso-instance-5629_43322 .Pixso-frame-5588_11360 {
    width: 44px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_51195
    .Pixso-instance-5629_43322
    .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_51195
    .Pixso-instance-5629_43322
    .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_51195
    .Pixso-instance-5629_43322
    .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51196 .Pixso-paragraph-5629_43321 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_51196
    .Pixso-instance-5629_43322
    .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51196 .Pixso-instance-5629_43322 .Pixso-frame-5588_11360 {
    width: 44px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_51196
    .Pixso-instance-5629_43322
    .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_51196
    .Pixso-instance-5629_43322
    .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_51196
    .Pixso-instance-5629_43322
    .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51197 .Pixso-paragraph-5629_43321 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_51197
    .Pixso-instance-5629_43322
    .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51197 .Pixso-instance-5629_43322 .Pixso-frame-5588_11360 {
    width: 44px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_51197
    .Pixso-instance-5629_43322
    .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_51197
    .Pixso-instance-5629_43322
    .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_51197
    .Pixso-instance-5629_43322
    .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51198 .Pixso-paragraph-5629_43712 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_51198 .Pixso-instance-5629_43713 {
    width: 24px;
    height: 20px;
}
.Pixso-instance-5629_51198
    .Pixso-instance-5629_43713
    .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51198 .Pixso-instance-5629_43713 .Pixso-frame-5588_11360 {
    width: 44px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_51198
    .Pixso-instance-5629_43713
    .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_51198
    .Pixso-instance-5629_43713
    .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_51198
    .Pixso-instance-5629_43713
    .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51200
    .Pixso-instance-5629_41092
    .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51200 .Pixso-instance-5629_41092 .Pixso-frame-5588_11360 {
    width: 44px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_51200
    .Pixso-instance-5629_41092
    .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_51200
    .Pixso-instance-5629_41092
    .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_51200
    .Pixso-instance-5629_41092
    .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51200 .Pixso-paragraph-5558_51586 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_51201
    .Pixso-instance-5629_41092
    .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51201 .Pixso-instance-5629_41092 .Pixso-frame-5588_11360 {
    width: 44px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_51201
    .Pixso-instance-5629_41092
    .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_51201
    .Pixso-instance-5629_41092
    .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_51201
    .Pixso-instance-5629_41092
    .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51201 .Pixso-paragraph-5558_51586 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_51202
    .Pixso-instance-5629_41092
    .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51202 .Pixso-instance-5629_41092 .Pixso-frame-5588_11360 {
    width: 44px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_51202
    .Pixso-instance-5629_41092
    .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_51202
    .Pixso-instance-5629_41092
    .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_51202
    .Pixso-instance-5629_41092
    .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51202 .Pixso-paragraph-5558_51586 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_51203
    .Pixso-instance-5629_41092
    .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51203 .Pixso-instance-5629_41092 .Pixso-frame-5588_11360 {
    width: 44px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_51203
    .Pixso-instance-5629_41092
    .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_51203
    .Pixso-instance-5629_41092
    .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_51203
    .Pixso-instance-5629_41092
    .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51203 .Pixso-paragraph-5558_51586 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_51204
    .Pixso-instance-5629_41263
    .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51204 .Pixso-instance-5629_41263 .Pixso-frame-5588_11360 {
    width: 44px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_51204
    .Pixso-instance-5629_41263
    .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_51204
    .Pixso-instance-5629_41263
    .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_51204
    .Pixso-instance-5629_41263
    .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51204 .Pixso-paragraph-5629_41262 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_51204 .Pixso-instance-5629_41263 {
    width: 28px;
    height: 24px;
}
.Pixso-instance-5629_51206 .Pixso-paragraph-5629_42115 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_51206
    .Pixso-instance-5629_42116
    .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51206 .Pixso-instance-5629_42116 .Pixso-frame-5588_11360 {
    width: 44px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_51206
    .Pixso-instance-5629_42116
    .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_51206
    .Pixso-instance-5629_42116
    .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_51206
    .Pixso-instance-5629_42116
    .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51207 .Pixso-paragraph-5629_42115 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_51207
    .Pixso-instance-5629_42116
    .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51207 .Pixso-instance-5629_42116 .Pixso-frame-5588_11360 {
    width: 44px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_51207
    .Pixso-instance-5629_42116
    .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_51207
    .Pixso-instance-5629_42116
    .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_51207
    .Pixso-instance-5629_42116
    .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51208 .Pixso-paragraph-5629_42115 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_51208
    .Pixso-instance-5629_42116
    .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51208 .Pixso-instance-5629_42116 .Pixso-frame-5588_11360 {
    width: 44px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_51208
    .Pixso-instance-5629_42116
    .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_51208
    .Pixso-instance-5629_42116
    .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_51208
    .Pixso-instance-5629_42116
    .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51209 .Pixso-paragraph-5629_42115 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_51209
    .Pixso-instance-5629_42116
    .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51209 .Pixso-instance-5629_42116 .Pixso-frame-5588_11360 {
    width: 44px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_51209
    .Pixso-instance-5629_42116
    .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_51209
    .Pixso-instance-5629_42116
    .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_51209
    .Pixso-instance-5629_42116
    .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51210 .Pixso-paragraph-5629_42501 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_51210 .Pixso-instance-5629_42502 {
    width: 28px;
    height: 24px;
}
.Pixso-instance-5629_51210
    .Pixso-instance-5629_42502
    .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51210 .Pixso-instance-5629_42502 .Pixso-frame-5588_11360 {
    width: 44px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_51210
    .Pixso-instance-5629_42502
    .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_51210
    .Pixso-instance-5629_42502
    .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_51210
    .Pixso-instance-5629_42502
    .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51212 .Pixso-paragraph-5629_43812 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_51212
    .Pixso-instance-5629_43813
    .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51212 .Pixso-instance-5629_43813 .Pixso-frame-5588_11360 {
    width: 44px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_51212
    .Pixso-instance-5629_43813
    .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_51212
    .Pixso-instance-5629_43813
    .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_51212
    .Pixso-instance-5629_43813
    .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51213 .Pixso-paragraph-5629_43812 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_51213
    .Pixso-instance-5629_43813
    .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51213 .Pixso-instance-5629_43813 .Pixso-frame-5588_11360 {
    width: 44px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_51213
    .Pixso-instance-5629_43813
    .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_51213
    .Pixso-instance-5629_43813
    .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_51213
    .Pixso-instance-5629_43813
    .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51214 .Pixso-paragraph-5629_43812 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_51214
    .Pixso-instance-5629_43813
    .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51214 .Pixso-instance-5629_43813 .Pixso-frame-5588_11360 {
    width: 44px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_51214
    .Pixso-instance-5629_43813
    .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_51214
    .Pixso-instance-5629_43813
    .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_51214
    .Pixso-instance-5629_43813
    .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51215 .Pixso-paragraph-5629_43812 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_51215
    .Pixso-instance-5629_43813
    .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51215 .Pixso-instance-5629_43813 .Pixso-frame-5588_11360 {
    width: 44px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_51215
    .Pixso-instance-5629_43813
    .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_51215
    .Pixso-instance-5629_43813
    .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_51215
    .Pixso-instance-5629_43813
    .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51216 .Pixso-paragraph-5629_43824 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_51216 .Pixso-instance-5629_43825 {
    width: 24px;
    height: 20px;
}
.Pixso-instance-5629_51216
    .Pixso-instance-5629_43825
    .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51216 .Pixso-instance-5629_43825 .Pixso-frame-5588_11360 {
    width: 44px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_51216
    .Pixso-instance-5629_43825
    .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_51216
    .Pixso-instance-5629_43825
    .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_51216
    .Pixso-instance-5629_43825
    .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51218 .Pixso-paragraph-5629_43904 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_51218
    .Pixso-instance-5629_43905
    .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51218 .Pixso-instance-5629_43905 .Pixso-frame-5588_11360 {
    width: 44px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_51218
    .Pixso-instance-5629_43905
    .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_51218
    .Pixso-instance-5629_43905
    .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_51218
    .Pixso-instance-5629_43905
    .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51219 .Pixso-paragraph-5629_43904 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_51219
    .Pixso-instance-5629_43905
    .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51219 .Pixso-instance-5629_43905 .Pixso-frame-5588_11360 {
    width: 44px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_51219
    .Pixso-instance-5629_43905
    .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_51219
    .Pixso-instance-5629_43905
    .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_51219
    .Pixso-instance-5629_43905
    .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51220 .Pixso-paragraph-5629_43904 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_51220
    .Pixso-instance-5629_43905
    .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51220 .Pixso-instance-5629_43905 .Pixso-frame-5588_11360 {
    width: 44px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_51220
    .Pixso-instance-5629_43905
    .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_51220
    .Pixso-instance-5629_43905
    .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_51220
    .Pixso-instance-5629_43905
    .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51221 .Pixso-paragraph-5629_43904 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_51221
    .Pixso-instance-5629_43905
    .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51221 .Pixso-instance-5629_43905 .Pixso-frame-5588_11360 {
    width: 44px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_51221
    .Pixso-instance-5629_43905
    .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_51221
    .Pixso-instance-5629_43905
    .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_51221
    .Pixso-instance-5629_43905
    .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51222 .Pixso-paragraph-5629_43916 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_51222 .Pixso-instance-5629_43917 {
    width: 24px;
    height: 20px;
}
.Pixso-instance-5629_51222
    .Pixso-instance-5629_43917
    .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51222 .Pixso-instance-5629_43917 .Pixso-frame-5588_11360 {
    width: 44px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_51222
    .Pixso-instance-5629_43917
    .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_51222
    .Pixso-instance-5629_43917
    .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_51222
    .Pixso-instance-5629_43917
    .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51230 .Pixso-paragraph-5629_44272 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_51230
    .Pixso-instance-5629_44273
    .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51230 .Pixso-instance-5629_44273 .Pixso-frame-5588_11360 {
    width: 44px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_51230
    .Pixso-instance-5629_44273
    .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_51230
    .Pixso-instance-5629_44273
    .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_51230
    .Pixso-instance-5629_44273
    .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51231 .Pixso-paragraph-5629_44272 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_51231
    .Pixso-instance-5629_44273
    .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51231 .Pixso-instance-5629_44273 .Pixso-frame-5588_11360 {
    width: 44px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_51231
    .Pixso-instance-5629_44273
    .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_51231
    .Pixso-instance-5629_44273
    .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_51231
    .Pixso-instance-5629_44273
    .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51232 .Pixso-paragraph-5629_44272 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_51232
    .Pixso-instance-5629_44273
    .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51232 .Pixso-instance-5629_44273 .Pixso-frame-5588_11360 {
    width: 44px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_51232
    .Pixso-instance-5629_44273
    .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_51232
    .Pixso-instance-5629_44273
    .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_51232
    .Pixso-instance-5629_44273
    .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51233 .Pixso-paragraph-5629_44272 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_51233
    .Pixso-instance-5629_44273
    .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51233 .Pixso-instance-5629_44273 .Pixso-frame-5588_11360 {
    width: 44px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_51233
    .Pixso-instance-5629_44273
    .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_51233
    .Pixso-instance-5629_44273
    .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_51233
    .Pixso-instance-5629_44273
    .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51234 .Pixso-paragraph-5629_44280 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_51234 .Pixso-instance-5629_44281 {
    width: 24px;
    height: 20px;
}
.Pixso-instance-5629_51234
    .Pixso-instance-5629_44281
    .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51234 .Pixso-instance-5629_44281 .Pixso-frame-5588_11360 {
    width: 44px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_51234
    .Pixso-instance-5629_44281
    .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_51234
    .Pixso-instance-5629_44281
    .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_51234
    .Pixso-instance-5629_44281
    .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51236
    .Pixso-instance-5629_41456
    .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51236 .Pixso-instance-5629_41456 .Pixso-frame-5588_11360 {
    width: 44px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_51236
    .Pixso-instance-5629_41456
    .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_51236
    .Pixso-instance-5629_41456
    .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_51236
    .Pixso-instance-5629_41456
    .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51236 .Pixso-paragraph-5629_41455 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_51237
    .Pixso-instance-5629_41456
    .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51237 .Pixso-instance-5629_41456 .Pixso-frame-5588_11360 {
    width: 44px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_51237
    .Pixso-instance-5629_41456
    .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_51237
    .Pixso-instance-5629_41456
    .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_51237
    .Pixso-instance-5629_41456
    .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51237 .Pixso-paragraph-5629_41455 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_51238
    .Pixso-instance-5629_41456
    .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51238 .Pixso-instance-5629_41456 .Pixso-frame-5588_11360 {
    width: 44px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_51238
    .Pixso-instance-5629_41456
    .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_51238
    .Pixso-instance-5629_41456
    .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_51238
    .Pixso-instance-5629_41456
    .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51238 .Pixso-paragraph-5629_41455 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_51239
    .Pixso-instance-5629_41456
    .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51239 .Pixso-instance-5629_41456 .Pixso-frame-5588_11360 {
    width: 44px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_51239
    .Pixso-instance-5629_41456
    .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_51239
    .Pixso-instance-5629_41456
    .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_51239
    .Pixso-instance-5629_41456
    .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51239 .Pixso-paragraph-5629_41455 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_51240
    .Pixso-instance-5629_41464
    .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51240 .Pixso-instance-5629_41464 .Pixso-frame-5588_11360 {
    width: 44px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_51240
    .Pixso-instance-5629_41464
    .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_51240
    .Pixso-instance-5629_41464
    .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_51240
    .Pixso-instance-5629_41464
    .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51240 .Pixso-paragraph-5629_41463 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_51240 .Pixso-instance-5629_41464 {
    width: 28px;
    height: 24px;
}
.Pixso-instance-5629_51242
    .Pixso-instance-5629_41548
    .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51242 .Pixso-instance-5629_41548 .Pixso-frame-5588_11360 {
    width: 44px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_51242
    .Pixso-instance-5629_41548
    .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_51242
    .Pixso-instance-5629_41548
    .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_51242
    .Pixso-instance-5629_41548
    .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51242 .Pixso-paragraph-5629_41547 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_51243
    .Pixso-instance-5629_41548
    .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51243 .Pixso-instance-5629_41548 .Pixso-frame-5588_11360 {
    width: 44px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_51243
    .Pixso-instance-5629_41548
    .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_51243
    .Pixso-instance-5629_41548
    .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_51243
    .Pixso-instance-5629_41548
    .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51243 .Pixso-paragraph-5629_41547 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_51244
    .Pixso-instance-5629_41548
    .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51244 .Pixso-instance-5629_41548 .Pixso-frame-5588_11360 {
    width: 44px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_51244
    .Pixso-instance-5629_41548
    .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_51244
    .Pixso-instance-5629_41548
    .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_51244
    .Pixso-instance-5629_41548
    .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51244 .Pixso-paragraph-5629_41547 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_51245
    .Pixso-instance-5629_41548
    .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51245 .Pixso-instance-5629_41548 .Pixso-frame-5588_11360 {
    width: 44px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_51245
    .Pixso-instance-5629_41548
    .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_51245
    .Pixso-instance-5629_41548
    .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_51245
    .Pixso-instance-5629_41548
    .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51245 .Pixso-paragraph-5629_41547 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_51246
    .Pixso-instance-5629_41556
    .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51246 .Pixso-instance-5629_41556 .Pixso-frame-5588_11360 {
    width: 44px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_51246
    .Pixso-instance-5629_41556
    .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_51246
    .Pixso-instance-5629_41556
    .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_51246
    .Pixso-instance-5629_41556
    .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51246 .Pixso-paragraph-5629_41555 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_51246 .Pixso-instance-5629_41556 {
    width: 28px;
    height: 24px;
}
.Pixso-instance-5629_51248 .Pixso-paragraph-5629_42693 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_51248
    .Pixso-instance-5629_42694
    .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51248 .Pixso-instance-5629_42694 .Pixso-frame-5588_11360 {
    width: 44px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_51248
    .Pixso-instance-5629_42694
    .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_51248
    .Pixso-instance-5629_42694
    .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_51248
    .Pixso-instance-5629_42694
    .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51249 .Pixso-paragraph-5629_42693 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_51249
    .Pixso-instance-5629_42694
    .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51249 .Pixso-instance-5629_42694 .Pixso-frame-5588_11360 {
    width: 44px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_51249
    .Pixso-instance-5629_42694
    .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_51249
    .Pixso-instance-5629_42694
    .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_51249
    .Pixso-instance-5629_42694
    .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51250 .Pixso-paragraph-5629_42693 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_51250
    .Pixso-instance-5629_42694
    .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51250 .Pixso-instance-5629_42694 .Pixso-frame-5588_11360 {
    width: 44px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_51250
    .Pixso-instance-5629_42694
    .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_51250
    .Pixso-instance-5629_42694
    .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_51250
    .Pixso-instance-5629_42694
    .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51251 .Pixso-paragraph-5629_42693 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_51251
    .Pixso-instance-5629_42694
    .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51251 .Pixso-instance-5629_42694 .Pixso-frame-5588_11360 {
    width: 44px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_51251
    .Pixso-instance-5629_42694
    .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_51251
    .Pixso-instance-5629_42694
    .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_51251
    .Pixso-instance-5629_42694
    .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51252 .Pixso-paragraph-5629_42705 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_51252 .Pixso-instance-5629_42706 {
    width: 28px;
    height: 24px;
}
.Pixso-instance-5629_51252
    .Pixso-instance-5629_42706
    .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51252 .Pixso-instance-5629_42706 .Pixso-frame-5588_11360 {
    width: 44px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_51252
    .Pixso-instance-5629_42706
    .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_51252
    .Pixso-instance-5629_42706
    .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_51252
    .Pixso-instance-5629_42706
    .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51260
    .Pixso-instance-5629_44355
    .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51260 .Pixso-instance-5629_44355 .Pixso-frame-5588_11360 {
    width: 44px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_51260
    .Pixso-instance-5629_44355
    .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_51260
    .Pixso-instance-5629_44355
    .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_51260
    .Pixso-instance-5629_44355
    .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51260 .Pixso-paragraph-5629_44354 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_51261
    .Pixso-instance-5629_44355
    .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51261 .Pixso-instance-5629_44355 .Pixso-frame-5588_11360 {
    width: 44px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_51261
    .Pixso-instance-5629_44355
    .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_51261
    .Pixso-instance-5629_44355
    .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_51261
    .Pixso-instance-5629_44355
    .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51261 .Pixso-paragraph-5629_44354 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_51262
    .Pixso-instance-5629_44355
    .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51262 .Pixso-instance-5629_44355 .Pixso-frame-5588_11360 {
    width: 44px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_51262
    .Pixso-instance-5629_44355
    .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_51262
    .Pixso-instance-5629_44355
    .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_51262
    .Pixso-instance-5629_44355
    .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51262 .Pixso-paragraph-5629_44354 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_51263
    .Pixso-instance-5629_44355
    .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51263 .Pixso-instance-5629_44355 .Pixso-frame-5588_11360 {
    width: 44px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_51263
    .Pixso-instance-5629_44355
    .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_51263
    .Pixso-instance-5629_44355
    .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_51263
    .Pixso-instance-5629_44355
    .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51263 .Pixso-paragraph-5629_44354 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_51264
    .Pixso-instance-5629_44363
    .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51264 .Pixso-instance-5629_44363 .Pixso-frame-5588_11360 {
    width: 44px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_51264
    .Pixso-instance-5629_44363
    .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_51264
    .Pixso-instance-5629_44363
    .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_51264
    .Pixso-instance-5629_44363
    .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51264 .Pixso-paragraph-5629_44362 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_51264 .Pixso-instance-5629_44363 {
    width: 28px;
    height: 24px;
}
.Pixso-instance-5629_51266 .Pixso-paragraph-5629_42601 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_51266
    .Pixso-instance-5629_42602
    .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51266 .Pixso-instance-5629_42602 .Pixso-frame-5588_11360 {
    width: 44px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_51266
    .Pixso-instance-5629_42602
    .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_51266
    .Pixso-instance-5629_42602
    .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_51266
    .Pixso-instance-5629_42602
    .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51267 .Pixso-paragraph-5629_42601 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_51267
    .Pixso-instance-5629_42602
    .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51267 .Pixso-instance-5629_42602 .Pixso-frame-5588_11360 {
    width: 44px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_51267
    .Pixso-instance-5629_42602
    .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_51267
    .Pixso-instance-5629_42602
    .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_51267
    .Pixso-instance-5629_42602
    .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51268 .Pixso-paragraph-5629_42601 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_51268
    .Pixso-instance-5629_42602
    .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51268 .Pixso-instance-5629_42602 .Pixso-frame-5588_11360 {
    width: 44px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_51268
    .Pixso-instance-5629_42602
    .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_51268
    .Pixso-instance-5629_42602
    .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_51268
    .Pixso-instance-5629_42602
    .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51269 .Pixso-paragraph-5629_42601 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_51269
    .Pixso-instance-5629_42602
    .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51269 .Pixso-instance-5629_42602 .Pixso-frame-5588_11360 {
    width: 44px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_51269
    .Pixso-instance-5629_42602
    .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_51269
    .Pixso-instance-5629_42602
    .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_51269
    .Pixso-instance-5629_42602
    .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51270 .Pixso-paragraph-5629_42613 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_51270 .Pixso-instance-5629_42614 {
    width: 28px;
    height: 24px;
}
.Pixso-instance-5629_51270
    .Pixso-instance-5629_42614
    .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51270 .Pixso-instance-5629_42614 .Pixso-frame-5588_11360 {
    width: 44px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_51270
    .Pixso-instance-5629_42614
    .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_51270
    .Pixso-instance-5629_42614
    .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_51270
    .Pixso-instance-5629_42614
    .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51278 .Pixso-paragraph-5629_44456 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_51278
    .Pixso-instance-5629_44457
    .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51278 .Pixso-instance-5629_44457 .Pixso-frame-5588_11360 {
    width: 44px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_51278
    .Pixso-instance-5629_44457
    .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_51278
    .Pixso-instance-5629_44457
    .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_51278
    .Pixso-instance-5629_44457
    .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51279 .Pixso-paragraph-5629_44456 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_51279
    .Pixso-instance-5629_44457
    .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51279 .Pixso-instance-5629_44457 .Pixso-frame-5588_11360 {
    width: 44px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_51279
    .Pixso-instance-5629_44457
    .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_51279
    .Pixso-instance-5629_44457
    .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_51279
    .Pixso-instance-5629_44457
    .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51280 .Pixso-paragraph-5629_44456 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_51280
    .Pixso-instance-5629_44457
    .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51280 .Pixso-instance-5629_44457 .Pixso-frame-5588_11360 {
    width: 44px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_51280
    .Pixso-instance-5629_44457
    .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_51280
    .Pixso-instance-5629_44457
    .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_51280
    .Pixso-instance-5629_44457
    .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51281 .Pixso-paragraph-5629_44456 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_51281
    .Pixso-instance-5629_44457
    .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51281 .Pixso-instance-5629_44457 .Pixso-frame-5588_11360 {
    width: 44px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_51281
    .Pixso-instance-5629_44457
    .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_51281
    .Pixso-instance-5629_44457
    .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_51281
    .Pixso-instance-5629_44457
    .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51282 .Pixso-paragraph-5629_44464 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_51282 .Pixso-instance-5629_44465 {
    width: 28px;
    height: 24px;
}
.Pixso-instance-5629_51282
    .Pixso-instance-5629_44465
    .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_51282 .Pixso-instance-5629_44465 .Pixso-frame-5588_11360 {
    width: 44px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5629_51282
    .Pixso-instance-5629_44465
    .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5629_51282
    .Pixso-instance-5629_44465
    .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5629_51282
    .Pixso-instance-5629_44465
    .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5629_47594 .Pixso-symbol-5629_43319 {
    width: 99px;
    height: 36px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 8px 12px 8px 12px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_47684 .Pixso-symbol-5629_43319 {
    width: 81px;
    height: 36px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 8px 12px 8px 12px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_47694 .Pixso-symbol-5629_43319 {
    width: 85px;
    height: 36px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 8px 12px 8px 12px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_47704 .Pixso-symbol-5629_43319 {
    width: 111px;
    height: 36px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 8px 12px 8px 12px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_51194 .Pixso-symbol-5629_43319 {
    width: 111px;
    height: 36px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 8px 12px 8px 12px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_51195 .Pixso-symbol-5629_43319 {
    width: 111px;
    height: 36px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 8px 12px 8px 12px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_51196 .Pixso-symbol-5629_43319 {
    width: 111px;
    height: 36px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 8px 12px 8px 12px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_51197 .Pixso-symbol-5629_43319 {
    width: 111px;
    height: 36px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 8px 12px 8px 12px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_47594 .Pixso-instance-5629_43320 {
    width: 16px;
    height: 16px;
}
.Pixso-instance-5629_47684 .Pixso-instance-5629_43320 {
    width: 16px;
    height: 16px;
}
.Pixso-instance-5629_47694 .Pixso-instance-5629_43320 {
    width: 16px;
    height: 16px;
}
.Pixso-instance-5629_47704 .Pixso-instance-5629_43320 {
    width: 16px;
    height: 16px;
}
.Pixso-instance-5629_51194 .Pixso-instance-5629_43320 {
    width: 16px;
    height: 16px;
}
.Pixso-instance-5629_51195 .Pixso-instance-5629_43320 {
    width: 16px;
    height: 16px;
}
.Pixso-instance-5629_51196 .Pixso-instance-5629_43320 {
    width: 16px;
    height: 16px;
}
.Pixso-instance-5629_51197 .Pixso-instance-5629_43320 {
    width: 16px;
    height: 16px;
}
.Pixso-instance-5629_47594 .Pixso-instance-5629_43322 {
    width: 24px;
    height: 20px;
}
.Pixso-instance-5629_47684 .Pixso-instance-5629_43322 {
    width: 24px;
    height: 20px;
}
.Pixso-instance-5629_47694 .Pixso-instance-5629_43322 {
    width: 24px;
    height: 20px;
}
.Pixso-instance-5629_47704 .Pixso-instance-5629_43322 {
    width: 24px;
    height: 20px;
}
.Pixso-instance-5629_51194 .Pixso-instance-5629_43322 {
    width: 24px;
    height: 20px;
}
.Pixso-instance-5629_51195 .Pixso-instance-5629_43322 {
    width: 24px;
    height: 20px;
}
.Pixso-instance-5629_51196 .Pixso-instance-5629_43322 {
    width: 24px;
    height: 20px;
}
.Pixso-instance-5629_51197 .Pixso-instance-5629_43322 {
    width: 24px;
    height: 20px;
}
.Pixso-instance-5629_50493 .Pixso-symbol-5629_43810 {
    width: 99px;
    height: 36px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 8px 12px 8px 12px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_50494 .Pixso-symbol-5629_43810 {
    width: 81px;
    height: 36px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 8px 12px 8px 12px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_50495 .Pixso-symbol-5629_43810 {
    width: 85px;
    height: 36px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 8px 12px 8px 12px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_50496 .Pixso-symbol-5629_43810 {
    width: 111px;
    height: 36px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 8px 12px 8px 12px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_51212 .Pixso-symbol-5629_43810 {
    width: 111px;
    height: 36px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 8px 12px 8px 12px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_51213 .Pixso-symbol-5629_43810 {
    width: 111px;
    height: 36px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 8px 12px 8px 12px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_51214 .Pixso-symbol-5629_43810 {
    width: 111px;
    height: 36px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 8px 12px 8px 12px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_51215 .Pixso-symbol-5629_43810 {
    width: 111px;
    height: 36px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 8px 12px 8px 12px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_50493 .Pixso-instance-5629_43811 {
    width: 16px;
    height: 16px;
}
.Pixso-instance-5629_50494 .Pixso-instance-5629_43811 {
    width: 16px;
    height: 16px;
}
.Pixso-instance-5629_50495 .Pixso-instance-5629_43811 {
    width: 16px;
    height: 16px;
}
.Pixso-instance-5629_50496 .Pixso-instance-5629_43811 {
    width: 16px;
    height: 16px;
}
.Pixso-instance-5629_51212 .Pixso-instance-5629_43811 {
    width: 16px;
    height: 16px;
}
.Pixso-instance-5629_51213 .Pixso-instance-5629_43811 {
    width: 16px;
    height: 16px;
}
.Pixso-instance-5629_51214 .Pixso-instance-5629_43811 {
    width: 16px;
    height: 16px;
}
.Pixso-instance-5629_51215 .Pixso-instance-5629_43811 {
    width: 16px;
    height: 16px;
}
.Pixso-instance-5629_50493 .Pixso-instance-5629_43813 {
    width: 24px;
    height: 20px;
}
.Pixso-instance-5629_50494 .Pixso-instance-5629_43813 {
    width: 24px;
    height: 20px;
}
.Pixso-instance-5629_50495 .Pixso-instance-5629_43813 {
    width: 24px;
    height: 20px;
}
.Pixso-instance-5629_50496 .Pixso-instance-5629_43813 {
    width: 24px;
    height: 20px;
}
.Pixso-instance-5629_51212 .Pixso-instance-5629_43813 {
    width: 24px;
    height: 20px;
}
.Pixso-instance-5629_51213 .Pixso-instance-5629_43813 {
    width: 24px;
    height: 20px;
}
.Pixso-instance-5629_51214 .Pixso-instance-5629_43813 {
    width: 24px;
    height: 20px;
}
.Pixso-instance-5629_51215 .Pixso-instance-5629_43813 {
    width: 24px;
    height: 20px;
}
.Pixso-instance-5629_50679 .Pixso-symbol-5629_43902 {
    width: 99px;
    height: 36px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 8px 12px 8px 12px;
}
.Pixso-instance-5629_50680 .Pixso-symbol-5629_43902 {
    width: 81px;
    height: 36px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 8px 12px 8px 12px;
}
.Pixso-instance-5629_50681 .Pixso-symbol-5629_43902 {
    width: 85px;
    height: 36px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 8px 12px 8px 12px;
}
.Pixso-instance-5629_50682 .Pixso-symbol-5629_43902 {
    width: 111px;
    height: 36px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 8px 12px 8px 12px;
}
.Pixso-instance-5629_51218 .Pixso-symbol-5629_43902 {
    width: 111px;
    height: 36px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 8px 12px 8px 12px;
}
.Pixso-instance-5629_51219 .Pixso-symbol-5629_43902 {
    width: 111px;
    height: 36px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 8px 12px 8px 12px;
}
.Pixso-instance-5629_51220 .Pixso-symbol-5629_43902 {
    width: 111px;
    height: 36px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 8px 12px 8px 12px;
}
.Pixso-instance-5629_51221 .Pixso-symbol-5629_43902 {
    width: 111px;
    height: 36px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 8px 12px 8px 12px;
}
.Pixso-instance-5629_50679 .Pixso-instance-5629_43903 {
    width: 16px;
    height: 16px;
}
.Pixso-instance-5629_50680 .Pixso-instance-5629_43903 {
    width: 16px;
    height: 16px;
}
.Pixso-instance-5629_50681 .Pixso-instance-5629_43903 {
    width: 16px;
    height: 16px;
}
.Pixso-instance-5629_50682 .Pixso-instance-5629_43903 {
    width: 16px;
    height: 16px;
}
.Pixso-instance-5629_51218 .Pixso-instance-5629_43903 {
    width: 16px;
    height: 16px;
}
.Pixso-instance-5629_51219 .Pixso-instance-5629_43903 {
    width: 16px;
    height: 16px;
}
.Pixso-instance-5629_51220 .Pixso-instance-5629_43903 {
    width: 16px;
    height: 16px;
}
.Pixso-instance-5629_51221 .Pixso-instance-5629_43903 {
    width: 16px;
    height: 16px;
}
.Pixso-instance-5629_50679 .Pixso-instance-5629_43905 {
    width: 24px;
    height: 20px;
}
.Pixso-instance-5629_50680 .Pixso-instance-5629_43905 {
    width: 24px;
    height: 20px;
}
.Pixso-instance-5629_50681 .Pixso-instance-5629_43905 {
    width: 24px;
    height: 20px;
}
.Pixso-instance-5629_50682 .Pixso-instance-5629_43905 {
    width: 24px;
    height: 20px;
}
.Pixso-instance-5629_51218 .Pixso-instance-5629_43905 {
    width: 24px;
    height: 20px;
}
.Pixso-instance-5629_51219 .Pixso-instance-5629_43905 {
    width: 24px;
    height: 20px;
}
.Pixso-instance-5629_51220 .Pixso-instance-5629_43905 {
    width: 24px;
    height: 20px;
}
.Pixso-instance-5629_51221 .Pixso-instance-5629_43905 {
    width: 24px;
    height: 20px;
}
.Pixso-instance-5629_51050 .Pixso-symbol-5629_44270 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 8px 12px 8px 12px;
}
.Pixso-instance-5629_51050 .stroke-wrapper-5629_44270 {
    width: 99px;
    height: 36px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5629_51050 .stroke-5629_44270 {
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 0px 2px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5629_51051 .Pixso-symbol-5629_44270 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 8px 12px 8px 12px;
}
.Pixso-instance-5629_51051 .stroke-wrapper-5629_44270 {
    width: 81px;
    height: 36px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5629_51051 .stroke-5629_44270 {
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 0px 2px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5629_51052 .Pixso-symbol-5629_44270 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 8px 12px 8px 12px;
}
.Pixso-instance-5629_51052 .stroke-wrapper-5629_44270 {
    width: 85px;
    height: 36px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5629_51052 .stroke-5629_44270 {
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 0px 2px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5629_51053 .Pixso-symbol-5629_44270 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 8px 12px 8px 12px;
}
.Pixso-instance-5629_51053 .stroke-wrapper-5629_44270 {
    width: 111px;
    height: 36px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5629_51053 .stroke-5629_44270 {
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 0px 2px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5629_51230 .Pixso-symbol-5629_44270 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 8px 12px 8px 12px;
}
.Pixso-instance-5629_51230 .stroke-wrapper-5629_44270 {
    width: 111px;
    height: 36px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5629_51230 .stroke-5629_44270 {
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 0px 2px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5629_51231 .Pixso-symbol-5629_44270 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 8px 12px 8px 12px;
}
.Pixso-instance-5629_51231 .stroke-wrapper-5629_44270 {
    width: 111px;
    height: 36px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5629_51231 .stroke-5629_44270 {
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 0px 2px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5629_51232 .Pixso-symbol-5629_44270 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 8px 12px 8px 12px;
}
.Pixso-instance-5629_51232 .stroke-wrapper-5629_44270 {
    width: 111px;
    height: 36px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5629_51232 .stroke-5629_44270 {
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 0px 2px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5629_51233 .Pixso-symbol-5629_44270 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 8px 12px 8px 12px;
}
.Pixso-instance-5629_51233 .stroke-wrapper-5629_44270 {
    width: 111px;
    height: 36px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5629_51233 .stroke-5629_44270 {
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 0px 2px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5629_51050 .Pixso-instance-5629_44271 {
    width: 16px;
    height: 16px;
}
.Pixso-instance-5629_51051 .Pixso-instance-5629_44271 {
    width: 16px;
    height: 16px;
}
.Pixso-instance-5629_51052 .Pixso-instance-5629_44271 {
    width: 16px;
    height: 16px;
}
.Pixso-instance-5629_51053 .Pixso-instance-5629_44271 {
    width: 16px;
    height: 16px;
}
.Pixso-instance-5629_51230 .Pixso-instance-5629_44271 {
    width: 16px;
    height: 16px;
}
.Pixso-instance-5629_51231 .Pixso-instance-5629_44271 {
    width: 16px;
    height: 16px;
}
.Pixso-instance-5629_51232 .Pixso-instance-5629_44271 {
    width: 16px;
    height: 16px;
}
.Pixso-instance-5629_51233 .Pixso-instance-5629_44271 {
    width: 16px;
    height: 16px;
}
.Pixso-instance-5629_51050 .Pixso-instance-5629_44273 {
    width: 24px;
    height: 20px;
}
.Pixso-instance-5629_51051 .Pixso-instance-5629_44273 {
    width: 24px;
    height: 20px;
}
.Pixso-instance-5629_51052 .Pixso-instance-5629_44273 {
    width: 24px;
    height: 20px;
}
.Pixso-instance-5629_51053 .Pixso-instance-5629_44273 {
    width: 24px;
    height: 20px;
}
.Pixso-instance-5629_51230 .Pixso-instance-5629_44273 {
    width: 24px;
    height: 20px;
}
.Pixso-instance-5629_51231 .Pixso-instance-5629_44273 {
    width: 24px;
    height: 20px;
}
.Pixso-instance-5629_51232 .Pixso-instance-5629_44273 {
    width: 24px;
    height: 20px;
}
.Pixso-instance-5629_51233 .Pixso-instance-5629_44273 {
    width: 24px;
    height: 20px;
}
.Pixso-instance-5629_50683 .Pixso-symbol-5629_43914 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 8px 12px 8px 12px;
}
.Pixso-instance-5629_50683 .stroke-wrapper-5629_43914 {
    width: 100px;
    height: 36px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5629_50683 .stroke-5629_43914 {
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 2px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5629_51222 .Pixso-symbol-5629_43914 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 8px 12px 8px 12px;
}
.Pixso-instance-5629_51222 .stroke-wrapper-5629_43914 {
    width: 111px;
    height: 36px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5629_51222 .stroke-5629_43914 {
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 2px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5629_50683 .Pixso-instance-5629_43915 {
    width: 16px;
    height: 16px;
}
.Pixso-instance-5629_51222 .Pixso-instance-5629_43915 {
    width: 16px;
    height: 16px;
}
.Pixso-instance-5629_47714 .Pixso-symbol-5629_43710 {
    width: 100px;
    height: 36px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 8px 12px 8px 12px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_51198 .Pixso-symbol-5629_43710 {
    width: 111px;
    height: 36px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 8px 12px 8px 12px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_47714 .Pixso-instance-5629_43711 {
    width: 16px;
    height: 16px;
}
.Pixso-instance-5629_51198 .Pixso-instance-5629_43711 {
    width: 16px;
    height: 16px;
}
.Pixso-instance-5629_50497 .Pixso-symbol-5629_43822 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 8px 12px 8px 12px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_50497 .stroke-wrapper-5629_43822 {
    width: 100px;
    height: 36px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5629_50497 .stroke-5629_43822 {
    inset: 0px;
    border-radius: 1234px 1234px 1234px 1234px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5629_51216 .Pixso-symbol-5629_43822 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 8px 12px 8px 12px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_51216 .stroke-wrapper-5629_43822 {
    width: 111px;
    height: 36px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5629_51216 .stroke-5629_43822 {
    inset: 0px;
    border-radius: 1234px 1234px 1234px 1234px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5629_50497 .Pixso-instance-5629_43823 {
    width: 16px;
    height: 16px;
}
.Pixso-instance-5629_51216 .Pixso-instance-5629_43823 {
    width: 16px;
    height: 16px;
}
.Pixso-instance-5629_51054 .Pixso-symbol-5629_44278 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 8px 12px 8px 12px;
}
.Pixso-instance-5629_51054 .stroke-wrapper-5629_44278 {
    width: 100px;
    height: 36px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5629_51054 .stroke-5629_44278 {
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 0px 2px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5629_51234 .Pixso-symbol-5629_44278 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 8px 12px 8px 12px;
}
.Pixso-instance-5629_51234 .stroke-wrapper-5629_44278 {
    width: 111px;
    height: 36px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5629_51234 .stroke-5629_44278 {
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 0px 2px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5629_51054 .Pixso-instance-5629_44279 {
    width: 16px;
    height: 16px;
}
.Pixso-instance-5629_51234 .Pixso-instance-5629_44279 {
    width: 16px;
    height: 16px;
}
.Pixso-instance-5629_47760 .Pixso-symbol-5558_51587 {
    width: 107px;
    height: 40px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 8px 16px 8px 16px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_47761 .Pixso-symbol-5558_51587 {
    width: 89px;
    height: 40px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 8px 16px 8px 16px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_47762 .Pixso-symbol-5558_51587 {
    width: 93px;
    height: 40px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 8px 16px 8px 16px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_47763 .Pixso-symbol-5558_51587 {
    width: 119px;
    height: 40px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 8px 16px 8px 16px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_51200 .Pixso-symbol-5558_51587 {
    width: 119px;
    height: 40px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 8px 16px 8px 16px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_51201 .Pixso-symbol-5558_51587 {
    width: 119px;
    height: 40px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 8px 16px 8px 16px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_51202 .Pixso-symbol-5558_51587 {
    width: 119px;
    height: 40px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 8px 16px 8px 16px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_51203 .Pixso-symbol-5558_51587 {
    width: 119px;
    height: 40px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 8px 16px 8px 16px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_50499 .Pixso-symbol-5629_41545 {
    width: 107px;
    height: 40px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 8px 16px 8px 16px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_50500 .Pixso-symbol-5629_41545 {
    width: 89px;
    height: 40px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 8px 16px 8px 16px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_50501 .Pixso-symbol-5629_41545 {
    width: 93px;
    height: 40px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 8px 16px 8px 16px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_50502 .Pixso-symbol-5629_41545 {
    width: 119px;
    height: 40px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 8px 16px 8px 16px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_51242 .Pixso-symbol-5629_41545 {
    width: 119px;
    height: 40px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 8px 16px 8px 16px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_51243 .Pixso-symbol-5629_41545 {
    width: 119px;
    height: 40px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 8px 16px 8px 16px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_51244 .Pixso-symbol-5629_41545 {
    width: 119px;
    height: 40px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 8px 16px 8px 16px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_51245 .Pixso-symbol-5629_41545 {
    width: 119px;
    height: 40px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 8px 16px 8px 16px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_50685 .Pixso-symbol-5629_41453 {
    width: 107px;
    height: 40px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 8px 16px 8px 16px;
}
.Pixso-instance-5629_50686 .Pixso-symbol-5629_41453 {
    width: 89px;
    height: 40px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 8px 16px 8px 16px;
}
.Pixso-instance-5629_50687 .Pixso-symbol-5629_41453 {
    width: 93px;
    height: 40px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 8px 16px 8px 16px;
}
.Pixso-instance-5629_50688 .Pixso-symbol-5629_41453 {
    width: 119px;
    height: 40px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 8px 16px 8px 16px;
}
.Pixso-instance-5629_50689 .Pixso-symbol-5629_41461 .Pixso-symbol-5629_41453 {
    width: 112px;
    height: 40px;
    overflow: hidden;
    position: absolute;
    left: 408px;
    top: 0px;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 8px 16px 8px 16px;
}
.Pixso-instance-5629_51236 .Pixso-symbol-5629_41453 {
    width: 119px;
    height: 40px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 8px 16px 8px 16px;
}
.Pixso-instance-5629_51237 .Pixso-symbol-5629_41453 {
    width: 119px;
    height: 40px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 8px 16px 8px 16px;
}
.Pixso-instance-5629_51238 .Pixso-symbol-5629_41453 {
    width: 119px;
    height: 40px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 8px 16px 8px 16px;
}
.Pixso-instance-5629_51239 .Pixso-symbol-5629_41453 {
    width: 119px;
    height: 40px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 8px 16px 8px 16px;
}
.Pixso-instance-5629_51056 .Pixso-symbol-5629_44352 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 8px 16px 8px 16px;
}
.Pixso-instance-5629_51056 .stroke-wrapper-5629_44352 {
    width: 107px;
    height: 40px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5629_51056 .stroke-5629_44352 {
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 0px 2px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5629_51057 .Pixso-symbol-5629_44352 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 8px 16px 8px 16px;
}
.Pixso-instance-5629_51057 .stroke-wrapper-5629_44352 {
    width: 89px;
    height: 40px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5629_51057 .stroke-5629_44352 {
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 0px 2px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5629_51058 .Pixso-symbol-5629_44352 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 8px 16px 8px 16px;
}
.Pixso-instance-5629_51058 .stroke-wrapper-5629_44352 {
    width: 93px;
    height: 40px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5629_51058 .stroke-5629_44352 {
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 0px 2px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5629_51059 .Pixso-symbol-5629_44352 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 8px 16px 8px 16px;
}
.Pixso-instance-5629_51059 .stroke-wrapper-5629_44352 {
    width: 119px;
    height: 40px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5629_51059 .stroke-5629_44352 {
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 0px 2px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5629_51260 .Pixso-symbol-5629_44352 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 8px 16px 8px 16px;
}
.Pixso-instance-5629_51260 .stroke-wrapper-5629_44352 {
    width: 119px;
    height: 40px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5629_51260 .stroke-5629_44352 {
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 0px 2px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5629_51261 .Pixso-symbol-5629_44352 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 8px 16px 8px 16px;
}
.Pixso-instance-5629_51261 .stroke-wrapper-5629_44352 {
    width: 119px;
    height: 40px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5629_51261 .stroke-5629_44352 {
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 0px 2px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5629_51262 .Pixso-symbol-5629_44352 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 8px 16px 8px 16px;
}
.Pixso-instance-5629_51262 .stroke-wrapper-5629_44352 {
    width: 119px;
    height: 40px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5629_51262 .stroke-5629_44352 {
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 0px 2px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5629_51263 .Pixso-symbol-5629_44352 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 8px 16px 8px 16px;
}
.Pixso-instance-5629_51263 .stroke-wrapper-5629_44352 {
    width: 119px;
    height: 40px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5629_51263 .stroke-5629_44352 {
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 0px 2px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5629_47764 .Pixso-symbol-5629_41260 {
    width: 112px;
    height: 40px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 8px 16px 8px 16px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_51204 .Pixso-symbol-5629_41260 {
    width: 119px;
    height: 40px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 8px 16px 8px 16px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_50503 .Pixso-symbol-5629_41553 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 8px 16px 8px 16px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_50503 .stroke-wrapper-5629_41553 {
    width: 112px;
    height: 40px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5629_50503 .stroke-5629_41553 {
    inset: 0px;
    border-radius: 1234px 1234px 1234px 1234px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5629_51246 .Pixso-symbol-5629_41553 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 8px 16px 8px 16px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_51246 .stroke-wrapper-5629_41553 {
    width: 119px;
    height: 40px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5629_51246 .stroke-5629_41553 {
    inset: 0px;
    border-radius: 1234px 1234px 1234px 1234px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5629_50686 .Pixso-symbol-5629_41453 .Pixso-symbol-5629_41461 {
    width: 89px;
    height: 40px;
    overflow: hidden;
    position: absolute;
    left: 107px;
    top: 0px;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 8px 16px 8px 16px;
}
.Pixso-instance-5629_50689 .Pixso-symbol-5629_41461 {
    width: 112px;
    height: 40px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 8px 16px 8px 16px;
}
.Pixso-instance-5629_51240 .Pixso-symbol-5629_41461 {
    width: 119px;
    height: 40px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 8px 16px 8px 16px;
}
.Pixso-instance-5629_51060 .Pixso-symbol-5629_44360 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 8px 16px 8px 16px;
}
.Pixso-instance-5629_51060 .stroke-wrapper-5629_44360 {
    width: 112px;
    height: 40px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5629_51060 .stroke-5629_44360 {
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 0px 2px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5629_51264 .Pixso-symbol-5629_44360 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 8px 16px 8px 16px;
}
.Pixso-instance-5629_51264 .stroke-wrapper-5629_44360 {
    width: 119px;
    height: 40px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5629_51264 .stroke-5629_44360 {
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 0px 2px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5629_47808 .Pixso-symbol-5629_42113 {
    width: 118px;
    height: 48px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 10px;
    justify-content: center;
    align-items: center;
    padding: 12px 16px 12px 16px;
    min-height: 48px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_47809 .Pixso-symbol-5629_42113 {
    width: 97px;
    height: 48px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 10px;
    justify-content: center;
    align-items: center;
    padding: 12px 16px 12px 16px;
    min-height: 48px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_47810 .Pixso-symbol-5629_42113 {
    width: 101px;
    height: 48px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 10px;
    justify-content: center;
    align-items: center;
    padding: 12px 16px 12px 16px;
    min-height: 48px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_47811 .Pixso-symbol-5629_42113 {
    width: 131px;
    height: 48px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 10px;
    justify-content: center;
    align-items: center;
    padding: 12px 16px 12px 16px;
    min-height: 48px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_51206 .Pixso-symbol-5629_42113 {
    width: 131px;
    height: 48px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 10px;
    justify-content: center;
    align-items: center;
    padding: 12px 16px 12px 16px;
    min-height: 48px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_51207 .Pixso-symbol-5629_42113 {
    width: 131px;
    height: 48px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 10px;
    justify-content: center;
    align-items: center;
    padding: 12px 16px 12px 16px;
    min-height: 48px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_51208 .Pixso-symbol-5629_42113 {
    width: 131px;
    height: 48px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 10px;
    justify-content: center;
    align-items: center;
    padding: 12px 16px 12px 16px;
    min-height: 48px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_51209 .Pixso-symbol-5629_42113 {
    width: 131px;
    height: 48px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 10px;
    justify-content: center;
    align-items: center;
    padding: 12px 16px 12px 16px;
    min-height: 48px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_47808 .Pixso-instance-5629_42114 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5629_47809 .Pixso-instance-5629_42114 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5629_47810 .Pixso-instance-5629_42114 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5629_47811 .Pixso-instance-5629_42114 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5629_51206 .Pixso-instance-5629_42114 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5629_51207 .Pixso-instance-5629_42114 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5629_51208 .Pixso-instance-5629_42114 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5629_51209 .Pixso-instance-5629_42114 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5629_47808 .Pixso-instance-5629_42116 {
    width: 28px;
    height: 24px;
}
.Pixso-instance-5629_47809 .Pixso-instance-5629_42116 {
    width: 28px;
    height: 24px;
}
.Pixso-instance-5629_47810 .Pixso-instance-5629_42116 {
    width: 28px;
    height: 24px;
}
.Pixso-instance-5629_47811 .Pixso-instance-5629_42116 {
    width: 28px;
    height: 24px;
}
.Pixso-instance-5629_51206 .Pixso-instance-5629_42116 {
    width: 28px;
    height: 24px;
}
.Pixso-instance-5629_51207 .Pixso-instance-5629_42116 {
    width: 28px;
    height: 24px;
}
.Pixso-instance-5629_51208 .Pixso-instance-5629_42116 {
    width: 28px;
    height: 24px;
}
.Pixso-instance-5629_51209 .Pixso-instance-5629_42116 {
    width: 28px;
    height: 24px;
}
.Pixso-instance-5629_50505 .Pixso-symbol-5629_42599 {
    width: 118px;
    height: 48px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 10px;
    justify-content: center;
    align-items: center;
    padding: 12px 16px 12px 16px;
    min-height: 48px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_50506 .Pixso-symbol-5629_42599 {
    width: 97px;
    height: 48px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 10px;
    justify-content: center;
    align-items: center;
    padding: 12px 16px 12px 16px;
    min-height: 48px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_50507 .Pixso-symbol-5629_42599 {
    width: 101px;
    height: 48px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 10px;
    justify-content: center;
    align-items: center;
    padding: 12px 16px 12px 16px;
    min-height: 48px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_50508 .Pixso-symbol-5629_42599 {
    width: 131px;
    height: 48px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 10px;
    justify-content: center;
    align-items: center;
    padding: 12px 16px 12px 16px;
    min-height: 48px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_51266 .Pixso-symbol-5629_42599 {
    width: 131px;
    height: 48px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 10px;
    justify-content: center;
    align-items: center;
    padding: 12px 16px 12px 16px;
    min-height: 48px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_51267 .Pixso-symbol-5629_42599 {
    width: 131px;
    height: 48px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 10px;
    justify-content: center;
    align-items: center;
    padding: 12px 16px 12px 16px;
    min-height: 48px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_51268 .Pixso-symbol-5629_42599 {
    width: 131px;
    height: 48px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 10px;
    justify-content: center;
    align-items: center;
    padding: 12px 16px 12px 16px;
    min-height: 48px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_51269 .Pixso-symbol-5629_42599 {
    width: 131px;
    height: 48px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 10px;
    justify-content: center;
    align-items: center;
    padding: 12px 16px 12px 16px;
    min-height: 48px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_50505 .Pixso-instance-5629_42600 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5629_50506 .Pixso-instance-5629_42600 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5629_50507 .Pixso-instance-5629_42600 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5629_50508 .Pixso-instance-5629_42600 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5629_51266 .Pixso-instance-5629_42600 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5629_51267 .Pixso-instance-5629_42600 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5629_51268 .Pixso-instance-5629_42600 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5629_51269 .Pixso-instance-5629_42600 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5629_50505 .Pixso-instance-5629_42602 {
    width: 28px;
    height: 24px;
}
.Pixso-instance-5629_50506 .Pixso-instance-5629_42602 {
    width: 28px;
    height: 24px;
}
.Pixso-instance-5629_50507 .Pixso-instance-5629_42602 {
    width: 28px;
    height: 24px;
}
.Pixso-instance-5629_50508 .Pixso-instance-5629_42602 {
    width: 28px;
    height: 24px;
}
.Pixso-instance-5629_51266 .Pixso-instance-5629_42602 {
    width: 28px;
    height: 24px;
}
.Pixso-instance-5629_51267 .Pixso-instance-5629_42602 {
    width: 28px;
    height: 24px;
}
.Pixso-instance-5629_51268 .Pixso-instance-5629_42602 {
    width: 28px;
    height: 24px;
}
.Pixso-instance-5629_51269 .Pixso-instance-5629_42602 {
    width: 28px;
    height: 24px;
}
.Pixso-instance-5629_50691 .Pixso-symbol-5629_42691 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 10px;
    justify-content: center;
    align-items: center;
    padding: 12px 16px 12px 16px;
    min-height: 48px;
}
.Pixso-instance-5629_50691 .stroke-wrapper-5629_42691 {
    width: 118px;
    height: 48px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5629_50691 .stroke-5629_42691 {
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 2px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5629_50692 .Pixso-symbol-5629_42691 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 10px;
    justify-content: center;
    align-items: center;
    padding: 12px 16px 12px 16px;
    min-height: 48px;
}
.Pixso-instance-5629_50692 .stroke-wrapper-5629_42691 {
    width: 97px;
    height: 48px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5629_50692 .stroke-5629_42691 {
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 2px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5629_50693 .Pixso-symbol-5629_42691 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 10px;
    justify-content: center;
    align-items: center;
    padding: 12px 16px 12px 16px;
    min-height: 48px;
}
.Pixso-instance-5629_50693 .stroke-wrapper-5629_42691 {
    width: 101px;
    height: 48px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5629_50693 .stroke-5629_42691 {
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 2px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5629_50694 .Pixso-symbol-5629_42691 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 10px;
    justify-content: center;
    align-items: center;
    padding: 12px 16px 12px 16px;
    min-height: 48px;
}
.Pixso-instance-5629_50694 .stroke-wrapper-5629_42691 {
    width: 131px;
    height: 48px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5629_50694 .stroke-5629_42691 {
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 2px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5629_51248 .Pixso-symbol-5629_42691 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 10px;
    justify-content: center;
    align-items: center;
    padding: 12px 16px 12px 16px;
    min-height: 48px;
}
.Pixso-instance-5629_51248 .stroke-wrapper-5629_42691 {
    width: 131px;
    height: 48px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5629_51248 .stroke-5629_42691 {
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 2px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5629_51249 .Pixso-symbol-5629_42691 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 10px;
    justify-content: center;
    align-items: center;
    padding: 12px 16px 12px 16px;
    min-height: 48px;
}
.Pixso-instance-5629_51249 .stroke-wrapper-5629_42691 {
    width: 131px;
    height: 48px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5629_51249 .stroke-5629_42691 {
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 2px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5629_51250 .Pixso-symbol-5629_42691 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 10px;
    justify-content: center;
    align-items: center;
    padding: 12px 16px 12px 16px;
    min-height: 48px;
}
.Pixso-instance-5629_51250 .stroke-wrapper-5629_42691 {
    width: 131px;
    height: 48px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5629_51250 .stroke-5629_42691 {
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 2px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5629_51251 .Pixso-symbol-5629_42691 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 10px;
    justify-content: center;
    align-items: center;
    padding: 12px 16px 12px 16px;
    min-height: 48px;
}
.Pixso-instance-5629_51251 .stroke-wrapper-5629_42691 {
    width: 131px;
    height: 48px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5629_51251 .stroke-5629_42691 {
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 2px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5629_50691 .Pixso-instance-5629_42692 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5629_50692 .Pixso-instance-5629_42692 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5629_50693 .Pixso-instance-5629_42692 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5629_50694 .Pixso-instance-5629_42692 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5629_51248 .Pixso-instance-5629_42692 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5629_51249 .Pixso-instance-5629_42692 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5629_51250 .Pixso-instance-5629_42692 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5629_51251 .Pixso-instance-5629_42692 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5629_50691 .Pixso-instance-5629_42694 {
    width: 28px;
    height: 24px;
}
.Pixso-instance-5629_50692 .Pixso-instance-5629_42694 {
    width: 28px;
    height: 24px;
}
.Pixso-instance-5629_50693 .Pixso-instance-5629_42694 {
    width: 28px;
    height: 24px;
}
.Pixso-instance-5629_50694 .Pixso-instance-5629_42694 {
    width: 28px;
    height: 24px;
}
.Pixso-instance-5629_51248 .Pixso-instance-5629_42694 {
    width: 28px;
    height: 24px;
}
.Pixso-instance-5629_51249 .Pixso-instance-5629_42694 {
    width: 28px;
    height: 24px;
}
.Pixso-instance-5629_51250 .Pixso-instance-5629_42694 {
    width: 28px;
    height: 24px;
}
.Pixso-instance-5629_51251 .Pixso-instance-5629_42694 {
    width: 28px;
    height: 24px;
}
.Pixso-instance-5629_51062 .Pixso-symbol-5629_44454 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 10px;
    justify-content: center;
    align-items: center;
    padding: 12px 16px 12px 16px;
    min-height: 48px;
}
.Pixso-instance-5629_51062 .stroke-wrapper-5629_44454 {
    width: 118px;
    height: 48px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5629_51062 .stroke-5629_44454 {
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 0px 2px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5629_51063 .Pixso-symbol-5629_44454 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 10px;
    justify-content: center;
    align-items: center;
    padding: 12px 16px 12px 16px;
    min-height: 48px;
}
.Pixso-instance-5629_51063 .stroke-wrapper-5629_44454 {
    width: 97px;
    height: 48px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5629_51063 .stroke-5629_44454 {
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 0px 2px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5629_51064 .Pixso-symbol-5629_44454 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 10px;
    justify-content: center;
    align-items: center;
    padding: 12px 16px 12px 16px;
    min-height: 48px;
}
.Pixso-instance-5629_51064 .stroke-wrapper-5629_44454 {
    width: 101px;
    height: 48px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5629_51064 .stroke-5629_44454 {
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 0px 2px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5629_51065 .Pixso-symbol-5629_44454 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 10px;
    justify-content: center;
    align-items: center;
    padding: 12px 16px 12px 16px;
    min-height: 48px;
}
.Pixso-instance-5629_51065 .stroke-wrapper-5629_44454 {
    width: 131px;
    height: 48px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5629_51065 .stroke-5629_44454 {
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 0px 2px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5629_51278 .Pixso-symbol-5629_44454 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 10px;
    justify-content: center;
    align-items: center;
    padding: 12px 16px 12px 16px;
    min-height: 48px;
}
.Pixso-instance-5629_51278 .stroke-wrapper-5629_44454 {
    width: 131px;
    height: 48px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5629_51278 .stroke-5629_44454 {
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 0px 2px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5629_51279 .Pixso-symbol-5629_44454 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 10px;
    justify-content: center;
    align-items: center;
    padding: 12px 16px 12px 16px;
    min-height: 48px;
}
.Pixso-instance-5629_51279 .stroke-wrapper-5629_44454 {
    width: 131px;
    height: 48px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5629_51279 .stroke-5629_44454 {
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 0px 2px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5629_51280 .Pixso-symbol-5629_44454 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 10px;
    justify-content: center;
    align-items: center;
    padding: 12px 16px 12px 16px;
    min-height: 48px;
}
.Pixso-instance-5629_51280 .stroke-wrapper-5629_44454 {
    width: 131px;
    height: 48px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5629_51280 .stroke-5629_44454 {
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 0px 2px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5629_51281 .Pixso-symbol-5629_44454 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 10px;
    justify-content: center;
    align-items: center;
    padding: 12px 16px 12px 16px;
    min-height: 48px;
}
.Pixso-instance-5629_51281 .stroke-wrapper-5629_44454 {
    width: 131px;
    height: 48px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5629_51281 .stroke-5629_44454 {
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 0px 2px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5629_51062 .Pixso-instance-5629_44455 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5629_51063 .Pixso-instance-5629_44455 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5629_51064 .Pixso-instance-5629_44455 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5629_51065 .Pixso-instance-5629_44455 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5629_51278 .Pixso-instance-5629_44455 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5629_51279 .Pixso-instance-5629_44455 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5629_51280 .Pixso-instance-5629_44455 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5629_51281 .Pixso-instance-5629_44455 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5629_51062 .Pixso-instance-5629_44457 {
    width: 28px;
    height: 24px;
}
.Pixso-instance-5629_51063 .Pixso-instance-5629_44457 {
    width: 28px;
    height: 24px;
}
.Pixso-instance-5629_51064 .Pixso-instance-5629_44457 {
    width: 28px;
    height: 24px;
}
.Pixso-instance-5629_51065 .Pixso-instance-5629_44457 {
    width: 28px;
    height: 24px;
}
.Pixso-instance-5629_51278 .Pixso-instance-5629_44457 {
    width: 28px;
    height: 24px;
}
.Pixso-instance-5629_51279 .Pixso-instance-5629_44457 {
    width: 28px;
    height: 24px;
}
.Pixso-instance-5629_51280 .Pixso-instance-5629_44457 {
    width: 28px;
    height: 24px;
}
.Pixso-instance-5629_51281 .Pixso-instance-5629_44457 {
    width: 28px;
    height: 24px;
}
.Pixso-instance-5629_50695 .Pixso-symbol-5629_42703 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 10px;
    justify-content: center;
    align-items: center;
    padding: 12px 16px 12px 16px;
    min-height: 48px;
}
.Pixso-instance-5629_50695 .stroke-wrapper-5629_42703 {
    width: 120px;
    height: 48px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5629_50695 .stroke-5629_42703 {
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 2px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5629_51252 .Pixso-symbol-5629_42703 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 10px;
    justify-content: center;
    align-items: center;
    padding: 12px 16px 12px 16px;
    min-height: 48px;
}
.Pixso-instance-5629_51252 .stroke-wrapper-5629_42703 {
    width: 131px;
    height: 48px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5629_51252 .stroke-5629_42703 {
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 2px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5629_50695 .Pixso-instance-5629_42704 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5629_51252 .Pixso-instance-5629_42704 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5629_47812 .Pixso-symbol-5629_42499 {
    width: 120px;
    height: 48px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 10px;
    justify-content: center;
    align-items: center;
    padding: 12px 16px 12px 16px;
    min-height: 48px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_51210 .Pixso-symbol-5629_42499 {
    width: 131px;
    height: 48px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 10px;
    justify-content: center;
    align-items: center;
    padding: 12px 16px 12px 16px;
    min-height: 48px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_47812 .Pixso-instance-5629_42500 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5629_51210 .Pixso-instance-5629_42500 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5629_50509 .Pixso-symbol-5629_42611 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 10px;
    justify-content: center;
    align-items: center;
    padding: 12px 16px 12px 16px;
    min-height: 48px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_50509 .stroke-wrapper-5629_42611 {
    width: 120px;
    height: 48px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5629_50509 .stroke-5629_42611 {
    inset: 0px;
    border-radius: 1234px 1234px 1234px 1234px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5629_51270 .Pixso-symbol-5629_42611 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 10px;
    justify-content: center;
    align-items: center;
    padding: 12px 16px 12px 16px;
    min-height: 48px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5629_51270 .stroke-wrapper-5629_42611 {
    width: 131px;
    height: 48px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5629_51270 .stroke-5629_42611 {
    inset: 0px;
    border-radius: 1234px 1234px 1234px 1234px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5629_50509 .Pixso-instance-5629_42612 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5629_51270 .Pixso-instance-5629_42612 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5629_51066 .Pixso-symbol-5629_44462 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 10px;
    justify-content: center;
    align-items: center;
    padding: 12px 16px 12px 16px;
    min-height: 48px;
}
.Pixso-instance-5629_51066 .stroke-wrapper-5629_44462 {
    width: 120px;
    height: 48px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5629_51066 .stroke-5629_44462 {
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 0px 2px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5629_51282 .Pixso-symbol-5629_44462 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 10px;
    justify-content: center;
    align-items: center;
    padding: 12px 16px 12px 16px;
    min-height: 48px;
}
.Pixso-instance-5629_51282 .stroke-wrapper-5629_44462 {
    width: 131px;
    height: 48px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5629_51282 .stroke-5629_44462 {
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 0px 2px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5629_51066 .Pixso-instance-5629_44463 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5629_51282 .Pixso-instance-5629_44463 {
    width: 20px;
    height: 20px;
}
</style>
