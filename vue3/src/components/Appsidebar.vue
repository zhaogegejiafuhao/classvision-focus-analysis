<template>
    <div class="component-5984_59825">
        <div id="5984_59825" class="Pixso-symbol-5984_59825">
            <div
                id="5982_59216"
                class="stroke-wrapper-5982_59216"
                v-if="
                    Theme === 'White' &&
                    IsMobile === 'False' &&
                    Type === 'Default'
                "
            >
                <div class="Pixso-symbol-5982_59216 fill-gray0-white-67_3285">
                    <div id="5982_59115" class="Pixso-frame-5982_59115">
                        <div class="frame-content-5982_59115">
                            <div id="5982_59116" class="Pixso-frame-5982_59116">
                                <div class="frame-content-5982_59116">
                                    <slot name="slot_5982_59117">
                                        <Logo
                                            id="5982_59117"
                                            class="Pixso-instance-5982_59117"
                                            IsDarkMode="False"
                                        />
                                    </slot>
                                </div>
                            </div>
                            <slot name="slot_5982_59118">
                                <InputText
                                    id="5982_59118"
                                    class="Pixso-instance-5982_59118"
                                    :visible_5607_114="false"
                                    :visible_5607_117="false"
                                    State="Default"
                                    Type="Default"
                                    Size="md"
                                >
                                    <template #slot_5976_53794>
                                        <InputTextBase
                                            id="5976_53794"
                                            class="Pixso-instance-5976_53794"
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
                                        </InputTextBase>
                                    </template>
                                </InputText>
                            </slot>
                            <div id="5982_59119" class="Pixso-frame-5982_59119">
                                <slot name="slot_5982_59120">
                                    <AppSidebarItem
                                        id="5982_59120"
                                        class="Pixso-instance-5982_59120"
                                        :visible_5982_36="false"
                                        :visible_5982_41="false"
                                        text_5982_39="Home"
                                        Theme="White"
                                        State="Default"
                                    >
                                        <template #slot_5979_34883>
                                            <p
                                                id="5979_34883"
                                                class="Pixso-paragraph-5979_34883 fill-gray80-32_4123-paragraph text-text-mdbold-423_3205"
                                            >
                                                {{ "Home" }}
                                            </p>
                                        </template>
                                        <template #slot_5979_34885>
                                            <BadgeText
                                                id="5979_34885"
                                                class="Pixso-instance-5979_34885"
                                                :visible_5586_119="false"
                                                :visible_5586_121="false"
                                                :visible_5586_123="false"
                                                text_5588_129="10"
                                                Size="md"
                                                Color="Brand"
                                                Hierarchy="Secondary"
                                                State="Default"
                                            >
                                                <template #slot_5588_11356>
                                                    <p
                                                        id="5588_11356"
                                                        class="Pixso-paragraph-5588_11356 fill-brand60-1257_33467-paragraph text-text-smsemibold-423_3209"
                                                    >
                                                        {{ "10" }}
                                                    </p>
                                                </template>
                                            </BadgeText>
                                        </template>
                                    </AppSidebarItem>
                                </slot>
                                <slot name="slot_5982_59121">
                                    <AppSidebarItem
                                        id="5982_59121"
                                        class="Pixso-instance-5982_59121"
                                        :visible_5982_36="false"
                                        :visible_5982_41="false"
                                        :visible_5982_37="false"
                                        text_5982_39="Tasks"
                                        Theme="White"
                                        State="Default"
                                    >
                                        <template #slot_5979_34883>
                                            <p
                                                id="5979_34883"
                                                class="Pixso-paragraph-5979_34883 fill-gray80-32_4123-paragraph text-text-mdbold-423_3205"
                                            >
                                                {{ "Tasks" }}
                                            </p>
                                        </template>
                                        <template #slot_5980_54116>
                                            <ListBullets
                                                id="5980_54116"
                                                class="Pixso-instance-5980_54116"
                                            />
                                        </template>
                                    </AppSidebarItem>
                                </slot>
                                <slot name="slot_5982_59122">
                                    <AppSidebarItem
                                        id="5982_59122"
                                        class="Pixso-instance-5982_59122"
                                        :visible_5982_36="false"
                                        :visible_5982_41="false"
                                        text_5982_39="Users"
                                        Theme="White"
                                        State="Default"
                                    >
                                        <template #slot_5979_34883>
                                            <p
                                                id="5979_34883"
                                                class="Pixso-paragraph-5979_34883 fill-gray80-32_4123-paragraph text-text-mdbold-423_3205"
                                            >
                                                {{ "Users" }}
                                            </p>
                                        </template>
                                        <template #slot_5980_54116>
                                            <Users
                                                id="5980_54116"
                                                class="Pixso-instance-5980_54116"
                                            />
                                        </template>
                                        <template #slot_5979_34885>
                                            <BadgeText
                                                id="5979_34885"
                                                class="Pixso-instance-5979_34885"
                                                :visible_5586_119="false"
                                                :visible_5586_121="false"
                                                :visible_5586_123="false"
                                                text_5588_129="10"
                                                Size="md"
                                                Color="Brand"
                                                Hierarchy="Secondary"
                                                State="Default"
                                            >
                                                <template #slot_5588_11356>
                                                    <p
                                                        id="5588_11356"
                                                        class="Pixso-paragraph-5588_11356 fill-brand60-1257_33467-paragraph text-text-smsemibold-423_3209"
                                                    >
                                                        {{ "10" }}
                                                    </p>
                                                </template>
                                            </BadgeText>
                                        </template>
                                    </AppSidebarItem>
                                </slot>
                                <slot name="slot_5982_59123">
                                    <AppSidebarItem
                                        id="5982_59123"
                                        class="Pixso-instance-5982_59123"
                                        :visible_5982_36="false"
                                        :visible_5982_41="false"
                                        :visible_5982_37="false"
                                        text_5982_39="APIs"
                                        Theme="White"
                                        State="Default"
                                    >
                                        <template #slot_5979_34883>
                                            <p
                                                id="5979_34883"
                                                class="Pixso-paragraph-5979_34883 fill-gray80-32_4123-paragraph text-text-mdbold-423_3205"
                                            >
                                                {{ "APIs" }}
                                            </p>
                                        </template>
                                        <template #slot_5980_54116>
                                            <Cube
                                                id="5980_54116"
                                                class="Pixso-instance-5980_54116"
                                            />
                                        </template>
                                    </AppSidebarItem>
                                </slot>
                                <slot name="slot_5982_59124">
                                    <AppSidebarItem
                                        id="5982_59124"
                                        class="Pixso-instance-5982_59124"
                                        :visible_5982_36="false"
                                        :visible_5982_41="false"
                                        :visible_5982_37="false"
                                        text_5982_39="Subscription"
                                        Theme="White"
                                        State="Default"
                                    >
                                        <template #slot_5979_34883>
                                            <p
                                                id="5979_34883"
                                                class="Pixso-paragraph-5979_34883 fill-gray80-32_4123-paragraph text-text-mdbold-423_3205"
                                            >
                                                {{ "Subscription" }}
                                            </p>
                                        </template>
                                        <template #slot_5980_54116>
                                            <CreditCard
                                                id="5980_54116"
                                                class="Pixso-instance-5980_54116"
                                            />
                                        </template>
                                    </AppSidebarItem>
                                </slot>
                                <slot name="slot_5982_59125">
                                    <AppSidebarItem
                                        id="5982_59125"
                                        class="Pixso-instance-5982_59125"
                                        :visible_5982_36="false"
                                        :visible_5982_41="false"
                                        :visible_5982_37="false"
                                        text_5982_39="Settings"
                                        Theme="White"
                                        State="Default"
                                    >
                                        <template #slot_5979_34883>
                                            <p
                                                id="5979_34883"
                                                class="Pixso-paragraph-5979_34883 fill-gray80-32_4123-paragraph text-text-mdbold-423_3205"
                                            >
                                                {{ "Settings" }}
                                            </p>
                                        </template>
                                        <template #slot_5980_54116>
                                            <GearSix
                                                id="5980_54116"
                                                class="Pixso-instance-5980_54116"
                                            />
                                        </template>
                                    </AppSidebarItem>
                                </slot>
                                <slot name="slot_5982_59126">
                                    <AppSidebarItem
                                        id="5982_59126"
                                        class="Pixso-instance-5982_59126"
                                        :visible_5982_36="false"
                                        :visible_5982_41="false"
                                        :visible_5982_37="false"
                                        text_5982_39="Help &amp; Support"
                                        Theme="White"
                                        State="Default"
                                    >
                                        <template #slot_5979_34883>
                                            <p
                                                id="5979_34883"
                                                class="Pixso-paragraph-5979_34883 fill-gray80-32_4123-paragraph text-text-mdbold-423_3205"
                                            >
                                                {{ "Help & Support" }}
                                            </p>
                                        </template>
                                        <template #slot_5980_54116>
                                            <ChatTeardropDots
                                                id="5980_54116"
                                                class="Pixso-instance-5980_54116"
                                            />
                                        </template>
                                    </AppSidebarItem>
                                </slot>
                            </div>
                        </div>
                    </div>
                    <div id="5982_59127" class="Pixso-frame-5982_59127">
                        <slot name="slot_6360_36928">
                            <NavFeaturedCard
                                id="6360_36928"
                                class="Pixso-instance-6360_36928"
                                Theme="Light Gray"
                                Type="Icon"
                            >
                                <template #slot_6360_36891>
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
                                                class="Pixso-paragraph-5603_17111 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                                            >
                                                {{ "Dismiss" }}
                                            </p>
                                        </template>
                                    </Button>
                                </template>
                                <template #slot_6360_36892>
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
                                                class="Pixso-paragraph-5603_17351 fill-brand60-1257_33467-paragraph text-text-smbold-423_3208"
                                            >
                                                {{ "Go Pro" }}
                                            </p>
                                        </template>
                                    </Button>
                                </template>
                            </NavFeaturedCard>
                        </slot>
                        <div id="5982_59129" class="stroke-wrapper-5982_59129">
                            <div class="Pixso-frame-5982_59129">
                                <div class="frame-content-5982_59129">
                                    <div
                                        id="5982_59130"
                                        class="Pixso-frame-5982_59130"
                                    >
                                        <div class="frame-content-5982_59130">
                                            <slot name="slot_5982_59131">
                                                <Avatar
                                                    id="5982_59131"
                                                    class="Pixso-instance-5982_59131"
                                                    Size="md"
                                                    Type="Image"
                                                    Indicator="None"
                                                />
                                            </slot>
                                            <div
                                                id="5982_59132"
                                                class="Pixso-frame-5982_59132"
                                            >
                                                <div
                                                    class="frame-content-5982_59132"
                                                >
                                                    <slot
                                                        name="slot_5982_59133"
                                                    >
                                                        <p
                                                            id="5982_59133"
                                                            class="Pixso-paragraph-5982_59133 fill-gray80-32_4123-paragraph text-text-mdbold-423_3205"
                                                        >
                                                            {{
                                                                "Azunyan U. Wu"
                                                            }}
                                                        </p>
                                                    </slot>
                                                    <slot
                                                        name="slot_5982_59134"
                                                    >
                                                        <p
                                                            id="5982_59134"
                                                            class="Pixso-paragraph-5982_59134 fill-gray60-83_2722-paragraph text-text-smmedium-5454_21607"
                                                        >
                                                            {{ "Basic Member" }}
                                                        </p>
                                                    </slot>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                    <slot name="slot_5982_59135">
                                        <ButtonIcon
                                            id="5982_59135"
                                            class="Pixso-instance-5982_59135"
                                            Hierarchy="No Fill"
                                            Size="md"
                                            Color="Gray"
                                            State="Default"
                                        >
                                            <template #slot_5590_22158>
                                                <SignOut
                                                    id="5590_22158"
                                                    class="Pixso-instance-5590_22158"
                                                />
                                            </template>
                                        </ButtonIcon>
                                    </slot>
                                </div>
                            </div>
                            <div
                                class="stroke-5982_59129 stroke-gray20-36_1844"
                            ></div>
                        </div>
                    </div>
                </div>
                <div class="stroke-5982_59216 stroke-gray20-36_1844"></div>
            </div>
            <div
                id="6360_51957"
                class="Pixso-symbol-6360_51957 fill-gray5-32_4120"
                v-if="
                    Theme === 'Light Gray' &&
                    IsMobile === 'False' &&
                    Type === 'Default'
                "
            >
                <div id="6360_51958" class="Pixso-frame-6360_51958">
                    <div class="frame-content-6360_51958">
                        <div id="6360_51959" class="Pixso-frame-6360_51959">
                            <div class="frame-content-6360_51959">
                                <slot name="slot_6360_51960">
                                    <Logo
                                        id="6360_51960"
                                        class="Pixso-instance-6360_51960"
                                        IsDarkMode="False"
                                    />
                                </slot>
                            </div>
                        </div>
                        <slot name="slot_6360_51961">
                            <InputText
                                id="6360_51961"
                                class="Pixso-instance-6360_51961"
                                :visible_5607_114="false"
                                :visible_5607_117="false"
                                State="Default"
                                Type="Default"
                                Size="md"
                            >
                                <template #slot_5976_53794>
                                    <InputTextBase
                                        id="5976_53794"
                                        class="Pixso-instance-5976_53794"
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
                                    </InputTextBase>
                                </template>
                            </InputText>
                        </slot>
                        <div id="6360_51962" class="Pixso-frame-6360_51962">
                            <slot name="slot_6360_51963">
                                <AppSidebarItem
                                    id="6360_51963"
                                    class="Pixso-instance-6360_51963"
                                    :visible_5982_36="false"
                                    :visible_5982_41="false"
                                    text_5982_39="Home"
                                    Theme="Light Gray"
                                    State="Default"
                                >
                                    <template #slot_6360_52184>
                                        <p
                                            id="6360_52184"
                                            class="Pixso-paragraph-6360_52184 fill-gray80-32_4123-paragraph text-text-mdbold-423_3205"
                                        >
                                            {{ "Home" }}
                                        </p>
                                    </template>
                                    <template #slot_6360_52185>
                                        <BadgeText
                                            id="6360_52185"
                                            class="Pixso-instance-6360_52185"
                                            :visible_5586_119="false"
                                            :visible_5586_121="false"
                                            :visible_5586_123="false"
                                            text_5588_129="10"
                                            Size="md"
                                            Color="Brand"
                                            Hierarchy="Secondary"
                                            State="Default"
                                        >
                                            <template #slot_5588_11356>
                                                <p
                                                    id="5588_11356"
                                                    class="Pixso-paragraph-5588_11356 fill-brand60-1257_33467-paragraph text-text-smsemibold-423_3209"
                                                >
                                                    {{ "10" }}
                                                </p>
                                            </template>
                                        </BadgeText>
                                    </template>
                                </AppSidebarItem>
                            </slot>
                            <slot name="slot_6360_51964">
                                <AppSidebarItem
                                    id="6360_51964"
                                    class="Pixso-instance-6360_51964"
                                    :visible_5982_36="false"
                                    :visible_5982_41="false"
                                    :visible_5982_37="false"
                                    text_5982_39="Tasks"
                                    Theme="Light Gray"
                                    State="Default"
                                >
                                    <template #slot_6360_52184>
                                        <p
                                            id="6360_52184"
                                            class="Pixso-paragraph-6360_52184 fill-gray80-32_4123-paragraph text-text-mdbold-423_3205"
                                        >
                                            {{ "Tasks" }}
                                        </p>
                                    </template>
                                    <template #slot_6360_52183>
                                        <ListBullets
                                            id="6360_52183"
                                            class="Pixso-instance-6360_52183"
                                        />
                                    </template>
                                </AppSidebarItem>
                            </slot>
                            <slot name="slot_6360_51965">
                                <AppSidebarItem
                                    id="6360_51965"
                                    class="Pixso-instance-6360_51965"
                                    :visible_5982_36="false"
                                    :visible_5982_41="false"
                                    text_5982_39="Users"
                                    Theme="Light Gray"
                                    State="Default"
                                >
                                    <template #slot_6360_52184>
                                        <p
                                            id="6360_52184"
                                            class="Pixso-paragraph-6360_52184 fill-gray80-32_4123-paragraph text-text-mdbold-423_3205"
                                        >
                                            {{ "Users" }}
                                        </p>
                                    </template>
                                    <template #slot_6360_52183>
                                        <Users
                                            id="6360_52183"
                                            class="Pixso-instance-6360_52183"
                                        />
                                    </template>
                                    <template #slot_6360_52185>
                                        <BadgeText
                                            id="6360_52185"
                                            class="Pixso-instance-6360_52185"
                                            :visible_5586_119="false"
                                            :visible_5586_121="false"
                                            :visible_5586_123="false"
                                            text_5588_129="10"
                                            Size="md"
                                            Color="Brand"
                                            Hierarchy="Secondary"
                                            State="Default"
                                        >
                                            <template #slot_5588_11356>
                                                <p
                                                    id="5588_11356"
                                                    class="Pixso-paragraph-5588_11356 fill-brand60-1257_33467-paragraph text-text-smsemibold-423_3209"
                                                >
                                                    {{ "10" }}
                                                </p>
                                            </template>
                                        </BadgeText>
                                    </template>
                                </AppSidebarItem>
                            </slot>
                            <slot name="slot_6360_51966">
                                <AppSidebarItem
                                    id="6360_51966"
                                    class="Pixso-instance-6360_51966"
                                    :visible_5982_36="false"
                                    :visible_5982_41="false"
                                    :visible_5982_37="false"
                                    text_5982_39="APIs"
                                    Theme="Light Gray"
                                    State="Default"
                                >
                                    <template #slot_6360_52184>
                                        <p
                                            id="6360_52184"
                                            class="Pixso-paragraph-6360_52184 fill-gray80-32_4123-paragraph text-text-mdbold-423_3205"
                                        >
                                            {{ "APIs" }}
                                        </p>
                                    </template>
                                    <template #slot_6360_52183>
                                        <Cube
                                            id="6360_52183"
                                            class="Pixso-instance-6360_52183"
                                        />
                                    </template>
                                </AppSidebarItem>
                            </slot>
                            <slot name="slot_6360_51967">
                                <AppSidebarItem
                                    id="6360_51967"
                                    class="Pixso-instance-6360_51967"
                                    :visible_5982_36="false"
                                    :visible_5982_41="false"
                                    :visible_5982_37="false"
                                    text_5982_39="Subscription"
                                    Theme="Light Gray"
                                    State="Default"
                                >
                                    <template #slot_6360_52184>
                                        <p
                                            id="6360_52184"
                                            class="Pixso-paragraph-6360_52184 fill-gray80-32_4123-paragraph text-text-mdbold-423_3205"
                                        >
                                            {{ "Subscription" }}
                                        </p>
                                    </template>
                                    <template #slot_6360_52183>
                                        <CreditCard
                                            id="6360_52183"
                                            class="Pixso-instance-6360_52183"
                                        />
                                    </template>
                                </AppSidebarItem>
                            </slot>
                            <slot name="slot_6360_51968">
                                <AppSidebarItem
                                    id="6360_51968"
                                    class="Pixso-instance-6360_51968"
                                    :visible_5982_36="false"
                                    :visible_5982_41="false"
                                    :visible_5982_37="false"
                                    text_5982_39="Settings"
                                    Theme="Light Gray"
                                    State="Default"
                                >
                                    <template #slot_6360_52184>
                                        <p
                                            id="6360_52184"
                                            class="Pixso-paragraph-6360_52184 fill-gray80-32_4123-paragraph text-text-mdbold-423_3205"
                                        >
                                            {{ "Settings" }}
                                        </p>
                                    </template>
                                    <template #slot_6360_52183>
                                        <GearSix
                                            id="6360_52183"
                                            class="Pixso-instance-6360_52183"
                                        />
                                    </template>
                                </AppSidebarItem>
                            </slot>
                            <slot name="slot_6360_51969">
                                <AppSidebarItem
                                    id="6360_51969"
                                    class="Pixso-instance-6360_51969"
                                    :visible_5982_36="false"
                                    :visible_5982_41="false"
                                    :visible_5982_37="false"
                                    text_5982_39="Help &amp; Support"
                                    Theme="Light Gray"
                                    State="Default"
                                >
                                    <template #slot_6360_52184>
                                        <p
                                            id="6360_52184"
                                            class="Pixso-paragraph-6360_52184 fill-gray80-32_4123-paragraph text-text-mdbold-423_3205"
                                        >
                                            {{ "Help & Support" }}
                                        </p>
                                    </template>
                                    <template #slot_6360_52183>
                                        <ChatTeardropDots
                                            id="6360_52183"
                                            class="Pixso-instance-6360_52183"
                                        />
                                    </template>
                                </AppSidebarItem>
                            </slot>
                        </div>
                    </div>
                </div>
                <div id="6360_51970" class="Pixso-frame-6360_51970">
                    <slot name="slot_6360_54190">
                        <NavFeaturedCard
                            id="6360_54190"
                            class="Pixso-instance-6360_54190"
                            Theme="White"
                            Type="Icon"
                        >
                            <template #slot_6360_54139>
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
                                            class="Pixso-paragraph-5603_17111 fill-gray60-83_2722-paragraph text-text-smbold-423_3208 fill-gray30-35_1481-paragraph"
                                        >
                                            {{ "Dismiss" }}
                                        </p>
                                    </template>
                                </Button>
                            </template>
                            <template #slot_6360_54140>
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
                                            class="Pixso-paragraph-5603_17351 fill-brand60-1257_33467-paragraph text-text-smbold-423_3208 fill-gray0-white-67_3285-paragraph"
                                        >
                                            {{ "Go Pro" }}
                                        </p>
                                    </template>
                                </Button>
                            </template>
                        </NavFeaturedCard>
                    </slot>
                    <div id="6360_51972" class="stroke-wrapper-6360_51972">
                        <div class="Pixso-frame-6360_51972">
                            <div class="frame-content-6360_51972">
                                <div
                                    id="6360_51973"
                                    class="Pixso-frame-6360_51973"
                                >
                                    <div class="frame-content-6360_51973">
                                        <slot name="slot_6360_51974">
                                            <Avatar
                                                id="6360_51974"
                                                class="Pixso-instance-6360_51974"
                                                Size="md"
                                                Type="Image"
                                                Indicator="None"
                                            />
                                        </slot>
                                        <div
                                            id="6360_51975"
                                            class="Pixso-frame-6360_51975"
                                        >
                                            <div
                                                class="frame-content-6360_51975"
                                            >
                                                <slot name="slot_6360_51976">
                                                    <p
                                                        id="6360_51976"
                                                        class="Pixso-paragraph-6360_51976 fill-gray80-32_4123-paragraph text-text-mdbold-423_3205"
                                                    >
                                                        {{ "Azunyan U. Wu" }}
                                                    </p>
                                                </slot>
                                                <slot name="slot_6360_51977">
                                                    <p
                                                        id="6360_51977"
                                                        class="Pixso-paragraph-6360_51977 fill-gray60-83_2722-paragraph text-text-smmedium-5454_21607"
                                                    >
                                                        {{ "Basic Member" }}
                                                    </p>
                                                </slot>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <slot name="slot_6360_51978">
                                    <ButtonIcon
                                        id="6360_51978"
                                        class="Pixso-instance-6360_51978"
                                        Hierarchy="No Fill"
                                        Size="md"
                                        Color="Brand"
                                        State="Default"
                                    >
                                        <template #slot_5591_22532>
                                            <SignOut
                                                id="5591_22532"
                                                class="Pixso-instance-5591_22532"
                                            />
                                        </template>
                                    </ButtonIcon>
                                </slot>
                            </div>
                        </div>
                        <div
                            class="stroke-6360_51972 stroke-gray20-36_1844"
                        ></div>
                    </div>
                </div>
            </div>
            <div
                id="6360_52834"
                class="Pixso-symbol-6360_52834 fill-gray80-32_4123"
                v-if="
                    Theme === 'Dark' &&
                    IsMobile === 'False' &&
                    Type === 'Default'
                "
            >
                <div id="6360_52835" class="Pixso-frame-6360_52835">
                    <div class="frame-content-6360_52835">
                        <div id="6361_54550" class="Pixso-frame-6361_54550">
                            <div class="frame-content-6361_54550">
                                <slot name="slot_6361_54551">
                                    <Logo
                                        id="6361_54551"
                                        class="Pixso-instance-6361_54551"
                                        IsDarkMode="True"
                                    />
                                </slot>
                            </div>
                        </div>
                        <slot name="slot_6360_52838">
                            <InputText
                                id="6360_52838"
                                class="Pixso-instance-6360_52838"
                                :visible_5607_114="false"
                                :visible_5607_117="false"
                                State="Default"
                                Type="Default"
                                Size="md"
                            >
                                <template #slot_5976_53794>
                                    <InputTextBase
                                        id="5976_53794"
                                        class="Pixso-instance-5976_53794"
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
                                    </InputTextBase>
                                </template>
                            </InputText>
                        </slot>
                        <div id="6360_52839" class="Pixso-frame-6360_52839">
                            <slot name="slot_6360_52840">
                                <AppSidebarItem
                                    id="6360_52840"
                                    class="Pixso-instance-6360_52840"
                                    :visible_5982_36="false"
                                    :visible_5982_41="false"
                                    text_5982_39="Home"
                                    Theme="Dark"
                                    State="Default"
                                >
                                    <template #slot_6360_52671>
                                        <p
                                            id="6360_52671"
                                            class="Pixso-paragraph-6360_52671 fill-gray0-white-67_3285-paragraph text-text-mdbold-423_3205"
                                        >
                                            {{ "Home" }}
                                        </p>
                                    </template>
                                    <template #slot_6360_52672>
                                        <BadgeText
                                            id="6360_52672"
                                            class="Pixso-instance-6360_52672"
                                            :visible_5586_119="false"
                                            :visible_5586_121="false"
                                            :visible_5586_123="false"
                                            text_5588_129="10"
                                            Size="md"
                                            Color="Gray"
                                            Hierarchy="Primary"
                                            State="Default"
                                        >
                                            <template #slot_5588_11527>
                                                <p
                                                    id="5588_11527"
                                                    class="Pixso-paragraph-5588_11527 fill-gray0-white-67_3285-paragraph text-text-smsemibold-423_3209 fill-gray80-32_4123-paragraph"
                                                >
                                                    {{ "10" }}
                                                </p>
                                            </template>
                                        </BadgeText>
                                    </template>
                                </AppSidebarItem>
                            </slot>
                            <slot name="slot_6360_52841">
                                <AppSidebarItem
                                    id="6360_52841"
                                    class="Pixso-instance-6360_52841"
                                    :visible_5982_36="false"
                                    :visible_5982_41="false"
                                    :visible_5982_37="false"
                                    text_5982_39="Tasks"
                                    Theme="Dark"
                                    State="Default"
                                >
                                    <template #slot_6360_52671>
                                        <p
                                            id="6360_52671"
                                            class="Pixso-paragraph-6360_52671 fill-gray0-white-67_3285-paragraph text-text-mdbold-423_3205"
                                        >
                                            {{ "Tasks" }}
                                        </p>
                                    </template>
                                    <template #slot_6360_52670>
                                        <ListBullets
                                            id="6360_52670"
                                            class="Pixso-instance-6360_52670"
                                        />
                                    </template>
                                </AppSidebarItem>
                            </slot>
                            <slot name="slot_6360_52842">
                                <AppSidebarItem
                                    id="6360_52842"
                                    class="Pixso-instance-6360_52842"
                                    :visible_5982_36="false"
                                    :visible_5982_41="false"
                                    text_5982_39="Users"
                                    Theme="Dark"
                                    State="Default"
                                >
                                    <template #slot_6360_52671>
                                        <p
                                            id="6360_52671"
                                            class="Pixso-paragraph-6360_52671 fill-gray0-white-67_3285-paragraph text-text-mdbold-423_3205"
                                        >
                                            {{ "Users" }}
                                        </p>
                                    </template>
                                    <template #slot_6360_52670>
                                        <Users
                                            id="6360_52670"
                                            class="Pixso-instance-6360_52670"
                                        />
                                    </template>
                                    <template #slot_6360_52672>
                                        <BadgeText
                                            id="6360_52672"
                                            class="Pixso-instance-6360_52672"
                                            :visible_5586_119="false"
                                            :visible_5586_121="false"
                                            :visible_5586_123="false"
                                            text_5588_129="10"
                                            Size="md"
                                            Color="Gray"
                                            Hierarchy="Primary"
                                            State="Default"
                                        >
                                            <template #slot_5588_11527>
                                                <p
                                                    id="5588_11527"
                                                    class="Pixso-paragraph-5588_11527 fill-gray0-white-67_3285-paragraph text-text-smsemibold-423_3209 fill-brand60-1257_33467-paragraph"
                                                >
                                                    {{ "10" }}
                                                </p>
                                            </template>
                                        </BadgeText>
                                    </template>
                                </AppSidebarItem>
                            </slot>
                            <slot name="slot_6360_52843">
                                <AppSidebarItem
                                    id="6360_52843"
                                    class="Pixso-instance-6360_52843"
                                    :visible_5982_36="false"
                                    :visible_5982_41="false"
                                    :visible_5982_37="false"
                                    text_5982_39="APIs"
                                    Theme="Dark"
                                    State="Default"
                                >
                                    <template #slot_6360_52671>
                                        <p
                                            id="6360_52671"
                                            class="Pixso-paragraph-6360_52671 fill-gray0-white-67_3285-paragraph text-text-mdbold-423_3205"
                                        >
                                            {{ "APIs" }}
                                        </p>
                                    </template>
                                    <template #slot_6360_52670>
                                        <Cube
                                            id="6360_52670"
                                            class="Pixso-instance-6360_52670"
                                        />
                                    </template>
                                </AppSidebarItem>
                            </slot>
                            <slot name="slot_6360_52844">
                                <AppSidebarItem
                                    id="6360_52844"
                                    class="Pixso-instance-6360_52844"
                                    :visible_5982_36="false"
                                    :visible_5982_41="false"
                                    :visible_5982_37="false"
                                    text_5982_39="Subscription"
                                    Theme="Dark"
                                    State="Default"
                                >
                                    <template #slot_6360_52671>
                                        <p
                                            id="6360_52671"
                                            class="Pixso-paragraph-6360_52671 fill-gray0-white-67_3285-paragraph text-text-mdbold-423_3205"
                                        >
                                            {{ "Subscription" }}
                                        </p>
                                    </template>
                                    <template #slot_6360_52670>
                                        <CreditCard
                                            id="6360_52670"
                                            class="Pixso-instance-6360_52670"
                                        />
                                    </template>
                                </AppSidebarItem>
                            </slot>
                            <slot name="slot_6360_52845">
                                <AppSidebarItem
                                    id="6360_52845"
                                    class="Pixso-instance-6360_52845"
                                    :visible_5982_36="false"
                                    :visible_5982_41="false"
                                    :visible_5982_37="false"
                                    text_5982_39="Settings"
                                    Theme="Dark"
                                    State="Default"
                                >
                                    <template #slot_6360_52671>
                                        <p
                                            id="6360_52671"
                                            class="Pixso-paragraph-6360_52671 fill-gray0-white-67_3285-paragraph text-text-mdbold-423_3205"
                                        >
                                            {{ "Settings" }}
                                        </p>
                                    </template>
                                    <template #slot_6360_52670>
                                        <GearSix
                                            id="6360_52670"
                                            class="Pixso-instance-6360_52670"
                                        />
                                    </template>
                                </AppSidebarItem>
                            </slot>
                            <slot name="slot_6360_52846">
                                <AppSidebarItem
                                    id="6360_52846"
                                    class="Pixso-instance-6360_52846"
                                    :visible_5982_36="false"
                                    :visible_5982_41="false"
                                    :visible_5982_37="false"
                                    text_5982_39="Help &amp; Support"
                                    Theme="Dark"
                                    State="Default"
                                >
                                    <template #slot_6360_52671>
                                        <p
                                            id="6360_52671"
                                            class="Pixso-paragraph-6360_52671 fill-gray0-white-67_3285-paragraph text-text-mdbold-423_3205"
                                        >
                                            {{ "Help & Support" }}
                                        </p>
                                    </template>
                                    <template #slot_6360_52670>
                                        <ChatTeardropDots
                                            id="6360_52670"
                                            class="Pixso-instance-6360_52670"
                                        />
                                    </template>
                                </AppSidebarItem>
                            </slot>
                        </div>
                    </div>
                </div>
                <div id="6360_52847" class="Pixso-frame-6360_52847">
                    <slot name="slot_6360_52848">
                        <NavFeaturedCard
                            id="6360_52848"
                            class="Pixso-instance-6360_52848"
                            Theme="Dark"
                            Type="Icon"
                        >
                            <template #slot_6360_54327>
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
                                            class="Pixso-paragraph-5603_17111 fill-gray60-83_2722-paragraph text-text-smbold-423_3208 fill-brand20-1257_33462-paragraph"
                                        >
                                            {{ "Dismiss" }}
                                        </p>
                                    </template>
                                </Button>
                            </template>
                            <template #slot_6360_54328>
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
                                            class="Pixso-paragraph-5603_17351 fill-brand60-1257_33467-paragraph text-text-smbold-423_3208 fill-gray0-white-67_3285-paragraph"
                                        >
                                            {{ "Go Pro" }}
                                        </p>
                                    </template>
                                </Button>
                            </template>
                        </NavFeaturedCard>
                    </slot>
                    <div id="6360_52849" class="stroke-wrapper-6360_52849">
                        <div class="Pixso-frame-6360_52849">
                            <div class="frame-content-6360_52849">
                                <div
                                    id="6360_52850"
                                    class="Pixso-frame-6360_52850"
                                >
                                    <div class="frame-content-6360_52850">
                                        <slot name="slot_6360_52851">
                                            <Avatar
                                                id="6360_52851"
                                                class="Pixso-instance-6360_52851"
                                                Size="md"
                                                Type="Image"
                                                Indicator="None"
                                            />
                                        </slot>
                                        <div
                                            id="6360_52852"
                                            class="Pixso-frame-6360_52852"
                                        >
                                            <div
                                                class="frame-content-6360_52852"
                                            >
                                                <slot name="slot_6360_52853">
                                                    <p
                                                        id="6360_52853"
                                                        class="Pixso-paragraph-6360_52853 fill-gray0-white-67_3285-paragraph text-text-mdbold-423_3205"
                                                    >
                                                        {{ "Azunyan U. Wu" }}
                                                    </p>
                                                </slot>
                                                <slot name="slot_6360_52854">
                                                    <p
                                                        id="6360_52854"
                                                        class="Pixso-paragraph-6360_52854 fill-gray20-36_1844-paragraph text-text-smmedium-5454_21607"
                                                    >
                                                        {{ "Basic Member" }}
                                                    </p>
                                                </slot>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <slot name="slot_6360_52855">
                                    <ButtonIcon
                                        id="6360_52855"
                                        class="Pixso-instance-6360_52855"
                                        Hierarchy="No Fill"
                                        Size="md"
                                        Color="Brand"
                                        State="Default"
                                    >
                                        <template #slot_5591_22532>
                                            <SignOut
                                                id="5591_22532"
                                                class="Pixso-instance-5591_22532"
                                            />
                                        </template>
                                    </ButtonIcon>
                                </slot>
                            </div>
                        </div>
                        <div
                            class="stroke-6360_52849 stroke-gray60-83_2722"
                        ></div>
                    </div>
                </div>
            </div>
            <div
                id="5978_31519"
                class="Pixso-symbol-5978_31519 fill-brand60-1257_33467"
                v-if="
                    Theme === 'Brand' &&
                    IsMobile === 'False' &&
                    Type === 'Default'
                "
            >
                <div id="5982_58829" class="Pixso-frame-5982_58829">
                    <div id="5982_57987" class="Pixso-frame-5982_57987">
                        <div class="frame-content-5982_57987">
                            <slot name="slot_5976_55198">
                                <Logo
                                    id="5976_55198"
                                    class="Pixso-instance-5976_55198"
                                    IsDarkMode="True"
                                >
                                    <template #slot_5572_73848>
                                        <Logomark
                                            id="5572_73848"
                                            class="Pixso-instance-5572_73848"
                                        />
                                    </template>
                                </Logo>
                            </slot>
                        </div>
                    </div>
                    <slot name="slot_5976_58202">
                        <InputText
                            id="5976_58202"
                            class="Pixso-instance-5976_58202"
                            :visible_5607_114="false"
                            :visible_5607_117="false"
                            State="Default"
                            Type="Default"
                            Size="md"
                        >
                            <template #slot_5976_53794>
                                <InputTextBase
                                    id="5976_53794"
                                    class="Pixso-instance-5976_53794"
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
                                </InputTextBase>
                            </template>
                        </InputText>
                    </slot>
                    <div id="5982_55242" class="Pixso-frame-5982_55242">
                        <slot name="slot_5980_54129">
                            <AppSidebarItem
                                id="5980_54129"
                                class="Pixso-instance-5980_54129"
                                :visible_5982_36="false"
                                :visible_5982_41="false"
                                text_5982_39="Home"
                                Theme="Brand"
                                State="Default"
                            >
                                <template #slot_5982_54581>
                                    <p
                                        id="5982_54581"
                                        class="Pixso-paragraph-5982_54581 fill-gray0-white-67_3285-paragraph text-text-mdbold-423_3205"
                                    >
                                        {{ "Home" }}
                                    </p>
                                </template>
                                <template #slot_5982_54582>
                                    <BadgeText
                                        id="5982_54582"
                                        class="Pixso-instance-5982_54582"
                                        :visible_5586_119="false"
                                        :visible_5586_121="false"
                                        :visible_5586_123="false"
                                        text_5588_129="10"
                                        Size="md"
                                        Color="Gray"
                                        Hierarchy="Primary"
                                        State="Default"
                                    >
                                        <template #slot_5588_11527>
                                            <p
                                                id="5588_11527"
                                                class="Pixso-paragraph-5588_11527 fill-gray0-white-67_3285-paragraph text-text-smsemibold-423_3209 fill-brand60-1257_33467-paragraph"
                                            >
                                                {{ "10" }}
                                            </p>
                                        </template>
                                    </BadgeText>
                                </template>
                            </AppSidebarItem>
                        </slot>
                        <slot name="slot_5982_54782">
                            <AppSidebarItem
                                id="5982_54782"
                                class="Pixso-instance-5982_54782"
                                :visible_5982_36="false"
                                :visible_5982_41="false"
                                :visible_5982_37="false"
                                text_5982_39="Tasks"
                                Theme="Brand"
                                State="Default"
                            >
                                <template #slot_5982_54581>
                                    <p
                                        id="5982_54581"
                                        class="Pixso-paragraph-5982_54581 fill-gray0-white-67_3285-paragraph text-text-mdbold-423_3205"
                                    >
                                        {{ "Tasks" }}
                                    </p>
                                </template>
                                <template #slot_5982_54580>
                                    <ListBullets
                                        id="5982_54580"
                                        class="Pixso-instance-5982_54580"
                                    />
                                </template>
                            </AppSidebarItem>
                        </slot>
                        <slot name="slot_5982_54844">
                            <AppSidebarItem
                                id="5982_54844"
                                class="Pixso-instance-5982_54844"
                                :visible_5982_36="false"
                                :visible_5982_41="false"
                                text_5982_39="Users"
                                Theme="Brand"
                                State="Default"
                            >
                                <template #slot_5982_54581>
                                    <p
                                        id="5982_54581"
                                        class="Pixso-paragraph-5982_54581 fill-gray0-white-67_3285-paragraph text-text-mdbold-423_3205"
                                    >
                                        {{ "Users" }}
                                    </p>
                                </template>
                                <template #slot_5982_54580>
                                    <Users
                                        id="5982_54580"
                                        class="Pixso-instance-5982_54580"
                                    />
                                </template>
                                <template #slot_5982_54582>
                                    <BadgeText
                                        id="5982_54582"
                                        class="Pixso-instance-5982_54582"
                                        :visible_5586_119="false"
                                        :visible_5586_121="false"
                                        :visible_5586_123="false"
                                        text_5588_129="10"
                                        Size="md"
                                        Color="Gray"
                                        Hierarchy="Primary"
                                        State="Default"
                                    >
                                        <template #slot_5588_11527>
                                            <p
                                                id="5588_11527"
                                                class="Pixso-paragraph-5588_11527 fill-gray0-white-67_3285-paragraph text-text-smsemibold-423_3209"
                                            >
                                                {{ "10" }}
                                            </p>
                                        </template>
                                    </BadgeText>
                                </template>
                            </AppSidebarItem>
                        </slot>
                        <slot name="slot_5982_54921">
                            <AppSidebarItem
                                id="5982_54921"
                                class="Pixso-instance-5982_54921"
                                :visible_5982_36="false"
                                :visible_5982_41="false"
                                :visible_5982_37="false"
                                text_5982_39="APIs"
                                Theme="Brand"
                                State="Default"
                            >
                                <template #slot_5982_54581>
                                    <p
                                        id="5982_54581"
                                        class="Pixso-paragraph-5982_54581 fill-gray0-white-67_3285-paragraph text-text-mdbold-423_3205"
                                    >
                                        {{ "APIs" }}
                                    </p>
                                </template>
                                <template #slot_5982_54580>
                                    <Cube
                                        id="5982_54580"
                                        class="Pixso-instance-5982_54580"
                                    />
                                </template>
                            </AppSidebarItem>
                        </slot>
                        <slot name="slot_5982_55013">
                            <AppSidebarItem
                                id="5982_55013"
                                class="Pixso-instance-5982_55013"
                                :visible_5982_36="false"
                                :visible_5982_41="false"
                                :visible_5982_37="false"
                                text_5982_39="Subscription"
                                Theme="Brand"
                                State="Default"
                            >
                                <template #slot_5982_54581>
                                    <p
                                        id="5982_54581"
                                        class="Pixso-paragraph-5982_54581 fill-gray0-white-67_3285-paragraph text-text-mdbold-423_3205"
                                    >
                                        {{ "Subscription" }}
                                    </p>
                                </template>
                                <template #slot_5982_54580>
                                    <CreditCard
                                        id="5982_54580"
                                        class="Pixso-instance-5982_54580"
                                    />
                                </template>
                            </AppSidebarItem>
                        </slot>
                        <slot name="slot_5982_55120">
                            <AppSidebarItem
                                id="5982_55120"
                                class="Pixso-instance-5982_55120"
                                :visible_5982_36="false"
                                :visible_5982_41="false"
                                :visible_5982_37="false"
                                text_5982_39="Settings"
                                Theme="Brand"
                                State="Default"
                            >
                                <template #slot_5982_54581>
                                    <p
                                        id="5982_54581"
                                        class="Pixso-paragraph-5982_54581 fill-gray0-white-67_3285-paragraph text-text-mdbold-423_3205"
                                    >
                                        {{ "Settings" }}
                                    </p>
                                </template>
                                <template #slot_5982_54580>
                                    <GearSix
                                        id="5982_54580"
                                        class="Pixso-instance-5982_54580"
                                    />
                                </template>
                            </AppSidebarItem>
                        </slot>
                        <slot name="slot_5982_58638">
                            <AppSidebarItem
                                id="5982_58638"
                                class="Pixso-instance-5982_58638"
                                :visible_5982_36="false"
                                :visible_5982_41="false"
                                :visible_5982_37="false"
                                text_5982_39="Help &amp; Support"
                                Theme="Brand"
                                State="Default"
                            >
                                <template #slot_5982_54581>
                                    <p
                                        id="5982_54581"
                                        class="Pixso-paragraph-5982_54581 fill-gray0-white-67_3285-paragraph text-text-mdbold-423_3205"
                                    >
                                        {{ "Help & Support" }}
                                    </p>
                                </template>
                                <template #slot_5982_54580>
                                    <ChatTeardropDots
                                        id="5982_54580"
                                        class="Pixso-instance-5982_54580"
                                    />
                                </template>
                            </AppSidebarItem>
                        </slot>
                    </div>
                </div>
                <div id="5982_58728" class="Pixso-frame-5982_58728">
                    <slot name="slot_6360_37700">
                        <NavFeaturedCard
                            id="6360_37700"
                            class="Pixso-instance-6360_37700"
                            Theme="Brand"
                            Type="Icon"
                        >
                            <template #slot_6360_36912>
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
                                            class="Pixso-paragraph-5603_17111 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                                        >
                                            {{ "Dismiss" }}
                                        </p>
                                    </template>
                                </Button>
                            </template>
                            <template #slot_6360_36913>
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
                                            class="Pixso-paragraph-5603_17351 fill-brand60-1257_33467-paragraph text-text-smbold-423_3208"
                                        >
                                            {{ "Go Pro" }}
                                        </p>
                                    </template>
                                </Button>
                            </template>
                        </NavFeaturedCard>
                    </slot>
                    <div id="5982_57071" class="stroke-wrapper-5982_57071">
                        <div class="Pixso-frame-5982_57071">
                            <div class="frame-content-5982_57071">
                                <div
                                    id="5982_56616"
                                    class="Pixso-frame-5982_56616"
                                >
                                    <div class="frame-content-5982_56616">
                                        <slot name="slot_5982_55911">
                                            <Avatar
                                                id="5982_55911"
                                                class="Pixso-instance-5982_55911"
                                                Size="md"
                                                Type="Image"
                                                Indicator="None"
                                            />
                                        </slot>
                                        <div
                                            id="5982_56474"
                                            class="Pixso-frame-5982_56474"
                                        >
                                            <div
                                                class="frame-content-5982_56474"
                                            >
                                                <slot name="slot_5982_56193">
                                                    <p
                                                        id="5982_56193"
                                                        class="Pixso-paragraph-5982_56193 fill-gray0-white-67_3285-paragraph text-text-mdbold-423_3205"
                                                    >
                                                        {{ "Azunyan U. Wu" }}
                                                    </p>
                                                </slot>
                                                <slot name="slot_5982_56333">
                                                    <p
                                                        id="5982_56333"
                                                        class="Pixso-paragraph-5982_56333 fill-brand20-1257_33462-paragraph text-text-smmedium-5454_21607"
                                                    >
                                                        {{ "Basic Member" }}
                                                    </p>
                                                </slot>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <slot name="slot_5982_56899">
                                    <ButtonIcon
                                        id="5982_56899"
                                        class="Pixso-instance-5982_56899"
                                        Hierarchy="Primary"
                                        Size="md"
                                        Color="Brand"
                                        State="Default"
                                    >
                                        <template #slot_5591_22530>
                                            <SignOut
                                                id="5591_22530"
                                                class="Pixso-instance-5591_22530"
                                            />
                                        </template>
                                    </ButtonIcon>
                                </slot>
                            </div>
                        </div>
                        <div
                            class="stroke-5982_57071 stroke-brand50-1257_33466"
                        ></div>
                    </div>
                </div>
            </div>
            <div
                id="5648_26772"
                class="stroke-wrapper-5648_26772"
                v-if="
                    Theme === 'White' && IsMobile === 'False' && Type === 'Slim'
                "
            >
                <div class="Pixso-symbol-5648_26772 fill-gray0-white-67_3285">
                    <div id="5648_26771" class="Pixso-frame-5648_26771">
                        <slot name="slot_5648_26648">
                            <Logomark
                                id="5648_26648"
                                class="Pixso-instance-5648_26648"
                                Background="Gradient"
                            />
                        </slot>
                        <div id="5648_26641" class="Pixso-frame-5648_26641">
                            <slot name="slot_5648_26642">
                                <ButtonIcon
                                    id="5648_26642"
                                    class="Pixso-instance-5648_26642"
                                    Hierarchy="Secondary"
                                    Size="lg"
                                    Color="Gray"
                                    State="Hover"
                                >
                                    <template #slot_5590_21884>
                                        <HouseSimple
                                            id="5590_21884"
                                            class="Pixso-instance-5590_21884"
                                        />
                                    </template>
                                </ButtonIcon>
                            </slot>
                            <slot name="slot_5648_26643">
                                <ButtonIcon
                                    id="5648_26643"
                                    class="Pixso-instance-5648_26643"
                                    Hierarchy="No Fill"
                                    Size="lg"
                                    Color="Gray"
                                    State="Default"
                                >
                                    <template #slot_5590_22160>
                                        <ChartBar
                                            id="5590_22160"
                                            class="Pixso-instance-5590_22160"
                                        />
                                    </template>
                                </ButtonIcon>
                            </slot>
                            <slot name="slot_5648_26644">
                                <ButtonIcon
                                    id="5648_26644"
                                    class="Pixso-instance-5648_26644"
                                    Hierarchy="No Fill"
                                    Size="lg"
                                    Color="Gray"
                                    State="Default"
                                >
                                    <template #slot_5590_22160>
                                        <User
                                            id="5590_22160"
                                            class="Pixso-instance-5590_22160"
                                        />
                                    </template>
                                </ButtonIcon>
                            </slot>
                            <slot name="slot_5648_26645">
                                <ButtonIcon
                                    id="5648_26645"
                                    class="Pixso-instance-5648_26645"
                                    Hierarchy="No Fill"
                                    Size="lg"
                                    Color="Gray"
                                    State="Default"
                                >
                                    <template #slot_5590_22160>
                                        <CalendarBlank
                                            id="5590_22160"
                                            class="Pixso-instance-5590_22160"
                                        />
                                    </template>
                                </ButtonIcon>
                            </slot>
                            <slot name="slot_5648_26766">
                                <ButtonIcon
                                    id="5648_26766"
                                    class="Pixso-instance-5648_26766"
                                    Hierarchy="No Fill"
                                    Size="lg"
                                    Color="Gray"
                                    State="Default"
                                >
                                    <template #slot_5590_22160>
                                        <Lightning
                                            id="5590_22160"
                                            class="Pixso-instance-5590_22160"
                                        />
                                    </template>
                                </ButtonIcon>
                            </slot>
                            <slot name="slot_5648_26646">
                                <ButtonIcon
                                    id="5648_26646"
                                    class="Pixso-instance-5648_26646"
                                    Hierarchy="No Fill"
                                    Size="lg"
                                    Color="Gray"
                                    State="Default"
                                >
                                    <template #slot_5590_22160>
                                        <BellSimple
                                            id="5590_22160"
                                            class="Pixso-instance-5590_22160"
                                        />
                                    </template>
                                </ButtonIcon>
                            </slot>
                        </div>
                    </div>
                    <div id="5648_26765" class="Pixso-frame-5648_26765">
                        <slot name="slot_5648_26647">
                            <ButtonIcon
                                id="5648_26647"
                                class="Pixso-instance-5648_26647"
                                Hierarchy="No Fill"
                                Size="lg"
                                Color="Gray"
                                State="Default"
                            >
                                <template #slot_5590_22160>
                                    <GearSix
                                        id="5590_22160"
                                        class="Pixso-instance-5590_22160"
                                    />
                                </template>
                            </ButtonIcon>
                        </slot>
                        <slot name="slot_5648_26649">
                            <Avatar
                                id="5648_26649"
                                class="Pixso-instance-5648_26649"
                                Size="lg"
                                Type="Image"
                                Indicator="None"
                            />
                        </slot>
                    </div>
                </div>
                <div class="stroke-5648_26772 stroke-gray20-36_1844"></div>
            </div>
            <div
                id="6361_54407"
                class="Pixso-symbol-6361_54407 fill-gray5-32_4120"
                v-if="
                    Theme === 'Light Gray' &&
                    IsMobile === 'False' &&
                    Type === 'Slim'
                "
            >
                <div id="6361_54408" class="Pixso-frame-6361_54408">
                    <slot name="slot_6361_54409">
                        <Logomark
                            id="6361_54409"
                            class="Pixso-instance-6361_54409"
                            Background="Gradient"
                        />
                    </slot>
                    <div id="6361_54410" class="Pixso-frame-6361_54410">
                        <slot name="slot_6361_54411">
                            <ButtonIcon
                                id="6361_54411"
                                class="Pixso-instance-6361_54411"
                                Hierarchy="Secondary"
                                Size="lg"
                                Color="Gray"
                                State="Hover"
                            >
                                <template #slot_5590_21884>
                                    <HouseSimple
                                        id="5590_21884"
                                        class="Pixso-instance-5590_21884"
                                    />
                                </template>
                            </ButtonIcon>
                        </slot>
                        <slot name="slot_6361_54412">
                            <ButtonIcon
                                id="6361_54412"
                                class="Pixso-instance-6361_54412"
                                Hierarchy="No Fill"
                                Size="lg"
                                Color="Gray"
                                State="Default"
                            >
                                <template #slot_5590_22160>
                                    <ChartBar
                                        id="5590_22160"
                                        class="Pixso-instance-5590_22160"
                                    />
                                </template>
                            </ButtonIcon>
                        </slot>
                        <slot name="slot_6361_54413">
                            <ButtonIcon
                                id="6361_54413"
                                class="Pixso-instance-6361_54413"
                                Hierarchy="No Fill"
                                Size="lg"
                                Color="Gray"
                                State="Default"
                            >
                                <template #slot_5590_22160>
                                    <User
                                        id="5590_22160"
                                        class="Pixso-instance-5590_22160"
                                    />
                                </template>
                            </ButtonIcon>
                        </slot>
                        <slot name="slot_6361_54414">
                            <ButtonIcon
                                id="6361_54414"
                                class="Pixso-instance-6361_54414"
                                Hierarchy="No Fill"
                                Size="lg"
                                Color="Gray"
                                State="Default"
                            >
                                <template #slot_5590_22160>
                                    <CalendarBlank
                                        id="5590_22160"
                                        class="Pixso-instance-5590_22160"
                                    />
                                </template>
                            </ButtonIcon>
                        </slot>
                        <slot name="slot_6361_54415">
                            <ButtonIcon
                                id="6361_54415"
                                class="Pixso-instance-6361_54415"
                                Hierarchy="No Fill"
                                Size="lg"
                                Color="Gray"
                                State="Default"
                            >
                                <template #slot_5590_22160>
                                    <Lightning
                                        id="5590_22160"
                                        class="Pixso-instance-5590_22160"
                                    />
                                </template>
                            </ButtonIcon>
                        </slot>
                        <slot name="slot_6361_54416">
                            <ButtonIcon
                                id="6361_54416"
                                class="Pixso-instance-6361_54416"
                                Hierarchy="No Fill"
                                Size="lg"
                                Color="Gray"
                                State="Default"
                            >
                                <template #slot_5590_22160>
                                    <BellSimple
                                        id="5590_22160"
                                        class="Pixso-instance-5590_22160"
                                    />
                                </template>
                            </ButtonIcon>
                        </slot>
                    </div>
                </div>
                <div id="6361_54417" class="Pixso-frame-6361_54417">
                    <slot name="slot_6361_54418">
                        <ButtonIcon
                            id="6361_54418"
                            class="Pixso-instance-6361_54418"
                            Hierarchy="No Fill"
                            Size="lg"
                            Color="Gray"
                            State="Default"
                        >
                            <template #slot_5590_22160>
                                <GearSix
                                    id="5590_22160"
                                    class="Pixso-instance-5590_22160"
                                />
                            </template>
                        </ButtonIcon>
                    </slot>
                    <slot name="slot_6361_54419">
                        <Avatar
                            id="6361_54419"
                            class="Pixso-instance-6361_54419"
                            Size="lg"
                            Type="Image"
                            Indicator="None"
                        />
                    </slot>
                </div>
            </div>
            <div
                id="5648_26862"
                class="Pixso-symbol-5648_26862 fill-brand60-1257_33467"
                v-if="
                    Theme === 'Brand' && IsMobile === 'False' && Type === 'Slim'
                "
            >
                <div id="5648_26863" class="Pixso-frame-5648_26863">
                    <slot name="slot_5648_26864">
                        <Logomark
                            id="5648_26864"
                            class="Pixso-instance-5648_26864"
                            Background="White"
                        />
                    </slot>
                    <div id="5648_26865" class="Pixso-frame-5648_26865">
                        <slot name="slot_5648_26866">
                            <ButtonIcon
                                id="5648_26866"
                                class="Pixso-instance-5648_26866"
                                Hierarchy="Secondary"
                                Size="lg"
                                Color="Gray"
                                State="Hover"
                            >
                                <template #slot_5590_21884>
                                    <HouseSimple
                                        id="5590_21884"
                                        class="Pixso-instance-5590_21884"
                                    />
                                </template>
                            </ButtonIcon>
                        </slot>
                        <slot name="slot_5648_26867">
                            <ButtonIcon
                                id="5648_26867"
                                class="Pixso-instance-5648_26867"
                                Hierarchy="No Fill"
                                Size="lg"
                                Color="Gray"
                                State="Default"
                            >
                                <template #slot_5590_22160>
                                    <ChartBar
                                        id="5590_22160"
                                        class="Pixso-instance-5590_22160"
                                    />
                                </template>
                            </ButtonIcon>
                        </slot>
                        <slot name="slot_5648_26868">
                            <ButtonIcon
                                id="5648_26868"
                                class="Pixso-instance-5648_26868"
                                Hierarchy="No Fill"
                                Size="lg"
                                Color="Gray"
                                State="Default"
                            >
                                <template #slot_5590_22160>
                                    <User
                                        id="5590_22160"
                                        class="Pixso-instance-5590_22160"
                                    />
                                </template>
                            </ButtonIcon>
                        </slot>
                        <slot name="slot_5648_26869">
                            <ButtonIcon
                                id="5648_26869"
                                class="Pixso-instance-5648_26869"
                                Hierarchy="No Fill"
                                Size="lg"
                                Color="Gray"
                                State="Default"
                            >
                                <template #slot_5590_22160>
                                    <CalendarBlank
                                        id="5590_22160"
                                        class="Pixso-instance-5590_22160"
                                    />
                                </template>
                            </ButtonIcon>
                        </slot>
                        <slot name="slot_5648_26870">
                            <ButtonIcon
                                id="5648_26870"
                                class="Pixso-instance-5648_26870"
                                Hierarchy="No Fill"
                                Size="lg"
                                Color="Gray"
                                State="Default"
                            >
                                <template #slot_5590_22160>
                                    <Lightning
                                        id="5590_22160"
                                        class="Pixso-instance-5590_22160"
                                    />
                                </template>
                            </ButtonIcon>
                        </slot>
                        <slot name="slot_5648_26871">
                            <ButtonIcon
                                id="5648_26871"
                                class="Pixso-instance-5648_26871"
                                Hierarchy="No Fill"
                                Size="lg"
                                Color="Gray"
                                State="Default"
                            >
                                <template #slot_5590_22160>
                                    <BellSimple
                                        id="5590_22160"
                                        class="Pixso-instance-5590_22160"
                                    />
                                </template>
                            </ButtonIcon>
                        </slot>
                    </div>
                </div>
                <div id="5648_26886" class="Pixso-frame-5648_26886">
                    <slot name="slot_5648_26887">
                        <ButtonIcon
                            id="5648_26887"
                            class="Pixso-instance-5648_26887"
                            Hierarchy="No Fill"
                            Size="lg"
                            Color="Gray"
                            State="Default"
                        >
                            <template #slot_5590_22160>
                                <GearSix
                                    id="5590_22160"
                                    class="Pixso-instance-5590_22160"
                                />
                            </template>
                        </ButtonIcon>
                    </slot>
                    <slot name="slot_5648_26888">
                        <Avatar
                            id="5648_26888"
                            class="Pixso-instance-5648_26888"
                            Size="lg"
                            Type="Image"
                            Indicator="None"
                        />
                    </slot>
                </div>
            </div>
            <div
                id="6361_54484"
                class="Pixso-symbol-6361_54484 fill-gray80-32_4123"
                v-if="
                    Theme === 'Dark' && IsMobile === 'False' && Type === 'Slim'
                "
            >
                <div id="6361_54485" class="Pixso-frame-6361_54485">
                    <slot name="slot_6361_54486">
                        <Logomark
                            id="6361_54486"
                            class="Pixso-instance-6361_54486"
                            Background="White"
                        />
                    </slot>
                    <div id="6361_54487" class="Pixso-frame-6361_54487">
                        <slot name="slot_6361_54488">
                            <ButtonIcon
                                id="6361_54488"
                                class="Pixso-instance-6361_54488"
                                Hierarchy="Secondary"
                                Size="lg"
                                Color="Gray"
                                State="Hover"
                            >
                                <template #slot_5590_21884>
                                    <HouseSimple
                                        id="5590_21884"
                                        class="Pixso-instance-5590_21884"
                                    />
                                </template>
                            </ButtonIcon>
                        </slot>
                        <slot name="slot_6361_54489">
                            <ButtonIcon
                                id="6361_54489"
                                class="Pixso-instance-6361_54489"
                                Hierarchy="No Fill"
                                Size="lg"
                                Color="Gray"
                                State="Default"
                            >
                                <template #slot_5590_22160>
                                    <ChartBar
                                        id="5590_22160"
                                        class="Pixso-instance-5590_22160"
                                    />
                                </template>
                            </ButtonIcon>
                        </slot>
                        <slot name="slot_6361_54490">
                            <ButtonIcon
                                id="6361_54490"
                                class="Pixso-instance-6361_54490"
                                Hierarchy="No Fill"
                                Size="lg"
                                Color="Gray"
                                State="Default"
                            >
                                <template #slot_5590_22160>
                                    <User
                                        id="5590_22160"
                                        class="Pixso-instance-5590_22160"
                                    />
                                </template>
                            </ButtonIcon>
                        </slot>
                        <slot name="slot_6361_54491">
                            <ButtonIcon
                                id="6361_54491"
                                class="Pixso-instance-6361_54491"
                                Hierarchy="No Fill"
                                Size="lg"
                                Color="Gray"
                                State="Default"
                            >
                                <template #slot_5590_22160>
                                    <CalendarBlank
                                        id="5590_22160"
                                        class="Pixso-instance-5590_22160"
                                    />
                                </template>
                            </ButtonIcon>
                        </slot>
                        <slot name="slot_6361_54492">
                            <ButtonIcon
                                id="6361_54492"
                                class="Pixso-instance-6361_54492"
                                Hierarchy="No Fill"
                                Size="lg"
                                Color="Gray"
                                State="Default"
                            >
                                <template #slot_5590_22160>
                                    <Lightning
                                        id="5590_22160"
                                        class="Pixso-instance-5590_22160"
                                    />
                                </template>
                            </ButtonIcon>
                        </slot>
                        <slot name="slot_6361_54493">
                            <ButtonIcon
                                id="6361_54493"
                                class="Pixso-instance-6361_54493"
                                Hierarchy="No Fill"
                                Size="lg"
                                Color="Gray"
                                State="Default"
                            >
                                <template #slot_5590_22160>
                                    <BellSimple
                                        id="5590_22160"
                                        class="Pixso-instance-5590_22160"
                                    />
                                </template>
                            </ButtonIcon>
                        </slot>
                    </div>
                </div>
                <div id="6361_54494" class="Pixso-frame-6361_54494">
                    <slot name="slot_6361_54495">
                        <ButtonIcon
                            id="6361_54495"
                            class="Pixso-instance-6361_54495"
                            Hierarchy="No Fill"
                            Size="lg"
                            Color="Gray"
                            State="Default"
                        >
                            <template #slot_5590_22160>
                                <GearSix
                                    id="5590_22160"
                                    class="Pixso-instance-5590_22160"
                                />
                            </template>
                        </ButtonIcon>
                    </slot>
                    <slot name="slot_6361_54496">
                        <Avatar
                            id="6361_54496"
                            class="Pixso-instance-6361_54496"
                            Size="lg"
                            Type="Image"
                            Indicator="None"
                        />
                    </slot>
                </div>
            </div>
            <div
                id="6012_50232"
                class="Pixso-symbol-6012_50232 fill-brand60-1257_33467"
                v-if="
                    Theme === 'Brand' && IsMobile === 'True' && Type === 'Slim'
                "
            >
                <div id="6012_50233" class="Pixso-frame-6012_50233">
                    <slot name="slot_6012_50234">
                        <Logo
                            id="6012_50234"
                            class="Pixso-instance-6012_50234"
                            IsDarkMode="True"
                        >
                            <template #slot_5572_73848>
                                <Logomark
                                    id="5572_73848"
                                    class="Pixso-instance-5572_73848"
                                />
                            </template>
                        </Logo>
                    </slot>
                </div>
                <slot name="slot_6012_50235">
                    <ButtonIcon
                        id="6012_50235"
                        class="Pixso-instance-6012_50235"
                        Hierarchy="No Fill"
                        Size="md"
                        Color="Gray"
                        State="Default"
                    >
                        <template #slot_5590_22158>
                            <List
                                id="5590_22158"
                                class="Pixso-instance-5590_22158"
                            />
                        </template>
                    </ButtonIcon>
                </slot>
            </div>
            <div
                id="6361_54541"
                class="Pixso-symbol-6361_54541 fill-gray80-32_4123"
                v-if="
                    Theme === 'Dark' && IsMobile === 'True' && Type === 'Slim'
                "
            >
                <div id="6361_54542" class="Pixso-frame-6361_54542">
                    <slot name="slot_6361_54543">
                        <Logo
                            id="6361_54543"
                            class="Pixso-instance-6361_54543"
                            IsDarkMode="True"
                        />
                    </slot>
                </div>
                <slot name="slot_6361_54544">
                    <ButtonIcon
                        id="6361_54544"
                        class="Pixso-instance-6361_54544"
                        Hierarchy="No Fill"
                        Size="md"
                        Color="Gray"
                        State="Default"
                    >
                        <template #slot_5590_22158>
                            <List
                                id="5590_22158"
                                class="Pixso-instance-5590_22158"
                            />
                        </template>
                    </ButtonIcon>
                </slot>
            </div>
            <div
                id="6012_50236"
                class="stroke-wrapper-6012_50236"
                v-if="
                    Theme === 'White' && IsMobile === 'True' && Type === 'Slim'
                "
            >
                <div class="Pixso-symbol-6012_50236 fill-gray0-white-67_3285">
                    <div id="6012_50237" class="Pixso-frame-6012_50237">
                        <slot name="slot_6012_50238">
                            <Logo
                                id="6012_50238"
                                class="Pixso-instance-6012_50238"
                                IsDarkMode="False"
                            />
                        </slot>
                    </div>
                    <slot name="slot_6012_50239">
                        <ButtonIcon
                            id="6012_50239"
                            class="Pixso-instance-6012_50239"
                            Hierarchy="No Fill"
                            Size="md"
                            Color="Gray"
                            State="Default"
                        >
                            <template #slot_5590_22158>
                                <List
                                    id="5590_22158"
                                    class="Pixso-instance-5590_22158"
                                />
                            </template>
                        </ButtonIcon>
                    </slot>
                </div>
                <div class="stroke-6012_50236 stroke-gray20-36_1844"></div>
            </div>
            <div
                id="6361_54522"
                class="Pixso-symbol-6361_54522 fill-gray5-32_4120"
                v-if="
                    Theme === 'Light Gray' &&
                    IsMobile === 'True' &&
                    Type === 'Slim'
                "
            >
                <div id="6361_54523" class="Pixso-frame-6361_54523">
                    <slot name="slot_6361_54524">
                        <Logo
                            id="6361_54524"
                            class="Pixso-instance-6361_54524"
                            IsDarkMode="False"
                        />
                    </slot>
                </div>
                <slot name="slot_6361_54525">
                    <ButtonIcon
                        id="6361_54525"
                        class="Pixso-instance-6361_54525"
                        Hierarchy="No Fill"
                        Size="md"
                        Color="Gray"
                        State="Default"
                    >
                        <template #slot_5590_22158>
                            <List
                                id="5590_22158"
                                class="Pixso-instance-5590_22158"
                            />
                        </template>
                    </ButtonIcon>
                </slot>
            </div>
            <div
                id="6361_54651"
                class="Pixso-symbol-6361_54651 fill-brand60-1257_33467"
                v-if="
                    Theme === 'Brand' &&
                    IsMobile === 'True' &&
                    Type === 'Default'
                "
            >
                <div id="6361_54652" class="Pixso-frame-6361_54652">
                    <slot name="slot_6361_54653">
                        <Logo
                            id="6361_54653"
                            class="Pixso-instance-6361_54653"
                            IsDarkMode="True"
                        >
                            <template #slot_5572_73848>
                                <Logomark
                                    id="5572_73848"
                                    class="Pixso-instance-5572_73848"
                                />
                            </template>
                        </Logo>
                    </slot>
                </div>
                <slot name="slot_6361_54654">
                    <ButtonIcon
                        id="6361_54654"
                        class="Pixso-instance-6361_54654"
                        Hierarchy="No Fill"
                        Size="md"
                        Color="Gray"
                        State="Default"
                    >
                        <template #slot_5590_22158>
                            <List
                                id="5590_22158"
                                class="Pixso-instance-5590_22158"
                            />
                        </template>
                    </ButtonIcon>
                </slot>
            </div>
            <div
                id="6361_54655"
                class="Pixso-symbol-6361_54655 fill-gray80-32_4123"
                v-if="
                    Theme === 'Dark' &&
                    IsMobile === 'True' &&
                    Type === 'Default'
                "
            >
                <div id="6361_54656" class="Pixso-frame-6361_54656">
                    <slot name="slot_6361_54657">
                        <Logo
                            id="6361_54657"
                            class="Pixso-instance-6361_54657"
                            IsDarkMode="True"
                        />
                    </slot>
                </div>
                <slot name="slot_6361_54658">
                    <ButtonIcon
                        id="6361_54658"
                        class="Pixso-instance-6361_54658"
                        Hierarchy="No Fill"
                        Size="md"
                        Color="Gray"
                        State="Default"
                    >
                        <template #slot_5590_22158>
                            <List
                                id="5590_22158"
                                class="Pixso-instance-5590_22158"
                            />
                        </template>
                    </ButtonIcon>
                </slot>
            </div>
            <div
                id="6361_54659"
                class="stroke-wrapper-6361_54659"
                v-if="
                    Theme === 'White' &&
                    IsMobile === 'True' &&
                    Type === 'Default'
                "
            >
                <div class="Pixso-symbol-6361_54659 fill-gray0-white-67_3285">
                    <div id="6361_54660" class="Pixso-frame-6361_54660">
                        <slot name="slot_6361_54661">
                            <Logo
                                id="6361_54661"
                                class="Pixso-instance-6361_54661"
                                IsDarkMode="False"
                            />
                        </slot>
                    </div>
                    <slot name="slot_6361_54662">
                        <ButtonIcon
                            id="6361_54662"
                            class="Pixso-instance-6361_54662"
                            Hierarchy="No Fill"
                            Size="md"
                            Color="Gray"
                            State="Default"
                        >
                            <template #slot_5590_22158>
                                <List
                                    id="5590_22158"
                                    class="Pixso-instance-5590_22158"
                                />
                            </template>
                        </ButtonIcon>
                    </slot>
                </div>
                <div class="stroke-6361_54659 stroke-gray20-36_1844"></div>
            </div>
            <div
                id="6361_54663"
                class="Pixso-symbol-6361_54663 fill-gray5-32_4120"
                v-if="
                    Theme === 'Light Gray' &&
                    IsMobile === 'True' &&
                    Type === 'Default'
                "
            >
                <div id="6361_54664" class="Pixso-frame-6361_54664">
                    <slot name="slot_6361_54665">
                        <Logo
                            id="6361_54665"
                            class="Pixso-instance-6361_54665"
                            IsDarkMode="False"
                        />
                    </slot>
                </div>
                <slot name="slot_6361_54666">
                    <ButtonIcon
                        id="6361_54666"
                        class="Pixso-instance-6361_54666"
                        Hierarchy="No Fill"
                        Size="md"
                        Color="Gray"
                        State="Default"
                    >
                        <template #slot_5590_22158>
                            <List
                                id="5590_22158"
                                class="Pixso-instance-5590_22158"
                            />
                        </template>
                    </ButtonIcon>
                </slot>
            </div>
        </div>
    </div>
</template>
<script lang="ts" setup>
import Logo from "@/components/Logo.vue";
import InputText from "@/components/Inputtext.vue";
import InputTextBase from "@/components/Inputtextbase.vue";
import User from "@/components/User.vue";
import AppSidebarItem from "@/components/Appsidebaritem.vue";
import BadgeText from "@/components/Badgetext.vue";
import ListBullets from "@/components/Listbullets.vue";
import Users from "@/components/Users.vue";
import Cube from "@/components/Cube.vue";
import CreditCard from "@/components/Creditcard.vue";
import GearSix from "@/components/Gearsix.vue";
import ChatTeardropDots from "@/components/Chatteardropdots.vue";
import NavFeaturedCard from "@/components/Navfeaturedcard.vue";
import Button from "@/components/Button.vue";
import Avatar from "@/components/Avatar.vue";
import ButtonIcon from "@/components/Buttonicon.vue";
import SignOut from "@/components/Signout.vue";
import Logomark from "@/components/Logomark.vue";
import HouseSimple from "@/components/Housesimple.vue";
import ChartBar from "@/components/Chartbar.vue";
import CalendarBlank from "@/components/Calendarblank.vue";
import Lightning from "@/components/Lightning.vue";
import BellSimple from "@/components/Bellsimple.vue";
import List from "@/components/List.vue";
const props = defineProps({
    Theme: { type: String },
    IsMobile: { type: String },
    Type: { type: String }
});
</script>
<style>
.Pixso-symbol-5984_59825 {
}
.Pixso-symbol-5982_59216 {
    width: 100%;
    height: 100%;
    position: relative;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    align-items: flex-start;
    padding: 32px 16px 32px 16px;
}
.stroke-wrapper-5982_59216 {
    position: relative;
    width: 312px;
    height: 960px;
    display: flex;
}
.stroke-5982_59216 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 1px 0px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-frame-5982_59115 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
}
.frame-content-5982_59115 {
    display: flex;
    flex-direction: column;
    gap: 32px;
    align-items: flex-start;
    width: 100%;
    position: relative;
}
.Pixso-frame-5982_59116 {
    width: 280px;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
}
.frame-content-5982_59116 {
    display: flex;
    flex-direction: column;
    gap: 10px;
    align-items: flex-start;
    width: 100%;
    position: relative;
}
.Pixso-instance-5982_59117 {
    width: 109px;
    height: 32px;
}
.Pixso-instance-5982_59118 {
    width: 280px;
    height: 40px;
}
.Pixso-instance-5976_53794 {
    width: 320px;
    height: 40px;
}
.Pixso-instance-5976_52049 {
    width: 20px;
    height: 20px;
}
.Pixso-frame-5982_59119 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    gap: 8px;
    align-items: flex-start;
}
.Pixso-instance-5982_59120 {
    width: 280px;
    height: 48px;
}
.Pixso-paragraph-5979_34883 {
    position: relative;
    flex-shrink: 1;
    width: 100%;
    flex-grow: 1;
    flex-basis: 0;
    height: auto;
}
.Pixso-instance-5979_34885 {
    width: 36px;
    height: 28px;
}
.Pixso-paragraph-5588_11356 {
    text-align: center;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    width: auto;
    height: auto;
    flex-grow: 0;
}
.Pixso-instance-5982_59121 {
    width: 280px;
    height: 48px;
}
.Pixso-instance-5980_54116 {
    width: undefinedpx;
    height: undefinedpx;
}
.Pixso-instance-5982_59122 {
    width: 280px;
    height: 48px;
}
.Pixso-instance-5982_59123 {
    width: 280px;
    height: 48px;
}
.Pixso-instance-5982_59124 {
    width: 280px;
    height: 48px;
}
.Pixso-instance-5982_59125 {
    width: 280px;
    height: 48px;
}
.Pixso-instance-5982_59126 {
    width: 280px;
    height: 48px;
}
.Pixso-frame-5982_59127 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    gap: 24px;
    align-items: flex-start;
}
.Pixso-instance-6360_36928 {
    width: 280px;
    height: 168px;
}
.Pixso-instance-6360_36891 {
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
.Pixso-instance-6360_36892 {
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
.Pixso-frame-5982_59129 {
    width: 100%;
    height: 100%;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    align-items: flex-end;
}
.frame-content-5982_59129 {
    display: flex;
    flex-direction: row;
    gap: 16px;
    align-items: flex-end;
    padding: 24px 0px 0px 0px;
    width: 100%;
    position: relative;
}
.stroke-wrapper-5982_59129 {
    position: relative;
    width: 280px;
    height: auto;
    display: flex;
    flex-shrink: 0;
}
.stroke-5982_59129 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 1px 0px 0px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-frame-5982_59130 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: row;
    align-items: center;
    flex-grow: 1;
    flex-basis: 0;
}
.frame-content-5982_59130 {
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    width: 100%;
    position: relative;
}
.Pixso-instance-5982_59131 {
    width: 40px;
    height: 40px;
}
.Pixso-frame-5982_59132 {
    width: 100%;
    height: 46px;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    flex-grow: 1;
    flex-basis: 0;
}
.frame-content-5982_59132 {
    display: flex;
    flex-direction: column;
    gap: 2px;
    align-items: flex-start;
    width: 100%;
    height: 100%;
    position: relative;
}
.Pixso-paragraph-5982_59133 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-paragraph-5982_59134 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5982_59135 {
    width: 40px;
    height: 40px;
}
.Pixso-instance-5590_22158 {
    width: undefinedpx;
    height: undefinedpx;
}
.Pixso-symbol-6360_51957 {
    width: 312px;
    height: 960px;
    position: relative;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    align-items: flex-start;
    padding: 32px 16px 32px 16px;
}
.Pixso-frame-6360_51958 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
}
.frame-content-6360_51958 {
    display: flex;
    flex-direction: column;
    gap: 32px;
    align-items: flex-start;
    width: 100%;
    position: relative;
}
.Pixso-frame-6360_51959 {
    width: 280px;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
}
.frame-content-6360_51959 {
    display: flex;
    flex-direction: column;
    gap: 10px;
    align-items: flex-start;
    width: 100%;
    position: relative;
}
.Pixso-instance-6360_51960 {
    width: 109px;
    height: 32px;
}
.Pixso-instance-6360_51961 {
    width: 280px;
    height: 40px;
}
.Pixso-frame-6360_51962 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    gap: 8px;
    align-items: flex-start;
}
.Pixso-instance-6360_51963 {
    width: 280px;
    height: 48px;
}
.Pixso-paragraph-6360_52184 {
    position: relative;
    flex-shrink: 1;
    width: 100%;
    flex-grow: 1;
    flex-basis: 0;
    height: auto;
}
.Pixso-instance-6360_52185 {
    width: 36px;
    height: 28px;
}
.Pixso-instance-6360_51964 {
    width: 280px;
    height: 48px;
}
.Pixso-instance-6360_52183 {
    width: undefinedpx;
    height: undefinedpx;
}
.Pixso-instance-6360_51965 {
    width: 280px;
    height: 48px;
}
.Pixso-instance-6360_51966 {
    width: 280px;
    height: 48px;
}
.Pixso-instance-6360_51967 {
    width: 280px;
    height: 48px;
}
.Pixso-instance-6360_51968 {
    width: 280px;
    height: 48px;
}
.Pixso-instance-6360_51969 {
    width: 280px;
    height: 48px;
}
.Pixso-frame-6360_51970 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    gap: 24px;
    align-items: flex-start;
}
.Pixso-instance-6360_54190 {
    width: 280px;
    height: 168px;
}
.Pixso-instance-6360_54139 {
    width: 52px;
    height: 20px;
}
.Pixso-instance-6360_54140 {
    width: 46px;
    height: 20px;
}
.Pixso-frame-6360_51972 {
    width: 100%;
    height: 100%;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    align-items: flex-end;
}
.frame-content-6360_51972 {
    display: flex;
    flex-direction: row;
    gap: 16px;
    align-items: flex-end;
    padding: 24px 0px 0px 0px;
    width: 100%;
    position: relative;
}
.stroke-wrapper-6360_51972 {
    position: relative;
    width: 280px;
    height: auto;
    display: flex;
    flex-shrink: 0;
}
.stroke-6360_51972 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 1px 0px 0px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-frame-6360_51973 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: row;
    align-items: center;
    flex-grow: 1;
    flex-basis: 0;
}
.frame-content-6360_51973 {
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    width: 100%;
    position: relative;
}
.Pixso-instance-6360_51974 {
    width: 40px;
    height: 40px;
}
.Pixso-frame-6360_51975 {
    width: 100%;
    height: 46px;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    flex-grow: 1;
    flex-basis: 0;
}
.frame-content-6360_51975 {
    display: flex;
    flex-direction: column;
    gap: 2px;
    align-items: flex-start;
    width: 100%;
    height: 100%;
    position: relative;
}
.Pixso-paragraph-6360_51976 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-paragraph-6360_51977 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-6360_51978 {
    width: 40px;
    height: 40px;
}
.Pixso-instance-5591_22532 {
    width: undefinedpx;
    height: undefinedpx;
}
.Pixso-symbol-6360_52834 {
    width: 312px;
    height: 960px;
    position: relative;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    align-items: flex-start;
    padding: 32px 16px 32px 16px;
}
.Pixso-frame-6360_52835 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
}
.frame-content-6360_52835 {
    display: flex;
    flex-direction: column;
    gap: 32px;
    align-items: flex-start;
    width: 100%;
    position: relative;
}
.Pixso-frame-6361_54550 {
    width: 280px;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
}
.frame-content-6361_54550 {
    display: flex;
    flex-direction: column;
    gap: 10px;
    align-items: flex-start;
    width: 100%;
    position: relative;
}
.Pixso-instance-6361_54551 {
    width: 109px;
    height: 32px;
}
.Pixso-instance-6360_52838 {
    width: 280px;
    height: 40px;
}
.Pixso-frame-6360_52839 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    gap: 8px;
    align-items: flex-start;
}
.Pixso-instance-6360_52840 {
    width: 280px;
    height: 48px;
}
.Pixso-paragraph-6360_52671 {
    position: relative;
    flex-shrink: 1;
    width: 100%;
    flex-grow: 1;
    flex-basis: 0;
    height: auto;
}
.Pixso-instance-6360_52672 {
    width: 36px;
    height: 28px;
}
.Pixso-paragraph-5588_11527 {
    text-align: center;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    width: auto;
    height: auto;
    flex-grow: 0;
}
.Pixso-instance-6360_52841 {
    width: 280px;
    height: 48px;
}
.Pixso-instance-6360_52670 {
    width: undefinedpx;
    height: undefinedpx;
}
.Pixso-instance-6360_52842 {
    width: 280px;
    height: 48px;
}
.Pixso-instance-6360_52843 {
    width: 280px;
    height: 48px;
}
.Pixso-instance-6360_52844 {
    width: 280px;
    height: 48px;
}
.Pixso-instance-6360_52845 {
    width: 280px;
    height: 48px;
}
.Pixso-instance-6360_52846 {
    width: 280px;
    height: 48px;
}
.Pixso-frame-6360_52847 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    gap: 24px;
    align-items: flex-start;
}
.Pixso-instance-6360_52848 {
    width: 280px;
    height: 168px;
}
.Pixso-instance-6360_54327 {
    width: 52px;
    height: 20px;
}
.Pixso-instance-6360_54328 {
    width: 46px;
    height: 20px;
}
.Pixso-frame-6360_52849 {
    width: 100%;
    height: 100%;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    align-items: flex-end;
}
.frame-content-6360_52849 {
    display: flex;
    flex-direction: row;
    gap: 16px;
    align-items: flex-end;
    padding: 24px 0px 0px 0px;
    width: 100%;
    position: relative;
}
.stroke-wrapper-6360_52849 {
    position: relative;
    width: 280px;
    height: auto;
    display: flex;
    flex-shrink: 0;
}
.stroke-6360_52849 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 1px 0px 0px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-frame-6360_52850 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: row;
    align-items: center;
    flex-grow: 1;
    flex-basis: 0;
}
.frame-content-6360_52850 {
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    width: 100%;
    position: relative;
}
.Pixso-instance-6360_52851 {
    width: 40px;
    height: 40px;
}
.Pixso-frame-6360_52852 {
    width: 100%;
    height: 46px;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    flex-grow: 1;
    flex-basis: 0;
}
.frame-content-6360_52852 {
    display: flex;
    flex-direction: column;
    gap: 2px;
    align-items: flex-start;
    width: 100%;
    height: 100%;
    position: relative;
}
.Pixso-paragraph-6360_52853 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-paragraph-6360_52854 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-6360_52855 {
    width: 40px;
    height: 40px;
}
.Pixso-symbol-5978_31519 {
    width: 312px;
    height: 960px;
    position: relative;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    align-items: flex-start;
    padding: 32px 16px 32px 16px;
}
.Pixso-frame-5982_58829 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    gap: 32px;
    align-items: flex-start;
}
.Pixso-frame-5982_57987 {
    width: 280px;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
}
.frame-content-5982_57987 {
    display: flex;
    flex-direction: column;
    gap: 10px;
    align-items: flex-start;
    width: 100%;
    position: relative;
}
.Pixso-instance-5976_55198 {
    width: 109px;
    height: 32px;
}
.Pixso-instance-5572_73848 {
    width: 32px;
    height: 32px;
}
.Pixso-instance-5976_58202 {
    width: 280px;
    height: 40px;
}
.Pixso-frame-5982_55242 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    gap: 8px;
    align-items: flex-start;
}
.Pixso-instance-5980_54129 {
    width: 280px;
    height: 48px;
}
.Pixso-paragraph-5982_54581 {
    position: relative;
    flex-shrink: 1;
    width: 100%;
    flex-grow: 1;
    flex-basis: 0;
    height: auto;
}
.Pixso-instance-5982_54582 {
    width: 36px;
    height: 28px;
}
.Pixso-instance-5982_54782 {
    width: 280px;
    height: 48px;
}
.Pixso-instance-5982_54580 {
    width: undefinedpx;
    height: undefinedpx;
}
.Pixso-instance-5982_54844 {
    width: 280px;
    height: 48px;
}
.Pixso-instance-5982_54921 {
    width: 280px;
    height: 48px;
}
.Pixso-instance-5982_55013 {
    width: 280px;
    height: 48px;
}
.Pixso-instance-5982_55120 {
    width: 280px;
    height: 48px;
}
.Pixso-instance-5982_58638 {
    width: 280px;
    height: 48px;
}
.Pixso-frame-5982_58728 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    gap: 24px;
    align-items: flex-start;
}
.Pixso-instance-6360_37700 {
    width: 280px;
    height: 168px;
}
.Pixso-instance-6360_36912 {
    width: 52px;
    height: 20px;
}
.Pixso-instance-6360_36913 {
    width: 46px;
    height: 20px;
}
.Pixso-frame-5982_57071 {
    width: 100%;
    height: 100%;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    align-items: flex-end;
}
.frame-content-5982_57071 {
    display: flex;
    flex-direction: row;
    gap: 16px;
    align-items: flex-end;
    padding: 24px 0px 0px 0px;
    width: 100%;
    position: relative;
}
.stroke-wrapper-5982_57071 {
    position: relative;
    width: 280px;
    height: auto;
    display: flex;
    flex-shrink: 0;
}
.stroke-5982_57071 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 1px 0px 0px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-frame-5982_56616 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: row;
    align-items: center;
    flex-grow: 1;
    flex-basis: 0;
}
.frame-content-5982_56616 {
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    width: 100%;
    position: relative;
}
.Pixso-instance-5982_55911 {
    width: 40px;
    height: 40px;
}
.Pixso-frame-5982_56474 {
    width: 100%;
    height: 46px;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    flex-grow: 1;
    flex-basis: 0;
}
.frame-content-5982_56474 {
    display: flex;
    flex-direction: column;
    gap: 2px;
    align-items: flex-start;
    width: 100%;
    height: 100%;
    position: relative;
}
.Pixso-paragraph-5982_56193 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-paragraph-5982_56333 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-instance-5982_56899 {
    width: 40px;
    height: 40px;
}
.Pixso-instance-5591_22530 {
    width: undefinedpx;
    height: undefinedpx;
}
.Pixso-symbol-5648_26772 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 368px;
    align-items: flex-start;
    padding: 24px 16px 24px 16px;
}
.stroke-wrapper-5648_26772 {
    position: relative;
    width: auto;
    height: auto;
    display: flex;
}
.stroke-5648_26772 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 1px 0px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-frame-5648_26771 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    gap: 32px;
    align-items: center;
}
.Pixso-instance-5648_26648 {
    width: 32px;
    height: 32px;
}
.Pixso-frame-5648_26641 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    gap: 16px;
    align-items: flex-start;
}
.Pixso-instance-5648_26642 {
    width: 48px;
    height: 48px;
}
.Pixso-instance-5590_21884 {
    width: undefinedpx;
    height: undefinedpx;
}
.Pixso-instance-5648_26643 {
    width: 48px;
    height: 48px;
}
.Pixso-instance-5590_22160 {
    width: undefinedpx;
    height: undefinedpx;
}
.Pixso-instance-5648_26644 {
    width: 48px;
    height: 48px;
}
.Pixso-instance-5648_26645 {
    width: 48px;
    height: 48px;
}
.Pixso-instance-5648_26766 {
    width: 48px;
    height: 48px;
}
.Pixso-instance-5648_26646 {
    width: 48px;
    height: 48px;
}
.Pixso-frame-5648_26765 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    gap: 16px;
    align-items: flex-start;
}
.Pixso-instance-5648_26647 {
    width: 48px;
    height: 48px;
}
.Pixso-instance-5648_26649 {
    width: 48px;
    height: 48px;
}
.Pixso-symbol-6361_54407 {
    width: auto;
    height: auto;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 368px;
    align-items: flex-start;
    padding: 24px 16px 24px 16px;
}
.Pixso-frame-6361_54408 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    gap: 32px;
    align-items: center;
}
.Pixso-instance-6361_54409 {
    width: 32px;
    height: 32px;
}
.Pixso-frame-6361_54410 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    gap: 16px;
    align-items: flex-start;
}
.Pixso-instance-6361_54411 {
    width: 48px;
    height: 48px;
}
.Pixso-instance-6361_54412 {
    width: 48px;
    height: 48px;
}
.Pixso-instance-6361_54413 {
    width: 48px;
    height: 48px;
}
.Pixso-instance-6361_54414 {
    width: 48px;
    height: 48px;
}
.Pixso-instance-6361_54415 {
    width: 48px;
    height: 48px;
}
.Pixso-instance-6361_54416 {
    width: 48px;
    height: 48px;
}
.Pixso-frame-6361_54417 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    gap: 16px;
    align-items: flex-start;
}
.Pixso-instance-6361_54418 {
    width: 48px;
    height: 48px;
}
.Pixso-instance-6361_54419 {
    width: 48px;
    height: 48px;
}
.Pixso-symbol-5648_26862 {
    width: 80px;
    height: 960px;
    overflow: hidden;
    position: relative;
}
.Pixso-frame-5648_26863 {
    width: auto;
    height: auto;
    position: absolute;
    left: 16px;
    top: 24px;
    display: flex;
    flex-direction: column;
    gap: 32px;
    align-items: center;
}
.Pixso-instance-5648_26864 {
    width: 32px;
    height: 32px;
}
.Pixso-frame-5648_26865 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    gap: 16px;
    align-items: flex-start;
}
.Pixso-instance-5648_26866 {
    width: 48px;
    height: 48px;
}
.Pixso-instance-5648_26867 {
    width: 48px;
    height: 48px;
}
.Pixso-instance-5648_26868 {
    width: 48px;
    height: 48px;
}
.Pixso-instance-5648_26869 {
    width: 48px;
    height: 48px;
}
.Pixso-instance-5648_26870 {
    width: 48px;
    height: 48px;
}
.Pixso-instance-5648_26871 {
    width: 48px;
    height: 48px;
}
.Pixso-frame-5648_26886 {
    width: auto;
    height: auto;
    position: absolute;
    left: 16px;
    top: 824px;
    display: flex;
    flex-direction: column;
    gap: 16px;
    align-items: flex-start;
}
.Pixso-instance-5648_26887 {
    width: 48px;
    height: 48px;
}
.Pixso-instance-5648_26888 {
    width: 48px;
    height: 48px;
}
.Pixso-symbol-6361_54484 {
    width: 80px;
    height: 960px;
    overflow: hidden;
    position: relative;
}
.Pixso-frame-6361_54485 {
    width: auto;
    height: auto;
    position: absolute;
    left: 16px;
    top: 24px;
    display: flex;
    flex-direction: column;
    gap: 32px;
    align-items: center;
}
.Pixso-instance-6361_54486 {
    width: 32px;
    height: 32px;
}
.Pixso-frame-6361_54487 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    gap: 16px;
    align-items: flex-start;
}
.Pixso-instance-6361_54488 {
    width: 48px;
    height: 48px;
}
.Pixso-instance-6361_54489 {
    width: 48px;
    height: 48px;
}
.Pixso-instance-6361_54490 {
    width: 48px;
    height: 48px;
}
.Pixso-instance-6361_54491 {
    width: 48px;
    height: 48px;
}
.Pixso-instance-6361_54492 {
    width: 48px;
    height: 48px;
}
.Pixso-instance-6361_54493 {
    width: 48px;
    height: 48px;
}
.Pixso-frame-6361_54494 {
    width: auto;
    height: auto;
    position: absolute;
    left: 16px;
    top: 824px;
    display: flex;
    flex-direction: column;
    gap: 16px;
    align-items: flex-start;
}
.Pixso-instance-6361_54495 {
    width: 48px;
    height: 48px;
}
.Pixso-instance-6361_54496 {
    width: 48px;
    height: 48px;
}
.Pixso-symbol-6012_50232 {
    width: 375px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 10px;
    align-items: center;
    padding: 12px 16px 12px 16px;
}
.Pixso-frame-6012_50233 {
    width: 100%;
    height: 32px;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-6012_50234 {
    width: 109px;
    height: 32px;
}
.Pixso-instance-6012_50235 {
    width: 40px;
    height: 40px;
}
.Pixso-symbol-6361_54541 {
    width: 375px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 10px;
    align-items: center;
    padding: 12px 16px 12px 16px;
}
.Pixso-frame-6361_54542 {
    width: 100%;
    height: 32px;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-6361_54543 {
    width: 109px;
    height: 32px;
}
.Pixso-instance-6361_54544 {
    width: 40px;
    height: 40px;
}
.Pixso-symbol-6012_50236 {
    width: 100%;
    height: 100%;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 10px;
    align-items: center;
    padding: 12px 16px 12px 16px;
}
.stroke-wrapper-6012_50236 {
    position: relative;
    width: 375px;
    height: auto;
    display: flex;
}
.stroke-6012_50236 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 1px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-frame-6012_50237 {
    width: 100%;
    height: 32px;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-6012_50238 {
    width: 109px;
    height: 32px;
}
.Pixso-instance-6012_50239 {
    width: 40px;
    height: 40px;
}
.Pixso-symbol-6361_54522 {
    width: 375px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 10px;
    align-items: center;
    padding: 12px 16px 12px 16px;
}
.Pixso-frame-6361_54523 {
    width: 100%;
    height: 32px;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-6361_54524 {
    width: 109px;
    height: 32px;
}
.Pixso-instance-6361_54525 {
    width: 40px;
    height: 40px;
}
.Pixso-symbol-6361_54651 {
    width: 375px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 10px;
    align-items: center;
    padding: 12px 16px 12px 16px;
}
.Pixso-frame-6361_54652 {
    width: 100%;
    height: 32px;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-6361_54653 {
    width: 109px;
    height: 32px;
}
.Pixso-instance-6361_54654 {
    width: 40px;
    height: 40px;
}
.Pixso-symbol-6361_54655 {
    width: 375px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 10px;
    align-items: center;
    padding: 12px 16px 12px 16px;
}
.Pixso-frame-6361_54656 {
    width: 100%;
    height: 32px;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-6361_54657 {
    width: 109px;
    height: 32px;
}
.Pixso-instance-6361_54658 {
    width: 40px;
    height: 40px;
}
.Pixso-symbol-6361_54659 {
    width: 100%;
    height: 100%;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 10px;
    align-items: center;
    padding: 12px 16px 12px 16px;
}
.stroke-wrapper-6361_54659 {
    position: relative;
    width: 375px;
    height: auto;
    display: flex;
}
.stroke-6361_54659 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 1px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-frame-6361_54660 {
    width: 100%;
    height: 32px;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-6361_54661 {
    width: 109px;
    height: 32px;
}
.Pixso-instance-6361_54662 {
    width: 40px;
    height: 40px;
}
.Pixso-symbol-6361_54663 {
    width: 375px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 10px;
    align-items: center;
    padding: 12px 16px 12px 16px;
}
.Pixso-frame-6361_54664 {
    width: 100%;
    height: 32px;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-6361_54665 {
    width: 109px;
    height: 32px;
}
.Pixso-instance-6361_54666 {
    width: 40px;
    height: 40px;
}

.Pixso-instance-5982_59117 .Pixso-vector-5490_11743 {
    width: 69px;
    height: 17px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5982_59117 .Pixso-symbol-5569_17873 {
    width: 109px;
    height: 32px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
}
.Pixso-instance-5982_59117 .Pixso-instance-5572_73326 {
    width: 32px;
    height: 32px;
}
.Pixso-instance-5982_59118
    .Pixso-instance-5976_53794
    .Pixso-instance-5976_52049
    .Pixso-vector-5578_150579 {
    width: 70.4%;
    height: 70.4%;
    background-image: url(@/assets/images/Vector105.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 6.44%;
    right: 23.16%;
    top: 6.44%;
    bottom: 23.16%;
}
.Pixso-instance-5976_53794
    .Pixso-instance-5976_52049
    .Pixso-vector-5578_150579 {
    width: 70.4%;
    height: 70.4%;
    background-image: url(@/assets/images/Vector105.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 6.44%;
    right: 23.16%;
    top: 6.44%;
    bottom: 23.16%;
}
.Pixso-instance-5982_59118 .Pixso-instance-5976_53794 {
    width: 320px;
    height: 40px;
}
.Pixso-instance-5976_53794 .Pixso-instance-5976_53794 {
    width: 320px;
    height: 40px;
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
.Pixso-instance-5976_52049 .Pixso-vector-5578_150579 {
    width: 84.48%;
    height: 84.48%;
    position: absolute;
    left: 7.73%;
    right: 7.79%;
    top: 7.73%;
    bottom: 7.79%;
}
.Pixso-instance-5982_59118
    .Pixso-instance-5976_53794
    .Pixso-instance-5976_52049 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5976_53794 .Pixso-instance-5976_52049 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5976_52049 .Pixso-instance-5976_52049 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5982_59120 .Pixso-paragraph-5979_34883 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5982_59120 .Pixso-instance-5979_34885 {
    width: 36px;
    height: 28px;
}
.Pixso-instance-5982_59120 .Pixso-instance-5979_34908 {
    width: 24px;
    height: 24px;
}
.Pixso-instance-5982_59120 .Pixso-instance-5980_54108 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5982_59120 .Pixso-instance-5980_54116 {
    width: 24px;
    height: 24px;
}
.Pixso-instance-5982_59120 .Pixso-symbol-5980_54125 {
    width: 280px;
    height: 48px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
    padding: 10px 12px 10px 12px;
    min-height: 48px;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5982_59120 .Pixso-frame-5980_54290 {
    width: 100%;
    height: 24px;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5982_59120
    .Pixso-instance-5979_34885
    .Pixso-instance-5588_11353 {
    width: 16px;
    height: 16px;
}
.Pixso-instance-5982_59120 .Pixso-instance-5979_34885 .Pixso-frame-5588_11354 {
    width: 50px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 5px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5982_59120
    .Pixso-instance-5979_34885
    .Pixso-instance-5588_11355 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5982_59120
    .Pixso-instance-5979_34885
    .Pixso-paragraph-5588_11356 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5982_59120
    .Pixso-instance-5979_34885
    .Pixso-instance-5588_11357 {
    width: 16px;
    height: 16px;
}
.Pixso-instance-5979_34885 .Pixso-symbol-5588_11352 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 6px;
    justify-content: center;
    align-items: center;
    padding: 4px 10px 4px 10px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5979_34885 .stroke-wrapper-5588_11352 {
    width: 36px;
    height: 28px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5979_34885 .stroke-5588_11352 {
    inset: 0px;
    border-radius: 1234px 1234px 1234px 1234px;
    pointer-events: none;
    border-width: 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5979_34885 .Pixso-instance-5588_11353 {
    width: 16px;
    height: 16px;
}
.Pixso-instance-5979_34885 .Pixso-frame-5588_11354 {
    width: 9px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 5px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5979_34885 .Pixso-instance-5588_11355 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5979_34885 .Pixso-paragraph-5588_11356 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5979_34885 .Pixso-instance-5588_11357 {
    width: 16px;
    height: 16px;
}
.Pixso-instance-5979_34885 .Pixso-instance-5979_34885 {
    width: 36px;
    height: 28px;
}
.Pixso-instance-5982_59121 .Pixso-paragraph-5979_34883 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5982_59121 .Pixso-instance-5979_34885 {
    width: 36px;
    height: 28px;
}
.Pixso-instance-5982_59121 .Pixso-instance-5979_34908 {
    width: 24px;
    height: 24px;
}
.Pixso-instance-5982_59121 .Pixso-instance-5980_54108 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5982_59121 .Pixso-symbol-5980_54125 {
    width: 280px;
    height: 48px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
    padding: 10px 12px 10px 12px;
    min-height: 48px;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5982_59121 .Pixso-frame-5980_54290 {
    width: 100%;
    height: 24px;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5982_59121
    .Pixso-instance-5979_34885
    .Pixso-instance-5588_11353 {
    width: 16px;
    height: 16px;
}
.Pixso-instance-5982_59121 .Pixso-instance-5979_34885 .Pixso-frame-5588_11354 {
    width: 50px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 5px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5982_59121
    .Pixso-instance-5979_34885
    .Pixso-instance-5588_11355 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5982_59121
    .Pixso-instance-5979_34885
    .Pixso-paragraph-5588_11356 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5982_59121
    .Pixso-instance-5979_34885
    .Pixso-instance-5588_11357 {
    width: 16px;
    height: 16px;
}
.Pixso-instance-5980_54116 .Pixso-instance-5980_54116 {
    width: 24px;
    height: 24px;
}
.Pixso-instance-5982_59122 .Pixso-paragraph-5979_34883 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5982_59122 .Pixso-instance-5979_34885 {
    width: 36px;
    height: 28px;
}
.Pixso-instance-5982_59122 .Pixso-instance-5979_34908 {
    width: 24px;
    height: 24px;
}
.Pixso-instance-5982_59122 .Pixso-instance-5980_54108 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5982_59122
    .Pixso-instance-5980_54116
    .Pixso-symbol-5579_152493 {
    width: 24px;
    height: 24px;
    position: absolute;
    left: 0px;
    top: 0px;
    background-color: transparent;
}
.Pixso-instance-5982_59122 .Pixso-symbol-5980_54125 {
    width: 280px;
    height: 48px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
    padding: 10px 12px 10px 12px;
    min-height: 48px;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5982_59122 .Pixso-frame-5980_54290 {
    width: 100%;
    height: 24px;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5982_59122
    .Pixso-instance-5980_54116
    .Pixso-vector-5579_152494 {
    width: 99.21%;
    height: 64.1%;
    background-image: url(@/assets/images/Vector54.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 0.39%;
    right: 0.4%;
    top: 17.17%;
    bottom: 18.73%;
}
.Pixso-instance-5982_59122
    .Pixso-instance-5979_34885
    .Pixso-instance-5588_11353 {
    width: 16px;
    height: 16px;
}
.Pixso-instance-5982_59122 .Pixso-instance-5979_34885 .Pixso-frame-5588_11354 {
    width: 9px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 5px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5982_59122
    .Pixso-instance-5979_34885
    .Pixso-instance-5588_11355 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5982_59122
    .Pixso-instance-5979_34885
    .Pixso-paragraph-5588_11356 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5982_59122
    .Pixso-instance-5979_34885
    .Pixso-instance-5588_11357 {
    width: 16px;
    height: 16px;
}
.Pixso-instance-5980_54116 .Pixso-vector-5579_152494 {
    width: 99.21%;
    height: 64.1%;
    position: absolute;
    left: 0.39%;
    right: 0.4%;
    top: 17.17%;
    bottom: 18.73%;
}
.Pixso-instance-5982_59123 .Pixso-paragraph-5979_34883 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5982_59123 .Pixso-instance-5979_34885 {
    width: 36px;
    height: 28px;
}
.Pixso-instance-5982_59123 .Pixso-instance-5979_34908 {
    width: 24px;
    height: 24px;
}
.Pixso-instance-5982_59123 .Pixso-instance-5980_54108 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5982_59123
    .Pixso-instance-5980_54116
    .Pixso-symbol-5578_149025 {
    width: 24px;
    height: 24px;
    position: absolute;
    left: 0px;
    top: 0px;
    background-color: transparent;
}
.Pixso-instance-5982_59123 .Pixso-symbol-5980_54125 {
    width: 280px;
    height: 48px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
    padding: 10px 12px 10px 12px;
    min-height: 48px;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5982_59123 .Pixso-frame-5980_54290 {
    width: 100%;
    height: 24px;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5982_59123
    .Pixso-instance-5980_54116
    .Pixso-vector-5578_149026 {
    width: 84.38%;
    height: 90.62%;
    background-image: url(@/assets/images/Vector15.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 4.69%;
    bottom: 4.69%;
}
.Pixso-instance-5982_59123
    .Pixso-instance-5979_34885
    .Pixso-instance-5588_11353 {
    width: 16px;
    height: 16px;
}
.Pixso-instance-5982_59123 .Pixso-instance-5979_34885 .Pixso-frame-5588_11354 {
    width: 50px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 5px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5982_59123
    .Pixso-instance-5979_34885
    .Pixso-instance-5588_11355 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5982_59123
    .Pixso-instance-5979_34885
    .Pixso-paragraph-5588_11356 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5982_59123
    .Pixso-instance-5979_34885
    .Pixso-instance-5588_11357 {
    width: 16px;
    height: 16px;
}
.Pixso-instance-5980_54116 .Pixso-vector-5578_149026 {
    width: 84.38%;
    height: 90.62%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 4.69%;
    bottom: 4.69%;
}
.Pixso-instance-5982_59124 .Pixso-paragraph-5979_34883 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5982_59124 .Pixso-instance-5979_34885 {
    width: 36px;
    height: 28px;
}
.Pixso-instance-5982_59124 .Pixso-instance-5979_34908 {
    width: 24px;
    height: 24px;
}
.Pixso-instance-5982_59124 .Pixso-instance-5980_54108 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5982_59124
    .Pixso-instance-5980_54116
    .Pixso-symbol-5579_152031 {
    width: 24px;
    height: 24px;
    position: absolute;
    left: 0px;
    top: 0px;
    background-color: transparent;
}
.Pixso-instance-5982_59124 .Pixso-symbol-5980_54125 {
    width: 280px;
    height: 48px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
    padding: 10px 12px 10px 12px;
    min-height: 48px;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5982_59124 .Pixso-frame-5980_54290 {
    width: 100%;
    height: 24px;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5982_59124
    .Pixso-instance-5980_54116
    .Pixso-vector-5579_152032 {
    width: 90.62%;
    height: 65.62%;
    background-image: url(@/assets/images/Vector2031.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 4.69%;
    right: 4.69%;
    top: 17.19%;
    bottom: 17.19%;
}
.Pixso-instance-5982_59124
    .Pixso-instance-5979_34885
    .Pixso-instance-5588_11353 {
    width: 16px;
    height: 16px;
}
.Pixso-instance-5982_59124 .Pixso-instance-5979_34885 .Pixso-frame-5588_11354 {
    width: 50px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 5px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5982_59124
    .Pixso-instance-5979_34885
    .Pixso-instance-5588_11355 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5982_59124
    .Pixso-instance-5979_34885
    .Pixso-paragraph-5588_11356 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5982_59124
    .Pixso-instance-5979_34885
    .Pixso-instance-5588_11357 {
    width: 16px;
    height: 16px;
}
.Pixso-instance-5980_54116 .Pixso-vector-5579_152032 {
    width: 90.62%;
    height: 65.62%;
    position: absolute;
    left: 4.69%;
    right: 4.69%;
    top: 17.19%;
    bottom: 17.19%;
}
.Pixso-instance-5982_59125 .Pixso-paragraph-5979_34883 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5982_59125 .Pixso-instance-5979_34885 {
    width: 36px;
    height: 28px;
}
.Pixso-instance-5982_59125 .Pixso-instance-5979_34908 {
    width: 24px;
    height: 24px;
}
.Pixso-instance-5982_59125 .Pixso-instance-5980_54108 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5982_59125
    .Pixso-instance-5980_54116
    .Pixso-symbol-5578_150332 {
    width: 24px;
    height: 24px;
    position: absolute;
    left: 0px;
    top: 0px;
    background-color: transparent;
}
.Pixso-instance-5982_59125 .Pixso-symbol-5980_54125 {
    width: 280px;
    height: 48px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
    padding: 10px 12px 10px 12px;
    min-height: 48px;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5982_59125 .Pixso-frame-5980_54290 {
    width: 100%;
    height: 24px;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5982_59125
    .Pixso-instance-5980_54116
    .Pixso-vector-5578_150333 {
    width: 90.61%;
    height: 84.38%;
    background-image: url(@/assets/images/Vector87.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 4.7%;
    right: 4.69%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5982_59125
    .Pixso-instance-5979_34885
    .Pixso-instance-5588_11353 {
    width: 16px;
    height: 16px;
}
.Pixso-instance-5982_59125 .Pixso-instance-5979_34885 .Pixso-frame-5588_11354 {
    width: 50px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 5px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5982_59125
    .Pixso-instance-5979_34885
    .Pixso-instance-5588_11355 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5982_59125
    .Pixso-instance-5979_34885
    .Pixso-paragraph-5588_11356 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5982_59125
    .Pixso-instance-5979_34885
    .Pixso-instance-5588_11357 {
    width: 16px;
    height: 16px;
}
.Pixso-instance-5980_54116 .Pixso-vector-5578_150333 {
    width: 90.61%;
    height: 84.38%;
    position: absolute;
    left: 4.7%;
    right: 4.69%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5982_59126 .Pixso-paragraph-5979_34883 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5982_59126 .Pixso-instance-5979_34885 {
    width: 36px;
    height: 28px;
}
.Pixso-instance-5982_59126 .Pixso-instance-5979_34908 {
    width: 24px;
    height: 24px;
}
.Pixso-instance-5982_59126 .Pixso-instance-5980_54108 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5982_59126
    .Pixso-instance-5980_54116
    .Pixso-symbol-5577_146643 {
    width: 24px;
    height: 24px;
    position: absolute;
    left: 0px;
    top: 0px;
    background-color: transparent;
}
.Pixso-instance-5982_59126 .Pixso-symbol-5980_54125 {
    width: 280px;
    height: 48px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
    padding: 10px 12px 10px 12px;
    min-height: 48px;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5982_59126 .Pixso-frame-5980_54290 {
    width: 100%;
    height: 24px;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5982_59126
    .Pixso-instance-5980_54116
    .Pixso-vector-5577_146644 {
    width: 81.25%;
    height: 81.25%;
    background-image: url(@/assets/images/Vector327.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 10.94%;
    right: 7.81%;
    top: 7.81%;
    bottom: 10.94%;
}
.Pixso-instance-5982_59126
    .Pixso-instance-5979_34885
    .Pixso-instance-5588_11353 {
    width: 16px;
    height: 16px;
}
.Pixso-instance-5982_59126 .Pixso-instance-5979_34885 .Pixso-frame-5588_11354 {
    width: 50px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 5px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5982_59126
    .Pixso-instance-5979_34885
    .Pixso-instance-5588_11355 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5982_59126
    .Pixso-instance-5979_34885
    .Pixso-paragraph-5588_11356 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5982_59126
    .Pixso-instance-5979_34885
    .Pixso-instance-5588_11357 {
    width: 16px;
    height: 16px;
}
.Pixso-instance-5980_54116 .Pixso-vector-5577_146644 {
    width: 81.25%;
    height: 81.25%;
    position: absolute;
    left: 10.94%;
    right: 7.81%;
    top: 7.81%;
    bottom: 10.94%;
}
.Pixso-instance-6360_36928 .Pixso-instance-6358_22757 {
    width: 40px;
    height: 40px;
}
.Pixso-instance-6360_36928 .Pixso-symbol-6360_36880 {
    width: 280px;
    height: 168px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    gap: 16px;
    align-items: flex-start;
    padding: 16px 16px 16px 16px;
    border-radius: 24px 24px 24px 24px;
}
.Pixso-instance-6360_36928 .Pixso-instance-6360_36888 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-6360_36928 .Pixso-instance-6360_36891 {
    width: 52px;
    height: 20px;
}
.Pixso-instance-6360_36928 .Pixso-instance-6360_36892 {
    width: 46px;
    height: 20px;
}
.Pixso-instance-6360_36928 .Pixso-frame-6360_36904 {
    width: 100%;
    height: 40px;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: row;
    gap: 10px;
    align-items: flex-start;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-6360_36928
    .Pixso-instance-6360_36891
    .Pixso-instance-5603_17110 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-6360_36928
    .Pixso-instance-6360_36891
    .Pixso-paragraph-5603_17111 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-6360_36928
    .Pixso-instance-6360_36891
    .Pixso-instance-5603_17112 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-6360_36928
    .Pixso-instance-6360_36892
    .Pixso-instance-5603_17350 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-6360_36928
    .Pixso-instance-6360_36892
    .Pixso-paragraph-5603_17351 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-6360_36928
    .Pixso-instance-6360_36892
    .Pixso-instance-5603_17352 {
    width: 20px;
    height: 20px;
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
.Pixso-instance-6360_36891 .Pixso-instance-6360_36891 {
    width: 52px;
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
.Pixso-instance-6360_36892 .Pixso-instance-6360_36892 {
    width: 46px;
    height: 20px;
}
.Pixso-instance-5982_59131 .Pixso-symbol-5468_1033 {
    width: 40px;
    height: 40px;
    position: relative;
    flex-shrink: 0;
    border-radius: 76.875px 76.875px 76.875px 76.875px;
}
.Pixso-instance-5982_59135 .Pixso-symbol-5590_22157 {
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
.Pixso-instance-5982_59135
    .Pixso-instance-5590_22158
    .Pixso-symbol-5578_150697 {
    width: 24px;
    height: 24px;
    position: absolute;
    left: 0px;
    top: 0px;
    background-color: transparent;
}
.Pixso-instance-5982_59135
    .Pixso-instance-5590_22158
    .Pixso-vector-5578_150698 {
    width: 78.13%;
    height: 78.12%;
    background-image: url(@/assets/images/Vector111.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 14.06%;
    right: 7.81%;
    top: 10.94%;
    bottom: 10.94%;
}
.Pixso-instance-5590_22158 .Pixso-vector-5578_150698 {
    width: 78.13%;
    height: 78.12%;
    position: absolute;
    left: 14.06%;
    right: 7.81%;
    top: 10.94%;
    bottom: 10.94%;
}
.Pixso-instance-5590_22158 .Pixso-instance-5590_22158 {
    width: 24px;
    height: 24px;
}
.Pixso-instance-6360_51960 .Pixso-vector-5490_11743 {
    width: 69px;
    height: 17px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-6360_51960 .Pixso-symbol-5569_17873 {
    width: 109px;
    height: 32px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
}
.Pixso-instance-6360_51960 .Pixso-instance-5572_73326 {
    width: 32px;
    height: 32px;
}
.Pixso-instance-6360_51961 .Pixso-instance-5976_53794 {
    width: 320px;
    height: 40px;
}
.Pixso-instance-6360_51961
    .Pixso-instance-5976_53794
    .Pixso-instance-5976_52049 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-6360_51961
    .Pixso-instance-5976_53794
    .Pixso-instance-5976_52049
    .Pixso-vector-5578_150579 {
    width: 70.4%;
    height: 70.4%;
    background-image: url(@/assets/images/Vector105.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 6.44%;
    right: 23.16%;
    top: 6.44%;
    bottom: 23.16%;
}
.Pixso-instance-6360_51963 .Pixso-symbol-6360_52180 {
    width: 280px;
    height: 48px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
    padding: 10px 12px 10px 12px;
    min-height: 48px;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-6360_51963 .Pixso-frame-6360_52181 {
    width: 100%;
    height: 24px;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-6360_51963 .Pixso-instance-6360_52182 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-6360_51963 .Pixso-instance-6360_52183 {
    width: 24px;
    height: 24px;
}
.Pixso-instance-6360_51963 .Pixso-paragraph-6360_52184 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-6360_51963 .Pixso-instance-6360_52185 {
    width: 36px;
    height: 28px;
}
.Pixso-instance-6360_51963 .Pixso-instance-6360_52186 {
    width: 24px;
    height: 24px;
}
.Pixso-instance-6360_51963
    .Pixso-instance-6360_52185
    .Pixso-instance-5588_11353 {
    width: 16px;
    height: 16px;
}
.Pixso-instance-6360_51963 .Pixso-instance-6360_52185 .Pixso-frame-5588_11354 {
    width: 50px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 5px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-6360_51963
    .Pixso-instance-6360_52185
    .Pixso-instance-5588_11355 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-6360_51963
    .Pixso-instance-6360_52185
    .Pixso-paragraph-5588_11356 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-6360_51963
    .Pixso-instance-6360_52185
    .Pixso-instance-5588_11357 {
    width: 16px;
    height: 16px;
}
.Pixso-instance-6360_52185 .Pixso-symbol-5588_11352 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 6px;
    justify-content: center;
    align-items: center;
    padding: 4px 10px 4px 10px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-6360_52185 .stroke-wrapper-5588_11352 {
    width: 36px;
    height: 28px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-6360_52185 .stroke-5588_11352 {
    inset: 0px;
    border-radius: 1234px 1234px 1234px 1234px;
    pointer-events: none;
    border-width: 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-6360_52185 .Pixso-instance-5588_11353 {
    width: 16px;
    height: 16px;
}
.Pixso-instance-6360_52185 .Pixso-frame-5588_11354 {
    width: 9px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 5px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-6360_52185 .Pixso-instance-5588_11355 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-6360_52185 .Pixso-paragraph-5588_11356 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-6360_52185 .Pixso-instance-5588_11357 {
    width: 16px;
    height: 16px;
}
.Pixso-instance-6360_52185 .Pixso-instance-6360_52185 {
    width: 36px;
    height: 28px;
}
.Pixso-instance-6360_51964 .Pixso-symbol-6360_52180 {
    width: 280px;
    height: 48px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
    padding: 10px 12px 10px 12px;
    min-height: 48px;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-6360_51964 .Pixso-frame-6360_52181 {
    width: 100%;
    height: 24px;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-6360_51964 .Pixso-instance-6360_52182 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-6360_51964 .Pixso-paragraph-6360_52184 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-6360_51964 .Pixso-instance-6360_52185 {
    width: 36px;
    height: 28px;
}
.Pixso-instance-6360_51964 .Pixso-instance-6360_52186 {
    width: 24px;
    height: 24px;
}
.Pixso-instance-6360_51964
    .Pixso-instance-6360_52185
    .Pixso-instance-5588_11353 {
    width: 16px;
    height: 16px;
}
.Pixso-instance-6360_51964 .Pixso-instance-6360_52185 .Pixso-frame-5588_11354 {
    width: 50px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 5px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-6360_51964
    .Pixso-instance-6360_52185
    .Pixso-instance-5588_11355 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-6360_51964
    .Pixso-instance-6360_52185
    .Pixso-paragraph-5588_11356 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-6360_51964
    .Pixso-instance-6360_52185
    .Pixso-instance-5588_11357 {
    width: 16px;
    height: 16px;
}
.Pixso-instance-6360_52183 .Pixso-instance-6360_52183 {
    width: 24px;
    height: 24px;
}
.Pixso-instance-6360_51965 .Pixso-symbol-6360_52180 {
    width: 280px;
    height: 48px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
    padding: 10px 12px 10px 12px;
    min-height: 48px;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-6360_51965 .Pixso-frame-6360_52181 {
    width: 100%;
    height: 24px;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-6360_51965 .Pixso-instance-6360_52182 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-6360_51965
    .Pixso-instance-6360_52183
    .Pixso-symbol-5579_152493 {
    width: 24px;
    height: 24px;
    position: absolute;
    left: 0px;
    top: 0px;
    background-color: transparent;
}
.Pixso-instance-6360_51965 .Pixso-paragraph-6360_52184 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-6360_51965 .Pixso-instance-6360_52185 {
    width: 36px;
    height: 28px;
}
.Pixso-instance-6360_51965 .Pixso-instance-6360_52186 {
    width: 24px;
    height: 24px;
}
.Pixso-instance-6360_51965
    .Pixso-instance-6360_52183
    .Pixso-vector-5579_152494 {
    width: 99.21%;
    height: 64.1%;
    background-image: url(@/assets/images/Vector54.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 0.39%;
    right: 0.4%;
    top: 17.17%;
    bottom: 18.73%;
}
.Pixso-instance-6360_51965
    .Pixso-instance-6360_52185
    .Pixso-instance-5588_11353 {
    width: 16px;
    height: 16px;
}
.Pixso-instance-6360_51965 .Pixso-instance-6360_52185 .Pixso-frame-5588_11354 {
    width: 9px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 5px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-6360_51965
    .Pixso-instance-6360_52185
    .Pixso-instance-5588_11355 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-6360_51965
    .Pixso-instance-6360_52185
    .Pixso-paragraph-5588_11356 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-6360_51965
    .Pixso-instance-6360_52185
    .Pixso-instance-5588_11357 {
    width: 16px;
    height: 16px;
}
.Pixso-instance-6360_52183 .Pixso-vector-5579_152494 {
    width: 99.21%;
    height: 64.1%;
    position: absolute;
    left: 0.39%;
    right: 0.4%;
    top: 17.17%;
    bottom: 18.73%;
}
.Pixso-instance-6360_51966 .Pixso-symbol-6360_52180 {
    width: 280px;
    height: 48px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
    padding: 10px 12px 10px 12px;
    min-height: 48px;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-6360_51966 .Pixso-frame-6360_52181 {
    width: 100%;
    height: 24px;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-6360_51966 .Pixso-instance-6360_52182 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-6360_51966
    .Pixso-instance-6360_52183
    .Pixso-symbol-5578_149025 {
    width: 24px;
    height: 24px;
    position: absolute;
    left: 0px;
    top: 0px;
    background-color: transparent;
}
.Pixso-instance-6360_51966 .Pixso-paragraph-6360_52184 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-6360_51966 .Pixso-instance-6360_52185 {
    width: 36px;
    height: 28px;
}
.Pixso-instance-6360_51966 .Pixso-instance-6360_52186 {
    width: 24px;
    height: 24px;
}
.Pixso-instance-6360_51966
    .Pixso-instance-6360_52183
    .Pixso-vector-5578_149026 {
    width: 84.38%;
    height: 90.62%;
    background-image: url(@/assets/images/Vector15.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 4.69%;
    bottom: 4.69%;
}
.Pixso-instance-6360_51966
    .Pixso-instance-6360_52185
    .Pixso-instance-5588_11353 {
    width: 16px;
    height: 16px;
}
.Pixso-instance-6360_51966 .Pixso-instance-6360_52185 .Pixso-frame-5588_11354 {
    width: 50px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 5px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-6360_51966
    .Pixso-instance-6360_52185
    .Pixso-instance-5588_11355 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-6360_51966
    .Pixso-instance-6360_52185
    .Pixso-paragraph-5588_11356 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-6360_51966
    .Pixso-instance-6360_52185
    .Pixso-instance-5588_11357 {
    width: 16px;
    height: 16px;
}
.Pixso-instance-6360_52183 .Pixso-vector-5578_149026 {
    width: 84.38%;
    height: 90.62%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 4.69%;
    bottom: 4.69%;
}
.Pixso-instance-6360_51967 .Pixso-symbol-6360_52180 {
    width: 280px;
    height: 48px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
    padding: 10px 12px 10px 12px;
    min-height: 48px;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-6360_51967 .Pixso-frame-6360_52181 {
    width: 100%;
    height: 24px;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-6360_51967 .Pixso-instance-6360_52182 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-6360_51967
    .Pixso-instance-6360_52183
    .Pixso-symbol-5579_152031 {
    width: 24px;
    height: 24px;
    position: absolute;
    left: 0px;
    top: 0px;
    background-color: transparent;
}
.Pixso-instance-6360_51967 .Pixso-paragraph-6360_52184 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-6360_51967 .Pixso-instance-6360_52185 {
    width: 36px;
    height: 28px;
}
.Pixso-instance-6360_51967 .Pixso-instance-6360_52186 {
    width: 24px;
    height: 24px;
}
.Pixso-instance-6360_51967
    .Pixso-instance-6360_52183
    .Pixso-vector-5579_152032 {
    width: 90.62%;
    height: 65.62%;
    background-image: url(@/assets/images/Vector2031.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 4.69%;
    right: 4.69%;
    top: 17.19%;
    bottom: 17.19%;
}
.Pixso-instance-6360_51967
    .Pixso-instance-6360_52185
    .Pixso-instance-5588_11353 {
    width: 16px;
    height: 16px;
}
.Pixso-instance-6360_51967 .Pixso-instance-6360_52185 .Pixso-frame-5588_11354 {
    width: 50px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 5px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-6360_51967
    .Pixso-instance-6360_52185
    .Pixso-instance-5588_11355 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-6360_51967
    .Pixso-instance-6360_52185
    .Pixso-paragraph-5588_11356 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-6360_51967
    .Pixso-instance-6360_52185
    .Pixso-instance-5588_11357 {
    width: 16px;
    height: 16px;
}
.Pixso-instance-6360_52183 .Pixso-vector-5579_152032 {
    width: 90.62%;
    height: 65.62%;
    position: absolute;
    left: 4.69%;
    right: 4.69%;
    top: 17.19%;
    bottom: 17.19%;
}
.Pixso-instance-6360_51968 .Pixso-symbol-6360_52180 {
    width: 280px;
    height: 48px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
    padding: 10px 12px 10px 12px;
    min-height: 48px;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-6360_51968 .Pixso-frame-6360_52181 {
    width: 100%;
    height: 24px;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-6360_51968 .Pixso-instance-6360_52182 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-6360_51968
    .Pixso-instance-6360_52183
    .Pixso-symbol-5578_150332 {
    width: 24px;
    height: 24px;
    position: absolute;
    left: 0px;
    top: 0px;
    background-color: transparent;
}
.Pixso-instance-6360_51968 .Pixso-paragraph-6360_52184 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-6360_51968 .Pixso-instance-6360_52185 {
    width: 36px;
    height: 28px;
}
.Pixso-instance-6360_51968 .Pixso-instance-6360_52186 {
    width: 24px;
    height: 24px;
}
.Pixso-instance-6360_51968
    .Pixso-instance-6360_52183
    .Pixso-vector-5578_150333 {
    width: 90.61%;
    height: 84.38%;
    background-image: url(@/assets/images/Vector87.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 4.7%;
    right: 4.69%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-6360_51968
    .Pixso-instance-6360_52185
    .Pixso-instance-5588_11353 {
    width: 16px;
    height: 16px;
}
.Pixso-instance-6360_51968 .Pixso-instance-6360_52185 .Pixso-frame-5588_11354 {
    width: 50px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 5px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-6360_51968
    .Pixso-instance-6360_52185
    .Pixso-instance-5588_11355 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-6360_51968
    .Pixso-instance-6360_52185
    .Pixso-paragraph-5588_11356 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-6360_51968
    .Pixso-instance-6360_52185
    .Pixso-instance-5588_11357 {
    width: 16px;
    height: 16px;
}
.Pixso-instance-6360_52183 .Pixso-vector-5578_150333 {
    width: 90.61%;
    height: 84.38%;
    position: absolute;
    left: 4.7%;
    right: 4.69%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-6360_51969 .Pixso-symbol-6360_52180 {
    width: 280px;
    height: 48px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
    padding: 10px 12px 10px 12px;
    min-height: 48px;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-6360_51969 .Pixso-frame-6360_52181 {
    width: 100%;
    height: 24px;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-6360_51969 .Pixso-instance-6360_52182 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-6360_51969
    .Pixso-instance-6360_52183
    .Pixso-symbol-5577_146643 {
    width: 24px;
    height: 24px;
    position: absolute;
    left: 0px;
    top: 0px;
    background-color: transparent;
}
.Pixso-instance-6360_51969 .Pixso-paragraph-6360_52184 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-6360_51969 .Pixso-instance-6360_52185 {
    width: 36px;
    height: 28px;
}
.Pixso-instance-6360_51969 .Pixso-instance-6360_52186 {
    width: 24px;
    height: 24px;
}
.Pixso-instance-6360_51969
    .Pixso-instance-6360_52183
    .Pixso-vector-5577_146644 {
    width: 81.25%;
    height: 81.25%;
    background-image: url(@/assets/images/Vector327.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 10.94%;
    right: 7.81%;
    top: 7.81%;
    bottom: 10.94%;
}
.Pixso-instance-6360_51969
    .Pixso-instance-6360_52185
    .Pixso-instance-5588_11353 {
    width: 16px;
    height: 16px;
}
.Pixso-instance-6360_51969 .Pixso-instance-6360_52185 .Pixso-frame-5588_11354 {
    width: 50px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 5px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-6360_51969
    .Pixso-instance-6360_52185
    .Pixso-instance-5588_11355 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-6360_51969
    .Pixso-instance-6360_52185
    .Pixso-paragraph-5588_11356 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-6360_51969
    .Pixso-instance-6360_52185
    .Pixso-instance-5588_11357 {
    width: 16px;
    height: 16px;
}
.Pixso-instance-6360_52183 .Pixso-vector-5577_146644 {
    width: 81.25%;
    height: 81.25%;
    position: absolute;
    left: 10.94%;
    right: 7.81%;
    top: 7.81%;
    bottom: 10.94%;
}
.Pixso-instance-6360_54190 .Pixso-symbol-6360_54132 {
    width: 280px;
    height: 168px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    gap: 16px;
    align-items: flex-start;
    padding: 16px 16px 16px 16px;
    border-radius: 24px 24px 24px 24px;
}
.Pixso-instance-6360_54190 .Pixso-frame-6360_54134 {
    width: 100%;
    height: 40px;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: row;
    gap: 10px;
    align-items: flex-start;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-6360_54190 .Pixso-instance-6360_54135 {
    width: 40px;
    height: 40px;
}
.Pixso-instance-6360_54190 .Pixso-instance-6360_54136 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-6360_54190 .Pixso-instance-6360_54139 {
    width: 52px;
    height: 20px;
}
.Pixso-instance-6360_54190 .Pixso-instance-6360_54140 {
    width: 46px;
    height: 20px;
}
.Pixso-instance-6360_54190
    .Pixso-instance-6360_54139
    .Pixso-instance-5603_17110 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-6360_54190
    .Pixso-instance-6360_54139
    .Pixso-paragraph-5603_17111 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-6360_54190
    .Pixso-instance-6360_54139
    .Pixso-instance-5603_17112 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-6360_54190
    .Pixso-instance-6360_54140
    .Pixso-instance-5603_17350 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-6360_54190
    .Pixso-instance-6360_54140
    .Pixso-paragraph-5603_17351 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-6360_54190
    .Pixso-instance-6360_54140
    .Pixso-instance-5603_17352 {
    width: 20px;
    height: 20px;
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
.Pixso-instance-6360_54139 .Pixso-instance-6360_54139 {
    width: 52px;
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
.Pixso-instance-6360_54140 .Pixso-instance-6360_54140 {
    width: 46px;
    height: 20px;
}
.Pixso-instance-6360_51974 .Pixso-symbol-5468_1033 {
    width: 40px;
    height: 40px;
    position: relative;
    flex-shrink: 0;
    border-radius: 76.875px 76.875px 76.875px 76.875px;
}
.Pixso-instance-6360_51978 .Pixso-symbol-5591_22531 {
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
.Pixso-instance-6360_51978
    .Pixso-instance-5591_22532
    .Pixso-symbol-5578_150697 {
    width: 24px;
    height: 24px;
    position: absolute;
    left: 0px;
    top: 0px;
    background-color: transparent;
}
.Pixso-instance-6360_51978
    .Pixso-instance-5591_22532
    .Pixso-vector-5578_150698 {
    width: 78.13%;
    height: 78.12%;
    background-image: url(@/assets/images/Vector111.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 14.06%;
    right: 7.81%;
    top: 10.94%;
    bottom: 10.94%;
}
.Pixso-instance-5591_22532 .Pixso-vector-5578_150698 {
    width: 78.13%;
    height: 78.12%;
    position: absolute;
    left: 14.06%;
    right: 7.81%;
    top: 10.94%;
    bottom: 10.94%;
}
.Pixso-instance-5591_22532 .Pixso-instance-5591_22532 {
    width: 24px;
    height: 24px;
}
.Pixso-instance-6361_54551 .Pixso-instance-5572_73848 {
    width: 32px;
    height: 32px;
}
.Pixso-instance-6361_54551 .Pixso-vector-5572_73849 {
    width: 69px;
    height: 17px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-6361_54551 .Pixso-symbol-5572_73852 {
    width: 109px;
    height: 32px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
}
.Pixso-instance-6360_52838 .Pixso-instance-5976_53794 {
    width: 320px;
    height: 40px;
}
.Pixso-instance-6360_52838
    .Pixso-instance-5976_53794
    .Pixso-instance-5976_52049 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-6360_52838
    .Pixso-instance-5976_53794
    .Pixso-instance-5976_52049
    .Pixso-vector-5578_150579 {
    width: 70.4%;
    height: 70.4%;
    background-image: url(@/assets/images/Vector105.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 6.44%;
    right: 23.16%;
    top: 6.44%;
    bottom: 23.16%;
}
.Pixso-instance-6360_52840 .Pixso-symbol-6360_52667 {
    width: 280px;
    height: 48px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
    padding: 10px 12px 10px 12px;
    min-height: 48px;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-6360_52840 .Pixso-frame-6360_52668 {
    width: 100%;
    height: 24px;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-6360_52840 .Pixso-instance-6360_52669 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-6360_52840 .Pixso-instance-6360_52670 {
    width: 24px;
    height: 24px;
}
.Pixso-instance-6360_52840 .Pixso-paragraph-6360_52671 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-6360_52840 .Pixso-instance-6360_52672 {
    width: 36px;
    height: 28px;
}
.Pixso-instance-6360_52840 .Pixso-instance-6360_52673 {
    width: 24px;
    height: 24px;
}
.Pixso-instance-6360_52840
    .Pixso-instance-6360_52672
    .Pixso-instance-5588_11524 {
    width: 16px;
    height: 16px;
}
.Pixso-instance-6360_52840 .Pixso-instance-6360_52672 .Pixso-frame-5588_11525 {
    width: 50px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 5px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-6360_52840
    .Pixso-instance-6360_52672
    .Pixso-instance-5588_11526 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-6360_52840
    .Pixso-instance-6360_52672
    .Pixso-paragraph-5588_11527 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-6360_52840
    .Pixso-instance-6360_52672
    .Pixso-instance-5588_11528 {
    width: 16px;
    height: 16px;
}
.Pixso-instance-6360_52672 .Pixso-symbol-5588_11523 {
    width: 36px;
    height: 28px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 6px;
    justify-content: center;
    align-items: center;
    padding: 4px 10px 4px 10px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-6360_52672 .Pixso-instance-5588_11524 {
    width: 16px;
    height: 16px;
}
.Pixso-instance-6360_52672 .Pixso-frame-5588_11525 {
    width: 9px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 5px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-6360_52672 .Pixso-instance-5588_11526 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-6360_52672 .Pixso-paragraph-5588_11527 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-6360_52672 .Pixso-instance-5588_11528 {
    width: 16px;
    height: 16px;
}
.Pixso-instance-6360_52672 .Pixso-instance-6360_52672 {
    width: 36px;
    height: 28px;
}
.Pixso-instance-6360_52841 .Pixso-symbol-6360_52667 {
    width: 280px;
    height: 48px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
    padding: 10px 12px 10px 12px;
    min-height: 48px;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-6360_52841 .Pixso-frame-6360_52668 {
    width: 100%;
    height: 24px;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-6360_52841 .Pixso-instance-6360_52669 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-6360_52841 .Pixso-paragraph-6360_52671 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-6360_52841 .Pixso-instance-6360_52672 {
    width: 36px;
    height: 28px;
}
.Pixso-instance-6360_52841 .Pixso-instance-6360_52673 {
    width: 24px;
    height: 24px;
}
.Pixso-instance-6360_52841
    .Pixso-instance-6360_52672
    .Pixso-instance-5588_11524 {
    width: 16px;
    height: 16px;
}
.Pixso-instance-6360_52841 .Pixso-instance-6360_52672 .Pixso-frame-5588_11525 {
    width: 50px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 5px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-6360_52841
    .Pixso-instance-6360_52672
    .Pixso-instance-5588_11526 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-6360_52841
    .Pixso-instance-6360_52672
    .Pixso-paragraph-5588_11527 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-6360_52841
    .Pixso-instance-6360_52672
    .Pixso-instance-5588_11528 {
    width: 16px;
    height: 16px;
}
.Pixso-instance-6360_52670 .Pixso-instance-6360_52670 {
    width: 24px;
    height: 24px;
}
.Pixso-instance-6360_52842 .Pixso-symbol-6360_52667 {
    width: 280px;
    height: 48px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
    padding: 10px 12px 10px 12px;
    min-height: 48px;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-6360_52842 .Pixso-frame-6360_52668 {
    width: 100%;
    height: 24px;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-6360_52842 .Pixso-instance-6360_52669 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-6360_52842
    .Pixso-instance-6360_52670
    .Pixso-symbol-5579_152493 {
    width: 24px;
    height: 24px;
    position: absolute;
    left: 0px;
    top: 0px;
    background-color: transparent;
}
.Pixso-instance-6360_52842 .Pixso-paragraph-6360_52671 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-6360_52842 .Pixso-instance-6360_52672 {
    width: 36px;
    height: 28px;
}
.Pixso-instance-6360_52842 .Pixso-instance-6360_52673 {
    width: 24px;
    height: 24px;
}
.Pixso-instance-6360_52842
    .Pixso-instance-6360_52670
    .Pixso-vector-5579_152494 {
    width: 99.21%;
    height: 64.1%;
    background-image: url(@/assets/images/Vector54.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 0.39%;
    right: 0.4%;
    top: 17.17%;
    bottom: 18.73%;
}
.Pixso-instance-6360_52842
    .Pixso-instance-6360_52672
    .Pixso-instance-5588_11524 {
    width: 16px;
    height: 16px;
}
.Pixso-instance-6360_52842 .Pixso-instance-6360_52672 .Pixso-frame-5588_11525 {
    width: 9px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 5px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-6360_52842
    .Pixso-instance-6360_52672
    .Pixso-instance-5588_11526 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-6360_52842
    .Pixso-instance-6360_52672
    .Pixso-paragraph-5588_11527 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-6360_52842
    .Pixso-instance-6360_52672
    .Pixso-instance-5588_11528 {
    width: 16px;
    height: 16px;
}
.Pixso-instance-6360_52670 .Pixso-vector-5579_152494 {
    width: 99.21%;
    height: 64.1%;
    position: absolute;
    left: 0.39%;
    right: 0.4%;
    top: 17.17%;
    bottom: 18.73%;
}
.Pixso-instance-6360_52843 .Pixso-symbol-6360_52667 {
    width: 280px;
    height: 48px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
    padding: 10px 12px 10px 12px;
    min-height: 48px;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-6360_52843 .Pixso-frame-6360_52668 {
    width: 100%;
    height: 24px;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-6360_52843 .Pixso-instance-6360_52669 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-6360_52843
    .Pixso-instance-6360_52670
    .Pixso-symbol-5578_149025 {
    width: 24px;
    height: 24px;
    position: absolute;
    left: 0px;
    top: 0px;
    background-color: transparent;
}
.Pixso-instance-6360_52843 .Pixso-paragraph-6360_52671 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-6360_52843 .Pixso-instance-6360_52672 {
    width: 36px;
    height: 28px;
}
.Pixso-instance-6360_52843 .Pixso-instance-6360_52673 {
    width: 24px;
    height: 24px;
}
.Pixso-instance-6360_52843
    .Pixso-instance-6360_52670
    .Pixso-vector-5578_149026 {
    width: 84.38%;
    height: 90.62%;
    background-image: url(@/assets/images/Vector15.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 4.69%;
    bottom: 4.69%;
}
.Pixso-instance-6360_52843
    .Pixso-instance-6360_52672
    .Pixso-instance-5588_11524 {
    width: 16px;
    height: 16px;
}
.Pixso-instance-6360_52843 .Pixso-instance-6360_52672 .Pixso-frame-5588_11525 {
    width: 50px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 5px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-6360_52843
    .Pixso-instance-6360_52672
    .Pixso-instance-5588_11526 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-6360_52843
    .Pixso-instance-6360_52672
    .Pixso-paragraph-5588_11527 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-6360_52843
    .Pixso-instance-6360_52672
    .Pixso-instance-5588_11528 {
    width: 16px;
    height: 16px;
}
.Pixso-instance-6360_52670 .Pixso-vector-5578_149026 {
    width: 84.38%;
    height: 90.62%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 4.69%;
    bottom: 4.69%;
}
.Pixso-instance-6360_52844 .Pixso-symbol-6360_52667 {
    width: 280px;
    height: 48px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
    padding: 10px 12px 10px 12px;
    min-height: 48px;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-6360_52844 .Pixso-frame-6360_52668 {
    width: 100%;
    height: 24px;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-6360_52844 .Pixso-instance-6360_52669 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-6360_52844
    .Pixso-instance-6360_52670
    .Pixso-symbol-5579_152031 {
    width: 24px;
    height: 24px;
    position: absolute;
    left: 0px;
    top: 0px;
    background-color: transparent;
}
.Pixso-instance-6360_52844 .Pixso-paragraph-6360_52671 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-6360_52844 .Pixso-instance-6360_52672 {
    width: 36px;
    height: 28px;
}
.Pixso-instance-6360_52844 .Pixso-instance-6360_52673 {
    width: 24px;
    height: 24px;
}
.Pixso-instance-6360_52844
    .Pixso-instance-6360_52670
    .Pixso-vector-5579_152032 {
    width: 90.62%;
    height: 65.62%;
    background-image: url(@/assets/images/Vector2031.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 4.69%;
    right: 4.69%;
    top: 17.19%;
    bottom: 17.19%;
}
.Pixso-instance-6360_52844
    .Pixso-instance-6360_52672
    .Pixso-instance-5588_11524 {
    width: 16px;
    height: 16px;
}
.Pixso-instance-6360_52844 .Pixso-instance-6360_52672 .Pixso-frame-5588_11525 {
    width: 50px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 5px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-6360_52844
    .Pixso-instance-6360_52672
    .Pixso-instance-5588_11526 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-6360_52844
    .Pixso-instance-6360_52672
    .Pixso-paragraph-5588_11527 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-6360_52844
    .Pixso-instance-6360_52672
    .Pixso-instance-5588_11528 {
    width: 16px;
    height: 16px;
}
.Pixso-instance-6360_52670 .Pixso-vector-5579_152032 {
    width: 90.62%;
    height: 65.62%;
    position: absolute;
    left: 4.69%;
    right: 4.69%;
    top: 17.19%;
    bottom: 17.19%;
}
.Pixso-instance-6360_52845 .Pixso-symbol-6360_52667 {
    width: 280px;
    height: 48px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
    padding: 10px 12px 10px 12px;
    min-height: 48px;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-6360_52845 .Pixso-frame-6360_52668 {
    width: 100%;
    height: 24px;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-6360_52845 .Pixso-instance-6360_52669 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-6360_52845
    .Pixso-instance-6360_52670
    .Pixso-symbol-5578_150332 {
    width: 24px;
    height: 24px;
    position: absolute;
    left: 0px;
    top: 0px;
    background-color: transparent;
}
.Pixso-instance-6360_52845 .Pixso-paragraph-6360_52671 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-6360_52845 .Pixso-instance-6360_52672 {
    width: 36px;
    height: 28px;
}
.Pixso-instance-6360_52845 .Pixso-instance-6360_52673 {
    width: 24px;
    height: 24px;
}
.Pixso-instance-6360_52845
    .Pixso-instance-6360_52670
    .Pixso-vector-5578_150333 {
    width: 90.61%;
    height: 84.38%;
    background-image: url(@/assets/images/Vector87.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 4.7%;
    right: 4.69%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-6360_52845
    .Pixso-instance-6360_52672
    .Pixso-instance-5588_11524 {
    width: 16px;
    height: 16px;
}
.Pixso-instance-6360_52845 .Pixso-instance-6360_52672 .Pixso-frame-5588_11525 {
    width: 50px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 5px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-6360_52845
    .Pixso-instance-6360_52672
    .Pixso-instance-5588_11526 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-6360_52845
    .Pixso-instance-6360_52672
    .Pixso-paragraph-5588_11527 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-6360_52845
    .Pixso-instance-6360_52672
    .Pixso-instance-5588_11528 {
    width: 16px;
    height: 16px;
}
.Pixso-instance-6360_52670 .Pixso-vector-5578_150333 {
    width: 90.61%;
    height: 84.38%;
    position: absolute;
    left: 4.7%;
    right: 4.69%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-6360_52846 .Pixso-symbol-6360_52667 {
    width: 280px;
    height: 48px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
    padding: 10px 12px 10px 12px;
    min-height: 48px;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-6360_52846 .Pixso-frame-6360_52668 {
    width: 100%;
    height: 24px;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-6360_52846 .Pixso-instance-6360_52669 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-6360_52846
    .Pixso-instance-6360_52670
    .Pixso-symbol-5577_146643 {
    width: 24px;
    height: 24px;
    position: absolute;
    left: 0px;
    top: 0px;
    background-color: transparent;
}
.Pixso-instance-6360_52846 .Pixso-paragraph-6360_52671 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-6360_52846 .Pixso-instance-6360_52672 {
    width: 36px;
    height: 28px;
}
.Pixso-instance-6360_52846 .Pixso-instance-6360_52673 {
    width: 24px;
    height: 24px;
}
.Pixso-instance-6360_52846
    .Pixso-instance-6360_52670
    .Pixso-vector-5577_146644 {
    width: 81.25%;
    height: 81.25%;
    background-image: url(@/assets/images/Vector327.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 10.94%;
    right: 7.81%;
    top: 7.81%;
    bottom: 10.94%;
}
.Pixso-instance-6360_52846
    .Pixso-instance-6360_52672
    .Pixso-instance-5588_11524 {
    width: 16px;
    height: 16px;
}
.Pixso-instance-6360_52846 .Pixso-instance-6360_52672 .Pixso-frame-5588_11525 {
    width: 50px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 5px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-6360_52846
    .Pixso-instance-6360_52672
    .Pixso-instance-5588_11526 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-6360_52846
    .Pixso-instance-6360_52672
    .Pixso-paragraph-5588_11527 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-6360_52846
    .Pixso-instance-6360_52672
    .Pixso-instance-5588_11528 {
    width: 16px;
    height: 16px;
}
.Pixso-instance-6360_52670 .Pixso-vector-5577_146644 {
    width: 81.25%;
    height: 81.25%;
    position: absolute;
    left: 10.94%;
    right: 7.81%;
    top: 7.81%;
    bottom: 10.94%;
}
.Pixso-instance-6360_52848 .Pixso-symbol-6360_54320 {
    width: 280px;
    height: 168px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    gap: 16px;
    align-items: flex-start;
    padding: 16px 16px 16px 16px;
    border-radius: 24px 24px 24px 24px;
}
.Pixso-instance-6360_52848 .Pixso-frame-6360_54322 {
    width: 100%;
    height: 40px;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: row;
    gap: 10px;
    align-items: flex-start;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-6360_52848 .Pixso-instance-6360_54323 {
    width: 40px;
    height: 40px;
}
.Pixso-instance-6360_52848 .Pixso-instance-6360_54324 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-6360_52848 .Pixso-instance-6360_54327 {
    width: 52px;
    height: 20px;
}
.Pixso-instance-6360_52848 .Pixso-instance-6360_54328 {
    width: 46px;
    height: 20px;
}
.Pixso-instance-6360_52848
    .Pixso-instance-6360_54327
    .Pixso-instance-5603_17110 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-6360_52848
    .Pixso-instance-6360_54327
    .Pixso-paragraph-5603_17111 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-6360_52848
    .Pixso-instance-6360_54327
    .Pixso-instance-5603_17112 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-6360_52848
    .Pixso-instance-6360_54328
    .Pixso-instance-5603_17350 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-6360_52848
    .Pixso-instance-6360_54328
    .Pixso-paragraph-5603_17351 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-6360_52848
    .Pixso-instance-6360_54328
    .Pixso-instance-5603_17352 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-6360_52848
    .Pixso-instance-6360_54328
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
.Pixso-instance-6360_54327 .Pixso-instance-6360_54327 {
    width: 52px;
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
.Pixso-instance-6360_54328
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
.Pixso-instance-6360_54328 .Pixso-instance-6360_54328 {
    width: 46px;
    height: 20px;
}
.Pixso-instance-6360_52851 .Pixso-symbol-5468_1033 {
    width: 40px;
    height: 40px;
    position: relative;
    flex-shrink: 0;
    border-radius: 76.875px 76.875px 76.875px 76.875px;
}
.Pixso-instance-6360_52855 .Pixso-symbol-5591_22531 {
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
.Pixso-instance-6360_52855
    .Pixso-instance-5591_22532
    .Pixso-symbol-5578_150697 {
    width: 24px;
    height: 24px;
    position: absolute;
    left: 0px;
    top: 0px;
    background-color: transparent;
}
.Pixso-instance-6360_52855
    .Pixso-instance-5591_22532
    .Pixso-vector-5578_150698 {
    width: 78.13%;
    height: 78.12%;
    background-image: url(@/assets/images/Vector111.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 14.06%;
    right: 7.81%;
    top: 10.94%;
    bottom: 10.94%;
}
.Pixso-instance-5976_55198 .Pixso-instance-5572_73848 .Pixso-symbol-5572_73168 {
    width: 100%;
    height: 100%;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 5px;
    justify-content: center;
    align-items: center;
    border-radius: 12px 12px 12px 12px;
    box-shadow: 0px 4px 8px 0px rgba(79, 70, 229, 0.1);
}
.Pixso-instance-5976_55198
    .Pixso-instance-5572_73848
    .stroke-wrapper-5572_73168 {
    width: 32px;
    height: 32px;
    display: flex;
}
.Pixso-instance-5976_55198 .Pixso-instance-5572_73848 .stroke-5572_73168 {
    inset: 0px;
    border-radius: 12px 12px 12px 12px;
    pointer-events: none;
    border-width: 0.5px 0.5px 0.5px 0.5px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5976_55198 .Pixso-vector-5572_73849 {
    width: 69px;
    height: 17px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5976_55198 .Pixso-symbol-5572_73852 {
    width: 109px;
    height: 32px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
}
.Pixso-instance-5572_73848 .Pixso-symbol-5572_73168 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 5px;
    justify-content: center;
    align-items: center;
    border-radius: 12px 12px 12px 12px;
    box-shadow: 0px 4px 8px 0px rgba(79, 70, 229, 0.1);
}
.Pixso-instance-5572_73848 .stroke-wrapper-5572_73168 {
    width: 32px;
    height: 32px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5572_73848 .stroke-5572_73168 {
    inset: 0px;
    border-radius: 12px 12px 12px 12px;
    pointer-events: none;
    border-width: 0.5px 0.5px 0.5px 0.5px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5976_58202 .Pixso-instance-5976_53794 {
    width: 320px;
    height: 40px;
}
.Pixso-instance-5976_58202
    .Pixso-instance-5976_53794
    .Pixso-instance-5976_52049 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5976_58202
    .Pixso-instance-5976_53794
    .Pixso-instance-5976_52049
    .Pixso-vector-5578_150579 {
    width: 70.4%;
    height: 70.4%;
    background-image: url(@/assets/images/Vector105.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 6.44%;
    right: 23.16%;
    top: 6.44%;
    bottom: 23.16%;
}
.Pixso-instance-5980_54129 .Pixso-symbol-5982_54577 {
    width: 280px;
    height: 48px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
    padding: 10px 12px 10px 12px;
    min-height: 48px;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5980_54129 .Pixso-frame-5982_54578 {
    width: 100%;
    height: 24px;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5980_54129 .Pixso-instance-5982_54579 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5980_54129 .Pixso-instance-5982_54580 {
    width: 24px;
    height: 24px;
}
.Pixso-instance-5980_54129 .Pixso-paragraph-5982_54581 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5980_54129 .Pixso-instance-5982_54582 {
    width: 36px;
    height: 28px;
}
.Pixso-instance-5980_54129 .Pixso-instance-5982_54583 {
    width: 24px;
    height: 24px;
}
.Pixso-instance-5980_54129
    .Pixso-instance-5982_54582
    .Pixso-instance-5588_11524 {
    width: 16px;
    height: 16px;
}
.Pixso-instance-5980_54129 .Pixso-instance-5982_54582 .Pixso-frame-5588_11525 {
    width: 50px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 5px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5980_54129
    .Pixso-instance-5982_54582
    .Pixso-instance-5588_11526 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5980_54129
    .Pixso-instance-5982_54582
    .Pixso-paragraph-5588_11527 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5980_54129
    .Pixso-instance-5982_54582
    .Pixso-instance-5588_11528 {
    width: 16px;
    height: 16px;
}
.Pixso-instance-5982_54582 .Pixso-symbol-5588_11523 {
    width: 36px;
    height: 28px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 6px;
    justify-content: center;
    align-items: center;
    padding: 4px 10px 4px 10px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5982_54582 .Pixso-instance-5588_11524 {
    width: 16px;
    height: 16px;
}
.Pixso-instance-5982_54582 .Pixso-frame-5588_11525 {
    width: 9px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 5px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5982_54582 .Pixso-instance-5588_11526 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5982_54582 .Pixso-paragraph-5588_11527 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5982_54582 .Pixso-instance-5588_11528 {
    width: 16px;
    height: 16px;
}
.Pixso-instance-5982_54582 .Pixso-instance-5982_54582 {
    width: 36px;
    height: 28px;
}
.Pixso-instance-5982_54782 .Pixso-symbol-5982_54577 {
    width: 280px;
    height: 48px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
    padding: 10px 12px 10px 12px;
    min-height: 48px;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5982_54782 .Pixso-frame-5982_54578 {
    width: 100%;
    height: 24px;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5982_54782 .Pixso-instance-5982_54579 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5982_54782 .Pixso-paragraph-5982_54581 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5982_54782 .Pixso-instance-5982_54582 {
    width: 36px;
    height: 28px;
}
.Pixso-instance-5982_54782 .Pixso-instance-5982_54583 {
    width: 24px;
    height: 24px;
}
.Pixso-instance-5982_54782
    .Pixso-instance-5982_54582
    .Pixso-instance-5588_11524 {
    width: 16px;
    height: 16px;
}
.Pixso-instance-5982_54782 .Pixso-instance-5982_54582 .Pixso-frame-5588_11525 {
    width: 50px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 5px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5982_54782
    .Pixso-instance-5982_54582
    .Pixso-instance-5588_11526 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5982_54782
    .Pixso-instance-5982_54582
    .Pixso-paragraph-5588_11527 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5982_54782
    .Pixso-instance-5982_54582
    .Pixso-instance-5588_11528 {
    width: 16px;
    height: 16px;
}
.Pixso-instance-5982_54580 .Pixso-instance-5982_54580 {
    width: 24px;
    height: 24px;
}
.Pixso-instance-5982_54844 .Pixso-symbol-5982_54577 {
    width: 280px;
    height: 48px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
    padding: 10px 12px 10px 12px;
    min-height: 48px;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5982_54844 .Pixso-frame-5982_54578 {
    width: 100%;
    height: 24px;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5982_54844 .Pixso-instance-5982_54579 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5982_54844
    .Pixso-instance-5982_54580
    .Pixso-symbol-5579_152493 {
    width: 24px;
    height: 24px;
    position: absolute;
    left: 0px;
    top: 0px;
    background-color: transparent;
}
.Pixso-instance-5982_54844 .Pixso-paragraph-5982_54581 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5982_54844 .Pixso-instance-5982_54582 {
    width: 36px;
    height: 28px;
}
.Pixso-instance-5982_54844 .Pixso-instance-5982_54583 {
    width: 24px;
    height: 24px;
}
.Pixso-instance-5982_54844
    .Pixso-instance-5982_54580
    .Pixso-vector-5579_152494 {
    width: 99.21%;
    height: 64.1%;
    background-image: url(@/assets/images/Vector54.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 0.39%;
    right: 0.4%;
    top: 17.17%;
    bottom: 18.73%;
}
.Pixso-instance-5982_54844
    .Pixso-instance-5982_54582
    .Pixso-instance-5588_11524 {
    width: 16px;
    height: 16px;
}
.Pixso-instance-5982_54844 .Pixso-instance-5982_54582 .Pixso-frame-5588_11525 {
    width: 9px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 5px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5982_54844
    .Pixso-instance-5982_54582
    .Pixso-instance-5588_11526 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5982_54844
    .Pixso-instance-5982_54582
    .Pixso-paragraph-5588_11527 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5982_54844
    .Pixso-instance-5982_54582
    .Pixso-instance-5588_11528 {
    width: 16px;
    height: 16px;
}
.Pixso-instance-5982_54580 .Pixso-vector-5579_152494 {
    width: 99.21%;
    height: 64.1%;
    position: absolute;
    left: 0.39%;
    right: 0.4%;
    top: 17.17%;
    bottom: 18.73%;
}
.Pixso-instance-5982_54921 .Pixso-symbol-5982_54577 {
    width: 280px;
    height: 48px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
    padding: 10px 12px 10px 12px;
    min-height: 48px;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5982_54921 .Pixso-frame-5982_54578 {
    width: 100%;
    height: 24px;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5982_54921 .Pixso-instance-5982_54579 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5982_54921
    .Pixso-instance-5982_54580
    .Pixso-symbol-5578_149025 {
    width: 24px;
    height: 24px;
    position: absolute;
    left: 0px;
    top: 0px;
    background-color: transparent;
}
.Pixso-instance-5982_54921 .Pixso-paragraph-5982_54581 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5982_54921 .Pixso-instance-5982_54582 {
    width: 36px;
    height: 28px;
}
.Pixso-instance-5982_54921 .Pixso-instance-5982_54583 {
    width: 24px;
    height: 24px;
}
.Pixso-instance-5982_54921
    .Pixso-instance-5982_54580
    .Pixso-vector-5578_149026 {
    width: 84.38%;
    height: 90.62%;
    background-image: url(@/assets/images/Vector15.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 4.69%;
    bottom: 4.69%;
}
.Pixso-instance-5982_54921
    .Pixso-instance-5982_54582
    .Pixso-instance-5588_11524 {
    width: 16px;
    height: 16px;
}
.Pixso-instance-5982_54921 .Pixso-instance-5982_54582 .Pixso-frame-5588_11525 {
    width: 50px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 5px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5982_54921
    .Pixso-instance-5982_54582
    .Pixso-instance-5588_11526 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5982_54921
    .Pixso-instance-5982_54582
    .Pixso-paragraph-5588_11527 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5982_54921
    .Pixso-instance-5982_54582
    .Pixso-instance-5588_11528 {
    width: 16px;
    height: 16px;
}
.Pixso-instance-5982_54580 .Pixso-vector-5578_149026 {
    width: 84.38%;
    height: 90.62%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 4.69%;
    bottom: 4.69%;
}
.Pixso-instance-5982_55013 .Pixso-symbol-5982_54577 {
    width: 280px;
    height: 48px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
    padding: 10px 12px 10px 12px;
    min-height: 48px;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5982_55013 .Pixso-frame-5982_54578 {
    width: 100%;
    height: 24px;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5982_55013 .Pixso-instance-5982_54579 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5982_55013
    .Pixso-instance-5982_54580
    .Pixso-symbol-5579_152031 {
    width: 24px;
    height: 24px;
    position: absolute;
    left: 0px;
    top: 0px;
    background-color: transparent;
}
.Pixso-instance-5982_55013 .Pixso-paragraph-5982_54581 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5982_55013 .Pixso-instance-5982_54582 {
    width: 36px;
    height: 28px;
}
.Pixso-instance-5982_55013 .Pixso-instance-5982_54583 {
    width: 24px;
    height: 24px;
}
.Pixso-instance-5982_55013
    .Pixso-instance-5982_54580
    .Pixso-vector-5579_152032 {
    width: 90.62%;
    height: 65.62%;
    background-image: url(@/assets/images/Vector2031.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 4.69%;
    right: 4.69%;
    top: 17.19%;
    bottom: 17.19%;
}
.Pixso-instance-5982_55013
    .Pixso-instance-5982_54582
    .Pixso-instance-5588_11524 {
    width: 16px;
    height: 16px;
}
.Pixso-instance-5982_55013 .Pixso-instance-5982_54582 .Pixso-frame-5588_11525 {
    width: 50px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 5px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5982_55013
    .Pixso-instance-5982_54582
    .Pixso-instance-5588_11526 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5982_55013
    .Pixso-instance-5982_54582
    .Pixso-paragraph-5588_11527 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5982_55013
    .Pixso-instance-5982_54582
    .Pixso-instance-5588_11528 {
    width: 16px;
    height: 16px;
}
.Pixso-instance-5982_54580 .Pixso-vector-5579_152032 {
    width: 90.62%;
    height: 65.62%;
    position: absolute;
    left: 4.69%;
    right: 4.69%;
    top: 17.19%;
    bottom: 17.19%;
}
.Pixso-instance-5982_55120 .Pixso-symbol-5982_54577 {
    width: 280px;
    height: 48px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
    padding: 10px 12px 10px 12px;
    min-height: 48px;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5982_55120 .Pixso-frame-5982_54578 {
    width: 100%;
    height: 24px;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5982_55120 .Pixso-instance-5982_54579 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5982_55120
    .Pixso-instance-5982_54580
    .Pixso-symbol-5578_150332 {
    width: 24px;
    height: 24px;
    position: absolute;
    left: 0px;
    top: 0px;
    background-color: transparent;
}
.Pixso-instance-5982_55120 .Pixso-paragraph-5982_54581 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5982_55120 .Pixso-instance-5982_54582 {
    width: 36px;
    height: 28px;
}
.Pixso-instance-5982_55120 .Pixso-instance-5982_54583 {
    width: 24px;
    height: 24px;
}
.Pixso-instance-5982_55120
    .Pixso-instance-5982_54580
    .Pixso-vector-5578_150333 {
    width: 90.61%;
    height: 84.38%;
    background-image: url(@/assets/images/Vector87.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 4.7%;
    right: 4.69%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5982_55120
    .Pixso-instance-5982_54582
    .Pixso-instance-5588_11524 {
    width: 16px;
    height: 16px;
}
.Pixso-instance-5982_55120 .Pixso-instance-5982_54582 .Pixso-frame-5588_11525 {
    width: 50px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 5px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5982_55120
    .Pixso-instance-5982_54582
    .Pixso-instance-5588_11526 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5982_55120
    .Pixso-instance-5982_54582
    .Pixso-paragraph-5588_11527 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5982_55120
    .Pixso-instance-5982_54582
    .Pixso-instance-5588_11528 {
    width: 16px;
    height: 16px;
}
.Pixso-instance-5982_54580 .Pixso-vector-5578_150333 {
    width: 90.61%;
    height: 84.38%;
    position: absolute;
    left: 4.7%;
    right: 4.69%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5982_58638 .Pixso-symbol-5982_54577 {
    width: 280px;
    height: 48px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
    padding: 10px 12px 10px 12px;
    min-height: 48px;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-instance-5982_58638 .Pixso-frame-5982_54578 {
    width: 100%;
    height: 24px;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5982_58638 .Pixso-instance-5982_54579 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5982_58638
    .Pixso-instance-5982_54580
    .Pixso-symbol-5577_146643 {
    width: 24px;
    height: 24px;
    position: absolute;
    left: 0px;
    top: 0px;
    background-color: transparent;
}
.Pixso-instance-5982_58638 .Pixso-paragraph-5982_54581 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5982_58638 .Pixso-instance-5982_54582 {
    width: 36px;
    height: 28px;
}
.Pixso-instance-5982_58638 .Pixso-instance-5982_54583 {
    width: 24px;
    height: 24px;
}
.Pixso-instance-5982_58638
    .Pixso-instance-5982_54580
    .Pixso-vector-5577_146644 {
    width: 81.25%;
    height: 81.25%;
    background-image: url(@/assets/images/Vector327.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 10.94%;
    right: 7.81%;
    top: 7.81%;
    bottom: 10.94%;
}
.Pixso-instance-5982_58638
    .Pixso-instance-5982_54582
    .Pixso-instance-5588_11524 {
    width: 16px;
    height: 16px;
}
.Pixso-instance-5982_58638 .Pixso-instance-5982_54582 .Pixso-frame-5588_11525 {
    width: 50px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 5px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5982_58638
    .Pixso-instance-5982_54582
    .Pixso-instance-5588_11526 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5982_58638
    .Pixso-instance-5982_54582
    .Pixso-paragraph-5588_11527 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5982_58638
    .Pixso-instance-5982_54582
    .Pixso-instance-5588_11528 {
    width: 16px;
    height: 16px;
}
.Pixso-instance-5982_54580 .Pixso-vector-5577_146644 {
    width: 81.25%;
    height: 81.25%;
    position: absolute;
    left: 10.94%;
    right: 7.81%;
    top: 7.81%;
    bottom: 10.94%;
}
.Pixso-instance-6360_37700 .Pixso-instance-6359_30100 {
    width: 40px;
    height: 40px;
}
.Pixso-instance-6360_37700 .Pixso-symbol-6360_36905 {
    width: 280px;
    height: 168px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    gap: 16px;
    align-items: flex-start;
    padding: 16px 16px 16px 16px;
    border-radius: 24px 24px 24px 24px;
}
.Pixso-instance-6360_37700 .Pixso-frame-6360_36907 {
    width: 100%;
    height: 40px;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: row;
    gap: 10px;
    align-items: flex-start;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-6360_37700 .Pixso-instance-6360_36909 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-6360_37700 .Pixso-instance-6360_36912 {
    width: 52px;
    height: 20px;
}
.Pixso-instance-6360_37700 .Pixso-instance-6360_36913 {
    width: 46px;
    height: 20px;
}
.Pixso-instance-6360_37700
    .Pixso-instance-6360_36912
    .Pixso-instance-5603_17110 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-6360_37700
    .Pixso-instance-6360_36912
    .Pixso-paragraph-5603_17111 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-6360_37700
    .Pixso-instance-6360_36912
    .Pixso-instance-5603_17112 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-6360_37700
    .Pixso-instance-6360_36913
    .Pixso-instance-5603_17350 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-6360_37700
    .Pixso-instance-6360_36913
    .Pixso-paragraph-5603_17351 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-6360_37700
    .Pixso-instance-6360_36913
    .Pixso-instance-5603_17352 {
    width: 20px;
    height: 20px;
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
.Pixso-instance-6360_36912 .Pixso-instance-6360_36912 {
    width: 52px;
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
.Pixso-instance-6360_36913 .Pixso-instance-6360_36913 {
    width: 46px;
    height: 20px;
}
.Pixso-instance-5982_55911 .Pixso-symbol-5468_1033 {
    width: 40px;
    height: 40px;
    position: relative;
    flex-shrink: 0;
    border-radius: 76.875px 76.875px 76.875px 76.875px;
}
.Pixso-instance-5982_56899 .Pixso-symbol-5591_22529 {
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
.Pixso-instance-5982_56899
    .Pixso-instance-5591_22530
    .Pixso-symbol-5578_150697 {
    width: 24px;
    height: 24px;
    position: absolute;
    left: 0px;
    top: 0px;
    background-color: transparent;
}
.Pixso-instance-5982_56899
    .Pixso-instance-5591_22530
    .Pixso-vector-5578_150698 {
    width: 78.13%;
    height: 78.12%;
    background-image: url(@/assets/images/Vector111.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 14.06%;
    right: 7.81%;
    top: 10.94%;
    bottom: 10.94%;
}
.Pixso-instance-5591_22530 .Pixso-vector-5578_150698 {
    width: 78.13%;
    height: 78.12%;
    position: absolute;
    left: 14.06%;
    right: 7.81%;
    top: 10.94%;
    bottom: 10.94%;
}
.Pixso-instance-5591_22530 .Pixso-instance-5591_22530 {
    width: 24px;
    height: 24px;
}
.Pixso-instance-5648_26648 .Pixso-symbol-5572_73147 {
    width: 32px;
    height: 32px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 5px;
    justify-content: center;
    align-items: center;
    border-radius: 12px 12px 12px 12px;
    box-shadow: 0px 4px 8px 0px rgba(79, 70, 229, 0.1);
}
.Pixso-instance-5648_26642 .Pixso-symbol-5590_21883 {
    width: 48px;
    height: 48px;
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
.Pixso-instance-5648_26642 .Pixso-instance-5590_21884 .Pixso-symbol-6041_60589 {
    width: 24px;
    height: 24px;
    position: absolute;
    left: 0px;
    top: 0px;
    background-color: transparent;
}
.Pixso-instance-5648_26642 .Pixso-instance-5590_21884 .Pixso-vector-6041_60590 {
    width: 78.12%;
    height: 81.25%;
    background-image: url(@/assets/images/Vector339.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 10.94%;
    right: 10.94%;
    top: 7.81%;
    bottom: 10.94%;
}
.Pixso-instance-5590_21884 .Pixso-vector-6041_60590 {
    width: 78.12%;
    height: 81.25%;
    position: absolute;
    left: 10.94%;
    right: 10.94%;
    top: 7.81%;
    bottom: 10.94%;
}
.Pixso-instance-5590_21884 .Pixso-instance-5590_21884 {
    width: 24px;
    height: 24px;
}
.Pixso-instance-5648_26643 .Pixso-symbol-5590_22159 {
    width: 48px;
    height: 48px;
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
.Pixso-instance-5648_26643
    .Pixso-instance-5590_22160
    .Pixso-symbol-5579_150832 {
    width: 24px;
    height: 24px;
    position: absolute;
    left: 0px;
    top: 0px;
    background-color: transparent;
}
.Pixso-instance-5648_26643
    .Pixso-instance-5590_22160
    .Pixso-vector-5579_150833 {
    width: 84.38%;
    height: 75%;
    background-image: url(@/assets/images/Vector117.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 10.94%;
    bottom: 14.06%;
}
.Pixso-instance-5590_22160 .Pixso-vector-5579_150833 {
    width: 84.38%;
    height: 75%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 10.94%;
    bottom: 14.06%;
}
.Pixso-instance-5590_22160 .Pixso-instance-5590_22160 {
    width: 24px;
    height: 24px;
}
.Pixso-instance-5648_26644 .Pixso-symbol-5590_22159 {
    width: 48px;
    height: 48px;
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
.Pixso-instance-5648_26644
    .Pixso-instance-5590_22160
    .Pixso-symbol-5579_152455 {
    width: 24px;
    height: 24px;
    position: absolute;
    left: 0px;
    top: 0px;
    background-color: transparent;
}
.Pixso-instance-5648_26644
    .Pixso-instance-5590_22160
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
.Pixso-instance-5590_22160 .Pixso-vector-5579_152456 {
    width: 84.37%;
    height: 81.39%;
    position: absolute;
    left: 7.74%;
    right: 7.89%;
    top: 7.8%;
    bottom: 10.81%;
}
.Pixso-instance-5648_26645 .Pixso-symbol-5590_22159 {
    width: 48px;
    height: 48px;
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
.Pixso-instance-5648_26645
    .Pixso-instance-5590_22160
    .Pixso-symbol-5578_148822 {
    width: 24px;
    height: 24px;
    position: absolute;
    left: 0px;
    top: 0px;
    background-color: transparent;
}
.Pixso-instance-5648_26645
    .Pixso-instance-5590_22160
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
.Pixso-instance-5590_22160 .Pixso-vector-5578_148823 {
    width: 78.12%;
    height: 84.37%;
    position: absolute;
    left: 10.94%;
    right: 10.94%;
    top: 4.69%;
    bottom: 10.94%;
}
.Pixso-instance-5648_26766 .Pixso-symbol-5590_22159 {
    width: 48px;
    height: 48px;
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
.Pixso-instance-5648_26766
    .Pixso-instance-5590_22160
    .Pixso-symbol-5578_150464 {
    width: 24px;
    height: 24px;
    position: absolute;
    left: 0px;
    top: 0px;
    background-color: transparent;
}
.Pixso-instance-5648_26766
    .Pixso-instance-5590_22160
    .Pixso-vector-5578_150465 {
    width: 71.88%;
    height: 96.9%;
    background-image: url(@/assets/images/Vector93.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 14.06%;
    right: 14.06%;
    top: 1.55%;
    bottom: 1.55%;
}
.Pixso-instance-5590_22160 .Pixso-vector-5578_150465 {
    width: 71.88%;
    height: 96.9%;
    position: absolute;
    left: 14.06%;
    right: 14.06%;
    top: 1.55%;
    bottom: 1.55%;
}
.Pixso-instance-5648_26646 .Pixso-symbol-5590_22159 {
    width: 48px;
    height: 48px;
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
.Pixso-instance-5648_26646
    .Pixso-instance-5590_22160
    .Pixso-symbol-5578_149473 {
    width: 24px;
    height: 24px;
    position: absolute;
    left: 0px;
    top: 0px;
    background-color: transparent;
}
.Pixso-instance-5648_26646
    .Pixso-instance-5590_22160
    .Pixso-vector-5578_149474 {
    width: 78.12%;
    height: 84.38%;
    background-image: url(@/assets/images/Vector33.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 10.94%;
    right: 10.94%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5590_22160 .Pixso-vector-5578_149474 {
    width: 78.12%;
    height: 84.38%;
    position: absolute;
    left: 10.94%;
    right: 10.94%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5648_26647 .Pixso-symbol-5590_22159 {
    width: 48px;
    height: 48px;
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
.Pixso-instance-5648_26647
    .Pixso-instance-5590_22160
    .Pixso-symbol-5578_150332 {
    width: 24px;
    height: 24px;
    position: absolute;
    left: 0px;
    top: 0px;
    background-color: transparent;
}
.Pixso-instance-5648_26647
    .Pixso-instance-5590_22160
    .Pixso-vector-5578_150333 {
    width: 90.61%;
    height: 84.38%;
    background-image: url(@/assets/images/Vector87.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 4.7%;
    right: 4.69%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5590_22160 .Pixso-vector-5578_150333 {
    width: 90.61%;
    height: 84.38%;
    position: absolute;
    left: 4.7%;
    right: 4.69%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5648_26649 .Pixso-symbol-5468_1029 {
    width: 48px;
    height: 48px;
    position: relative;
    flex-shrink: 0;
    border-radius: 92.25px 92.25px 92.25px 92.25px;
}
.Pixso-instance-6361_54409 .Pixso-symbol-5572_73147 {
    width: 32px;
    height: 32px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 5px;
    justify-content: center;
    align-items: center;
    border-radius: 12px 12px 12px 12px;
    box-shadow: 0px 4px 8px 0px rgba(79, 70, 229, 0.1);
}
.Pixso-instance-6361_54411 .Pixso-symbol-5590_21883 {
    width: 48px;
    height: 48px;
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
.Pixso-instance-6361_54411 .Pixso-instance-5590_21884 .Pixso-symbol-6041_60589 {
    width: 24px;
    height: 24px;
    position: absolute;
    left: 0px;
    top: 0px;
    background-color: transparent;
}
.Pixso-instance-6361_54411 .Pixso-instance-5590_21884 .Pixso-vector-6041_60590 {
    width: 78.12%;
    height: 81.25%;
    background-image: url(@/assets/images/Vector339.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 10.94%;
    right: 10.94%;
    top: 7.81%;
    bottom: 10.94%;
}
.Pixso-instance-6361_54412 .Pixso-symbol-5590_22159 {
    width: 48px;
    height: 48px;
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
.Pixso-instance-6361_54412
    .Pixso-instance-5590_22160
    .Pixso-symbol-5579_150832 {
    width: 24px;
    height: 24px;
    position: absolute;
    left: 0px;
    top: 0px;
    background-color: transparent;
}
.Pixso-instance-6361_54412
    .Pixso-instance-5590_22160
    .Pixso-vector-5579_150833 {
    width: 84.38%;
    height: 75%;
    background-image: url(@/assets/images/Vector117.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 10.94%;
    bottom: 14.06%;
}
.Pixso-instance-6361_54413 .Pixso-symbol-5590_22159 {
    width: 48px;
    height: 48px;
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
.Pixso-instance-6361_54413
    .Pixso-instance-5590_22160
    .Pixso-symbol-5579_152455 {
    width: 24px;
    height: 24px;
    position: absolute;
    left: 0px;
    top: 0px;
    background-color: transparent;
}
.Pixso-instance-6361_54413
    .Pixso-instance-5590_22160
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
.Pixso-instance-6361_54414 .Pixso-symbol-5590_22159 {
    width: 48px;
    height: 48px;
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
.Pixso-instance-6361_54414
    .Pixso-instance-5590_22160
    .Pixso-symbol-5578_148822 {
    width: 24px;
    height: 24px;
    position: absolute;
    left: 0px;
    top: 0px;
    background-color: transparent;
}
.Pixso-instance-6361_54414
    .Pixso-instance-5590_22160
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
.Pixso-instance-6361_54415 .Pixso-symbol-5590_22159 {
    width: 48px;
    height: 48px;
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
.Pixso-instance-6361_54415
    .Pixso-instance-5590_22160
    .Pixso-symbol-5578_150464 {
    width: 24px;
    height: 24px;
    position: absolute;
    left: 0px;
    top: 0px;
    background-color: transparent;
}
.Pixso-instance-6361_54415
    .Pixso-instance-5590_22160
    .Pixso-vector-5578_150465 {
    width: 71.88%;
    height: 96.9%;
    background-image: url(@/assets/images/Vector93.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 14.06%;
    right: 14.06%;
    top: 1.55%;
    bottom: 1.55%;
}
.Pixso-instance-6361_54416 .Pixso-symbol-5590_22159 {
    width: 48px;
    height: 48px;
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
.Pixso-instance-6361_54416
    .Pixso-instance-5590_22160
    .Pixso-symbol-5578_149473 {
    width: 24px;
    height: 24px;
    position: absolute;
    left: 0px;
    top: 0px;
    background-color: transparent;
}
.Pixso-instance-6361_54416
    .Pixso-instance-5590_22160
    .Pixso-vector-5578_149474 {
    width: 78.12%;
    height: 84.38%;
    background-image: url(@/assets/images/Vector33.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 10.94%;
    right: 10.94%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-6361_54418 .Pixso-symbol-5590_22159 {
    width: 48px;
    height: 48px;
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
.Pixso-instance-6361_54418
    .Pixso-instance-5590_22160
    .Pixso-symbol-5578_150332 {
    width: 24px;
    height: 24px;
    position: absolute;
    left: 0px;
    top: 0px;
    background-color: transparent;
}
.Pixso-instance-6361_54418
    .Pixso-instance-5590_22160
    .Pixso-vector-5578_150333 {
    width: 90.61%;
    height: 84.38%;
    background-image: url(@/assets/images/Vector87.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 4.7%;
    right: 4.69%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-6361_54419 .Pixso-symbol-5468_1029 {
    width: 48px;
    height: 48px;
    position: relative;
    flex-shrink: 0;
    border-radius: 92.25px 92.25px 92.25px 92.25px;
}
.Pixso-instance-5648_26864 .Pixso-symbol-5572_73168 {
    width: 32px;
    height: 32px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 5px;
    justify-content: center;
    align-items: center;
    border-radius: 12px 12px 12px 12px;
    box-shadow: 0px 4px 8px 0px rgba(79, 70, 229, 0.1);
}
.Pixso-instance-5648_26866 .Pixso-symbol-5590_21883 {
    width: 48px;
    height: 48px;
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
.Pixso-instance-5648_26866 .Pixso-instance-5590_21884 .Pixso-symbol-6041_60589 {
    width: 24px;
    height: 24px;
    position: absolute;
    left: 0px;
    top: 0px;
    background-color: transparent;
}
.Pixso-instance-5648_26866 .Pixso-instance-5590_21884 .Pixso-vector-6041_60590 {
    width: 78.12%;
    height: 81.25%;
    background-image: url(@/assets/images/Vector339.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 10.94%;
    right: 10.94%;
    top: 7.81%;
    bottom: 10.94%;
}
.Pixso-instance-5648_26867 .Pixso-symbol-5590_22159 {
    width: 48px;
    height: 48px;
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
.Pixso-instance-5648_26867
    .Pixso-instance-5590_22160
    .Pixso-symbol-5579_150832 {
    width: 24px;
    height: 24px;
    position: absolute;
    left: 0px;
    top: 0px;
    background-color: transparent;
}
.Pixso-instance-5648_26867
    .Pixso-instance-5590_22160
    .Pixso-vector-5579_150833 {
    width: 84.38%;
    height: 75%;
    background-image: url(@/assets/images/Vector117.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 10.94%;
    bottom: 14.06%;
}
.Pixso-instance-5648_26868 .Pixso-symbol-5590_22159 {
    width: 48px;
    height: 48px;
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
.Pixso-instance-5648_26868
    .Pixso-instance-5590_22160
    .Pixso-symbol-5579_152455 {
    width: 24px;
    height: 24px;
    position: absolute;
    left: 0px;
    top: 0px;
    background-color: transparent;
}
.Pixso-instance-5648_26868
    .Pixso-instance-5590_22160
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
.Pixso-instance-5648_26869 .Pixso-symbol-5590_22159 {
    width: 48px;
    height: 48px;
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
.Pixso-instance-5648_26869
    .Pixso-instance-5590_22160
    .Pixso-symbol-5578_148822 {
    width: 24px;
    height: 24px;
    position: absolute;
    left: 0px;
    top: 0px;
    background-color: transparent;
}
.Pixso-instance-5648_26869
    .Pixso-instance-5590_22160
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
.Pixso-instance-5648_26870 .Pixso-symbol-5590_22159 {
    width: 48px;
    height: 48px;
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
.Pixso-instance-5648_26870
    .Pixso-instance-5590_22160
    .Pixso-symbol-5578_150464 {
    width: 24px;
    height: 24px;
    position: absolute;
    left: 0px;
    top: 0px;
    background-color: transparent;
}
.Pixso-instance-5648_26870
    .Pixso-instance-5590_22160
    .Pixso-vector-5578_150465 {
    width: 71.88%;
    height: 96.9%;
    background-image: url(@/assets/images/Vector93.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 14.06%;
    right: 14.06%;
    top: 1.55%;
    bottom: 1.55%;
}
.Pixso-instance-5648_26871 .Pixso-symbol-5590_22159 {
    width: 48px;
    height: 48px;
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
.Pixso-instance-5648_26871
    .Pixso-instance-5590_22160
    .Pixso-symbol-5578_149473 {
    width: 24px;
    height: 24px;
    position: absolute;
    left: 0px;
    top: 0px;
    background-color: transparent;
}
.Pixso-instance-5648_26871
    .Pixso-instance-5590_22160
    .Pixso-vector-5578_149474 {
    width: 78.12%;
    height: 84.38%;
    background-image: url(@/assets/images/Vector33.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 10.94%;
    right: 10.94%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5648_26887 .Pixso-symbol-5590_22159 {
    width: 48px;
    height: 48px;
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
.Pixso-instance-5648_26887
    .Pixso-instance-5590_22160
    .Pixso-symbol-5578_150332 {
    width: 24px;
    height: 24px;
    position: absolute;
    left: 0px;
    top: 0px;
    background-color: transparent;
}
.Pixso-instance-5648_26887
    .Pixso-instance-5590_22160
    .Pixso-vector-5578_150333 {
    width: 90.61%;
    height: 84.38%;
    background-image: url(@/assets/images/Vector87.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 4.7%;
    right: 4.69%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5648_26888 .Pixso-symbol-5468_1029 {
    width: 48px;
    height: 48px;
    position: relative;
    flex-shrink: 0;
    border-radius: 92.25px 92.25px 92.25px 92.25px;
}
.Pixso-instance-6361_54486 .Pixso-symbol-5572_73168 {
    width: 32px;
    height: 32px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 5px;
    justify-content: center;
    align-items: center;
    border-radius: 12px 12px 12px 12px;
    box-shadow: 0px 4px 8px 0px rgba(79, 70, 229, 0.1);
}
.Pixso-instance-6361_54488 .Pixso-symbol-5590_21883 {
    width: 48px;
    height: 48px;
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
.Pixso-instance-6361_54488 .Pixso-instance-5590_21884 .Pixso-symbol-6041_60589 {
    width: 24px;
    height: 24px;
    position: absolute;
    left: 0px;
    top: 0px;
    background-color: transparent;
}
.Pixso-instance-6361_54488 .Pixso-instance-5590_21884 .Pixso-vector-6041_60590 {
    width: 78.12%;
    height: 81.25%;
    background-image: url(@/assets/images/Vector339.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 10.94%;
    right: 10.94%;
    top: 7.81%;
    bottom: 10.94%;
}
.Pixso-instance-6361_54489 .Pixso-symbol-5590_22159 {
    width: 48px;
    height: 48px;
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
.Pixso-instance-6361_54489
    .Pixso-instance-5590_22160
    .Pixso-symbol-5579_150832 {
    width: 24px;
    height: 24px;
    position: absolute;
    left: 0px;
    top: 0px;
    background-color: transparent;
}
.Pixso-instance-6361_54489
    .Pixso-instance-5590_22160
    .Pixso-vector-5579_150833 {
    width: 84.38%;
    height: 75%;
    background-image: url(@/assets/images/Vector117.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 10.94%;
    bottom: 14.06%;
}
.Pixso-instance-6361_54490 .Pixso-symbol-5590_22159 {
    width: 48px;
    height: 48px;
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
.Pixso-instance-6361_54490
    .Pixso-instance-5590_22160
    .Pixso-symbol-5579_152455 {
    width: 24px;
    height: 24px;
    position: absolute;
    left: 0px;
    top: 0px;
    background-color: transparent;
}
.Pixso-instance-6361_54490
    .Pixso-instance-5590_22160
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
.Pixso-instance-6361_54491 .Pixso-symbol-5590_22159 {
    width: 48px;
    height: 48px;
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
.Pixso-instance-6361_54491
    .Pixso-instance-5590_22160
    .Pixso-symbol-5578_148822 {
    width: 24px;
    height: 24px;
    position: absolute;
    left: 0px;
    top: 0px;
    background-color: transparent;
}
.Pixso-instance-6361_54491
    .Pixso-instance-5590_22160
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
.Pixso-instance-6361_54492 .Pixso-symbol-5590_22159 {
    width: 48px;
    height: 48px;
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
.Pixso-instance-6361_54492
    .Pixso-instance-5590_22160
    .Pixso-symbol-5578_150464 {
    width: 24px;
    height: 24px;
    position: absolute;
    left: 0px;
    top: 0px;
    background-color: transparent;
}
.Pixso-instance-6361_54492
    .Pixso-instance-5590_22160
    .Pixso-vector-5578_150465 {
    width: 71.88%;
    height: 96.9%;
    background-image: url(@/assets/images/Vector93.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 14.06%;
    right: 14.06%;
    top: 1.55%;
    bottom: 1.55%;
}
.Pixso-instance-6361_54493 .Pixso-symbol-5590_22159 {
    width: 48px;
    height: 48px;
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
.Pixso-instance-6361_54493
    .Pixso-instance-5590_22160
    .Pixso-symbol-5578_149473 {
    width: 24px;
    height: 24px;
    position: absolute;
    left: 0px;
    top: 0px;
    background-color: transparent;
}
.Pixso-instance-6361_54493
    .Pixso-instance-5590_22160
    .Pixso-vector-5578_149474 {
    width: 78.12%;
    height: 84.38%;
    background-image: url(@/assets/images/Vector33.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 10.94%;
    right: 10.94%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-6361_54495 .Pixso-symbol-5590_22159 {
    width: 48px;
    height: 48px;
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
.Pixso-instance-6361_54495
    .Pixso-instance-5590_22160
    .Pixso-symbol-5578_150332 {
    width: 24px;
    height: 24px;
    position: absolute;
    left: 0px;
    top: 0px;
    background-color: transparent;
}
.Pixso-instance-6361_54495
    .Pixso-instance-5590_22160
    .Pixso-vector-5578_150333 {
    width: 90.61%;
    height: 84.38%;
    background-image: url(@/assets/images/Vector87.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 4.7%;
    right: 4.69%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-6361_54496 .Pixso-symbol-5468_1029 {
    width: 48px;
    height: 48px;
    position: relative;
    flex-shrink: 0;
    border-radius: 92.25px 92.25px 92.25px 92.25px;
}
.Pixso-instance-6012_50234 .Pixso-instance-5572_73848 .Pixso-symbol-5572_73168 {
    width: 100%;
    height: 100%;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 5px;
    justify-content: center;
    align-items: center;
    border-radius: 12px 12px 12px 12px;
    box-shadow: 0px 4px 8px 0px rgba(79, 70, 229, 0.1);
}
.Pixso-instance-6012_50234
    .Pixso-instance-5572_73848
    .stroke-wrapper-5572_73168 {
    width: 32px;
    height: 32px;
    display: flex;
}
.Pixso-instance-6012_50234 .Pixso-instance-5572_73848 .stroke-5572_73168 {
    inset: 0px;
    border-radius: 12px 12px 12px 12px;
    pointer-events: none;
    border-width: 0.5px 0.5px 0.5px 0.5px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-6012_50234 .Pixso-vector-5572_73849 {
    width: 69px;
    height: 17px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-6012_50234 .Pixso-symbol-5572_73852 {
    width: 109px;
    height: 32px;
    position: absolute;
    left: 0px;
    top: 0px;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
}
.Pixso-instance-6012_50235 .Pixso-symbol-5590_22157 {
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
.Pixso-instance-6012_50235
    .Pixso-instance-5590_22158
    .Pixso-symbol-5579_151727 {
    width: 24px;
    height: 24px;
    position: absolute;
    left: 0px;
    top: 0px;
    background-color: transparent;
}
.Pixso-instance-6012_50235
    .Pixso-instance-5590_22158
    .Pixso-vector-5579_151728 {
    width: 78.12%;
    height: 59.38%;
    background-image: url(@/assets/images/Vector2028.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 10.94%;
    right: 10.94%;
    top: 20.31%;
    bottom: 20.31%;
}
.Pixso-instance-5590_22158 .Pixso-vector-5579_151728 {
    width: 78.12%;
    height: 59.38%;
    position: absolute;
    left: 10.94%;
    right: 10.94%;
    top: 20.31%;
    bottom: 20.31%;
}
.Pixso-instance-6361_54543 .Pixso-instance-5572_73848 {
    width: 32px;
    height: 32px;
}
.Pixso-instance-6361_54543 .Pixso-vector-5572_73849 {
    width: 69px;
    height: 17px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-6361_54543 .Pixso-symbol-5572_73852 {
    width: 109px;
    height: 32px;
    position: absolute;
    left: 0px;
    top: 0px;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
}
.Pixso-instance-6361_54544 .Pixso-symbol-5590_22157 {
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
.Pixso-instance-6361_54544
    .Pixso-instance-5590_22158
    .Pixso-symbol-5579_151727 {
    width: 24px;
    height: 24px;
    position: absolute;
    left: 0px;
    top: 0px;
    background-color: transparent;
}
.Pixso-instance-6361_54544
    .Pixso-instance-5590_22158
    .Pixso-vector-5579_151728 {
    width: 78.12%;
    height: 59.38%;
    background-image: url(@/assets/images/Vector2028.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 10.94%;
    right: 10.94%;
    top: 20.31%;
    bottom: 20.31%;
}
.Pixso-instance-6012_50238 .Pixso-vector-5490_11743 {
    width: 69px;
    height: 17px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-6012_50238 .Pixso-symbol-5569_17873 {
    width: 109px;
    height: 32px;
    position: absolute;
    left: 0px;
    top: 0px;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
}
.Pixso-instance-6012_50238 .Pixso-instance-5572_73326 {
    width: 32px;
    height: 32px;
}
.Pixso-instance-6012_50239 .Pixso-symbol-5590_22157 {
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
.Pixso-instance-6012_50239
    .Pixso-instance-5590_22158
    .Pixso-symbol-5579_151727 {
    width: 24px;
    height: 24px;
    position: absolute;
    left: 0px;
    top: 0px;
    background-color: transparent;
}
.Pixso-instance-6012_50239
    .Pixso-instance-5590_22158
    .Pixso-vector-5579_151728 {
    width: 78.12%;
    height: 59.38%;
    background-image: url(@/assets/images/Vector2028.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 10.94%;
    right: 10.94%;
    top: 20.31%;
    bottom: 20.31%;
}
.Pixso-instance-6361_54524 .Pixso-vector-5490_11743 {
    width: 69px;
    height: 17px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-6361_54524 .Pixso-symbol-5569_17873 {
    width: 109px;
    height: 32px;
    position: absolute;
    left: 0px;
    top: 0px;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
}
.Pixso-instance-6361_54524 .Pixso-instance-5572_73326 {
    width: 32px;
    height: 32px;
}
.Pixso-instance-6361_54525 .Pixso-symbol-5590_22157 {
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
.Pixso-instance-6361_54525
    .Pixso-instance-5590_22158
    .Pixso-symbol-5579_151727 {
    width: 24px;
    height: 24px;
    position: absolute;
    left: 0px;
    top: 0px;
    background-color: transparent;
}
.Pixso-instance-6361_54525
    .Pixso-instance-5590_22158
    .Pixso-vector-5579_151728 {
    width: 78.12%;
    height: 59.38%;
    background-image: url(@/assets/images/Vector2028.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 10.94%;
    right: 10.94%;
    top: 20.31%;
    bottom: 20.31%;
}
.Pixso-instance-6361_54653 .Pixso-instance-5572_73848 .Pixso-symbol-5572_73168 {
    width: 100%;
    height: 100%;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 5px;
    justify-content: center;
    align-items: center;
    border-radius: 12px 12px 12px 12px;
    box-shadow: 0px 4px 8px 0px rgba(79, 70, 229, 0.1);
}
.Pixso-instance-6361_54653
    .Pixso-instance-5572_73848
    .stroke-wrapper-5572_73168 {
    width: 32px;
    height: 32px;
    display: flex;
}
.Pixso-instance-6361_54653 .Pixso-instance-5572_73848 .stroke-5572_73168 {
    inset: 0px;
    border-radius: 12px 12px 12px 12px;
    pointer-events: none;
    border-width: 0.5px 0.5px 0.5px 0.5px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-6361_54653 .Pixso-vector-5572_73849 {
    width: 69px;
    height: 17px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-6361_54653 .Pixso-symbol-5572_73852 {
    width: 109px;
    height: 32px;
    position: absolute;
    left: 0px;
    top: 0px;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
}
.Pixso-instance-6361_54654 .Pixso-symbol-5590_22157 {
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
.Pixso-instance-6361_54654
    .Pixso-instance-5590_22158
    .Pixso-symbol-5579_151727 {
    width: 24px;
    height: 24px;
    position: absolute;
    left: 0px;
    top: 0px;
    background-color: transparent;
}
.Pixso-instance-6361_54654
    .Pixso-instance-5590_22158
    .Pixso-vector-5579_151728 {
    width: 78.12%;
    height: 59.38%;
    background-image: url(@/assets/images/Vector2028.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 10.94%;
    right: 10.94%;
    top: 20.31%;
    bottom: 20.31%;
}
.Pixso-instance-6361_54657 .Pixso-instance-5572_73848 {
    width: 32px;
    height: 32px;
}
.Pixso-instance-6361_54657 .Pixso-vector-5572_73849 {
    width: 69px;
    height: 17px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-6361_54657 .Pixso-symbol-5572_73852 {
    width: 109px;
    height: 32px;
    position: absolute;
    left: 0px;
    top: 0px;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
}
.Pixso-instance-6361_54658 .Pixso-symbol-5590_22157 {
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
.Pixso-instance-6361_54658
    .Pixso-instance-5590_22158
    .Pixso-symbol-5579_151727 {
    width: 24px;
    height: 24px;
    position: absolute;
    left: 0px;
    top: 0px;
    background-color: transparent;
}
.Pixso-instance-6361_54658
    .Pixso-instance-5590_22158
    .Pixso-vector-5579_151728 {
    width: 78.12%;
    height: 59.38%;
    background-image: url(@/assets/images/Vector2028.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 10.94%;
    right: 10.94%;
    top: 20.31%;
    bottom: 20.31%;
}
.Pixso-instance-6361_54661 .Pixso-vector-5490_11743 {
    width: 69px;
    height: 17px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-6361_54661 .Pixso-symbol-5569_17873 {
    width: 109px;
    height: 32px;
    position: absolute;
    left: 0px;
    top: 0px;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
}
.Pixso-instance-6361_54661 .Pixso-instance-5572_73326 {
    width: 32px;
    height: 32px;
}
.Pixso-instance-6361_54662 .Pixso-symbol-5590_22157 {
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
.Pixso-instance-6361_54662
    .Pixso-instance-5590_22158
    .Pixso-symbol-5579_151727 {
    width: 24px;
    height: 24px;
    position: absolute;
    left: 0px;
    top: 0px;
    background-color: transparent;
}
.Pixso-instance-6361_54662
    .Pixso-instance-5590_22158
    .Pixso-vector-5579_151728 {
    width: 78.12%;
    height: 59.38%;
    background-image: url(@/assets/images/Vector2028.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 10.94%;
    right: 10.94%;
    top: 20.31%;
    bottom: 20.31%;
}
.Pixso-instance-6361_54665 .Pixso-vector-5490_11743 {
    width: 69px;
    height: 17px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-6361_54665 .Pixso-symbol-5569_17873 {
    width: 109px;
    height: 32px;
    position: absolute;
    left: 0px;
    top: 0px;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
}
.Pixso-instance-6361_54665 .Pixso-instance-5572_73326 {
    width: 32px;
    height: 32px;
}
.Pixso-instance-6361_54666 .Pixso-symbol-5590_22157 {
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
.Pixso-instance-6361_54666
    .Pixso-instance-5590_22158
    .Pixso-symbol-5579_151727 {
    width: 24px;
    height: 24px;
    position: absolute;
    left: 0px;
    top: 0px;
    background-color: transparent;
}
.Pixso-instance-6361_54666
    .Pixso-instance-5590_22158
    .Pixso-vector-5579_151728 {
    width: 78.12%;
    height: 59.38%;
    background-image: url(@/assets/images/Vector2028.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 10.94%;
    right: 10.94%;
    top: 20.31%;
    bottom: 20.31%;
}
.Pixso-instance-5982_59118 .Pixso-symbol-5976_53791 {
    width: 280px;
    height: 40px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    gap: 6px;
    align-items: flex-end;
}
.Pixso-instance-6360_51961 .Pixso-symbol-5976_53791 {
    width: 280px;
    height: 40px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    gap: 6px;
    align-items: flex-end;
}
.Pixso-instance-6360_52838 .Pixso-symbol-5976_53791 {
    width: 280px;
    height: 40px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    gap: 6px;
    align-items: flex-end;
}
.Pixso-instance-5976_58202 .Pixso-symbol-5976_53791 {
    width: 280px;
    height: 40px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    gap: 6px;
    align-items: flex-end;
}
.Pixso-instance-5982_59118 .Pixso-frame-5976_53792 {
    width: 100%;
    height: 40px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    gap: 6px;
    align-items: flex-end;
}
.Pixso-instance-6360_51961 .Pixso-frame-5976_53792 {
    width: 100%;
    height: 40px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    gap: 6px;
    align-items: flex-end;
}
.Pixso-instance-6360_52838 .Pixso-frame-5976_53792 {
    width: 100%;
    height: 40px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    gap: 6px;
    align-items: flex-end;
}
.Pixso-instance-5976_58202 .Pixso-frame-5976_53792 {
    width: 100%;
    height: 40px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    gap: 6px;
    align-items: flex-end;
}
.Pixso-instance-5982_59118
    .Pixso-instance-5976_53794
    .Pixso-instance-5976_52051 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5976_53794 .Pixso-instance-5976_52051 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-6360_51961
    .Pixso-instance-5976_53794
    .Pixso-instance-5976_52051 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-6360_52838
    .Pixso-instance-5976_53794
    .Pixso-instance-5976_52051 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5976_58202
    .Pixso-instance-5976_53794
    .Pixso-instance-5976_52051 {
    width: 20px;
    height: 20px;
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
.Pixso-instance-5982_59118 .Pixso-instance-5976_53794 .Pixso-frame-5976_52048 {
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
.Pixso-instance-6360_51961 .Pixso-instance-5976_53794 .Pixso-frame-5976_52048 {
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
.Pixso-instance-6360_52838 .Pixso-instance-5976_53794 .Pixso-frame-5976_52048 {
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
.Pixso-instance-5976_58202 .Pixso-instance-5976_53794 .Pixso-frame-5976_52048 {
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
.Pixso-instance-5982_59118
    .Pixso-instance-5976_53794
    .Pixso-paragraph-5976_52050 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
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
.Pixso-instance-6360_51961
    .Pixso-instance-5976_53794
    .Pixso-paragraph-5976_52050 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-6360_52838
    .Pixso-instance-5976_53794
    .Pixso-paragraph-5976_52050 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5976_58202
    .Pixso-instance-5976_53794
    .Pixso-paragraph-5976_52050 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5982_59121
    .Pixso-instance-5980_54116
    .Pixso-symbol-5579_151770 {
    width: 24px;
    height: 24px;
    position: absolute;
    left: 52px;
    top: 12px;
    background-color: transparent;
}
.Pixso-instance-6360_51964
    .Pixso-instance-6360_52183
    .Pixso-symbol-5579_151770 {
    width: 24px;
    height: 24px;
    position: absolute;
    left: 52px;
    top: 12px;
    background-color: transparent;
}
.Pixso-instance-6360_52841
    .Pixso-instance-6360_52670
    .Pixso-symbol-5579_151770 {
    width: 24px;
    height: 24px;
    position: absolute;
    left: 52px;
    top: 12px;
    background-color: transparent;
}
.Pixso-instance-5982_54782
    .Pixso-instance-5982_54580
    .Pixso-symbol-5579_151770 {
    width: 24px;
    height: 24px;
    position: absolute;
    left: 52px;
    top: 12px;
    background-color: transparent;
}
.Pixso-instance-5982_59121
    .Pixso-instance-5980_54116
    .Pixso-vector-5579_151771 {
    width: 78.12%;
    height: 62.5%;
    background-image: url(@/assets/images/Vector2063.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 10.94%;
    right: 10.94%;
    top: 18.75%;
    bottom: 18.75%;
}
.Pixso-instance-5980_54116 .Pixso-vector-5579_151771 {
    width: 78.12%;
    height: 62.5%;
    position: absolute;
    left: 10.94%;
    right: 10.94%;
    top: 18.75%;
    bottom: 18.75%;
}
.Pixso-instance-6360_51964
    .Pixso-instance-6360_52183
    .Pixso-vector-5579_151771 {
    width: 78.12%;
    height: 62.5%;
    background-image: url(@/assets/images/Vector2063.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 10.94%;
    right: 10.94%;
    top: 18.75%;
    bottom: 18.75%;
}
.Pixso-instance-6360_52183 .Pixso-vector-5579_151771 {
    width: 78.12%;
    height: 62.5%;
    position: absolute;
    left: 10.94%;
    right: 10.94%;
    top: 18.75%;
    bottom: 18.75%;
}
.Pixso-instance-6360_52841
    .Pixso-instance-6360_52670
    .Pixso-vector-5579_151771 {
    width: 78.12%;
    height: 62.5%;
    background-image: url(@/assets/images/Vector2063.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 10.94%;
    right: 10.94%;
    top: 18.75%;
    bottom: 18.75%;
}
.Pixso-instance-6360_52670 .Pixso-vector-5579_151771 {
    width: 78.12%;
    height: 62.5%;
    position: absolute;
    left: 10.94%;
    right: 10.94%;
    top: 18.75%;
    bottom: 18.75%;
}
.Pixso-instance-5982_54782
    .Pixso-instance-5982_54580
    .Pixso-vector-5579_151771 {
    width: 78.12%;
    height: 62.5%;
    background-image: url(@/assets/images/Vector2063.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 10.94%;
    right: 10.94%;
    top: 18.75%;
    bottom: 18.75%;
}
.Pixso-instance-5982_54580 .Pixso-vector-5579_151771 {
    width: 78.12%;
    height: 62.5%;
    position: absolute;
    left: 10.94%;
    right: 10.94%;
    top: 18.75%;
    bottom: 18.75%;
}
</style>
