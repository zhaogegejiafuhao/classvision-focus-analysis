<template>
    <div class="component-6359_30141">
        <div id="6359_30141" class="Pixso-symbol-6359_30141">
            <div
                id="6360_54099"
                class="Pixso-symbol-6360_54099 fill-gray0-white-67_3285"
                v-if="Theme === 'White' && Type === 'Progress Bar'"
            >
                <div id="6360_54100" class="Pixso-frame-6360_54100">
                    <div class="frame-content-6360_54100">
                        <div id="6360_54101" class="Pixso-frame-6360_54101">
                            <div class="frame-content-6360_54101">
                                <slot name="slot_6360_54102">
                                    <p
                                        id="6360_54102"
                                        class="Pixso-paragraph-6360_54102 fill-gray80-32_4123-paragraph text-text-smbold-423_3208"
                                    >
                                        {{ "Space  Almost Expired" }}
                                    </p>
                                </slot>
                                <slot name="slot_6360_54103">
                                    <p
                                        id="6360_54103"
                                        class="Pixso-paragraph-6360_54103 fill-gray60-83_2722-paragraph text-paragraphsm-20_2107"
                                    >
                                        {{
                                            "You’re running out of space. Please upgrade or go pro today."
                                        }}
                                    </p>
                                </slot>
                            </div>
                        </div>
                        <slot name="slot_6360_54104">
                            <X
                                id="6360_54104"
                                class="Pixso-instance-6360_54104"
                                Format="Outline"
                                Weight="Bold"
                            />
                        </slot>
                    </div>
                </div>
                <slot name="slot_6360_54105">
                    <ProgressBar
                        id="6360_54105"
                        class="Pixso-instance-6360_54105"
                        Progression="60"
                        Size="md"
                        Label="None"
                    />
                </slot>
                <div
                    id="6360_54106"
                    class="Pixso-frame-6360_54106"
                    v-if="visible_6359_3"
                >
                    <slot name="slot_6360_54107">
                        <Button
                            id="6360_54107"
                            class="Pixso-instance-6360_54107"
                            :visible_5588_131="false"
                            :visible_5588_152="false"
                            text_5588_173="Dismiss"
                            Size="md"
                            Color="Gray"
                            Hierarchy="Link"
                            State="Default"
                        >
                            <template #slot_5603_17111>
                                <p
                                    id="5603_17111"
                                    class="Pixso-paragraph-5603_17111 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                                >
                                    {{ "Dismiss" }}
                                </p>
                            </template>
                        </Button>
                    </slot>
                    <slot name="slot_6360_54108">
                        <Button
                            id="6360_54108"
                            class="Pixso-instance-6360_54108"
                            :visible_5588_131="false"
                            :visible_5588_152="false"
                            text_5588_173="Go Pro"
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
                                    {{ "Go Pro" }}
                                </p>
                            </template>
                        </Button>
                    </slot>
                </div>
            </div>
            <div
                id="6358_28279"
                class="Pixso-symbol-6358_28279 fill-gray5-32_4120"
                v-if="Theme === 'Light Gray' && Type === 'Progress Bar'"
            >
                <div id="6360_36834" class="Pixso-frame-6360_36834">
                    <div class="frame-content-6360_36834">
                        <div id="6358_21527" class="Pixso-frame-6358_21527">
                            <div class="frame-content-6358_21527">
                                <slot name="slot_6358_21525">
                                    <p
                                        id="6358_21525"
                                        class="Pixso-paragraph-6358_21525 fill-gray80-32_4123-paragraph text-text-smbold-423_3208"
                                    >
                                        {{ "Space  Almost Expired" }}
                                    </p>
                                </slot>
                                <slot name="slot_6358_21526">
                                    <p
                                        id="6358_21526"
                                        class="Pixso-paragraph-6358_21526 fill-gray60-83_2722-paragraph text-paragraphsm-20_2107"
                                    >
                                        {{
                                            "You’re running out of space. Please upgrade or go pro today."
                                        }}
                                    </p>
                                </slot>
                            </div>
                        </div>
                        <slot name="slot_6358_21528">
                            <X
                                id="6358_21528"
                                class="Pixso-instance-6358_21528"
                                Format="Outline"
                                Weight="Bold"
                            />
                        </slot>
                    </div>
                </div>
                <slot name="slot_6359_30127">
                    <ProgressBar
                        id="6359_30127"
                        class="Pixso-instance-6359_30127"
                        Progression="60"
                        Size="md"
                        Label="None"
                    />
                </slot>
                <div
                    id="6358_21580"
                    class="Pixso-frame-6358_21580"
                    v-if="visible_6359_3"
                >
                    <slot name="slot_6358_21562">
                        <Button
                            id="6358_21562"
                            class="Pixso-instance-6358_21562"
                            :visible_5588_131="false"
                            :visible_5588_152="false"
                            text_5588_173="Dismiss"
                            Size="md"
                            Color="Gray"
                            Hierarchy="Link"
                            State="Default"
                        >
                            <template #slot_5603_17111>
                                <p
                                    id="5603_17111"
                                    class="Pixso-paragraph-5603_17111 fill-gray60-83_2722-paragraph text-text-smbold-423_3208 fill-brand20-1257_33462-paragraph"
                                >
                                    {{ "Dismiss" }}
                                </p>
                            </template>
                        </Button>
                    </slot>
                    <slot name="slot_6358_21576">
                        <Button
                            id="6358_21576"
                            class="Pixso-instance-6358_21576"
                            :visible_5588_131="false"
                            :visible_5588_152="false"
                            text_5588_173="Go Pro"
                            Size="md"
                            Color="Brand"
                            Hierarchy="Link"
                            State="Default"
                        >
                            <template #slot_5603_17351>
                                <p
                                    id="5603_17351"
                                    class="Pixso-paragraph-5603_17351 fill-brand60-1257_33467-paragraph text-text-smbold-423_3208 fill-gray0-white-67_3285-paragraph"
                                >
                                    {{ "Go Pro" }}
                                </p>
                            </template>
                        </Button>
                    </slot>
                </div>
            </div>
            <div
                id="6359_30121"
                class="Pixso-symbol-6359_30121 fill-brand50-1257_33466"
                v-if="Theme === 'Brand' && Type === 'Progress Bar'"
            >
                <div id="6360_36835" class="Pixso-frame-6360_36835">
                    <div class="frame-content-6360_36835">
                        <div id="6359_30102" class="Pixso-frame-6359_30102">
                            <div class="frame-content-6359_30102">
                                <slot name="slot_6359_30103">
                                    <p
                                        id="6359_30103"
                                        class="Pixso-paragraph-6359_30103 fill-gray0-white-67_3285-paragraph text-text-smbold-423_3208"
                                    >
                                        {{ "Space  Almost Expired" }}
                                    </p>
                                </slot>
                                <slot name="slot_6359_30104">
                                    <p
                                        id="6359_30104"
                                        class="Pixso-paragraph-6359_30104 fill-brand10-1257_33461-paragraph text-paragraphsm-20_2107"
                                    >
                                        {{
                                            "You’re running out of space. Please upgrade or go pro today."
                                        }}
                                    </p>
                                </slot>
                            </div>
                        </div>
                        <slot name="slot_6359_30101">
                            <X
                                id="6359_30101"
                                class="Pixso-instance-6359_30101"
                                Format="Outline"
                                Weight="Bold"
                            />
                        </slot>
                    </div>
                </div>
                <slot name="slot_6359_30137">
                    <ProgressBar
                        id="6359_30137"
                        class="Pixso-instance-6359_30137"
                        Progression="60"
                        Size="md"
                        Label="None"
                    />
                </slot>
                <div
                    id="6359_30105"
                    class="Pixso-frame-6359_30105"
                    v-if="visible_6359_3"
                >
                    <slot name="slot_6359_30106">
                        <Button
                            id="6359_30106"
                            class="Pixso-instance-6359_30106"
                            :visible_5588_131="false"
                            :visible_5588_152="false"
                            text_5588_173="Dismiss"
                            Size="md"
                            Color="Gray"
                            Hierarchy="Link"
                            State="Default"
                        >
                            <template #slot_5603_17111>
                                <p
                                    id="5603_17111"
                                    class="Pixso-paragraph-5603_17111 fill-gray60-83_2722-paragraph text-text-smbold-423_3208 fill-gray30-35_1481-paragraph"
                                >
                                    {{ "Dismiss" }}
                                </p>
                            </template>
                        </Button>
                    </slot>
                    <slot name="slot_6359_30107">
                        <Button
                            id="6359_30107"
                            class="Pixso-instance-6359_30107"
                            :visible_5588_131="false"
                            :visible_5588_152="false"
                            text_5588_173="Go Pro"
                            Size="md"
                            Color="Brand"
                            Hierarchy="Link"
                            State="Default"
                        >
                            <template #slot_5603_17351>
                                <p
                                    id="5603_17351"
                                    class="Pixso-paragraph-5603_17351 fill-brand60-1257_33467-paragraph text-text-smbold-423_3208 fill-gray0-white-67_3285-paragraph"
                                >
                                    {{ "Go Pro" }}
                                </p>
                            </template>
                        </Button>
                    </slot>
                </div>
            </div>
            <div
                id="6360_54287"
                class="Pixso-symbol-6360_54287 fill-gray70-32_4121"
                v-if="Theme === 'Dark' && Type === 'Progress Bar'"
            >
                <div id="6360_54288" class="Pixso-frame-6360_54288">
                    <div class="frame-content-6360_54288">
                        <div id="6360_54289" class="Pixso-frame-6360_54289">
                            <div class="frame-content-6360_54289">
                                <slot name="slot_6360_54290">
                                    <p
                                        id="6360_54290"
                                        class="Pixso-paragraph-6360_54290 fill-gray0-white-67_3285-paragraph text-text-smbold-423_3208"
                                    >
                                        {{ "Space  Almost Expired" }}
                                    </p>
                                </slot>
                                <slot name="slot_6360_54291">
                                    <p
                                        id="6360_54291"
                                        class="Pixso-paragraph-6360_54291 fill-gray20-36_1844-paragraph text-paragraphsm-20_2107"
                                    >
                                        {{
                                            "You’re running out of space. Please upgrade or go pro today."
                                        }}
                                    </p>
                                </slot>
                            </div>
                        </div>
                        <slot name="slot_6360_54292">
                            <X
                                id="6360_54292"
                                class="Pixso-instance-6360_54292"
                                Format="Outline"
                                Weight="Bold"
                            />
                        </slot>
                    </div>
                </div>
                <slot name="slot_6360_54293">
                    <ProgressBar
                        id="6360_54293"
                        class="Pixso-instance-6360_54293"
                        Progression="60"
                        Size="md"
                        Label="None"
                    />
                </slot>
                <div
                    id="6360_54294"
                    class="Pixso-frame-6360_54294"
                    v-if="visible_6359_3"
                >
                    <slot name="slot_6360_54295">
                        <Button
                            id="6360_54295"
                            class="Pixso-instance-6360_54295"
                            :visible_5588_131="false"
                            :visible_5588_152="false"
                            text_5588_173="Dismiss"
                            Size="md"
                            Color="Gray"
                            Hierarchy="Link"
                            State="Default"
                        >
                            <template #slot_5603_17111>
                                <p
                                    id="5603_17111"
                                    class="Pixso-paragraph-5603_17111 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                                >
                                    {{ "Dismiss" }}
                                </p>
                            </template>
                        </Button>
                    </slot>
                    <slot name="slot_6360_54296">
                        <Button
                            id="6360_54296"
                            class="Pixso-instance-6360_54296"
                            :visible_5588_131="false"
                            :visible_5588_152="false"
                            text_5588_173="Go Pro"
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
                                    {{ "Go Pro" }}
                                </p>
                            </template>
                        </Button>
                    </slot>
                </div>
            </div>
            <div
                id="6360_54119"
                class="Pixso-symbol-6360_54119 fill-gray0-white-67_3285"
                v-if="Theme === 'White' && Type === 'Pricing'"
            >
                <div id="6360_54120" class="Pixso-frame-6360_54120">
                    <div class="frame-content-6360_54120">
                        <div id="6360_54121" class="Pixso-frame-6360_54121">
                            <div class="frame-content-6360_54121">
                                <slot name="slot_6360_54122">
                                    <p
                                        id="6360_54122"
                                        class="Pixso-paragraph-6360_54122 fill-gray80-32_4123-paragraph text-text-smbold-423_3208"
                                    >
                                        {{ "Pro Plan" }}
                                    </p>
                                </slot>
                                <div
                                    id="6360_54123"
                                    class="Pixso-frame-6360_54123"
                                >
                                    <div class="frame-content-6360_54123">
                                        <slot name="slot_6360_54124">
                                            <p
                                                id="6360_54124"
                                                class="Pixso-paragraph-6360_54124 fill-gray80-32_4123-paragraph text-heading-smextrabold-423_3188"
                                            >
                                                {{ "$15.99" }}
                                            </p>
                                        </slot>
                                        <div
                                            id="6360_54125"
                                            class="Pixso-frame-6360_54125"
                                        >
                                            <slot name="slot_6360_54126">
                                                <p
                                                    id="6360_54126"
                                                    class="Pixso-paragraph-6360_54126 fill-gray60-83_2722-paragraph text-text-mdmedium-5454_21606"
                                                >
                                                    {{ "/mo" }}
                                                </p>
                                            </slot>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <slot name="slot_6360_54127">
                            <X
                                id="6360_54127"
                                class="Pixso-instance-6360_54127"
                                Format="Outline"
                                Weight="Bold"
                            />
                        </slot>
                    </div>
                </div>
                <slot name="slot_6360_54128">
                    <p
                        id="6360_54128"
                        class="Pixso-paragraph-6360_54128 fill-gray60-83_2722-paragraph text-paragraphsm-20_2107"
                    >
                        {{
                            "Enjoy unlimited access to our app with only a small price monthly."
                        }}
                    </p>
                </slot>
                <div
                    id="6360_54129"
                    class="Pixso-frame-6360_54129"
                    v-if="visible_6359_3"
                >
                    <slot name="slot_6360_54130">
                        <Button
                            id="6360_54130"
                            class="Pixso-instance-6360_54130"
                            :visible_5588_131="false"
                            :visible_5588_152="false"
                            text_5588_173="Dismiss"
                            Size="md"
                            Color="Gray"
                            Hierarchy="Link"
                            State="Default"
                        >
                            <template #slot_5603_17111>
                                <p
                                    id="5603_17111"
                                    class="Pixso-paragraph-5603_17111 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                                >
                                    {{ "Dismiss" }}
                                </p>
                            </template>
                        </Button>
                    </slot>
                    <slot name="slot_6360_54131">
                        <Button
                            id="6360_54131"
                            class="Pixso-instance-6360_54131"
                            :visible_5588_131="false"
                            :visible_5588_152="false"
                            text_5588_173="Go Pro"
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
                                    {{ "Go Pro" }}
                                </p>
                            </template>
                        </Button>
                    </slot>
                </div>
            </div>
            <div
                id="6359_35279"
                class="Pixso-symbol-6359_35279 fill-gray5-32_4120"
                v-if="Theme === 'Light Gray' && Type === 'Pricing'"
            >
                <div id="6359_36831" class="Pixso-frame-6359_36831">
                    <div class="frame-content-6359_36831">
                        <div id="6359_36832" class="Pixso-frame-6359_36832">
                            <div class="frame-content-6359_36832">
                                <slot name="slot_6359_35282">
                                    <p
                                        id="6359_35282"
                                        class="Pixso-paragraph-6359_35282 fill-gray80-32_4123-paragraph text-text-smbold-423_3208"
                                    >
                                        {{ "Pro Plan" }}
                                    </p>
                                </slot>
                                <div
                                    id="6359_35322"
                                    class="Pixso-frame-6359_35322"
                                >
                                    <div class="frame-content-6359_35322">
                                        <slot name="slot_6359_35283">
                                            <p
                                                id="6359_35283"
                                                class="Pixso-paragraph-6359_35283 fill-gray80-32_4123-paragraph text-heading-smextrabold-423_3188"
                                            >
                                                {{ "$15.99" }}
                                            </p>
                                        </slot>
                                        <div
                                            id="6359_36289"
                                            class="Pixso-frame-6359_36289"
                                        >
                                            <slot name="slot_6359_35321">
                                                <p
                                                    id="6359_35321"
                                                    class="Pixso-paragraph-6359_35321 fill-gray60-83_2722-paragraph text-text-mdmedium-5454_21606"
                                                >
                                                    {{ "/mo" }}
                                                </p>
                                            </slot>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <slot name="slot_6359_35284">
                            <X
                                id="6359_35284"
                                class="Pixso-instance-6359_35284"
                                Format="Outline"
                                Weight="Bold"
                            />
                        </slot>
                    </div>
                </div>
                <slot name="slot_6359_36833">
                    <p
                        id="6359_36833"
                        class="Pixso-paragraph-6359_36833 fill-gray60-83_2722-paragraph text-paragraphsm-20_2107"
                    >
                        {{
                            "Enjoy unlimited access to our app with only a small price monthly."
                        }}
                    </p>
                </slot>
                <div
                    id="6359_35286"
                    class="Pixso-frame-6359_35286"
                    v-if="visible_6359_3"
                >
                    <slot name="slot_6359_35287">
                        <Button
                            id="6359_35287"
                            class="Pixso-instance-6359_35287"
                            :visible_5588_131="false"
                            :visible_5588_152="false"
                            text_5588_173="Dismiss"
                            Size="md"
                            Color="Gray"
                            Hierarchy="Link"
                            State="Default"
                        >
                            <template #slot_5603_17111>
                                <p
                                    id="5603_17111"
                                    class="Pixso-paragraph-5603_17111 fill-gray60-83_2722-paragraph text-text-smbold-423_3208 fill-brand20-1257_33462-paragraph"
                                >
                                    {{ "Dismiss" }}
                                </p>
                            </template>
                        </Button>
                    </slot>
                    <slot name="slot_6359_35288">
                        <Button
                            id="6359_35288"
                            class="Pixso-instance-6359_35288"
                            :visible_5588_131="false"
                            :visible_5588_152="false"
                            text_5588_173="Go Pro"
                            Size="md"
                            Color="Brand"
                            Hierarchy="Link"
                            State="Default"
                        >
                            <template #slot_5603_17351>
                                <p
                                    id="5603_17351"
                                    class="Pixso-paragraph-5603_17351 fill-brand60-1257_33467-paragraph text-text-smbold-423_3208 fill-gray0-white-67_3285-paragraph"
                                >
                                    {{ "Go Pro" }}
                                </p>
                            </template>
                        </Button>
                    </slot>
                </div>
            </div>
            <div
                id="6360_36856"
                class="Pixso-symbol-6360_36856 fill-brand50-1257_33466"
                v-if="Theme === 'Brand' && Type === 'Pricing'"
            >
                <div id="6360_36857" class="Pixso-frame-6360_36857">
                    <div class="frame-content-6360_36857">
                        <div id="6360_36858" class="Pixso-frame-6360_36858">
                            <div class="frame-content-6360_36858">
                                <slot name="slot_6360_36859">
                                    <p
                                        id="6360_36859"
                                        class="Pixso-paragraph-6360_36859 fill-gray0-white-67_3285-paragraph text-text-smbold-423_3208"
                                    >
                                        {{ "Pro Plan" }}
                                    </p>
                                </slot>
                                <div
                                    id="6360_36860"
                                    class="Pixso-frame-6360_36860"
                                >
                                    <div class="frame-content-6360_36860">
                                        <slot name="slot_6360_36861">
                                            <p
                                                id="6360_36861"
                                                class="Pixso-paragraph-6360_36861 fill-gray0-white-67_3285-paragraph text-heading-smextrabold-423_3188"
                                            >
                                                {{ "$15.99" }}
                                            </p>
                                        </slot>
                                        <div
                                            id="6360_36862"
                                            class="Pixso-frame-6360_36862"
                                        >
                                            <slot name="slot_6360_36863">
                                                <p
                                                    id="6360_36863"
                                                    class="Pixso-paragraph-6360_36863 fill-gray0-white-67_3285-paragraph text-text-mdmedium-5454_21606"
                                                >
                                                    {{ "/mo" }}
                                                </p>
                                            </slot>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <slot name="slot_6360_36864">
                            <X
                                id="6360_36864"
                                class="Pixso-instance-6360_36864"
                                Format="Outline"
                                Weight="Bold"
                            />
                        </slot>
                    </div>
                </div>
                <slot name="slot_6360_36865">
                    <p
                        id="6360_36865"
                        class="Pixso-paragraph-6360_36865 fill-brand10-1257_33461-paragraph text-paragraphsm-20_2107"
                    >
                        {{
                            "Enjoy unlimited access to our app with only a small price monthly."
                        }}
                    </p>
                </slot>
                <div
                    id="6360_36866"
                    class="Pixso-frame-6360_36866"
                    v-if="visible_6359_3"
                >
                    <slot name="slot_6360_36867">
                        <Button
                            id="6360_36867"
                            class="Pixso-instance-6360_36867"
                            :visible_5588_131="false"
                            :visible_5588_152="false"
                            text_5588_173="Dismiss"
                            Size="md"
                            Color="Gray"
                            Hierarchy="Link"
                            State="Default"
                        >
                            <template #slot_5603_17111>
                                <p
                                    id="5603_17111"
                                    class="Pixso-paragraph-5603_17111 fill-gray60-83_2722-paragraph text-text-smbold-423_3208 fill-gray30-35_1481-paragraph"
                                >
                                    {{ "Dismiss" }}
                                </p>
                            </template>
                        </Button>
                    </slot>
                    <slot name="slot_6360_36868">
                        <Button
                            id="6360_36868"
                            class="Pixso-instance-6360_36868"
                            :visible_5588_131="false"
                            :visible_5588_152="false"
                            text_5588_173="Go Pro"
                            Size="md"
                            Color="Brand"
                            Hierarchy="Link"
                            State="Default"
                        >
                            <template #slot_5603_17351>
                                <p
                                    id="5603_17351"
                                    class="Pixso-paragraph-5603_17351 fill-brand60-1257_33467-paragraph text-text-smbold-423_3208 fill-gray0-white-67_3285-paragraph"
                                >
                                    {{ "Go Pro" }}
                                </p>
                            </template>
                        </Button>
                    </slot>
                </div>
            </div>
            <div
                id="6360_54307"
                class="Pixso-symbol-6360_54307 fill-gray70-32_4121"
                v-if="Theme === 'Dark' && Type === 'Pricing'"
            >
                <div id="6360_54308" class="Pixso-frame-6360_54308">
                    <div class="frame-content-6360_54308">
                        <div id="6360_54309" class="Pixso-frame-6360_54309">
                            <div class="frame-content-6360_54309">
                                <slot name="slot_6360_54310">
                                    <p
                                        id="6360_54310"
                                        class="Pixso-paragraph-6360_54310 fill-gray0-white-67_3285-paragraph text-text-smbold-423_3208"
                                    >
                                        {{ "Pro Plan" }}
                                    </p>
                                </slot>
                                <div
                                    id="6360_54311"
                                    class="Pixso-frame-6360_54311"
                                >
                                    <div class="frame-content-6360_54311">
                                        <slot name="slot_6360_54312">
                                            <p
                                                id="6360_54312"
                                                class="Pixso-paragraph-6360_54312 fill-gray0-white-67_3285-paragraph text-heading-smextrabold-423_3188"
                                            >
                                                {{ "$15.99" }}
                                            </p>
                                        </slot>
                                        <div
                                            id="6360_54313"
                                            class="Pixso-frame-6360_54313"
                                        >
                                            <slot name="slot_6360_54314">
                                                <p
                                                    id="6360_54314"
                                                    class="Pixso-paragraph-6360_54314 fill-gray0-white-67_3285-paragraph text-text-mdmedium-5454_21606"
                                                >
                                                    {{ "/mo" }}
                                                </p>
                                            </slot>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <slot name="slot_6360_54315">
                            <X
                                id="6360_54315"
                                class="Pixso-instance-6360_54315"
                                Format="Outline"
                                Weight="Bold"
                            />
                        </slot>
                    </div>
                </div>
                <slot name="slot_6360_54316">
                    <p
                        id="6360_54316"
                        class="Pixso-paragraph-6360_54316 fill-gray20-36_1844-paragraph text-paragraphsm-20_2107"
                    >
                        {{
                            "Enjoy unlimited access to our app with only a small price monthly."
                        }}
                    </p>
                </slot>
                <div
                    id="6360_54317"
                    class="Pixso-frame-6360_54317"
                    v-if="visible_6359_3"
                >
                    <slot name="slot_6360_54318">
                        <Button
                            id="6360_54318"
                            class="Pixso-instance-6360_54318"
                            :visible_5588_131="false"
                            :visible_5588_152="false"
                            text_5588_173="Dismiss"
                            Size="md"
                            Color="Gray"
                            Hierarchy="Link"
                            State="Default"
                        >
                            <template #slot_5603_17111>
                                <p
                                    id="5603_17111"
                                    class="Pixso-paragraph-5603_17111 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                                >
                                    {{ "Dismiss" }}
                                </p>
                            </template>
                        </Button>
                    </slot>
                    <slot name="slot_6360_54319">
                        <Button
                            id="6360_54319"
                            class="Pixso-instance-6360_54319"
                            :visible_5588_131="false"
                            :visible_5588_152="false"
                            text_5588_173="Go Pro"
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
                                    {{ "Go Pro" }}
                                </p>
                            </template>
                        </Button>
                    </slot>
                </div>
            </div>
            <div
                id="6360_54132"
                class="Pixso-symbol-6360_54132 fill-gray0-white-67_3285"
                v-if="Theme === 'White' && Type === 'Icon'"
            >
                <div id="6360_54133" class="Pixso-frame-6360_54133">
                    <div class="frame-content-6360_54133">
                        <div id="6360_54134" class="Pixso-frame-6360_54134">
                            <div class="frame-content-6360_54134">
                                <slot name="slot_6360_54135">
                                    <IconContainer
                                        id="6360_54135"
                                        class="Pixso-instance-6360_54135"
                                        Size="md"
                                        Color="Gray"
                                        Style="Secondary"
                                    >
                                        <template #slot_5546_2449>
                                            <Warning
                                                id="5546_2449"
                                                class="Pixso-instance-5546_2449"
                                            />
                                        </template>
                                    </IconContainer>
                                </slot>
                            </div>
                        </div>
                        <slot name="slot_6360_54136">
                            <X
                                id="6360_54136"
                                class="Pixso-instance-6360_54136"
                                Format="Outline"
                                Weight="Bold"
                            />
                        </slot>
                    </div>
                </div>
                <slot name="slot_6360_54137">
                    <p
                        id="6360_54137"
                        class="Pixso-paragraph-6360_54137 fill-gray60-83_2722-paragraph text-paragraphsm-20_2107"
                    >
                        {{
                            "Enjoy unlimited access to our app with only a small price monthly."
                        }}
                    </p>
                </slot>
                <div
                    id="6360_54138"
                    class="Pixso-frame-6360_54138"
                    v-if="visible_6359_3"
                >
                    <slot name="slot_6360_54139">
                        <Button
                            id="6360_54139"
                            class="Pixso-instance-6360_54139"
                            :visible_5588_131="false"
                            :visible_5588_152="false"
                            text_5588_173="Dismiss"
                            Size="md"
                            Color="Gray"
                            Hierarchy="Link"
                            State="Default"
                        >
                            <template #slot_5603_17111>
                                <p
                                    id="5603_17111"
                                    class="Pixso-paragraph-5603_17111 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                                >
                                    {{ "Dismiss" }}
                                </p>
                            </template>
                        </Button>
                    </slot>
                    <slot name="slot_6360_54140">
                        <Button
                            id="6360_54140"
                            class="Pixso-instance-6360_54140"
                            :visible_5588_131="false"
                            :visible_5588_152="false"
                            text_5588_173="Go Pro"
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
                                    {{ "Go Pro" }}
                                </p>
                            </template>
                        </Button>
                    </slot>
                </div>
            </div>
            <div
                id="6360_36880"
                class="Pixso-symbol-6360_36880 fill-gray5-32_4120"
                v-if="Theme === 'Light Gray' && Type === 'Icon'"
            >
                <div id="6360_36881" class="Pixso-frame-6360_36881">
                    <div class="frame-content-6360_36881">
                        <div id="6360_36904" class="Pixso-frame-6360_36904">
                            <div class="frame-content-6360_36904">
                                <slot name="slot_6358_22757">
                                    <IconContainer
                                        id="6358_22757"
                                        class="Pixso-instance-6358_22757"
                                        Size="md"
                                        Color="Gray"
                                        Style="Secondary"
                                    >
                                        <template #slot_5546_2449>
                                            <Warning
                                                id="5546_2449"
                                                class="Pixso-instance-5546_2449"
                                            />
                                        </template>
                                    </IconContainer>
                                </slot>
                            </div>
                        </div>
                        <slot name="slot_6360_36888">
                            <X
                                id="6360_36888"
                                class="Pixso-instance-6360_36888"
                                Format="Outline"
                                Weight="Bold"
                            />
                        </slot>
                    </div>
                </div>
                <slot name="slot_6360_36889">
                    <p
                        id="6360_36889"
                        class="Pixso-paragraph-6360_36889 fill-gray60-83_2722-paragraph text-paragraphsm-20_2107"
                    >
                        {{
                            "Enjoy unlimited access to our app with only a small price monthly."
                        }}
                    </p>
                </slot>
                <div
                    id="6360_36890"
                    class="Pixso-frame-6360_36890"
                    v-if="visible_6359_3"
                >
                    <slot name="slot_6360_36891">
                        <Button
                            id="6360_36891"
                            class="Pixso-instance-6360_36891"
                            :visible_5588_131="false"
                            :visible_5588_152="false"
                            text_5588_173="Dismiss"
                            Size="md"
                            Color="Gray"
                            Hierarchy="Link"
                            State="Default"
                        >
                            <template #slot_5603_17111>
                                <p
                                    id="5603_17111"
                                    class="Pixso-paragraph-5603_17111 fill-gray60-83_2722-paragraph text-text-smbold-423_3208 fill-brand20-1257_33462-paragraph"
                                >
                                    {{ "Dismiss" }}
                                </p>
                            </template>
                        </Button>
                    </slot>
                    <slot name="slot_6360_36892">
                        <Button
                            id="6360_36892"
                            class="Pixso-instance-6360_36892"
                            :visible_5588_131="false"
                            :visible_5588_152="false"
                            text_5588_173="Go Pro"
                            Size="md"
                            Color="Brand"
                            Hierarchy="Link"
                            State="Default"
                        >
                            <template #slot_5603_17351>
                                <p
                                    id="5603_17351"
                                    class="Pixso-paragraph-5603_17351 fill-brand60-1257_33467-paragraph text-text-smbold-423_3208 fill-gray0-white-67_3285-paragraph"
                                >
                                    {{ "Go Pro" }}
                                </p>
                            </template>
                        </Button>
                    </slot>
                </div>
            </div>
            <div
                id="6360_36905"
                class="Pixso-symbol-6360_36905 fill-brand50-1257_33466"
                v-if="Theme === 'Brand' && Type === 'Icon'"
            >
                <div id="6360_36906" class="Pixso-frame-6360_36906">
                    <div class="frame-content-6360_36906">
                        <div id="6360_36907" class="Pixso-frame-6360_36907">
                            <div class="frame-content-6360_36907">
                                <slot name="slot_6359_30100">
                                    <IconContainer
                                        id="6359_30100"
                                        class="Pixso-instance-6359_30100"
                                        Size="md"
                                        Color="Gray"
                                        Style="Secondary"
                                    >
                                        <template #slot_5546_2449>
                                            <Warning
                                                id="5546_2449"
                                                class="Pixso-instance-5546_2449"
                                            />
                                        </template>
                                    </IconContainer>
                                </slot>
                            </div>
                        </div>
                        <slot name="slot_6360_36909">
                            <X
                                id="6360_36909"
                                class="Pixso-instance-6360_36909"
                                Format="Outline"
                                Weight="Bold"
                            />
                        </slot>
                    </div>
                </div>
                <slot name="slot_6360_36910">
                    <p
                        id="6360_36910"
                        class="Pixso-paragraph-6360_36910 fill-brand10-1257_33461-paragraph text-paragraphsm-20_2107"
                    >
                        {{
                            "Enjoy unlimited access to our app with only a small price monthly."
                        }}
                    </p>
                </slot>
                <div
                    id="6360_36911"
                    class="Pixso-frame-6360_36911"
                    v-if="visible_6359_3"
                >
                    <slot name="slot_6360_36912">
                        <Button
                            id="6360_36912"
                            class="Pixso-instance-6360_36912"
                            :visible_5588_131="false"
                            :visible_5588_152="false"
                            text_5588_173="Dismiss"
                            Size="md"
                            Color="Gray"
                            Hierarchy="Link"
                            State="Default"
                        >
                            <template #slot_5603_17111>
                                <p
                                    id="5603_17111"
                                    class="Pixso-paragraph-5603_17111 fill-gray60-83_2722-paragraph text-text-smbold-423_3208 fill-gray30-35_1481-paragraph"
                                >
                                    {{ "Dismiss" }}
                                </p>
                            </template>
                        </Button>
                    </slot>
                    <slot name="slot_6360_36913">
                        <Button
                            id="6360_36913"
                            class="Pixso-instance-6360_36913"
                            :visible_5588_131="false"
                            :visible_5588_152="false"
                            text_5588_173="Go Pro"
                            Size="md"
                            Color="Brand"
                            Hierarchy="Link"
                            State="Default"
                        >
                            <template #slot_5603_17351>
                                <p
                                    id="5603_17351"
                                    class="Pixso-paragraph-5603_17351 fill-brand60-1257_33467-paragraph text-text-smbold-423_3208 fill-gray0-white-67_3285-paragraph"
                                >
                                    {{ "Go Pro" }}
                                </p>
                            </template>
                        </Button>
                    </slot>
                </div>
            </div>
            <div
                id="6360_54320"
                class="Pixso-symbol-6360_54320 fill-gray70-32_4121"
                v-if="Theme === 'Dark' && Type === 'Icon'"
            >
                <div id="6360_54321" class="Pixso-frame-6360_54321">
                    <div class="frame-content-6360_54321">
                        <div id="6360_54322" class="Pixso-frame-6360_54322">
                            <div class="frame-content-6360_54322">
                                <slot name="slot_6360_54323">
                                    <IconContainer
                                        id="6360_54323"
                                        class="Pixso-instance-6360_54323"
                                        Size="md"
                                        Color="Gray"
                                        Style="Secondary"
                                    >
                                        <template #slot_5546_2449>
                                            <Warning
                                                id="5546_2449"
                                                class="Pixso-instance-5546_2449"
                                            />
                                        </template>
                                    </IconContainer>
                                </slot>
                            </div>
                        </div>
                        <slot name="slot_6360_54324">
                            <X
                                id="6360_54324"
                                class="Pixso-instance-6360_54324"
                                Format="Outline"
                                Weight="Bold"
                            />
                        </slot>
                    </div>
                </div>
                <slot name="slot_6360_54325">
                    <p
                        id="6360_54325"
                        class="Pixso-paragraph-6360_54325 fill-gray20-36_1844-paragraph text-paragraphsm-20_2107"
                    >
                        {{
                            "Enjoy unlimited access to our app with only a small price monthly."
                        }}
                    </p>
                </slot>
                <div
                    id="6360_54326"
                    class="Pixso-frame-6360_54326"
                    v-if="visible_6359_3"
                >
                    <slot name="slot_6360_54327">
                        <Button
                            id="6360_54327"
                            class="Pixso-instance-6360_54327"
                            :visible_5588_131="false"
                            :visible_5588_152="false"
                            text_5588_173="Dismiss"
                            Size="md"
                            Color="Gray"
                            Hierarchy="Link"
                            State="Default"
                        >
                            <template #slot_5603_17111>
                                <p
                                    id="5603_17111"
                                    class="Pixso-paragraph-5603_17111 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                                >
                                    {{ "Dismiss" }}
                                </p>
                            </template>
                        </Button>
                    </slot>
                    <slot name="slot_6360_54328">
                        <Button
                            id="6360_54328"
                            class="Pixso-instance-6360_54328"
                            :visible_5588_131="false"
                            :visible_5588_152="false"
                            text_5588_173="Go Pro"
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
                                    {{ "Go Pro" }}
                                </p>
                            </template>
                        </Button>
                    </slot>
                </div>
            </div>
        </div>
    </div>
</template>
<script lang="ts" setup>
import X from "@/components/X.vue";
import ProgressBar from "@/components/Progressbar.vue";
import Button from "@/components/Button.vue";
import IconContainer from "@/components/Iconcontainer.vue";
import Warning from "@/components/Warning.vue";
const props = defineProps({
    visible_6359_3: { type: Boolean, default: true },
    Theme: { type: String },
    Type: { type: String }
});
</script>
<style>
.Pixso-symbol-6359_30141 {
}
.Pixso-symbol-6360_54099 {
    width: 280px;
    height: auto;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 16px;
    align-items: flex-start;
    padding: 16px 16px 16px 16px;
    border-radius: 24px 24px 24px 24px;
}
.Pixso-frame-6360_54100 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    align-items: flex-start;
}
.frame-content-6360_54100 {
    display: flex;
    flex-direction: row;
    gap: 16px;
    align-items: flex-start;
    width: 100%;
    position: relative;
}
.Pixso-frame-6360_54101 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    flex-grow: 1;
    flex-basis: 0;
}
.frame-content-6360_54101 {
    display: flex;
    flex-direction: column;
    gap: 4px;
    align-items: flex-start;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-6360_54102 {
    white-space: pre-wrap;
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-paragraph-6360_54103 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-6360_54104 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-6360_54105 {
    width: 248px;
    height: 8px;
}
.Pixso-frame-6360_54106 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 16px;
    align-items: flex-start;
}
.Pixso-instance-6360_54107 {
    width: 52px;
    height: 20px;
}
.Pixso-paragraph-5603_17111 {
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    width: auto;
    height: auto;
    flex-grow: 0;
}
.Pixso-instance-6360_54108 {
    width: 46px;
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
.Pixso-symbol-6358_28279 {
    width: 280px;
    height: auto;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 16px;
    align-items: flex-start;
    padding: 16px 16px 16px 16px;
    border-radius: 24px 24px 24px 24px;
}
.Pixso-frame-6360_36834 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    align-items: flex-start;
}
.frame-content-6360_36834 {
    display: flex;
    flex-direction: row;
    gap: 16px;
    align-items: flex-start;
    width: 100%;
    position: relative;
}
.Pixso-frame-6358_21527 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    flex-grow: 1;
    flex-basis: 0;
}
.frame-content-6358_21527 {
    display: flex;
    flex-direction: column;
    gap: 4px;
    align-items: flex-start;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-6358_21525 {
    white-space: pre-wrap;
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-paragraph-6358_21526 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-6358_21528 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-6359_30127 {
    width: 248px;
    height: 8px;
}
.Pixso-frame-6358_21580 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 16px;
    align-items: flex-start;
}
.Pixso-instance-6358_21562 {
    width: 52px;
    height: 20px;
}
.Pixso-instance-6358_21576 {
    width: 46px;
    height: 20px;
}
.Pixso-symbol-6359_30121 {
    width: 280px;
    height: auto;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 16px;
    align-items: flex-start;
    padding: 16px 16px 16px 16px;
    border-radius: 24px 24px 24px 24px;
}
.Pixso-frame-6360_36835 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    align-items: flex-start;
}
.frame-content-6360_36835 {
    display: flex;
    flex-direction: row;
    gap: 16px;
    align-items: flex-start;
    width: 100%;
    position: relative;
}
.Pixso-frame-6359_30102 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    flex-grow: 1;
    flex-basis: 0;
}
.frame-content-6359_30102 {
    display: flex;
    flex-direction: column;
    gap: 4px;
    align-items: flex-start;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-6359_30103 {
    white-space: pre-wrap;
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-paragraph-6359_30104 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-6359_30101 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-6359_30137 {
    width: 248px;
    height: 8px;
}
.Pixso-frame-6359_30105 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 16px;
    align-items: flex-start;
}
.Pixso-instance-6359_30106 {
    width: 52px;
    height: 20px;
}
.Pixso-instance-6359_30107 {
    width: 46px;
    height: 20px;
}
.Pixso-symbol-6360_54287 {
    width: 280px;
    height: auto;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 16px;
    align-items: flex-start;
    padding: 16px 16px 16px 16px;
    border-radius: 24px 24px 24px 24px;
}
.Pixso-frame-6360_54288 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    align-items: flex-start;
}
.frame-content-6360_54288 {
    display: flex;
    flex-direction: row;
    gap: 16px;
    align-items: flex-start;
    width: 100%;
    position: relative;
}
.Pixso-frame-6360_54289 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    flex-grow: 1;
    flex-basis: 0;
}
.frame-content-6360_54289 {
    display: flex;
    flex-direction: column;
    gap: 4px;
    align-items: flex-start;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-6360_54290 {
    white-space: pre-wrap;
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-paragraph-6360_54291 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-6360_54292 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-6360_54293 {
    width: 248px;
    height: 8px;
}
.Pixso-frame-6360_54294 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 16px;
    align-items: flex-start;
}
.Pixso-instance-6360_54295 {
    width: 52px;
    height: 20px;
}
.Pixso-instance-6360_54296 {
    width: 46px;
    height: 20px;
}
.Pixso-symbol-6360_54119 {
    width: 280px;
    height: auto;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 16px;
    align-items: flex-start;
    padding: 16px 16px 16px 16px;
    border-radius: 24px 24px 24px 24px;
}
.Pixso-frame-6360_54120 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    align-items: flex-start;
}
.frame-content-6360_54120 {
    display: flex;
    flex-direction: row;
    gap: 16px;
    align-items: flex-start;
    width: 100%;
    position: relative;
}
.Pixso-frame-6360_54121 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    flex-grow: 1;
    flex-basis: 0;
}
.frame-content-6360_54121 {
    display: flex;
    flex-direction: column;
    gap: 4px;
    align-items: flex-start;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-6360_54122 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-frame-6360_54123 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    align-items: flex-end;
}
.frame-content-6360_54123 {
    display: flex;
    flex-direction: row;
    align-items: flex-end;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-6360_54124 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-frame-6360_54125 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 10px;
    align-items: flex-end;
    padding: 0px 0px 3px 0px;
}
.Pixso-paragraph-6360_54126 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-6360_54127 {
    width: 20px;
    height: 20px;
}
.Pixso-paragraph-6360_54128 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-frame-6360_54129 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 16px;
    align-items: flex-start;
}
.Pixso-instance-6360_54130 {
    width: 52px;
    height: 20px;
}
.Pixso-instance-6360_54131 {
    width: 46px;
    height: 20px;
}
.Pixso-symbol-6359_35279 {
    width: 280px;
    height: auto;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 16px;
    align-items: flex-start;
    padding: 16px 16px 16px 16px;
    border-radius: 24px 24px 24px 24px;
}
.Pixso-frame-6359_36831 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    align-items: flex-start;
}
.frame-content-6359_36831 {
    display: flex;
    flex-direction: row;
    gap: 16px;
    align-items: flex-start;
    width: 100%;
    position: relative;
}
.Pixso-frame-6359_36832 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    flex-grow: 1;
    flex-basis: 0;
}
.frame-content-6359_36832 {
    display: flex;
    flex-direction: column;
    gap: 4px;
    align-items: flex-start;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-6359_35282 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-frame-6359_35322 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    align-items: flex-end;
}
.frame-content-6359_35322 {
    display: flex;
    flex-direction: row;
    align-items: flex-end;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-6359_35283 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-frame-6359_36289 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 10px;
    align-items: flex-end;
    padding: 0px 0px 3px 0px;
}
.Pixso-paragraph-6359_35321 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-6359_35284 {
    width: 20px;
    height: 20px;
}
.Pixso-paragraph-6359_36833 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-frame-6359_35286 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 16px;
    align-items: flex-start;
}
.Pixso-instance-6359_35287 {
    width: 52px;
    height: 20px;
}
.Pixso-instance-6359_35288 {
    width: 46px;
    height: 20px;
}
.Pixso-symbol-6360_36856 {
    width: 280px;
    height: auto;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 16px;
    align-items: flex-start;
    padding: 16px 16px 16px 16px;
    border-radius: 24px 24px 24px 24px;
}
.Pixso-frame-6360_36857 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    align-items: flex-start;
}
.frame-content-6360_36857 {
    display: flex;
    flex-direction: row;
    gap: 16px;
    align-items: flex-start;
    width: 100%;
    position: relative;
}
.Pixso-frame-6360_36858 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    flex-grow: 1;
    flex-basis: 0;
}
.frame-content-6360_36858 {
    display: flex;
    flex-direction: column;
    gap: 4px;
    align-items: flex-start;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-6360_36859 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-frame-6360_36860 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    align-items: flex-end;
}
.frame-content-6360_36860 {
    display: flex;
    flex-direction: row;
    align-items: flex-end;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-6360_36861 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-frame-6360_36862 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 10px;
    align-items: flex-end;
    padding: 0px 0px 3px 0px;
}
.Pixso-paragraph-6360_36863 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-6360_36864 {
    width: 20px;
    height: 20px;
}
.Pixso-paragraph-6360_36865 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-frame-6360_36866 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 16px;
    align-items: flex-start;
}
.Pixso-instance-6360_36867 {
    width: 52px;
    height: 20px;
}
.Pixso-instance-6360_36868 {
    width: 46px;
    height: 20px;
}
.Pixso-symbol-6360_54307 {
    width: 280px;
    height: auto;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 16px;
    align-items: flex-start;
    padding: 16px 16px 16px 16px;
    border-radius: 24px 24px 24px 24px;
}
.Pixso-frame-6360_54308 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    align-items: flex-start;
}
.frame-content-6360_54308 {
    display: flex;
    flex-direction: row;
    gap: 16px;
    align-items: flex-start;
    width: 100%;
    position: relative;
}
.Pixso-frame-6360_54309 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    flex-grow: 1;
    flex-basis: 0;
}
.frame-content-6360_54309 {
    display: flex;
    flex-direction: column;
    gap: 4px;
    align-items: flex-start;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-6360_54310 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-frame-6360_54311 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    align-items: flex-end;
}
.frame-content-6360_54311 {
    display: flex;
    flex-direction: row;
    align-items: flex-end;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-6360_54312 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-frame-6360_54313 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 10px;
    align-items: flex-end;
    padding: 0px 0px 3px 0px;
}
.Pixso-paragraph-6360_54314 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-6360_54315 {
    width: 20px;
    height: 20px;
}
.Pixso-paragraph-6360_54316 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-frame-6360_54317 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 16px;
    align-items: flex-start;
}
.Pixso-instance-6360_54318 {
    width: 52px;
    height: 20px;
}
.Pixso-instance-6360_54319 {
    width: 46px;
    height: 20px;
}
.Pixso-symbol-6360_54132 {
    width: 280px;
    height: auto;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 16px;
    align-items: flex-start;
    padding: 16px 16px 16px 16px;
    border-radius: 24px 24px 24px 24px;
}
.Pixso-frame-6360_54133 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    align-items: flex-start;
}
.frame-content-6360_54133 {
    display: flex;
    flex-direction: row;
    gap: 16px;
    align-items: flex-start;
    width: 100%;
    position: relative;
}
.Pixso-frame-6360_54134 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: row;
    align-items: flex-start;
    flex-grow: 1;
    flex-basis: 0;
}
.frame-content-6360_54134 {
    display: flex;
    flex-direction: row;
    gap: 10px;
    align-items: flex-start;
    width: 100%;
    position: relative;
}
.Pixso-instance-6360_54135 {
    width: 40px;
    height: 40px;
}
.Pixso-instance-5546_2449 {
    width: undefinedpx;
    height: undefinedpx;
}
.Pixso-instance-6360_54136 {
    width: 20px;
    height: 20px;
}
.Pixso-paragraph-6360_54137 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-frame-6360_54138 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 16px;
    align-items: flex-start;
}
.Pixso-instance-6360_54139 {
    width: 52px;
    height: 20px;
}
.Pixso-instance-6360_54140 {
    width: 46px;
    height: 20px;
}
.Pixso-symbol-6360_36880 {
    width: 280px;
    height: auto;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 16px;
    align-items: flex-start;
    padding: 16px 16px 16px 16px;
    border-radius: 24px 24px 24px 24px;
}
.Pixso-frame-6360_36881 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    align-items: flex-start;
}
.frame-content-6360_36881 {
    display: flex;
    flex-direction: row;
    gap: 16px;
    align-items: flex-start;
    width: 100%;
    position: relative;
}
.Pixso-frame-6360_36904 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: row;
    align-items: flex-start;
    flex-grow: 1;
    flex-basis: 0;
}
.frame-content-6360_36904 {
    display: flex;
    flex-direction: row;
    gap: 10px;
    align-items: flex-start;
    width: 100%;
    position: relative;
}
.Pixso-instance-6358_22757 {
    width: 40px;
    height: 40px;
}
.Pixso-instance-6360_36888 {
    width: 20px;
    height: 20px;
}
.Pixso-paragraph-6360_36889 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-frame-6360_36890 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 16px;
    align-items: flex-start;
}
.Pixso-instance-6360_36891 {
    width: 52px;
    height: 20px;
}
.Pixso-instance-6360_36892 {
    width: 46px;
    height: 20px;
}
.Pixso-symbol-6360_36905 {
    width: 280px;
    height: auto;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 16px;
    align-items: flex-start;
    padding: 16px 16px 16px 16px;
    border-radius: 24px 24px 24px 24px;
}
.Pixso-frame-6360_36906 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    align-items: flex-start;
}
.frame-content-6360_36906 {
    display: flex;
    flex-direction: row;
    gap: 16px;
    align-items: flex-start;
    width: 100%;
    position: relative;
}
.Pixso-frame-6360_36907 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: row;
    align-items: flex-start;
    flex-grow: 1;
    flex-basis: 0;
}
.frame-content-6360_36907 {
    display: flex;
    flex-direction: row;
    gap: 10px;
    align-items: flex-start;
    width: 100%;
    position: relative;
}
.Pixso-instance-6359_30100 {
    width: 40px;
    height: 40px;
}
.Pixso-instance-6360_36909 {
    width: 20px;
    height: 20px;
}
.Pixso-paragraph-6360_36910 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-frame-6360_36911 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 16px;
    align-items: flex-start;
}
.Pixso-instance-6360_36912 {
    width: 52px;
    height: 20px;
}
.Pixso-instance-6360_36913 {
    width: 46px;
    height: 20px;
}
.Pixso-symbol-6360_54320 {
    width: 280px;
    height: auto;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 16px;
    align-items: flex-start;
    padding: 16px 16px 16px 16px;
    border-radius: 24px 24px 24px 24px;
}
.Pixso-frame-6360_54321 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    align-items: flex-start;
}
.frame-content-6360_54321 {
    display: flex;
    flex-direction: row;
    gap: 16px;
    align-items: flex-start;
    width: 100%;
    position: relative;
}
.Pixso-frame-6360_54322 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: row;
    align-items: flex-start;
    flex-grow: 1;
    flex-basis: 0;
}
.frame-content-6360_54322 {
    display: flex;
    flex-direction: row;
    gap: 10px;
    align-items: flex-start;
    width: 100%;
    position: relative;
}
.Pixso-instance-6360_54323 {
    width: 40px;
    height: 40px;
}
.Pixso-instance-6360_54324 {
    width: 20px;
    height: 20px;
}
.Pixso-paragraph-6360_54325 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-frame-6360_54326 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 16px;
    align-items: flex-start;
}
.Pixso-instance-6360_54327 {
    width: 52px;
    height: 20px;
}
.Pixso-instance-6360_54328 {
    width: 46px;
    height: 20px;
}

.Pixso-instance-6360_54104 .Pixso-symbol-5579_151156 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-6360_54104 .Pixso-vector-5579_151157 {
    width: 65.64%;
    height: 65.65%;
    position: absolute;
    left: 17.18%;
    right: 17.18%;
    top: 17.17%;
    bottom: 17.18%;
}
.Pixso-instance-6360_54107 .Pixso-symbol-5603_17109 {
    width: 52px;
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
.Pixso-instance-6360_54107 .Pixso-instance-5603_17110 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-6360_54107 .Pixso-paragraph-5603_17111 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-6360_54107 .Pixso-instance-5603_17112 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-6360_54108 .Pixso-symbol-5603_17349 {
    width: 46px;
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
.Pixso-instance-6360_54108 .Pixso-instance-5603_17350 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-6360_54108 .Pixso-paragraph-5603_17351 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-6360_54108 .Pixso-instance-5603_17352 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-6360_54108
    .Pixso-instance-5603_17352
    .Pixso-vector-5577_144540 {
    width: 78.14%;
    height: 65.64%;
    background-image: url(@/assets/images/Vector42.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 9.11%;
    right: 12.75%;
    top: 14.31%;
    bottom: 20.05%;
}
.Pixso-instance-6358_21528 .Pixso-symbol-5579_151156 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-6358_21528 .Pixso-vector-5579_151157 {
    width: 65.64%;
    height: 65.65%;
    position: absolute;
    left: 17.18%;
    right: 17.18%;
    top: 17.17%;
    bottom: 17.18%;
}
.Pixso-instance-6358_21562 .Pixso-symbol-5603_17109 {
    width: 52px;
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
.Pixso-instance-6358_21562 .Pixso-instance-5603_17110 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-6358_21562 .Pixso-paragraph-5603_17111 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-6358_21562 .Pixso-instance-5603_17112 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-6358_21576 .Pixso-symbol-5603_17349 {
    width: 46px;
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
.Pixso-instance-6358_21576 .Pixso-instance-5603_17350 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-6358_21576 .Pixso-paragraph-5603_17351 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-6358_21576 .Pixso-instance-5603_17352 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-6358_21576
    .Pixso-instance-5603_17352
    .Pixso-vector-5577_144540 {
    width: 78.14%;
    height: 65.64%;
    background-image: url(@/assets/images/Vector42.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 9.11%;
    right: 12.75%;
    top: 14.31%;
    bottom: 20.05%;
}
.Pixso-instance-6359_30101 .Pixso-symbol-5579_151156 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-6359_30101 .Pixso-vector-5579_151157 {
    width: 65.64%;
    height: 65.65%;
    position: absolute;
    left: 17.18%;
    right: 17.18%;
    top: 17.17%;
    bottom: 17.18%;
}
.Pixso-instance-6359_30106 .Pixso-symbol-5603_17109 {
    width: 52px;
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
.Pixso-instance-6359_30106 .Pixso-instance-5603_17110 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-6359_30106 .Pixso-paragraph-5603_17111 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-6359_30106 .Pixso-instance-5603_17112 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-6359_30107 .Pixso-symbol-5603_17349 {
    width: 46px;
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
.Pixso-instance-6359_30107 .Pixso-instance-5603_17350 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-6359_30107 .Pixso-paragraph-5603_17351 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-6359_30107 .Pixso-instance-5603_17352 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-6359_30107
    .Pixso-instance-5603_17352
    .Pixso-vector-5577_144540 {
    width: 78.14%;
    height: 65.64%;
    background-image: url(@/assets/images/Vector42.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 9.11%;
    right: 12.75%;
    top: 14.31%;
    bottom: 20.05%;
}
.Pixso-instance-6360_54292 .Pixso-symbol-5579_151156 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-6360_54292 .Pixso-vector-5579_151157 {
    width: 65.64%;
    height: 65.65%;
    position: absolute;
    left: 17.18%;
    right: 17.18%;
    top: 17.17%;
    bottom: 17.18%;
}
.Pixso-instance-6360_54295 .Pixso-symbol-5603_17109 {
    width: 52px;
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
.Pixso-instance-6360_54295 .Pixso-instance-5603_17110 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-6360_54295 .Pixso-paragraph-5603_17111 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-6360_54295 .Pixso-instance-5603_17112 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-6360_54296 .Pixso-symbol-5603_17349 {
    width: 46px;
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
.Pixso-instance-6360_54296 .Pixso-instance-5603_17350 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-6360_54296 .Pixso-paragraph-5603_17351 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-6360_54296 .Pixso-instance-5603_17352 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-6360_54296
    .Pixso-instance-5603_17352
    .Pixso-vector-5577_144540 {
    width: 78.14%;
    height: 65.64%;
    background-image: url(@/assets/images/Vector42.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 9.11%;
    right: 12.75%;
    top: 14.31%;
    bottom: 20.05%;
}
.Pixso-instance-6360_54127 .Pixso-symbol-5579_151156 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-6360_54127 .Pixso-vector-5579_151157 {
    width: 65.64%;
    height: 65.65%;
    position: absolute;
    left: 17.18%;
    right: 17.18%;
    top: 17.17%;
    bottom: 17.18%;
}
.Pixso-instance-6360_54130 .Pixso-symbol-5603_17109 {
    width: 52px;
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
.Pixso-instance-6360_54130 .Pixso-instance-5603_17110 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-6360_54130 .Pixso-paragraph-5603_17111 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-6360_54130 .Pixso-instance-5603_17112 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-6360_54131 .Pixso-symbol-5603_17349 {
    width: 46px;
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
.Pixso-instance-6360_54131 .Pixso-instance-5603_17350 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-6360_54131 .Pixso-paragraph-5603_17351 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-6360_54131 .Pixso-instance-5603_17352 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-6360_54131
    .Pixso-instance-5603_17352
    .Pixso-vector-5577_144540 {
    width: 78.14%;
    height: 65.64%;
    background-image: url(@/assets/images/Vector42.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 9.11%;
    right: 12.75%;
    top: 14.31%;
    bottom: 20.05%;
}
.Pixso-instance-6359_35284 .Pixso-symbol-5579_151156 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-6359_35284 .Pixso-vector-5579_151157 {
    width: 65.64%;
    height: 65.65%;
    position: absolute;
    left: 17.18%;
    right: 17.18%;
    top: 17.17%;
    bottom: 17.18%;
}
.Pixso-instance-6359_35287 .Pixso-symbol-5603_17109 {
    width: 52px;
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
.Pixso-instance-6359_35287 .Pixso-instance-5603_17110 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-6359_35287 .Pixso-paragraph-5603_17111 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-6359_35287 .Pixso-instance-5603_17112 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-6359_35288 .Pixso-symbol-5603_17349 {
    width: 46px;
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
.Pixso-instance-6359_35288 .Pixso-instance-5603_17350 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-6359_35288 .Pixso-paragraph-5603_17351 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-6359_35288 .Pixso-instance-5603_17352 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-6359_35288
    .Pixso-instance-5603_17352
    .Pixso-vector-5577_144540 {
    width: 78.14%;
    height: 65.64%;
    background-image: url(@/assets/images/Vector42.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 9.11%;
    right: 12.75%;
    top: 14.31%;
    bottom: 20.05%;
}
.Pixso-instance-6360_36864 .Pixso-symbol-5579_151156 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-6360_36864 .Pixso-vector-5579_151157 {
    width: 65.64%;
    height: 65.65%;
    position: absolute;
    left: 17.18%;
    right: 17.18%;
    top: 17.17%;
    bottom: 17.18%;
}
.Pixso-instance-6360_36867 .Pixso-symbol-5603_17109 {
    width: 52px;
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
.Pixso-instance-6360_36867 .Pixso-instance-5603_17110 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-6360_36867 .Pixso-paragraph-5603_17111 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-6360_36867 .Pixso-instance-5603_17112 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-6360_36868 .Pixso-symbol-5603_17349 {
    width: 46px;
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
.Pixso-instance-6360_36868 .Pixso-instance-5603_17350 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-6360_36868 .Pixso-paragraph-5603_17351 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-6360_36868 .Pixso-instance-5603_17352 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-6360_36868
    .Pixso-instance-5603_17352
    .Pixso-vector-5577_144540 {
    width: 78.14%;
    height: 65.64%;
    background-image: url(@/assets/images/Vector42.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 9.11%;
    right: 12.75%;
    top: 14.31%;
    bottom: 20.05%;
}
.Pixso-instance-6360_54315 .Pixso-symbol-5579_151156 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-6360_54315 .Pixso-vector-5579_151157 {
    width: 65.64%;
    height: 65.65%;
    position: absolute;
    left: 17.18%;
    right: 17.18%;
    top: 17.17%;
    bottom: 17.18%;
}
.Pixso-instance-6360_54318 .Pixso-symbol-5603_17109 {
    width: 52px;
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
.Pixso-instance-6360_54318 .Pixso-instance-5603_17110 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-6360_54318 .Pixso-paragraph-5603_17111 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-6360_54318 .Pixso-instance-5603_17112 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-6360_54319 .Pixso-symbol-5603_17349 {
    width: 46px;
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
.Pixso-instance-6360_54319 .Pixso-instance-5603_17350 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-6360_54319 .Pixso-paragraph-5603_17351 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-6360_54319 .Pixso-instance-5603_17352 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-6360_54319
    .Pixso-instance-5603_17352
    .Pixso-vector-5577_144540 {
    width: 78.14%;
    height: 65.64%;
    background-image: url(@/assets/images/Vector42.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 9.11%;
    right: 12.75%;
    top: 14.31%;
    bottom: 20.05%;
}
.Pixso-instance-6360_54135 .Pixso-symbol-5546_2473 {
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
.Pixso-instance-6360_54135 .Pixso-instance-5546_2449 .Pixso-vector-5579_153340 {
    width: 75.53%;
    height: 67.71%;
    background-image: url(@/assets/images/Vector84.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 3.9%;
    right: 20.57%;
    top: 6.51%;
    bottom: 25.78%;
}
.Pixso-instance-5546_2449 .Pixso-vector-5579_153340 {
    width: 75.53%;
    height: 67.71%;
    position: absolute;
    left: 3.9%;
    right: 20.57%;
    top: 6.51%;
    bottom: 25.78%;
}
.Pixso-instance-6360_54136 .Pixso-symbol-5579_151156 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-6360_54136 .Pixso-vector-5579_151157 {
    width: 65.64%;
    height: 65.65%;
    position: absolute;
    left: 17.18%;
    right: 17.18%;
    top: 17.17%;
    bottom: 17.18%;
}
.Pixso-instance-6360_54139 .Pixso-symbol-5603_17109 {
    width: 52px;
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
.Pixso-instance-6360_54139 .Pixso-instance-5603_17110 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-6360_54139 .Pixso-paragraph-5603_17111 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-6360_54139 .Pixso-instance-5603_17112 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-6360_54140 .Pixso-symbol-5603_17349 {
    width: 46px;
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
.Pixso-instance-6360_54140 .Pixso-instance-5603_17350 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-6360_54140 .Pixso-paragraph-5603_17351 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-6360_54140 .Pixso-instance-5603_17352 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-6360_54140
    .Pixso-instance-5603_17352
    .Pixso-vector-5577_144540 {
    width: 78.14%;
    height: 65.64%;
    background-image: url(@/assets/images/Vector42.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 9.11%;
    right: 12.75%;
    top: 14.31%;
    bottom: 20.05%;
}
.Pixso-instance-6358_22757 .Pixso-symbol-5546_2473 {
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
.Pixso-instance-6358_22757 .Pixso-instance-5546_2449 .Pixso-vector-5579_153340 {
    width: 75.53%;
    height: 67.71%;
    background-image: url(@/assets/images/Vector84.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 3.9%;
    right: 20.57%;
    top: 6.51%;
    bottom: 25.78%;
}
.Pixso-instance-6360_36888 .Pixso-symbol-5579_151156 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-6360_36888 .Pixso-vector-5579_151157 {
    width: 65.64%;
    height: 65.65%;
    position: absolute;
    left: 17.18%;
    right: 17.18%;
    top: 17.17%;
    bottom: 17.18%;
}
.Pixso-instance-6360_36891 .Pixso-symbol-5603_17109 {
    width: 52px;
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
.Pixso-instance-6360_36891 .Pixso-instance-5603_17110 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-6360_36891 .Pixso-paragraph-5603_17111 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-6360_36891 .Pixso-instance-5603_17112 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-6360_36892 .Pixso-symbol-5603_17349 {
    width: 46px;
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
.Pixso-instance-6360_36892 .Pixso-instance-5603_17350 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-6360_36892 .Pixso-paragraph-5603_17351 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-6360_36892 .Pixso-instance-5603_17352 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-6360_36892
    .Pixso-instance-5603_17352
    .Pixso-vector-5577_144540 {
    width: 78.14%;
    height: 65.64%;
    background-image: url(@/assets/images/Vector42.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 9.11%;
    right: 12.75%;
    top: 14.31%;
    bottom: 20.05%;
}
.Pixso-instance-6359_30100 .Pixso-symbol-5546_2473 {
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
.Pixso-instance-6359_30100 .Pixso-instance-5546_2449 .Pixso-vector-5579_153340 {
    width: 75.53%;
    height: 67.71%;
    background-image: url(@/assets/images/Vector84.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 3.9%;
    right: 20.57%;
    top: 6.51%;
    bottom: 25.78%;
}
.Pixso-instance-6360_36909 .Pixso-symbol-5579_151156 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-6360_36909 .Pixso-vector-5579_151157 {
    width: 65.64%;
    height: 65.65%;
    position: absolute;
    left: 17.18%;
    right: 17.18%;
    top: 17.17%;
    bottom: 17.18%;
}
.Pixso-instance-6360_36912 .Pixso-symbol-5603_17109 {
    width: 52px;
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
.Pixso-instance-6360_36912 .Pixso-instance-5603_17110 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-6360_36912 .Pixso-paragraph-5603_17111 {
    text-decoration: none;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-6360_36912 .Pixso-instance-5603_17112 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-6360_36913 .Pixso-symbol-5603_17349 {
    width: 46px;
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
.Pixso-instance-6360_36913 .Pixso-instance-5603_17350 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-6360_36913 .Pixso-paragraph-5603_17351 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-6360_36913 .Pixso-instance-5603_17352 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-6360_36913
    .Pixso-instance-5603_17352
    .Pixso-vector-5577_144540 {
    width: 78.14%;
    height: 65.64%;
    background-image: url(@/assets/images/Vector42.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 9.11%;
    right: 12.75%;
    top: 14.31%;
    bottom: 20.05%;
}
.Pixso-instance-6360_54323 .Pixso-symbol-5546_2473 {
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
.Pixso-instance-6360_54323 .Pixso-instance-5546_2449 .Pixso-vector-5579_153340 {
    width: 75.53%;
    height: 67.71%;
    background-image: url(@/assets/images/Vector84.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 3.9%;
    right: 20.57%;
    top: 6.51%;
    bottom: 25.78%;
}
.Pixso-instance-6360_54324 .Pixso-symbol-5579_151156 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-6360_54324 .Pixso-vector-5579_151157 {
    width: 65.64%;
    height: 65.65%;
    position: absolute;
    left: 17.18%;
    right: 17.18%;
    top: 17.17%;
    bottom: 17.18%;
}
.Pixso-instance-6360_54327 .Pixso-symbol-5603_17109 {
    width: 52px;
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
.Pixso-instance-6360_54327 .Pixso-instance-5603_17110 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-6360_54327 .Pixso-paragraph-5603_17111 {
    text-decoration: none;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-6360_54327 .Pixso-instance-5603_17112 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-6360_54328 .Pixso-symbol-5603_17349 {
    width: 46px;
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
.Pixso-instance-6360_54328 .Pixso-instance-5603_17350 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-6360_54328 .Pixso-paragraph-5603_17351 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-6360_54328 .Pixso-instance-5603_17352 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-6360_54105 .Pixso-symbol-1264_9885 {
    width: 248px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    gap: 10px;
    align-items: flex-start;
    border-radius: 8px 8px 8px 8px;
    background-color: transparent;
}
.Pixso-instance-6359_30127 .Pixso-symbol-1264_9885 {
    width: 248px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    gap: 10px;
    align-items: flex-start;
    border-radius: 8px 8px 8px 8px;
    background-color: transparent;
}
.Pixso-instance-6359_30137 .Pixso-symbol-1264_9885 {
    width: 248px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    gap: 10px;
    align-items: flex-start;
    border-radius: 8px 8px 8px 8px;
    background-color: transparent;
}
.Pixso-instance-6360_54293 .Pixso-symbol-1264_9885 {
    width: 248px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    gap: 10px;
    align-items: flex-start;
    border-radius: 8px 8px 8px 8px;
    background-color: transparent;
}
.Pixso-instance-6360_54105 .Pixso-frame-1264_9886 {
    width: 100%;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-6359_30127 .Pixso-frame-1264_9886 {
    width: 100%;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-6359_30137 .Pixso-frame-1264_9886 {
    width: 100%;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-6360_54293 .Pixso-frame-1264_9886 {
    width: 100%;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-6360_54105 .Pixso-instance-1264_9887 {
    width: 320px;
    height: 8px;
}
.Pixso-instance-6359_30127 .Pixso-instance-1264_9887 {
    width: 320px;
    height: 8px;
}
.Pixso-instance-6359_30137 .Pixso-instance-1264_9887 {
    width: 320px;
    height: 8px;
}
.Pixso-instance-6360_54293 .Pixso-instance-1264_9887 {
    width: 320px;
    height: 8px;
}
.Pixso-instance-6360_54105 .Pixso-instance-1264_9888 {
    width: 211px;
    height: 8px;
}
.Pixso-instance-6359_30127 .Pixso-instance-1264_9888 {
    width: 211px;
    height: 8px;
}
.Pixso-instance-6359_30137 .Pixso-instance-1264_9888 {
    width: 211px;
    height: 8px;
}
.Pixso-instance-6360_54293 .Pixso-instance-1264_9888 {
    width: 211px;
    height: 8px;
}
</style>
