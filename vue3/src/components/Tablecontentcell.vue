<template>
    <div class="component-5561_52659">
        <div id="5561_52659" class="Pixso-symbol-5561_52659">
            <div
                id="5561_52629"
                class="stroke-wrapper-5561_52629"
                v-if="
                    Type === 'Text' &&
                    State === 'Default' &&
                    FormControl === 'None'
                "
            >
                <div class="Pixso-symbol-5561_52629 fill-gray0-white-67_3285">
                    <div id="5631_53408" class="Pixso-frame-5631_53408">
                        <div class="frame-content-5631_53408">
                            <slot name="slot_5561_52617" v-if="visible_5986_57">
                                <p
                                    id="5561_52617"
                                    class="Pixso-paragraph-5561_52617 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                                >
                                    {{ text_5565_13 ?? "Main Text" }}
                                </p>
                            </slot>
                            <slot name="slot_5631_53387" v-if="visible_5565_0">
                                <p
                                    id="5631_53387"
                                    class="Pixso-paragraph-5631_53387 fill-gray60-83_2722-paragraph text-paragraphsm-20_2107"
                                >
                                    {{ text_5565_26 ?? "Supporting Text" }}
                                </p>
                            </slot>
                        </div>
                    </div>
                    <slot name="slot_5631_53518" v-if="visible_5634_741">
                        <Info
                            id="5631_53518"
                            class="Pixso-instance-5631_53518"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div class="stroke-5561_52629 stroke-gray20-36_1844"></div>
            </div>
            <div
                id="5631_53447"
                class="stroke-wrapper-5631_53447"
                v-if="
                    Type === 'Avatar Single' &&
                    State === 'Default' &&
                    FormControl === 'None'
                "
            >
                <div class="Pixso-symbol-5631_53447 fill-gray0-white-67_3285">
                    <slot name="slot_5631_53453">
                        <Avatar
                            id="5631_53453"
                            class="Pixso-instance-5631_53453"
                            Size="md"
                            Type="Image"
                            Indicator="None"
                        />
                    </slot>
                    <div id="5631_53448" class="Pixso-frame-5631_53448">
                        <div class="frame-content-5631_53448">
                            <slot name="slot_5631_53449" v-if="visible_5986_57">
                                <p
                                    id="5631_53449"
                                    class="Pixso-paragraph-5631_53449 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                                >
                                    {{ text_5565_13 ?? "Main Text" }}
                                </p>
                            </slot>
                            <slot name="slot_5631_53450" v-if="visible_5565_0">
                                <p
                                    id="5631_53450"
                                    class="Pixso-paragraph-5631_53450 fill-gray60-83_2722-paragraph text-paragraphsm-20_2107"
                                >
                                    {{ text_5565_26 ?? "Supporting Text" }}
                                </p>
                            </slot>
                        </div>
                    </div>
                    <slot name="slot_5631_53575" v-if="visible_5634_741">
                        <Info
                            id="5631_53575"
                            class="Pixso-instance-5631_53575"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div class="stroke-5631_53447 stroke-gray20-36_1844"></div>
            </div>
            <div
                id="5631_53459"
                class="stroke-wrapper-5631_53459"
                v-if="
                    Type === 'Icon' &&
                    State === 'Default' &&
                    FormControl === 'None'
                "
            >
                <div class="Pixso-symbol-5631_53459 fill-gray0-white-67_3285">
                    <slot name="slot_5631_53464">
                        <IconContainer
                            id="5631_53464"
                            class="Pixso-instance-5631_53464"
                            Size="md"
                            Color="Brand"
                            Style="Secondary"
                        >
                            <template #slot_5546_2917>
                                <FileImage
                                    id="5546_2917"
                                    class="Pixso-instance-5546_2917"
                                />
                            </template>
                        </IconContainer>
                    </slot>
                    <div id="5631_53461" class="Pixso-frame-5631_53461">
                        <div class="frame-content-5631_53461">
                            <slot name="slot_5631_53462" v-if="visible_5986_57">
                                <p
                                    id="5631_53462"
                                    class="Pixso-paragraph-5631_53462 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                                >
                                    {{ text_5565_13 ?? "Main Text" }}
                                </p>
                            </slot>
                            <slot name="slot_5631_53463" v-if="visible_5565_0">
                                <p
                                    id="5631_53463"
                                    class="Pixso-paragraph-5631_53463 fill-gray60-83_2722-paragraph text-paragraphsm-20_2107"
                                >
                                    {{ text_5565_26 ?? "Supporting Text" }}
                                </p>
                            </slot>
                        </div>
                    </div>
                    <slot name="slot_5631_53577" v-if="visible_5634_741">
                        <Info
                            id="5631_53577"
                            class="Pixso-instance-5631_53577"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div class="stroke-5631_53459 stroke-gray20-36_1844"></div>
            </div>
            <div
                id="5633_54611"
                class="stroke-wrapper-5633_54611"
                v-if="
                    Type === 'Payment' &&
                    State === 'Default' &&
                    FormControl === 'None'
                "
            >
                <div class="Pixso-symbol-5633_54611 fill-gray0-white-67_3285">
                    <slot name="slot_5633_54620">
                        <PaymentLogo
                            id="5633_54620"
                            class="Pixso-instance-5633_54620"
                            Size="sm"
                            Company="Visa"
                        />
                    </slot>
                    <div id="5633_54613" class="Pixso-frame-5633_54613">
                        <div class="frame-content-5633_54613">
                            <slot name="slot_5633_54614" v-if="visible_5986_57">
                                <p
                                    id="5633_54614"
                                    class="Pixso-paragraph-5633_54614 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                                >
                                    {{ text_5565_13 ?? "Main Text" }}
                                </p>
                            </slot>
                            <slot name="slot_5633_54615" v-if="visible_5565_0">
                                <p
                                    id="5633_54615"
                                    class="Pixso-paragraph-5633_54615 fill-gray60-83_2722-paragraph text-paragraphsm-20_2107"
                                >
                                    {{ text_5565_26 ?? "Supporting Text" }}
                                </p>
                            </slot>
                        </div>
                    </div>
                    <slot name="slot_5633_54616" v-if="visible_5634_741">
                        <Info
                            id="5633_54616"
                            class="Pixso-instance-5633_54616"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div class="stroke-5633_54611 stroke-gray20-36_1844"></div>
            </div>
            <div
                id="5631_53483"
                class="stroke-wrapper-5631_53483"
                v-if="
                    Type === 'Image' &&
                    State === 'Default' &&
                    FormControl === 'None'
                "
            >
                <div class="Pixso-symbol-5631_53483 fill-gray0-white-67_3285">
                    <div id="5631_53490" class="Pixso-frame-5631_53490"></div>
                    <div id="5631_53485" class="Pixso-frame-5631_53485">
                        <div class="frame-content-5631_53485">
                            <slot name="slot_5631_53486" v-if="visible_5986_57">
                                <p
                                    id="5631_53486"
                                    class="Pixso-paragraph-5631_53486 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                                >
                                    {{ text_5565_13 ?? "Main Text" }}
                                </p>
                            </slot>
                            <slot name="slot_5631_53487" v-if="visible_5565_0">
                                <p
                                    id="5631_53487"
                                    class="Pixso-paragraph-5631_53487 fill-gray60-83_2722-paragraph text-paragraphsm-20_2107"
                                >
                                    {{ text_5565_26 ?? "Supporting Text" }}
                                </p>
                            </slot>
                        </div>
                    </div>
                    <slot name="slot_5631_53579" v-if="visible_5634_741">
                        <Info
                            id="5631_53579"
                            class="Pixso-instance-5631_53579"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div class="stroke-5631_53483 stroke-gray20-36_1844"></div>
            </div>
            <div
                id="5631_53496"
                class="stroke-wrapper-5631_53496"
                v-if="
                    Type === 'Flag' &&
                    State === 'Default' &&
                    FormControl === 'None'
                "
            >
                <div class="Pixso-symbol-5631_53496 fill-gray0-white-67_3285">
                    <slot name="slot_5631_53501">
                        <Flags
                            id="5631_53501"
                            class="Pixso-instance-5631_53501"
                            Country="abkhazia"
                        />
                    </slot>
                    <div id="5631_53498" class="Pixso-frame-5631_53498">
                        <div class="frame-content-5631_53498">
                            <slot name="slot_5631_53499" v-if="visible_5986_57">
                                <p
                                    id="5631_53499"
                                    class="Pixso-paragraph-5631_53499 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                                >
                                    {{ text_5565_13 ?? "Main Text" }}
                                </p>
                            </slot>
                            <slot name="slot_5631_53500" v-if="visible_5565_0">
                                <p
                                    id="5631_53500"
                                    class="Pixso-paragraph-5631_53500 fill-gray60-83_2722-paragraph text-paragraphsm-20_2107"
                                >
                                    {{ text_5565_26 ?? "Supporting Text" }}
                                </p>
                            </slot>
                        </div>
                    </div>
                    <slot name="slot_5631_53581" v-if="visible_5634_741">
                        <Info
                            id="5631_53581"
                            class="Pixso-instance-5631_53581"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div class="stroke-5631_53496 stroke-gray20-36_1844"></div>
            </div>
            <div
                id="5631_53793"
                class="stroke-wrapper-5631_53793"
                v-if="
                    Type === 'Progress' &&
                    State === 'Default' &&
                    FormControl === 'None'
                "
            >
                <div class="Pixso-symbol-5631_53793 fill-gray0-white-67_3285">
                    <slot name="slot_5631_53816">
                        <ProgressBar
                            id="5631_53816"
                            class="Pixso-instance-5631_53816"
                            Progression="40"
                            Size="lg"
                            Label="Right"
                        >
                            <template #slot_5631_54072>
                                <ProgressBar
                                    id="5631_54072"
                                    class="Pixso-instance-5631_54072"
                                    Progression="40"
                                    Size="lg"
                                    Label="None"
                                />
                            </template>
                        </ProgressBar>
                    </slot>
                    <slot name="slot_5631_53798" v-if="visible_5634_741">
                        <Info
                            id="5631_53798"
                            class="Pixso-instance-5631_53798"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div class="stroke-5631_53793 stroke-gray20-36_1844"></div>
            </div>
            <div
                id="5633_54346"
                class="stroke-wrapper-5633_54346"
                v-if="
                    Type === 'Input Field' &&
                    State === 'Default' &&
                    FormControl === 'None'
                "
            >
                <div class="Pixso-symbol-5633_54346 fill-gray0-white-67_3285">
                    <slot name="slot_5633_54355">
                        <InputTextBase
                            id="5633_54355"
                            class="Pixso-instance-5633_54355"
                            Type="Number"
                            Size="lg"
                        />
                    </slot>
                    <slot name="slot_5633_54348" v-if="visible_5634_741">
                        <Info
                            id="5633_54348"
                            class="Pixso-instance-5633_54348"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div class="stroke-5633_54346 stroke-gray20-36_1844"></div>
            </div>
            <div
                id="5633_54566"
                class="stroke-wrapper-5633_54566"
                v-if="
                    Type === 'Avatar Group' &&
                    State === 'Default' &&
                    FormControl === 'None'
                "
            >
                <div class="Pixso-symbol-5633_54566 fill-gray0-white-67_3285">
                    <slot name="slot_5633_54576">
                        <AvatarGroup
                            id="5633_54576"
                            class="Pixso-instance-5633_54576"
                            Size="sm"
                            IsAddUser="False"
                            IsMoreUser="True"
                        />
                    </slot>
                    <slot name="slot_5633_54568" v-if="visible_5634_741">
                        <Info
                            id="5633_54568"
                            class="Pixso-instance-5633_54568"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div class="stroke-5633_54566 stroke-gray20-36_1844"></div>
            </div>
            <div
                id="5633_54378"
                class="stroke-wrapper-5633_54378"
                v-if="
                    Type === 'Button Icon' &&
                    State === 'Default' &&
                    FormControl === 'None'
                "
            >
                <div class="Pixso-symbol-5633_54378 fill-gray0-white-67_3285">
                    <slot name="slot_5633_54393">
                        <ButtonIcon
                            id="5633_54393"
                            class="Pixso-instance-5633_54393"
                            Hierarchy="No Fill"
                            Size="md"
                            Color="Gray"
                            State="Default"
                        >
                            <template #slot_5590_22158>
                                <TrashSimple
                                    id="5590_22158"
                                    class="Pixso-instance-5590_22158"
                                />
                            </template>
                        </ButtonIcon>
                    </slot>
                    <slot name="slot_5633_54396">
                        <ButtonIcon
                            id="5633_54396"
                            class="Pixso-instance-5633_54396"
                            Hierarchy="No Fill"
                            Size="md"
                            Color="Gray"
                            State="Default"
                        >
                            <template #slot_5590_22158>
                                <Download
                                    id="5590_22158"
                                    class="Pixso-instance-5590_22158"
                                />
                            </template>
                        </ButtonIcon>
                    </slot>
                    <slot name="slot_5633_54402">
                        <ButtonIcon
                            id="5633_54402"
                            class="Pixso-instance-5633_54402"
                            Hierarchy="No Fill"
                            Size="md"
                            Color="Gray"
                            State="Default"
                        >
                            <template #slot_5590_22158>
                                <DotsThreeVertical
                                    id="5590_22158"
                                    class="Pixso-instance-5590_22158"
                                />
                            </template>
                        </ButtonIcon>
                    </slot>
                </div>
                <div class="stroke-5633_54378 stroke-gray20-36_1844"></div>
            </div>
            <div
                id="5633_54444"
                class="stroke-wrapper-5633_54444"
                v-if="
                    Type === 'Button' &&
                    State === 'Default' &&
                    FormControl === 'None'
                "
            >
                <div class="Pixso-symbol-5633_54444 fill-gray0-white-67_3285">
                    <slot name="slot_5633_54457">
                        <Button
                            id="5633_54457"
                            class="Pixso-instance-5633_54457"
                            :visible_5588_131="false"
                            :visible_5588_152="false"
                            text_5588_173="Delete"
                            Size="md"
                            Color="Destructive"
                            Hierarchy="Link"
                            State="Default"
                        >
                            <template #slot_5603_17591>
                                <p
                                    id="5603_17591"
                                    class="Pixso-paragraph-5603_17591 fill-destructive50-423_3219-paragraph text-text-smbold-423_3208"
                                >
                                    {{ "Delete" }}
                                </p>
                            </template>
                        </Button>
                    </slot>
                    <slot name="slot_5633_54468">
                        <Button
                            id="5633_54468"
                            class="Pixso-instance-5633_54468"
                            :visible_5588_131="false"
                            :visible_5588_152="false"
                            text_5588_173="Edit"
                            Size="md"
                            Color="Brand"
                            Hierarchy="Link"
                            State="Default"
                        >
                            <template #slot_5603_17351>
                                <p
                                    id="5603_17351"
                                    class="Pixso-paragraph-5603_17351 fill-brand60-1257_33467-paragraph text-text-smbold-423_3208"
                                >
                                    {{ "Edit" }}
                                </p>
                            </template>
                        </Button>
                    </slot>
                </div>
                <div class="stroke-5633_54444 stroke-gray20-36_1844"></div>
            </div>
            <div
                id="5633_54418"
                class="stroke-wrapper-5633_54418"
                v-if="
                    Type === 'Rating' &&
                    State === 'Default' &&
                    FormControl === 'None'
                "
            >
                <div class="Pixso-symbol-5633_54418 fill-gray0-white-67_3285">
                    <slot name="slot_5633_54526">
                        <Rating
                            id="5633_54526"
                            class="Pixso-instance-5633_54526"
                            Star="5"
                            Size="md"
                            Color="Default"
                        />
                    </slot>
                    <slot name="slot_5633_54537" v-if="visible_5633_717">
                        <p
                            id="5633_54537"
                            class="Pixso-paragraph-5633_54537 fill-gray60-83_2722-paragraph text-text-mdsemibold-423_3206"
                        >
                            {{ text_5633_729 ?? "4.5" }}
                        </p>
                    </slot>
                </div>
                <div class="stroke-5633_54418 stroke-gray20-36_1844"></div>
            </div>
            <div
                id="5631_53686"
                class="stroke-wrapper-5631_53686"
                v-if="
                    Type === 'Trend' &&
                    State === 'Default' &&
                    FormControl === 'None'
                "
            >
                <div class="Pixso-symbol-5631_53686 fill-gray0-white-67_3285">
                    <div id="5631_53726" class="Pixso-frame-5631_53726">
                        <slot name="slot_5631_53689" v-if="visible_5986_57">
                            <p
                                id="5631_53689"
                                class="Pixso-paragraph-5631_53689 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                            >
                                {{ text_5565_13 ?? "Main Text" }}
                            </p>
                        </slot>
                        <slot name="slot_5631_53709">
                            <BadgeText
                                id="5631_53709"
                                class="Pixso-instance-5631_53709"
                                :visible_5586_119="false"
                                :visible_5586_121="false"
                                text_5588_129="48%"
                                Size="sm"
                                Color="Success"
                                Hierarchy="Secondary"
                                State="Default"
                            >
                                <template #slot_5588_12217>
                                    <TrendUp
                                        id="5588_12217"
                                        class="Pixso-instance-5588_12217"
                                    />
                                </template>
                                <template #slot_5588_12220>
                                    <p
                                        id="5588_12220"
                                        class="Pixso-paragraph-5588_12220 fill-success50-1636_81205-paragraph text-text-xssemibold-439_9521"
                                    >
                                        {{ "48%" }}
                                    </p>
                                </template>
                            </BadgeText>
                        </slot>
                    </div>
                    <slot name="slot_5631_53691" v-if="visible_5634_741">
                        <Info
                            id="5631_53691"
                            class="Pixso-instance-5631_53691"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div class="stroke-5631_53686 stroke-gray20-36_1844"></div>
            </div>
            <div
                id="5633_54639"
                class="stroke-wrapper-5633_54639"
                v-if="
                    Type === 'Badge Single' &&
                    State === 'Default' &&
                    FormControl === 'None'
                "
            >
                <div class="Pixso-symbol-5633_54639 fill-gray0-white-67_3285">
                    <slot name="slot_5633_54642">
                        <BadgeText
                            id="5633_54642"
                            class="Pixso-instance-5633_54642"
                            :visible_5586_119="false"
                            :visible_5586_121="false"
                            :visible_5586_123="false"
                            Size="sm"
                            Color="Brand"
                            Hierarchy="Secondary"
                            State="Default"
                        />
                    </slot>
                    <slot name="slot_5633_54643" v-if="visible_5634_741">
                        <Info
                            id="5633_54643"
                            class="Pixso-instance-5633_54643"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div class="stroke-5633_54639 stroke-gray20-36_1844"></div>
            </div>
            <div
                id="5633_54663"
                class="stroke-wrapper-5633_54663"
                v-if="
                    Type === 'Badge Group' &&
                    State === 'Default' &&
                    FormControl === 'None'
                "
            >
                <div class="Pixso-symbol-5633_54663 fill-gray0-white-67_3285">
                    <div id="5633_54693" class="Pixso-frame-5633_54693">
                        <slot name="slot_5633_54664">
                            <BadgeText
                                id="5633_54664"
                                class="Pixso-instance-5633_54664"
                                :visible_5586_119="false"
                                :visible_5586_121="false"
                                :visible_5586_123="false"
                                Size="sm"
                                Color="Brand"
                                Hierarchy="Secondary"
                                State="Default"
                            />
                        </slot>
                        <slot name="slot_5633_54675">
                            <BadgeText
                                id="5633_54675"
                                class="Pixso-instance-5633_54675"
                                :visible_5586_119="false"
                                :visible_5586_121="false"
                                :visible_5586_123="false"
                                Size="sm"
                                Color="Warning"
                                Hierarchy="Secondary"
                                State="Default"
                            />
                        </slot>
                        <slot name="slot_5633_54684">
                            <BadgeText
                                id="5633_54684"
                                class="Pixso-instance-5633_54684"
                                :visible_5586_119="false"
                                :visible_5586_121="false"
                                :visible_5586_123="false"
                                Size="sm"
                                Color="Destructive"
                                Hierarchy="Secondary"
                                State="Default"
                            />
                        </slot>
                    </div>
                    <slot name="slot_5633_54665" v-if="visible_5634_741">
                        <Info
                            id="5633_54665"
                            class="Pixso-instance-5633_54665"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div class="stroke-5633_54663 stroke-gray20-36_1844"></div>
            </div>
            <div
                id="5634_54959"
                class="stroke-wrapper-5634_54959"
                v-if="
                    Type === 'Text' &&
                    State === 'Hover' &&
                    FormControl === 'None'
                "
            >
                <div class="Pixso-symbol-5634_54959 fill-gray5-32_4120">
                    <div id="5634_54960" class="Pixso-frame-5634_54960">
                        <div class="frame-content-5634_54960">
                            <slot name="slot_5634_54961" v-if="visible_5986_57">
                                <p
                                    id="5634_54961"
                                    class="Pixso-paragraph-5634_54961 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                                >
                                    {{ text_5565_13 ?? "Main Text" }}
                                </p>
                            </slot>
                            <slot name="slot_5634_54962" v-if="visible_5565_0">
                                <p
                                    id="5634_54962"
                                    class="Pixso-paragraph-5634_54962 fill-gray60-83_2722-paragraph text-paragraphsm-20_2107"
                                >
                                    {{ text_5565_26 ?? "Supporting Text" }}
                                </p>
                            </slot>
                        </div>
                    </div>
                    <slot name="slot_5634_54963" v-if="visible_5634_741">
                        <Info
                            id="5634_54963"
                            class="Pixso-instance-5634_54963"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div class="stroke-5634_54959 stroke-gray20-36_1844"></div>
            </div>
            <div
                id="5634_54964"
                class="stroke-wrapper-5634_54964"
                v-if="
                    Type === 'Avatar Single' &&
                    State === 'Hover' &&
                    FormControl === 'None'
                "
            >
                <div class="Pixso-symbol-5634_54964 fill-gray5-32_4120">
                    <slot name="slot_5634_54965">
                        <Avatar
                            id="5634_54965"
                            class="Pixso-instance-5634_54965"
                            Size="md"
                            Type="Image"
                            Indicator="None"
                        />
                    </slot>
                    <div id="5634_54966" class="Pixso-frame-5634_54966">
                        <div class="frame-content-5634_54966">
                            <slot name="slot_5634_54967" v-if="visible_5986_57">
                                <p
                                    id="5634_54967"
                                    class="Pixso-paragraph-5634_54967 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                                >
                                    {{ text_5565_13 ?? "Main Text" }}
                                </p>
                            </slot>
                            <slot name="slot_5634_54968" v-if="visible_5565_0">
                                <p
                                    id="5634_54968"
                                    class="Pixso-paragraph-5634_54968 fill-gray60-83_2722-paragraph text-paragraphsm-20_2107"
                                >
                                    {{ text_5565_26 ?? "Supporting Text" }}
                                </p>
                            </slot>
                        </div>
                    </div>
                    <slot name="slot_5634_54969" v-if="visible_5634_741">
                        <Info
                            id="5634_54969"
                            class="Pixso-instance-5634_54969"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div class="stroke-5634_54964 stroke-gray20-36_1844"></div>
            </div>
            <div
                id="5634_54970"
                class="stroke-wrapper-5634_54970"
                v-if="
                    Type === 'Icon' &&
                    State === 'Hover' &&
                    FormControl === 'None'
                "
            >
                <div class="Pixso-symbol-5634_54970 fill-gray5-32_4120">
                    <slot name="slot_5634_54971">
                        <IconContainer
                            id="5634_54971"
                            class="Pixso-instance-5634_54971"
                            Size="md"
                            Color="Brand"
                            Style="Secondary"
                        >
                            <template #slot_5546_2917>
                                <FileImage
                                    id="5546_2917"
                                    class="Pixso-instance-5546_2917"
                                />
                            </template>
                        </IconContainer>
                    </slot>
                    <div id="5634_54972" class="Pixso-frame-5634_54972">
                        <div class="frame-content-5634_54972">
                            <slot name="slot_5634_54973" v-if="visible_5986_57">
                                <p
                                    id="5634_54973"
                                    class="Pixso-paragraph-5634_54973 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                                >
                                    {{ text_5565_13 ?? "Main Text" }}
                                </p>
                            </slot>
                            <slot name="slot_5634_54974" v-if="visible_5565_0">
                                <p
                                    id="5634_54974"
                                    class="Pixso-paragraph-5634_54974 fill-gray60-83_2722-paragraph text-paragraphsm-20_2107"
                                >
                                    {{ text_5565_26 ?? "Supporting Text" }}
                                </p>
                            </slot>
                        </div>
                    </div>
                    <slot name="slot_5634_54975" v-if="visible_5634_741">
                        <Info
                            id="5634_54975"
                            class="Pixso-instance-5634_54975"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div class="stroke-5634_54970 stroke-gray20-36_1844"></div>
            </div>
            <div
                id="5634_54976"
                class="stroke-wrapper-5634_54976"
                v-if="
                    Type === 'Payment' &&
                    State === 'Hover' &&
                    FormControl === 'None'
                "
            >
                <div class="Pixso-symbol-5634_54976 fill-gray5-32_4120">
                    <slot name="slot_5634_54977">
                        <PaymentLogo
                            id="5634_54977"
                            class="Pixso-instance-5634_54977"
                            Size="sm"
                            Company="Visa"
                        />
                    </slot>
                    <div id="5634_54978" class="Pixso-frame-5634_54978">
                        <div class="frame-content-5634_54978">
                            <slot name="slot_5634_54979" v-if="visible_5986_57">
                                <p
                                    id="5634_54979"
                                    class="Pixso-paragraph-5634_54979 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                                >
                                    {{ text_5565_13 ?? "Main Text" }}
                                </p>
                            </slot>
                            <slot name="slot_5634_54980" v-if="visible_5565_0">
                                <p
                                    id="5634_54980"
                                    class="Pixso-paragraph-5634_54980 fill-gray60-83_2722-paragraph text-paragraphsm-20_2107"
                                >
                                    {{ text_5565_26 ?? "Supporting Text" }}
                                </p>
                            </slot>
                        </div>
                    </div>
                    <slot name="slot_5634_54981" v-if="visible_5634_741">
                        <Info
                            id="5634_54981"
                            class="Pixso-instance-5634_54981"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div class="stroke-5634_54976 stroke-gray20-36_1844"></div>
            </div>
            <div
                id="5634_54982"
                class="stroke-wrapper-5634_54982"
                v-if="
                    Type === 'Image' &&
                    State === 'Hover' &&
                    FormControl === 'None'
                "
            >
                <div class="Pixso-symbol-5634_54982 fill-gray5-32_4120">
                    <div id="5634_54983" class="Pixso-frame-5634_54983"></div>
                    <div id="5634_54984" class="Pixso-frame-5634_54984">
                        <div class="frame-content-5634_54984">
                            <slot name="slot_5634_54985" v-if="visible_5986_57">
                                <p
                                    id="5634_54985"
                                    class="Pixso-paragraph-5634_54985 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                                >
                                    {{ text_5565_13 ?? "Main Text" }}
                                </p>
                            </slot>
                            <slot name="slot_5634_54986" v-if="visible_5565_0">
                                <p
                                    id="5634_54986"
                                    class="Pixso-paragraph-5634_54986 fill-gray60-83_2722-paragraph text-paragraphsm-20_2107"
                                >
                                    {{ text_5565_26 ?? "Supporting Text" }}
                                </p>
                            </slot>
                        </div>
                    </div>
                    <slot name="slot_5634_54987" v-if="visible_5634_741">
                        <Info
                            id="5634_54987"
                            class="Pixso-instance-5634_54987"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div class="stroke-5634_54982 stroke-gray20-36_1844"></div>
            </div>
            <div
                id="5634_54988"
                class="stroke-wrapper-5634_54988"
                v-if="
                    Type === 'Flag' &&
                    State === 'Hover' &&
                    FormControl === 'None'
                "
            >
                <div class="Pixso-symbol-5634_54988 fill-gray5-32_4120">
                    <slot name="slot_5634_54989">
                        <Flags
                            id="5634_54989"
                            class="Pixso-instance-5634_54989"
                            Country="abkhazia"
                        />
                    </slot>
                    <div id="5634_54990" class="Pixso-frame-5634_54990">
                        <div class="frame-content-5634_54990">
                            <slot name="slot_5634_54991" v-if="visible_5986_57">
                                <p
                                    id="5634_54991"
                                    class="Pixso-paragraph-5634_54991 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                                >
                                    {{ text_5565_13 ?? "Main Text" }}
                                </p>
                            </slot>
                            <slot name="slot_5634_54992" v-if="visible_5565_0">
                                <p
                                    id="5634_54992"
                                    class="Pixso-paragraph-5634_54992 fill-gray60-83_2722-paragraph text-paragraphsm-20_2107"
                                >
                                    {{ text_5565_26 ?? "Supporting Text" }}
                                </p>
                            </slot>
                        </div>
                    </div>
                    <slot name="slot_5634_54993" v-if="visible_5634_741">
                        <Info
                            id="5634_54993"
                            class="Pixso-instance-5634_54993"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div class="stroke-5634_54988 stroke-gray20-36_1844"></div>
            </div>
            <div
                id="5634_54994"
                class="stroke-wrapper-5634_54994"
                v-if="
                    Type === 'Progress' &&
                    State === 'Hover' &&
                    FormControl === 'None'
                "
            >
                <div class="Pixso-symbol-5634_54994 fill-gray5-32_4120">
                    <slot name="slot_5634_54995">
                        <ProgressBar
                            id="5634_54995"
                            class="Pixso-instance-5634_54995"
                            Progression="40"
                            Size="lg"
                            Label="Right"
                        >
                            <template #slot_5631_54072>
                                <ProgressBar
                                    id="5631_54072"
                                    class="Pixso-instance-5631_54072"
                                    Progression="40"
                                    Size="lg"
                                    Label="None"
                                />
                            </template>
                        </ProgressBar>
                    </slot>
                    <slot name="slot_5634_54996" v-if="visible_5634_741">
                        <Info
                            id="5634_54996"
                            class="Pixso-instance-5634_54996"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div class="stroke-5634_54994 stroke-gray20-36_1844"></div>
            </div>
            <div
                id="5634_54997"
                class="stroke-wrapper-5634_54997"
                v-if="
                    Type === 'Input Field' &&
                    State === 'Hover' &&
                    FormControl === 'None'
                "
            >
                <div class="Pixso-symbol-5634_54997 fill-gray5-32_4120">
                    <slot name="slot_5634_54998">
                        <InputTextBase
                            id="5634_54998"
                            class="Pixso-instance-5634_54998"
                            Type="Number"
                            Size="lg"
                        />
                    </slot>
                    <slot name="slot_5634_54999" v-if="visible_5634_741">
                        <Info
                            id="5634_54999"
                            class="Pixso-instance-5634_54999"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div class="stroke-5634_54997 stroke-gray20-36_1844"></div>
            </div>
            <div
                id="5634_55000"
                class="stroke-wrapper-5634_55000"
                v-if="
                    Type === 'Avatar Group' &&
                    State === 'Hover' &&
                    FormControl === 'None'
                "
            >
                <div class="Pixso-symbol-5634_55000 fill-gray5-32_4120">
                    <slot name="slot_5634_55001">
                        <AvatarGroup
                            id="5634_55001"
                            class="Pixso-instance-5634_55001"
                            Size="sm"
                            IsAddUser="False"
                            IsMoreUser="True"
                        />
                    </slot>
                    <slot name="slot_5634_55002" v-if="visible_5634_741">
                        <Info
                            id="5634_55002"
                            class="Pixso-instance-5634_55002"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div class="stroke-5634_55000 stroke-gray20-36_1844"></div>
            </div>
            <div
                id="5634_55003"
                class="stroke-wrapper-5634_55003"
                v-if="
                    Type === 'Button Icon' &&
                    State === 'Hover' &&
                    FormControl === 'None'
                "
            >
                <div class="Pixso-symbol-5634_55003 fill-gray5-32_4120">
                    <slot name="slot_5634_55004">
                        <ButtonIcon
                            id="5634_55004"
                            class="Pixso-instance-5634_55004"
                            Hierarchy="No Fill"
                            Size="md"
                            Color="Gray"
                            State="Default"
                        >
                            <template #slot_5590_22158>
                                <TrashSimple
                                    id="5590_22158"
                                    class="Pixso-instance-5590_22158"
                                />
                            </template>
                        </ButtonIcon>
                    </slot>
                    <slot name="slot_5634_55005">
                        <ButtonIcon
                            id="5634_55005"
                            class="Pixso-instance-5634_55005"
                            Hierarchy="No Fill"
                            Size="md"
                            Color="Gray"
                            State="Default"
                        >
                            <template #slot_5590_22158>
                                <Download
                                    id="5590_22158"
                                    class="Pixso-instance-5590_22158"
                                />
                            </template>
                        </ButtonIcon>
                    </slot>
                    <slot name="slot_5634_55006">
                        <ButtonIcon
                            id="5634_55006"
                            class="Pixso-instance-5634_55006"
                            Hierarchy="No Fill"
                            Size="md"
                            Color="Gray"
                            State="Default"
                        >
                            <template #slot_5590_22158>
                                <DotsThreeVertical
                                    id="5590_22158"
                                    class="Pixso-instance-5590_22158"
                                />
                            </template>
                        </ButtonIcon>
                    </slot>
                </div>
                <div class="stroke-5634_55003 stroke-gray20-36_1844"></div>
            </div>
            <div
                id="5634_55007"
                class="stroke-wrapper-5634_55007"
                v-if="
                    Type === 'Button' &&
                    State === 'Hover' &&
                    FormControl === 'None'
                "
            >
                <div class="Pixso-symbol-5634_55007 fill-gray5-32_4120">
                    <slot name="slot_5634_55008">
                        <Button
                            id="5634_55008"
                            class="Pixso-instance-5634_55008"
                            :visible_5588_131="false"
                            :visible_5588_152="false"
                            text_5588_173="Delete"
                            Size="md"
                            Color="Destructive"
                            Hierarchy="Link"
                            State="Default"
                        >
                            <template #slot_5603_17591>
                                <p
                                    id="5603_17591"
                                    class="Pixso-paragraph-5603_17591 fill-destructive50-423_3219-paragraph text-text-smbold-423_3208"
                                >
                                    {{ "Delete" }}
                                </p>
                            </template>
                        </Button>
                    </slot>
                    <slot name="slot_5634_55009">
                        <Button
                            id="5634_55009"
                            class="Pixso-instance-5634_55009"
                            :visible_5588_131="false"
                            :visible_5588_152="false"
                            text_5588_173="Edit"
                            Size="md"
                            Color="Brand"
                            Hierarchy="Link"
                            State="Default"
                        >
                            <template #slot_5603_17351>
                                <p
                                    id="5603_17351"
                                    class="Pixso-paragraph-5603_17351 fill-brand60-1257_33467-paragraph text-text-smbold-423_3208"
                                >
                                    {{ "Edit" }}
                                </p>
                            </template>
                        </Button>
                    </slot>
                </div>
                <div class="stroke-5634_55007 stroke-gray20-36_1844"></div>
            </div>
            <div
                id="5634_55010"
                class="stroke-wrapper-5634_55010"
                v-if="
                    Type === 'Rating' &&
                    State === 'Hover' &&
                    FormControl === 'None'
                "
            >
                <div class="Pixso-symbol-5634_55010 fill-gray5-32_4120">
                    <slot name="slot_5634_55011">
                        <Rating
                            id="5634_55011"
                            class="Pixso-instance-5634_55011"
                            Star="5"
                            Size="md"
                            Color="Default"
                        />
                    </slot>
                    <slot name="slot_5634_55012" v-if="visible_5633_717">
                        <p
                            id="5634_55012"
                            class="Pixso-paragraph-5634_55012 fill-gray60-83_2722-paragraph text-text-mdsemibold-423_3206"
                        >
                            {{ text_5633_729 ?? "4.5" }}
                        </p>
                    </slot>
                </div>
                <div class="stroke-5634_55010 stroke-gray20-36_1844"></div>
            </div>
            <div
                id="5634_55013"
                class="stroke-wrapper-5634_55013"
                v-if="
                    Type === 'Trend' &&
                    State === 'Hover' &&
                    FormControl === 'None'
                "
            >
                <div class="Pixso-symbol-5634_55013 fill-gray5-32_4120">
                    <div id="5634_55014" class="Pixso-frame-5634_55014">
                        <slot name="slot_5634_55015" v-if="visible_5986_57">
                            <p
                                id="5634_55015"
                                class="Pixso-paragraph-5634_55015 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                            >
                                {{ text_5565_13 ?? "Main Text" }}
                            </p>
                        </slot>
                        <slot name="slot_5634_55016">
                            <BadgeText
                                id="5634_55016"
                                class="Pixso-instance-5634_55016"
                                :visible_5586_119="false"
                                :visible_5586_121="false"
                                text_5588_129="48%"
                                Size="sm"
                                Color="Success"
                                Hierarchy="Secondary"
                                State="Default"
                            >
                                <template #slot_5588_12217>
                                    <TrendUp
                                        id="5588_12217"
                                        class="Pixso-instance-5588_12217"
                                    />
                                </template>
                                <template #slot_5588_12220>
                                    <p
                                        id="5588_12220"
                                        class="Pixso-paragraph-5588_12220 fill-success50-1636_81205-paragraph text-text-xssemibold-439_9521"
                                    >
                                        {{ "48%" }}
                                    </p>
                                </template>
                            </BadgeText>
                        </slot>
                    </div>
                    <slot name="slot_5634_55017" v-if="visible_5634_741">
                        <Info
                            id="5634_55017"
                            class="Pixso-instance-5634_55017"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div class="stroke-5634_55013 stroke-gray20-36_1844"></div>
            </div>
            <div
                id="5634_55018"
                class="stroke-wrapper-5634_55018"
                v-if="
                    Type === 'Badge Single' &&
                    State === 'Hover' &&
                    FormControl === 'None'
                "
            >
                <div class="Pixso-symbol-5634_55018 fill-gray5-32_4120">
                    <slot name="slot_5634_55019">
                        <BadgeText
                            id="5634_55019"
                            class="Pixso-instance-5634_55019"
                            :visible_5586_119="false"
                            :visible_5586_121="false"
                            :visible_5586_123="false"
                            Size="sm"
                            Color="Brand"
                            Hierarchy="Secondary"
                            State="Hover"
                        />
                    </slot>
                    <slot name="slot_5634_55020" v-if="visible_5634_741">
                        <Info
                            id="5634_55020"
                            class="Pixso-instance-5634_55020"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div class="stroke-5634_55018 stroke-gray20-36_1844"></div>
            </div>
            <div
                id="5634_55021"
                class="stroke-wrapper-5634_55021"
                v-if="
                    Type === 'Badge Group' &&
                    State === 'Hover' &&
                    FormControl === 'None'
                "
            >
                <div class="Pixso-symbol-5634_55021 fill-gray5-32_4120">
                    <div id="5634_55022" class="Pixso-frame-5634_55022">
                        <slot name="slot_5634_55023">
                            <BadgeText
                                id="5634_55023"
                                class="Pixso-instance-5634_55023"
                                :visible_5586_119="false"
                                :visible_5586_121="false"
                                :visible_5586_123="false"
                                Size="sm"
                                Color="Brand"
                                Hierarchy="Secondary"
                                State="Hover"
                            />
                        </slot>
                        <slot name="slot_5634_55024">
                            <BadgeText
                                id="5634_55024"
                                class="Pixso-instance-5634_55024"
                                :visible_5586_119="false"
                                :visible_5586_121="false"
                                :visible_5586_123="false"
                                Size="sm"
                                Color="Warning"
                                Hierarchy="Secondary"
                                State="Hover"
                            />
                        </slot>
                        <slot name="slot_5634_55025">
                            <BadgeText
                                id="5634_55025"
                                class="Pixso-instance-5634_55025"
                                :visible_5586_119="false"
                                :visible_5586_121="false"
                                :visible_5586_123="false"
                                Size="sm"
                                Color="Destructive"
                                Hierarchy="Secondary"
                                State="Hover"
                            />
                        </slot>
                    </div>
                    <slot name="slot_5634_55026" v-if="visible_5634_741">
                        <Info
                            id="5634_55026"
                            class="Pixso-instance-5634_55026"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div class="stroke-5634_55021 stroke-gray20-36_1844"></div>
            </div>
            <div
                id="5634_55525"
                class="stroke-wrapper-5634_55525"
                v-if="
                    Type === 'Text' &&
                    State === 'Default' &&
                    FormControl === 'Checkbox'
                "
            >
                <div class="Pixso-symbol-5634_55525 fill-gray0-white-67_3285">
                    <slot name="slot_5634_55906">
                        <CheckboxOnly
                            id="5634_55906"
                            class="Pixso-instance-5634_55906"
                            Size="md"
                            State="Defaut"
                            IsIndeterminate="False"
                            IsChecked="False"
                        />
                    </slot>
                    <div id="5634_55526" class="Pixso-frame-5634_55526">
                        <div class="frame-content-5634_55526">
                            <slot name="slot_5634_55527" v-if="visible_5986_57">
                                <p
                                    id="5634_55527"
                                    class="Pixso-paragraph-5634_55527 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                                >
                                    {{ text_5565_13 ?? "Main Text" }}
                                </p>
                            </slot>
                            <slot name="slot_5634_55528" v-if="visible_5565_0">
                                <p
                                    id="5634_55528"
                                    class="Pixso-paragraph-5634_55528 fill-gray60-83_2722-paragraph text-paragraphsm-20_2107"
                                >
                                    {{ text_5565_26 ?? "Supporting Text" }}
                                </p>
                            </slot>
                        </div>
                    </div>
                    <slot name="slot_5634_55529" v-if="visible_5634_741">
                        <Info
                            id="5634_55529"
                            class="Pixso-instance-5634_55529"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div class="stroke-5634_55525 stroke-gray20-36_1844"></div>
            </div>
            <div
                id="5634_57284"
                class="stroke-wrapper-5634_57284"
                v-if="
                    Type === 'Text' &&
                    State === 'Default' &&
                    FormControl === 'Radio'
                "
            >
                <div class="Pixso-symbol-5634_57284 fill-gray0-white-67_3285">
                    <slot name="slot_5634_57285">
                        <RadioOnly
                            id="5634_57285"
                            class="Pixso-instance-5634_57285"
                            Size="md"
                            State="Default"
                            IsChecked="False"
                        />
                    </slot>
                    <div id="5634_57286" class="Pixso-frame-5634_57286">
                        <div class="frame-content-5634_57286">
                            <slot name="slot_5634_57287" v-if="visible_5986_57">
                                <p
                                    id="5634_57287"
                                    class="Pixso-paragraph-5634_57287 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                                >
                                    {{ text_5565_13 ?? "Main Text" }}
                                </p>
                            </slot>
                            <slot name="slot_5634_57288" v-if="visible_5565_0">
                                <p
                                    id="5634_57288"
                                    class="Pixso-paragraph-5634_57288 fill-gray60-83_2722-paragraph text-paragraphsm-20_2107"
                                >
                                    {{ text_5565_26 ?? "Supporting Text" }}
                                </p>
                            </slot>
                        </div>
                    </div>
                    <slot name="slot_5634_57289" v-if="visible_5634_741">
                        <Info
                            id="5634_57289"
                            class="Pixso-instance-5634_57289"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div class="stroke-5634_57284 stroke-gray20-36_1844"></div>
            </div>
            <div
                id="5634_58255"
                class="stroke-wrapper-5634_58255"
                v-if="
                    Type === 'Text' &&
                    State === 'Default' &&
                    FormControl === 'Toggle'
                "
            >
                <div class="Pixso-symbol-5634_58255 fill-gray0-white-67_3285">
                    <slot name="slot_5634_58256">
                        <ToggleOnly
                            id="5634_58256"
                            class="Pixso-instance-5634_58256"
                            IsActive="False"
                            Size="md"
                            State="Default"
                            IsIcon="False"
                        />
                    </slot>
                    <div id="5634_58257" class="Pixso-frame-5634_58257">
                        <div class="frame-content-5634_58257">
                            <slot name="slot_5634_58258" v-if="visible_5986_57">
                                <p
                                    id="5634_58258"
                                    class="Pixso-paragraph-5634_58258 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                                >
                                    {{ text_5565_13 ?? "Main Text" }}
                                </p>
                            </slot>
                            <slot name="slot_5634_58259" v-if="visible_5565_0">
                                <p
                                    id="5634_58259"
                                    class="Pixso-paragraph-5634_58259 fill-gray60-83_2722-paragraph text-paragraphsm-20_2107"
                                >
                                    {{ text_5565_26 ?? "Supporting Text" }}
                                </p>
                            </slot>
                        </div>
                    </div>
                    <slot name="slot_5634_58260" v-if="visible_5634_741">
                        <Info
                            id="5634_58260"
                            class="Pixso-instance-5634_58260"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div class="stroke-5634_58255 stroke-gray20-36_1844"></div>
            </div>
            <div
                id="5634_57676"
                class="stroke-wrapper-5634_57676"
                v-if="
                    Type === 'Text' &&
                    State === 'Hover' &&
                    FormControl === 'Radio'
                "
            >
                <div class="Pixso-symbol-5634_57676 fill-gray5-32_4120">
                    <slot name="slot_5634_57677">
                        <RadioOnly
                            id="5634_57677"
                            class="Pixso-instance-5634_57677"
                            Size="md"
                            State="Default"
                            IsChecked="False"
                        />
                    </slot>
                    <div id="5634_57678" class="Pixso-frame-5634_57678">
                        <div class="frame-content-5634_57678">
                            <slot name="slot_5634_57679" v-if="visible_5986_57">
                                <p
                                    id="5634_57679"
                                    class="Pixso-paragraph-5634_57679 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                                >
                                    {{ text_5565_13 ?? "Main Text" }}
                                </p>
                            </slot>
                            <slot name="slot_5634_57680" v-if="visible_5565_0">
                                <p
                                    id="5634_57680"
                                    class="Pixso-paragraph-5634_57680 fill-gray60-83_2722-paragraph text-paragraphsm-20_2107"
                                >
                                    {{ text_5565_26 ?? "Supporting Text" }}
                                </p>
                            </slot>
                        </div>
                    </div>
                    <slot name="slot_5634_57681" v-if="visible_5634_741">
                        <Info
                            id="5634_57681"
                            class="Pixso-instance-5634_57681"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div class="stroke-5634_57676 stroke-gray20-36_1844"></div>
            </div>
            <div
                id="5634_58261"
                class="stroke-wrapper-5634_58261"
                v-if="
                    Type === 'Text' &&
                    State === 'Hover' &&
                    FormControl === 'Toggle'
                "
            >
                <div class="Pixso-symbol-5634_58261 fill-gray5-32_4120">
                    <slot name="slot_5634_58262">
                        <ToggleOnly
                            id="5634_58262"
                            class="Pixso-instance-5634_58262"
                            IsActive="False"
                            Size="md"
                            State="Default"
                            IsIcon="False"
                        />
                    </slot>
                    <div id="5634_58263" class="Pixso-frame-5634_58263">
                        <div class="frame-content-5634_58263">
                            <slot name="slot_5634_58264" v-if="visible_5986_57">
                                <p
                                    id="5634_58264"
                                    class="Pixso-paragraph-5634_58264 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                                >
                                    {{ text_5565_13 ?? "Main Text" }}
                                </p>
                            </slot>
                            <slot name="slot_5634_58265" v-if="visible_5565_0">
                                <p
                                    id="5634_58265"
                                    class="Pixso-paragraph-5634_58265 fill-gray60-83_2722-paragraph text-paragraphsm-20_2107"
                                >
                                    {{ text_5565_26 ?? "Supporting Text" }}
                                </p>
                            </slot>
                        </div>
                    </div>
                    <slot name="slot_5634_58266" v-if="visible_5634_741">
                        <Info
                            id="5634_58266"
                            class="Pixso-instance-5634_58266"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div class="stroke-5634_58261 stroke-gray20-36_1844"></div>
            </div>
            <div
                id="5634_55530"
                class="stroke-wrapper-5634_55530"
                v-if="
                    Type === 'Avatar Single' &&
                    State === 'Default' &&
                    FormControl === 'Checkbox'
                "
            >
                <div class="Pixso-symbol-5634_55530 fill-gray0-white-67_3285">
                    <slot name="slot_5634_55907">
                        <CheckboxOnly
                            id="5634_55907"
                            class="Pixso-instance-5634_55907"
                            Size="md"
                            State="Defaut"
                            IsIndeterminate="False"
                            IsChecked="False"
                        />
                    </slot>
                    <slot name="slot_5634_55531">
                        <Avatar
                            id="5634_55531"
                            class="Pixso-instance-5634_55531"
                            Size="md"
                            Type="Image"
                            Indicator="None"
                        />
                    </slot>
                    <div id="5634_55532" class="Pixso-frame-5634_55532">
                        <div class="frame-content-5634_55532">
                            <slot name="slot_5634_55533" v-if="visible_5986_57">
                                <p
                                    id="5634_55533"
                                    class="Pixso-paragraph-5634_55533 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                                >
                                    {{ text_5565_13 ?? "Main Text" }}
                                </p>
                            </slot>
                            <slot name="slot_5634_55534" v-if="visible_5565_0">
                                <p
                                    id="5634_55534"
                                    class="Pixso-paragraph-5634_55534 fill-gray60-83_2722-paragraph text-paragraphsm-20_2107"
                                >
                                    {{ text_5565_26 ?? "Supporting Text" }}
                                </p>
                            </slot>
                        </div>
                    </div>
                    <slot name="slot_5634_55535" v-if="visible_5634_741">
                        <Info
                            id="5634_55535"
                            class="Pixso-instance-5634_55535"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div class="stroke-5634_55530 stroke-gray20-36_1844"></div>
            </div>
            <div
                id="5634_56108"
                class="stroke-wrapper-5634_56108"
                v-if="
                    Type === 'Text' &&
                    State === 'Hover' &&
                    FormControl === 'Checkbox'
                "
            >
                <div class="Pixso-symbol-5634_56108 fill-gray5-32_4120">
                    <slot name="slot_5634_56109">
                        <CheckboxOnly
                            id="5634_56109"
                            class="Pixso-instance-5634_56109"
                            Size="md"
                            State="Defaut"
                            IsIndeterminate="False"
                            IsChecked="False"
                        />
                    </slot>
                    <div id="5634_56110" class="Pixso-frame-5634_56110">
                        <div class="frame-content-5634_56110">
                            <slot name="slot_5634_56111" v-if="visible_5986_57">
                                <p
                                    id="5634_56111"
                                    class="Pixso-paragraph-5634_56111 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                                >
                                    {{ text_5565_13 ?? "Main Text" }}
                                </p>
                            </slot>
                            <slot name="slot_5634_56112" v-if="visible_5565_0">
                                <p
                                    id="5634_56112"
                                    class="Pixso-paragraph-5634_56112 fill-gray60-83_2722-paragraph text-paragraphsm-20_2107"
                                >
                                    {{ text_5565_26 ?? "Supporting Text" }}
                                </p>
                            </slot>
                        </div>
                    </div>
                    <slot name="slot_5634_56113" v-if="visible_5634_741">
                        <Info
                            id="5634_56113"
                            class="Pixso-instance-5634_56113"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div class="stroke-5634_56108 stroke-gray20-36_1844"></div>
            </div>
            <div
                id="5634_57290"
                class="stroke-wrapper-5634_57290"
                v-if="
                    Type === 'Avatar Single' &&
                    State === 'Default' &&
                    FormControl === 'Radio'
                "
            >
                <div class="Pixso-symbol-5634_57290 fill-gray0-white-67_3285">
                    <slot name="slot_5634_57291">
                        <RadioOnly
                            id="5634_57291"
                            class="Pixso-instance-5634_57291"
                            Size="md"
                            State="Default"
                            IsChecked="False"
                        />
                    </slot>
                    <slot name="slot_5634_57292">
                        <Avatar
                            id="5634_57292"
                            class="Pixso-instance-5634_57292"
                            Size="md"
                            Type="Image"
                            Indicator="None"
                        />
                    </slot>
                    <div id="5634_57293" class="Pixso-frame-5634_57293">
                        <div class="frame-content-5634_57293">
                            <slot name="slot_5634_57294" v-if="visible_5986_57">
                                <p
                                    id="5634_57294"
                                    class="Pixso-paragraph-5634_57294 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                                >
                                    {{ text_5565_13 ?? "Main Text" }}
                                </p>
                            </slot>
                            <slot name="slot_5634_57295" v-if="visible_5565_0">
                                <p
                                    id="5634_57295"
                                    class="Pixso-paragraph-5634_57295 fill-gray60-83_2722-paragraph text-paragraphsm-20_2107"
                                >
                                    {{ text_5565_26 ?? "Supporting Text" }}
                                </p>
                            </slot>
                        </div>
                    </div>
                    <slot name="slot_5634_57296" v-if="visible_5634_741">
                        <Info
                            id="5634_57296"
                            class="Pixso-instance-5634_57296"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div class="stroke-5634_57290 stroke-gray20-36_1844"></div>
            </div>
            <div
                id="5634_58267"
                class="stroke-wrapper-5634_58267"
                v-if="
                    Type === 'Avatar Single' &&
                    State === 'Default' &&
                    FormControl === 'Toggle'
                "
            >
                <div class="Pixso-symbol-5634_58267 fill-gray0-white-67_3285">
                    <slot name="slot_5634_58268">
                        <ToggleOnly
                            id="5634_58268"
                            class="Pixso-instance-5634_58268"
                            IsActive="False"
                            Size="md"
                            State="Default"
                            IsIcon="False"
                        />
                    </slot>
                    <slot name="slot_5634_58269">
                        <Avatar
                            id="5634_58269"
                            class="Pixso-instance-5634_58269"
                            Size="md"
                            Type="Image"
                            Indicator="None"
                        />
                    </slot>
                    <div id="5634_58270" class="Pixso-frame-5634_58270">
                        <div class="frame-content-5634_58270">
                            <slot name="slot_5634_58271" v-if="visible_5986_57">
                                <p
                                    id="5634_58271"
                                    class="Pixso-paragraph-5634_58271 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                                >
                                    {{ text_5565_13 ?? "Main Text" }}
                                </p>
                            </slot>
                            <slot name="slot_5634_58272" v-if="visible_5565_0">
                                <p
                                    id="5634_58272"
                                    class="Pixso-paragraph-5634_58272 fill-gray60-83_2722-paragraph text-paragraphsm-20_2107"
                                >
                                    {{ text_5565_26 ?? "Supporting Text" }}
                                </p>
                            </slot>
                        </div>
                    </div>
                    <slot name="slot_5634_58273" v-if="visible_5634_741">
                        <Info
                            id="5634_58273"
                            class="Pixso-instance-5634_58273"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div class="stroke-5634_58267 stroke-gray20-36_1844"></div>
            </div>
            <div
                id="5634_55536"
                class="stroke-wrapper-5634_55536"
                v-if="
                    Type === 'Icon' &&
                    State === 'Default' &&
                    FormControl === 'Checkbox'
                "
            >
                <div class="Pixso-symbol-5634_55536 fill-gray0-white-67_3285">
                    <slot name="slot_5634_55908">
                        <CheckboxOnly
                            id="5634_55908"
                            class="Pixso-instance-5634_55908"
                            Size="md"
                            State="Defaut"
                            IsIndeterminate="False"
                            IsChecked="False"
                        />
                    </slot>
                    <slot name="slot_5634_55537">
                        <IconContainer
                            id="5634_55537"
                            class="Pixso-instance-5634_55537"
                            Size="md"
                            Color="Brand"
                            Style="Secondary"
                        >
                            <template #slot_5546_2917>
                                <FileImage
                                    id="5546_2917"
                                    class="Pixso-instance-5546_2917"
                                />
                            </template>
                        </IconContainer>
                    </slot>
                    <div id="5634_55538" class="Pixso-frame-5634_55538">
                        <div class="frame-content-5634_55538">
                            <slot name="slot_5634_55539" v-if="visible_5986_57">
                                <p
                                    id="5634_55539"
                                    class="Pixso-paragraph-5634_55539 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                                >
                                    {{ text_5565_13 ?? "Main Text" }}
                                </p>
                            </slot>
                            <slot name="slot_5634_55540" v-if="visible_5565_0">
                                <p
                                    id="5634_55540"
                                    class="Pixso-paragraph-5634_55540 fill-gray60-83_2722-paragraph text-paragraphsm-20_2107"
                                >
                                    {{ text_5565_26 ?? "Supporting Text" }}
                                </p>
                            </slot>
                        </div>
                    </div>
                    <slot name="slot_5634_55541" v-if="visible_5634_741">
                        <Info
                            id="5634_55541"
                            class="Pixso-instance-5634_55541"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div class="stroke-5634_55536 stroke-gray20-36_1844"></div>
            </div>
            <div
                id="5634_57682"
                class="stroke-wrapper-5634_57682"
                v-if="
                    Type === 'Avatar Single' &&
                    State === 'Hover' &&
                    FormControl === 'Radio'
                "
            >
                <div class="Pixso-symbol-5634_57682 fill-gray5-32_4120">
                    <slot name="slot_5634_57683">
                        <RadioOnly
                            id="5634_57683"
                            class="Pixso-instance-5634_57683"
                            Size="md"
                            State="Default"
                            IsChecked="False"
                        />
                    </slot>
                    <slot name="slot_5634_57684">
                        <Avatar
                            id="5634_57684"
                            class="Pixso-instance-5634_57684"
                            Size="md"
                            Type="Image"
                            Indicator="None"
                        />
                    </slot>
                    <div id="5634_57685" class="Pixso-frame-5634_57685">
                        <div class="frame-content-5634_57685">
                            <slot name="slot_5634_57686" v-if="visible_5986_57">
                                <p
                                    id="5634_57686"
                                    class="Pixso-paragraph-5634_57686 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                                >
                                    {{ text_5565_13 ?? "Main Text" }}
                                </p>
                            </slot>
                            <slot name="slot_5634_57687" v-if="visible_5565_0">
                                <p
                                    id="5634_57687"
                                    class="Pixso-paragraph-5634_57687 fill-gray60-83_2722-paragraph text-paragraphsm-20_2107"
                                >
                                    {{ text_5565_26 ?? "Supporting Text" }}
                                </p>
                            </slot>
                        </div>
                    </div>
                    <slot name="slot_5634_57688" v-if="visible_5634_741">
                        <Info
                            id="5634_57688"
                            class="Pixso-instance-5634_57688"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div class="stroke-5634_57682 stroke-gray20-36_1844"></div>
            </div>
            <div
                id="5634_58274"
                class="stroke-wrapper-5634_58274"
                v-if="
                    Type === 'Avatar Single' &&
                    State === 'Hover' &&
                    FormControl === 'Toggle'
                "
            >
                <div class="Pixso-symbol-5634_58274 fill-gray5-32_4120">
                    <slot name="slot_5634_58275">
                        <ToggleOnly
                            id="5634_58275"
                            class="Pixso-instance-5634_58275"
                            IsActive="False"
                            Size="md"
                            State="Default"
                            IsIcon="False"
                        />
                    </slot>
                    <slot name="slot_5634_58276">
                        <Avatar
                            id="5634_58276"
                            class="Pixso-instance-5634_58276"
                            Size="md"
                            Type="Image"
                            Indicator="None"
                        />
                    </slot>
                    <div id="5634_58277" class="Pixso-frame-5634_58277">
                        <div class="frame-content-5634_58277">
                            <slot name="slot_5634_58278" v-if="visible_5986_57">
                                <p
                                    id="5634_58278"
                                    class="Pixso-paragraph-5634_58278 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                                >
                                    {{ text_5565_13 ?? "Main Text" }}
                                </p>
                            </slot>
                            <slot name="slot_5634_58279" v-if="visible_5565_0">
                                <p
                                    id="5634_58279"
                                    class="Pixso-paragraph-5634_58279 fill-gray60-83_2722-paragraph text-paragraphsm-20_2107"
                                >
                                    {{ text_5565_26 ?? "Supporting Text" }}
                                </p>
                            </slot>
                        </div>
                    </div>
                    <slot name="slot_5634_58280" v-if="visible_5634_741">
                        <Info
                            id="5634_58280"
                            class="Pixso-instance-5634_58280"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div class="stroke-5634_58274 stroke-gray20-36_1844"></div>
            </div>
            <div
                id="5634_55542"
                class="stroke-wrapper-5634_55542"
                v-if="
                    Type === 'Payment' &&
                    State === 'Default' &&
                    FormControl === 'Checkbox'
                "
            >
                <div class="Pixso-symbol-5634_55542 fill-gray0-white-67_3285">
                    <slot name="slot_5634_55909">
                        <CheckboxOnly
                            id="5634_55909"
                            class="Pixso-instance-5634_55909"
                            Size="md"
                            State="Defaut"
                            IsIndeterminate="False"
                            IsChecked="False"
                        />
                    </slot>
                    <slot name="slot_5634_55543">
                        <PaymentLogo
                            id="5634_55543"
                            class="Pixso-instance-5634_55543"
                            Size="sm"
                            Company="Visa"
                        />
                    </slot>
                    <div id="5634_55544" class="Pixso-frame-5634_55544">
                        <div class="frame-content-5634_55544">
                            <slot name="slot_5634_55545" v-if="visible_5986_57">
                                <p
                                    id="5634_55545"
                                    class="Pixso-paragraph-5634_55545 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                                >
                                    {{ text_5565_13 ?? "Main Text" }}
                                </p>
                            </slot>
                            <slot name="slot_5634_55546" v-if="visible_5565_0">
                                <p
                                    id="5634_55546"
                                    class="Pixso-paragraph-5634_55546 fill-gray60-83_2722-paragraph text-paragraphsm-20_2107"
                                >
                                    {{ text_5565_26 ?? "Supporting Text" }}
                                </p>
                            </slot>
                        </div>
                    </div>
                    <slot name="slot_5634_55547" v-if="visible_5634_741">
                        <Info
                            id="5634_55547"
                            class="Pixso-instance-5634_55547"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div class="stroke-5634_55542 stroke-gray20-36_1844"></div>
            </div>
            <div
                id="5634_57297"
                class="stroke-wrapper-5634_57297"
                v-if="
                    Type === 'Icon' &&
                    State === 'Default' &&
                    FormControl === 'Radio'
                "
            >
                <div class="Pixso-symbol-5634_57297 fill-gray0-white-67_3285">
                    <slot name="slot_5634_57298">
                        <RadioOnly
                            id="5634_57298"
                            class="Pixso-instance-5634_57298"
                            Size="md"
                            State="Default"
                            IsChecked="False"
                        />
                    </slot>
                    <slot name="slot_5634_57299">
                        <IconContainer
                            id="5634_57299"
                            class="Pixso-instance-5634_57299"
                            Size="md"
                            Color="Brand"
                            Style="Secondary"
                        >
                            <template #slot_5546_2917>
                                <FileImage
                                    id="5546_2917"
                                    class="Pixso-instance-5546_2917"
                                />
                            </template>
                        </IconContainer>
                    </slot>
                    <div id="5634_57300" class="Pixso-frame-5634_57300">
                        <div class="frame-content-5634_57300">
                            <slot name="slot_5634_57301" v-if="visible_5986_57">
                                <p
                                    id="5634_57301"
                                    class="Pixso-paragraph-5634_57301 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                                >
                                    {{ text_5565_13 ?? "Main Text" }}
                                </p>
                            </slot>
                            <slot name="slot_5634_57302" v-if="visible_5565_0">
                                <p
                                    id="5634_57302"
                                    class="Pixso-paragraph-5634_57302 fill-gray60-83_2722-paragraph text-paragraphsm-20_2107"
                                >
                                    {{ text_5565_26 ?? "Supporting Text" }}
                                </p>
                            </slot>
                        </div>
                    </div>
                    <slot name="slot_5634_57303" v-if="visible_5634_741">
                        <Info
                            id="5634_57303"
                            class="Pixso-instance-5634_57303"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div class="stroke-5634_57297 stroke-gray20-36_1844"></div>
            </div>
            <div
                id="5634_58281"
                class="stroke-wrapper-5634_58281"
                v-if="
                    Type === 'Icon' &&
                    State === 'Default' &&
                    FormControl === 'Toggle'
                "
            >
                <div class="Pixso-symbol-5634_58281 fill-gray0-white-67_3285">
                    <slot name="slot_5634_58282">
                        <ToggleOnly
                            id="5634_58282"
                            class="Pixso-instance-5634_58282"
                            IsActive="False"
                            Size="md"
                            State="Default"
                            IsIcon="False"
                        />
                    </slot>
                    <slot name="slot_5634_58283">
                        <IconContainer
                            id="5634_58283"
                            class="Pixso-instance-5634_58283"
                            Size="md"
                            Color="Brand"
                            Style="Secondary"
                        >
                            <template #slot_5546_2917>
                                <FileImage
                                    id="5546_2917"
                                    class="Pixso-instance-5546_2917"
                                />
                            </template>
                        </IconContainer>
                    </slot>
                    <div id="5634_58284" class="Pixso-frame-5634_58284">
                        <div class="frame-content-5634_58284">
                            <slot name="slot_5634_58285" v-if="visible_5986_57">
                                <p
                                    id="5634_58285"
                                    class="Pixso-paragraph-5634_58285 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                                >
                                    {{ text_5565_13 ?? "Main Text" }}
                                </p>
                            </slot>
                            <slot name="slot_5634_58286" v-if="visible_5565_0">
                                <p
                                    id="5634_58286"
                                    class="Pixso-paragraph-5634_58286 fill-gray60-83_2722-paragraph text-paragraphsm-20_2107"
                                >
                                    {{ text_5565_26 ?? "Supporting Text" }}
                                </p>
                            </slot>
                        </div>
                    </div>
                    <slot name="slot_5634_58287" v-if="visible_5634_741">
                        <Info
                            id="5634_58287"
                            class="Pixso-instance-5634_58287"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div class="stroke-5634_58281 stroke-gray20-36_1844"></div>
            </div>
            <div
                id="5634_56114"
                class="stroke-wrapper-5634_56114"
                v-if="
                    Type === 'Avatar Single' &&
                    State === 'Hover' &&
                    FormControl === 'Checkbox'
                "
            >
                <div class="Pixso-symbol-5634_56114 fill-gray5-32_4120">
                    <slot name="slot_5634_56115">
                        <CheckboxOnly
                            id="5634_56115"
                            class="Pixso-instance-5634_56115"
                            Size="md"
                            State="Defaut"
                            IsIndeterminate="False"
                            IsChecked="False"
                        />
                    </slot>
                    <slot name="slot_5634_56116">
                        <Avatar
                            id="5634_56116"
                            class="Pixso-instance-5634_56116"
                            Size="md"
                            Type="Image"
                            Indicator="None"
                        />
                    </slot>
                    <div id="5634_56117" class="Pixso-frame-5634_56117">
                        <div class="frame-content-5634_56117">
                            <slot name="slot_5634_56118" v-if="visible_5986_57">
                                <p
                                    id="5634_56118"
                                    class="Pixso-paragraph-5634_56118 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                                >
                                    {{ text_5565_13 ?? "Main Text" }}
                                </p>
                            </slot>
                            <slot name="slot_5634_56119" v-if="visible_5565_0">
                                <p
                                    id="5634_56119"
                                    class="Pixso-paragraph-5634_56119 fill-gray60-83_2722-paragraph text-paragraphsm-20_2107"
                                >
                                    {{ text_5565_26 ?? "Supporting Text" }}
                                </p>
                            </slot>
                        </div>
                    </div>
                    <slot name="slot_5634_56120" v-if="visible_5634_741">
                        <Info
                            id="5634_56120"
                            class="Pixso-instance-5634_56120"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div class="stroke-5634_56114 stroke-gray20-36_1844"></div>
            </div>
            <div
                id="5634_55548"
                class="stroke-wrapper-5634_55548"
                v-if="
                    Type === 'Image' &&
                    State === 'Default' &&
                    FormControl === 'Checkbox'
                "
            >
                <div class="Pixso-symbol-5634_55548 fill-gray0-white-67_3285">
                    <slot name="slot_5634_55910">
                        <CheckboxOnly
                            id="5634_55910"
                            class="Pixso-instance-5634_55910"
                            Size="md"
                            State="Defaut"
                            IsIndeterminate="False"
                            IsChecked="False"
                        />
                    </slot>
                    <div id="5634_55549" class="Pixso-frame-5634_55549"></div>
                    <div id="5634_55550" class="Pixso-frame-5634_55550">
                        <div class="frame-content-5634_55550">
                            <slot name="slot_5634_55551" v-if="visible_5986_57">
                                <p
                                    id="5634_55551"
                                    class="Pixso-paragraph-5634_55551 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                                >
                                    {{ text_5565_13 ?? "Main Text" }}
                                </p>
                            </slot>
                            <slot name="slot_5634_55552" v-if="visible_5565_0">
                                <p
                                    id="5634_55552"
                                    class="Pixso-paragraph-5634_55552 fill-gray60-83_2722-paragraph text-paragraphsm-20_2107"
                                >
                                    {{ text_5565_26 ?? "Supporting Text" }}
                                </p>
                            </slot>
                        </div>
                    </div>
                    <slot name="slot_5634_55553" v-if="visible_5634_741">
                        <Info
                            id="5634_55553"
                            class="Pixso-instance-5634_55553"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div class="stroke-5634_55548 stroke-gray20-36_1844"></div>
            </div>
            <div
                id="5634_57689"
                class="stroke-wrapper-5634_57689"
                v-if="
                    Type === 'Icon' &&
                    State === 'Hover' &&
                    FormControl === 'Radio'
                "
            >
                <div class="Pixso-symbol-5634_57689 fill-gray5-32_4120">
                    <slot name="slot_5634_57690">
                        <RadioOnly
                            id="5634_57690"
                            class="Pixso-instance-5634_57690"
                            Size="md"
                            State="Default"
                            IsChecked="False"
                        />
                    </slot>
                    <slot name="slot_5634_57691">
                        <IconContainer
                            id="5634_57691"
                            class="Pixso-instance-5634_57691"
                            Size="md"
                            Color="Brand"
                            Style="Secondary"
                        >
                            <template #slot_5546_2917>
                                <FileImage
                                    id="5546_2917"
                                    class="Pixso-instance-5546_2917"
                                />
                            </template>
                        </IconContainer>
                    </slot>
                    <div id="5634_57692" class="Pixso-frame-5634_57692">
                        <div class="frame-content-5634_57692">
                            <slot name="slot_5634_57693" v-if="visible_5986_57">
                                <p
                                    id="5634_57693"
                                    class="Pixso-paragraph-5634_57693 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                                >
                                    {{ text_5565_13 ?? "Main Text" }}
                                </p>
                            </slot>
                            <slot name="slot_5634_57694" v-if="visible_5565_0">
                                <p
                                    id="5634_57694"
                                    class="Pixso-paragraph-5634_57694 fill-gray60-83_2722-paragraph text-paragraphsm-20_2107"
                                >
                                    {{ text_5565_26 ?? "Supporting Text" }}
                                </p>
                            </slot>
                        </div>
                    </div>
                    <slot name="slot_5634_57695" v-if="visible_5634_741">
                        <Info
                            id="5634_57695"
                            class="Pixso-instance-5634_57695"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div class="stroke-5634_57689 stroke-gray20-36_1844"></div>
            </div>
            <div
                id="5634_58288"
                class="stroke-wrapper-5634_58288"
                v-if="
                    Type === 'Icon' &&
                    State === 'Hover' &&
                    FormControl === 'Toggle'
                "
            >
                <div class="Pixso-symbol-5634_58288 fill-gray5-32_4120">
                    <slot name="slot_5634_58289">
                        <ToggleOnly
                            id="5634_58289"
                            class="Pixso-instance-5634_58289"
                            IsActive="False"
                            Size="md"
                            State="Default"
                            IsIcon="False"
                        />
                    </slot>
                    <slot name="slot_5634_58290">
                        <IconContainer
                            id="5634_58290"
                            class="Pixso-instance-5634_58290"
                            Size="md"
                            Color="Brand"
                            Style="Secondary"
                        >
                            <template #slot_5546_2917>
                                <FileImage
                                    id="5546_2917"
                                    class="Pixso-instance-5546_2917"
                                />
                            </template>
                        </IconContainer>
                    </slot>
                    <div id="5634_58291" class="Pixso-frame-5634_58291">
                        <div class="frame-content-5634_58291">
                            <slot name="slot_5634_58292" v-if="visible_5986_57">
                                <p
                                    id="5634_58292"
                                    class="Pixso-paragraph-5634_58292 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                                >
                                    {{ text_5565_13 ?? "Main Text" }}
                                </p>
                            </slot>
                            <slot name="slot_5634_58293" v-if="visible_5565_0">
                                <p
                                    id="5634_58293"
                                    class="Pixso-paragraph-5634_58293 fill-gray60-83_2722-paragraph text-paragraphsm-20_2107"
                                >
                                    {{ text_5565_26 ?? "Supporting Text" }}
                                </p>
                            </slot>
                        </div>
                    </div>
                    <slot name="slot_5634_58294" v-if="visible_5634_741">
                        <Info
                            id="5634_58294"
                            class="Pixso-instance-5634_58294"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div class="stroke-5634_58288 stroke-gray20-36_1844"></div>
            </div>
            <div
                id="5634_57304"
                class="stroke-wrapper-5634_57304"
                v-if="
                    Type === 'Payment' &&
                    State === 'Default' &&
                    FormControl === 'Radio'
                "
            >
                <div class="Pixso-symbol-5634_57304 fill-gray0-white-67_3285">
                    <slot name="slot_5634_57305">
                        <RadioOnly
                            id="5634_57305"
                            class="Pixso-instance-5634_57305"
                            Size="md"
                            State="Default"
                            IsChecked="False"
                        />
                    </slot>
                    <slot name="slot_5634_57306">
                        <PaymentLogo
                            id="5634_57306"
                            class="Pixso-instance-5634_57306"
                            Size="sm"
                            Company="Visa"
                        />
                    </slot>
                    <div id="5634_57307" class="Pixso-frame-5634_57307">
                        <div class="frame-content-5634_57307">
                            <slot name="slot_5634_57308" v-if="visible_5986_57">
                                <p
                                    id="5634_57308"
                                    class="Pixso-paragraph-5634_57308 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                                >
                                    {{ text_5565_13 ?? "Main Text" }}
                                </p>
                            </slot>
                            <slot name="slot_5634_57309" v-if="visible_5565_0">
                                <p
                                    id="5634_57309"
                                    class="Pixso-paragraph-5634_57309 fill-gray60-83_2722-paragraph text-paragraphsm-20_2107"
                                >
                                    {{ text_5565_26 ?? "Supporting Text" }}
                                </p>
                            </slot>
                        </div>
                    </div>
                    <slot name="slot_5634_57310" v-if="visible_5634_741">
                        <Info
                            id="5634_57310"
                            class="Pixso-instance-5634_57310"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div class="stroke-5634_57304 stroke-gray20-36_1844"></div>
            </div>
            <div
                id="5634_58295"
                class="stroke-wrapper-5634_58295"
                v-if="
                    Type === 'Payment' &&
                    State === 'Default' &&
                    FormControl === 'Toggle'
                "
            >
                <div class="Pixso-symbol-5634_58295 fill-gray0-white-67_3285">
                    <slot name="slot_5634_58296">
                        <ToggleOnly
                            id="5634_58296"
                            class="Pixso-instance-5634_58296"
                            IsActive="False"
                            Size="md"
                            State="Default"
                            IsIcon="False"
                        />
                    </slot>
                    <slot name="slot_5634_58297">
                        <PaymentLogo
                            id="5634_58297"
                            class="Pixso-instance-5634_58297"
                            Size="sm"
                            Company="Visa"
                        />
                    </slot>
                    <div id="5634_58298" class="Pixso-frame-5634_58298">
                        <div class="frame-content-5634_58298">
                            <slot name="slot_5634_58299" v-if="visible_5986_57">
                                <p
                                    id="5634_58299"
                                    class="Pixso-paragraph-5634_58299 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                                >
                                    {{ text_5565_13 ?? "Main Text" }}
                                </p>
                            </slot>
                            <slot name="slot_5634_58300" v-if="visible_5565_0">
                                <p
                                    id="5634_58300"
                                    class="Pixso-paragraph-5634_58300 fill-gray60-83_2722-paragraph text-paragraphsm-20_2107"
                                >
                                    {{ text_5565_26 ?? "Supporting Text" }}
                                </p>
                            </slot>
                        </div>
                    </div>
                    <slot name="slot_5634_58301" v-if="visible_5634_741">
                        <Info
                            id="5634_58301"
                            class="Pixso-instance-5634_58301"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div class="stroke-5634_58295 stroke-gray20-36_1844"></div>
            </div>
            <div
                id="5634_55554"
                class="stroke-wrapper-5634_55554"
                v-if="
                    Type === 'Flag' &&
                    State === 'Default' &&
                    FormControl === 'Checkbox'
                "
            >
                <div class="Pixso-symbol-5634_55554 fill-gray0-white-67_3285">
                    <slot name="slot_5634_55911">
                        <CheckboxOnly
                            id="5634_55911"
                            class="Pixso-instance-5634_55911"
                            Size="md"
                            State="Defaut"
                            IsIndeterminate="False"
                            IsChecked="False"
                        />
                    </slot>
                    <slot name="slot_5634_55555">
                        <Flags
                            id="5634_55555"
                            class="Pixso-instance-5634_55555"
                            Country="abkhazia"
                        />
                    </slot>
                    <div id="5634_55556" class="Pixso-frame-5634_55556">
                        <div class="frame-content-5634_55556">
                            <slot name="slot_5634_55557" v-if="visible_5986_57">
                                <p
                                    id="5634_55557"
                                    class="Pixso-paragraph-5634_55557 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                                >
                                    {{ text_5565_13 ?? "Main Text" }}
                                </p>
                            </slot>
                            <slot name="slot_5634_55558" v-if="visible_5565_0">
                                <p
                                    id="5634_55558"
                                    class="Pixso-paragraph-5634_55558 fill-gray60-83_2722-paragraph text-paragraphsm-20_2107"
                                >
                                    {{ text_5565_26 ?? "Supporting Text" }}
                                </p>
                            </slot>
                        </div>
                    </div>
                    <slot name="slot_5634_55559" v-if="visible_5634_741">
                        <Info
                            id="5634_55559"
                            class="Pixso-instance-5634_55559"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div class="stroke-5634_55554 stroke-gray20-36_1844"></div>
            </div>
            <div
                id="5634_56121"
                class="stroke-wrapper-5634_56121"
                v-if="
                    Type === 'Icon' &&
                    State === 'Hover' &&
                    FormControl === 'Checkbox'
                "
            >
                <div class="Pixso-symbol-5634_56121 fill-gray5-32_4120">
                    <slot name="slot_5634_56122">
                        <CheckboxOnly
                            id="5634_56122"
                            class="Pixso-instance-5634_56122"
                            Size="md"
                            State="Defaut"
                            IsIndeterminate="False"
                            IsChecked="False"
                        />
                    </slot>
                    <slot name="slot_5634_56123">
                        <IconContainer
                            id="5634_56123"
                            class="Pixso-instance-5634_56123"
                            Size="md"
                            Color="Brand"
                            Style="Secondary"
                        >
                            <template #slot_5546_2917>
                                <FileImage
                                    id="5546_2917"
                                    class="Pixso-instance-5546_2917"
                                />
                            </template>
                        </IconContainer>
                    </slot>
                    <div id="5634_56124" class="Pixso-frame-5634_56124">
                        <div class="frame-content-5634_56124">
                            <slot name="slot_5634_56125" v-if="visible_5986_57">
                                <p
                                    id="5634_56125"
                                    class="Pixso-paragraph-5634_56125 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                                >
                                    {{ text_5565_13 ?? "Main Text" }}
                                </p>
                            </slot>
                            <slot name="slot_5634_56126" v-if="visible_5565_0">
                                <p
                                    id="5634_56126"
                                    class="Pixso-paragraph-5634_56126 fill-gray60-83_2722-paragraph text-paragraphsm-20_2107"
                                >
                                    {{ text_5565_26 ?? "Supporting Text" }}
                                </p>
                            </slot>
                        </div>
                    </div>
                    <slot name="slot_5634_56127" v-if="visible_5634_741">
                        <Info
                            id="5634_56127"
                            class="Pixso-instance-5634_56127"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div class="stroke-5634_56121 stroke-gray20-36_1844"></div>
            </div>
            <div
                id="5634_55560"
                class="stroke-wrapper-5634_55560"
                v-if="
                    Type === 'Progress' &&
                    State === 'Default' &&
                    FormControl === 'Checkbox'
                "
            >
                <div class="Pixso-symbol-5634_55560 fill-gray0-white-67_3285">
                    <slot name="slot_5634_55912">
                        <CheckboxOnly
                            id="5634_55912"
                            class="Pixso-instance-5634_55912"
                            Size="md"
                            State="Defaut"
                            IsIndeterminate="False"
                            IsChecked="False"
                        />
                    </slot>
                    <slot name="slot_5634_55561">
                        <ProgressBar
                            id="5634_55561"
                            class="Pixso-instance-5634_55561"
                            Progression="40"
                            Size="lg"
                            Label="Right"
                        >
                            <template #slot_5631_54072>
                                <ProgressBar
                                    id="5631_54072"
                                    class="Pixso-instance-5631_54072"
                                    Progression="40"
                                    Size="lg"
                                    Label="None"
                                />
                            </template>
                        </ProgressBar>
                    </slot>
                    <slot name="slot_5634_55562" v-if="visible_5634_741">
                        <Info
                            id="5634_55562"
                            class="Pixso-instance-5634_55562"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div class="stroke-5634_55560 stroke-gray20-36_1844"></div>
            </div>
            <div
                id="5634_57311"
                class="stroke-wrapper-5634_57311"
                v-if="
                    Type === 'Image' &&
                    State === 'Default' &&
                    FormControl === 'Radio'
                "
            >
                <div class="Pixso-symbol-5634_57311 fill-gray0-white-67_3285">
                    <slot name="slot_5634_57312">
                        <RadioOnly
                            id="5634_57312"
                            class="Pixso-instance-5634_57312"
                            Size="md"
                            State="Default"
                            IsChecked="False"
                        />
                    </slot>
                    <div id="5634_57313" class="Pixso-frame-5634_57313"></div>
                    <div id="5634_57314" class="Pixso-frame-5634_57314">
                        <div class="frame-content-5634_57314">
                            <slot name="slot_5634_57315" v-if="visible_5986_57">
                                <p
                                    id="5634_57315"
                                    class="Pixso-paragraph-5634_57315 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                                >
                                    {{ text_5565_13 ?? "Main Text" }}
                                </p>
                            </slot>
                            <slot name="slot_5634_57316" v-if="visible_5565_0">
                                <p
                                    id="5634_57316"
                                    class="Pixso-paragraph-5634_57316 fill-gray60-83_2722-paragraph text-paragraphsm-20_2107"
                                >
                                    {{ text_5565_26 ?? "Supporting Text" }}
                                </p>
                            </slot>
                        </div>
                    </div>
                    <slot name="slot_5634_57317" v-if="visible_5634_741">
                        <Info
                            id="5634_57317"
                            class="Pixso-instance-5634_57317"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div class="stroke-5634_57311 stroke-gray20-36_1844"></div>
            </div>
            <div
                id="5634_58302"
                class="stroke-wrapper-5634_58302"
                v-if="
                    Type === 'Image' &&
                    State === 'Default' &&
                    FormControl === 'Toggle'
                "
            >
                <div class="Pixso-symbol-5634_58302 fill-gray0-white-67_3285">
                    <slot name="slot_5634_58303">
                        <ToggleOnly
                            id="5634_58303"
                            class="Pixso-instance-5634_58303"
                            IsActive="False"
                            Size="md"
                            State="Default"
                            IsIcon="False"
                        />
                    </slot>
                    <div id="5634_58304" class="Pixso-frame-5634_58304"></div>
                    <div id="5634_58305" class="Pixso-frame-5634_58305">
                        <div class="frame-content-5634_58305">
                            <slot name="slot_5634_58306" v-if="visible_5986_57">
                                <p
                                    id="5634_58306"
                                    class="Pixso-paragraph-5634_58306 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                                >
                                    {{ text_5565_13 ?? "Main Text" }}
                                </p>
                            </slot>
                            <slot name="slot_5634_58307" v-if="visible_5565_0">
                                <p
                                    id="5634_58307"
                                    class="Pixso-paragraph-5634_58307 fill-gray60-83_2722-paragraph text-paragraphsm-20_2107"
                                >
                                    {{ text_5565_26 ?? "Supporting Text" }}
                                </p>
                            </slot>
                        </div>
                    </div>
                    <slot name="slot_5634_58308" v-if="visible_5634_741">
                        <Info
                            id="5634_58308"
                            class="Pixso-instance-5634_58308"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div class="stroke-5634_58302 stroke-gray20-36_1844"></div>
            </div>
            <div
                id="5634_57696"
                class="stroke-wrapper-5634_57696"
                v-if="
                    Type === 'Payment' &&
                    State === 'Hover' &&
                    FormControl === 'Radio'
                "
            >
                <div class="Pixso-symbol-5634_57696 fill-gray5-32_4120">
                    <slot name="slot_5634_57697">
                        <RadioOnly
                            id="5634_57697"
                            class="Pixso-instance-5634_57697"
                            Size="md"
                            State="Default"
                            IsChecked="False"
                        />
                    </slot>
                    <slot name="slot_5634_57698">
                        <PaymentLogo
                            id="5634_57698"
                            class="Pixso-instance-5634_57698"
                            Size="sm"
                            Company="Visa"
                        />
                    </slot>
                    <div id="5634_57699" class="Pixso-frame-5634_57699">
                        <div class="frame-content-5634_57699">
                            <slot name="slot_5634_57700" v-if="visible_5986_57">
                                <p
                                    id="5634_57700"
                                    class="Pixso-paragraph-5634_57700 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                                >
                                    {{ text_5565_13 ?? "Main Text" }}
                                </p>
                            </slot>
                            <slot name="slot_5634_57701" v-if="visible_5565_0">
                                <p
                                    id="5634_57701"
                                    class="Pixso-paragraph-5634_57701 fill-gray60-83_2722-paragraph text-paragraphsm-20_2107"
                                >
                                    {{ text_5565_26 ?? "Supporting Text" }}
                                </p>
                            </slot>
                        </div>
                    </div>
                    <slot name="slot_5634_57702" v-if="visible_5634_741">
                        <Info
                            id="5634_57702"
                            class="Pixso-instance-5634_57702"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div class="stroke-5634_57696 stroke-gray20-36_1844"></div>
            </div>
            <div
                id="5634_58309"
                class="stroke-wrapper-5634_58309"
                v-if="
                    Type === 'Payment' &&
                    State === 'Hover' &&
                    FormControl === 'Toggle'
                "
            >
                <div class="Pixso-symbol-5634_58309 fill-gray5-32_4120">
                    <slot name="slot_5634_58310">
                        <ToggleOnly
                            id="5634_58310"
                            class="Pixso-instance-5634_58310"
                            IsActive="False"
                            Size="md"
                            State="Default"
                            IsIcon="False"
                        />
                    </slot>
                    <slot name="slot_5634_58311">
                        <PaymentLogo
                            id="5634_58311"
                            class="Pixso-instance-5634_58311"
                            Size="sm"
                            Company="Visa"
                        />
                    </slot>
                    <div id="5634_58312" class="Pixso-frame-5634_58312">
                        <div class="frame-content-5634_58312">
                            <slot name="slot_5634_58313" v-if="visible_5986_57">
                                <p
                                    id="5634_58313"
                                    class="Pixso-paragraph-5634_58313 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                                >
                                    {{ text_5565_13 ?? "Main Text" }}
                                </p>
                            </slot>
                            <slot name="slot_5634_58314" v-if="visible_5565_0">
                                <p
                                    id="5634_58314"
                                    class="Pixso-paragraph-5634_58314 fill-gray60-83_2722-paragraph text-paragraphsm-20_2107"
                                >
                                    {{ text_5565_26 ?? "Supporting Text" }}
                                </p>
                            </slot>
                        </div>
                    </div>
                    <slot name="slot_5634_58315" v-if="visible_5634_741">
                        <Info
                            id="5634_58315"
                            class="Pixso-instance-5634_58315"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div class="stroke-5634_58309 stroke-gray20-36_1844"></div>
            </div>
            <div
                id="5634_55563"
                class="stroke-wrapper-5634_55563"
                v-if="
                    Type === 'Input Field' &&
                    State === 'Default' &&
                    FormControl === 'Checkbox'
                "
            >
                <div class="Pixso-symbol-5634_55563 fill-gray0-white-67_3285">
                    <slot name="slot_5634_55913">
                        <CheckboxOnly
                            id="5634_55913"
                            class="Pixso-instance-5634_55913"
                            Size="md"
                            State="Defaut"
                            IsIndeterminate="False"
                            IsChecked="False"
                        />
                    </slot>
                    <slot name="slot_5634_55564">
                        <InputTextBase
                            id="5634_55564"
                            class="Pixso-instance-5634_55564"
                            Type="Number"
                            Size="lg"
                        />
                    </slot>
                    <slot name="slot_5634_55565" v-if="visible_5634_741">
                        <Info
                            id="5634_55565"
                            class="Pixso-instance-5634_55565"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div class="stroke-5634_55563 stroke-gray20-36_1844"></div>
            </div>
            <div
                id="5634_56128"
                class="stroke-wrapper-5634_56128"
                v-if="
                    Type === 'Payment' &&
                    State === 'Hover' &&
                    FormControl === 'Checkbox'
                "
            >
                <div class="Pixso-symbol-5634_56128 fill-gray5-32_4120">
                    <slot name="slot_5634_56129">
                        <CheckboxOnly
                            id="5634_56129"
                            class="Pixso-instance-5634_56129"
                            Size="md"
                            State="Defaut"
                            IsIndeterminate="False"
                            IsChecked="False"
                        />
                    </slot>
                    <slot name="slot_5634_56130">
                        <PaymentLogo
                            id="5634_56130"
                            class="Pixso-instance-5634_56130"
                            Size="sm"
                            Company="Visa"
                        />
                    </slot>
                    <div id="5634_56131" class="Pixso-frame-5634_56131">
                        <div class="frame-content-5634_56131">
                            <slot name="slot_5634_56132" v-if="visible_5986_57">
                                <p
                                    id="5634_56132"
                                    class="Pixso-paragraph-5634_56132 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                                >
                                    {{ text_5565_13 ?? "Main Text" }}
                                </p>
                            </slot>
                            <slot name="slot_5634_56133" v-if="visible_5565_0">
                                <p
                                    id="5634_56133"
                                    class="Pixso-paragraph-5634_56133 fill-gray60-83_2722-paragraph text-paragraphsm-20_2107"
                                >
                                    {{ text_5565_26 ?? "Supporting Text" }}
                                </p>
                            </slot>
                        </div>
                    </div>
                    <slot name="slot_5634_56134" v-if="visible_5634_741">
                        <Info
                            id="5634_56134"
                            class="Pixso-instance-5634_56134"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div class="stroke-5634_56128 stroke-gray20-36_1844"></div>
            </div>
            <div
                id="5634_57318"
                class="stroke-wrapper-5634_57318"
                v-if="
                    Type === 'Flag' &&
                    State === 'Default' &&
                    FormControl === 'Radio'
                "
            >
                <div class="Pixso-symbol-5634_57318 fill-gray0-white-67_3285">
                    <slot name="slot_5634_57319">
                        <RadioOnly
                            id="5634_57319"
                            class="Pixso-instance-5634_57319"
                            Size="md"
                            State="Default"
                            IsChecked="False"
                        />
                    </slot>
                    <slot name="slot_5634_57320">
                        <Flags
                            id="5634_57320"
                            class="Pixso-instance-5634_57320"
                            Country="abkhazia"
                        />
                    </slot>
                    <div id="5634_57321" class="Pixso-frame-5634_57321">
                        <div class="frame-content-5634_57321">
                            <slot name="slot_5634_57322" v-if="visible_5986_57">
                                <p
                                    id="5634_57322"
                                    class="Pixso-paragraph-5634_57322 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                                >
                                    {{ text_5565_13 ?? "Main Text" }}
                                </p>
                            </slot>
                            <slot name="slot_5634_57323" v-if="visible_5565_0">
                                <p
                                    id="5634_57323"
                                    class="Pixso-paragraph-5634_57323 fill-gray60-83_2722-paragraph text-paragraphsm-20_2107"
                                >
                                    {{ text_5565_26 ?? "Supporting Text" }}
                                </p>
                            </slot>
                        </div>
                    </div>
                    <slot name="slot_5634_57324" v-if="visible_5634_741">
                        <Info
                            id="5634_57324"
                            class="Pixso-instance-5634_57324"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div class="stroke-5634_57318 stroke-gray20-36_1844"></div>
            </div>
            <div
                id="5634_58316"
                class="stroke-wrapper-5634_58316"
                v-if="
                    Type === 'Flag' &&
                    State === 'Default' &&
                    FormControl === 'Toggle'
                "
            >
                <div class="Pixso-symbol-5634_58316 fill-gray0-white-67_3285">
                    <slot name="slot_5634_58317">
                        <ToggleOnly
                            id="5634_58317"
                            class="Pixso-instance-5634_58317"
                            IsActive="False"
                            Size="md"
                            State="Default"
                            IsIcon="False"
                        />
                    </slot>
                    <slot name="slot_5634_58318">
                        <Flags
                            id="5634_58318"
                            class="Pixso-instance-5634_58318"
                            Country="abkhazia"
                        />
                    </slot>
                    <div id="5634_58319" class="Pixso-frame-5634_58319">
                        <div class="frame-content-5634_58319">
                            <slot name="slot_5634_58320" v-if="visible_5986_57">
                                <p
                                    id="5634_58320"
                                    class="Pixso-paragraph-5634_58320 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                                >
                                    {{ text_5565_13 ?? "Main Text" }}
                                </p>
                            </slot>
                            <slot name="slot_5634_58321" v-if="visible_5565_0">
                                <p
                                    id="5634_58321"
                                    class="Pixso-paragraph-5634_58321 fill-gray60-83_2722-paragraph text-paragraphsm-20_2107"
                                >
                                    {{ text_5565_26 ?? "Supporting Text" }}
                                </p>
                            </slot>
                        </div>
                    </div>
                    <slot name="slot_5634_58322" v-if="visible_5634_741">
                        <Info
                            id="5634_58322"
                            class="Pixso-instance-5634_58322"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div class="stroke-5634_58316 stroke-gray20-36_1844"></div>
            </div>
            <div
                id="5634_55566"
                class="stroke-wrapper-5634_55566"
                v-if="
                    Type === 'Avatar Group' &&
                    State === 'Default' &&
                    FormControl === 'Checkbox'
                "
            >
                <div class="Pixso-symbol-5634_55566 fill-gray0-white-67_3285">
                    <slot name="slot_5634_55914">
                        <CheckboxOnly
                            id="5634_55914"
                            class="Pixso-instance-5634_55914"
                            Size="md"
                            State="Defaut"
                            IsIndeterminate="False"
                            IsChecked="False"
                        />
                    </slot>
                    <slot name="slot_5634_55567">
                        <AvatarGroup
                            id="5634_55567"
                            class="Pixso-instance-5634_55567"
                            Size="sm"
                            IsAddUser="False"
                            IsMoreUser="True"
                        />
                    </slot>
                    <slot name="slot_5634_55568" v-if="visible_5634_741">
                        <Info
                            id="5634_55568"
                            class="Pixso-instance-5634_55568"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div class="stroke-5634_55566 stroke-gray20-36_1844"></div>
            </div>
            <div
                id="5634_57703"
                class="stroke-wrapper-5634_57703"
                v-if="
                    Type === 'Image' &&
                    State === 'Hover' &&
                    FormControl === 'Radio'
                "
            >
                <div class="Pixso-symbol-5634_57703 fill-gray5-32_4120">
                    <slot name="slot_5634_57704">
                        <RadioOnly
                            id="5634_57704"
                            class="Pixso-instance-5634_57704"
                            Size="md"
                            State="Default"
                            IsChecked="False"
                        />
                    </slot>
                    <div id="5634_57705" class="Pixso-frame-5634_57705"></div>
                    <div id="5634_57706" class="Pixso-frame-5634_57706">
                        <div class="frame-content-5634_57706">
                            <slot name="slot_5634_57707" v-if="visible_5986_57">
                                <p
                                    id="5634_57707"
                                    class="Pixso-paragraph-5634_57707 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                                >
                                    {{ text_5565_13 ?? "Main Text" }}
                                </p>
                            </slot>
                            <slot name="slot_5634_57708" v-if="visible_5565_0">
                                <p
                                    id="5634_57708"
                                    class="Pixso-paragraph-5634_57708 fill-gray60-83_2722-paragraph text-paragraphsm-20_2107"
                                >
                                    {{ text_5565_26 ?? "Supporting Text" }}
                                </p>
                            </slot>
                        </div>
                    </div>
                    <slot name="slot_5634_57709" v-if="visible_5634_741">
                        <Info
                            id="5634_57709"
                            class="Pixso-instance-5634_57709"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div class="stroke-5634_57703 stroke-gray20-36_1844"></div>
            </div>
            <div
                id="5634_58323"
                class="stroke-wrapper-5634_58323"
                v-if="
                    Type === 'Image' &&
                    State === 'Hover' &&
                    FormControl === 'Toggle'
                "
            >
                <div class="Pixso-symbol-5634_58323 fill-gray5-32_4120">
                    <slot name="slot_5634_58324">
                        <ToggleOnly
                            id="5634_58324"
                            class="Pixso-instance-5634_58324"
                            IsActive="False"
                            Size="md"
                            State="Default"
                            IsIcon="False"
                        />
                    </slot>
                    <div id="5634_58325" class="Pixso-frame-5634_58325"></div>
                    <div id="5634_58326" class="Pixso-frame-5634_58326">
                        <div class="frame-content-5634_58326">
                            <slot name="slot_5634_58327" v-if="visible_5986_57">
                                <p
                                    id="5634_58327"
                                    class="Pixso-paragraph-5634_58327 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                                >
                                    {{ text_5565_13 ?? "Main Text" }}
                                </p>
                            </slot>
                            <slot name="slot_5634_58328" v-if="visible_5565_0">
                                <p
                                    id="5634_58328"
                                    class="Pixso-paragraph-5634_58328 fill-gray60-83_2722-paragraph text-paragraphsm-20_2107"
                                >
                                    {{ text_5565_26 ?? "Supporting Text" }}
                                </p>
                            </slot>
                        </div>
                    </div>
                    <slot name="slot_5634_58329" v-if="visible_5634_741">
                        <Info
                            id="5634_58329"
                            class="Pixso-instance-5634_58329"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div class="stroke-5634_58323 stroke-gray20-36_1844"></div>
            </div>
            <div
                id="5634_55569"
                class="stroke-wrapper-5634_55569"
                v-if="
                    Type === 'Button Icon' &&
                    State === 'Default' &&
                    FormControl === 'Checkbox'
                "
            >
                <div class="Pixso-symbol-5634_55569 fill-gray0-white-67_3285">
                    <slot name="slot_5634_55915">
                        <CheckboxOnly
                            id="5634_55915"
                            class="Pixso-instance-5634_55915"
                            Size="md"
                            State="Defaut"
                            IsIndeterminate="False"
                            IsChecked="False"
                        />
                    </slot>
                    <slot name="slot_5634_55570">
                        <ButtonIcon
                            id="5634_55570"
                            class="Pixso-instance-5634_55570"
                            Hierarchy="No Fill"
                            Size="md"
                            Color="Gray"
                            State="Default"
                        >
                            <template #slot_5590_22158>
                                <TrashSimple
                                    id="5590_22158"
                                    class="Pixso-instance-5590_22158"
                                />
                            </template>
                        </ButtonIcon>
                    </slot>
                    <slot name="slot_5634_55571">
                        <ButtonIcon
                            id="5634_55571"
                            class="Pixso-instance-5634_55571"
                            Hierarchy="No Fill"
                            Size="md"
                            Color="Gray"
                            State="Default"
                        >
                            <template #slot_5590_22158>
                                <Download
                                    id="5590_22158"
                                    class="Pixso-instance-5590_22158"
                                />
                            </template>
                        </ButtonIcon>
                    </slot>
                    <slot name="slot_5634_55572">
                        <ButtonIcon
                            id="5634_55572"
                            class="Pixso-instance-5634_55572"
                            Hierarchy="No Fill"
                            Size="md"
                            Color="Gray"
                            State="Default"
                        >
                            <template #slot_5590_22158>
                                <DotsThreeVertical
                                    id="5590_22158"
                                    class="Pixso-instance-5590_22158"
                                />
                            </template>
                        </ButtonIcon>
                    </slot>
                </div>
                <div class="stroke-5634_55569 stroke-gray20-36_1844"></div>
            </div>
            <div
                id="5634_57325"
                class="stroke-wrapper-5634_57325"
                v-if="
                    Type === 'Progress' &&
                    State === 'Default' &&
                    FormControl === 'Radio'
                "
            >
                <div class="Pixso-symbol-5634_57325 fill-gray0-white-67_3285">
                    <slot name="slot_5634_57326">
                        <RadioOnly
                            id="5634_57326"
                            class="Pixso-instance-5634_57326"
                            Size="md"
                            State="Default"
                            IsChecked="False"
                        />
                    </slot>
                    <slot name="slot_5634_57327">
                        <ProgressBar
                            id="5634_57327"
                            class="Pixso-instance-5634_57327"
                            Progression="40"
                            Size="lg"
                            Label="Right"
                        >
                            <template #slot_5631_54072>
                                <ProgressBar
                                    id="5631_54072"
                                    class="Pixso-instance-5631_54072"
                                    Progression="40"
                                    Size="lg"
                                    Label="None"
                                />
                            </template>
                        </ProgressBar>
                    </slot>
                    <slot name="slot_5634_57328" v-if="visible_5634_741">
                        <Info
                            id="5634_57328"
                            class="Pixso-instance-5634_57328"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div class="stroke-5634_57325 stroke-gray20-36_1844"></div>
            </div>
            <div
                id="5634_58330"
                class="stroke-wrapper-5634_58330"
                v-if="
                    Type === 'Progress' &&
                    State === 'Default' &&
                    FormControl === 'Toggle'
                "
            >
                <div class="Pixso-symbol-5634_58330 fill-gray0-white-67_3285">
                    <slot name="slot_5634_58331">
                        <ToggleOnly
                            id="5634_58331"
                            class="Pixso-instance-5634_58331"
                            IsActive="False"
                            Size="md"
                            State="Default"
                            IsIcon="False"
                        />
                    </slot>
                    <slot name="slot_5634_58332">
                        <ProgressBar
                            id="5634_58332"
                            class="Pixso-instance-5634_58332"
                            Progression="40"
                            Size="lg"
                            Label="Right"
                        >
                            <template #slot_5631_54072>
                                <ProgressBar
                                    id="5631_54072"
                                    class="Pixso-instance-5631_54072"
                                    Progression="40"
                                    Size="lg"
                                    Label="None"
                                />
                            </template>
                        </ProgressBar>
                    </slot>
                    <slot name="slot_5634_58333" v-if="visible_5634_741">
                        <Info
                            id="5634_58333"
                            class="Pixso-instance-5634_58333"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div class="stroke-5634_58330 stroke-gray20-36_1844"></div>
            </div>
            <div
                id="5634_56135"
                class="stroke-wrapper-5634_56135"
                v-if="
                    Type === 'Image' &&
                    State === 'Hover' &&
                    FormControl === 'Checkbox'
                "
            >
                <div class="Pixso-symbol-5634_56135 fill-gray5-32_4120">
                    <slot name="slot_5634_56136">
                        <CheckboxOnly
                            id="5634_56136"
                            class="Pixso-instance-5634_56136"
                            Size="md"
                            State="Defaut"
                            IsIndeterminate="False"
                            IsChecked="False"
                        />
                    </slot>
                    <div id="5634_56137" class="Pixso-frame-5634_56137"></div>
                    <div id="5634_56138" class="Pixso-frame-5634_56138">
                        <div class="frame-content-5634_56138">
                            <slot name="slot_5634_56139" v-if="visible_5986_57">
                                <p
                                    id="5634_56139"
                                    class="Pixso-paragraph-5634_56139 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                                >
                                    {{ text_5565_13 ?? "Main Text" }}
                                </p>
                            </slot>
                            <slot name="slot_5634_56140" v-if="visible_5565_0">
                                <p
                                    id="5634_56140"
                                    class="Pixso-paragraph-5634_56140 fill-gray60-83_2722-paragraph text-paragraphsm-20_2107"
                                >
                                    {{ text_5565_26 ?? "Supporting Text" }}
                                </p>
                            </slot>
                        </div>
                    </div>
                    <slot name="slot_5634_56141" v-if="visible_5634_741">
                        <Info
                            id="5634_56141"
                            class="Pixso-instance-5634_56141"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div class="stroke-5634_56135 stroke-gray20-36_1844"></div>
            </div>
            <div
                id="5634_55573"
                class="stroke-wrapper-5634_55573"
                v-if="
                    Type === 'Button' &&
                    State === 'Default' &&
                    FormControl === 'Checkbox'
                "
            >
                <div class="Pixso-symbol-5634_55573 fill-gray0-white-67_3285">
                    <slot name="slot_5634_55916">
                        <CheckboxOnly
                            id="5634_55916"
                            class="Pixso-instance-5634_55916"
                            Size="md"
                            State="Defaut"
                            IsIndeterminate="False"
                            IsChecked="False"
                        />
                    </slot>
                    <slot name="slot_5634_55574">
                        <Button
                            id="5634_55574"
                            class="Pixso-instance-5634_55574"
                            :visible_5588_131="false"
                            :visible_5588_152="false"
                            text_5588_173="Delete"
                            Size="md"
                            Color="Destructive"
                            Hierarchy="Link"
                            State="Default"
                        >
                            <template #slot_5603_17591>
                                <p
                                    id="5603_17591"
                                    class="Pixso-paragraph-5603_17591 fill-destructive50-423_3219-paragraph text-text-smbold-423_3208"
                                >
                                    {{ "Delete" }}
                                </p>
                            </template>
                        </Button>
                    </slot>
                    <slot name="slot_5634_55575">
                        <Button
                            id="5634_55575"
                            class="Pixso-instance-5634_55575"
                            :visible_5588_131="false"
                            :visible_5588_152="false"
                            text_5588_173="Edit"
                            Size="md"
                            Color="Brand"
                            Hierarchy="Link"
                            State="Default"
                        >
                            <template #slot_5603_17351>
                                <p
                                    id="5603_17351"
                                    class="Pixso-paragraph-5603_17351 fill-brand60-1257_33467-paragraph text-text-smbold-423_3208"
                                >
                                    {{ "Edit" }}
                                </p>
                            </template>
                        </Button>
                    </slot>
                </div>
                <div class="stroke-5634_55573 stroke-gray20-36_1844"></div>
            </div>
            <div
                id="5634_57710"
                class="stroke-wrapper-5634_57710"
                v-if="
                    Type === 'Flag' &&
                    State === 'Hover' &&
                    FormControl === 'Radio'
                "
            >
                <div class="Pixso-symbol-5634_57710 fill-gray5-32_4120">
                    <slot name="slot_5634_57711">
                        <RadioOnly
                            id="5634_57711"
                            class="Pixso-instance-5634_57711"
                            Size="md"
                            State="Default"
                            IsChecked="False"
                        />
                    </slot>
                    <slot name="slot_5634_57712">
                        <Flags
                            id="5634_57712"
                            class="Pixso-instance-5634_57712"
                            Country="abkhazia"
                        />
                    </slot>
                    <div id="5634_57713" class="Pixso-frame-5634_57713">
                        <div class="frame-content-5634_57713">
                            <slot name="slot_5634_57714" v-if="visible_5986_57">
                                <p
                                    id="5634_57714"
                                    class="Pixso-paragraph-5634_57714 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                                >
                                    {{ text_5565_13 ?? "Main Text" }}
                                </p>
                            </slot>
                            <slot name="slot_5634_57715" v-if="visible_5565_0">
                                <p
                                    id="5634_57715"
                                    class="Pixso-paragraph-5634_57715 fill-gray60-83_2722-paragraph text-paragraphsm-20_2107"
                                >
                                    {{ text_5565_26 ?? "Supporting Text" }}
                                </p>
                            </slot>
                        </div>
                    </div>
                    <slot name="slot_5634_57716" v-if="visible_5634_741">
                        <Info
                            id="5634_57716"
                            class="Pixso-instance-5634_57716"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div class="stroke-5634_57710 stroke-gray20-36_1844"></div>
            </div>
            <div
                id="5634_58334"
                class="stroke-wrapper-5634_58334"
                v-if="
                    Type === 'Flag' &&
                    State === 'Hover' &&
                    FormControl === 'Toggle'
                "
            >
                <div class="Pixso-symbol-5634_58334 fill-gray5-32_4120">
                    <slot name="slot_5634_58335">
                        <ToggleOnly
                            id="5634_58335"
                            class="Pixso-instance-5634_58335"
                            IsActive="False"
                            Size="md"
                            State="Default"
                            IsIcon="False"
                        />
                    </slot>
                    <slot name="slot_5634_58336">
                        <Flags
                            id="5634_58336"
                            class="Pixso-instance-5634_58336"
                            Country="abkhazia"
                        />
                    </slot>
                    <div id="5634_58337" class="Pixso-frame-5634_58337">
                        <div class="frame-content-5634_58337">
                            <slot name="slot_5634_58338" v-if="visible_5986_57">
                                <p
                                    id="5634_58338"
                                    class="Pixso-paragraph-5634_58338 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                                >
                                    {{ text_5565_13 ?? "Main Text" }}
                                </p>
                            </slot>
                            <slot name="slot_5634_58339" v-if="visible_5565_0">
                                <p
                                    id="5634_58339"
                                    class="Pixso-paragraph-5634_58339 fill-gray60-83_2722-paragraph text-paragraphsm-20_2107"
                                >
                                    {{ text_5565_26 ?? "Supporting Text" }}
                                </p>
                            </slot>
                        </div>
                    </div>
                    <slot name="slot_5634_58340" v-if="visible_5634_741">
                        <Info
                            id="5634_58340"
                            class="Pixso-instance-5634_58340"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div class="stroke-5634_58334 stroke-gray20-36_1844"></div>
            </div>
            <div
                id="5634_57329"
                class="stroke-wrapper-5634_57329"
                v-if="
                    Type === 'Input Field' &&
                    State === 'Default' &&
                    FormControl === 'Radio'
                "
            >
                <div class="Pixso-symbol-5634_57329 fill-gray0-white-67_3285">
                    <slot name="slot_5634_57330">
                        <RadioOnly
                            id="5634_57330"
                            class="Pixso-instance-5634_57330"
                            Size="md"
                            State="Default"
                            IsChecked="False"
                        />
                    </slot>
                    <slot name="slot_5634_57331">
                        <InputTextBase
                            id="5634_57331"
                            class="Pixso-instance-5634_57331"
                            Type="Number"
                            Size="lg"
                        />
                    </slot>
                    <slot name="slot_5634_57332" v-if="visible_5634_741">
                        <Info
                            id="5634_57332"
                            class="Pixso-instance-5634_57332"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div class="stroke-5634_57329 stroke-gray20-36_1844"></div>
            </div>
            <div
                id="5634_58341"
                class="stroke-wrapper-5634_58341"
                v-if="
                    Type === 'Input Field' &&
                    State === 'Default' &&
                    FormControl === 'Toggle'
                "
            >
                <div class="Pixso-symbol-5634_58341 fill-gray0-white-67_3285">
                    <slot name="slot_5634_58342">
                        <ToggleOnly
                            id="5634_58342"
                            class="Pixso-instance-5634_58342"
                            IsActive="False"
                            Size="md"
                            State="Default"
                            IsIcon="False"
                        />
                    </slot>
                    <slot name="slot_5634_58343">
                        <InputTextBase
                            id="5634_58343"
                            class="Pixso-instance-5634_58343"
                            Type="Number"
                            Size="lg"
                        />
                    </slot>
                    <slot name="slot_5634_58344" v-if="visible_5634_741">
                        <Info
                            id="5634_58344"
                            class="Pixso-instance-5634_58344"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div class="stroke-5634_58341 stroke-gray20-36_1844"></div>
            </div>
            <div
                id="5634_55576"
                class="stroke-wrapper-5634_55576"
                v-if="
                    Type === 'Rating' &&
                    State === 'Default' &&
                    FormControl === 'Checkbox'
                "
            >
                <div class="Pixso-symbol-5634_55576 fill-gray0-white-67_3285">
                    <slot name="slot_5634_55917">
                        <CheckboxOnly
                            id="5634_55917"
                            class="Pixso-instance-5634_55917"
                            Size="md"
                            State="Defaut"
                            IsIndeterminate="False"
                            IsChecked="False"
                        />
                    </slot>
                    <slot name="slot_5634_55577">
                        <Rating
                            id="5634_55577"
                            class="Pixso-instance-5634_55577"
                            Star="5"
                            Size="md"
                            Color="Default"
                        />
                    </slot>
                    <slot name="slot_5634_55578" v-if="visible_5633_717">
                        <p
                            id="5634_55578"
                            class="Pixso-paragraph-5634_55578 fill-gray60-83_2722-paragraph text-text-mdsemibold-423_3206"
                        >
                            {{ text_5633_729 ?? "4.5" }}
                        </p>
                    </slot>
                </div>
                <div class="stroke-5634_55576 stroke-gray20-36_1844"></div>
            </div>
            <div
                id="5634_57333"
                class="stroke-wrapper-5634_57333"
                v-if="
                    Type === 'Avatar Group' &&
                    State === 'Default' &&
                    FormControl === 'Radio'
                "
            >
                <div class="Pixso-symbol-5634_57333 fill-gray0-white-67_3285">
                    <slot name="slot_5634_57334">
                        <RadioOnly
                            id="5634_57334"
                            class="Pixso-instance-5634_57334"
                            Size="md"
                            State="Default"
                            IsChecked="False"
                        />
                    </slot>
                    <slot name="slot_5634_57335">
                        <AvatarGroup
                            id="5634_57335"
                            class="Pixso-instance-5634_57335"
                            Size="sm"
                            IsAddUser="False"
                            IsMoreUser="True"
                        />
                    </slot>
                    <slot name="slot_5634_57336" v-if="visible_5634_741">
                        <Info
                            id="5634_57336"
                            class="Pixso-instance-5634_57336"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div class="stroke-5634_57333 stroke-gray20-36_1844"></div>
            </div>
            <div
                id="5634_58345"
                class="stroke-wrapper-5634_58345"
                v-if="
                    Type === 'Avatar Group' &&
                    State === 'Default' &&
                    FormControl === 'Toggle'
                "
            >
                <div class="Pixso-symbol-5634_58345 fill-gray0-white-67_3285">
                    <slot name="slot_5634_58346">
                        <ToggleOnly
                            id="5634_58346"
                            class="Pixso-instance-5634_58346"
                            IsActive="False"
                            Size="md"
                            State="Default"
                            IsIcon="False"
                        />
                    </slot>
                    <slot name="slot_5634_58347">
                        <AvatarGroup
                            id="5634_58347"
                            class="Pixso-instance-5634_58347"
                            Size="sm"
                            IsAddUser="False"
                            IsMoreUser="True"
                        />
                    </slot>
                    <slot name="slot_5634_58348" v-if="visible_5634_741">
                        <Info
                            id="5634_58348"
                            class="Pixso-instance-5634_58348"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div class="stroke-5634_58345 stroke-gray20-36_1844"></div>
            </div>
            <div
                id="5634_56142"
                class="stroke-wrapper-5634_56142"
                v-if="
                    Type === 'Flag' &&
                    State === 'Hover' &&
                    FormControl === 'Checkbox'
                "
            >
                <div class="Pixso-symbol-5634_56142 fill-gray5-32_4120">
                    <slot name="slot_5634_56143">
                        <CheckboxOnly
                            id="5634_56143"
                            class="Pixso-instance-5634_56143"
                            Size="md"
                            State="Defaut"
                            IsIndeterminate="False"
                            IsChecked="False"
                        />
                    </slot>
                    <slot name="slot_5634_56144">
                        <Flags
                            id="5634_56144"
                            class="Pixso-instance-5634_56144"
                            Country="abkhazia"
                        />
                    </slot>
                    <div id="5634_56145" class="Pixso-frame-5634_56145">
                        <div class="frame-content-5634_56145">
                            <slot name="slot_5634_56146" v-if="visible_5986_57">
                                <p
                                    id="5634_56146"
                                    class="Pixso-paragraph-5634_56146 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                                >
                                    {{ text_5565_13 ?? "Main Text" }}
                                </p>
                            </slot>
                            <slot name="slot_5634_56147" v-if="visible_5565_0">
                                <p
                                    id="5634_56147"
                                    class="Pixso-paragraph-5634_56147 fill-gray60-83_2722-paragraph text-paragraphsm-20_2107"
                                >
                                    {{ text_5565_26 ?? "Supporting Text" }}
                                </p>
                            </slot>
                        </div>
                    </div>
                    <slot name="slot_5634_56148" v-if="visible_5634_741">
                        <Info
                            id="5634_56148"
                            class="Pixso-instance-5634_56148"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div class="stroke-5634_56142 stroke-gray20-36_1844"></div>
            </div>
            <div
                id="5634_57337"
                class="stroke-wrapper-5634_57337"
                v-if="
                    Type === 'Button Icon' &&
                    State === 'Default' &&
                    FormControl === 'Radio'
                "
            >
                <div class="Pixso-symbol-5634_57337 fill-gray0-white-67_3285">
                    <slot name="slot_5634_57338">
                        <RadioOnly
                            id="5634_57338"
                            class="Pixso-instance-5634_57338"
                            Size="md"
                            State="Default"
                            IsChecked="False"
                        />
                    </slot>
                    <slot name="slot_5634_57339">
                        <ButtonIcon
                            id="5634_57339"
                            class="Pixso-instance-5634_57339"
                            Hierarchy="No Fill"
                            Size="md"
                            Color="Gray"
                            State="Default"
                        >
                            <template #slot_5590_22158>
                                <TrashSimple
                                    id="5590_22158"
                                    class="Pixso-instance-5590_22158"
                                />
                            </template>
                        </ButtonIcon>
                    </slot>
                    <slot name="slot_5634_57340">
                        <ButtonIcon
                            id="5634_57340"
                            class="Pixso-instance-5634_57340"
                            Hierarchy="No Fill"
                            Size="md"
                            Color="Gray"
                            State="Default"
                        >
                            <template #slot_5590_22158>
                                <Download
                                    id="5590_22158"
                                    class="Pixso-instance-5590_22158"
                                />
                            </template>
                        </ButtonIcon>
                    </slot>
                    <slot name="slot_5634_57341">
                        <ButtonIcon
                            id="5634_57341"
                            class="Pixso-instance-5634_57341"
                            Hierarchy="No Fill"
                            Size="md"
                            Color="Gray"
                            State="Default"
                        >
                            <template #slot_5590_22158>
                                <DotsThreeVertical
                                    id="5590_22158"
                                    class="Pixso-instance-5590_22158"
                                />
                            </template>
                        </ButtonIcon>
                    </slot>
                </div>
                <div class="stroke-5634_57337 stroke-gray20-36_1844"></div>
            </div>
            <div
                id="5634_58349"
                class="stroke-wrapper-5634_58349"
                v-if="
                    Type === 'Button Icon' &&
                    State === 'Default' &&
                    FormControl === 'Toggle'
                "
            >
                <div class="Pixso-symbol-5634_58349 fill-gray0-white-67_3285">
                    <slot name="slot_5634_58350">
                        <ToggleOnly
                            id="5634_58350"
                            class="Pixso-instance-5634_58350"
                            IsActive="False"
                            Size="md"
                            State="Default"
                            IsIcon="False"
                        />
                    </slot>
                    <slot name="slot_5634_58351">
                        <ButtonIcon
                            id="5634_58351"
                            class="Pixso-instance-5634_58351"
                            Hierarchy="No Fill"
                            Size="md"
                            Color="Gray"
                            State="Default"
                        >
                            <template #slot_5590_22158>
                                <TrashSimple
                                    id="5590_22158"
                                    class="Pixso-instance-5590_22158"
                                />
                            </template>
                        </ButtonIcon>
                    </slot>
                    <slot name="slot_5634_58352">
                        <ButtonIcon
                            id="5634_58352"
                            class="Pixso-instance-5634_58352"
                            Hierarchy="No Fill"
                            Size="md"
                            Color="Gray"
                            State="Default"
                        >
                            <template #slot_5590_22158>
                                <Download
                                    id="5590_22158"
                                    class="Pixso-instance-5590_22158"
                                />
                            </template>
                        </ButtonIcon>
                    </slot>
                    <slot name="slot_5634_58353">
                        <ButtonIcon
                            id="5634_58353"
                            class="Pixso-instance-5634_58353"
                            Hierarchy="No Fill"
                            Size="md"
                            Color="Gray"
                            State="Default"
                        >
                            <template #slot_5590_22158>
                                <DotsThreeVertical
                                    id="5590_22158"
                                    class="Pixso-instance-5590_22158"
                                />
                            </template>
                        </ButtonIcon>
                    </slot>
                </div>
                <div class="stroke-5634_58349 stroke-gray20-36_1844"></div>
            </div>
            <div
                id="5634_55579"
                class="stroke-wrapper-5634_55579"
                v-if="
                    Type === 'Trend' &&
                    State === 'Default' &&
                    FormControl === 'Checkbox'
                "
            >
                <div class="Pixso-symbol-5634_55579 fill-gray0-white-67_3285">
                    <slot name="slot_5634_55918">
                        <CheckboxOnly
                            id="5634_55918"
                            class="Pixso-instance-5634_55918"
                            Size="md"
                            State="Defaut"
                            IsIndeterminate="False"
                            IsChecked="False"
                        />
                    </slot>
                    <div id="5634_55580" class="Pixso-frame-5634_55580">
                        <slot name="slot_5634_55581" v-if="visible_5986_57">
                            <p
                                id="5634_55581"
                                class="Pixso-paragraph-5634_55581 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                            >
                                {{ text_5565_13 ?? "Main Text" }}
                            </p>
                        </slot>
                        <slot name="slot_5634_55582">
                            <BadgeText
                                id="5634_55582"
                                class="Pixso-instance-5634_55582"
                                :visible_5586_119="false"
                                :visible_5586_121="false"
                                text_5588_129="48%"
                                Size="sm"
                                Color="Success"
                                Hierarchy="Secondary"
                                State="Default"
                            >
                                <template #slot_5588_12217>
                                    <TrendUp
                                        id="5588_12217"
                                        class="Pixso-instance-5588_12217"
                                    />
                                </template>
                                <template #slot_5588_12220>
                                    <p
                                        id="5588_12220"
                                        class="Pixso-paragraph-5588_12220 fill-success50-1636_81205-paragraph text-text-xssemibold-439_9521"
                                    >
                                        {{ "48%" }}
                                    </p>
                                </template>
                            </BadgeText>
                        </slot>
                    </div>
                    <slot name="slot_5634_55583" v-if="visible_5634_741">
                        <Info
                            id="5634_55583"
                            class="Pixso-instance-5634_55583"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div class="stroke-5634_55579 stroke-gray20-36_1844"></div>
            </div>
            <div
                id="5634_57342"
                class="stroke-wrapper-5634_57342"
                v-if="
                    Type === 'Button' &&
                    State === 'Default' &&
                    FormControl === 'Radio'
                "
            >
                <div class="Pixso-symbol-5634_57342 fill-gray0-white-67_3285">
                    <slot name="slot_5634_57343">
                        <RadioOnly
                            id="5634_57343"
                            class="Pixso-instance-5634_57343"
                            Size="md"
                            State="Default"
                            IsChecked="False"
                        />
                    </slot>
                    <slot name="slot_5634_57344">
                        <Button
                            id="5634_57344"
                            class="Pixso-instance-5634_57344"
                            :visible_5588_131="false"
                            :visible_5588_152="false"
                            text_5588_173="Delete"
                            Size="md"
                            Color="Destructive"
                            Hierarchy="Link"
                            State="Default"
                        >
                            <template #slot_5603_17591>
                                <p
                                    id="5603_17591"
                                    class="Pixso-paragraph-5603_17591 fill-destructive50-423_3219-paragraph text-text-smbold-423_3208"
                                >
                                    {{ "Delete" }}
                                </p>
                            </template>
                        </Button>
                    </slot>
                    <slot name="slot_5634_57345">
                        <Button
                            id="5634_57345"
                            class="Pixso-instance-5634_57345"
                            :visible_5588_131="false"
                            :visible_5588_152="false"
                            text_5588_173="Edit"
                            Size="md"
                            Color="Brand"
                            Hierarchy="Link"
                            State="Default"
                        >
                            <template #slot_5603_17351>
                                <p
                                    id="5603_17351"
                                    class="Pixso-paragraph-5603_17351 fill-brand60-1257_33467-paragraph text-text-smbold-423_3208"
                                >
                                    {{ "Edit" }}
                                </p>
                            </template>
                        </Button>
                    </slot>
                </div>
                <div class="stroke-5634_57342 stroke-gray20-36_1844"></div>
            </div>
            <div
                id="5634_58354"
                class="stroke-wrapper-5634_58354"
                v-if="
                    Type === 'Button' &&
                    State === 'Default' &&
                    FormControl === 'Toggle'
                "
            >
                <div class="Pixso-symbol-5634_58354 fill-gray0-white-67_3285">
                    <slot name="slot_5634_58355">
                        <ToggleOnly
                            id="5634_58355"
                            class="Pixso-instance-5634_58355"
                            IsActive="False"
                            Size="md"
                            State="Default"
                            IsIcon="False"
                        />
                    </slot>
                    <slot name="slot_5634_58356">
                        <Button
                            id="5634_58356"
                            class="Pixso-instance-5634_58356"
                            :visible_5588_131="false"
                            :visible_5588_152="false"
                            text_5588_173="Delete"
                            Size="md"
                            Color="Destructive"
                            Hierarchy="Link"
                            State="Default"
                        >
                            <template #slot_5603_17591>
                                <p
                                    id="5603_17591"
                                    class="Pixso-paragraph-5603_17591 fill-destructive50-423_3219-paragraph text-text-smbold-423_3208"
                                >
                                    {{ "Delete" }}
                                </p>
                            </template>
                        </Button>
                    </slot>
                    <slot name="slot_5634_58357">
                        <Button
                            id="5634_58357"
                            class="Pixso-instance-5634_58357"
                            :visible_5588_131="false"
                            :visible_5588_152="false"
                            text_5588_173="Edit"
                            Size="md"
                            Color="Brand"
                            Hierarchy="Link"
                            State="Default"
                        >
                            <template #slot_5603_17351>
                                <p
                                    id="5603_17351"
                                    class="Pixso-paragraph-5603_17351 fill-brand60-1257_33467-paragraph text-text-smbold-423_3208"
                                >
                                    {{ "Edit" }}
                                </p>
                            </template>
                        </Button>
                    </slot>
                </div>
                <div class="stroke-5634_58354 stroke-gray20-36_1844"></div>
            </div>
            <div
                id="5634_57717"
                class="stroke-wrapper-5634_57717"
                v-if="
                    Type === 'Progress' &&
                    State === 'Hover' &&
                    FormControl === 'Radio'
                "
            >
                <div class="Pixso-symbol-5634_57717 fill-gray5-32_4120">
                    <slot name="slot_5634_57718">
                        <RadioOnly
                            id="5634_57718"
                            class="Pixso-instance-5634_57718"
                            Size="md"
                            State="Default"
                            IsChecked="False"
                        />
                    </slot>
                    <slot name="slot_5634_57719">
                        <ProgressBar
                            id="5634_57719"
                            class="Pixso-instance-5634_57719"
                            Progression="40"
                            Size="lg"
                            Label="Right"
                        >
                            <template #slot_5631_54072>
                                <ProgressBar
                                    id="5631_54072"
                                    class="Pixso-instance-5631_54072"
                                    Progression="40"
                                    Size="lg"
                                    Label="None"
                                />
                            </template>
                        </ProgressBar>
                    </slot>
                    <slot name="slot_5634_57720" v-if="visible_5634_741">
                        <Info
                            id="5634_57720"
                            class="Pixso-instance-5634_57720"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div class="stroke-5634_57717 stroke-gray20-36_1844"></div>
            </div>
            <div
                id="5634_58358"
                class="stroke-wrapper-5634_58358"
                v-if="
                    Type === 'Progress' &&
                    State === 'Hover' &&
                    FormControl === 'Toggle'
                "
            >
                <div class="Pixso-symbol-5634_58358 fill-gray5-32_4120">
                    <slot name="slot_5634_58359">
                        <ToggleOnly
                            id="5634_58359"
                            class="Pixso-instance-5634_58359"
                            IsActive="False"
                            Size="md"
                            State="Default"
                            IsIcon="False"
                        />
                    </slot>
                    <slot name="slot_5634_58360">
                        <ProgressBar
                            id="5634_58360"
                            class="Pixso-instance-5634_58360"
                            Progression="40"
                            Size="lg"
                            Label="Right"
                        >
                            <template #slot_5631_54072>
                                <ProgressBar
                                    id="5631_54072"
                                    class="Pixso-instance-5631_54072"
                                    Progression="40"
                                    Size="lg"
                                    Label="None"
                                />
                            </template>
                        </ProgressBar>
                    </slot>
                    <slot name="slot_5634_58361" v-if="visible_5634_741">
                        <Info
                            id="5634_58361"
                            class="Pixso-instance-5634_58361"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div class="stroke-5634_58358 stroke-gray20-36_1844"></div>
            </div>
            <div
                id="5634_57346"
                class="stroke-wrapper-5634_57346"
                v-if="
                    Type === 'Rating' &&
                    State === 'Default' &&
                    FormControl === 'Radio'
                "
            >
                <div class="Pixso-symbol-5634_57346 fill-gray0-white-67_3285">
                    <slot name="slot_5634_57347">
                        <RadioOnly
                            id="5634_57347"
                            class="Pixso-instance-5634_57347"
                            Size="md"
                            State="Default"
                            IsChecked="False"
                        />
                    </slot>
                    <slot name="slot_5634_57348">
                        <Rating
                            id="5634_57348"
                            class="Pixso-instance-5634_57348"
                            Star="5"
                            Size="md"
                            Color="Default"
                        />
                    </slot>
                    <slot name="slot_5634_57349" v-if="visible_5633_717">
                        <p
                            id="5634_57349"
                            class="Pixso-paragraph-5634_57349 fill-gray60-83_2722-paragraph text-text-mdsemibold-423_3206"
                        >
                            {{ text_5633_729 ?? "4.5" }}
                        </p>
                    </slot>
                </div>
                <div class="stroke-5634_57346 stroke-gray20-36_1844"></div>
            </div>
            <div
                id="5634_58362"
                class="stroke-wrapper-5634_58362"
                v-if="
                    Type === 'Rating' &&
                    State === 'Default' &&
                    FormControl === 'Toggle'
                "
            >
                <div class="Pixso-symbol-5634_58362 fill-gray0-white-67_3285">
                    <slot name="slot_5634_58363">
                        <ToggleOnly
                            id="5634_58363"
                            class="Pixso-instance-5634_58363"
                            IsActive="False"
                            Size="md"
                            State="Default"
                            IsIcon="False"
                        />
                    </slot>
                    <slot name="slot_5634_58364">
                        <Rating
                            id="5634_58364"
                            class="Pixso-instance-5634_58364"
                            Star="5"
                            Size="md"
                            Color="Default"
                        />
                    </slot>
                    <slot name="slot_5634_58365" v-if="visible_5633_717">
                        <p
                            id="5634_58365"
                            class="Pixso-paragraph-5634_58365 fill-gray60-83_2722-paragraph text-text-mdsemibold-423_3206"
                        >
                            {{ text_5633_729 ?? "4.5" }}
                        </p>
                    </slot>
                </div>
                <div class="stroke-5634_58362 stroke-gray20-36_1844"></div>
            </div>
            <div
                id="5634_55584"
                class="stroke-wrapper-5634_55584"
                v-if="
                    Type === 'Badge Single' &&
                    State === 'Default' &&
                    FormControl === 'Checkbox'
                "
            >
                <div class="Pixso-symbol-5634_55584 fill-gray0-white-67_3285">
                    <slot name="slot_5634_55919">
                        <CheckboxOnly
                            id="5634_55919"
                            class="Pixso-instance-5634_55919"
                            Size="md"
                            State="Defaut"
                            IsIndeterminate="False"
                            IsChecked="False"
                        />
                    </slot>
                    <slot name="slot_5634_55585">
                        <BadgeText
                            id="5634_55585"
                            class="Pixso-instance-5634_55585"
                            :visible_5586_119="false"
                            :visible_5586_121="false"
                            :visible_5586_123="false"
                            Size="sm"
                            Color="Brand"
                            Hierarchy="Secondary"
                            State="Default"
                        />
                    </slot>
                    <slot name="slot_5634_55586" v-if="visible_5634_741">
                        <Info
                            id="5634_55586"
                            class="Pixso-instance-5634_55586"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div class="stroke-5634_55584 stroke-gray20-36_1844"></div>
            </div>
            <div
                id="5634_57350"
                class="stroke-wrapper-5634_57350"
                v-if="
                    Type === 'Trend' &&
                    State === 'Default' &&
                    FormControl === 'Radio'
                "
            >
                <div class="Pixso-symbol-5634_57350 fill-gray0-white-67_3285">
                    <slot name="slot_5634_57351">
                        <RadioOnly
                            id="5634_57351"
                            class="Pixso-instance-5634_57351"
                            Size="md"
                            State="Default"
                            IsChecked="False"
                        />
                    </slot>
                    <div id="5634_57352" class="Pixso-frame-5634_57352">
                        <slot name="slot_5634_57353" v-if="visible_5986_57">
                            <p
                                id="5634_57353"
                                class="Pixso-paragraph-5634_57353 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                            >
                                {{ text_5565_13 ?? "Main Text" }}
                            </p>
                        </slot>
                        <slot name="slot_5634_57354">
                            <BadgeText
                                id="5634_57354"
                                class="Pixso-instance-5634_57354"
                                :visible_5586_119="false"
                                :visible_5586_121="false"
                                text_5588_129="48%"
                                Size="sm"
                                Color="Success"
                                Hierarchy="Secondary"
                                State="Default"
                            >
                                <template #slot_5588_12217>
                                    <TrendUp
                                        id="5588_12217"
                                        class="Pixso-instance-5588_12217"
                                    />
                                </template>
                                <template #slot_5588_12220>
                                    <p
                                        id="5588_12220"
                                        class="Pixso-paragraph-5588_12220 fill-success50-1636_81205-paragraph text-text-xssemibold-439_9521"
                                    >
                                        {{ "48%" }}
                                    </p>
                                </template>
                            </BadgeText>
                        </slot>
                    </div>
                    <slot name="slot_5634_57355" v-if="visible_5634_741">
                        <Info
                            id="5634_57355"
                            class="Pixso-instance-5634_57355"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div class="stroke-5634_57350 stroke-gray20-36_1844"></div>
            </div>
            <div
                id="5634_58366"
                class="stroke-wrapper-5634_58366"
                v-if="
                    Type === 'Trend' &&
                    State === 'Default' &&
                    FormControl === 'Toggle'
                "
            >
                <div class="Pixso-symbol-5634_58366 fill-gray0-white-67_3285">
                    <slot name="slot_5634_58367">
                        <ToggleOnly
                            id="5634_58367"
                            class="Pixso-instance-5634_58367"
                            IsActive="False"
                            Size="md"
                            State="Default"
                            IsIcon="False"
                        />
                    </slot>
                    <div id="5634_58368" class="Pixso-frame-5634_58368">
                        <slot name="slot_5634_58369" v-if="visible_5986_57">
                            <p
                                id="5634_58369"
                                class="Pixso-paragraph-5634_58369 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                            >
                                {{ text_5565_13 ?? "Main Text" }}
                            </p>
                        </slot>
                        <slot name="slot_5634_58370">
                            <BadgeText
                                id="5634_58370"
                                class="Pixso-instance-5634_58370"
                                :visible_5586_119="false"
                                :visible_5586_121="false"
                                text_5588_129="48%"
                                Size="sm"
                                Color="Success"
                                Hierarchy="Secondary"
                                State="Default"
                            >
                                <template #slot_5588_12217>
                                    <TrendUp
                                        id="5588_12217"
                                        class="Pixso-instance-5588_12217"
                                    />
                                </template>
                                <template #slot_5588_12220>
                                    <p
                                        id="5588_12220"
                                        class="Pixso-paragraph-5588_12220 fill-success50-1636_81205-paragraph text-text-xssemibold-439_9521"
                                    >
                                        {{ "48%" }}
                                    </p>
                                </template>
                            </BadgeText>
                        </slot>
                    </div>
                    <slot name="slot_5634_58371" v-if="visible_5634_741">
                        <Info
                            id="5634_58371"
                            class="Pixso-instance-5634_58371"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div class="stroke-5634_58366 stroke-gray20-36_1844"></div>
            </div>
            <div
                id="5634_56149"
                class="stroke-wrapper-5634_56149"
                v-if="
                    Type === 'Progress' &&
                    State === 'Hover' &&
                    FormControl === 'Checkbox'
                "
            >
                <div class="Pixso-symbol-5634_56149 fill-gray5-32_4120">
                    <slot name="slot_5634_56150">
                        <CheckboxOnly
                            id="5634_56150"
                            class="Pixso-instance-5634_56150"
                            Size="md"
                            State="Defaut"
                            IsIndeterminate="False"
                            IsChecked="False"
                        />
                    </slot>
                    <slot name="slot_5634_56151">
                        <ProgressBar
                            id="5634_56151"
                            class="Pixso-instance-5634_56151"
                            Progression="40"
                            Size="lg"
                            Label="Right"
                        >
                            <template #slot_5631_54072>
                                <ProgressBar
                                    id="5631_54072"
                                    class="Pixso-instance-5631_54072"
                                    Progression="40"
                                    Size="lg"
                                    Label="None"
                                />
                            </template>
                        </ProgressBar>
                    </slot>
                    <slot name="slot_5634_56152" v-if="visible_5634_741">
                        <Info
                            id="5634_56152"
                            class="Pixso-instance-5634_56152"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div class="stroke-5634_56149 stroke-gray20-36_1844"></div>
            </div>
            <div
                id="5634_57356"
                class="stroke-wrapper-5634_57356"
                v-if="
                    Type === 'Badge Single' &&
                    State === 'Default' &&
                    FormControl === 'Radio'
                "
            >
                <div class="Pixso-symbol-5634_57356 fill-gray0-white-67_3285">
                    <slot name="slot_5634_57357">
                        <RadioOnly
                            id="5634_57357"
                            class="Pixso-instance-5634_57357"
                            Size="md"
                            State="Default"
                            IsChecked="False"
                        />
                    </slot>
                    <slot name="slot_5634_57358">
                        <BadgeText
                            id="5634_57358"
                            class="Pixso-instance-5634_57358"
                            :visible_5586_119="false"
                            :visible_5586_121="false"
                            :visible_5586_123="false"
                            Size="sm"
                            Color="Brand"
                            Hierarchy="Secondary"
                            State="Default"
                        />
                    </slot>
                    <slot name="slot_5634_57359" v-if="visible_5634_741">
                        <Info
                            id="5634_57359"
                            class="Pixso-instance-5634_57359"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div class="stroke-5634_57356 stroke-gray20-36_1844"></div>
            </div>
            <div
                id="5634_58372"
                class="stroke-wrapper-5634_58372"
                v-if="
                    Type === 'Badge Single' &&
                    State === 'Default' &&
                    FormControl === 'Toggle'
                "
            >
                <div class="Pixso-symbol-5634_58372 fill-gray0-white-67_3285">
                    <slot name="slot_5634_58373">
                        <ToggleOnly
                            id="5634_58373"
                            class="Pixso-instance-5634_58373"
                            IsActive="False"
                            Size="md"
                            State="Default"
                            IsIcon="False"
                        />
                    </slot>
                    <slot name="slot_5634_58374">
                        <BadgeText
                            id="5634_58374"
                            class="Pixso-instance-5634_58374"
                            :visible_5586_119="false"
                            :visible_5586_121="false"
                            :visible_5586_123="false"
                            Size="sm"
                            Color="Brand"
                            Hierarchy="Secondary"
                            State="Default"
                        />
                    </slot>
                    <slot name="slot_5634_58375" v-if="visible_5634_741">
                        <Info
                            id="5634_58375"
                            class="Pixso-instance-5634_58375"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div class="stroke-5634_58372 stroke-gray20-36_1844"></div>
            </div>
            <div
                id="5634_55587"
                class="stroke-wrapper-5634_55587"
                v-if="
                    Type === 'Badge Group' &&
                    State === 'Default' &&
                    FormControl === 'Checkbox'
                "
            >
                <div class="Pixso-symbol-5634_55587 fill-gray0-white-67_3285">
                    <slot name="slot_5634_55920">
                        <CheckboxOnly
                            id="5634_55920"
                            class="Pixso-instance-5634_55920"
                            Size="md"
                            State="Defaut"
                            IsIndeterminate="False"
                            IsChecked="False"
                        />
                    </slot>
                    <div id="5634_55588" class="Pixso-frame-5634_55588">
                        <slot name="slot_5634_55589">
                            <BadgeText
                                id="5634_55589"
                                class="Pixso-instance-5634_55589"
                                :visible_5586_119="false"
                                :visible_5586_121="false"
                                :visible_5586_123="false"
                                Size="sm"
                                Color="Brand"
                                Hierarchy="Secondary"
                                State="Default"
                            />
                        </slot>
                        <slot name="slot_5634_55590">
                            <BadgeText
                                id="5634_55590"
                                class="Pixso-instance-5634_55590"
                                :visible_5586_119="false"
                                :visible_5586_121="false"
                                :visible_5586_123="false"
                                Size="sm"
                                Color="Warning"
                                Hierarchy="Secondary"
                                State="Default"
                            />
                        </slot>
                        <slot name="slot_5634_55591">
                            <BadgeText
                                id="5634_55591"
                                class="Pixso-instance-5634_55591"
                                :visible_5586_119="false"
                                :visible_5586_121="false"
                                :visible_5586_123="false"
                                Size="sm"
                                Color="Destructive"
                                Hierarchy="Secondary"
                                State="Default"
                            />
                        </slot>
                    </div>
                    <slot name="slot_5634_55592" v-if="visible_5634_741">
                        <Info
                            id="5634_55592"
                            class="Pixso-instance-5634_55592"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div class="stroke-5634_55587 stroke-gray20-36_1844"></div>
            </div>
            <div
                id="5634_57360"
                class="stroke-wrapper-5634_57360"
                v-if="
                    Type === 'Badge Group' &&
                    State === 'Default' &&
                    FormControl === 'Radio'
                "
            >
                <div class="Pixso-symbol-5634_57360 fill-gray0-white-67_3285">
                    <slot name="slot_5634_57361">
                        <RadioOnly
                            id="5634_57361"
                            class="Pixso-instance-5634_57361"
                            Size="md"
                            State="Default"
                            IsChecked="False"
                        />
                    </slot>
                    <div id="5634_57362" class="Pixso-frame-5634_57362">
                        <slot name="slot_5634_57363">
                            <BadgeText
                                id="5634_57363"
                                class="Pixso-instance-5634_57363"
                                :visible_5586_119="false"
                                :visible_5586_121="false"
                                :visible_5586_123="false"
                                Size="sm"
                                Color="Brand"
                                Hierarchy="Secondary"
                                State="Default"
                            />
                        </slot>
                        <slot name="slot_5634_57364">
                            <BadgeText
                                id="5634_57364"
                                class="Pixso-instance-5634_57364"
                                :visible_5586_119="false"
                                :visible_5586_121="false"
                                :visible_5586_123="false"
                                Size="sm"
                                Color="Warning"
                                Hierarchy="Secondary"
                                State="Default"
                            />
                        </slot>
                        <slot name="slot_5634_57365">
                            <BadgeText
                                id="5634_57365"
                                class="Pixso-instance-5634_57365"
                                :visible_5586_119="false"
                                :visible_5586_121="false"
                                :visible_5586_123="false"
                                Size="sm"
                                Color="Destructive"
                                Hierarchy="Secondary"
                                State="Default"
                            />
                        </slot>
                    </div>
                    <slot name="slot_5634_57366" v-if="visible_5634_741">
                        <Info
                            id="5634_57366"
                            class="Pixso-instance-5634_57366"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div class="stroke-5634_57360 stroke-gray20-36_1844"></div>
            </div>
            <div
                id="5634_58376"
                class="stroke-wrapper-5634_58376"
                v-if="
                    Type === 'Badge Group' &&
                    State === 'Default' &&
                    FormControl === 'Toggle'
                "
            >
                <div class="Pixso-symbol-5634_58376 fill-gray0-white-67_3285">
                    <slot name="slot_5634_58377">
                        <ToggleOnly
                            id="5634_58377"
                            class="Pixso-instance-5634_58377"
                            IsActive="False"
                            Size="md"
                            State="Default"
                            IsIcon="False"
                        />
                    </slot>
                    <div id="5634_58378" class="Pixso-frame-5634_58378">
                        <slot name="slot_5634_58379">
                            <BadgeText
                                id="5634_58379"
                                class="Pixso-instance-5634_58379"
                                :visible_5586_119="false"
                                :visible_5586_121="false"
                                :visible_5586_123="false"
                                Size="sm"
                                Color="Brand"
                                Hierarchy="Secondary"
                                State="Default"
                            />
                        </slot>
                        <slot name="slot_5634_58380">
                            <BadgeText
                                id="5634_58380"
                                class="Pixso-instance-5634_58380"
                                :visible_5586_119="false"
                                :visible_5586_121="false"
                                :visible_5586_123="false"
                                Size="sm"
                                Color="Warning"
                                Hierarchy="Secondary"
                                State="Default"
                            />
                        </slot>
                        <slot name="slot_5634_58381">
                            <BadgeText
                                id="5634_58381"
                                class="Pixso-instance-5634_58381"
                                :visible_5586_119="false"
                                :visible_5586_121="false"
                                :visible_5586_123="false"
                                Size="sm"
                                Color="Destructive"
                                Hierarchy="Secondary"
                                State="Default"
                            />
                        </slot>
                    </div>
                    <slot name="slot_5634_58382" v-if="visible_5634_741">
                        <Info
                            id="5634_58382"
                            class="Pixso-instance-5634_58382"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div class="stroke-5634_58376 stroke-gray20-36_1844"></div>
            </div>
            <div
                id="5634_57721"
                class="stroke-wrapper-5634_57721"
                v-if="
                    Type === 'Input Field' &&
                    State === 'Hover' &&
                    FormControl === 'Radio'
                "
            >
                <div class="Pixso-symbol-5634_57721 fill-gray5-32_4120">
                    <slot name="slot_5634_57722">
                        <RadioOnly
                            id="5634_57722"
                            class="Pixso-instance-5634_57722"
                            Size="md"
                            State="Default"
                            IsChecked="False"
                        />
                    </slot>
                    <slot name="slot_5634_57723">
                        <InputTextBase
                            id="5634_57723"
                            class="Pixso-instance-5634_57723"
                            Type="Number"
                            Size="lg"
                        />
                    </slot>
                    <slot name="slot_5634_57724" v-if="visible_5634_741">
                        <Info
                            id="5634_57724"
                            class="Pixso-instance-5634_57724"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div class="stroke-5634_57721 stroke-gray20-36_1844"></div>
            </div>
            <div
                id="5634_58383"
                class="stroke-wrapper-5634_58383"
                v-if="
                    Type === 'Input Field' &&
                    State === 'Hover' &&
                    FormControl === 'Toggle'
                "
            >
                <div class="Pixso-symbol-5634_58383 fill-gray5-32_4120">
                    <slot name="slot_5634_58384">
                        <ToggleOnly
                            id="5634_58384"
                            class="Pixso-instance-5634_58384"
                            IsActive="False"
                            Size="md"
                            State="Default"
                            IsIcon="False"
                        />
                    </slot>
                    <slot name="slot_5634_58385">
                        <InputTextBase
                            id="5634_58385"
                            class="Pixso-instance-5634_58385"
                            Type="Number"
                            Size="lg"
                        />
                    </slot>
                    <slot name="slot_5634_58386" v-if="visible_5634_741">
                        <Info
                            id="5634_58386"
                            class="Pixso-instance-5634_58386"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div class="stroke-5634_58383 stroke-gray20-36_1844"></div>
            </div>
            <div
                id="5634_56153"
                class="stroke-wrapper-5634_56153"
                v-if="
                    Type === 'Input Field' &&
                    State === 'Hover' &&
                    FormControl === 'Checkbox'
                "
            >
                <div class="Pixso-symbol-5634_56153 fill-gray5-32_4120">
                    <slot name="slot_5634_56154">
                        <CheckboxOnly
                            id="5634_56154"
                            class="Pixso-instance-5634_56154"
                            Size="md"
                            State="Defaut"
                            IsIndeterminate="False"
                            IsChecked="False"
                        />
                    </slot>
                    <slot name="slot_5634_56155">
                        <InputTextBase
                            id="5634_56155"
                            class="Pixso-instance-5634_56155"
                            Type="Number"
                            Size="lg"
                        />
                    </slot>
                    <slot name="slot_5634_56156" v-if="visible_5634_741">
                        <Info
                            id="5634_56156"
                            class="Pixso-instance-5634_56156"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div class="stroke-5634_56153 stroke-gray20-36_1844"></div>
            </div>
            <div
                id="5634_57725"
                class="stroke-wrapper-5634_57725"
                v-if="
                    Type === 'Avatar Group' &&
                    State === 'Hover' &&
                    FormControl === 'Radio'
                "
            >
                <div class="Pixso-symbol-5634_57725 fill-gray5-32_4120">
                    <slot name="slot_5634_57726">
                        <RadioOnly
                            id="5634_57726"
                            class="Pixso-instance-5634_57726"
                            Size="md"
                            State="Default"
                            IsChecked="False"
                        />
                    </slot>
                    <slot name="slot_5634_57727">
                        <AvatarGroup
                            id="5634_57727"
                            class="Pixso-instance-5634_57727"
                            Size="sm"
                            IsAddUser="False"
                            IsMoreUser="True"
                        />
                    </slot>
                    <slot name="slot_5634_57728" v-if="visible_5634_741">
                        <Info
                            id="5634_57728"
                            class="Pixso-instance-5634_57728"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div class="stroke-5634_57725 stroke-gray20-36_1844"></div>
            </div>
            <div
                id="5634_58387"
                class="stroke-wrapper-5634_58387"
                v-if="
                    Type === 'Avatar Group' &&
                    State === 'Hover' &&
                    FormControl === 'Toggle'
                "
            >
                <div class="Pixso-symbol-5634_58387 fill-gray5-32_4120">
                    <slot name="slot_5634_58388">
                        <ToggleOnly
                            id="5634_58388"
                            class="Pixso-instance-5634_58388"
                            IsActive="False"
                            Size="md"
                            State="Default"
                            IsIcon="False"
                        />
                    </slot>
                    <slot name="slot_5634_58389">
                        <AvatarGroup
                            id="5634_58389"
                            class="Pixso-instance-5634_58389"
                            Size="sm"
                            IsAddUser="False"
                            IsMoreUser="True"
                        />
                    </slot>
                    <slot name="slot_5634_58390" v-if="visible_5634_741">
                        <Info
                            id="5634_58390"
                            class="Pixso-instance-5634_58390"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div class="stroke-5634_58387 stroke-gray20-36_1844"></div>
            </div>
            <div
                id="5634_56157"
                class="stroke-wrapper-5634_56157"
                v-if="
                    Type === 'Avatar Group' &&
                    State === 'Hover' &&
                    FormControl === 'Checkbox'
                "
            >
                <div class="Pixso-symbol-5634_56157 fill-gray5-32_4120">
                    <slot name="slot_5634_56158">
                        <CheckboxOnly
                            id="5634_56158"
                            class="Pixso-instance-5634_56158"
                            Size="md"
                            State="Defaut"
                            IsIndeterminate="False"
                            IsChecked="False"
                        />
                    </slot>
                    <slot name="slot_5634_56159">
                        <AvatarGroup
                            id="5634_56159"
                            class="Pixso-instance-5634_56159"
                            Size="sm"
                            IsAddUser="False"
                            IsMoreUser="True"
                        />
                    </slot>
                    <slot name="slot_5634_56160" v-if="visible_5634_741">
                        <Info
                            id="5634_56160"
                            class="Pixso-instance-5634_56160"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div class="stroke-5634_56157 stroke-gray20-36_1844"></div>
            </div>
            <div
                id="5634_57729"
                class="stroke-wrapper-5634_57729"
                v-if="
                    Type === 'Button Icon' &&
                    State === 'Hover' &&
                    FormControl === 'Radio'
                "
            >
                <div class="Pixso-symbol-5634_57729 fill-gray5-32_4120">
                    <slot name="slot_5634_57730">
                        <RadioOnly
                            id="5634_57730"
                            class="Pixso-instance-5634_57730"
                            Size="md"
                            State="Default"
                            IsChecked="False"
                        />
                    </slot>
                    <slot name="slot_5634_57731">
                        <ButtonIcon
                            id="5634_57731"
                            class="Pixso-instance-5634_57731"
                            Hierarchy="No Fill"
                            Size="md"
                            Color="Gray"
                            State="Default"
                        >
                            <template #slot_5590_22158>
                                <TrashSimple
                                    id="5590_22158"
                                    class="Pixso-instance-5590_22158"
                                />
                            </template>
                        </ButtonIcon>
                    </slot>
                    <slot name="slot_5634_57732">
                        <ButtonIcon
                            id="5634_57732"
                            class="Pixso-instance-5634_57732"
                            Hierarchy="No Fill"
                            Size="md"
                            Color="Gray"
                            State="Default"
                        >
                            <template #slot_5590_22158>
                                <Download
                                    id="5590_22158"
                                    class="Pixso-instance-5590_22158"
                                />
                            </template>
                        </ButtonIcon>
                    </slot>
                    <slot name="slot_5634_57733">
                        <ButtonIcon
                            id="5634_57733"
                            class="Pixso-instance-5634_57733"
                            Hierarchy="No Fill"
                            Size="md"
                            Color="Gray"
                            State="Default"
                        >
                            <template #slot_5590_22158>
                                <DotsThreeVertical
                                    id="5590_22158"
                                    class="Pixso-instance-5590_22158"
                                />
                            </template>
                        </ButtonIcon>
                    </slot>
                </div>
                <div class="stroke-5634_57729 stroke-gray20-36_1844"></div>
            </div>
            <div
                id="5634_58391"
                class="stroke-wrapper-5634_58391"
                v-if="
                    Type === 'Button Icon' &&
                    State === 'Hover' &&
                    FormControl === 'Toggle'
                "
            >
                <div class="Pixso-symbol-5634_58391 fill-gray5-32_4120">
                    <slot name="slot_5634_58392">
                        <ToggleOnly
                            id="5634_58392"
                            class="Pixso-instance-5634_58392"
                            IsActive="False"
                            Size="md"
                            State="Default"
                            IsIcon="False"
                        />
                    </slot>
                    <slot name="slot_5634_58393">
                        <ButtonIcon
                            id="5634_58393"
                            class="Pixso-instance-5634_58393"
                            Hierarchy="No Fill"
                            Size="md"
                            Color="Gray"
                            State="Default"
                        >
                            <template #slot_5590_22158>
                                <TrashSimple
                                    id="5590_22158"
                                    class="Pixso-instance-5590_22158"
                                />
                            </template>
                        </ButtonIcon>
                    </slot>
                    <slot name="slot_5634_58394">
                        <ButtonIcon
                            id="5634_58394"
                            class="Pixso-instance-5634_58394"
                            Hierarchy="No Fill"
                            Size="md"
                            Color="Gray"
                            State="Default"
                        >
                            <template #slot_5590_22158>
                                <Download
                                    id="5590_22158"
                                    class="Pixso-instance-5590_22158"
                                />
                            </template>
                        </ButtonIcon>
                    </slot>
                    <slot name="slot_5634_58395">
                        <ButtonIcon
                            id="5634_58395"
                            class="Pixso-instance-5634_58395"
                            Hierarchy="No Fill"
                            Size="md"
                            Color="Gray"
                            State="Default"
                        >
                            <template #slot_5590_22158>
                                <DotsThreeVertical
                                    id="5590_22158"
                                    class="Pixso-instance-5590_22158"
                                />
                            </template>
                        </ButtonIcon>
                    </slot>
                </div>
                <div class="stroke-5634_58391 stroke-gray20-36_1844"></div>
            </div>
            <div
                id="5634_56161"
                class="stroke-wrapper-5634_56161"
                v-if="
                    Type === 'Button Icon' &&
                    State === 'Hover' &&
                    FormControl === 'Checkbox'
                "
            >
                <div class="Pixso-symbol-5634_56161 fill-gray5-32_4120">
                    <slot name="slot_5634_56162">
                        <CheckboxOnly
                            id="5634_56162"
                            class="Pixso-instance-5634_56162"
                            Size="md"
                            State="Defaut"
                            IsIndeterminate="False"
                            IsChecked="False"
                        />
                    </slot>
                    <slot name="slot_5634_56163">
                        <ButtonIcon
                            id="5634_56163"
                            class="Pixso-instance-5634_56163"
                            Hierarchy="No Fill"
                            Size="md"
                            Color="Gray"
                            State="Default"
                        >
                            <template #slot_5590_22158>
                                <TrashSimple
                                    id="5590_22158"
                                    class="Pixso-instance-5590_22158"
                                />
                            </template>
                        </ButtonIcon>
                    </slot>
                    <slot name="slot_5634_56164">
                        <ButtonIcon
                            id="5634_56164"
                            class="Pixso-instance-5634_56164"
                            Hierarchy="No Fill"
                            Size="md"
                            Color="Gray"
                            State="Default"
                        >
                            <template #slot_5590_22158>
                                <Download
                                    id="5590_22158"
                                    class="Pixso-instance-5590_22158"
                                />
                            </template>
                        </ButtonIcon>
                    </slot>
                    <slot name="slot_5634_56165">
                        <ButtonIcon
                            id="5634_56165"
                            class="Pixso-instance-5634_56165"
                            Hierarchy="No Fill"
                            Size="md"
                            Color="Gray"
                            State="Default"
                        >
                            <template #slot_5590_22158>
                                <DotsThreeVertical
                                    id="5590_22158"
                                    class="Pixso-instance-5590_22158"
                                />
                            </template>
                        </ButtonIcon>
                    </slot>
                </div>
                <div class="stroke-5634_56161 stroke-gray20-36_1844"></div>
            </div>
            <div
                id="5634_57734"
                class="stroke-wrapper-5634_57734"
                v-if="
                    Type === 'Button' &&
                    State === 'Hover' &&
                    FormControl === 'Radio'
                "
            >
                <div class="Pixso-symbol-5634_57734 fill-gray5-32_4120">
                    <slot name="slot_5634_57735">
                        <RadioOnly
                            id="5634_57735"
                            class="Pixso-instance-5634_57735"
                            Size="md"
                            State="Default"
                            IsChecked="False"
                        />
                    </slot>
                    <slot name="slot_5634_57736">
                        <Button
                            id="5634_57736"
                            class="Pixso-instance-5634_57736"
                            :visible_5588_131="false"
                            :visible_5588_152="false"
                            text_5588_173="Delete"
                            Size="md"
                            Color="Destructive"
                            Hierarchy="Link"
                            State="Default"
                        >
                            <template #slot_5603_17591>
                                <p
                                    id="5603_17591"
                                    class="Pixso-paragraph-5603_17591 fill-destructive50-423_3219-paragraph text-text-smbold-423_3208"
                                >
                                    {{ "Delete" }}
                                </p>
                            </template>
                        </Button>
                    </slot>
                    <slot name="slot_5634_57737">
                        <Button
                            id="5634_57737"
                            class="Pixso-instance-5634_57737"
                            :visible_5588_131="false"
                            :visible_5588_152="false"
                            text_5588_173="Edit"
                            Size="md"
                            Color="Brand"
                            Hierarchy="Link"
                            State="Default"
                        >
                            <template #slot_5603_17351>
                                <p
                                    id="5603_17351"
                                    class="Pixso-paragraph-5603_17351 fill-brand60-1257_33467-paragraph text-text-smbold-423_3208"
                                >
                                    {{ "Edit" }}
                                </p>
                            </template>
                        </Button>
                    </slot>
                </div>
                <div class="stroke-5634_57734 stroke-gray20-36_1844"></div>
            </div>
            <div
                id="5634_58396"
                class="stroke-wrapper-5634_58396"
                v-if="
                    Type === 'Button' &&
                    State === 'Hover' &&
                    FormControl === 'Toggle'
                "
            >
                <div class="Pixso-symbol-5634_58396 fill-gray5-32_4120">
                    <slot name="slot_5634_58397">
                        <ToggleOnly
                            id="5634_58397"
                            class="Pixso-instance-5634_58397"
                            IsActive="False"
                            Size="md"
                            State="Default"
                            IsIcon="False"
                        />
                    </slot>
                    <slot name="slot_5634_58398">
                        <Button
                            id="5634_58398"
                            class="Pixso-instance-5634_58398"
                            :visible_5588_131="false"
                            :visible_5588_152="false"
                            text_5588_173="Delete"
                            Size="md"
                            Color="Destructive"
                            Hierarchy="Link"
                            State="Default"
                        >
                            <template #slot_5603_17591>
                                <p
                                    id="5603_17591"
                                    class="Pixso-paragraph-5603_17591 fill-destructive50-423_3219-paragraph text-text-smbold-423_3208"
                                >
                                    {{ "Delete" }}
                                </p>
                            </template>
                        </Button>
                    </slot>
                    <slot name="slot_5634_58399">
                        <Button
                            id="5634_58399"
                            class="Pixso-instance-5634_58399"
                            :visible_5588_131="false"
                            :visible_5588_152="false"
                            text_5588_173="Edit"
                            Size="md"
                            Color="Brand"
                            Hierarchy="Link"
                            State="Default"
                        >
                            <template #slot_5603_17351>
                                <p
                                    id="5603_17351"
                                    class="Pixso-paragraph-5603_17351 fill-brand60-1257_33467-paragraph text-text-smbold-423_3208"
                                >
                                    {{ "Edit" }}
                                </p>
                            </template>
                        </Button>
                    </slot>
                </div>
                <div class="stroke-5634_58396 stroke-gray20-36_1844"></div>
            </div>
            <div
                id="5634_56166"
                class="stroke-wrapper-5634_56166"
                v-if="
                    Type === 'Button' &&
                    State === 'Hover' &&
                    FormControl === 'Checkbox'
                "
            >
                <div class="Pixso-symbol-5634_56166 fill-gray5-32_4120">
                    <slot name="slot_5634_56167">
                        <CheckboxOnly
                            id="5634_56167"
                            class="Pixso-instance-5634_56167"
                            Size="md"
                            State="Defaut"
                            IsIndeterminate="False"
                            IsChecked="False"
                        />
                    </slot>
                    <slot name="slot_5634_56168">
                        <Button
                            id="5634_56168"
                            class="Pixso-instance-5634_56168"
                            :visible_5588_131="false"
                            :visible_5588_152="false"
                            text_5588_173="Delete"
                            Size="md"
                            Color="Destructive"
                            Hierarchy="Link"
                            State="Default"
                        >
                            <template #slot_5603_17591>
                                <p
                                    id="5603_17591"
                                    class="Pixso-paragraph-5603_17591 fill-destructive50-423_3219-paragraph text-text-smbold-423_3208"
                                >
                                    {{ "Delete" }}
                                </p>
                            </template>
                        </Button>
                    </slot>
                    <slot name="slot_5634_56169">
                        <Button
                            id="5634_56169"
                            class="Pixso-instance-5634_56169"
                            :visible_5588_131="false"
                            :visible_5588_152="false"
                            text_5588_173="Edit"
                            Size="md"
                            Color="Brand"
                            Hierarchy="Link"
                            State="Default"
                        >
                            <template #slot_5603_17351>
                                <p
                                    id="5603_17351"
                                    class="Pixso-paragraph-5603_17351 fill-brand60-1257_33467-paragraph text-text-smbold-423_3208"
                                >
                                    {{ "Edit" }}
                                </p>
                            </template>
                        </Button>
                    </slot>
                </div>
                <div class="stroke-5634_56166 stroke-gray20-36_1844"></div>
            </div>
            <div
                id="5634_57738"
                class="stroke-wrapper-5634_57738"
                v-if="
                    Type === 'Rating' &&
                    State === 'Hover' &&
                    FormControl === 'Radio'
                "
            >
                <div class="Pixso-symbol-5634_57738 fill-gray5-32_4120">
                    <slot name="slot_5634_57739">
                        <RadioOnly
                            id="5634_57739"
                            class="Pixso-instance-5634_57739"
                            Size="md"
                            State="Default"
                            IsChecked="False"
                        />
                    </slot>
                    <slot name="slot_5634_57740">
                        <Rating
                            id="5634_57740"
                            class="Pixso-instance-5634_57740"
                            Star="5"
                            Size="md"
                            Color="Default"
                        />
                    </slot>
                    <slot name="slot_5634_57741" v-if="visible_5633_717">
                        <p
                            id="5634_57741"
                            class="Pixso-paragraph-5634_57741 fill-gray60-83_2722-paragraph text-text-mdsemibold-423_3206"
                        >
                            {{ text_5633_729 ?? "4.5" }}
                        </p>
                    </slot>
                </div>
                <div class="stroke-5634_57738 stroke-gray20-36_1844"></div>
            </div>
            <div
                id="5634_58400"
                class="stroke-wrapper-5634_58400"
                v-if="
                    Type === 'Rating' &&
                    State === 'Hover' &&
                    FormControl === 'Toggle'
                "
            >
                <div class="Pixso-symbol-5634_58400 fill-gray5-32_4120">
                    <slot name="slot_5634_58401">
                        <ToggleOnly
                            id="5634_58401"
                            class="Pixso-instance-5634_58401"
                            IsActive="False"
                            Size="md"
                            State="Default"
                            IsIcon="False"
                        />
                    </slot>
                    <slot name="slot_5634_58402">
                        <Rating
                            id="5634_58402"
                            class="Pixso-instance-5634_58402"
                            Star="5"
                            Size="md"
                            Color="Default"
                        />
                    </slot>
                    <slot name="slot_5634_58403" v-if="visible_5633_717">
                        <p
                            id="5634_58403"
                            class="Pixso-paragraph-5634_58403 fill-gray60-83_2722-paragraph text-text-mdsemibold-423_3206"
                        >
                            {{ text_5633_729 ?? "4.5" }}
                        </p>
                    </slot>
                </div>
                <div class="stroke-5634_58400 stroke-gray20-36_1844"></div>
            </div>
            <div
                id="5634_56170"
                class="stroke-wrapper-5634_56170"
                v-if="
                    Type === 'Rating' &&
                    State === 'Hover' &&
                    FormControl === 'Checkbox'
                "
            >
                <div class="Pixso-symbol-5634_56170 fill-gray5-32_4120">
                    <slot name="slot_5634_56171">
                        <CheckboxOnly
                            id="5634_56171"
                            class="Pixso-instance-5634_56171"
                            Size="md"
                            State="Defaut"
                            IsIndeterminate="False"
                            IsChecked="False"
                        />
                    </slot>
                    <slot name="slot_5634_56172">
                        <Rating
                            id="5634_56172"
                            class="Pixso-instance-5634_56172"
                            Star="5"
                            Size="md"
                            Color="Default"
                        />
                    </slot>
                    <slot name="slot_5634_56173" v-if="visible_5633_717">
                        <p
                            id="5634_56173"
                            class="Pixso-paragraph-5634_56173 fill-gray60-83_2722-paragraph text-text-mdsemibold-423_3206"
                        >
                            {{ text_5633_729 ?? "4.5" }}
                        </p>
                    </slot>
                </div>
                <div class="stroke-5634_56170 stroke-gray20-36_1844"></div>
            </div>
            <div
                id="5634_57742"
                class="stroke-wrapper-5634_57742"
                v-if="
                    Type === 'Trend' &&
                    State === 'Hover' &&
                    FormControl === 'Radio'
                "
            >
                <div class="Pixso-symbol-5634_57742 fill-gray5-32_4120">
                    <slot name="slot_5634_57743">
                        <RadioOnly
                            id="5634_57743"
                            class="Pixso-instance-5634_57743"
                            Size="md"
                            State="Default"
                            IsChecked="False"
                        />
                    </slot>
                    <div id="5634_57744" class="Pixso-frame-5634_57744">
                        <slot name="slot_5634_57745" v-if="visible_5986_57">
                            <p
                                id="5634_57745"
                                class="Pixso-paragraph-5634_57745 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                            >
                                {{ text_5565_13 ?? "Main Text" }}
                            </p>
                        </slot>
                        <slot name="slot_5634_57746">
                            <BadgeText
                                id="5634_57746"
                                class="Pixso-instance-5634_57746"
                                :visible_5586_119="false"
                                :visible_5586_121="false"
                                text_5588_129="48%"
                                Size="sm"
                                Color="Success"
                                Hierarchy="Secondary"
                                State="Default"
                            >
                                <template #slot_5588_12217>
                                    <TrendUp
                                        id="5588_12217"
                                        class="Pixso-instance-5588_12217"
                                    />
                                </template>
                                <template #slot_5588_12220>
                                    <p
                                        id="5588_12220"
                                        class="Pixso-paragraph-5588_12220 fill-success50-1636_81205-paragraph text-text-xssemibold-439_9521"
                                    >
                                        {{ "48%" }}
                                    </p>
                                </template>
                            </BadgeText>
                        </slot>
                    </div>
                    <slot name="slot_5634_57747" v-if="visible_5634_741">
                        <Info
                            id="5634_57747"
                            class="Pixso-instance-5634_57747"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div class="stroke-5634_57742 stroke-gray20-36_1844"></div>
            </div>
            <div
                id="5634_58404"
                class="stroke-wrapper-5634_58404"
                v-if="
                    Type === 'Trend' &&
                    State === 'Hover' &&
                    FormControl === 'Toggle'
                "
            >
                <div class="Pixso-symbol-5634_58404 fill-gray5-32_4120">
                    <slot name="slot_5634_58405">
                        <ToggleOnly
                            id="5634_58405"
                            class="Pixso-instance-5634_58405"
                            IsActive="False"
                            Size="md"
                            State="Default"
                            IsIcon="False"
                        />
                    </slot>
                    <div id="5634_58406" class="Pixso-frame-5634_58406">
                        <slot name="slot_5634_58407" v-if="visible_5986_57">
                            <p
                                id="5634_58407"
                                class="Pixso-paragraph-5634_58407 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                            >
                                {{ text_5565_13 ?? "Main Text" }}
                            </p>
                        </slot>
                        <slot name="slot_5634_58408">
                            <BadgeText
                                id="5634_58408"
                                class="Pixso-instance-5634_58408"
                                :visible_5586_119="false"
                                :visible_5586_121="false"
                                text_5588_129="48%"
                                Size="sm"
                                Color="Success"
                                Hierarchy="Secondary"
                                State="Default"
                            >
                                <template #slot_5588_12217>
                                    <TrendUp
                                        id="5588_12217"
                                        class="Pixso-instance-5588_12217"
                                    />
                                </template>
                                <template #slot_5588_12220>
                                    <p
                                        id="5588_12220"
                                        class="Pixso-paragraph-5588_12220 fill-success50-1636_81205-paragraph text-text-xssemibold-439_9521"
                                    >
                                        {{ "48%" }}
                                    </p>
                                </template>
                            </BadgeText>
                        </slot>
                    </div>
                    <slot name="slot_5634_58409" v-if="visible_5634_741">
                        <Info
                            id="5634_58409"
                            class="Pixso-instance-5634_58409"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div class="stroke-5634_58404 stroke-gray20-36_1844"></div>
            </div>
            <div
                id="5634_56174"
                class="stroke-wrapper-5634_56174"
                v-if="
                    Type === 'Trend' &&
                    State === 'Hover' &&
                    FormControl === 'Checkbox'
                "
            >
                <div class="Pixso-symbol-5634_56174 fill-gray5-32_4120">
                    <slot name="slot_5634_56175">
                        <CheckboxOnly
                            id="5634_56175"
                            class="Pixso-instance-5634_56175"
                            Size="md"
                            State="Defaut"
                            IsIndeterminate="False"
                            IsChecked="False"
                        />
                    </slot>
                    <div id="5634_56176" class="Pixso-frame-5634_56176">
                        <slot name="slot_5634_56177" v-if="visible_5986_57">
                            <p
                                id="5634_56177"
                                class="Pixso-paragraph-5634_56177 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                            >
                                {{ text_5565_13 ?? "Main Text" }}
                            </p>
                        </slot>
                        <slot name="slot_5634_56178">
                            <BadgeText
                                id="5634_56178"
                                class="Pixso-instance-5634_56178"
                                :visible_5586_119="false"
                                :visible_5586_121="false"
                                text_5588_129="48%"
                                Size="sm"
                                Color="Success"
                                Hierarchy="Secondary"
                                State="Default"
                            >
                                <template #slot_5588_12217>
                                    <TrendUp
                                        id="5588_12217"
                                        class="Pixso-instance-5588_12217"
                                    />
                                </template>
                                <template #slot_5588_12220>
                                    <p
                                        id="5588_12220"
                                        class="Pixso-paragraph-5588_12220 fill-success50-1636_81205-paragraph text-text-xssemibold-439_9521"
                                    >
                                        {{ "48%" }}
                                    </p>
                                </template>
                            </BadgeText>
                        </slot>
                    </div>
                    <slot name="slot_5634_56179" v-if="visible_5634_741">
                        <Info
                            id="5634_56179"
                            class="Pixso-instance-5634_56179"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div class="stroke-5634_56174 stroke-gray20-36_1844"></div>
            </div>
            <div
                id="5634_57748"
                class="stroke-wrapper-5634_57748"
                v-if="
                    Type === 'Badge Single' &&
                    State === 'Hover' &&
                    FormControl === 'Radio'
                "
            >
                <div class="Pixso-symbol-5634_57748 fill-gray5-32_4120">
                    <slot name="slot_5634_57749">
                        <RadioOnly
                            id="5634_57749"
                            class="Pixso-instance-5634_57749"
                            Size="md"
                            State="Default"
                            IsChecked="False"
                        />
                    </slot>
                    <slot name="slot_5634_57750">
                        <BadgeText
                            id="5634_57750"
                            class="Pixso-instance-5634_57750"
                            :visible_5586_119="false"
                            :visible_5586_121="false"
                            :visible_5586_123="false"
                            Size="sm"
                            Color="Brand"
                            Hierarchy="Secondary"
                            State="Default"
                        />
                    </slot>
                    <slot name="slot_5634_57751" v-if="visible_5634_741">
                        <Info
                            id="5634_57751"
                            class="Pixso-instance-5634_57751"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div class="stroke-5634_57748 stroke-gray20-36_1844"></div>
            </div>
            <div
                id="5634_58410"
                class="stroke-wrapper-5634_58410"
                v-if="
                    Type === 'Badge Single' &&
                    State === 'Hover' &&
                    FormControl === 'Toggle'
                "
            >
                <div class="Pixso-symbol-5634_58410 fill-gray5-32_4120">
                    <slot name="slot_5634_58411">
                        <ToggleOnly
                            id="5634_58411"
                            class="Pixso-instance-5634_58411"
                            IsActive="False"
                            Size="md"
                            State="Default"
                            IsIcon="False"
                        />
                    </slot>
                    <slot name="slot_5634_58412">
                        <BadgeText
                            id="5634_58412"
                            class="Pixso-instance-5634_58412"
                            :visible_5586_119="false"
                            :visible_5586_121="false"
                            :visible_5586_123="false"
                            Size="sm"
                            Color="Brand"
                            Hierarchy="Secondary"
                            State="Default"
                        />
                    </slot>
                    <slot name="slot_5634_58413" v-if="visible_5634_741">
                        <Info
                            id="5634_58413"
                            class="Pixso-instance-5634_58413"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div class="stroke-5634_58410 stroke-gray20-36_1844"></div>
            </div>
            <div
                id="5634_56180"
                class="stroke-wrapper-5634_56180"
                v-if="
                    Type === 'Badge Single' &&
                    State === 'Hover' &&
                    FormControl === 'Checkbox'
                "
            >
                <div class="Pixso-symbol-5634_56180 fill-gray5-32_4120">
                    <slot name="slot_5634_56181">
                        <CheckboxOnly
                            id="5634_56181"
                            class="Pixso-instance-5634_56181"
                            Size="md"
                            State="Defaut"
                            IsIndeterminate="False"
                            IsChecked="False"
                        />
                    </slot>
                    <slot name="slot_5634_56182">
                        <BadgeText
                            id="5634_56182"
                            class="Pixso-instance-5634_56182"
                            :visible_5586_119="false"
                            :visible_5586_121="false"
                            :visible_5586_123="false"
                            Size="sm"
                            Color="Brand"
                            Hierarchy="Secondary"
                            State="Default"
                        />
                    </slot>
                    <slot name="slot_5634_56183" v-if="visible_5634_741">
                        <Info
                            id="5634_56183"
                            class="Pixso-instance-5634_56183"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div class="stroke-5634_56180 stroke-gray20-36_1844"></div>
            </div>
            <div
                id="5634_57752"
                class="stroke-wrapper-5634_57752"
                v-if="
                    Type === 'Badge Group' &&
                    State === 'Hover' &&
                    FormControl === 'Radio'
                "
            >
                <div class="Pixso-symbol-5634_57752 fill-gray5-32_4120">
                    <slot name="slot_5634_57753">
                        <RadioOnly
                            id="5634_57753"
                            class="Pixso-instance-5634_57753"
                            Size="md"
                            State="Default"
                            IsChecked="False"
                        />
                    </slot>
                    <div id="5634_57754" class="Pixso-frame-5634_57754">
                        <slot name="slot_5634_57755">
                            <BadgeText
                                id="5634_57755"
                                class="Pixso-instance-5634_57755"
                                :visible_5586_119="false"
                                :visible_5586_121="false"
                                :visible_5586_123="false"
                                Size="sm"
                                Color="Brand"
                                Hierarchy="Secondary"
                                State="Default"
                            />
                        </slot>
                        <slot name="slot_5634_57756">
                            <BadgeText
                                id="5634_57756"
                                class="Pixso-instance-5634_57756"
                                :visible_5586_119="false"
                                :visible_5586_121="false"
                                :visible_5586_123="false"
                                Size="sm"
                                Color="Warning"
                                Hierarchy="Secondary"
                                State="Default"
                            />
                        </slot>
                        <slot name="slot_5634_57757">
                            <BadgeText
                                id="5634_57757"
                                class="Pixso-instance-5634_57757"
                                :visible_5586_119="false"
                                :visible_5586_121="false"
                                :visible_5586_123="false"
                                Size="sm"
                                Color="Destructive"
                                Hierarchy="Secondary"
                                State="Default"
                            />
                        </slot>
                    </div>
                    <slot name="slot_5634_57758" v-if="visible_5634_741">
                        <Info
                            id="5634_57758"
                            class="Pixso-instance-5634_57758"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div class="stroke-5634_57752 stroke-gray20-36_1844"></div>
            </div>
            <div
                id="5634_58414"
                class="stroke-wrapper-5634_58414"
                v-if="
                    Type === 'Badge Group' &&
                    State === 'Hover' &&
                    FormControl === 'Toggle'
                "
            >
                <div class="Pixso-symbol-5634_58414 fill-gray5-32_4120">
                    <slot name="slot_5634_58415">
                        <ToggleOnly
                            id="5634_58415"
                            class="Pixso-instance-5634_58415"
                            IsActive="False"
                            Size="md"
                            State="Default"
                            IsIcon="False"
                        />
                    </slot>
                    <div id="5634_58416" class="Pixso-frame-5634_58416">
                        <slot name="slot_5634_58417">
                            <BadgeText
                                id="5634_58417"
                                class="Pixso-instance-5634_58417"
                                :visible_5586_119="false"
                                :visible_5586_121="false"
                                :visible_5586_123="false"
                                Size="sm"
                                Color="Brand"
                                Hierarchy="Secondary"
                                State="Default"
                            />
                        </slot>
                        <slot name="slot_5634_58418">
                            <BadgeText
                                id="5634_58418"
                                class="Pixso-instance-5634_58418"
                                :visible_5586_119="false"
                                :visible_5586_121="false"
                                :visible_5586_123="false"
                                Size="sm"
                                Color="Warning"
                                Hierarchy="Secondary"
                                State="Default"
                            />
                        </slot>
                        <slot name="slot_5634_58419">
                            <BadgeText
                                id="5634_58419"
                                class="Pixso-instance-5634_58419"
                                :visible_5586_119="false"
                                :visible_5586_121="false"
                                :visible_5586_123="false"
                                Size="sm"
                                Color="Destructive"
                                Hierarchy="Secondary"
                                State="Default"
                            />
                        </slot>
                    </div>
                    <slot name="slot_5634_58420" v-if="visible_5634_741">
                        <Info
                            id="5634_58420"
                            class="Pixso-instance-5634_58420"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div class="stroke-5634_58414 stroke-gray20-36_1844"></div>
            </div>
            <div
                id="5634_56184"
                class="stroke-wrapper-5634_56184"
                v-if="
                    Type === 'Badge Group' &&
                    State === 'Hover' &&
                    FormControl === 'Checkbox'
                "
            >
                <div class="Pixso-symbol-5634_56184 fill-gray5-32_4120">
                    <slot name="slot_5634_56185">
                        <CheckboxOnly
                            id="5634_56185"
                            class="Pixso-instance-5634_56185"
                            Size="md"
                            State="Defaut"
                            IsIndeterminate="False"
                            IsChecked="False"
                        />
                    </slot>
                    <div id="5634_56186" class="Pixso-frame-5634_56186">
                        <slot name="slot_5634_56187">
                            <BadgeText
                                id="5634_56187"
                                class="Pixso-instance-5634_56187"
                                :visible_5586_119="false"
                                :visible_5586_121="false"
                                :visible_5586_123="false"
                                Size="sm"
                                Color="Brand"
                                Hierarchy="Secondary"
                                State="Default"
                            />
                        </slot>
                        <slot name="slot_5634_56188">
                            <BadgeText
                                id="5634_56188"
                                class="Pixso-instance-5634_56188"
                                :visible_5586_119="false"
                                :visible_5586_121="false"
                                :visible_5586_123="false"
                                Size="sm"
                                Color="Warning"
                                Hierarchy="Secondary"
                                State="Default"
                            />
                        </slot>
                        <slot name="slot_5634_56189">
                            <BadgeText
                                id="5634_56189"
                                class="Pixso-instance-5634_56189"
                                :visible_5586_119="false"
                                :visible_5586_121="false"
                                :visible_5586_123="false"
                                Size="sm"
                                Color="Destructive"
                                Hierarchy="Secondary"
                                State="Default"
                            />
                        </slot>
                    </div>
                    <slot name="slot_5634_56190" v-if="visible_5634_741">
                        <Info
                            id="5634_56190"
                            class="Pixso-instance-5634_56190"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div class="stroke-5634_56184 stroke-gray20-36_1844"></div>
            </div>
        </div>
    </div>
</template>
<script lang="ts" setup>
import Info from "@/components/Info.vue";
import Avatar from "@/components/Avatar.vue";
import IconContainer from "@/components/Iconcontainer.vue";
import FileImage from "@/components/Fileimage.vue";
import PaymentLogo from "@/components/Paymentlogo.vue";
import Flags from "@/components/Flags.vue";
import ProgressBar from "@/components/Progressbar.vue";
import InputTextBase from "@/components/Inputtextbase.vue";
import AvatarGroup from "@/components/Avatargroup.vue";
import ButtonIcon from "@/components/Buttonicon.vue";
import TrashSimple from "@/components/Trashsimple.vue";
import Download from "@/components/Download.vue";
import DotsThreeVertical from "@/components/Dotsthreevertical.vue";
import Button from "@/components/Button.vue";
import Rating from "@/components/Rating.vue";
import BadgeText from "@/components/Badgetext.vue";
import TrendUp from "@/components/Trendup.vue";
import CheckboxOnly from "@/components/Checkboxonly.vue";
import RadioOnly from "@/components/Radioonly.vue";
import ToggleOnly from "@/components/Toggleonly.vue";
const props = defineProps({
    visible_5565_0: { type: Boolean, default: true },
    text_5565_13: { type: String, default: "Main Text" },
    text_5565_26: { type: String, default: "Supporting Text" },
    visible_5633_717: { type: Boolean, default: true },
    text_5633_729: { type: String, default: "4.5" },
    visible_5634_741: { type: Boolean, default: true },
    visible_5986_57: { type: Boolean, default: true },
    Type: { type: String },
    State: { type: String },
    FormControl: { type: String }
});
</script>
<style>
.Pixso-symbol-5561_52659 {
}
.Pixso-symbol-5561_52629 {
    width: 100%;
    height: 100%;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 12px 24px 12px 24px;
    min-height: 72px;
}
.stroke-wrapper-5561_52629 {
    position: relative;
    width: 343px;
    height: auto;
    display: flex;
}
.stroke-5561_52629 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 1px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-frame-5631_53408 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: flex-start;
    flex-grow: 1;
    flex-basis: 0;
}
.frame-content-5631_53408 {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: center;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5561_52617 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-paragraph-5631_53387 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5631_53518 {
    width: 20px;
    height: 20px;
}
.Pixso-symbol-5631_53447 {
    width: 100%;
    height: 100%;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 12px 24px 12px 24px;
    min-height: 72px;
}
.stroke-wrapper-5631_53447 {
    position: relative;
    width: 343px;
    height: auto;
    display: flex;
}
.stroke-5631_53447 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 1px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5631_53453 {
    width: 40px;
    height: 40px;
}
.Pixso-frame-5631_53448 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: flex-start;
    flex-grow: 1;
    flex-basis: 0;
}
.frame-content-5631_53448 {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: center;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5631_53449 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-paragraph-5631_53450 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5631_53575 {
    width: 20px;
    height: 20px;
}
.Pixso-symbol-5631_53459 {
    width: 100%;
    height: 100%;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 12px 24px 12px 24px;
    min-height: 72px;
}
.stroke-wrapper-5631_53459 {
    position: relative;
    width: 343px;
    height: auto;
    display: flex;
}
.stroke-5631_53459 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 1px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5631_53464 {
    width: 40px;
    height: 40px;
}
.Pixso-instance-5546_2917 {
    width: undefinedpx;
    height: undefinedpx;
}
.Pixso-frame-5631_53461 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: flex-start;
    flex-grow: 1;
    flex-basis: 0;
}
.frame-content-5631_53461 {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: center;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5631_53462 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-paragraph-5631_53463 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5631_53577 {
    width: 20px;
    height: 20px;
}
.Pixso-symbol-5633_54611 {
    width: 100%;
    height: 100%;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 12px 24px 12px 24px;
    min-height: 72px;
}
.stroke-wrapper-5633_54611 {
    position: relative;
    width: 343px;
    height: auto;
    display: flex;
}
.stroke-5633_54611 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 1px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5633_54620 {
    width: 36px;
    height: 24px;
}
.Pixso-frame-5633_54613 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: flex-start;
    flex-grow: 1;
    flex-basis: 0;
}
.frame-content-5633_54613 {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: center;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5633_54614 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-paragraph-5633_54615 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5633_54616 {
    width: 20px;
    height: 20px;
}
.Pixso-symbol-5631_53483 {
    width: 100%;
    height: 100%;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 12px 24px 12px 24px;
    min-height: 72px;
}
.stroke-wrapper-5631_53483 {
    position: relative;
    width: 343px;
    height: auto;
    display: flex;
}
.stroke-5631_53483 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 1px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-frame-5631_53490 {
    width: 40px;
    height: 40px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    border-radius: 12px 12px 12px 12px;
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-image: url(@/assets/images/fd6c3c9d619f8227fa8fac58deaaeef02777ba71.png);
}
.Pixso-frame-5631_53485 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: flex-start;
    flex-grow: 1;
    flex-basis: 0;
}
.frame-content-5631_53485 {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: center;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5631_53486 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-paragraph-5631_53487 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5631_53579 {
    width: 20px;
    height: 20px;
}
.Pixso-symbol-5631_53496 {
    width: 100%;
    height: 100%;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 12px 24px 12px 24px;
    min-height: 72px;
}
.stroke-wrapper-5631_53496 {
    position: relative;
    width: 343px;
    height: auto;
    display: flex;
}
.stroke-5631_53496 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 1px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5631_53501 {
    width: 32px;
    height: 32px;
}
.Pixso-frame-5631_53498 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: flex-start;
    flex-grow: 1;
    flex-basis: 0;
}
.frame-content-5631_53498 {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: center;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5631_53499 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-paragraph-5631_53500 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5631_53581 {
    width: 20px;
    height: 20px;
}
.Pixso-symbol-5631_53793 {
    width: 100%;
    height: 100%;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 12px 24px 12px 24px;
    min-height: 72px;
}
.stroke-wrapper-5631_53793 {
    position: relative;
    width: 343px;
    height: auto;
    display: flex;
}
.stroke-5631_53793 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 1px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5631_53816 {
    width: 263px;
    height: 20px;
}
.Pixso-instance-5631_54072 {
    width: 274px;
    height: 12px;
}
.Pixso-instance-5631_53798 {
    width: 20px;
    height: 20px;
}
.Pixso-symbol-5633_54346 {
    width: 100%;
    height: 100%;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 12px 24px 12px 24px;
    min-height: 72px;
}
.stroke-wrapper-5633_54346 {
    position: relative;
    width: 343px;
    height: auto;
    display: flex;
}
.stroke-5633_54346 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 1px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5633_54355 {
    width: 263px;
    height: 48px;
}
.Pixso-instance-5633_54348 {
    width: 20px;
    height: 20px;
}
.Pixso-symbol-5633_54566 {
    width: 100%;
    height: 100%;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 12px 24px 12px 24px;
    min-height: 72px;
}
.stroke-wrapper-5633_54566 {
    position: relative;
    width: auto;
    height: auto;
    display: flex;
}
.stroke-5633_54566 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 1px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5633_54576 {
    width: 200px;
    height: 32px;
}
.Pixso-instance-5633_54568 {
    width: 20px;
    height: 20px;
}
.Pixso-symbol-5633_54378 {
    width: 100%;
    height: 100%;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
    padding: 12px 24px 12px 24px;
    min-height: 72px;
}
.stroke-wrapper-5633_54378 {
    position: relative;
    width: auto;
    height: auto;
    display: flex;
}
.stroke-5633_54378 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 1px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5633_54393 {
    width: 40px;
    height: 40px;
}
.Pixso-instance-5590_22158 {
    width: undefinedpx;
    height: undefinedpx;
}
.Pixso-instance-5633_54396 {
    width: 40px;
    height: 40px;
}
.Pixso-instance-5633_54402 {
    width: 40px;
    height: 40px;
}
.Pixso-symbol-5633_54444 {
    width: 100%;
    height: 100%;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 12px 24px 12px 24px;
    min-height: 72px;
}
.stroke-wrapper-5633_54444 {
    position: relative;
    width: auto;
    height: auto;
    display: flex;
}
.stroke-5633_54444 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 1px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5633_54457 {
    width: 45px;
    height: 20px;
}
.Pixso-paragraph-5603_17591 {
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    width: auto;
    height: auto;
    flex-grow: 0;
}
.Pixso-instance-5633_54468 {
    width: 27px;
    height: 20px;
}
.Pixso-paragraph-5603_17351 {
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    width: auto;
    height: auto;
    flex-grow: 0;
}
.Pixso-symbol-5633_54418 {
    width: 100%;
    height: 100%;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 12px 24px 12px 24px;
    min-height: 72px;
}
.stroke-wrapper-5633_54418 {
    position: relative;
    width: auto;
    height: auto;
    display: flex;
}
.stroke-5633_54418 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 1px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5633_54526 {
    width: 152px;
    height: 24px;
}
.Pixso-paragraph-5633_54537 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-symbol-5631_53686 {
    width: 100%;
    height: 100%;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 12px 24px 12px 24px;
    min-height: 72px;
}
.stroke-wrapper-5631_53686 {
    position: relative;
    width: auto;
    height: auto;
    display: flex;
}
.stroke-5631_53686 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 1px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-frame-5631_53726 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
}
.Pixso-paragraph-5631_53689 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5631_53709 {
    width: 60px;
    height: 24px;
}
.Pixso-instance-5588_12217 {
    width: undefinedpx;
    height: undefinedpx;
}
.Pixso-paragraph-5588_12220 {
    text-align: center;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    width: auto;
    height: auto;
    flex-grow: 0;
}
.Pixso-instance-5631_53691 {
    width: 20px;
    height: 20px;
}
.Pixso-symbol-5633_54639 {
    width: 100%;
    height: 100%;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 12px 24px 12px 24px;
    min-height: 72px;
}
.stroke-wrapper-5633_54639 {
    position: relative;
    width: auto;
    height: auto;
    display: flex;
}
.stroke-5633_54639 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 1px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5633_54642 {
    width: 48px;
    height: 24px;
}
.Pixso-instance-5633_54643 {
    width: 20px;
    height: 20px;
}
.Pixso-symbol-5633_54663 {
    width: 100%;
    height: 100%;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 12px 24px 12px 24px;
    min-height: 72px;
}
.stroke-wrapper-5633_54663 {
    position: relative;
    width: auto;
    height: auto;
    display: flex;
}
.stroke-5633_54663 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 1px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-frame-5633_54693 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
}
.Pixso-instance-5633_54664 {
    width: 48px;
    height: 24px;
}
.Pixso-instance-5633_54675 {
    width: 48px;
    height: 24px;
}
.Pixso-instance-5633_54684 {
    width: 48px;
    height: 24px;
}
.Pixso-instance-5633_54665 {
    width: 20px;
    height: 20px;
}
.Pixso-symbol-5634_54959 {
    width: 100%;
    height: 100%;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 12px 24px 12px 24px;
    min-height: 72px;
}
.stroke-wrapper-5634_54959 {
    position: relative;
    width: 343px;
    height: auto;
    display: flex;
}
.stroke-5634_54959 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 1px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-frame-5634_54960 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: flex-start;
    flex-grow: 1;
    flex-basis: 0;
}
.frame-content-5634_54960 {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: center;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5634_54961 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-paragraph-5634_54962 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5634_54963 {
    width: 20px;
    height: 20px;
}
.Pixso-symbol-5634_54964 {
    width: 100%;
    height: 100%;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 12px 24px 12px 24px;
    min-height: 72px;
}
.stroke-wrapper-5634_54964 {
    position: relative;
    width: 343px;
    height: auto;
    display: flex;
}
.stroke-5634_54964 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 1px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_54965 {
    width: 40px;
    height: 40px;
}
.Pixso-frame-5634_54966 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: flex-start;
    flex-grow: 1;
    flex-basis: 0;
}
.frame-content-5634_54966 {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: center;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5634_54967 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-paragraph-5634_54968 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5634_54969 {
    width: 20px;
    height: 20px;
}
.Pixso-symbol-5634_54970 {
    width: 100%;
    height: 100%;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 12px 24px 12px 24px;
    min-height: 72px;
}
.stroke-wrapper-5634_54970 {
    position: relative;
    width: 343px;
    height: auto;
    display: flex;
}
.stroke-5634_54970 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 1px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_54971 {
    width: 40px;
    height: 40px;
}
.Pixso-frame-5634_54972 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: flex-start;
    flex-grow: 1;
    flex-basis: 0;
}
.frame-content-5634_54972 {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: center;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5634_54973 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-paragraph-5634_54974 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5634_54975 {
    width: 20px;
    height: 20px;
}
.Pixso-symbol-5634_54976 {
    width: 100%;
    height: 100%;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 12px 24px 12px 24px;
    min-height: 72px;
}
.stroke-wrapper-5634_54976 {
    position: relative;
    width: 343px;
    height: auto;
    display: flex;
}
.stroke-5634_54976 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 1px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_54977 {
    width: 36px;
    height: 24px;
}
.Pixso-frame-5634_54978 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: flex-start;
    flex-grow: 1;
    flex-basis: 0;
}
.frame-content-5634_54978 {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: center;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5634_54979 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-paragraph-5634_54980 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5634_54981 {
    width: 20px;
    height: 20px;
}
.Pixso-symbol-5634_54982 {
    width: 100%;
    height: 100%;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 12px 24px 12px 24px;
    min-height: 72px;
}
.stroke-wrapper-5634_54982 {
    position: relative;
    width: 343px;
    height: auto;
    display: flex;
}
.stroke-5634_54982 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 1px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-frame-5634_54983 {
    width: 40px;
    height: 40px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    border-radius: 12px 12px 12px 12px;
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-image: url(@/assets/images/fd6c3c9d619f8227fa8fac58deaaeef02777ba71.png);
}
.Pixso-frame-5634_54984 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: flex-start;
    flex-grow: 1;
    flex-basis: 0;
}
.frame-content-5634_54984 {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: center;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5634_54985 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-paragraph-5634_54986 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5634_54987 {
    width: 20px;
    height: 20px;
}
.Pixso-symbol-5634_54988 {
    width: 100%;
    height: 100%;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 12px 24px 12px 24px;
    min-height: 72px;
}
.stroke-wrapper-5634_54988 {
    position: relative;
    width: 343px;
    height: auto;
    display: flex;
}
.stroke-5634_54988 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 1px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_54989 {
    width: 32px;
    height: 32px;
}
.Pixso-frame-5634_54990 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: flex-start;
    flex-grow: 1;
    flex-basis: 0;
}
.frame-content-5634_54990 {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: center;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5634_54991 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-paragraph-5634_54992 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5634_54993 {
    width: 20px;
    height: 20px;
}
.Pixso-symbol-5634_54994 {
    width: 100%;
    height: 100%;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 12px 24px 12px 24px;
    min-height: 72px;
}
.stroke-wrapper-5634_54994 {
    position: relative;
    width: 343px;
    height: auto;
    display: flex;
}
.stroke-5634_54994 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 1px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_54995 {
    width: 263px;
    height: 20px;
}
.Pixso-instance-5634_54996 {
    width: 20px;
    height: 20px;
}
.Pixso-symbol-5634_54997 {
    width: 100%;
    height: 100%;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 12px 24px 12px 24px;
    min-height: 72px;
}
.stroke-wrapper-5634_54997 {
    position: relative;
    width: 343px;
    height: auto;
    display: flex;
}
.stroke-5634_54997 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 1px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_54998 {
    width: 263px;
    height: 48px;
}
.Pixso-instance-5634_54999 {
    width: 20px;
    height: 20px;
}
.Pixso-symbol-5634_55000 {
    width: 100%;
    height: 100%;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 12px 24px 12px 24px;
    min-height: 72px;
}
.stroke-wrapper-5634_55000 {
    position: relative;
    width: auto;
    height: auto;
    display: flex;
}
.stroke-5634_55000 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 1px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_55001 {
    width: 200px;
    height: 32px;
}
.Pixso-instance-5634_55002 {
    width: 20px;
    height: 20px;
}
.Pixso-symbol-5634_55003 {
    width: 100%;
    height: 100%;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
    padding: 12px 24px 12px 24px;
    min-height: 72px;
}
.stroke-wrapper-5634_55003 {
    position: relative;
    width: auto;
    height: auto;
    display: flex;
}
.stroke-5634_55003 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 1px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_55004 {
    width: 40px;
    height: 40px;
}
.Pixso-instance-5634_55005 {
    width: 40px;
    height: 40px;
}
.Pixso-instance-5634_55006 {
    width: 40px;
    height: 40px;
}
.Pixso-symbol-5634_55007 {
    width: 100%;
    height: 100%;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 12px 24px 12px 24px;
    min-height: 72px;
}
.stroke-wrapper-5634_55007 {
    position: relative;
    width: auto;
    height: auto;
    display: flex;
}
.stroke-5634_55007 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 1px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_55008 {
    width: 45px;
    height: 20px;
}
.Pixso-instance-5634_55009 {
    width: 27px;
    height: 20px;
}
.Pixso-symbol-5634_55010 {
    width: 100%;
    height: 100%;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 12px 24px 12px 24px;
    min-height: 72px;
}
.stroke-wrapper-5634_55010 {
    position: relative;
    width: auto;
    height: auto;
    display: flex;
}
.stroke-5634_55010 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 1px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_55011 {
    width: 152px;
    height: 24px;
}
.Pixso-paragraph-5634_55012 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-symbol-5634_55013 {
    width: 100%;
    height: 100%;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 12px 24px 12px 24px;
    min-height: 72px;
}
.stroke-wrapper-5634_55013 {
    position: relative;
    width: auto;
    height: auto;
    display: flex;
}
.stroke-5634_55013 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 1px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-frame-5634_55014 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
}
.Pixso-paragraph-5634_55015 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5634_55016 {
    width: 60px;
    height: 24px;
}
.Pixso-instance-5634_55017 {
    width: 20px;
    height: 20px;
}
.Pixso-symbol-5634_55018 {
    width: 100%;
    height: 100%;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 12px 24px 12px 24px;
    min-height: 72px;
}
.stroke-wrapper-5634_55018 {
    position: relative;
    width: auto;
    height: auto;
    display: flex;
}
.stroke-5634_55018 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 1px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_55019 {
    width: 48px;
    height: 24px;
}
.Pixso-instance-5634_55020 {
    width: 20px;
    height: 20px;
}
.Pixso-symbol-5634_55021 {
    width: 100%;
    height: 100%;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 12px 24px 12px 24px;
    min-height: 72px;
}
.stroke-wrapper-5634_55021 {
    position: relative;
    width: auto;
    height: auto;
    display: flex;
}
.stroke-5634_55021 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 1px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-frame-5634_55022 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
}
.Pixso-instance-5634_55023 {
    width: 48px;
    height: 24px;
}
.Pixso-instance-5634_55024 {
    width: 48px;
    height: 24px;
}
.Pixso-instance-5634_55025 {
    width: 48px;
    height: 24px;
}
.Pixso-instance-5634_55026 {
    width: 20px;
    height: 20px;
}
.Pixso-symbol-5634_55525 {
    width: 100%;
    height: 100%;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 12px 24px 12px 24px;
    min-height: 72px;
}
.stroke-wrapper-5634_55525 {
    position: relative;
    width: 343px;
    height: auto;
    display: flex;
}
.stroke-5634_55525 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 1px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_55906 {
    width: 20px;
    height: 20px;
}
.Pixso-frame-5634_55526 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: flex-start;
    flex-grow: 1;
    flex-basis: 0;
}
.frame-content-5634_55526 {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: center;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5634_55527 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-paragraph-5634_55528 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5634_55529 {
    width: 20px;
    height: 20px;
}
.Pixso-symbol-5634_57284 {
    width: 100%;
    height: 100%;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 12px 24px 12px 24px;
    min-height: 72px;
}
.stroke-wrapper-5634_57284 {
    position: relative;
    width: 343px;
    height: auto;
    display: flex;
}
.stroke-5634_57284 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 1px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_57285 {
    width: 20px;
    height: 20px;
}
.Pixso-frame-5634_57286 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: flex-start;
    flex-grow: 1;
    flex-basis: 0;
}
.frame-content-5634_57286 {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: center;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5634_57287 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-paragraph-5634_57288 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5634_57289 {
    width: 20px;
    height: 20px;
}
.Pixso-symbol-5634_58255 {
    width: 100%;
    height: 100%;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 12px 24px 12px 24px;
    min-height: 72px;
}
.stroke-wrapper-5634_58255 {
    position: relative;
    width: 343px;
    height: auto;
    display: flex;
}
.stroke-5634_58255 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 1px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_58256 {
    width: 44px;
    height: 24px;
}
.Pixso-frame-5634_58257 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: flex-start;
    flex-grow: 1;
    flex-basis: 0;
}
.frame-content-5634_58257 {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: center;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5634_58258 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-paragraph-5634_58259 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5634_58260 {
    width: 20px;
    height: 20px;
}
.Pixso-symbol-5634_57676 {
    width: 100%;
    height: 100%;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 12px 24px 12px 24px;
    min-height: 72px;
}
.stroke-wrapper-5634_57676 {
    position: relative;
    width: 343px;
    height: auto;
    display: flex;
}
.stroke-5634_57676 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 1px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_57677 {
    width: 20px;
    height: 20px;
}
.Pixso-frame-5634_57678 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: flex-start;
    flex-grow: 1;
    flex-basis: 0;
}
.frame-content-5634_57678 {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: center;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5634_57679 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-paragraph-5634_57680 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5634_57681 {
    width: 20px;
    height: 20px;
}
.Pixso-symbol-5634_58261 {
    width: 100%;
    height: 100%;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 12px 24px 12px 24px;
    min-height: 72px;
}
.stroke-wrapper-5634_58261 {
    position: relative;
    width: 343px;
    height: auto;
    display: flex;
}
.stroke-5634_58261 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 1px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_58262 {
    width: 44px;
    height: 24px;
}
.Pixso-frame-5634_58263 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: flex-start;
    flex-grow: 1;
    flex-basis: 0;
}
.frame-content-5634_58263 {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: center;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5634_58264 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-paragraph-5634_58265 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5634_58266 {
    width: 20px;
    height: 20px;
}
.Pixso-symbol-5634_55530 {
    width: 100%;
    height: 100%;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 12px 24px 12px 24px;
    min-height: 72px;
}
.stroke-wrapper-5634_55530 {
    position: relative;
    width: 343px;
    height: auto;
    display: flex;
}
.stroke-5634_55530 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 1px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_55907 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5634_55531 {
    width: 40px;
    height: 40px;
}
.Pixso-frame-5634_55532 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: flex-start;
    flex-grow: 1;
    flex-basis: 0;
}
.frame-content-5634_55532 {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: center;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5634_55533 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-paragraph-5634_55534 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5634_55535 {
    width: 20px;
    height: 20px;
}
.Pixso-symbol-5634_56108 {
    width: 100%;
    height: 100%;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 12px 24px 12px 24px;
    min-height: 72px;
}
.stroke-wrapper-5634_56108 {
    position: relative;
    width: 343px;
    height: auto;
    display: flex;
}
.stroke-5634_56108 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 1px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_56109 {
    width: 20px;
    height: 20px;
}
.Pixso-frame-5634_56110 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: flex-start;
    flex-grow: 1;
    flex-basis: 0;
}
.frame-content-5634_56110 {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: center;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5634_56111 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-paragraph-5634_56112 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5634_56113 {
    width: 20px;
    height: 20px;
}
.Pixso-symbol-5634_57290 {
    width: 100%;
    height: 100%;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 12px 24px 12px 24px;
    min-height: 72px;
}
.stroke-wrapper-5634_57290 {
    position: relative;
    width: 343px;
    height: auto;
    display: flex;
}
.stroke-5634_57290 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 1px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_57291 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5634_57292 {
    width: 40px;
    height: 40px;
}
.Pixso-frame-5634_57293 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: flex-start;
    flex-grow: 1;
    flex-basis: 0;
}
.frame-content-5634_57293 {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: center;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5634_57294 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-paragraph-5634_57295 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5634_57296 {
    width: 20px;
    height: 20px;
}
.Pixso-symbol-5634_58267 {
    width: 100%;
    height: 100%;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 12px 24px 12px 24px;
    min-height: 72px;
}
.stroke-wrapper-5634_58267 {
    position: relative;
    width: 343px;
    height: auto;
    display: flex;
}
.stroke-5634_58267 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 1px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_58268 {
    width: 44px;
    height: 24px;
}
.Pixso-instance-5634_58269 {
    width: 40px;
    height: 40px;
}
.Pixso-frame-5634_58270 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: flex-start;
    flex-grow: 1;
    flex-basis: 0;
}
.frame-content-5634_58270 {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: center;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5634_58271 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-paragraph-5634_58272 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5634_58273 {
    width: 20px;
    height: 20px;
}
.Pixso-symbol-5634_55536 {
    width: 100%;
    height: 100%;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 12px 24px 12px 24px;
    min-height: 72px;
}
.stroke-wrapper-5634_55536 {
    position: relative;
    width: 343px;
    height: auto;
    display: flex;
}
.stroke-5634_55536 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 1px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_55908 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5634_55537 {
    width: 40px;
    height: 40px;
}
.Pixso-frame-5634_55538 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: flex-start;
    flex-grow: 1;
    flex-basis: 0;
}
.frame-content-5634_55538 {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: center;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5634_55539 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-paragraph-5634_55540 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5634_55541 {
    width: 20px;
    height: 20px;
}
.Pixso-symbol-5634_57682 {
    width: 100%;
    height: 100%;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 12px 24px 12px 24px;
    min-height: 72px;
}
.stroke-wrapper-5634_57682 {
    position: relative;
    width: 343px;
    height: auto;
    display: flex;
}
.stroke-5634_57682 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 1px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_57683 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5634_57684 {
    width: 40px;
    height: 40px;
}
.Pixso-frame-5634_57685 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: flex-start;
    flex-grow: 1;
    flex-basis: 0;
}
.frame-content-5634_57685 {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: center;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5634_57686 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-paragraph-5634_57687 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5634_57688 {
    width: 20px;
    height: 20px;
}
.Pixso-symbol-5634_58274 {
    width: 100%;
    height: 100%;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 12px 24px 12px 24px;
    min-height: 72px;
}
.stroke-wrapper-5634_58274 {
    position: relative;
    width: 343px;
    height: auto;
    display: flex;
}
.stroke-5634_58274 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 1px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_58275 {
    width: 44px;
    height: 24px;
}
.Pixso-instance-5634_58276 {
    width: 40px;
    height: 40px;
}
.Pixso-frame-5634_58277 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: flex-start;
    flex-grow: 1;
    flex-basis: 0;
}
.frame-content-5634_58277 {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: center;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5634_58278 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-paragraph-5634_58279 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5634_58280 {
    width: 20px;
    height: 20px;
}
.Pixso-symbol-5634_55542 {
    width: 100%;
    height: 100%;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 12px 24px 12px 24px;
    min-height: 72px;
}
.stroke-wrapper-5634_55542 {
    position: relative;
    width: 343px;
    height: auto;
    display: flex;
}
.stroke-5634_55542 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 1px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_55909 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5634_55543 {
    width: 36px;
    height: 24px;
}
.Pixso-frame-5634_55544 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: flex-start;
    flex-grow: 1;
    flex-basis: 0;
}
.frame-content-5634_55544 {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: center;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5634_55545 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-paragraph-5634_55546 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5634_55547 {
    width: 20px;
    height: 20px;
}
.Pixso-symbol-5634_57297 {
    width: 100%;
    height: 100%;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 12px 24px 12px 24px;
    min-height: 72px;
}
.stroke-wrapper-5634_57297 {
    position: relative;
    width: 343px;
    height: auto;
    display: flex;
}
.stroke-5634_57297 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 1px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_57298 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5634_57299 {
    width: 40px;
    height: 40px;
}
.Pixso-frame-5634_57300 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: flex-start;
    flex-grow: 1;
    flex-basis: 0;
}
.frame-content-5634_57300 {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: center;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5634_57301 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-paragraph-5634_57302 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5634_57303 {
    width: 20px;
    height: 20px;
}
.Pixso-symbol-5634_58281 {
    width: 100%;
    height: 100%;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 12px 24px 12px 24px;
    min-height: 72px;
}
.stroke-wrapper-5634_58281 {
    position: relative;
    width: 343px;
    height: auto;
    display: flex;
}
.stroke-5634_58281 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 1px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_58282 {
    width: 44px;
    height: 24px;
}
.Pixso-instance-5634_58283 {
    width: 40px;
    height: 40px;
}
.Pixso-frame-5634_58284 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: flex-start;
    flex-grow: 1;
    flex-basis: 0;
}
.frame-content-5634_58284 {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: center;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5634_58285 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-paragraph-5634_58286 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5634_58287 {
    width: 20px;
    height: 20px;
}
.Pixso-symbol-5634_56114 {
    width: 100%;
    height: 100%;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 12px 24px 12px 24px;
    min-height: 72px;
}
.stroke-wrapper-5634_56114 {
    position: relative;
    width: 343px;
    height: auto;
    display: flex;
}
.stroke-5634_56114 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 1px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_56115 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5634_56116 {
    width: 40px;
    height: 40px;
}
.Pixso-frame-5634_56117 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: flex-start;
    flex-grow: 1;
    flex-basis: 0;
}
.frame-content-5634_56117 {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: center;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5634_56118 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-paragraph-5634_56119 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5634_56120 {
    width: 20px;
    height: 20px;
}
.Pixso-symbol-5634_55548 {
    width: 100%;
    height: 100%;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 12px 24px 12px 24px;
    min-height: 72px;
}
.stroke-wrapper-5634_55548 {
    position: relative;
    width: 343px;
    height: auto;
    display: flex;
}
.stroke-5634_55548 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 1px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_55910 {
    width: 20px;
    height: 20px;
}
.Pixso-frame-5634_55549 {
    width: 40px;
    height: 40px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    border-radius: 12px 12px 12px 12px;
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-image: url(@/assets/images/fd6c3c9d619f8227fa8fac58deaaeef02777ba71.png);
}
.Pixso-frame-5634_55550 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: flex-start;
    flex-grow: 1;
    flex-basis: 0;
}
.frame-content-5634_55550 {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: center;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5634_55551 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-paragraph-5634_55552 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5634_55553 {
    width: 20px;
    height: 20px;
}
.Pixso-symbol-5634_57689 {
    width: 100%;
    height: 100%;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 12px 24px 12px 24px;
    min-height: 72px;
}
.stroke-wrapper-5634_57689 {
    position: relative;
    width: 343px;
    height: auto;
    display: flex;
}
.stroke-5634_57689 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 1px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_57690 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5634_57691 {
    width: 40px;
    height: 40px;
}
.Pixso-frame-5634_57692 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: flex-start;
    flex-grow: 1;
    flex-basis: 0;
}
.frame-content-5634_57692 {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: center;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5634_57693 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-paragraph-5634_57694 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5634_57695 {
    width: 20px;
    height: 20px;
}
.Pixso-symbol-5634_58288 {
    width: 100%;
    height: 100%;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 12px 24px 12px 24px;
    min-height: 72px;
}
.stroke-wrapper-5634_58288 {
    position: relative;
    width: 343px;
    height: auto;
    display: flex;
}
.stroke-5634_58288 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 1px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_58289 {
    width: 44px;
    height: 24px;
}
.Pixso-instance-5634_58290 {
    width: 40px;
    height: 40px;
}
.Pixso-frame-5634_58291 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: flex-start;
    flex-grow: 1;
    flex-basis: 0;
}
.frame-content-5634_58291 {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: center;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5634_58292 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-paragraph-5634_58293 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5634_58294 {
    width: 20px;
    height: 20px;
}
.Pixso-symbol-5634_57304 {
    width: 100%;
    height: 100%;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 12px 24px 12px 24px;
    min-height: 72px;
}
.stroke-wrapper-5634_57304 {
    position: relative;
    width: 343px;
    height: auto;
    display: flex;
}
.stroke-5634_57304 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 1px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_57305 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5634_57306 {
    width: 36px;
    height: 24px;
}
.Pixso-frame-5634_57307 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: flex-start;
    flex-grow: 1;
    flex-basis: 0;
}
.frame-content-5634_57307 {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: center;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5634_57308 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-paragraph-5634_57309 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5634_57310 {
    width: 20px;
    height: 20px;
}
.Pixso-symbol-5634_58295 {
    width: 100%;
    height: 100%;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 12px 24px 12px 24px;
    min-height: 72px;
}
.stroke-wrapper-5634_58295 {
    position: relative;
    width: 343px;
    height: auto;
    display: flex;
}
.stroke-5634_58295 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 1px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_58296 {
    width: 44px;
    height: 24px;
}
.Pixso-instance-5634_58297 {
    width: 36px;
    height: 24px;
}
.Pixso-frame-5634_58298 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: flex-start;
    flex-grow: 1;
    flex-basis: 0;
}
.frame-content-5634_58298 {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: center;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5634_58299 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-paragraph-5634_58300 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5634_58301 {
    width: 20px;
    height: 20px;
}
.Pixso-symbol-5634_55554 {
    width: 100%;
    height: 100%;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 12px 24px 12px 24px;
    min-height: 72px;
}
.stroke-wrapper-5634_55554 {
    position: relative;
    width: 343px;
    height: auto;
    display: flex;
}
.stroke-5634_55554 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 1px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_55911 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5634_55555 {
    width: 32px;
    height: 32px;
}
.Pixso-frame-5634_55556 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: flex-start;
    flex-grow: 1;
    flex-basis: 0;
}
.frame-content-5634_55556 {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: center;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5634_55557 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-paragraph-5634_55558 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5634_55559 {
    width: 20px;
    height: 20px;
}
.Pixso-symbol-5634_56121 {
    width: 100%;
    height: 100%;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 12px 24px 12px 24px;
    min-height: 72px;
}
.stroke-wrapper-5634_56121 {
    position: relative;
    width: 343px;
    height: auto;
    display: flex;
}
.stroke-5634_56121 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 1px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_56122 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5634_56123 {
    width: 40px;
    height: 40px;
}
.Pixso-frame-5634_56124 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: flex-start;
    flex-grow: 1;
    flex-basis: 0;
}
.frame-content-5634_56124 {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: center;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5634_56125 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-paragraph-5634_56126 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5634_56127 {
    width: 20px;
    height: 20px;
}
.Pixso-symbol-5634_55560 {
    width: 100%;
    height: 100%;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 12px 24px 12px 24px;
    min-height: 72px;
}
.stroke-wrapper-5634_55560 {
    position: relative;
    width: 343px;
    height: auto;
    display: flex;
}
.stroke-5634_55560 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 1px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_55912 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5634_55561 {
    width: 231px;
    height: 20px;
}
.Pixso-instance-5634_55562 {
    width: 20px;
    height: 20px;
}
.Pixso-symbol-5634_57311 {
    width: 100%;
    height: 100%;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 12px 24px 12px 24px;
    min-height: 72px;
}
.stroke-wrapper-5634_57311 {
    position: relative;
    width: 343px;
    height: auto;
    display: flex;
}
.stroke-5634_57311 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 1px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_57312 {
    width: 20px;
    height: 20px;
}
.Pixso-frame-5634_57313 {
    width: 40px;
    height: 40px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    border-radius: 12px 12px 12px 12px;
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-image: url(@/assets/images/fd6c3c9d619f8227fa8fac58deaaeef02777ba71.png);
}
.Pixso-frame-5634_57314 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: flex-start;
    flex-grow: 1;
    flex-basis: 0;
}
.frame-content-5634_57314 {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: center;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5634_57315 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-paragraph-5634_57316 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5634_57317 {
    width: 20px;
    height: 20px;
}
.Pixso-symbol-5634_58302 {
    width: 100%;
    height: 100%;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 12px 24px 12px 24px;
    min-height: 72px;
}
.stroke-wrapper-5634_58302 {
    position: relative;
    width: 343px;
    height: auto;
    display: flex;
}
.stroke-5634_58302 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 1px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_58303 {
    width: 44px;
    height: 24px;
}
.Pixso-frame-5634_58304 {
    width: 40px;
    height: 40px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    border-radius: 12px 12px 12px 12px;
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-image: url(@/assets/images/fd6c3c9d619f8227fa8fac58deaaeef02777ba71.png);
}
.Pixso-frame-5634_58305 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: flex-start;
    flex-grow: 1;
    flex-basis: 0;
}
.frame-content-5634_58305 {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: center;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5634_58306 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-paragraph-5634_58307 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5634_58308 {
    width: 20px;
    height: 20px;
}
.Pixso-symbol-5634_57696 {
    width: 100%;
    height: 100%;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 12px 24px 12px 24px;
    min-height: 72px;
}
.stroke-wrapper-5634_57696 {
    position: relative;
    width: 343px;
    height: auto;
    display: flex;
}
.stroke-5634_57696 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 1px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_57697 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5634_57698 {
    width: 36px;
    height: 24px;
}
.Pixso-frame-5634_57699 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: flex-start;
    flex-grow: 1;
    flex-basis: 0;
}
.frame-content-5634_57699 {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: center;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5634_57700 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-paragraph-5634_57701 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5634_57702 {
    width: 20px;
    height: 20px;
}
.Pixso-symbol-5634_58309 {
    width: 100%;
    height: 100%;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 12px 24px 12px 24px;
    min-height: 72px;
}
.stroke-wrapper-5634_58309 {
    position: relative;
    width: 343px;
    height: auto;
    display: flex;
}
.stroke-5634_58309 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 1px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_58310 {
    width: 44px;
    height: 24px;
}
.Pixso-instance-5634_58311 {
    width: 36px;
    height: 24px;
}
.Pixso-frame-5634_58312 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: flex-start;
    flex-grow: 1;
    flex-basis: 0;
}
.frame-content-5634_58312 {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: center;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5634_58313 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-paragraph-5634_58314 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5634_58315 {
    width: 20px;
    height: 20px;
}
.Pixso-symbol-5634_55563 {
    width: 100%;
    height: 100%;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 12px 24px 12px 24px;
    min-height: 72px;
}
.stroke-wrapper-5634_55563 {
    position: relative;
    width: 343px;
    height: auto;
    display: flex;
}
.stroke-5634_55563 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 1px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_55913 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5634_55564 {
    width: 231px;
    height: 48px;
}
.Pixso-instance-5634_55565 {
    width: 20px;
    height: 20px;
}
.Pixso-symbol-5634_56128 {
    width: 100%;
    height: 100%;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 12px 24px 12px 24px;
    min-height: 72px;
}
.stroke-wrapper-5634_56128 {
    position: relative;
    width: 343px;
    height: auto;
    display: flex;
}
.stroke-5634_56128 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 1px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_56129 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5634_56130 {
    width: 36px;
    height: 24px;
}
.Pixso-frame-5634_56131 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: flex-start;
    flex-grow: 1;
    flex-basis: 0;
}
.frame-content-5634_56131 {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: center;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5634_56132 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-paragraph-5634_56133 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5634_56134 {
    width: 20px;
    height: 20px;
}
.Pixso-symbol-5634_57318 {
    width: 100%;
    height: 100%;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 12px 24px 12px 24px;
    min-height: 72px;
}
.stroke-wrapper-5634_57318 {
    position: relative;
    width: 343px;
    height: auto;
    display: flex;
}
.stroke-5634_57318 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 1px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_57319 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5634_57320 {
    width: 32px;
    height: 32px;
}
.Pixso-frame-5634_57321 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: flex-start;
    flex-grow: 1;
    flex-basis: 0;
}
.frame-content-5634_57321 {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: center;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5634_57322 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-paragraph-5634_57323 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5634_57324 {
    width: 20px;
    height: 20px;
}
.Pixso-symbol-5634_58316 {
    width: 100%;
    height: 100%;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 12px 24px 12px 24px;
    min-height: 72px;
}
.stroke-wrapper-5634_58316 {
    position: relative;
    width: 343px;
    height: auto;
    display: flex;
}
.stroke-5634_58316 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 1px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_58317 {
    width: 44px;
    height: 24px;
}
.Pixso-instance-5634_58318 {
    width: 32px;
    height: 32px;
}
.Pixso-frame-5634_58319 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: flex-start;
    flex-grow: 1;
    flex-basis: 0;
}
.frame-content-5634_58319 {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: center;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5634_58320 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-paragraph-5634_58321 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5634_58322 {
    width: 20px;
    height: 20px;
}
.Pixso-symbol-5634_55566 {
    width: 100%;
    height: 100%;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 12px 24px 12px 24px;
    min-height: 72px;
}
.stroke-wrapper-5634_55566 {
    position: relative;
    width: auto;
    height: auto;
    display: flex;
}
.stroke-5634_55566 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 1px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_55914 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5634_55567 {
    width: 200px;
    height: 32px;
}
.Pixso-instance-5634_55568 {
    width: 20px;
    height: 20px;
}
.Pixso-symbol-5634_57703 {
    width: 100%;
    height: 100%;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 12px 24px 12px 24px;
    min-height: 72px;
}
.stroke-wrapper-5634_57703 {
    position: relative;
    width: 343px;
    height: auto;
    display: flex;
}
.stroke-5634_57703 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 1px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_57704 {
    width: 20px;
    height: 20px;
}
.Pixso-frame-5634_57705 {
    width: 40px;
    height: 40px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    border-radius: 12px 12px 12px 12px;
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-image: url(@/assets/images/fd6c3c9d619f8227fa8fac58deaaeef02777ba71.png);
}
.Pixso-frame-5634_57706 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: flex-start;
    flex-grow: 1;
    flex-basis: 0;
}
.frame-content-5634_57706 {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: center;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5634_57707 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-paragraph-5634_57708 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5634_57709 {
    width: 20px;
    height: 20px;
}
.Pixso-symbol-5634_58323 {
    width: 100%;
    height: 100%;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 12px 24px 12px 24px;
    min-height: 72px;
}
.stroke-wrapper-5634_58323 {
    position: relative;
    width: 343px;
    height: auto;
    display: flex;
}
.stroke-5634_58323 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 1px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_58324 {
    width: 44px;
    height: 24px;
}
.Pixso-frame-5634_58325 {
    width: 40px;
    height: 40px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    border-radius: 12px 12px 12px 12px;
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-image: url(@/assets/images/fd6c3c9d619f8227fa8fac58deaaeef02777ba71.png);
}
.Pixso-frame-5634_58326 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: flex-start;
    flex-grow: 1;
    flex-basis: 0;
}
.frame-content-5634_58326 {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: center;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5634_58327 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-paragraph-5634_58328 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5634_58329 {
    width: 20px;
    height: 20px;
}
.Pixso-symbol-5634_55569 {
    width: 100%;
    height: 100%;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
    padding: 12px 24px 12px 24px;
    min-height: 72px;
}
.stroke-wrapper-5634_55569 {
    position: relative;
    width: auto;
    height: auto;
    display: flex;
}
.stroke-5634_55569 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 1px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_55915 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5634_55570 {
    width: 40px;
    height: 40px;
}
.Pixso-instance-5634_55571 {
    width: 40px;
    height: 40px;
}
.Pixso-instance-5634_55572 {
    width: 40px;
    height: 40px;
}
.Pixso-symbol-5634_57325 {
    width: 100%;
    height: 100%;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 12px 24px 12px 24px;
    min-height: 72px;
}
.stroke-wrapper-5634_57325 {
    position: relative;
    width: 343px;
    height: auto;
    display: flex;
}
.stroke-5634_57325 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 1px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_57326 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5634_57327 {
    width: 231px;
    height: 20px;
}
.Pixso-instance-5634_57328 {
    width: 20px;
    height: 20px;
}
.Pixso-symbol-5634_58330 {
    width: 100%;
    height: 100%;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 12px 24px 12px 24px;
    min-height: 72px;
}
.stroke-wrapper-5634_58330 {
    position: relative;
    width: 343px;
    height: auto;
    display: flex;
}
.stroke-5634_58330 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 1px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_58331 {
    width: 44px;
    height: 24px;
}
.Pixso-instance-5634_58332 {
    width: 207px;
    height: 20px;
}
.Pixso-instance-5634_58333 {
    width: 20px;
    height: 20px;
}
.Pixso-symbol-5634_56135 {
    width: 100%;
    height: 100%;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 12px 24px 12px 24px;
    min-height: 72px;
}
.stroke-wrapper-5634_56135 {
    position: relative;
    width: 343px;
    height: auto;
    display: flex;
}
.stroke-5634_56135 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 1px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_56136 {
    width: 20px;
    height: 20px;
}
.Pixso-frame-5634_56137 {
    width: 40px;
    height: 40px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    border-radius: 12px 12px 12px 12px;
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-image: url(@/assets/images/fd6c3c9d619f8227fa8fac58deaaeef02777ba71.png);
}
.Pixso-frame-5634_56138 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: flex-start;
    flex-grow: 1;
    flex-basis: 0;
}
.frame-content-5634_56138 {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: center;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5634_56139 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-paragraph-5634_56140 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5634_56141 {
    width: 20px;
    height: 20px;
}
.Pixso-symbol-5634_55573 {
    width: 100%;
    height: 100%;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 12px 24px 12px 24px;
    min-height: 72px;
}
.stroke-wrapper-5634_55573 {
    position: relative;
    width: auto;
    height: auto;
    display: flex;
}
.stroke-5634_55573 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 1px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_55916 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5634_55574 {
    width: 45px;
    height: 20px;
}
.Pixso-instance-5634_55575 {
    width: 27px;
    height: 20px;
}
.Pixso-symbol-5634_57710 {
    width: 100%;
    height: 100%;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 12px 24px 12px 24px;
    min-height: 72px;
}
.stroke-wrapper-5634_57710 {
    position: relative;
    width: 343px;
    height: auto;
    display: flex;
}
.stroke-5634_57710 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 1px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_57711 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5634_57712 {
    width: 32px;
    height: 32px;
}
.Pixso-frame-5634_57713 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: flex-start;
    flex-grow: 1;
    flex-basis: 0;
}
.frame-content-5634_57713 {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: center;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5634_57714 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-paragraph-5634_57715 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5634_57716 {
    width: 20px;
    height: 20px;
}
.Pixso-symbol-5634_58334 {
    width: 100%;
    height: 100%;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 12px 24px 12px 24px;
    min-height: 72px;
}
.stroke-wrapper-5634_58334 {
    position: relative;
    width: 343px;
    height: auto;
    display: flex;
}
.stroke-5634_58334 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 1px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_58335 {
    width: 44px;
    height: 24px;
}
.Pixso-instance-5634_58336 {
    width: 32px;
    height: 32px;
}
.Pixso-frame-5634_58337 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: flex-start;
    flex-grow: 1;
    flex-basis: 0;
}
.frame-content-5634_58337 {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: center;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5634_58338 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-paragraph-5634_58339 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5634_58340 {
    width: 20px;
    height: 20px;
}
.Pixso-symbol-5634_57329 {
    width: 100%;
    height: 100%;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 12px 24px 12px 24px;
    min-height: 72px;
}
.stroke-wrapper-5634_57329 {
    position: relative;
    width: 343px;
    height: auto;
    display: flex;
}
.stroke-5634_57329 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 1px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_57330 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5634_57331 {
    width: 231px;
    height: 48px;
}
.Pixso-instance-5634_57332 {
    width: 20px;
    height: 20px;
}
.Pixso-symbol-5634_58341 {
    width: 100%;
    height: 100%;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 12px 24px 12px 24px;
    min-height: 72px;
}
.stroke-wrapper-5634_58341 {
    position: relative;
    width: 343px;
    height: auto;
    display: flex;
}
.stroke-5634_58341 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 1px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_58342 {
    width: 44px;
    height: 24px;
}
.Pixso-instance-5634_58343 {
    width: 207px;
    height: 48px;
}
.Pixso-instance-5634_58344 {
    width: 20px;
    height: 20px;
}
.Pixso-symbol-5634_55576 {
    width: 100%;
    height: 100%;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 12px 24px 12px 24px;
    min-height: 72px;
}
.stroke-wrapper-5634_55576 {
    position: relative;
    width: auto;
    height: auto;
    display: flex;
}
.stroke-5634_55576 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 1px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_55917 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5634_55577 {
    width: 152px;
    height: 24px;
}
.Pixso-paragraph-5634_55578 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-symbol-5634_57333 {
    width: 100%;
    height: 100%;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 12px 24px 12px 24px;
    min-height: 72px;
}
.stroke-wrapper-5634_57333 {
    position: relative;
    width: auto;
    height: auto;
    display: flex;
}
.stroke-5634_57333 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 1px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_57334 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5634_57335 {
    width: 200px;
    height: 32px;
}
.Pixso-instance-5634_57336 {
    width: 20px;
    height: 20px;
}
.Pixso-symbol-5634_58345 {
    width: 100%;
    height: 100%;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 12px 24px 12px 24px;
    min-height: 72px;
}
.stroke-wrapper-5634_58345 {
    position: relative;
    width: auto;
    height: auto;
    display: flex;
}
.stroke-5634_58345 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 1px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_58346 {
    width: 44px;
    height: 24px;
}
.Pixso-instance-5634_58347 {
    width: 200px;
    height: 32px;
}
.Pixso-instance-5634_58348 {
    width: 20px;
    height: 20px;
}
.Pixso-symbol-5634_56142 {
    width: 100%;
    height: 100%;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 12px 24px 12px 24px;
    min-height: 72px;
}
.stroke-wrapper-5634_56142 {
    position: relative;
    width: 343px;
    height: auto;
    display: flex;
}
.stroke-5634_56142 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 1px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_56143 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5634_56144 {
    width: 32px;
    height: 32px;
}
.Pixso-frame-5634_56145 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: flex-start;
    flex-grow: 1;
    flex-basis: 0;
}
.frame-content-5634_56145 {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: center;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5634_56146 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-paragraph-5634_56147 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5634_56148 {
    width: 20px;
    height: 20px;
}
.Pixso-symbol-5634_57337 {
    width: 100%;
    height: 100%;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
    padding: 12px 24px 12px 24px;
    min-height: 72px;
}
.stroke-wrapper-5634_57337 {
    position: relative;
    width: auto;
    height: auto;
    display: flex;
}
.stroke-5634_57337 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 1px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_57338 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5634_57339 {
    width: 40px;
    height: 40px;
}
.Pixso-instance-5634_57340 {
    width: 40px;
    height: 40px;
}
.Pixso-instance-5634_57341 {
    width: 40px;
    height: 40px;
}
.Pixso-symbol-5634_58349 {
    width: 100%;
    height: 100%;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
    padding: 12px 24px 12px 24px;
    min-height: 72px;
}
.stroke-wrapper-5634_58349 {
    position: relative;
    width: auto;
    height: auto;
    display: flex;
}
.stroke-5634_58349 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 1px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_58350 {
    width: 44px;
    height: 24px;
}
.Pixso-instance-5634_58351 {
    width: 40px;
    height: 40px;
}
.Pixso-instance-5634_58352 {
    width: 40px;
    height: 40px;
}
.Pixso-instance-5634_58353 {
    width: 40px;
    height: 40px;
}
.Pixso-symbol-5634_55579 {
    width: 100%;
    height: 100%;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 12px 24px 12px 24px;
    min-height: 72px;
}
.stroke-wrapper-5634_55579 {
    position: relative;
    width: auto;
    height: auto;
    display: flex;
}
.stroke-5634_55579 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 1px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_55918 {
    width: 20px;
    height: 20px;
}
.Pixso-frame-5634_55580 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
}
.Pixso-paragraph-5634_55581 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5634_55582 {
    width: 60px;
    height: 24px;
}
.Pixso-instance-5634_55583 {
    width: 20px;
    height: 20px;
}
.Pixso-symbol-5634_57342 {
    width: 100%;
    height: 100%;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 12px 24px 12px 24px;
    min-height: 72px;
}
.stroke-wrapper-5634_57342 {
    position: relative;
    width: auto;
    height: auto;
    display: flex;
}
.stroke-5634_57342 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 1px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_57343 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5634_57344 {
    width: 45px;
    height: 20px;
}
.Pixso-instance-5634_57345 {
    width: 27px;
    height: 20px;
}
.Pixso-symbol-5634_58354 {
    width: 100%;
    height: 100%;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 12px 24px 12px 24px;
    min-height: 72px;
}
.stroke-wrapper-5634_58354 {
    position: relative;
    width: auto;
    height: auto;
    display: flex;
}
.stroke-5634_58354 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 1px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_58355 {
    width: 44px;
    height: 24px;
}
.Pixso-instance-5634_58356 {
    width: 45px;
    height: 20px;
}
.Pixso-instance-5634_58357 {
    width: 27px;
    height: 20px;
}
.Pixso-symbol-5634_57717 {
    width: 100%;
    height: 100%;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 12px 24px 12px 24px;
    min-height: 72px;
}
.stroke-wrapper-5634_57717 {
    position: relative;
    width: 343px;
    height: auto;
    display: flex;
}
.stroke-5634_57717 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 1px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_57718 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5634_57719 {
    width: 231px;
    height: 20px;
}
.Pixso-instance-5634_57720 {
    width: 20px;
    height: 20px;
}
.Pixso-symbol-5634_58358 {
    width: 100%;
    height: 100%;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 12px 24px 12px 24px;
    min-height: 72px;
}
.stroke-wrapper-5634_58358 {
    position: relative;
    width: 343px;
    height: auto;
    display: flex;
}
.stroke-5634_58358 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 1px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_58359 {
    width: 44px;
    height: 24px;
}
.Pixso-instance-5634_58360 {
    width: 207px;
    height: 20px;
}
.Pixso-instance-5634_58361 {
    width: 20px;
    height: 20px;
}
.Pixso-symbol-5634_57346 {
    width: 100%;
    height: 100%;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 12px 24px 12px 24px;
    min-height: 72px;
}
.stroke-wrapper-5634_57346 {
    position: relative;
    width: auto;
    height: auto;
    display: flex;
}
.stroke-5634_57346 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 1px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_57347 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5634_57348 {
    width: 152px;
    height: 24px;
}
.Pixso-paragraph-5634_57349 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-symbol-5634_58362 {
    width: 100%;
    height: 100%;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 12px 24px 12px 24px;
    min-height: 72px;
}
.stroke-wrapper-5634_58362 {
    position: relative;
    width: auto;
    height: auto;
    display: flex;
}
.stroke-5634_58362 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 1px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_58363 {
    width: 44px;
    height: 24px;
}
.Pixso-instance-5634_58364 {
    width: 152px;
    height: 24px;
}
.Pixso-paragraph-5634_58365 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-symbol-5634_55584 {
    width: 100%;
    height: 100%;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 12px 24px 12px 24px;
    min-height: 72px;
}
.stroke-wrapper-5634_55584 {
    position: relative;
    width: auto;
    height: auto;
    display: flex;
}
.stroke-5634_55584 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 1px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_55919 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5634_55585 {
    width: 48px;
    height: 24px;
}
.Pixso-instance-5634_55586 {
    width: 20px;
    height: 20px;
}
.Pixso-symbol-5634_57350 {
    width: 100%;
    height: 100%;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 12px 24px 12px 24px;
    min-height: 72px;
}
.stroke-wrapper-5634_57350 {
    position: relative;
    width: auto;
    height: auto;
    display: flex;
}
.stroke-5634_57350 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 1px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_57351 {
    width: 20px;
    height: 20px;
}
.Pixso-frame-5634_57352 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
}
.Pixso-paragraph-5634_57353 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5634_57354 {
    width: 60px;
    height: 24px;
}
.Pixso-instance-5634_57355 {
    width: 20px;
    height: 20px;
}
.Pixso-symbol-5634_58366 {
    width: 100%;
    height: 100%;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 12px 24px 12px 24px;
    min-height: 72px;
}
.stroke-wrapper-5634_58366 {
    position: relative;
    width: auto;
    height: auto;
    display: flex;
}
.stroke-5634_58366 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 1px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_58367 {
    width: 44px;
    height: 24px;
}
.Pixso-frame-5634_58368 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
}
.Pixso-paragraph-5634_58369 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5634_58370 {
    width: 60px;
    height: 24px;
}
.Pixso-instance-5634_58371 {
    width: 20px;
    height: 20px;
}
.Pixso-symbol-5634_56149 {
    width: 100%;
    height: 100%;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 12px 24px 12px 24px;
    min-height: 72px;
}
.stroke-wrapper-5634_56149 {
    position: relative;
    width: 343px;
    height: auto;
    display: flex;
}
.stroke-5634_56149 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 1px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_56150 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5634_56151 {
    width: 231px;
    height: 20px;
}
.Pixso-instance-5634_56152 {
    width: 20px;
    height: 20px;
}
.Pixso-symbol-5634_57356 {
    width: 100%;
    height: 100%;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 12px 24px 12px 24px;
    min-height: 72px;
}
.stroke-wrapper-5634_57356 {
    position: relative;
    width: auto;
    height: auto;
    display: flex;
}
.stroke-5634_57356 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 1px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_57357 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5634_57358 {
    width: 48px;
    height: 24px;
}
.Pixso-instance-5634_57359 {
    width: 20px;
    height: 20px;
}
.Pixso-symbol-5634_58372 {
    width: 100%;
    height: 100%;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 12px 24px 12px 24px;
    min-height: 72px;
}
.stroke-wrapper-5634_58372 {
    position: relative;
    width: auto;
    height: auto;
    display: flex;
}
.stroke-5634_58372 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 1px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_58373 {
    width: 44px;
    height: 24px;
}
.Pixso-instance-5634_58374 {
    width: 48px;
    height: 24px;
}
.Pixso-instance-5634_58375 {
    width: 20px;
    height: 20px;
}
.Pixso-symbol-5634_55587 {
    width: 100%;
    height: 100%;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 12px 24px 12px 24px;
    min-height: 72px;
}
.stroke-wrapper-5634_55587 {
    position: relative;
    width: auto;
    height: auto;
    display: flex;
}
.stroke-5634_55587 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 1px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_55920 {
    width: 20px;
    height: 20px;
}
.Pixso-frame-5634_55588 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
}
.Pixso-instance-5634_55589 {
    width: 48px;
    height: 24px;
}
.Pixso-instance-5634_55590 {
    width: 48px;
    height: 24px;
}
.Pixso-instance-5634_55591 {
    width: 48px;
    height: 24px;
}
.Pixso-instance-5634_55592 {
    width: 20px;
    height: 20px;
}
.Pixso-symbol-5634_57360 {
    width: 100%;
    height: 100%;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 12px 24px 12px 24px;
    min-height: 72px;
}
.stroke-wrapper-5634_57360 {
    position: relative;
    width: auto;
    height: auto;
    display: flex;
}
.stroke-5634_57360 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 1px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_57361 {
    width: 20px;
    height: 20px;
}
.Pixso-frame-5634_57362 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
}
.Pixso-instance-5634_57363 {
    width: 48px;
    height: 24px;
}
.Pixso-instance-5634_57364 {
    width: 48px;
    height: 24px;
}
.Pixso-instance-5634_57365 {
    width: 48px;
    height: 24px;
}
.Pixso-instance-5634_57366 {
    width: 20px;
    height: 20px;
}
.Pixso-symbol-5634_58376 {
    width: 100%;
    height: 100%;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 12px 24px 12px 24px;
    min-height: 72px;
}
.stroke-wrapper-5634_58376 {
    position: relative;
    width: auto;
    height: auto;
    display: flex;
}
.stroke-5634_58376 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 1px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_58377 {
    width: 44px;
    height: 24px;
}
.Pixso-frame-5634_58378 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
}
.Pixso-instance-5634_58379 {
    width: 48px;
    height: 24px;
}
.Pixso-instance-5634_58380 {
    width: 48px;
    height: 24px;
}
.Pixso-instance-5634_58381 {
    width: 48px;
    height: 24px;
}
.Pixso-instance-5634_58382 {
    width: 20px;
    height: 20px;
}
.Pixso-symbol-5634_57721 {
    width: 100%;
    height: 100%;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 12px 24px 12px 24px;
    min-height: 72px;
}
.stroke-wrapper-5634_57721 {
    position: relative;
    width: 343px;
    height: auto;
    display: flex;
}
.stroke-5634_57721 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 1px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_57722 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5634_57723 {
    width: 231px;
    height: 48px;
}
.Pixso-instance-5634_57724 {
    width: 20px;
    height: 20px;
}
.Pixso-symbol-5634_58383 {
    width: 100%;
    height: 100%;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 12px 24px 12px 24px;
    min-height: 72px;
}
.stroke-wrapper-5634_58383 {
    position: relative;
    width: 343px;
    height: auto;
    display: flex;
}
.stroke-5634_58383 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 1px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_58384 {
    width: 44px;
    height: 24px;
}
.Pixso-instance-5634_58385 {
    width: 207px;
    height: 48px;
}
.Pixso-instance-5634_58386 {
    width: 20px;
    height: 20px;
}
.Pixso-symbol-5634_56153 {
    width: 100%;
    height: 100%;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 12px 24px 12px 24px;
    min-height: 72px;
}
.stroke-wrapper-5634_56153 {
    position: relative;
    width: 343px;
    height: auto;
    display: flex;
}
.stroke-5634_56153 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 1px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_56154 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5634_56155 {
    width: 231px;
    height: 48px;
}
.Pixso-instance-5634_56156 {
    width: 20px;
    height: 20px;
}
.Pixso-symbol-5634_57725 {
    width: 100%;
    height: 100%;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 12px 24px 12px 24px;
    min-height: 72px;
}
.stroke-wrapper-5634_57725 {
    position: relative;
    width: auto;
    height: auto;
    display: flex;
}
.stroke-5634_57725 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 1px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_57726 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5634_57727 {
    width: 200px;
    height: 32px;
}
.Pixso-instance-5634_57728 {
    width: 20px;
    height: 20px;
}
.Pixso-symbol-5634_58387 {
    width: 100%;
    height: 100%;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 12px 24px 12px 24px;
    min-height: 72px;
}
.stroke-wrapper-5634_58387 {
    position: relative;
    width: auto;
    height: auto;
    display: flex;
}
.stroke-5634_58387 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 1px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_58388 {
    width: 44px;
    height: 24px;
}
.Pixso-instance-5634_58389 {
    width: 200px;
    height: 32px;
}
.Pixso-instance-5634_58390 {
    width: 20px;
    height: 20px;
}
.Pixso-symbol-5634_56157 {
    width: 100%;
    height: 100%;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 12px 24px 12px 24px;
    min-height: 72px;
}
.stroke-wrapper-5634_56157 {
    position: relative;
    width: auto;
    height: auto;
    display: flex;
}
.stroke-5634_56157 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 1px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_56158 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5634_56159 {
    width: 200px;
    height: 32px;
}
.Pixso-instance-5634_56160 {
    width: 20px;
    height: 20px;
}
.Pixso-symbol-5634_57729 {
    width: 100%;
    height: 100%;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
    padding: 12px 24px 12px 24px;
    min-height: 72px;
}
.stroke-wrapper-5634_57729 {
    position: relative;
    width: auto;
    height: auto;
    display: flex;
}
.stroke-5634_57729 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 1px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_57730 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5634_57731 {
    width: 40px;
    height: 40px;
}
.Pixso-instance-5634_57732 {
    width: 40px;
    height: 40px;
}
.Pixso-instance-5634_57733 {
    width: 40px;
    height: 40px;
}
.Pixso-symbol-5634_58391 {
    width: 100%;
    height: 100%;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
    padding: 12px 24px 12px 24px;
    min-height: 72px;
}
.stroke-wrapper-5634_58391 {
    position: relative;
    width: auto;
    height: auto;
    display: flex;
}
.stroke-5634_58391 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 1px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_58392 {
    width: 44px;
    height: 24px;
}
.Pixso-instance-5634_58393 {
    width: 40px;
    height: 40px;
}
.Pixso-instance-5634_58394 {
    width: 40px;
    height: 40px;
}
.Pixso-instance-5634_58395 {
    width: 40px;
    height: 40px;
}
.Pixso-symbol-5634_56161 {
    width: 100%;
    height: 100%;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
    padding: 12px 24px 12px 24px;
    min-height: 72px;
}
.stroke-wrapper-5634_56161 {
    position: relative;
    width: auto;
    height: auto;
    display: flex;
}
.stroke-5634_56161 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 1px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_56162 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5634_56163 {
    width: 40px;
    height: 40px;
}
.Pixso-instance-5634_56164 {
    width: 40px;
    height: 40px;
}
.Pixso-instance-5634_56165 {
    width: 40px;
    height: 40px;
}
.Pixso-symbol-5634_57734 {
    width: 100%;
    height: 100%;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 12px 24px 12px 24px;
    min-height: 72px;
}
.stroke-wrapper-5634_57734 {
    position: relative;
    width: auto;
    height: auto;
    display: flex;
}
.stroke-5634_57734 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 1px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_57735 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5634_57736 {
    width: 45px;
    height: 20px;
}
.Pixso-instance-5634_57737 {
    width: 27px;
    height: 20px;
}
.Pixso-symbol-5634_58396 {
    width: 100%;
    height: 100%;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 12px 24px 12px 24px;
    min-height: 72px;
}
.stroke-wrapper-5634_58396 {
    position: relative;
    width: auto;
    height: auto;
    display: flex;
}
.stroke-5634_58396 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 1px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_58397 {
    width: 44px;
    height: 24px;
}
.Pixso-instance-5634_58398 {
    width: 45px;
    height: 20px;
}
.Pixso-instance-5634_58399 {
    width: 27px;
    height: 20px;
}
.Pixso-symbol-5634_56166 {
    width: 100%;
    height: 100%;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 12px 24px 12px 24px;
    min-height: 72px;
}
.stroke-wrapper-5634_56166 {
    position: relative;
    width: auto;
    height: auto;
    display: flex;
}
.stroke-5634_56166 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 1px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_56167 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5634_56168 {
    width: 45px;
    height: 20px;
}
.Pixso-instance-5634_56169 {
    width: 27px;
    height: 20px;
}
.Pixso-symbol-5634_57738 {
    width: 100%;
    height: 100%;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 12px 24px 12px 24px;
    min-height: 72px;
}
.stroke-wrapper-5634_57738 {
    position: relative;
    width: auto;
    height: auto;
    display: flex;
}
.stroke-5634_57738 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 1px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_57739 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5634_57740 {
    width: 152px;
    height: 24px;
}
.Pixso-paragraph-5634_57741 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-symbol-5634_58400 {
    width: 100%;
    height: 100%;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 12px 24px 12px 24px;
    min-height: 72px;
}
.stroke-wrapper-5634_58400 {
    position: relative;
    width: auto;
    height: auto;
    display: flex;
}
.stroke-5634_58400 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 1px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_58401 {
    width: 44px;
    height: 24px;
}
.Pixso-instance-5634_58402 {
    width: 152px;
    height: 24px;
}
.Pixso-paragraph-5634_58403 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-symbol-5634_56170 {
    width: 100%;
    height: 100%;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 12px 24px 12px 24px;
    min-height: 72px;
}
.stroke-wrapper-5634_56170 {
    position: relative;
    width: auto;
    height: auto;
    display: flex;
}
.stroke-5634_56170 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 1px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_56171 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5634_56172 {
    width: 152px;
    height: 24px;
}
.Pixso-paragraph-5634_56173 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-symbol-5634_57742 {
    width: 100%;
    height: 100%;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 12px 24px 12px 24px;
    min-height: 72px;
}
.stroke-wrapper-5634_57742 {
    position: relative;
    width: auto;
    height: auto;
    display: flex;
}
.stroke-5634_57742 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 1px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_57743 {
    width: 20px;
    height: 20px;
}
.Pixso-frame-5634_57744 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
}
.Pixso-paragraph-5634_57745 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5634_57746 {
    width: 60px;
    height: 24px;
}
.Pixso-instance-5634_57747 {
    width: 20px;
    height: 20px;
}
.Pixso-symbol-5634_58404 {
    width: 100%;
    height: 100%;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 12px 24px 12px 24px;
    min-height: 72px;
}
.stroke-wrapper-5634_58404 {
    position: relative;
    width: auto;
    height: auto;
    display: flex;
}
.stroke-5634_58404 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 1px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_58405 {
    width: 44px;
    height: 24px;
}
.Pixso-frame-5634_58406 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
}
.Pixso-paragraph-5634_58407 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5634_58408 {
    width: 60px;
    height: 24px;
}
.Pixso-instance-5634_58409 {
    width: 20px;
    height: 20px;
}
.Pixso-symbol-5634_56174 {
    width: 100%;
    height: 100%;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 12px 24px 12px 24px;
    min-height: 72px;
}
.stroke-wrapper-5634_56174 {
    position: relative;
    width: auto;
    height: auto;
    display: flex;
}
.stroke-5634_56174 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 1px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_56175 {
    width: 20px;
    height: 20px;
}
.Pixso-frame-5634_56176 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
}
.Pixso-paragraph-5634_56177 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5634_56178 {
    width: 60px;
    height: 24px;
}
.Pixso-instance-5634_56179 {
    width: 20px;
    height: 20px;
}
.Pixso-symbol-5634_57748 {
    width: 100%;
    height: 100%;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 12px 24px 12px 24px;
    min-height: 72px;
}
.stroke-wrapper-5634_57748 {
    position: relative;
    width: auto;
    height: auto;
    display: flex;
}
.stroke-5634_57748 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 1px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_57749 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5634_57750 {
    width: 48px;
    height: 24px;
}
.Pixso-instance-5634_57751 {
    width: 20px;
    height: 20px;
}
.Pixso-symbol-5634_58410 {
    width: 100%;
    height: 100%;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 12px 24px 12px 24px;
    min-height: 72px;
}
.stroke-wrapper-5634_58410 {
    position: relative;
    width: auto;
    height: auto;
    display: flex;
}
.stroke-5634_58410 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 1px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_58411 {
    width: 44px;
    height: 24px;
}
.Pixso-instance-5634_58412 {
    width: 48px;
    height: 24px;
}
.Pixso-instance-5634_58413 {
    width: 20px;
    height: 20px;
}
.Pixso-symbol-5634_56180 {
    width: 100%;
    height: 100%;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 12px 24px 12px 24px;
    min-height: 72px;
}
.stroke-wrapper-5634_56180 {
    position: relative;
    width: auto;
    height: auto;
    display: flex;
}
.stroke-5634_56180 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 1px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_56181 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5634_56182 {
    width: 48px;
    height: 24px;
}
.Pixso-instance-5634_56183 {
    width: 20px;
    height: 20px;
}
.Pixso-symbol-5634_57752 {
    width: 100%;
    height: 100%;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 12px 24px 12px 24px;
    min-height: 72px;
}
.stroke-wrapper-5634_57752 {
    position: relative;
    width: auto;
    height: auto;
    display: flex;
}
.stroke-5634_57752 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 1px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_57753 {
    width: 20px;
    height: 20px;
}
.Pixso-frame-5634_57754 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
}
.Pixso-instance-5634_57755 {
    width: 48px;
    height: 24px;
}
.Pixso-instance-5634_57756 {
    width: 48px;
    height: 24px;
}
.Pixso-instance-5634_57757 {
    width: 48px;
    height: 24px;
}
.Pixso-instance-5634_57758 {
    width: 20px;
    height: 20px;
}
.Pixso-symbol-5634_58414 {
    width: 100%;
    height: 100%;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 12px 24px 12px 24px;
    min-height: 72px;
}
.stroke-wrapper-5634_58414 {
    position: relative;
    width: auto;
    height: auto;
    display: flex;
}
.stroke-5634_58414 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 1px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_58415 {
    width: 44px;
    height: 24px;
}
.Pixso-frame-5634_58416 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
}
.Pixso-instance-5634_58417 {
    width: 48px;
    height: 24px;
}
.Pixso-instance-5634_58418 {
    width: 48px;
    height: 24px;
}
.Pixso-instance-5634_58419 {
    width: 48px;
    height: 24px;
}
.Pixso-instance-5634_58420 {
    width: 20px;
    height: 20px;
}
.Pixso-symbol-5634_56184 {
    width: 100%;
    height: 100%;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 12px 24px 12px 24px;
    min-height: 72px;
}
.stroke-wrapper-5634_56184 {
    position: relative;
    width: auto;
    height: auto;
    display: flex;
}
.stroke-5634_56184 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 1px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_56185 {
    width: 20px;
    height: 20px;
}
.Pixso-frame-5634_56186 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
}
.Pixso-instance-5634_56187 {
    width: 48px;
    height: 24px;
}
.Pixso-instance-5634_56188 {
    width: 48px;
    height: 24px;
}
.Pixso-instance-5634_56189 {
    width: 48px;
    height: 24px;
}
.Pixso-instance-5634_56190 {
    width: 20px;
    height: 20px;
}

.Pixso-instance-5631_53518 .Pixso-symbol-5579_152932 .Pixso-symbol-5578_149309 {
    width: 20px;
    height: 20px;
    position: absolute;
    left: 299px;
    top: 26px;
    background-color: transparent;
}
.Pixso-instance-5631_53518 .Pixso-vector-5579_152933 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5631_53518 .Pixso-symbol-5579_152932 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5631_53453 .Pixso-symbol-5468_1033 {
    width: 40px;
    height: 40px;
    position: relative;
    flex-shrink: 0;
    border-radius: 76.875px 76.875px 76.875px 76.875px;
}
.Pixso-instance-5631_53575 .Pixso-symbol-5579_152932 .Pixso-symbol-5578_150497 {
    width: 20px;
    height: 20px;
    position: absolute;
    left: 299px;
    top: 26px;
    background-color: transparent;
}
.Pixso-instance-5631_53575 .Pixso-vector-5579_152933 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5631_53575 .Pixso-symbol-5579_152932 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5631_53464 .Pixso-symbol-5546_2916 {
    width: 40px;
    height: 40px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 10px;
    justify-content: center;
    align-items: center;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5631_53464 .Pixso-instance-5546_2917 .Pixso-vector-5579_151560 {
    width: 67.7%;
    height: 70.31%;
    background-image: url(@/assets/images/Vector317.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 3.91%;
    right: 28.39%;
    top: 6.51%;
    bottom: 23.18%;
}
.Pixso-instance-5546_2917 .Pixso-vector-5579_151560 {
    width: 67.7%;
    height: 70.31%;
    position: absolute;
    left: 3.91%;
    right: 28.39%;
    top: 6.51%;
    bottom: 23.18%;
}
.Pixso-instance-5631_53577 .Pixso-symbol-5579_152932 .Pixso-symbol-5578_150188 {
    width: 20px;
    height: 20px;
    position: absolute;
    left: 299px;
    top: 26px;
    background-color: transparent;
}
.Pixso-instance-5631_53577 .Pixso-vector-5579_152933 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5631_53577 .Pixso-symbol-5579_152932 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5633_54620 .Pixso-symbol-5566_5797 {
    width: 36px;
    height: 24px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5633_54616 .Pixso-symbol-5579_152932 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5633_54616 .Pixso-vector-5579_152933 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5631_53579 .Pixso-symbol-5579_152932 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5631_53579 .Pixso-vector-5579_152933 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5631_53501 .Pixso-symbol-5461_33741 {
    width: 32px;
    height: 32px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5631_53581 .Pixso-symbol-5579_152932 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5631_53581 .Pixso-vector-5579_152933 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5631_53816 .Pixso-symbol-5631_54071 {
    width: 263px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
}
.Pixso-instance-5631_53816 .Pixso-instance-5631_54072 {
    width: 274px;
    height: 12px;
}
.Pixso-instance-5631_53816 .Pixso-paragraph-5631_54073 {
    text-align: right;
    display: flex;
    flex-direction: column;
    justify-content: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5631_53816
    .Pixso-instance-5631_54072
    .Pixso-instance-5615_9016 {
    width: 320px;
    height: 12px;
}
.Pixso-instance-5631_53816 .Pixso-instance-5631_54072 .Pixso-frame-5615_9015 {
    width: 100%;
    height: 12px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5631_53816
    .Pixso-instance-5631_54072
    .Pixso-instance-5615_9017 {
    width: 128px;
    height: 12px;
}
.Pixso-instance-5631_54072 .Pixso-symbol-5615_9014 {
    width: 274px;
    height: 12px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    gap: 10px;
    align-items: flex-start;
    border-radius: 8px 8px 8px 8px;
    background-color: transparent;
}
.Pixso-instance-5631_54072 .Pixso-frame-5615_9015 {
    width: 100%;
    height: 12px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5631_54072 .Pixso-instance-5615_9016 {
    width: 320px;
    height: 12px;
}
.Pixso-instance-5631_54072 .Pixso-instance-5615_9017 {
    width: 128px;
    height: 12px;
}
.Pixso-instance-5631_54072 .Pixso-instance-5631_54072 {
    width: 274px;
    height: 12px;
}
.Pixso-instance-5631_53798 .Pixso-symbol-5579_152932 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5631_53798 .Pixso-vector-5579_152933 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5633_54348 .Pixso-symbol-5579_152932 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5633_54348 .Pixso-vector-5579_152933 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5633_54568 .Pixso-symbol-5579_152932 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5633_54568 .Pixso-vector-5579_152933 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5633_54393 .Pixso-symbol-5590_22157 {
    width: 40px;
    height: 40px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 10px;
    justify-content: center;
    align-items: center;
    padding: 16px 16px 16px 16px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5633_54393 .Pixso-instance-5590_22158 .Pixso-symbol-5606_17909 {
    width: 24px;
    height: 24px;
    overflow: hidden;
    position: absolute;
    left: 0px;
    top: 0px;
    background-color: transparent;
}
.Pixso-instance-5633_54393 .Pixso-instance-5590_22158 .Pixso-vector-5606_17908 {
    width: 78.12%;
    height: 85.93%;
    background-image: url(@/assets/images/Vector2041.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 10.94%;
    right: 10.94%;
    top: 3.13%;
    bottom: 10.94%;
}
.Pixso-instance-5590_22158 .Pixso-vector-5606_17908 {
    width: 78.12%;
    height: 85.93%;
    position: absolute;
    left: 10.94%;
    right: 10.94%;
    top: 3.13%;
    bottom: 10.94%;
}
.Pixso-instance-5590_22158 .Pixso-instance-5590_22158 {
    width: 24px;
    height: 24px;
}
.Pixso-instance-5633_54396 .Pixso-symbol-5590_22157 {
    width: 40px;
    height: 40px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 10px;
    justify-content: center;
    align-items: center;
    padding: 16px 16px 16px 16px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5633_54396
    .Pixso-instance-5590_22158
    .Pixso-symbol-5578_150188 {
    width: 24px;
    height: 24px;
    position: absolute;
    left: 0px;
    top: 0px;
    background-color: transparent;
}
.Pixso-instance-5633_54396
    .Pixso-instance-5590_22158
    .Pixso-vector-5578_150189 {
    width: 90.62%;
    height: 81.25%;
    background-image: url(@/assets/images/Vector75.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 4.69%;
    right: 4.69%;
    top: 4.69%;
    bottom: 14.06%;
}
.Pixso-instance-5590_22158 .Pixso-vector-5578_150189 {
    width: 90.62%;
    height: 81.25%;
    position: absolute;
    left: 4.69%;
    right: 4.69%;
    top: 4.69%;
    bottom: 14.06%;
}
.Pixso-instance-5633_54402 .Pixso-symbol-5590_22157 {
    width: 40px;
    height: 40px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 10px;
    justify-content: center;
    align-items: center;
    padding: 16px 16px 16px 16px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5633_54402
    .Pixso-instance-5590_22158
    .Pixso-symbol-5578_150145 {
    width: 24px;
    height: 24px;
    position: absolute;
    left: 0px;
    top: 0px;
    background-color: transparent;
}
.Pixso-instance-5633_54402
    .Pixso-instance-5590_22158
    .Pixso-vector-5578_150146 {
    width: 12.5%;
    height: 65.62%;
    background-image: url(@/assets/images/Vector69.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 43.75%;
    right: 43.75%;
    top: 17.19%;
    bottom: 17.19%;
}
.Pixso-instance-5590_22158 .Pixso-vector-5578_150146 {
    width: 12.5%;
    height: 65.62%;
    position: absolute;
    left: 43.75%;
    right: 43.75%;
    top: 17.19%;
    bottom: 17.19%;
}
.Pixso-instance-5633_54457 .Pixso-symbol-5603_17589 {
    width: 45px;
    height: 20px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5633_54457 .Pixso-instance-5603_17590 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5633_54457 .Pixso-paragraph-5603_17591 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5633_54457 .Pixso-instance-5603_17592 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5633_54468 .Pixso-symbol-5603_17349 {
    width: 27px;
    height: 20px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5633_54468 .Pixso-instance-5603_17350 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5633_54468 .Pixso-paragraph-5603_17351 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5633_54468 .Pixso-instance-5603_17352 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5633_54526 .Pixso-instance-5566_688 {
    width: 24px;
    height: 24px;
}
.Pixso-instance-5633_54526 .Pixso-instance-5566_722 {
    width: 24px;
    height: 24px;
}
.Pixso-instance-5633_54526 .Pixso-instance-5566_725 {
    width: 24px;
    height: 24px;
}
.Pixso-instance-5633_54526 .Pixso-instance-5566_728 {
    width: 24px;
    height: 24px;
}
.Pixso-instance-5633_54526 .Pixso-instance-5566_731 {
    width: 24px;
    height: 24px;
}
.Pixso-instance-5633_54526 .Pixso-symbol-5566_1820 {
    width: 152px;
    height: 24px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: flex-start;
}
.Pixso-instance-5631_53709 .Pixso-symbol-5588_12216 {
    width: 100%;
    height: 100%;
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
.Pixso-instance-5631_53709 .stroke-wrapper-5588_12216 {
    width: 60px;
    height: 24px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5631_53709 .stroke-5588_12216 {
    inset: 0px;
    border-radius: 1234px 1234px 1234px 1234px;
    pointer-events: none;
    border-width: 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5631_53709
    .Pixso-instance-5588_12217
    .Pixso-symbol-5579_151118 {
    width: 24px;
    height: 24px;
    position: absolute;
    left: 0px;
    top: 0px;
    background-color: transparent;
}
.Pixso-instance-5631_53709 .Pixso-frame-5588_12218 {
    width: 28px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5631_53709 .Pixso-instance-5588_12219 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5631_53709 .Pixso-paragraph-5588_12220 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5631_53709 .Pixso-instance-5588_12221 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5631_53709
    .Pixso-instance-5588_12217
    .Pixso-vector-5579_151119 {
    width: 45.32%;
    height: 29.69%;
    background-image: url(@/assets/images/Vector129.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 2.34%;
    right: 52.34%;
    top: 8.59%;
    bottom: 61.72%;
}
.Pixso-instance-5588_12217 .Pixso-vector-5579_151119 {
    width: 45.32%;
    height: 29.69%;
    position: absolute;
    left: 2.34%;
    right: 52.34%;
    top: 8.59%;
    bottom: 61.72%;
}
.Pixso-instance-5588_12217 .Pixso-instance-5588_12217 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5631_53691 .Pixso-symbol-5579_152932 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5631_53691 .Pixso-vector-5579_152933 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5633_54642 .Pixso-symbol-5588_11358 {
    width: 48px;
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
.Pixso-instance-5633_54642 .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5633_54642 .Pixso-frame-5588_11360 {
    width: 32px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5633_54642 .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5633_54642 .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5633_54642 .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5633_54643 .Pixso-symbol-5579_152932 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5633_54643 .Pixso-vector-5579_152933 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5633_54664 .Pixso-symbol-5588_11358 {
    width: 48px;
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
.Pixso-instance-5633_54664 .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5633_54664 .Pixso-frame-5588_11360 {
    width: 32px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5633_54664 .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5633_54664 .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5633_54664 .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5633_54675 .Pixso-symbol-5588_12054 {
    width: 48px;
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
.Pixso-instance-5633_54675 .Pixso-instance-5588_12055 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5633_54675 .Pixso-frame-5588_12056 {
    width: 32px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5633_54675 .Pixso-instance-5588_12057 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5633_54675 .Pixso-paragraph-5588_12058 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5633_54675 .Pixso-instance-5588_12059 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5633_54684 .Pixso-symbol-5588_11883 {
    width: 48px;
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
.Pixso-instance-5633_54684 .Pixso-instance-5588_11884 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5633_54684 .Pixso-frame-5588_11885 {
    width: 32px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5633_54684 .Pixso-instance-5588_11886 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5633_54684 .Pixso-paragraph-5588_11887 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5633_54684 .Pixso-instance-5588_11888 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5633_54665 .Pixso-symbol-5579_152932 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5633_54665 .Pixso-vector-5579_152933 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5634_54963 .Pixso-symbol-5579_152932 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5634_54963 .Pixso-vector-5579_152933 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5634_54965 .Pixso-symbol-5468_1033 {
    width: 40px;
    height: 40px;
    position: relative;
    flex-shrink: 0;
    border-radius: 76.875px 76.875px 76.875px 76.875px;
}
.Pixso-instance-5634_54969 .Pixso-symbol-5579_152932 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5634_54969 .Pixso-vector-5579_152933 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5634_54971 .Pixso-symbol-5546_2916 {
    width: 40px;
    height: 40px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 10px;
    justify-content: center;
    align-items: center;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5634_54971 .Pixso-instance-5546_2917 .Pixso-vector-5579_151560 {
    width: 67.7%;
    height: 70.31%;
    background-image: url(@/assets/images/Vector317.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 3.91%;
    right: 28.39%;
    top: 6.51%;
    bottom: 23.18%;
}
.Pixso-instance-5634_54975 .Pixso-symbol-5579_152932 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5634_54975 .Pixso-vector-5579_152933 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5634_54977 .Pixso-symbol-5566_5797 {
    width: 36px;
    height: 24px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5634_54981 .Pixso-symbol-5579_152932 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5634_54981 .Pixso-vector-5579_152933 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5634_54987 .Pixso-symbol-5579_152932 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5634_54987 .Pixso-vector-5579_152933 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5634_54989 .Pixso-symbol-5461_33741 {
    width: 32px;
    height: 32px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5634_54993 .Pixso-symbol-5579_152932 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5634_54993 .Pixso-vector-5579_152933 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5634_54995 .Pixso-symbol-5631_54071 {
    width: 263px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
}
.Pixso-instance-5634_54995 .Pixso-instance-5631_54072 {
    width: 274px;
    height: 12px;
}
.Pixso-instance-5634_54995 .Pixso-paragraph-5631_54073 {
    text-align: right;
    display: flex;
    flex-direction: column;
    justify-content: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5634_54995
    .Pixso-instance-5631_54072
    .Pixso-instance-5615_9016 {
    width: 320px;
    height: 12px;
}
.Pixso-instance-5634_54995 .Pixso-instance-5631_54072 .Pixso-frame-5615_9015 {
    width: 100%;
    height: 12px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5634_54995
    .Pixso-instance-5631_54072
    .Pixso-instance-5615_9017 {
    width: 128px;
    height: 12px;
}
.Pixso-instance-5634_54996 .Pixso-symbol-5579_152932 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5634_54996 .Pixso-vector-5579_152933 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5634_54999 .Pixso-symbol-5579_152932 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5634_54999 .Pixso-vector-5579_152933 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5634_55002 .Pixso-symbol-5579_152932 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5634_55002 .Pixso-vector-5579_152933 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5634_55004 .Pixso-symbol-5590_22157 {
    width: 40px;
    height: 40px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 10px;
    justify-content: center;
    align-items: center;
    padding: 16px 16px 16px 16px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5634_55004 .Pixso-instance-5590_22158 .Pixso-symbol-5606_17909 {
    width: 24px;
    height: 24px;
    overflow: hidden;
    position: absolute;
    left: 0px;
    top: 0px;
    background-color: transparent;
}
.Pixso-instance-5634_55004 .Pixso-instance-5590_22158 .Pixso-vector-5606_17908 {
    width: 78.12%;
    height: 85.93%;
    background-image: url(@/assets/images/Vector2041.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 10.94%;
    right: 10.94%;
    top: 3.13%;
    bottom: 10.94%;
}
.Pixso-instance-5634_55005 .Pixso-symbol-5590_22157 {
    width: 40px;
    height: 40px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 10px;
    justify-content: center;
    align-items: center;
    padding: 16px 16px 16px 16px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5634_55005
    .Pixso-instance-5590_22158
    .Pixso-symbol-5578_150188 {
    width: 24px;
    height: 24px;
    position: absolute;
    left: 0px;
    top: 0px;
    background-color: transparent;
}
.Pixso-instance-5634_55005
    .Pixso-instance-5590_22158
    .Pixso-vector-5578_150189 {
    width: 90.62%;
    height: 81.25%;
    background-image: url(@/assets/images/Vector75.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 4.69%;
    right: 4.69%;
    top: 4.69%;
    bottom: 14.06%;
}
.Pixso-instance-5634_55006 .Pixso-symbol-5590_22157 {
    width: 40px;
    height: 40px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 10px;
    justify-content: center;
    align-items: center;
    padding: 16px 16px 16px 16px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5634_55006
    .Pixso-instance-5590_22158
    .Pixso-symbol-5578_150145 {
    width: 24px;
    height: 24px;
    position: absolute;
    left: 0px;
    top: 0px;
    background-color: transparent;
}
.Pixso-instance-5634_55006
    .Pixso-instance-5590_22158
    .Pixso-vector-5578_150146 {
    width: 12.5%;
    height: 65.62%;
    background-image: url(@/assets/images/Vector69.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 43.75%;
    right: 43.75%;
    top: 17.19%;
    bottom: 17.19%;
}
.Pixso-instance-5634_55008 .Pixso-symbol-5603_17589 {
    width: 45px;
    height: 20px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5634_55008 .Pixso-instance-5603_17590 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5634_55008 .Pixso-paragraph-5603_17591 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5634_55008 .Pixso-instance-5603_17592 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5634_55009 .Pixso-symbol-5603_17349 {
    width: 27px;
    height: 20px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5634_55009 .Pixso-instance-5603_17350 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5634_55009 .Pixso-paragraph-5603_17351 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5634_55009 .Pixso-instance-5603_17352 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5634_55011 .Pixso-instance-5566_688 {
    width: 24px;
    height: 24px;
}
.Pixso-instance-5634_55011 .Pixso-instance-5566_722 {
    width: 24px;
    height: 24px;
}
.Pixso-instance-5634_55011 .Pixso-instance-5566_725 {
    width: 24px;
    height: 24px;
}
.Pixso-instance-5634_55011 .Pixso-instance-5566_728 {
    width: 24px;
    height: 24px;
}
.Pixso-instance-5634_55011 .Pixso-instance-5566_731 {
    width: 24px;
    height: 24px;
}
.Pixso-instance-5634_55011 .Pixso-symbol-5566_1820 {
    width: 152px;
    height: 24px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: flex-start;
}
.Pixso-instance-5634_55016 .Pixso-symbol-5588_12216 {
    width: 100%;
    height: 100%;
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
.Pixso-instance-5634_55016 .stroke-wrapper-5588_12216 {
    width: 60px;
    height: 24px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5634_55016 .stroke-5588_12216 {
    inset: 0px;
    border-radius: 1234px 1234px 1234px 1234px;
    pointer-events: none;
    border-width: 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_55016
    .Pixso-instance-5588_12217
    .Pixso-symbol-5579_151118 {
    width: 24px;
    height: 24px;
    position: absolute;
    left: 0px;
    top: 0px;
    background-color: transparent;
}
.Pixso-instance-5634_55016 .Pixso-frame-5588_12218 {
    width: 28px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5634_55016 .Pixso-instance-5588_12219 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5634_55016 .Pixso-paragraph-5588_12220 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5634_55016 .Pixso-instance-5588_12221 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5634_55016
    .Pixso-instance-5588_12217
    .Pixso-vector-5579_151119 {
    width: 45.32%;
    height: 29.69%;
    background-image: url(@/assets/images/Vector129.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 2.34%;
    right: 52.34%;
    top: 8.59%;
    bottom: 61.72%;
}
.Pixso-instance-5634_55017 .Pixso-symbol-5579_152932 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5634_55017 .Pixso-vector-5579_152933 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5634_55019 .Pixso-symbol-5588_13114 {
    width: 48px;
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
.Pixso-instance-5634_55019 .Pixso-instance-5588_13115 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5634_55019 .Pixso-frame-5588_13116 {
    width: 32px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5634_55019 .Pixso-instance-5588_13117 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5634_55019 .Pixso-paragraph-5588_13118 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5634_55019 .Pixso-instance-5588_13119 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5634_55020 .Pixso-symbol-5579_152932 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5634_55020 .Pixso-vector-5579_152933 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5634_55023 .Pixso-symbol-5588_13114 {
    width: 48px;
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
.Pixso-instance-5634_55023 .Pixso-instance-5588_13115 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5634_55023 .Pixso-frame-5588_13116 {
    width: 32px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5634_55023 .Pixso-instance-5588_13117 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5634_55023 .Pixso-paragraph-5588_13118 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5634_55023 .Pixso-instance-5588_13119 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5634_55024 .Pixso-symbol-5588_13222 {
    width: 48px;
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
.Pixso-instance-5634_55024 .Pixso-instance-5588_13223 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5634_55024 .Pixso-frame-5588_13224 {
    width: 32px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5634_55024 .Pixso-instance-5588_13225 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5634_55024 .Pixso-paragraph-5588_13226 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5634_55024 .Pixso-instance-5588_13227 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5634_55025 .Pixso-symbol-5588_13216 {
    width: 48px;
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
.Pixso-instance-5634_55025 .Pixso-instance-5588_13217 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5634_55025 .Pixso-frame-5588_13218 {
    width: 32px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5634_55025 .Pixso-instance-5588_13219 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5634_55025 .Pixso-paragraph-5588_13220 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5634_55025 .Pixso-instance-5588_13221 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5634_55026 .Pixso-symbol-5579_152932 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5634_55026 .Pixso-vector-5579_152933 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5634_55906 .Pixso-symbol-5547_8762 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    border-radius: 8px 8px 8px 8px;
}
.Pixso-instance-5634_55906 .stroke-wrapper-5547_8762 {
    width: 20px;
    height: 20px;
    flex-shrink: 0;
}
.Pixso-instance-5634_55906 .stroke-5547_8762 {
    inset: 0px;
    border-radius: 8px 8px 8px 8px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_55529 .Pixso-symbol-5579_152932 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5634_55529 .Pixso-vector-5579_152933 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5634_57285 .Pixso-symbol-5550_11210 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5634_57285 .stroke-wrapper-5550_11210 {
    width: 20px;
    height: 20px;
    flex-shrink: 0;
}
.Pixso-instance-5634_57285 .stroke-5550_11210 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_57289 .Pixso-symbol-5579_152932 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5634_57289 .Pixso-vector-5579_152933 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5634_58260 .Pixso-symbol-5579_152932 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5634_58260 .Pixso-vector-5579_152933 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5634_57677 .Pixso-symbol-5550_11210 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5634_57677 .stroke-wrapper-5550_11210 {
    width: 20px;
    height: 20px;
    flex-shrink: 0;
}
.Pixso-instance-5634_57677 .stroke-5550_11210 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_57681 .Pixso-symbol-5579_152932 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5634_57681 .Pixso-vector-5579_152933 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5634_58266 .Pixso-symbol-5579_152932 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5634_58266 .Pixso-vector-5579_152933 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5634_55907 .Pixso-symbol-5547_8762 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    border-radius: 8px 8px 8px 8px;
}
.Pixso-instance-5634_55907 .stroke-wrapper-5547_8762 {
    width: 20px;
    height: 20px;
    flex-shrink: 0;
}
.Pixso-instance-5634_55907 .stroke-5547_8762 {
    inset: 0px;
    border-radius: 8px 8px 8px 8px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_55531 .Pixso-symbol-5468_1033 {
    width: 40px;
    height: 40px;
    position: relative;
    flex-shrink: 0;
    border-radius: 76.875px 76.875px 76.875px 76.875px;
}
.Pixso-instance-5634_55535 .Pixso-symbol-5579_152932 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5634_55535 .Pixso-vector-5579_152933 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5634_56109 .Pixso-symbol-5547_8762 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    border-radius: 8px 8px 8px 8px;
}
.Pixso-instance-5634_56109 .stroke-wrapper-5547_8762 {
    width: 20px;
    height: 20px;
    flex-shrink: 0;
}
.Pixso-instance-5634_56109 .stroke-5547_8762 {
    inset: 0px;
    border-radius: 8px 8px 8px 8px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_56113 .Pixso-symbol-5579_152932 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5634_56113 .Pixso-vector-5579_152933 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5634_57291 .Pixso-symbol-5550_11210 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5634_57291 .stroke-wrapper-5550_11210 {
    width: 20px;
    height: 20px;
    flex-shrink: 0;
}
.Pixso-instance-5634_57291 .stroke-5550_11210 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_57292 .Pixso-symbol-5468_1033 {
    width: 40px;
    height: 40px;
    position: relative;
    flex-shrink: 0;
    border-radius: 76.875px 76.875px 76.875px 76.875px;
}
.Pixso-instance-5634_57296 .Pixso-symbol-5579_152932 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5634_57296 .Pixso-vector-5579_152933 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5634_58269 .Pixso-symbol-5468_1033 {
    width: 40px;
    height: 40px;
    position: relative;
    flex-shrink: 0;
    border-radius: 76.875px 76.875px 76.875px 76.875px;
}
.Pixso-instance-5634_58273 .Pixso-symbol-5579_152932 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5634_58273 .Pixso-vector-5579_152933 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5634_55908 .Pixso-symbol-5547_8762 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    border-radius: 8px 8px 8px 8px;
}
.Pixso-instance-5634_55908 .stroke-wrapper-5547_8762 {
    width: 20px;
    height: 20px;
    flex-shrink: 0;
}
.Pixso-instance-5634_55908 .stroke-5547_8762 {
    inset: 0px;
    border-radius: 8px 8px 8px 8px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_55537 .Pixso-symbol-5546_2916 {
    width: 40px;
    height: 40px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 10px;
    justify-content: center;
    align-items: center;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5634_55537 .Pixso-instance-5546_2917 .Pixso-vector-5579_151560 {
    width: 67.7%;
    height: 70.31%;
    background-image: url(@/assets/images/Vector317.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 3.91%;
    right: 28.39%;
    top: 6.51%;
    bottom: 23.18%;
}
.Pixso-instance-5634_55541 .Pixso-symbol-5579_152932 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5634_55541 .Pixso-vector-5579_152933 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5634_57683 .Pixso-symbol-5550_11210 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5634_57683 .stroke-wrapper-5550_11210 {
    width: 20px;
    height: 20px;
    flex-shrink: 0;
}
.Pixso-instance-5634_57683 .stroke-5550_11210 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_57684 .Pixso-symbol-5468_1033 {
    width: 40px;
    height: 40px;
    position: relative;
    flex-shrink: 0;
    border-radius: 76.875px 76.875px 76.875px 76.875px;
}
.Pixso-instance-5634_57688 .Pixso-symbol-5579_152932 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5634_57688 .Pixso-vector-5579_152933 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5634_58276 .Pixso-symbol-5468_1033 {
    width: 40px;
    height: 40px;
    position: relative;
    flex-shrink: 0;
    border-radius: 76.875px 76.875px 76.875px 76.875px;
}
.Pixso-instance-5634_58280 .Pixso-symbol-5579_152932 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5634_58280 .Pixso-vector-5579_152933 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5634_55909 .Pixso-symbol-5547_8762 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    border-radius: 8px 8px 8px 8px;
}
.Pixso-instance-5634_55909 .stroke-wrapper-5547_8762 {
    width: 20px;
    height: 20px;
    flex-shrink: 0;
}
.Pixso-instance-5634_55909 .stroke-5547_8762 {
    inset: 0px;
    border-radius: 8px 8px 8px 8px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_55543 .Pixso-symbol-5566_5797 {
    width: 36px;
    height: 24px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5634_55547 .Pixso-symbol-5579_152932 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5634_55547 .Pixso-vector-5579_152933 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5634_57298 .Pixso-symbol-5550_11210 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5634_57298 .stroke-wrapper-5550_11210 {
    width: 20px;
    height: 20px;
    flex-shrink: 0;
}
.Pixso-instance-5634_57298 .stroke-5550_11210 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_57299 .Pixso-symbol-5546_2916 {
    width: 40px;
    height: 40px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 10px;
    justify-content: center;
    align-items: center;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5634_57299 .Pixso-instance-5546_2917 .Pixso-vector-5579_151560 {
    width: 67.7%;
    height: 70.31%;
    background-image: url(@/assets/images/Vector317.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 3.91%;
    right: 28.39%;
    top: 6.51%;
    bottom: 23.18%;
}
.Pixso-instance-5634_57303 .Pixso-symbol-5579_152932 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5634_57303 .Pixso-vector-5579_152933 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5634_58283 .Pixso-symbol-5546_2916 {
    width: 40px;
    height: 40px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 10px;
    justify-content: center;
    align-items: center;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5634_58283 .Pixso-instance-5546_2917 .Pixso-vector-5579_151560 {
    width: 67.7%;
    height: 70.31%;
    background-image: url(@/assets/images/Vector317.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 3.91%;
    right: 28.39%;
    top: 6.51%;
    bottom: 23.18%;
}
.Pixso-instance-5634_58287 .Pixso-symbol-5579_152932 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5634_58287 .Pixso-vector-5579_152933 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5634_56115 .Pixso-symbol-5547_8762 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    border-radius: 8px 8px 8px 8px;
}
.Pixso-instance-5634_56115 .stroke-wrapper-5547_8762 {
    width: 20px;
    height: 20px;
    flex-shrink: 0;
}
.Pixso-instance-5634_56115 .stroke-5547_8762 {
    inset: 0px;
    border-radius: 8px 8px 8px 8px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_56116 .Pixso-symbol-5468_1033 {
    width: 40px;
    height: 40px;
    position: relative;
    flex-shrink: 0;
    border-radius: 76.875px 76.875px 76.875px 76.875px;
}
.Pixso-instance-5634_56120 .Pixso-symbol-5579_152932 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5634_56120 .Pixso-vector-5579_152933 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5634_55910 .Pixso-symbol-5547_8762 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    border-radius: 8px 8px 8px 8px;
}
.Pixso-instance-5634_55910 .stroke-wrapper-5547_8762 {
    width: 20px;
    height: 20px;
    flex-shrink: 0;
}
.Pixso-instance-5634_55910 .stroke-5547_8762 {
    inset: 0px;
    border-radius: 8px 8px 8px 8px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_55553 .Pixso-symbol-5579_152932 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5634_55553 .Pixso-vector-5579_152933 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5634_57690 .Pixso-symbol-5550_11210 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5634_57690 .stroke-wrapper-5550_11210 {
    width: 20px;
    height: 20px;
    flex-shrink: 0;
}
.Pixso-instance-5634_57690 .stroke-5550_11210 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_57691 .Pixso-symbol-5546_2916 {
    width: 40px;
    height: 40px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 10px;
    justify-content: center;
    align-items: center;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5634_57691 .Pixso-instance-5546_2917 .Pixso-vector-5579_151560 {
    width: 67.7%;
    height: 70.31%;
    background-image: url(@/assets/images/Vector317.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 3.91%;
    right: 28.39%;
    top: 6.51%;
    bottom: 23.18%;
}
.Pixso-instance-5634_57695 .Pixso-symbol-5579_152932 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5634_57695 .Pixso-vector-5579_152933 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5634_58290 .Pixso-symbol-5546_2916 {
    width: 40px;
    height: 40px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 10px;
    justify-content: center;
    align-items: center;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5634_58290 .Pixso-instance-5546_2917 .Pixso-vector-5579_151560 {
    width: 67.7%;
    height: 70.31%;
    background-image: url(@/assets/images/Vector317.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 3.91%;
    right: 28.39%;
    top: 6.51%;
    bottom: 23.18%;
}
.Pixso-instance-5634_58294 .Pixso-symbol-5579_152932 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5634_58294 .Pixso-vector-5579_152933 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5634_57305 .Pixso-symbol-5550_11210 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5634_57305 .stroke-wrapper-5550_11210 {
    width: 20px;
    height: 20px;
    flex-shrink: 0;
}
.Pixso-instance-5634_57305 .stroke-5550_11210 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_57306 .Pixso-symbol-5566_5797 {
    width: 36px;
    height: 24px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5634_57310 .Pixso-symbol-5579_152932 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5634_57310 .Pixso-vector-5579_152933 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5634_58297 .Pixso-symbol-5566_5797 {
    width: 36px;
    height: 24px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5634_58301 .Pixso-symbol-5579_152932 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5634_58301 .Pixso-vector-5579_152933 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5634_55911 .Pixso-symbol-5547_8762 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    border-radius: 8px 8px 8px 8px;
}
.Pixso-instance-5634_55911 .stroke-wrapper-5547_8762 {
    width: 20px;
    height: 20px;
    flex-shrink: 0;
}
.Pixso-instance-5634_55911 .stroke-5547_8762 {
    inset: 0px;
    border-radius: 8px 8px 8px 8px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_55555 .Pixso-symbol-5461_33741 {
    width: 32px;
    height: 32px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5634_55559 .Pixso-symbol-5579_152932 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5634_55559 .Pixso-vector-5579_152933 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5634_56122 .Pixso-symbol-5547_8762 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    border-radius: 8px 8px 8px 8px;
}
.Pixso-instance-5634_56122 .stroke-wrapper-5547_8762 {
    width: 20px;
    height: 20px;
    flex-shrink: 0;
}
.Pixso-instance-5634_56122 .stroke-5547_8762 {
    inset: 0px;
    border-radius: 8px 8px 8px 8px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_56123 .Pixso-symbol-5546_2916 {
    width: 40px;
    height: 40px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 10px;
    justify-content: center;
    align-items: center;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5634_56123 .Pixso-instance-5546_2917 .Pixso-vector-5579_151560 {
    width: 67.7%;
    height: 70.31%;
    background-image: url(@/assets/images/Vector317.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 3.91%;
    right: 28.39%;
    top: 6.51%;
    bottom: 23.18%;
}
.Pixso-instance-5634_56127 .Pixso-symbol-5579_152932 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5634_56127 .Pixso-vector-5579_152933 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5634_55912 .Pixso-symbol-5547_8762 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    border-radius: 8px 8px 8px 8px;
}
.Pixso-instance-5634_55912 .stroke-wrapper-5547_8762 {
    width: 20px;
    height: 20px;
    flex-shrink: 0;
}
.Pixso-instance-5634_55912 .stroke-5547_8762 {
    inset: 0px;
    border-radius: 8px 8px 8px 8px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_55561 .Pixso-symbol-5631_54071 {
    width: 231px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
}
.Pixso-instance-5634_55561 .Pixso-instance-5631_54072 {
    width: 274px;
    height: 12px;
}
.Pixso-instance-5634_55561 .Pixso-paragraph-5631_54073 {
    text-align: right;
    display: flex;
    flex-direction: column;
    justify-content: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5634_55561
    .Pixso-instance-5631_54072
    .Pixso-instance-5615_9016 {
    width: 320px;
    height: 12px;
}
.Pixso-instance-5634_55561 .Pixso-instance-5631_54072 .Pixso-frame-5615_9015 {
    width: 100%;
    height: 12px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5634_55561
    .Pixso-instance-5631_54072
    .Pixso-instance-5615_9017 {
    width: 128px;
    height: 12px;
}
.Pixso-instance-5634_55562 .Pixso-symbol-5579_152932 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5634_55562 .Pixso-vector-5579_152933 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5634_57312 .Pixso-symbol-5550_11210 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5634_57312 .stroke-wrapper-5550_11210 {
    width: 20px;
    height: 20px;
    flex-shrink: 0;
}
.Pixso-instance-5634_57312 .stroke-5550_11210 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_57317 .Pixso-symbol-5579_152932 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5634_57317 .Pixso-vector-5579_152933 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5634_58308 .Pixso-symbol-5579_152932 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5634_58308 .Pixso-vector-5579_152933 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5634_57697 .Pixso-symbol-5550_11210 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5634_57697 .stroke-wrapper-5550_11210 {
    width: 20px;
    height: 20px;
    flex-shrink: 0;
}
.Pixso-instance-5634_57697 .stroke-5550_11210 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_57698 .Pixso-symbol-5566_5797 {
    width: 36px;
    height: 24px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5634_57702 .Pixso-symbol-5579_152932 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5634_57702 .Pixso-vector-5579_152933 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5634_58311 .Pixso-symbol-5566_5797 {
    width: 36px;
    height: 24px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5634_58315 .Pixso-symbol-5579_152932 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5634_58315 .Pixso-vector-5579_152933 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5634_55913 .Pixso-symbol-5547_8762 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    border-radius: 8px 8px 8px 8px;
}
.Pixso-instance-5634_55913 .stroke-wrapper-5547_8762 {
    width: 20px;
    height: 20px;
    flex-shrink: 0;
}
.Pixso-instance-5634_55913 .stroke-5547_8762 {
    inset: 0px;
    border-radius: 8px 8px 8px 8px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_55565 .Pixso-symbol-5579_152932 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5634_55565 .Pixso-vector-5579_152933 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5634_56129 .Pixso-symbol-5547_8762 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    border-radius: 8px 8px 8px 8px;
}
.Pixso-instance-5634_56129 .stroke-wrapper-5547_8762 {
    width: 20px;
    height: 20px;
    flex-shrink: 0;
}
.Pixso-instance-5634_56129 .stroke-5547_8762 {
    inset: 0px;
    border-radius: 8px 8px 8px 8px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_56130 .Pixso-symbol-5566_5797 {
    width: 36px;
    height: 24px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5634_56134 .Pixso-symbol-5579_152932 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5634_56134 .Pixso-vector-5579_152933 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5634_57319 .Pixso-symbol-5550_11210 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5634_57319 .stroke-wrapper-5550_11210 {
    width: 20px;
    height: 20px;
    flex-shrink: 0;
}
.Pixso-instance-5634_57319 .stroke-5550_11210 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_57320 .Pixso-symbol-5461_33741 {
    width: 32px;
    height: 32px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5634_57324 .Pixso-symbol-5579_152932 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5634_57324 .Pixso-vector-5579_152933 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5634_58318 .Pixso-symbol-5461_33741 {
    width: 32px;
    height: 32px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5634_58322 .Pixso-symbol-5579_152932 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5634_58322 .Pixso-vector-5579_152933 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5634_55914 .Pixso-symbol-5547_8762 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    border-radius: 8px 8px 8px 8px;
}
.Pixso-instance-5634_55914 .stroke-wrapper-5547_8762 {
    width: 20px;
    height: 20px;
    flex-shrink: 0;
}
.Pixso-instance-5634_55914 .stroke-5547_8762 {
    inset: 0px;
    border-radius: 8px 8px 8px 8px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_55568 .Pixso-symbol-5579_152932 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5634_55568 .Pixso-vector-5579_152933 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5634_57704 .Pixso-symbol-5550_11210 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5634_57704 .stroke-wrapper-5550_11210 {
    width: 20px;
    height: 20px;
    flex-shrink: 0;
}
.Pixso-instance-5634_57704 .stroke-5550_11210 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_57709 .Pixso-symbol-5579_152932 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5634_57709 .Pixso-vector-5579_152933 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5634_58329 .Pixso-symbol-5579_152932 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5634_58329 .Pixso-vector-5579_152933 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5634_55915 .Pixso-symbol-5547_8762 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    border-radius: 8px 8px 8px 8px;
}
.Pixso-instance-5634_55915 .stroke-wrapper-5547_8762 {
    width: 20px;
    height: 20px;
    flex-shrink: 0;
}
.Pixso-instance-5634_55915 .stroke-5547_8762 {
    inset: 0px;
    border-radius: 8px 8px 8px 8px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_55570 .Pixso-symbol-5590_22157 {
    width: 40px;
    height: 40px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 10px;
    justify-content: center;
    align-items: center;
    padding: 16px 16px 16px 16px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5634_55570 .Pixso-instance-5590_22158 .Pixso-symbol-5606_17909 {
    width: 24px;
    height: 24px;
    overflow: hidden;
    position: absolute;
    left: 0px;
    top: 0px;
    background-color: transparent;
}
.Pixso-instance-5634_55570 .Pixso-instance-5590_22158 .Pixso-vector-5606_17908 {
    width: 78.12%;
    height: 85.93%;
    background-image: url(@/assets/images/Vector2041.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 10.94%;
    right: 10.94%;
    top: 3.13%;
    bottom: 10.94%;
}
.Pixso-instance-5634_55571 .Pixso-symbol-5590_22157 {
    width: 40px;
    height: 40px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 10px;
    justify-content: center;
    align-items: center;
    padding: 16px 16px 16px 16px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5634_55571
    .Pixso-instance-5590_22158
    .Pixso-symbol-5578_150188 {
    width: 24px;
    height: 24px;
    position: absolute;
    left: 0px;
    top: 0px;
    background-color: transparent;
}
.Pixso-instance-5634_55571
    .Pixso-instance-5590_22158
    .Pixso-vector-5578_150189 {
    width: 90.62%;
    height: 81.25%;
    background-image: url(@/assets/images/Vector75.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 4.69%;
    right: 4.69%;
    top: 4.69%;
    bottom: 14.06%;
}
.Pixso-instance-5634_55572 .Pixso-symbol-5590_22157 {
    width: 40px;
    height: 40px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 10px;
    justify-content: center;
    align-items: center;
    padding: 16px 16px 16px 16px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5634_55572
    .Pixso-instance-5590_22158
    .Pixso-symbol-5578_150145 {
    width: 24px;
    height: 24px;
    position: absolute;
    left: 0px;
    top: 0px;
    background-color: transparent;
}
.Pixso-instance-5634_55572
    .Pixso-instance-5590_22158
    .Pixso-vector-5578_150146 {
    width: 12.5%;
    height: 65.62%;
    background-image: url(@/assets/images/Vector69.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 43.75%;
    right: 43.75%;
    top: 17.19%;
    bottom: 17.19%;
}
.Pixso-instance-5634_57326 .Pixso-symbol-5550_11210 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5634_57326 .stroke-wrapper-5550_11210 {
    width: 20px;
    height: 20px;
    flex-shrink: 0;
}
.Pixso-instance-5634_57326 .stroke-5550_11210 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_57327 .Pixso-symbol-5631_54071 {
    width: 231px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
}
.Pixso-instance-5634_57327 .Pixso-instance-5631_54072 {
    width: 274px;
    height: 12px;
}
.Pixso-instance-5634_57327 .Pixso-paragraph-5631_54073 {
    text-align: right;
    display: flex;
    flex-direction: column;
    justify-content: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5634_57327
    .Pixso-instance-5631_54072
    .Pixso-instance-5615_9016 {
    width: 320px;
    height: 12px;
}
.Pixso-instance-5634_57327 .Pixso-instance-5631_54072 .Pixso-frame-5615_9015 {
    width: 100%;
    height: 12px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5634_57327
    .Pixso-instance-5631_54072
    .Pixso-instance-5615_9017 {
    width: 128px;
    height: 12px;
}
.Pixso-instance-5634_57328 .Pixso-symbol-5579_152932 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5634_57328 .Pixso-vector-5579_152933 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5634_58332 .Pixso-symbol-5631_54071 {
    width: 207px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
}
.Pixso-instance-5634_58332 .Pixso-instance-5631_54072 {
    width: 274px;
    height: 12px;
}
.Pixso-instance-5634_58332 .Pixso-paragraph-5631_54073 {
    text-align: right;
    display: flex;
    flex-direction: column;
    justify-content: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5634_58332
    .Pixso-instance-5631_54072
    .Pixso-instance-5615_9016 {
    width: 320px;
    height: 12px;
}
.Pixso-instance-5634_58332 .Pixso-instance-5631_54072 .Pixso-frame-5615_9015 {
    width: 100%;
    height: 12px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5634_58332
    .Pixso-instance-5631_54072
    .Pixso-instance-5615_9017 {
    width: 128px;
    height: 12px;
}
.Pixso-instance-5634_58333 .Pixso-symbol-5579_152932 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5634_58333 .Pixso-vector-5579_152933 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5634_56136 .Pixso-symbol-5547_8762 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    border-radius: 8px 8px 8px 8px;
}
.Pixso-instance-5634_56136 .stroke-wrapper-5547_8762 {
    width: 20px;
    height: 20px;
    flex-shrink: 0;
}
.Pixso-instance-5634_56136 .stroke-5547_8762 {
    inset: 0px;
    border-radius: 8px 8px 8px 8px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_56141 .Pixso-symbol-5579_152932 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5634_56141 .Pixso-vector-5579_152933 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5634_55916 .Pixso-symbol-5547_8762 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    border-radius: 8px 8px 8px 8px;
}
.Pixso-instance-5634_55916 .stroke-wrapper-5547_8762 {
    width: 20px;
    height: 20px;
    flex-shrink: 0;
}
.Pixso-instance-5634_55916 .stroke-5547_8762 {
    inset: 0px;
    border-radius: 8px 8px 8px 8px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_55574 .Pixso-symbol-5603_17589 {
    width: 45px;
    height: 20px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5634_55574 .Pixso-instance-5603_17590 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5634_55574 .Pixso-paragraph-5603_17591 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5634_55574 .Pixso-instance-5603_17592 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5634_55575 .Pixso-symbol-5603_17349 {
    width: 27px;
    height: 20px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5634_55575 .Pixso-instance-5603_17350 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5634_55575 .Pixso-paragraph-5603_17351 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5634_55575 .Pixso-instance-5603_17352 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5634_57711 .Pixso-symbol-5550_11210 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5634_57711 .stroke-wrapper-5550_11210 {
    width: 20px;
    height: 20px;
    flex-shrink: 0;
}
.Pixso-instance-5634_57711 .stroke-5550_11210 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_57712 .Pixso-symbol-5461_33741 {
    width: 32px;
    height: 32px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5634_57716 .Pixso-symbol-5579_152932 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5634_57716 .Pixso-vector-5579_152933 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5634_58336 .Pixso-symbol-5461_33741 {
    width: 32px;
    height: 32px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5634_58340 .Pixso-symbol-5579_152932 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5634_58340 .Pixso-vector-5579_152933 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5634_57330 .Pixso-symbol-5550_11210 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5634_57330 .stroke-wrapper-5550_11210 {
    width: 20px;
    height: 20px;
    flex-shrink: 0;
}
.Pixso-instance-5634_57330 .stroke-5550_11210 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_57332 .Pixso-symbol-5579_152932 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5634_57332 .Pixso-vector-5579_152933 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5634_58344 .Pixso-symbol-5579_152932 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5634_58344 .Pixso-vector-5579_152933 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5634_55917 .Pixso-symbol-5547_8762 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    border-radius: 8px 8px 8px 8px;
}
.Pixso-instance-5634_55917 .stroke-wrapper-5547_8762 {
    width: 20px;
    height: 20px;
    flex-shrink: 0;
}
.Pixso-instance-5634_55917 .stroke-5547_8762 {
    inset: 0px;
    border-radius: 8px 8px 8px 8px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_55577 .Pixso-instance-5566_688 {
    width: 24px;
    height: 24px;
}
.Pixso-instance-5634_55577 .Pixso-instance-5566_722 {
    width: 24px;
    height: 24px;
}
.Pixso-instance-5634_55577 .Pixso-instance-5566_725 {
    width: 24px;
    height: 24px;
}
.Pixso-instance-5634_55577 .Pixso-instance-5566_728 {
    width: 24px;
    height: 24px;
}
.Pixso-instance-5634_55577 .Pixso-instance-5566_731 {
    width: 24px;
    height: 24px;
}
.Pixso-instance-5634_55577 .Pixso-symbol-5566_1820 {
    width: 152px;
    height: 24px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: flex-start;
}
.Pixso-instance-5634_57334 .Pixso-symbol-5550_11210 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5634_57334 .stroke-wrapper-5550_11210 {
    width: 20px;
    height: 20px;
    flex-shrink: 0;
}
.Pixso-instance-5634_57334 .stroke-5550_11210 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_57336 .Pixso-symbol-5579_152932 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5634_57336 .Pixso-vector-5579_152933 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5634_58348 .Pixso-symbol-5579_152932 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5634_58348 .Pixso-vector-5579_152933 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5634_56143 .Pixso-symbol-5547_8762 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    border-radius: 8px 8px 8px 8px;
}
.Pixso-instance-5634_56143 .stroke-wrapper-5547_8762 {
    width: 20px;
    height: 20px;
    flex-shrink: 0;
}
.Pixso-instance-5634_56143 .stroke-5547_8762 {
    inset: 0px;
    border-radius: 8px 8px 8px 8px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_56144 .Pixso-symbol-5461_33741 {
    width: 32px;
    height: 32px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5634_56148 .Pixso-symbol-5579_152932 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5634_56148 .Pixso-vector-5579_152933 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5634_57338 .Pixso-symbol-5550_11210 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5634_57338 .stroke-wrapper-5550_11210 {
    width: 20px;
    height: 20px;
    flex-shrink: 0;
}
.Pixso-instance-5634_57338 .stroke-5550_11210 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_57339 .Pixso-symbol-5590_22157 {
    width: 40px;
    height: 40px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 10px;
    justify-content: center;
    align-items: center;
    padding: 16px 16px 16px 16px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5634_57339 .Pixso-instance-5590_22158 .Pixso-symbol-5606_17909 {
    width: 24px;
    height: 24px;
    overflow: hidden;
    position: absolute;
    left: 0px;
    top: 0px;
    background-color: transparent;
}
.Pixso-instance-5634_57339 .Pixso-instance-5590_22158 .Pixso-vector-5606_17908 {
    width: 78.12%;
    height: 85.93%;
    background-image: url(@/assets/images/Vector2041.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 10.94%;
    right: 10.94%;
    top: 3.13%;
    bottom: 10.94%;
}
.Pixso-instance-5634_57340 .Pixso-symbol-5590_22157 {
    width: 40px;
    height: 40px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 10px;
    justify-content: center;
    align-items: center;
    padding: 16px 16px 16px 16px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5634_57340
    .Pixso-instance-5590_22158
    .Pixso-symbol-5578_150188 {
    width: 24px;
    height: 24px;
    position: absolute;
    left: 0px;
    top: 0px;
    background-color: transparent;
}
.Pixso-instance-5634_57340
    .Pixso-instance-5590_22158
    .Pixso-vector-5578_150189 {
    width: 90.62%;
    height: 81.25%;
    background-image: url(@/assets/images/Vector75.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 4.69%;
    right: 4.69%;
    top: 4.69%;
    bottom: 14.06%;
}
.Pixso-instance-5634_57341 .Pixso-symbol-5590_22157 {
    width: 40px;
    height: 40px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 10px;
    justify-content: center;
    align-items: center;
    padding: 16px 16px 16px 16px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5634_57341
    .Pixso-instance-5590_22158
    .Pixso-symbol-5578_150145 {
    width: 24px;
    height: 24px;
    position: absolute;
    left: 0px;
    top: 0px;
    background-color: transparent;
}
.Pixso-instance-5634_57341
    .Pixso-instance-5590_22158
    .Pixso-vector-5578_150146 {
    width: 12.5%;
    height: 65.62%;
    background-image: url(@/assets/images/Vector69.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 43.75%;
    right: 43.75%;
    top: 17.19%;
    bottom: 17.19%;
}
.Pixso-instance-5634_58351 .Pixso-symbol-5590_22157 {
    width: 40px;
    height: 40px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 10px;
    justify-content: center;
    align-items: center;
    padding: 16px 16px 16px 16px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5634_58351 .Pixso-instance-5590_22158 .Pixso-symbol-5606_17909 {
    width: 24px;
    height: 24px;
    overflow: hidden;
    position: absolute;
    left: 0px;
    top: 0px;
    background-color: transparent;
}
.Pixso-instance-5634_58351 .Pixso-instance-5590_22158 .Pixso-vector-5606_17908 {
    width: 78.12%;
    height: 85.93%;
    background-image: url(@/assets/images/Vector2041.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 10.94%;
    right: 10.94%;
    top: 3.13%;
    bottom: 10.94%;
}
.Pixso-instance-5634_58352 .Pixso-symbol-5590_22157 {
    width: 40px;
    height: 40px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 10px;
    justify-content: center;
    align-items: center;
    padding: 16px 16px 16px 16px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5634_58352
    .Pixso-instance-5590_22158
    .Pixso-symbol-5578_150188 {
    width: 24px;
    height: 24px;
    position: absolute;
    left: 0px;
    top: 0px;
    background-color: transparent;
}
.Pixso-instance-5634_58352
    .Pixso-instance-5590_22158
    .Pixso-vector-5578_150189 {
    width: 90.62%;
    height: 81.25%;
    background-image: url(@/assets/images/Vector75.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 4.69%;
    right: 4.69%;
    top: 4.69%;
    bottom: 14.06%;
}
.Pixso-instance-5634_58353 .Pixso-symbol-5590_22157 {
    width: 40px;
    height: 40px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 10px;
    justify-content: center;
    align-items: center;
    padding: 16px 16px 16px 16px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5634_58353
    .Pixso-instance-5590_22158
    .Pixso-symbol-5578_150145 {
    width: 24px;
    height: 24px;
    position: absolute;
    left: 0px;
    top: 0px;
    background-color: transparent;
}
.Pixso-instance-5634_58353
    .Pixso-instance-5590_22158
    .Pixso-vector-5578_150146 {
    width: 12.5%;
    height: 65.62%;
    background-image: url(@/assets/images/Vector69.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 43.75%;
    right: 43.75%;
    top: 17.19%;
    bottom: 17.19%;
}
.Pixso-instance-5634_55918 .Pixso-symbol-5547_8762 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    border-radius: 8px 8px 8px 8px;
}
.Pixso-instance-5634_55918 .stroke-wrapper-5547_8762 {
    width: 20px;
    height: 20px;
    flex-shrink: 0;
}
.Pixso-instance-5634_55918 .stroke-5547_8762 {
    inset: 0px;
    border-radius: 8px 8px 8px 8px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_55582 .Pixso-symbol-5588_12216 {
    width: 100%;
    height: 100%;
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
.Pixso-instance-5634_55582 .stroke-wrapper-5588_12216 {
    width: 60px;
    height: 24px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5634_55582 .stroke-5588_12216 {
    inset: 0px;
    border-radius: 1234px 1234px 1234px 1234px;
    pointer-events: none;
    border-width: 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_55582
    .Pixso-instance-5588_12217
    .Pixso-symbol-5579_151118 {
    width: 24px;
    height: 24px;
    position: absolute;
    left: 0px;
    top: 0px;
    background-color: transparent;
}
.Pixso-instance-5634_55582 .Pixso-frame-5588_12218 {
    width: 28px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5634_55582 .Pixso-instance-5588_12219 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5634_55582 .Pixso-paragraph-5588_12220 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5634_55582 .Pixso-instance-5588_12221 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5634_55582
    .Pixso-instance-5588_12217
    .Pixso-vector-5579_151119 {
    width: 45.32%;
    height: 29.69%;
    background-image: url(@/assets/images/Vector129.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 2.34%;
    right: 52.34%;
    top: 8.59%;
    bottom: 61.72%;
}
.Pixso-instance-5634_55583 .Pixso-symbol-5579_152932 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5634_55583 .Pixso-vector-5579_152933 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5634_57343 .Pixso-symbol-5550_11210 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5634_57343 .stroke-wrapper-5550_11210 {
    width: 20px;
    height: 20px;
    flex-shrink: 0;
}
.Pixso-instance-5634_57343 .stroke-5550_11210 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_57344 .Pixso-symbol-5603_17589 {
    width: 45px;
    height: 20px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5634_57344 .Pixso-instance-5603_17590 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5634_57344 .Pixso-paragraph-5603_17591 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5634_57344 .Pixso-instance-5603_17592 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5634_57345 .Pixso-symbol-5603_17349 {
    width: 27px;
    height: 20px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5634_57345 .Pixso-instance-5603_17350 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5634_57345 .Pixso-paragraph-5603_17351 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5634_57345 .Pixso-instance-5603_17352 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5634_58356 .Pixso-symbol-5603_17589 {
    width: 45px;
    height: 20px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5634_58356 .Pixso-instance-5603_17590 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5634_58356 .Pixso-paragraph-5603_17591 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5634_58356 .Pixso-instance-5603_17592 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5634_58357 .Pixso-symbol-5603_17349 {
    width: 27px;
    height: 20px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5634_58357 .Pixso-instance-5603_17350 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5634_58357 .Pixso-paragraph-5603_17351 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5634_58357 .Pixso-instance-5603_17352 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5634_57718 .Pixso-symbol-5550_11210 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5634_57718 .stroke-wrapper-5550_11210 {
    width: 20px;
    height: 20px;
    flex-shrink: 0;
}
.Pixso-instance-5634_57718 .stroke-5550_11210 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_57719 .Pixso-symbol-5631_54071 {
    width: 231px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
}
.Pixso-instance-5634_57719 .Pixso-instance-5631_54072 {
    width: 274px;
    height: 12px;
}
.Pixso-instance-5634_57719 .Pixso-paragraph-5631_54073 {
    text-align: right;
    display: flex;
    flex-direction: column;
    justify-content: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5634_57719
    .Pixso-instance-5631_54072
    .Pixso-instance-5615_9016 {
    width: 320px;
    height: 12px;
}
.Pixso-instance-5634_57719 .Pixso-instance-5631_54072 .Pixso-frame-5615_9015 {
    width: 100%;
    height: 12px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5634_57719
    .Pixso-instance-5631_54072
    .Pixso-instance-5615_9017 {
    width: 128px;
    height: 12px;
}
.Pixso-instance-5634_57720 .Pixso-symbol-5579_152932 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5634_57720 .Pixso-vector-5579_152933 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5634_58360 .Pixso-symbol-5631_54071 {
    width: 207px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
}
.Pixso-instance-5634_58360 .Pixso-instance-5631_54072 {
    width: 274px;
    height: 12px;
}
.Pixso-instance-5634_58360 .Pixso-paragraph-5631_54073 {
    text-align: right;
    display: flex;
    flex-direction: column;
    justify-content: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5634_58360
    .Pixso-instance-5631_54072
    .Pixso-instance-5615_9016 {
    width: 320px;
    height: 12px;
}
.Pixso-instance-5634_58360 .Pixso-instance-5631_54072 .Pixso-frame-5615_9015 {
    width: 100%;
    height: 12px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5634_58360
    .Pixso-instance-5631_54072
    .Pixso-instance-5615_9017 {
    width: 128px;
    height: 12px;
}
.Pixso-instance-5634_58361 .Pixso-symbol-5579_152932 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5634_58361 .Pixso-vector-5579_152933 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5634_57347 .Pixso-symbol-5550_11210 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5634_57347 .stroke-wrapper-5550_11210 {
    width: 20px;
    height: 20px;
    flex-shrink: 0;
}
.Pixso-instance-5634_57347 .stroke-5550_11210 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_57348 .Pixso-instance-5566_688 {
    width: 24px;
    height: 24px;
}
.Pixso-instance-5634_57348 .Pixso-instance-5566_722 {
    width: 24px;
    height: 24px;
}
.Pixso-instance-5634_57348 .Pixso-instance-5566_725 {
    width: 24px;
    height: 24px;
}
.Pixso-instance-5634_57348 .Pixso-instance-5566_728 {
    width: 24px;
    height: 24px;
}
.Pixso-instance-5634_57348 .Pixso-instance-5566_731 {
    width: 24px;
    height: 24px;
}
.Pixso-instance-5634_57348 .Pixso-symbol-5566_1820 {
    width: 152px;
    height: 24px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: flex-start;
}
.Pixso-instance-5634_58364 .Pixso-instance-5566_688 {
    width: 24px;
    height: 24px;
}
.Pixso-instance-5634_58364 .Pixso-instance-5566_722 {
    width: 24px;
    height: 24px;
}
.Pixso-instance-5634_58364 .Pixso-instance-5566_725 {
    width: 24px;
    height: 24px;
}
.Pixso-instance-5634_58364 .Pixso-instance-5566_728 {
    width: 24px;
    height: 24px;
}
.Pixso-instance-5634_58364 .Pixso-instance-5566_731 {
    width: 24px;
    height: 24px;
}
.Pixso-instance-5634_58364 .Pixso-symbol-5566_1820 {
    width: 152px;
    height: 24px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: flex-start;
}
.Pixso-instance-5634_55919 .Pixso-symbol-5547_8762 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    border-radius: 8px 8px 8px 8px;
}
.Pixso-instance-5634_55919 .stroke-wrapper-5547_8762 {
    width: 20px;
    height: 20px;
    flex-shrink: 0;
}
.Pixso-instance-5634_55919 .stroke-5547_8762 {
    inset: 0px;
    border-radius: 8px 8px 8px 8px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_55585 .Pixso-symbol-5588_11358 {
    width: 48px;
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
.Pixso-instance-5634_55585 .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5634_55585 .Pixso-frame-5588_11360 {
    width: 32px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5634_55585 .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5634_55585 .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5634_55585 .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5634_55586 .Pixso-symbol-5579_152932 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5634_55586 .Pixso-vector-5579_152933 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5634_57351 .Pixso-symbol-5550_11210 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5634_57351 .stroke-wrapper-5550_11210 {
    width: 20px;
    height: 20px;
    flex-shrink: 0;
}
.Pixso-instance-5634_57351 .stroke-5550_11210 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_57354 .Pixso-symbol-5588_12216 {
    width: 100%;
    height: 100%;
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
.Pixso-instance-5634_57354 .stroke-wrapper-5588_12216 {
    width: 60px;
    height: 24px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5634_57354 .stroke-5588_12216 {
    inset: 0px;
    border-radius: 1234px 1234px 1234px 1234px;
    pointer-events: none;
    border-width: 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_57354
    .Pixso-instance-5588_12217
    .Pixso-symbol-5579_151118 {
    width: 24px;
    height: 24px;
    position: absolute;
    left: 0px;
    top: 0px;
    background-color: transparent;
}
.Pixso-instance-5634_57354 .Pixso-frame-5588_12218 {
    width: 28px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5634_57354 .Pixso-instance-5588_12219 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5634_57354 .Pixso-paragraph-5588_12220 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5634_57354 .Pixso-instance-5588_12221 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5634_57354
    .Pixso-instance-5588_12217
    .Pixso-vector-5579_151119 {
    width: 45.32%;
    height: 29.69%;
    background-image: url(@/assets/images/Vector129.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 2.34%;
    right: 52.34%;
    top: 8.59%;
    bottom: 61.72%;
}
.Pixso-instance-5634_57355 .Pixso-symbol-5579_152932 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5634_57355 .Pixso-vector-5579_152933 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5634_58370 .Pixso-symbol-5588_12216 {
    width: 100%;
    height: 100%;
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
.Pixso-instance-5634_58370 .stroke-wrapper-5588_12216 {
    width: 60px;
    height: 24px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5634_58370 .stroke-5588_12216 {
    inset: 0px;
    border-radius: 1234px 1234px 1234px 1234px;
    pointer-events: none;
    border-width: 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_58370
    .Pixso-instance-5588_12217
    .Pixso-symbol-5579_151118 {
    width: 24px;
    height: 24px;
    position: absolute;
    left: 0px;
    top: 0px;
    background-color: transparent;
}
.Pixso-instance-5634_58370 .Pixso-frame-5588_12218 {
    width: 28px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5634_58370 .Pixso-instance-5588_12219 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5634_58370 .Pixso-paragraph-5588_12220 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5634_58370 .Pixso-instance-5588_12221 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5634_58370
    .Pixso-instance-5588_12217
    .Pixso-vector-5579_151119 {
    width: 45.32%;
    height: 29.69%;
    background-image: url(@/assets/images/Vector129.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 2.34%;
    right: 52.34%;
    top: 8.59%;
    bottom: 61.72%;
}
.Pixso-instance-5634_58371 .Pixso-symbol-5579_152932 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5634_58371 .Pixso-vector-5579_152933 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5634_56150 .Pixso-symbol-5547_8762 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    border-radius: 8px 8px 8px 8px;
}
.Pixso-instance-5634_56150 .stroke-wrapper-5547_8762 {
    width: 20px;
    height: 20px;
    flex-shrink: 0;
}
.Pixso-instance-5634_56150 .stroke-5547_8762 {
    inset: 0px;
    border-radius: 8px 8px 8px 8px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_56151 .Pixso-symbol-5631_54071 {
    width: 231px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
}
.Pixso-instance-5634_56151 .Pixso-instance-5631_54072 {
    width: 274px;
    height: 12px;
}
.Pixso-instance-5634_56151 .Pixso-paragraph-5631_54073 {
    text-align: right;
    display: flex;
    flex-direction: column;
    justify-content: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5634_56151
    .Pixso-instance-5631_54072
    .Pixso-instance-5615_9016 {
    width: 320px;
    height: 12px;
}
.Pixso-instance-5634_56151 .Pixso-instance-5631_54072 .Pixso-frame-5615_9015 {
    width: 100%;
    height: 12px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5634_56151
    .Pixso-instance-5631_54072
    .Pixso-instance-5615_9017 {
    width: 128px;
    height: 12px;
}
.Pixso-instance-5634_56152 .Pixso-symbol-5579_152932 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5634_56152 .Pixso-vector-5579_152933 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5634_57357 .Pixso-symbol-5550_11210 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5634_57357 .stroke-wrapper-5550_11210 {
    width: 20px;
    height: 20px;
    flex-shrink: 0;
}
.Pixso-instance-5634_57357 .stroke-5550_11210 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_57358 .Pixso-symbol-5588_11358 {
    width: 48px;
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
.Pixso-instance-5634_57358 .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5634_57358 .Pixso-frame-5588_11360 {
    width: 32px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5634_57358 .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5634_57358 .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5634_57358 .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5634_57359 .Pixso-symbol-5579_152932 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5634_57359 .Pixso-vector-5579_152933 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5634_58374 .Pixso-symbol-5588_11358 {
    width: 48px;
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
.Pixso-instance-5634_58374 .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5634_58374 .Pixso-frame-5588_11360 {
    width: 32px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5634_58374 .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5634_58374 .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5634_58374 .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5634_58375 .Pixso-symbol-5579_152932 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5634_58375 .Pixso-vector-5579_152933 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5634_55920 .Pixso-symbol-5547_8762 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    border-radius: 8px 8px 8px 8px;
}
.Pixso-instance-5634_55920 .stroke-wrapper-5547_8762 {
    width: 20px;
    height: 20px;
    flex-shrink: 0;
}
.Pixso-instance-5634_55920 .stroke-5547_8762 {
    inset: 0px;
    border-radius: 8px 8px 8px 8px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_55589 .Pixso-symbol-5588_11358 {
    width: 48px;
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
.Pixso-instance-5634_55589 .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5634_55589 .Pixso-frame-5588_11360 {
    width: 32px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5634_55589 .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5634_55589 .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5634_55589 .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5634_55590 .Pixso-symbol-5588_12054 {
    width: 48px;
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
.Pixso-instance-5634_55590 .Pixso-instance-5588_12055 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5634_55590 .Pixso-frame-5588_12056 {
    width: 32px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5634_55590 .Pixso-instance-5588_12057 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5634_55590 .Pixso-paragraph-5588_12058 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5634_55590 .Pixso-instance-5588_12059 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5634_55591 .Pixso-symbol-5588_11883 {
    width: 48px;
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
.Pixso-instance-5634_55591 .Pixso-instance-5588_11884 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5634_55591 .Pixso-frame-5588_11885 {
    width: 32px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5634_55591 .Pixso-instance-5588_11886 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5634_55591 .Pixso-paragraph-5588_11887 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5634_55591 .Pixso-instance-5588_11888 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5634_55592 .Pixso-symbol-5579_152932 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5634_55592 .Pixso-vector-5579_152933 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5634_57361 .Pixso-symbol-5550_11210 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5634_57361 .stroke-wrapper-5550_11210 {
    width: 20px;
    height: 20px;
    flex-shrink: 0;
}
.Pixso-instance-5634_57361 .stroke-5550_11210 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_57363 .Pixso-symbol-5588_11358 {
    width: 48px;
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
.Pixso-instance-5634_57363 .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5634_57363 .Pixso-frame-5588_11360 {
    width: 32px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5634_57363 .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5634_57363 .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5634_57363 .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5634_57364 .Pixso-symbol-5588_12054 {
    width: 48px;
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
.Pixso-instance-5634_57364 .Pixso-instance-5588_12055 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5634_57364 .Pixso-frame-5588_12056 {
    width: 32px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5634_57364 .Pixso-instance-5588_12057 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5634_57364 .Pixso-paragraph-5588_12058 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5634_57364 .Pixso-instance-5588_12059 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5634_57365 .Pixso-symbol-5588_11883 {
    width: 48px;
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
.Pixso-instance-5634_57365 .Pixso-instance-5588_11884 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5634_57365 .Pixso-frame-5588_11885 {
    width: 32px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5634_57365 .Pixso-instance-5588_11886 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5634_57365 .Pixso-paragraph-5588_11887 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5634_57365 .Pixso-instance-5588_11888 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5634_57366 .Pixso-symbol-5579_152932 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5634_57366 .Pixso-vector-5579_152933 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5634_58379 .Pixso-symbol-5588_11358 {
    width: 48px;
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
.Pixso-instance-5634_58379 .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5634_58379 .Pixso-frame-5588_11360 {
    width: 32px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5634_58379 .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5634_58379 .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5634_58379 .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5634_58380 .Pixso-symbol-5588_12054 {
    width: 48px;
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
.Pixso-instance-5634_58380 .Pixso-instance-5588_12055 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5634_58380 .Pixso-frame-5588_12056 {
    width: 32px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5634_58380 .Pixso-instance-5588_12057 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5634_58380 .Pixso-paragraph-5588_12058 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5634_58380 .Pixso-instance-5588_12059 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5634_58381 .Pixso-symbol-5588_11883 {
    width: 48px;
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
.Pixso-instance-5634_58381 .Pixso-instance-5588_11884 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5634_58381 .Pixso-frame-5588_11885 {
    width: 32px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5634_58381 .Pixso-instance-5588_11886 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5634_58381 .Pixso-paragraph-5588_11887 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5634_58381 .Pixso-instance-5588_11888 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5634_58382 .Pixso-symbol-5579_152932 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5634_58382 .Pixso-vector-5579_152933 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5634_57722 .Pixso-symbol-5550_11210 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5634_57722 .stroke-wrapper-5550_11210 {
    width: 20px;
    height: 20px;
    flex-shrink: 0;
}
.Pixso-instance-5634_57722 .stroke-5550_11210 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_57724 .Pixso-symbol-5579_152932 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5634_57724 .Pixso-vector-5579_152933 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5634_58386 .Pixso-symbol-5579_152932 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5634_58386 .Pixso-vector-5579_152933 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5634_56154 .Pixso-symbol-5547_8762 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    border-radius: 8px 8px 8px 8px;
}
.Pixso-instance-5634_56154 .stroke-wrapper-5547_8762 {
    width: 20px;
    height: 20px;
    flex-shrink: 0;
}
.Pixso-instance-5634_56154 .stroke-5547_8762 {
    inset: 0px;
    border-radius: 8px 8px 8px 8px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_56156 .Pixso-symbol-5579_152932 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5634_56156 .Pixso-vector-5579_152933 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5634_57726 .Pixso-symbol-5550_11210 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5634_57726 .stroke-wrapper-5550_11210 {
    width: 20px;
    height: 20px;
    flex-shrink: 0;
}
.Pixso-instance-5634_57726 .stroke-5550_11210 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_57728 .Pixso-symbol-5579_152932 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5634_57728 .Pixso-vector-5579_152933 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5634_58390 .Pixso-symbol-5579_152932 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5634_58390 .Pixso-vector-5579_152933 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5634_56158 .Pixso-symbol-5547_8762 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    border-radius: 8px 8px 8px 8px;
}
.Pixso-instance-5634_56158 .stroke-wrapper-5547_8762 {
    width: 20px;
    height: 20px;
    flex-shrink: 0;
}
.Pixso-instance-5634_56158 .stroke-5547_8762 {
    inset: 0px;
    border-radius: 8px 8px 8px 8px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_56160 .Pixso-symbol-5579_152932 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5634_56160 .Pixso-vector-5579_152933 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5634_57730 .Pixso-symbol-5550_11210 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5634_57730 .stroke-wrapper-5550_11210 {
    width: 20px;
    height: 20px;
    flex-shrink: 0;
}
.Pixso-instance-5634_57730 .stroke-5550_11210 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_57731 .Pixso-symbol-5590_22157 {
    width: 40px;
    height: 40px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 10px;
    justify-content: center;
    align-items: center;
    padding: 16px 16px 16px 16px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5634_57731 .Pixso-instance-5590_22158 .Pixso-symbol-5606_17909 {
    width: 24px;
    height: 24px;
    overflow: hidden;
    position: absolute;
    left: 0px;
    top: 0px;
    background-color: transparent;
}
.Pixso-instance-5634_57731 .Pixso-instance-5590_22158 .Pixso-vector-5606_17908 {
    width: 78.12%;
    height: 85.93%;
    background-image: url(@/assets/images/Vector2041.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 10.94%;
    right: 10.94%;
    top: 3.13%;
    bottom: 10.94%;
}
.Pixso-instance-5634_57732 .Pixso-symbol-5590_22157 {
    width: 40px;
    height: 40px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 10px;
    justify-content: center;
    align-items: center;
    padding: 16px 16px 16px 16px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5634_57732
    .Pixso-instance-5590_22158
    .Pixso-symbol-5578_150188 {
    width: 24px;
    height: 24px;
    position: absolute;
    left: 0px;
    top: 0px;
    background-color: transparent;
}
.Pixso-instance-5634_57732
    .Pixso-instance-5590_22158
    .Pixso-vector-5578_150189 {
    width: 90.62%;
    height: 81.25%;
    background-image: url(@/assets/images/Vector75.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 4.69%;
    right: 4.69%;
    top: 4.69%;
    bottom: 14.06%;
}
.Pixso-instance-5634_57733 .Pixso-symbol-5590_22157 {
    width: 40px;
    height: 40px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 10px;
    justify-content: center;
    align-items: center;
    padding: 16px 16px 16px 16px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5634_57733
    .Pixso-instance-5590_22158
    .Pixso-symbol-5578_150145 {
    width: 24px;
    height: 24px;
    position: absolute;
    left: 0px;
    top: 0px;
    background-color: transparent;
}
.Pixso-instance-5634_57733
    .Pixso-instance-5590_22158
    .Pixso-vector-5578_150146 {
    width: 12.5%;
    height: 65.62%;
    background-image: url(@/assets/images/Vector69.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 43.75%;
    right: 43.75%;
    top: 17.19%;
    bottom: 17.19%;
}
.Pixso-instance-5634_58393 .Pixso-symbol-5590_22157 {
    width: 40px;
    height: 40px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 10px;
    justify-content: center;
    align-items: center;
    padding: 16px 16px 16px 16px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5634_58393 .Pixso-instance-5590_22158 .Pixso-symbol-5606_17909 {
    width: 24px;
    height: 24px;
    overflow: hidden;
    position: absolute;
    left: 0px;
    top: 0px;
    background-color: transparent;
}
.Pixso-instance-5634_58393 .Pixso-instance-5590_22158 .Pixso-vector-5606_17908 {
    width: 78.12%;
    height: 85.93%;
    background-image: url(@/assets/images/Vector2041.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 10.94%;
    right: 10.94%;
    top: 3.13%;
    bottom: 10.94%;
}
.Pixso-instance-5634_58394 .Pixso-symbol-5590_22157 {
    width: 40px;
    height: 40px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 10px;
    justify-content: center;
    align-items: center;
    padding: 16px 16px 16px 16px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5634_58394
    .Pixso-instance-5590_22158
    .Pixso-symbol-5578_150188 {
    width: 24px;
    height: 24px;
    position: absolute;
    left: 0px;
    top: 0px;
    background-color: transparent;
}
.Pixso-instance-5634_58394
    .Pixso-instance-5590_22158
    .Pixso-vector-5578_150189 {
    width: 90.62%;
    height: 81.25%;
    background-image: url(@/assets/images/Vector75.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 4.69%;
    right: 4.69%;
    top: 4.69%;
    bottom: 14.06%;
}
.Pixso-instance-5634_58395 .Pixso-symbol-5590_22157 {
    width: 40px;
    height: 40px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 10px;
    justify-content: center;
    align-items: center;
    padding: 16px 16px 16px 16px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5634_58395
    .Pixso-instance-5590_22158
    .Pixso-symbol-5578_150145 {
    width: 24px;
    height: 24px;
    position: absolute;
    left: 0px;
    top: 0px;
    background-color: transparent;
}
.Pixso-instance-5634_58395
    .Pixso-instance-5590_22158
    .Pixso-vector-5578_150146 {
    width: 12.5%;
    height: 65.62%;
    background-image: url(@/assets/images/Vector69.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 43.75%;
    right: 43.75%;
    top: 17.19%;
    bottom: 17.19%;
}
.Pixso-instance-5634_56162 .Pixso-symbol-5547_8762 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    border-radius: 8px 8px 8px 8px;
}
.Pixso-instance-5634_56162 .stroke-wrapper-5547_8762 {
    width: 20px;
    height: 20px;
    flex-shrink: 0;
}
.Pixso-instance-5634_56162 .stroke-5547_8762 {
    inset: 0px;
    border-radius: 8px 8px 8px 8px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_56163 .Pixso-symbol-5590_22157 {
    width: 40px;
    height: 40px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 10px;
    justify-content: center;
    align-items: center;
    padding: 16px 16px 16px 16px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5634_56163 .Pixso-instance-5590_22158 .Pixso-symbol-5606_17909 {
    width: 24px;
    height: 24px;
    overflow: hidden;
    position: absolute;
    left: 0px;
    top: 0px;
    background-color: transparent;
}
.Pixso-instance-5634_56163 .Pixso-instance-5590_22158 .Pixso-vector-5606_17908 {
    width: 78.12%;
    height: 85.93%;
    background-image: url(@/assets/images/Vector2041.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 10.94%;
    right: 10.94%;
    top: 3.13%;
    bottom: 10.94%;
}
.Pixso-instance-5634_56164 .Pixso-symbol-5590_22157 {
    width: 40px;
    height: 40px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 10px;
    justify-content: center;
    align-items: center;
    padding: 16px 16px 16px 16px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5634_56164
    .Pixso-instance-5590_22158
    .Pixso-symbol-5578_150188 {
    width: 24px;
    height: 24px;
    position: absolute;
    left: 0px;
    top: 0px;
    background-color: transparent;
}
.Pixso-instance-5634_56164
    .Pixso-instance-5590_22158
    .Pixso-vector-5578_150189 {
    width: 90.62%;
    height: 81.25%;
    background-image: url(@/assets/images/Vector75.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 4.69%;
    right: 4.69%;
    top: 4.69%;
    bottom: 14.06%;
}
.Pixso-instance-5634_56165 .Pixso-symbol-5590_22157 {
    width: 40px;
    height: 40px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 10px;
    justify-content: center;
    align-items: center;
    padding: 16px 16px 16px 16px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5634_56165
    .Pixso-instance-5590_22158
    .Pixso-symbol-5578_150145 {
    width: 24px;
    height: 24px;
    position: absolute;
    left: 0px;
    top: 0px;
    background-color: transparent;
}
.Pixso-instance-5634_56165
    .Pixso-instance-5590_22158
    .Pixso-vector-5578_150146 {
    width: 12.5%;
    height: 65.62%;
    background-image: url(@/assets/images/Vector69.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 43.75%;
    right: 43.75%;
    top: 17.19%;
    bottom: 17.19%;
}
.Pixso-instance-5634_57735 .Pixso-symbol-5550_11210 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5634_57735 .stroke-wrapper-5550_11210 {
    width: 20px;
    height: 20px;
    flex-shrink: 0;
}
.Pixso-instance-5634_57735 .stroke-5550_11210 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_57736 .Pixso-symbol-5603_17589 {
    width: 45px;
    height: 20px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5634_57736 .Pixso-instance-5603_17590 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5634_57736 .Pixso-paragraph-5603_17591 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5634_57736 .Pixso-instance-5603_17592 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5634_57737 .Pixso-symbol-5603_17349 {
    width: 27px;
    height: 20px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5634_57737 .Pixso-instance-5603_17350 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5634_57737 .Pixso-paragraph-5603_17351 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5634_57737 .Pixso-instance-5603_17352 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5634_58398 .Pixso-symbol-5603_17589 {
    width: 45px;
    height: 20px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5634_58398 .Pixso-instance-5603_17590 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5634_58398 .Pixso-paragraph-5603_17591 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5634_58398 .Pixso-instance-5603_17592 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5634_58399 .Pixso-symbol-5603_17349 {
    width: 27px;
    height: 20px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5634_58399 .Pixso-instance-5603_17350 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5634_58399 .Pixso-paragraph-5603_17351 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5634_58399 .Pixso-instance-5603_17352 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5634_56167 .Pixso-symbol-5547_8762 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    border-radius: 8px 8px 8px 8px;
}
.Pixso-instance-5634_56167 .stroke-wrapper-5547_8762 {
    width: 20px;
    height: 20px;
    flex-shrink: 0;
}
.Pixso-instance-5634_56167 .stroke-5547_8762 {
    inset: 0px;
    border-radius: 8px 8px 8px 8px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_56168 .Pixso-symbol-5603_17589 {
    width: 45px;
    height: 20px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5634_56168 .Pixso-instance-5603_17590 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5634_56168 .Pixso-paragraph-5603_17591 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5634_56168 .Pixso-instance-5603_17592 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5634_56169 .Pixso-symbol-5603_17349 {
    width: 27px;
    height: 20px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5634_56169 .Pixso-instance-5603_17350 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5634_56169 .Pixso-paragraph-5603_17351 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5634_56169 .Pixso-instance-5603_17352 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5634_57739 .Pixso-symbol-5550_11210 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5634_57739 .stroke-wrapper-5550_11210 {
    width: 20px;
    height: 20px;
    flex-shrink: 0;
}
.Pixso-instance-5634_57739 .stroke-5550_11210 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_57740 .Pixso-instance-5566_688 {
    width: 24px;
    height: 24px;
}
.Pixso-instance-5634_57740 .Pixso-instance-5566_722 {
    width: 24px;
    height: 24px;
}
.Pixso-instance-5634_57740 .Pixso-instance-5566_725 {
    width: 24px;
    height: 24px;
}
.Pixso-instance-5634_57740 .Pixso-instance-5566_728 {
    width: 24px;
    height: 24px;
}
.Pixso-instance-5634_57740 .Pixso-instance-5566_731 {
    width: 24px;
    height: 24px;
}
.Pixso-instance-5634_57740 .Pixso-symbol-5566_1820 {
    width: 152px;
    height: 24px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: flex-start;
}
.Pixso-instance-5634_58402 .Pixso-instance-5566_688 {
    width: 24px;
    height: 24px;
}
.Pixso-instance-5634_58402 .Pixso-instance-5566_722 {
    width: 24px;
    height: 24px;
}
.Pixso-instance-5634_58402 .Pixso-instance-5566_725 {
    width: 24px;
    height: 24px;
}
.Pixso-instance-5634_58402 .Pixso-instance-5566_728 {
    width: 24px;
    height: 24px;
}
.Pixso-instance-5634_58402 .Pixso-instance-5566_731 {
    width: 24px;
    height: 24px;
}
.Pixso-instance-5634_58402 .Pixso-symbol-5566_1820 {
    width: 152px;
    height: 24px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: flex-start;
}
.Pixso-instance-5634_56171 .Pixso-symbol-5547_8762 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    border-radius: 8px 8px 8px 8px;
}
.Pixso-instance-5634_56171 .stroke-wrapper-5547_8762 {
    width: 20px;
    height: 20px;
    flex-shrink: 0;
}
.Pixso-instance-5634_56171 .stroke-5547_8762 {
    inset: 0px;
    border-radius: 8px 8px 8px 8px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_56172 .Pixso-instance-5566_688 {
    width: 24px;
    height: 24px;
}
.Pixso-instance-5634_56172 .Pixso-instance-5566_722 {
    width: 24px;
    height: 24px;
}
.Pixso-instance-5634_56172 .Pixso-instance-5566_725 {
    width: 24px;
    height: 24px;
}
.Pixso-instance-5634_56172 .Pixso-instance-5566_728 {
    width: 24px;
    height: 24px;
}
.Pixso-instance-5634_56172 .Pixso-instance-5566_731 {
    width: 24px;
    height: 24px;
}
.Pixso-instance-5634_56172 .Pixso-symbol-5566_1820 {
    width: 152px;
    height: 24px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: flex-start;
}
.Pixso-instance-5634_57743 .Pixso-symbol-5550_11210 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5634_57743 .stroke-wrapper-5550_11210 {
    width: 20px;
    height: 20px;
    flex-shrink: 0;
}
.Pixso-instance-5634_57743 .stroke-5550_11210 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_57746 .Pixso-symbol-5588_12216 {
    width: 100%;
    height: 100%;
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
.Pixso-instance-5634_57746 .stroke-wrapper-5588_12216 {
    width: 60px;
    height: 24px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5634_57746 .stroke-5588_12216 {
    inset: 0px;
    border-radius: 1234px 1234px 1234px 1234px;
    pointer-events: none;
    border-width: 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_57746
    .Pixso-instance-5588_12217
    .Pixso-symbol-5579_151118 {
    width: 24px;
    height: 24px;
    position: absolute;
    left: 0px;
    top: 0px;
    background-color: transparent;
}
.Pixso-instance-5634_57746 .Pixso-frame-5588_12218 {
    width: 28px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5634_57746 .Pixso-instance-5588_12219 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5634_57746 .Pixso-paragraph-5588_12220 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5634_57746 .Pixso-instance-5588_12221 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5634_57746
    .Pixso-instance-5588_12217
    .Pixso-vector-5579_151119 {
    width: 45.32%;
    height: 29.69%;
    background-image: url(@/assets/images/Vector129.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 2.34%;
    right: 52.34%;
    top: 8.59%;
    bottom: 61.72%;
}
.Pixso-instance-5634_57747 .Pixso-symbol-5579_152932 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5634_57747 .Pixso-vector-5579_152933 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5634_58408 .Pixso-symbol-5588_12216 {
    width: 100%;
    height: 100%;
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
.Pixso-instance-5634_58408 .stroke-wrapper-5588_12216 {
    width: 60px;
    height: 24px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5634_58408 .stroke-5588_12216 {
    inset: 0px;
    border-radius: 1234px 1234px 1234px 1234px;
    pointer-events: none;
    border-width: 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_58408
    .Pixso-instance-5588_12217
    .Pixso-symbol-5579_151118 {
    width: 24px;
    height: 24px;
    position: absolute;
    left: 0px;
    top: 0px;
    background-color: transparent;
}
.Pixso-instance-5634_58408 .Pixso-frame-5588_12218 {
    width: 28px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5634_58408 .Pixso-instance-5588_12219 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5634_58408 .Pixso-paragraph-5588_12220 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5634_58408 .Pixso-instance-5588_12221 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5634_58408
    .Pixso-instance-5588_12217
    .Pixso-vector-5579_151119 {
    width: 45.32%;
    height: 29.69%;
    background-image: url(@/assets/images/Vector129.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 2.34%;
    right: 52.34%;
    top: 8.59%;
    bottom: 61.72%;
}
.Pixso-instance-5634_58409 .Pixso-symbol-5579_152932 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5634_58409 .Pixso-vector-5579_152933 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5634_56175 .Pixso-symbol-5547_8762 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    border-radius: 8px 8px 8px 8px;
}
.Pixso-instance-5634_56175 .stroke-wrapper-5547_8762 {
    width: 20px;
    height: 20px;
    flex-shrink: 0;
}
.Pixso-instance-5634_56175 .stroke-5547_8762 {
    inset: 0px;
    border-radius: 8px 8px 8px 8px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_56178 .Pixso-symbol-5588_12216 {
    width: 100%;
    height: 100%;
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
.Pixso-instance-5634_56178 .stroke-wrapper-5588_12216 {
    width: 60px;
    height: 24px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5634_56178 .stroke-5588_12216 {
    inset: 0px;
    border-radius: 1234px 1234px 1234px 1234px;
    pointer-events: none;
    border-width: 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_56178
    .Pixso-instance-5588_12217
    .Pixso-symbol-5579_151118 {
    width: 24px;
    height: 24px;
    position: absolute;
    left: 0px;
    top: 0px;
    background-color: transparent;
}
.Pixso-instance-5634_56178 .Pixso-frame-5588_12218 {
    width: 28px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5634_56178 .Pixso-instance-5588_12219 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5634_56178 .Pixso-paragraph-5588_12220 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5634_56178 .Pixso-instance-5588_12221 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5634_56178
    .Pixso-instance-5588_12217
    .Pixso-vector-5579_151119 {
    width: 45.32%;
    height: 29.69%;
    background-image: url(@/assets/images/Vector129.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 2.34%;
    right: 52.34%;
    top: 8.59%;
    bottom: 61.72%;
}
.Pixso-instance-5634_56179 .Pixso-symbol-5579_152932 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5634_56179 .Pixso-vector-5579_152933 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5634_57749 .Pixso-symbol-5550_11210 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5634_57749 .stroke-wrapper-5550_11210 {
    width: 20px;
    height: 20px;
    flex-shrink: 0;
}
.Pixso-instance-5634_57749 .stroke-5550_11210 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_57750 .Pixso-symbol-5588_11358 {
    width: 48px;
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
.Pixso-instance-5634_57750 .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5634_57750 .Pixso-frame-5588_11360 {
    width: 32px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5634_57750 .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5634_57750 .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5634_57750 .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5634_57751 .Pixso-symbol-5579_152932 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5634_57751 .Pixso-vector-5579_152933 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5634_58412 .Pixso-symbol-5588_11358 {
    width: 48px;
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
.Pixso-instance-5634_58412 .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5634_58412 .Pixso-frame-5588_11360 {
    width: 32px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5634_58412 .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5634_58412 .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5634_58412 .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5634_58413 .Pixso-symbol-5579_152932 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5634_58413 .Pixso-vector-5579_152933 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5634_56181 .Pixso-symbol-5547_8762 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    border-radius: 8px 8px 8px 8px;
}
.Pixso-instance-5634_56181 .stroke-wrapper-5547_8762 {
    width: 20px;
    height: 20px;
    flex-shrink: 0;
}
.Pixso-instance-5634_56181 .stroke-5547_8762 {
    inset: 0px;
    border-radius: 8px 8px 8px 8px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_56182 .Pixso-symbol-5588_11358 {
    width: 48px;
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
.Pixso-instance-5634_56182 .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5634_56182 .Pixso-frame-5588_11360 {
    width: 32px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5634_56182 .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5634_56182 .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5634_56182 .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5634_56183 .Pixso-symbol-5579_152932 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5634_56183 .Pixso-vector-5579_152933 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5634_57753 .Pixso-symbol-5550_11210 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5634_57753 .stroke-wrapper-5550_11210 {
    width: 20px;
    height: 20px;
    flex-shrink: 0;
}
.Pixso-instance-5634_57753 .stroke-5550_11210 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_57755 .Pixso-symbol-5588_11358 {
    width: 48px;
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
.Pixso-instance-5634_57755 .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5634_57755 .Pixso-frame-5588_11360 {
    width: 32px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5634_57755 .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5634_57755 .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5634_57755 .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5634_57756 .Pixso-symbol-5588_12054 {
    width: 48px;
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
.Pixso-instance-5634_57756 .Pixso-instance-5588_12055 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5634_57756 .Pixso-frame-5588_12056 {
    width: 32px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5634_57756 .Pixso-instance-5588_12057 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5634_57756 .Pixso-paragraph-5588_12058 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5634_57756 .Pixso-instance-5588_12059 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5634_57757 .Pixso-symbol-5588_11883 {
    width: 48px;
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
.Pixso-instance-5634_57757 .Pixso-instance-5588_11884 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5634_57757 .Pixso-frame-5588_11885 {
    width: 32px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5634_57757 .Pixso-instance-5588_11886 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5634_57757 .Pixso-paragraph-5588_11887 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5634_57757 .Pixso-instance-5588_11888 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5634_57758 .Pixso-symbol-5579_152932 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5634_57758 .Pixso-vector-5579_152933 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5634_58417 .Pixso-symbol-5588_11358 {
    width: 48px;
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
.Pixso-instance-5634_58417 .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5634_58417 .Pixso-frame-5588_11360 {
    width: 32px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5634_58417 .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5634_58417 .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5634_58417 .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5634_58418 .Pixso-symbol-5588_12054 {
    width: 48px;
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
.Pixso-instance-5634_58418 .Pixso-instance-5588_12055 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5634_58418 .Pixso-frame-5588_12056 {
    width: 32px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5634_58418 .Pixso-instance-5588_12057 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5634_58418 .Pixso-paragraph-5588_12058 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5634_58418 .Pixso-instance-5588_12059 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5634_58419 .Pixso-symbol-5588_11883 {
    width: 48px;
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
.Pixso-instance-5634_58419 .Pixso-instance-5588_11884 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5634_58419 .Pixso-frame-5588_11885 {
    width: 32px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5634_58419 .Pixso-instance-5588_11886 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5634_58419 .Pixso-paragraph-5588_11887 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5634_58419 .Pixso-instance-5588_11888 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5634_58420 .Pixso-symbol-5579_152932 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5634_58420 .Pixso-vector-5579_152933 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5634_56185 .Pixso-symbol-5547_8762 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    border-radius: 8px 8px 8px 8px;
}
.Pixso-instance-5634_56185 .stroke-wrapper-5547_8762 {
    width: 20px;
    height: 20px;
    flex-shrink: 0;
}
.Pixso-instance-5634_56185 .stroke-5547_8762 {
    inset: 0px;
    border-radius: 8px 8px 8px 8px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_56187 .Pixso-symbol-5588_11358 {
    width: 48px;
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
.Pixso-instance-5634_56187 .Pixso-instance-5588_11359 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5634_56187 .Pixso-frame-5588_11360 {
    width: 32px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5634_56187 .Pixso-instance-5588_11361 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5634_56187 .Pixso-paragraph-5588_11362 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5634_56187 .Pixso-instance-5588_11363 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5634_56188 .Pixso-symbol-5588_12054 {
    width: 48px;
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
.Pixso-instance-5634_56188 .Pixso-instance-5588_12055 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5634_56188 .Pixso-frame-5588_12056 {
    width: 32px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5634_56188 .Pixso-instance-5588_12057 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5634_56188 .Pixso-paragraph-5588_12058 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5634_56188 .Pixso-instance-5588_12059 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5634_56189 .Pixso-symbol-5588_11883 {
    width: 48px;
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
.Pixso-instance-5634_56189 .Pixso-instance-5588_11884 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5634_56189 .Pixso-frame-5588_11885 {
    width: 32px;
    height: 16px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5634_56189 .Pixso-instance-5588_11886 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5634_56189 .Pixso-paragraph-5588_11887 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5634_56189 .Pixso-instance-5588_11888 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-5634_56190 .Pixso-symbol-5579_152932 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5634_56190 .Pixso-vector-5579_152933 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5634_58256 .Pixso-symbol-5550_11484 {
    width: 44px;
    height: 24px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    align-items: center;
    padding: 2px 2px 2px 2px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5634_58262 .Pixso-symbol-5550_11484 {
    width: 44px;
    height: 24px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    align-items: center;
    padding: 2px 2px 2px 2px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5634_58268 .Pixso-symbol-5550_11484 {
    width: 44px;
    height: 24px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    align-items: center;
    padding: 2px 2px 2px 2px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5634_58275 .Pixso-symbol-5550_11484 {
    width: 44px;
    height: 24px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    align-items: center;
    padding: 2px 2px 2px 2px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5634_58282 .Pixso-symbol-5550_11484 {
    width: 44px;
    height: 24px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    align-items: center;
    padding: 2px 2px 2px 2px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5634_58289 .Pixso-symbol-5550_11484 {
    width: 44px;
    height: 24px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    align-items: center;
    padding: 2px 2px 2px 2px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5634_58296 .Pixso-symbol-5550_11484 {
    width: 44px;
    height: 24px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    align-items: center;
    padding: 2px 2px 2px 2px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5634_58303 .Pixso-symbol-5550_11484 {
    width: 44px;
    height: 24px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    align-items: center;
    padding: 2px 2px 2px 2px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5634_58310 .Pixso-symbol-5550_11484 {
    width: 44px;
    height: 24px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    align-items: center;
    padding: 2px 2px 2px 2px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5634_58317 .Pixso-symbol-5550_11484 {
    width: 44px;
    height: 24px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    align-items: center;
    padding: 2px 2px 2px 2px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5634_58324 .Pixso-symbol-5550_11484 {
    width: 44px;
    height: 24px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    align-items: center;
    padding: 2px 2px 2px 2px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5634_58331 .Pixso-symbol-5550_11484 {
    width: 44px;
    height: 24px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    align-items: center;
    padding: 2px 2px 2px 2px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5634_58335 .Pixso-symbol-5550_11484 {
    width: 44px;
    height: 24px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    align-items: center;
    padding: 2px 2px 2px 2px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5634_58342 .Pixso-symbol-5550_11484 {
    width: 44px;
    height: 24px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    align-items: center;
    padding: 2px 2px 2px 2px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5634_58346 .Pixso-symbol-5550_11484 {
    width: 44px;
    height: 24px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    align-items: center;
    padding: 2px 2px 2px 2px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5634_58350 .Pixso-symbol-5550_11484 {
    width: 44px;
    height: 24px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    align-items: center;
    padding: 2px 2px 2px 2px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5634_58355 .Pixso-symbol-5550_11484 {
    width: 44px;
    height: 24px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    align-items: center;
    padding: 2px 2px 2px 2px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5634_58359 .Pixso-symbol-5550_11484 {
    width: 44px;
    height: 24px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    align-items: center;
    padding: 2px 2px 2px 2px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5634_58363 .Pixso-symbol-5550_11484 {
    width: 44px;
    height: 24px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    align-items: center;
    padding: 2px 2px 2px 2px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5634_58367 .Pixso-symbol-5550_11484 {
    width: 44px;
    height: 24px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    align-items: center;
    padding: 2px 2px 2px 2px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5634_58373 .Pixso-symbol-5550_11484 {
    width: 44px;
    height: 24px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    align-items: center;
    padding: 2px 2px 2px 2px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5634_58377 .Pixso-symbol-5550_11484 {
    width: 44px;
    height: 24px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    align-items: center;
    padding: 2px 2px 2px 2px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5634_58384 .Pixso-symbol-5550_11484 {
    width: 44px;
    height: 24px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    align-items: center;
    padding: 2px 2px 2px 2px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5634_58388 .Pixso-symbol-5550_11484 {
    width: 44px;
    height: 24px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    align-items: center;
    padding: 2px 2px 2px 2px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5634_58392 .Pixso-symbol-5550_11484 {
    width: 44px;
    height: 24px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    align-items: center;
    padding: 2px 2px 2px 2px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5634_58397 .Pixso-symbol-5550_11484 {
    width: 44px;
    height: 24px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    align-items: center;
    padding: 2px 2px 2px 2px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5634_58401 .Pixso-symbol-5550_11484 {
    width: 44px;
    height: 24px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    align-items: center;
    padding: 2px 2px 2px 2px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5634_58405 .Pixso-symbol-5550_11484 {
    width: 44px;
    height: 24px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    align-items: center;
    padding: 2px 2px 2px 2px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5634_58411 .Pixso-symbol-5550_11484 {
    width: 44px;
    height: 24px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    align-items: center;
    padding: 2px 2px 2px 2px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5634_58415 .Pixso-symbol-5550_11484 {
    width: 44px;
    height: 24px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    align-items: center;
    padding: 2px 2px 2px 2px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5633_54576 .Pixso-symbol-5476_6639 {
    width: 200px;
    height: 32px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    align-items: flex-start;
}
.Pixso-instance-5634_55001 .Pixso-symbol-5476_6639 {
    width: 200px;
    height: 32px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    align-items: flex-start;
}
.Pixso-instance-5634_55567 .Pixso-symbol-5476_6639 {
    width: 200px;
    height: 32px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    align-items: flex-start;
}
.Pixso-instance-5634_57335 .Pixso-symbol-5476_6639 {
    width: 200px;
    height: 32px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    align-items: flex-start;
}
.Pixso-instance-5634_58347 .Pixso-symbol-5476_6639 {
    width: 200px;
    height: 32px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    align-items: flex-start;
}
.Pixso-instance-5634_57727 .Pixso-symbol-5476_6639 {
    width: 200px;
    height: 32px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    align-items: flex-start;
}
.Pixso-instance-5634_58389 .Pixso-symbol-5476_6639 {
    width: 200px;
    height: 32px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    align-items: flex-start;
}
.Pixso-instance-5634_56159 .Pixso-symbol-5476_6639 {
    width: 200px;
    height: 32px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    align-items: flex-start;
}
.Pixso-instance-5633_54576 .Pixso-instance-5476_6640 {
    width: 32px;
    height: 32px;
}
.Pixso-instance-5634_55001 .Pixso-instance-5476_6640 {
    width: 32px;
    height: 32px;
}
.Pixso-instance-5634_55567 .Pixso-instance-5476_6640 {
    width: 32px;
    height: 32px;
}
.Pixso-instance-5634_57335 .Pixso-instance-5476_6640 {
    width: 32px;
    height: 32px;
}
.Pixso-instance-5634_58347 .Pixso-instance-5476_6640 {
    width: 32px;
    height: 32px;
}
.Pixso-instance-5634_57727 .Pixso-instance-5476_6640 {
    width: 32px;
    height: 32px;
}
.Pixso-instance-5634_58389 .Pixso-instance-5476_6640 {
    width: 32px;
    height: 32px;
}
.Pixso-instance-5634_56159 .Pixso-instance-5476_6640 {
    width: 32px;
    height: 32px;
}
.Pixso-instance-5633_54576 .Pixso-instance-5476_6641 {
    width: 32px;
    height: 32px;
}
.Pixso-instance-5634_55001 .Pixso-instance-5476_6641 {
    width: 32px;
    height: 32px;
}
.Pixso-instance-5634_55567 .Pixso-instance-5476_6641 {
    width: 32px;
    height: 32px;
}
.Pixso-instance-5634_57335 .Pixso-instance-5476_6641 {
    width: 32px;
    height: 32px;
}
.Pixso-instance-5634_58347 .Pixso-instance-5476_6641 {
    width: 32px;
    height: 32px;
}
.Pixso-instance-5634_57727 .Pixso-instance-5476_6641 {
    width: 32px;
    height: 32px;
}
.Pixso-instance-5634_58389 .Pixso-instance-5476_6641 {
    width: 32px;
    height: 32px;
}
.Pixso-instance-5634_56159 .Pixso-instance-5476_6641 {
    width: 32px;
    height: 32px;
}
.Pixso-instance-5633_54576 .Pixso-instance-5476_6642 {
    width: 32px;
    height: 32px;
}
.Pixso-instance-5634_55001 .Pixso-instance-5476_6642 {
    width: 32px;
    height: 32px;
}
.Pixso-instance-5634_55567 .Pixso-instance-5476_6642 {
    width: 32px;
    height: 32px;
}
.Pixso-instance-5634_57335 .Pixso-instance-5476_6642 {
    width: 32px;
    height: 32px;
}
.Pixso-instance-5634_58347 .Pixso-instance-5476_6642 {
    width: 32px;
    height: 32px;
}
.Pixso-instance-5634_57727 .Pixso-instance-5476_6642 {
    width: 32px;
    height: 32px;
}
.Pixso-instance-5634_58389 .Pixso-instance-5476_6642 {
    width: 32px;
    height: 32px;
}
.Pixso-instance-5634_56159 .Pixso-instance-5476_6642 {
    width: 32px;
    height: 32px;
}
.Pixso-instance-5633_54576 .Pixso-instance-5476_6643 {
    width: 32px;
    height: 32px;
}
.Pixso-instance-5634_55001 .Pixso-instance-5476_6643 {
    width: 32px;
    height: 32px;
}
.Pixso-instance-5634_55567 .Pixso-instance-5476_6643 {
    width: 32px;
    height: 32px;
}
.Pixso-instance-5634_57335 .Pixso-instance-5476_6643 {
    width: 32px;
    height: 32px;
}
.Pixso-instance-5634_58347 .Pixso-instance-5476_6643 {
    width: 32px;
    height: 32px;
}
.Pixso-instance-5634_57727 .Pixso-instance-5476_6643 {
    width: 32px;
    height: 32px;
}
.Pixso-instance-5634_58389 .Pixso-instance-5476_6643 {
    width: 32px;
    height: 32px;
}
.Pixso-instance-5634_56159 .Pixso-instance-5476_6643 {
    width: 32px;
    height: 32px;
}
.Pixso-instance-5633_54576 .Pixso-instance-5476_6644 {
    width: 32px;
    height: 32px;
}
.Pixso-instance-5634_55001 .Pixso-instance-5476_6644 {
    width: 32px;
    height: 32px;
}
.Pixso-instance-5634_55567 .Pixso-instance-5476_6644 {
    width: 32px;
    height: 32px;
}
.Pixso-instance-5634_57335 .Pixso-instance-5476_6644 {
    width: 32px;
    height: 32px;
}
.Pixso-instance-5634_58347 .Pixso-instance-5476_6644 {
    width: 32px;
    height: 32px;
}
.Pixso-instance-5634_57727 .Pixso-instance-5476_6644 {
    width: 32px;
    height: 32px;
}
.Pixso-instance-5634_58389 .Pixso-instance-5476_6644 {
    width: 32px;
    height: 32px;
}
.Pixso-instance-5634_56159 .Pixso-instance-5476_6644 {
    width: 32px;
    height: 32px;
}
.Pixso-instance-5633_54576 .Pixso-instance-5476_6645 {
    width: 32px;
    height: 32px;
}
.Pixso-instance-5634_55001 .Pixso-instance-5476_6645 {
    width: 32px;
    height: 32px;
}
.Pixso-instance-5634_55567 .Pixso-instance-5476_6645 {
    width: 32px;
    height: 32px;
}
.Pixso-instance-5634_57335 .Pixso-instance-5476_6645 {
    width: 32px;
    height: 32px;
}
.Pixso-instance-5634_58347 .Pixso-instance-5476_6645 {
    width: 32px;
    height: 32px;
}
.Pixso-instance-5634_57727 .Pixso-instance-5476_6645 {
    width: 32px;
    height: 32px;
}
.Pixso-instance-5634_58389 .Pixso-instance-5476_6645 {
    width: 32px;
    height: 32px;
}
.Pixso-instance-5634_56159 .Pixso-instance-5476_6645 {
    width: 32px;
    height: 32px;
}
.Pixso-instance-5633_54576 .Pixso-instance-5476_6646 {
    width: 32px;
    height: 32px;
}
.Pixso-instance-5634_55001 .Pixso-instance-5476_6646 {
    width: 32px;
    height: 32px;
}
.Pixso-instance-5634_55567 .Pixso-instance-5476_6646 {
    width: 32px;
    height: 32px;
}
.Pixso-instance-5634_57335 .Pixso-instance-5476_6646 {
    width: 32px;
    height: 32px;
}
.Pixso-instance-5634_58347 .Pixso-instance-5476_6646 {
    width: 32px;
    height: 32px;
}
.Pixso-instance-5634_57727 .Pixso-instance-5476_6646 {
    width: 32px;
    height: 32px;
}
.Pixso-instance-5634_58389 .Pixso-instance-5476_6646 {
    width: 32px;
    height: 32px;
}
.Pixso-instance-5634_56159 .Pixso-instance-5476_6646 {
    width: 32px;
    height: 32px;
}
.Pixso-instance-5633_54576 .Pixso-instance-5476_6647 {
    width: 32px;
    height: 32px;
}
.Pixso-instance-5634_55001 .Pixso-instance-5476_6647 {
    width: 32px;
    height: 32px;
}
.Pixso-instance-5634_55567 .Pixso-instance-5476_6647 {
    width: 32px;
    height: 32px;
}
.Pixso-instance-5634_57335 .Pixso-instance-5476_6647 {
    width: 32px;
    height: 32px;
}
.Pixso-instance-5634_58347 .Pixso-instance-5476_6647 {
    width: 32px;
    height: 32px;
}
.Pixso-instance-5634_57727 .Pixso-instance-5476_6647 {
    width: 32px;
    height: 32px;
}
.Pixso-instance-5634_58389 .Pixso-instance-5476_6647 {
    width: 32px;
    height: 32px;
}
.Pixso-instance-5634_56159 .Pixso-instance-5476_6647 {
    width: 32px;
    height: 32px;
}
.Pixso-instance-5633_54355 .Pixso-symbol-5609_21323 {
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
.Pixso-instance-5633_54355 .stroke-wrapper-5609_21323 {
    width: 263px;
    height: 48px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5633_54355 .stroke-5609_21323 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_54998 .Pixso-symbol-5609_21323 {
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
.Pixso-instance-5634_54998 .stroke-wrapper-5609_21323 {
    width: 263px;
    height: 48px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5634_54998 .stroke-5609_21323 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_55564 .Pixso-symbol-5609_21323 {
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
.Pixso-instance-5634_55564 .stroke-wrapper-5609_21323 {
    width: 231px;
    height: 48px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5634_55564 .stroke-5609_21323 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_57331 .Pixso-symbol-5609_21323 {
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
.Pixso-instance-5634_57331 .stroke-wrapper-5609_21323 {
    width: 231px;
    height: 48px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5634_57331 .stroke-5609_21323 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_58343 .Pixso-symbol-5609_21323 {
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
.Pixso-instance-5634_58343 .stroke-wrapper-5609_21323 {
    width: 207px;
    height: 48px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5634_58343 .stroke-5609_21323 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_57723 .Pixso-symbol-5609_21323 {
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
.Pixso-instance-5634_57723 .stroke-wrapper-5609_21323 {
    width: 231px;
    height: 48px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5634_57723 .stroke-5609_21323 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_58385 .Pixso-symbol-5609_21323 {
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
.Pixso-instance-5634_58385 .stroke-wrapper-5609_21323 {
    width: 207px;
    height: 48px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5634_58385 .stroke-5609_21323 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5634_56155 .Pixso-symbol-5609_21323 {
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
.Pixso-instance-5634_56155 .stroke-wrapper-5609_21323 {
    width: 231px;
    height: 48px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5634_56155 .stroke-5609_21323 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5633_54355 .Pixso-frame-5609_21324 {
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
.Pixso-instance-5634_54998 .Pixso-frame-5609_21324 {
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
.Pixso-instance-5634_55564 .Pixso-frame-5609_21324 {
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
.Pixso-instance-5634_57331 .Pixso-frame-5609_21324 {
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
.Pixso-instance-5634_58343 .Pixso-frame-5609_21324 {
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
.Pixso-instance-5634_57723 .Pixso-frame-5609_21324 {
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
.Pixso-instance-5634_58385 .Pixso-frame-5609_21324 {
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
.Pixso-instance-5634_56155 .Pixso-frame-5609_21324 {
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
.Pixso-instance-5633_54355 .Pixso-instance-5609_21325 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5634_54998 .Pixso-instance-5609_21325 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5634_55564 .Pixso-instance-5609_21325 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5634_57331 .Pixso-instance-5609_21325 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5634_58343 .Pixso-instance-5609_21325 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5634_57723 .Pixso-instance-5609_21325 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5634_58385 .Pixso-instance-5609_21325 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5634_56155 .Pixso-instance-5609_21325 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5633_54355 .Pixso-paragraph-5609_21326 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5634_54998 .Pixso-paragraph-5609_21326 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5634_55564 .Pixso-paragraph-5609_21326 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5634_57331 .Pixso-paragraph-5609_21326 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5634_58343 .Pixso-paragraph-5609_21326 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5634_57723 .Pixso-paragraph-5609_21326 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5634_58385 .Pixso-paragraph-5609_21326 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5634_56155 .Pixso-paragraph-5609_21326 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5633_54355 .Pixso-instance-5609_21330 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5634_54998 .Pixso-instance-5609_21330 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5634_55564 .Pixso-instance-5609_21330 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5634_57331 .Pixso-instance-5609_21330 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5634_58343 .Pixso-instance-5609_21330 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5634_57723 .Pixso-instance-5609_21330 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5634_58385 .Pixso-instance-5609_21330 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5634_56155 .Pixso-instance-5609_21330 {
    width: 20px;
    height: 20px;
}
</style>
