<template>
    <div class="component-5606_19150">
        <div id="5606_19150" class="Pixso-symbol-5606_19150">
            <div
                id="5606_19081"
                class="stroke-wrapper-5606_19081"
                v-if="Type === 'Default' && Size === 'lg'"
            >
                <div
                    class="Pixso-symbol-5606_19081 fill-gray0-white-67_3285 fill-gray5-32_4120"
                >
                    <div id="5606_19162" class="Pixso-frame-5606_19162">
                        <div class="frame-content-5606_19162">
                            <slot name="slot_5606_19068" v-if="visible_5606_43">
                                <User
                                    id="5606_19068"
                                    class="Pixso-instance-5606_19068"
                                    Format="Outline"
                                    Weight="Bold"
                                />
                            </slot>
                            <slot name="slot_5606_19069">
                                <p
                                    id="5606_19069"
                                    class="Pixso-paragraph-5606_19069 fill-gray60-83_2722-paragraph text-text-mdmedium-5454_21606 fill-gray30-35_1481-paragraph"
                                >
                                    {{ text_5606_42 ?? "Placeholder Text" }}
                                </p>
                            </slot>
                        </div>
                    </div>
                    <slot name="slot_5606_19072" v-if="visible_5606_41">
                        <Question
                            id="5606_19072"
                            class="Pixso-instance-5606_19072"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div class="stroke-5606_19081 stroke-gray30-35_1481"></div>
            </div>
            <div
                id="5976_52047"
                class="stroke-wrapper-5976_52047"
                v-if="Type === 'Default' && Size === 'md'"
            >
                <div
                    class="Pixso-symbol-5976_52047 fill-gray0-white-67_3285 fill-gray5-32_4120"
                >
                    <div id="5976_52048" class="Pixso-frame-5976_52048">
                        <div class="frame-content-5976_52048">
                            <slot name="slot_5976_52049" v-if="visible_5606_43">
                                <User
                                    id="5976_52049"
                                    class="Pixso-instance-5976_52049"
                                    Format="Outline"
                                    Weight="Bold"
                                />
                            </slot>
                            <slot name="slot_5976_52050">
                                <p
                                    id="5976_52050"
                                    class="Pixso-paragraph-5976_52050 fill-gray60-83_2722-paragraph text-text-mdmedium-5454_21606 fill-gray0-white-67_3285-paragraph fill-gray30-35_1481-paragraph"
                                >
                                    {{ text_5606_42 ?? "Placeholder Text" }}
                                </p>
                            </slot>
                        </div>
                    </div>
                    <slot name="slot_5976_52051" v-if="visible_5606_41">
                        <Question
                            id="5976_52051"
                            class="Pixso-instance-5976_52051"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div class="stroke-5976_52047 stroke-gray30-35_1481"></div>
            </div>
            <div
                id="5606_19148"
                class="stroke-wrapper-5606_19148"
                v-if="Type === 'Action' && Size === 'lg'"
            >
                <div class="Pixso-symbol-5606_19148 fill-gray0-white-67_3285">
                    <div id="5606_19163" class="Pixso-frame-5606_19163">
                        <div class="frame-content-5606_19163">
                            <slot name="slot_5606_19143">
                                <p
                                    id="5606_19143"
                                    class="Pixso-paragraph-5606_19143 fill-gray60-83_2722-paragraph text-text-mdmedium-5454_21606 fill-gray30-35_1481-paragraph"
                                >
                                    {{ text_5606_42 ?? "Placeholder Text" }}
                                </p>
                            </slot>
                        </div>
                    </div>
                    <div id="5606_19161" class="stroke-wrapper-5606_19161">
                        <div class="Pixso-frame-5606_19161 fill-gray5-32_4120">
                            <div class="frame-content-5606_19161">
                                <slot name="slot_5606_19152">
                                    <p
                                        id="5606_19152"
                                        class="Pixso-paragraph-5606_19152 fill-gray60-83_2722-paragraph text-text-mdmedium-5454_21606 fill-gray30-35_1481-paragraph"
                                    >
                                        {{ "Copy" }}
                                    </p>
                                </slot>
                                <slot
                                    name="slot_5606_19157"
                                    v-if="visible_5606_41"
                                >
                                    <CopySimple
                                        id="5606_19157"
                                        class="Pixso-instance-5606_19157"
                                        Format="Outline"
                                        Weight="Bold"
                                    />
                                </slot>
                            </div>
                        </div>
                        <div
                            class="stroke-5606_19161 stroke-gray30-35_1481"
                        ></div>
                    </div>
                </div>
                <div class="stroke-5606_19148 stroke-gray30-35_1481"></div>
            </div>
            <div
                id="5976_52052"
                class="stroke-wrapper-5976_52052"
                v-if="Type === 'Action' && Size === 'md'"
            >
                <div class="Pixso-symbol-5976_52052 fill-gray0-white-67_3285">
                    <div id="5976_52053" class="Pixso-frame-5976_52053">
                        <div class="frame-content-5976_52053">
                            <slot name="slot_5976_52054">
                                <p
                                    id="5976_52054"
                                    class="Pixso-paragraph-5976_52054 fill-gray60-83_2722-paragraph text-text-mdmedium-5454_21606 fill-gray30-35_1481-paragraph"
                                >
                                    {{ text_5606_42 ?? "Placeholder Text" }}
                                </p>
                            </slot>
                        </div>
                    </div>
                    <div id="5976_52055" class="stroke-wrapper-5976_52055">
                        <div class="Pixso-frame-5976_52055 fill-gray5-32_4120">
                            <div class="frame-content-5976_52055">
                                <slot name="slot_5976_52056">
                                    <p
                                        id="5976_52056"
                                        class="Pixso-paragraph-5976_52056 fill-gray60-83_2722-paragraph text-text-mdmedium-5454_21606 fill-gray30-35_1481-paragraph"
                                    >
                                        {{ "Copy" }}
                                    </p>
                                </slot>
                                <slot
                                    name="slot_5976_52057"
                                    v-if="visible_5606_41"
                                >
                                    <CopySimple
                                        id="5976_52057"
                                        class="Pixso-instance-5976_52057"
                                        Format="Outline"
                                        Weight="Bold"
                                    />
                                </slot>
                            </div>
                        </div>
                        <div
                            class="stroke-5976_52055 stroke-gray30-35_1481"
                        ></div>
                    </div>
                </div>
                <div class="stroke-5976_52052 stroke-gray30-35_1481"></div>
            </div>
            <div
                id="5606_19172"
                class="stroke-wrapper-5606_19172"
                v-if="Type === 'Currency' && Size === 'lg'"
            >
                <div class="Pixso-symbol-5606_19172 fill-gray0-white-67_3285">
                    <div id="5607_19244" class="stroke-wrapper-5607_19244">
                        <div class="Pixso-frame-5607_19244 fill-gray5-32_4120">
                            <div class="frame-content-5607_19244">
                                <slot name="slot_5606_19174">
                                    <CurrencyDollarSimple
                                        id="5606_19174"
                                        class="Pixso-instance-5606_19174"
                                        Format="Outline"
                                        Weight="Bold"
                                    />
                                </slot>
                            </div>
                        </div>
                        <div
                            class="stroke-5607_19244 stroke-gray30-35_1481"
                        ></div>
                    </div>
                    <div id="5607_19390" class="Pixso-frame-5607_19390">
                        <div class="frame-content-5607_19390">
                            <slot name="slot_5606_19175">
                                <p
                                    id="5606_19175"
                                    class="Pixso-paragraph-5606_19175 fill-gray60-83_2722-paragraph text-text-mdmedium-5454_21606 fill-gray30-35_1481-paragraph"
                                >
                                    {{ text_5606_54 ?? "Amount Text" }}
                                </p>
                            </slot>
                        </div>
                    </div>
                    <div id="5606_19240" class="stroke-wrapper-5606_19240">
                        <div class="Pixso-frame-5606_19240 fill-gray5-32_4120">
                            <div class="frame-content-5606_19240">
                                <slot name="slot_5606_19193">
                                    <p
                                        id="5606_19193"
                                        class="Pixso-paragraph-5606_19193 fill-gray60-83_2722-paragraph text-text-mdmedium-5454_21606 fill-gray30-35_1481-paragraph"
                                    >
                                        {{ text_5607_66 ?? "USD" }}
                                    </p>
                                </slot>
                                <slot name="slot_5606_19176">
                                    <CaretDown
                                        id="5606_19176"
                                        class="Pixso-instance-5606_19176"
                                        Format="Outline"
                                        Weight="Bold"
                                    />
                                </slot>
                            </div>
                        </div>
                        <div
                            class="stroke-5606_19240 stroke-gray30-35_1481"
                        ></div>
                    </div>
                </div>
                <div class="stroke-5606_19172 stroke-gray30-35_1481"></div>
            </div>
            <div
                id="5976_52058"
                class="stroke-wrapper-5976_52058"
                v-if="Type === 'Currency' && Size === 'md'"
            >
                <div class="Pixso-symbol-5976_52058 fill-gray0-white-67_3285">
                    <div id="5976_52059" class="stroke-wrapper-5976_52059">
                        <div class="Pixso-frame-5976_52059 fill-gray5-32_4120">
                            <div class="frame-content-5976_52059">
                                <slot name="slot_5976_52060">
                                    <CurrencyDollarSimple
                                        id="5976_52060"
                                        class="Pixso-instance-5976_52060"
                                        Format="Outline"
                                        Weight="Bold"
                                    />
                                </slot>
                            </div>
                        </div>
                        <div
                            class="stroke-5976_52059 stroke-gray30-35_1481"
                        ></div>
                    </div>
                    <div id="5976_52061" class="Pixso-frame-5976_52061">
                        <div class="frame-content-5976_52061">
                            <slot name="slot_5976_52062">
                                <p
                                    id="5976_52062"
                                    class="Pixso-paragraph-5976_52062 fill-gray60-83_2722-paragraph text-text-mdmedium-5454_21606 fill-gray30-35_1481-paragraph"
                                >
                                    {{ text_5606_54 ?? "Amount Text" }}
                                </p>
                            </slot>
                        </div>
                    </div>
                    <div id="5976_52063" class="stroke-wrapper-5976_52063">
                        <div class="Pixso-frame-5976_52063 fill-gray5-32_4120">
                            <div class="frame-content-5976_52063">
                                <slot name="slot_5976_52064">
                                    <p
                                        id="5976_52064"
                                        class="Pixso-paragraph-5976_52064 fill-gray60-83_2722-paragraph text-text-mdmedium-5454_21606 fill-gray30-35_1481-paragraph"
                                    >
                                        {{ text_5607_66 ?? "USD" }}
                                    </p>
                                </slot>
                                <slot name="slot_5976_52065">
                                    <CaretDown
                                        id="5976_52065"
                                        class="Pixso-instance-5976_52065"
                                        Format="Outline"
                                        Weight="Bold"
                                    />
                                </slot>
                            </div>
                        </div>
                        <div
                            class="stroke-5976_52063 stroke-gray30-35_1481"
                        ></div>
                    </div>
                </div>
                <div class="stroke-5976_52058 stroke-gray30-35_1481"></div>
            </div>
            <div
                id="5607_19283"
                class="stroke-wrapper-5607_19283"
                v-if="Type === 'Credit Card' && Size === 'lg'"
            >
                <div class="Pixso-symbol-5607_19283 fill-gray0-white-67_3285">
                    <slot name="slot_5607_19286">
                        <p
                            id="5607_19286"
                            class="Pixso-paragraph-5607_19286 fill-gray60-83_2722-paragraph text-text-mdmedium-5454_21606 fill-gray30-35_1481-paragraph"
                        >
                            {{ text_5607_70 ?? "0000 0000 0000 0000" }}
                        </p>
                    </slot>
                    <div id="5607_19315" class="Pixso-frame-5607_19315">
                        <slot name="slot_5607_19306">
                            <PaymentLogo
                                id="5607_19306"
                                class="Pixso-instance-5607_19306"
                                Size="sm"
                                Company="Visa"
                            />
                        </slot>
                        <slot name="slot_5607_19313" v-if="visible_5606_41">
                            <Question
                                id="5607_19313"
                                class="Pixso-instance-5607_19313"
                                Format="Outline"
                                Weight="Bold"
                            />
                        </slot>
                    </div>
                </div>
                <div class="stroke-5607_19283 stroke-gray30-35_1481"></div>
            </div>
            <div
                id="5976_52066"
                class="stroke-wrapper-5976_52066"
                v-if="Type === 'Credit Card' && Size === 'md'"
            >
                <div class="Pixso-symbol-5976_52066 fill-gray0-white-67_3285">
                    <slot name="slot_5976_52067">
                        <p
                            id="5976_52067"
                            class="Pixso-paragraph-5976_52067 fill-gray60-83_2722-paragraph text-text-mdmedium-5454_21606 fill-gray30-35_1481-paragraph"
                        >
                            {{ text_5607_70 ?? "0000 0000 0000 0000" }}
                        </p>
                    </slot>
                    <div id="5976_52068" class="Pixso-frame-5976_52068">
                        <slot name="slot_5976_52069">
                            <PaymentLogo
                                id="5976_52069"
                                class="Pixso-instance-5976_52069"
                                Size="sm"
                                Company="Visa"
                            />
                        </slot>
                        <slot name="slot_5976_52070" v-if="visible_5606_41">
                            <Question
                                id="5976_52070"
                                class="Pixso-instance-5976_52070"
                                Format="Outline"
                                Weight="Bold"
                            />
                        </slot>
                    </div>
                </div>
                <div class="stroke-5976_52066 stroke-gray30-35_1481"></div>
            </div>
            <div
                id="5607_19353"
                class="stroke-wrapper-5607_19353"
                v-if="Type === 'Date' && Size === 'lg'"
            >
                <div class="Pixso-symbol-5607_19353 fill-gray0-white-67_3285">
                    <slot name="slot_5607_19354">
                        <p
                            id="5607_19354"
                            class="Pixso-paragraph-5607_19354 fill-gray60-83_2722-paragraph text-text-mdmedium-5454_21606 fill-gray30-35_1481-paragraph"
                        >
                            {{ text_5607_75 ?? "00 / 00 / 0000" }}
                        </p>
                    </slot>
                    <slot name="slot_5607_19365">
                        <CalendarBlank
                            id="5607_19365"
                            class="Pixso-instance-5607_19365"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div class="stroke-5607_19353 stroke-gray30-35_1481"></div>
            </div>
            <div
                id="5976_52071"
                class="stroke-wrapper-5976_52071"
                v-if="Type === 'Date' && Size === 'md'"
            >
                <div class="Pixso-symbol-5976_52071 fill-gray0-white-67_3285">
                    <slot name="slot_5976_52072">
                        <p
                            id="5976_52072"
                            class="Pixso-paragraph-5976_52072 fill-gray60-83_2722-paragraph text-text-mdmedium-5454_21606 fill-gray30-35_1481-paragraph"
                        >
                            {{ text_5607_75 ?? "00 / 00 / 0000" }}
                        </p>
                    </slot>
                    <slot name="slot_5976_52073">
                        <CalendarBlank
                            id="5976_52073"
                            class="Pixso-instance-5976_52073"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div class="stroke-5976_52071 stroke-gray30-35_1481"></div>
            </div>
            <div
                id="5607_19379"
                class="stroke-wrapper-5607_19379"
                v-if="Type === 'Link' && Size === 'lg'"
            >
                <div class="Pixso-symbol-5607_19379 fill-gray0-white-67_3285">
                    <div id="5607_19383" class="stroke-wrapper-5607_19383">
                        <div class="Pixso-frame-5607_19383 fill-gray5-32_4120">
                            <div class="frame-content-5607_19383">
                                <slot name="slot_5607_19384">
                                    <p
                                        id="5607_19384"
                                        class="Pixso-paragraph-5607_19384 fill-gray60-83_2722-paragraph text-text-mdmedium-5454_21606 fill-gray30-35_1481-paragraph"
                                    >
                                        {{ "https://" }}
                                    </p>
                                </slot>
                            </div>
                        </div>
                        <div
                            class="stroke-5607_19383 stroke-gray30-35_1481"
                        ></div>
                    </div>
                    <div id="5607_19389" class="stroke-wrapper-5607_19389">
                        <div class="Pixso-frame-5607_19389">
                            <div class="frame-content-5607_19389">
                                <slot name="slot_5607_19380">
                                    <p
                                        id="5607_19380"
                                        class="Pixso-paragraph-5607_19380 fill-gray60-83_2722-paragraph text-text-mdmedium-5454_21606 fill-gray30-35_1481-paragraph"
                                    >
                                        {{ text_5607_81 ?? "Link Text" }}
                                    </p>
                                </slot>
                                <slot
                                    name="slot_5607_19387"
                                    v-if="visible_5606_41"
                                >
                                    <Question
                                        id="5607_19387"
                                        class="Pixso-instance-5607_19387"
                                        Format="Outline"
                                        Weight="Bold"
                                    />
                                </slot>
                            </div>
                        </div>
                        <div
                            class="stroke-5607_19389 stroke-gray30-35_1481"
                        ></div>
                    </div>
                </div>
                <div class="stroke-5607_19379 stroke-gray30-35_1481"></div>
            </div>
            <div
                id="5976_52074"
                class="stroke-wrapper-5976_52074"
                v-if="Type === 'Link' && Size === 'md'"
            >
                <div class="Pixso-symbol-5976_52074 fill-gray0-white-67_3285">
                    <div id="5976_52075" class="stroke-wrapper-5976_52075">
                        <div class="Pixso-frame-5976_52075 fill-gray5-32_4120">
                            <div class="frame-content-5976_52075">
                                <slot name="slot_5976_52076">
                                    <p
                                        id="5976_52076"
                                        class="Pixso-paragraph-5976_52076 fill-gray60-83_2722-paragraph text-text-mdmedium-5454_21606 fill-gray30-35_1481-paragraph"
                                    >
                                        {{ "https://" }}
                                    </p>
                                </slot>
                            </div>
                        </div>
                        <div
                            class="stroke-5976_52075 stroke-gray30-35_1481"
                        ></div>
                    </div>
                    <div id="5976_52077" class="stroke-wrapper-5976_52077">
                        <div class="Pixso-frame-5976_52077">
                            <div class="frame-content-5976_52077">
                                <slot name="slot_5976_52078">
                                    <p
                                        id="5976_52078"
                                        class="Pixso-paragraph-5976_52078 fill-gray60-83_2722-paragraph text-text-mdmedium-5454_21606 fill-gray30-35_1481-paragraph"
                                    >
                                        {{ text_5607_81 ?? "Link Text" }}
                                    </p>
                                </slot>
                                <slot
                                    name="slot_5976_52079"
                                    v-if="visible_5606_41"
                                >
                                    <Question
                                        id="5976_52079"
                                        class="Pixso-instance-5976_52079"
                                        Format="Outline"
                                        Weight="Bold"
                                    />
                                </slot>
                            </div>
                        </div>
                        <div
                            class="stroke-5976_52077 stroke-gray30-35_1481"
                        ></div>
                    </div>
                </div>
                <div class="stroke-5976_52074 stroke-gray30-35_1481"></div>
            </div>
            <div
                id="5607_19415"
                class="stroke-wrapper-5607_19415"
                v-if="Type === 'Password' && Size === 'lg'"
            >
                <div class="Pixso-symbol-5607_19415 fill-gray0-white-67_3285">
                    <div id="5607_19416" class="Pixso-frame-5607_19416">
                        <div class="frame-content-5607_19416">
                            <slot name="slot_5607_19417" v-if="visible_5606_43">
                                <LockSimple
                                    id="5607_19417"
                                    class="Pixso-instance-5607_19417"
                                    Format="Outline"
                                    Weight="Bold"
                                />
                            </slot>
                            <slot name="slot_5607_19418">
                                <p
                                    id="5607_19418"
                                    class="Pixso-paragraph-5607_19418 fill-gray60-83_2722-paragraph text-text-mdmedium-5454_21606 fill-gray30-35_1481-paragraph"
                                >
                                    {{ text_5607_88 ?? "*****************" }}
                                </p>
                            </slot>
                        </div>
                    </div>
                    <slot name="slot_5607_19419" v-if="visible_5606_41">
                        <EyeSlash
                            id="5607_19419"
                            class="Pixso-instance-5607_19419"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div class="stroke-5607_19415 stroke-gray30-35_1481"></div>
            </div>
            <div
                id="5976_52080"
                class="stroke-wrapper-5976_52080"
                v-if="Type === 'Password' && Size === 'md'"
            >
                <div class="Pixso-symbol-5976_52080 fill-gray0-white-67_3285">
                    <div id="5976_52081" class="Pixso-frame-5976_52081">
                        <div class="frame-content-5976_52081">
                            <slot name="slot_5976_52082" v-if="visible_5606_43">
                                <LockSimple
                                    id="5976_52082"
                                    class="Pixso-instance-5976_52082"
                                    Format="Outline"
                                    Weight="Bold"
                                />
                            </slot>
                            <slot name="slot_5976_52083">
                                <p
                                    id="5976_52083"
                                    class="Pixso-paragraph-5976_52083 fill-gray60-83_2722-paragraph text-text-mdmedium-5454_21606 fill-gray30-35_1481-paragraph"
                                >
                                    {{ text_5607_88 ?? "*****************" }}
                                </p>
                            </slot>
                        </div>
                    </div>
                    <slot name="slot_5976_52084" v-if="visible_5606_41">
                        <EyeSlash
                            id="5976_52084"
                            class="Pixso-instance-5976_52084"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div class="stroke-5976_52080 stroke-gray30-35_1481"></div>
            </div>
            <div
                id="5607_19447"
                class="stroke-wrapper-5607_19447"
                v-if="Type === 'Phone Number/Country' && Size === 'lg'"
            >
                <div class="Pixso-symbol-5607_19447 fill-gray0-white-67_3285">
                    <div id="5607_19473" class="stroke-wrapper-5607_19473">
                        <div class="Pixso-frame-5607_19473 fill-gray5-32_4120">
                            <div class="frame-content-5607_19473">
                                <slot name="slot_5607_19455">
                                    <Flags
                                        id="5607_19455"
                                        class="Pixso-instance-5607_19455"
                                        Country="united kingdom"
                                    />
                                </slot>
                                <slot name="slot_5607_19449">
                                    <CaretDown
                                        id="5607_19449"
                                        class="Pixso-instance-5607_19449"
                                        Format="Outline"
                                        Weight="Bold"
                                    />
                                </slot>
                            </div>
                        </div>
                        <div
                            class="stroke-5607_19473 stroke-gray30-35_1481"
                        ></div>
                    </div>
                    <div id="5607_19474" class="Pixso-frame-5607_19474">
                        <div class="frame-content-5607_19474">
                            <slot name="slot_5607_19450" v-if="visible_5978_0">
                                <p
                                    id="5607_19450"
                                    class="Pixso-paragraph-5607_19450 fill-gray60-83_2722-paragraph text-text-mdbold-423_3205 fill-gray30-35_1481-paragraph"
                                >
                                    {{ text_5607_105 ?? "+44" }}
                                </p>
                            </slot>
                            <slot name="slot_5607_19477">
                                <p
                                    id="5607_19477"
                                    class="Pixso-paragraph-5607_19477 fill-gray60-83_2722-paragraph text-text-mdmedium-5454_21606 fill-gray30-35_1481-paragraph"
                                >
                                    {{ text_5607_96 ?? "(000) 000-0000" }}
                                </p>
                            </slot>
                            <slot name="slot_5607_19475" v-if="visible_5606_41">
                                <Question
                                    id="5607_19475"
                                    class="Pixso-instance-5607_19475"
                                    Format="Outline"
                                    Weight="Bold"
                                />
                            </slot>
                        </div>
                    </div>
                </div>
                <div class="stroke-5607_19447 stroke-gray30-35_1481"></div>
            </div>
            <div
                id="5976_52085"
                class="stroke-wrapper-5976_52085"
                v-if="Type === 'Phone Number/Country' && Size === 'md'"
            >
                <div class="Pixso-symbol-5976_52085 fill-gray0-white-67_3285">
                    <div id="5976_52086" class="stroke-wrapper-5976_52086">
                        <div class="Pixso-frame-5976_52086 fill-gray5-32_4120">
                            <div class="frame-content-5976_52086">
                                <slot name="slot_5976_52087">
                                    <Flags
                                        id="5976_52087"
                                        class="Pixso-instance-5976_52087"
                                        Country="united kingdom"
                                    />
                                </slot>
                                <slot name="slot_5976_52088">
                                    <CaretDown
                                        id="5976_52088"
                                        class="Pixso-instance-5976_52088"
                                        Format="Outline"
                                        Weight="Bold"
                                    />
                                </slot>
                            </div>
                        </div>
                        <div
                            class="stroke-5976_52086 stroke-gray30-35_1481"
                        ></div>
                    </div>
                    <div id="5976_52089" class="Pixso-frame-5976_52089">
                        <div class="frame-content-5976_52089">
                            <slot name="slot_5976_52090" v-if="visible_5978_0">
                                <p
                                    id="5976_52090"
                                    class="Pixso-paragraph-5976_52090 fill-gray60-83_2722-paragraph text-text-mdbold-423_3205 fill-gray30-35_1481-paragraph"
                                >
                                    {{ text_5607_105 ?? "+44" }}
                                </p>
                            </slot>
                            <slot name="slot_5976_52091">
                                <p
                                    id="5976_52091"
                                    class="Pixso-paragraph-5976_52091 fill-gray60-83_2722-paragraph text-text-mdmedium-5454_21606 fill-gray30-35_1481-paragraph"
                                >
                                    {{ text_5607_96 ?? "(000) 000-0000" }}
                                </p>
                            </slot>
                            <slot name="slot_5976_52092" v-if="visible_5606_41">
                                <Question
                                    id="5976_52092"
                                    class="Pixso-instance-5976_52092"
                                    Format="Outline"
                                    Weight="Bold"
                                />
                            </slot>
                        </div>
                    </div>
                </div>
                <div class="stroke-5976_52085 stroke-gray30-35_1481"></div>
            </div>
            <div
                id="5609_21323"
                class="stroke-wrapper-5609_21323"
                v-if="Type === 'Number' && Size === 'lg'"
            >
                <div class="Pixso-symbol-5609_21323 fill-gray0-white-67_3285">
                    <div id="5609_21324" class="Pixso-frame-5609_21324">
                        <div class="frame-content-5609_21324">
                            <slot name="slot_5609_21325" v-if="visible_5606_43">
                                <User
                                    id="5609_21325"
                                    class="Pixso-instance-5609_21325"
                                    Format="Outline"
                                    Weight="Bold"
                                />
                            </slot>
                            <slot name="slot_5609_21326">
                                <p
                                    id="5609_21326"
                                    class="Pixso-paragraph-5609_21326 fill-gray60-83_2722-paragraph text-text-mdmedium-5454_21606 fill-gray30-35_1481-paragraph"
                                >
                                    {{ text_5609_157 ?? "Number Text" }}
                                </p>
                            </slot>
                        </div>
                    </div>
                    <slot name="slot_5609_21330">
                        <CaretUpDown
                            id="5609_21330"
                            class="Pixso-instance-5609_21330"
                            Format="Outline"
                            Weight="Fill"
                        />
                    </slot>
                </div>
                <div class="stroke-5609_21323 stroke-gray30-35_1481"></div>
            </div>
            <div
                id="5976_52093"
                class="stroke-wrapper-5976_52093"
                v-if="Type === 'Number' && Size === 'md'"
            >
                <div class="Pixso-symbol-5976_52093 fill-gray0-white-67_3285">
                    <div id="5976_52094" class="Pixso-frame-5976_52094">
                        <div class="frame-content-5976_52094">
                            <slot name="slot_5976_52095" v-if="visible_5606_43">
                                <User
                                    id="5976_52095"
                                    class="Pixso-instance-5976_52095"
                                    Format="Outline"
                                    Weight="Bold"
                                />
                            </slot>
                            <slot name="slot_5976_52096">
                                <p
                                    id="5976_52096"
                                    class="Pixso-paragraph-5976_52096 fill-gray60-83_2722-paragraph text-text-mdmedium-5454_21606 fill-gray30-35_1481-paragraph"
                                >
                                    {{ text_5609_157 ?? "Number Text" }}
                                </p>
                            </slot>
                        </div>
                    </div>
                    <slot name="slot_5976_52097">
                        <CaretUpDown
                            id="5976_52097"
                            class="Pixso-instance-5976_52097"
                            Format="Outline"
                            Weight="Fill"
                        />
                    </slot>
                </div>
                <div class="stroke-5976_52093 stroke-gray30-35_1481"></div>
            </div>
        </div>
    </div>
</template>
<script lang="ts" setup>
import User from "@/components/User.vue";
import Question from "@/components/Question.vue";
import CopySimple from "@/components/Copysimple.vue";
import CurrencyDollarSimple from "@/components/Currencydollarsimple.vue";
import CaretDown from "@/components/Caretdown.vue";
import PaymentLogo from "@/components/Paymentlogo.vue";
import CalendarBlank from "@/components/Calendarblank.vue";
import LockSimple from "@/components/Locksimple.vue";
import EyeSlash from "@/components/Eyeslash.vue";
import Flags from "@/components/Flags.vue";
import CaretUpDown from "@/components/Caretupdown.vue";
const props = defineProps({
    instance_5606_40: { type: String, default: "Component_5579_152455" },
    visible_5606_41: { type: Boolean, default: true },
    text_5606_42: { type: String, default: "Placeholder Text" },
    visible_5606_43: { type: Boolean, default: true },
    instance_5606_44: { type: String, default: "Component_5579_153182" },
    text_5606_54: { type: String, default: "Amount Text" },
    instance_5607_58: { type: String, default: "Component_5579_152190" },
    text_5607_66: { type: String, default: "USD" },
    text_5607_70: { type: String, default: "0000 0000 0000 0000" },
    text_5607_75: { type: String, default: "00 / 00 / 0000" },
    text_5607_81: { type: String, default: "Link Text" },
    text_5607_88: { type: String, default: "*****************" },
    text_5607_96: { type: String, default: "(000) 000-0000" },
    text_5607_105: { type: String, default: "+44" },
    text_5609_157: { type: String, default: "Number Text" },
    visible_5978_0: { type: Boolean, default: true },
    Type: { type: String },
    Size: { type: String }
});
</script>
<style>
.Pixso-symbol-5606_19150 {
}
.Pixso-symbol-5606_19081 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 12px 12px 12px 12px;
    min-height: 48px;
    border-radius: 123px 123px 123px 123px;
}
.stroke-wrapper-5606_19081 {
    position: relative;
    width: 320px;
    height: auto;
    display: flex;
}
.stroke-5606_19081 {
    position: absolute;
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-frame-5606_19162 {
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
.frame-content-5606_19162 {
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
    width: 100%;
    position: relative;
}
.Pixso-instance-5606_19068 {
    width: 20px;
    height: 20px;
}
.Pixso-paragraph-5606_19069 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5606_19072 {
    width: 20px;
    height: 20px;
}
.Pixso-symbol-5976_52047 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 8px 12px 8px 12px;
    min-height: 40px;
    border-radius: 123px 123px 123px 123px;
}
.stroke-wrapper-5976_52047 {
    position: relative;
    width: 320px;
    height: auto;
    display: flex;
}
.stroke-5976_52047 {
    position: absolute;
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-frame-5976_52048 {
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
.frame-content-5976_52048 {
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
    width: 100%;
    position: relative;
}
.Pixso-instance-5976_52049 {
    width: 20px;
    height: 20px;
}
.Pixso-paragraph-5976_52050 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5976_52051 {
    width: 20px;
    height: 20px;
}
.Pixso-symbol-5606_19148 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    align-items: center;
    min-height: 48px;
    border-radius: 123px 123px 123px 123px;
}
.stroke-wrapper-5606_19148 {
    position: relative;
    width: 320px;
    height: auto;
    display: flex;
}
.stroke-5606_19148 {
    position: absolute;
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-frame-5606_19163 {
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
.frame-content-5606_19163 {
    display: flex;
    flex-direction: row;
    gap: 6px;
    align-items: center;
    padding: 12px 12px 12px 12px;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5606_19143 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-frame-5606_19161 {
    width: 100%;
    height: 100%;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    align-items: center;
}
.frame-content-5606_19161 {
    display: flex;
    flex-direction: row;
    gap: 6px;
    align-items: center;
    padding: 12px 12px 12px 12px;
    height: 100%;
    position: relative;
}
.stroke-wrapper-5606_19161 {
    position: relative;
    width: auto;
    height: 48px;
    display: flex;
    flex-shrink: 0;
}
.stroke-5606_19161 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 0px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-paragraph-5606_19152 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5606_19157 {
    width: 20px;
    height: 20px;
}
.Pixso-symbol-5976_52052 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    align-items: center;
    min-height: 40px;
    border-radius: 123px 123px 123px 123px;
}
.stroke-wrapper-5976_52052 {
    position: relative;
    width: 320px;
    height: auto;
    display: flex;
}
.stroke-5976_52052 {
    position: absolute;
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-frame-5976_52053 {
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
.frame-content-5976_52053 {
    display: flex;
    flex-direction: row;
    gap: 6px;
    align-items: center;
    padding: 8px 12px 8px 12px;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5976_52054 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-frame-5976_52055 {
    width: 100%;
    height: 100%;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    align-items: center;
}
.frame-content-5976_52055 {
    display: flex;
    flex-direction: row;
    gap: 6px;
    align-items: center;
    padding: 8px 12px 8px 12px;
    height: 100%;
    position: relative;
}
.stroke-wrapper-5976_52055 {
    position: relative;
    width: auto;
    height: 40px;
    display: flex;
    flex-shrink: 0;
}
.stroke-5976_52055 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 0px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-paragraph-5976_52056 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5976_52057 {
    width: 20px;
    height: 20px;
}
.Pixso-symbol-5606_19172 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    align-items: center;
    min-height: 48px;
    border-radius: 123px 123px 123px 123px;
}
.stroke-wrapper-5606_19172 {
    position: relative;
    width: 320px;
    height: auto;
    display: flex;
}
.stroke-5606_19172 {
    position: absolute;
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-frame-5607_19244 {
    width: 100%;
    height: 100%;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    align-items: center;
}
.frame-content-5607_19244 {
    display: flex;
    flex-direction: row;
    gap: 6px;
    align-items: center;
    padding: 12px 12px 12px 12px;
    height: 100%;
    position: relative;
}
.stroke-wrapper-5607_19244 {
    position: relative;
    width: auto;
    height: 48px;
    display: flex;
    flex-shrink: 0;
}
.stroke-5607_19244 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 1px 0px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5606_19174 {
    width: 20px;
    height: 20px;
}
.Pixso-frame-5607_19390 {
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
.frame-content-5607_19390 {
    display: flex;
    flex-direction: row;
    gap: 6px;
    align-items: center;
    padding: 12px 12px 12px 12px;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5606_19175 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-frame-5606_19240 {
    width: 100%;
    height: 100%;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    align-items: center;
}
.frame-content-5606_19240 {
    display: flex;
    flex-direction: row;
    gap: 6px;
    align-items: center;
    padding: 12px 12px 12px 12px;
    height: 100%;
    position: relative;
}
.stroke-wrapper-5606_19240 {
    position: relative;
    width: auto;
    height: 48px;
    display: flex;
    flex-shrink: 0;
}
.stroke-5606_19240 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 0px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-paragraph-5606_19193 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5606_19176 {
    width: 20px;
    height: 20px;
}
.Pixso-symbol-5976_52058 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    align-items: center;
    min-height: 40px;
    border-radius: 123px 123px 123px 123px;
}
.stroke-wrapper-5976_52058 {
    position: relative;
    width: 320px;
    height: auto;
    display: flex;
}
.stroke-5976_52058 {
    position: absolute;
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-frame-5976_52059 {
    width: 100%;
    height: 100%;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    align-items: center;
}
.frame-content-5976_52059 {
    display: flex;
    flex-direction: row;
    gap: 6px;
    align-items: center;
    padding: 8px 12px 8px 12px;
    height: 100%;
    position: relative;
}
.stroke-wrapper-5976_52059 {
    position: relative;
    width: auto;
    height: 40px;
    display: flex;
    flex-shrink: 0;
}
.stroke-5976_52059 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 1px 0px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5976_52060 {
    width: 20px;
    height: 20px;
}
.Pixso-frame-5976_52061 {
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
.frame-content-5976_52061 {
    display: flex;
    flex-direction: row;
    gap: 6px;
    align-items: center;
    padding: 8px 12px 8px 12px;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5976_52062 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-frame-5976_52063 {
    width: 100%;
    height: 100%;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    align-items: center;
}
.frame-content-5976_52063 {
    display: flex;
    flex-direction: row;
    gap: 6px;
    align-items: center;
    padding: 8px 12px 8px 12px;
    height: 100%;
    position: relative;
}
.stroke-wrapper-5976_52063 {
    position: relative;
    width: auto;
    height: 40px;
    display: flex;
    flex-shrink: 0;
}
.stroke-5976_52063 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 0px 0px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-paragraph-5976_52064 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5976_52065 {
    width: 20px;
    height: 20px;
}
.Pixso-symbol-5607_19283 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 10px 12px 10px 12px;
    min-height: 48px;
    border-radius: 123px 123px 123px 123px;
}
.stroke-wrapper-5607_19283 {
    position: relative;
    width: 320px;
    height: auto;
    display: flex;
}
.stroke-5607_19283 {
    position: absolute;
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-paragraph-5607_19286 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-frame-5607_19315 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
}
.Pixso-instance-5607_19306 {
    width: 36px;
    height: 24px;
}
.Pixso-instance-5607_19313 {
    width: 20px;
    height: 20px;
}
.Pixso-symbol-5976_52066 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 8px 12px 8px 12px;
    min-height: 40px;
    border-radius: 123px 123px 123px 123px;
}
.stroke-wrapper-5976_52066 {
    position: relative;
    width: 320px;
    height: auto;
    display: flex;
}
.stroke-5976_52066 {
    position: absolute;
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-paragraph-5976_52067 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-frame-5976_52068 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
}
.Pixso-instance-5976_52069 {
    width: 36px;
    height: 24px;
}
.Pixso-instance-5976_52070 {
    width: 20px;
    height: 20px;
}
.Pixso-symbol-5607_19353 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 10px 12px 10px 12px;
    min-height: 48px;
    border-radius: 123px 123px 123px 123px;
}
.stroke-wrapper-5607_19353 {
    position: relative;
    width: 320px;
    height: auto;
    display: flex;
}
.stroke-5607_19353 {
    position: absolute;
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-paragraph-5607_19354 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5607_19365 {
    width: 20px;
    height: 20px;
}
.Pixso-symbol-5976_52071 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 8px 12px 8px 12px;
    min-height: 40px;
    border-radius: 123px 123px 123px 123px;
}
.stroke-wrapper-5976_52071 {
    position: relative;
    width: 320px;
    height: auto;
    display: flex;
}
.stroke-5976_52071 {
    position: absolute;
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-paragraph-5976_52072 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5976_52073 {
    width: 20px;
    height: 20px;
}
.Pixso-symbol-5607_19379 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    align-items: center;
    min-height: 48px;
    border-radius: 123px 123px 123px 123px;
}
.stroke-wrapper-5607_19379 {
    position: relative;
    width: 320px;
    height: auto;
    display: flex;
}
.stroke-5607_19379 {
    position: absolute;
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-frame-5607_19383 {
    width: 100%;
    height: 100%;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    align-items: center;
}
.frame-content-5607_19383 {
    display: flex;
    flex-direction: row;
    gap: 6px;
    align-items: center;
    padding: 12px 12px 12px 12px;
    height: 100%;
    position: relative;
}
.stroke-wrapper-5607_19383 {
    position: relative;
    width: auto;
    height: 48px;
    display: flex;
    flex-shrink: 0;
}
.stroke-5607_19383 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 1px 0px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-paragraph-5607_19384 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-frame-5607_19389 {
    width: 100%;
    height: 100%;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: row;
    align-items: center;
    flex-grow: 1;
    flex-basis: 0;
}
.frame-content-5607_19389 {
    display: flex;
    flex-direction: row;
    gap: 6px;
    align-items: center;
    padding: 12px 12px 12px 12px;
    width: 100%;
    position: relative;
}
.stroke-wrapper-5607_19389 {
    position: relative;
    width: 100%;
    height: auto;
    display: flex;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.stroke-5607_19389 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 1px 0px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-paragraph-5607_19380 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5607_19387 {
    width: 20px;
    height: 20px;
}
.Pixso-symbol-5976_52074 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    align-items: center;
    min-height: 40px;
    border-radius: 123px 123px 123px 123px;
}
.stroke-wrapper-5976_52074 {
    position: relative;
    width: 320px;
    height: auto;
    display: flex;
}
.stroke-5976_52074 {
    position: absolute;
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-frame-5976_52075 {
    width: 100%;
    height: 100%;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    align-items: center;
}
.frame-content-5976_52075 {
    display: flex;
    flex-direction: row;
    gap: 6px;
    align-items: center;
    padding: 8px 12px 8px 12px;
    height: 100%;
    position: relative;
}
.stroke-wrapper-5976_52075 {
    position: relative;
    width: auto;
    height: 40px;
    display: flex;
    flex-shrink: 0;
}
.stroke-5976_52075 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 1px 0px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-paragraph-5976_52076 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-frame-5976_52077 {
    width: 100%;
    height: 100%;
    position: relative;
    flex-shrink: 1;
    display: flex;
    flex-direction: row;
    align-items: center;
    flex-grow: 1;
    flex-basis: 0;
}
.frame-content-5976_52077 {
    display: flex;
    flex-direction: row;
    gap: 6px;
    align-items: center;
    padding: 8px 12px 8px 12px;
    width: 100%;
    position: relative;
}
.stroke-wrapper-5976_52077 {
    position: relative;
    width: 100%;
    height: auto;
    display: flex;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.stroke-5976_52077 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 1px 0px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-paragraph-5976_52078 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5976_52079 {
    width: 20px;
    height: 20px;
}
.Pixso-symbol-5607_19415 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 12px 12px 12px 12px;
    min-height: 48px;
    border-radius: 123px 123px 123px 123px;
}
.stroke-wrapper-5607_19415 {
    position: relative;
    width: 320px;
    height: auto;
    display: flex;
}
.stroke-5607_19415 {
    position: absolute;
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-frame-5607_19416 {
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
.frame-content-5607_19416 {
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
    width: 100%;
    position: relative;
}
.Pixso-instance-5607_19417 {
    width: 20px;
    height: 20px;
}
.Pixso-paragraph-5607_19418 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5607_19419 {
    width: 20px;
    height: 20px;
}
.Pixso-symbol-5976_52080 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 8px 12px 8px 12px;
    min-height: 40px;
    border-radius: 123px 123px 123px 123px;
}
.stroke-wrapper-5976_52080 {
    position: relative;
    width: 320px;
    height: auto;
    display: flex;
}
.stroke-5976_52080 {
    position: absolute;
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-frame-5976_52081 {
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
.frame-content-5976_52081 {
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
    width: 100%;
    position: relative;
}
.Pixso-instance-5976_52082 {
    width: 20px;
    height: 20px;
}
.Pixso-paragraph-5976_52083 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5976_52084 {
    width: 20px;
    height: 20px;
}
.Pixso-symbol-5607_19447 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    align-items: center;
    min-height: 48px;
    border-radius: 123px 123px 123px 123px;
}
.stroke-wrapper-5607_19447 {
    position: relative;
    width: 320px;
    height: auto;
    display: flex;
}
.stroke-5607_19447 {
    position: absolute;
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-frame-5607_19473 {
    width: 100%;
    height: 100%;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    align-items: center;
}
.frame-content-5607_19473 {
    display: flex;
    flex-direction: row;
    gap: 6px;
    align-items: center;
    padding: 12px 12px 12px 12px;
    height: 100%;
    position: relative;
}
.stroke-wrapper-5607_19473 {
    position: relative;
    width: auto;
    height: 48px;
    display: flex;
    flex-shrink: 0;
}
.stroke-5607_19473 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 1px 0px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5607_19455 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5607_19449 {
    width: 20px;
    height: 20px;
}
.Pixso-frame-5607_19474 {
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
.frame-content-5607_19474 {
    display: flex;
    flex-direction: row;
    gap: 6px;
    align-items: center;
    padding: 12px 12px 12px 12px;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5607_19450 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-paragraph-5607_19477 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5607_19475 {
    width: 20px;
    height: 20px;
}
.Pixso-symbol-5976_52085 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    align-items: center;
    min-height: 40px;
    border-radius: 123px 123px 123px 123px;
}
.stroke-wrapper-5976_52085 {
    position: relative;
    width: 320px;
    height: auto;
    display: flex;
}
.stroke-5976_52085 {
    position: absolute;
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-frame-5976_52086 {
    width: 100%;
    height: 100%;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    align-items: center;
}
.frame-content-5976_52086 {
    display: flex;
    flex-direction: row;
    gap: 6px;
    align-items: center;
    padding: 8px 12px 8px 12px;
    height: 100%;
    position: relative;
}
.stroke-wrapper-5976_52086 {
    position: relative;
    width: auto;
    height: 40px;
    display: flex;
    flex-shrink: 0;
}
.stroke-5976_52086 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 0px 1px 0px 0px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5976_52087 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5976_52088 {
    width: 20px;
    height: 20px;
}
.Pixso-frame-5976_52089 {
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
.frame-content-5976_52089 {
    display: flex;
    flex-direction: row;
    gap: 6px;
    align-items: center;
    padding: 8px 12px 8px 12px;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-5976_52090 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-paragraph-5976_52091 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5976_52092 {
    width: 20px;
    height: 20px;
}
.Pixso-symbol-5609_21323 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 12px 12px 12px 12px;
    min-height: 48px;
    border-radius: 123px 123px 123px 123px;
}
.stroke-wrapper-5609_21323 {
    position: relative;
    width: 320px;
    height: auto;
    display: flex;
}
.stroke-5609_21323 {
    position: absolute;
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-frame-5609_21324 {
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
.frame-content-5609_21324 {
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
    width: 100%;
    position: relative;
}
.Pixso-instance-5609_21325 {
    width: 20px;
    height: 20px;
}
.Pixso-paragraph-5609_21326 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5609_21330 {
    width: 20px;
    height: 20px;
}
.Pixso-symbol-5976_52093 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
    padding: 8px 12px 8px 12px;
    min-height: 40px;
    border-radius: 123px 123px 123px 123px;
}
.stroke-wrapper-5976_52093 {
    position: relative;
    width: 320px;
    height: auto;
    display: flex;
}
.stroke-5976_52093 {
    position: absolute;
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-frame-5976_52094 {
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
.frame-content-5976_52094 {
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
    width: 100%;
    position: relative;
}
.Pixso-instance-5976_52095 {
    width: 20px;
    height: 20px;
}
.Pixso-paragraph-5976_52096 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5976_52097 {
    width: 20px;
    height: 20px;
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
.Pixso-instance-5607_19306 .Pixso-symbol-5566_5797 {
    width: 100%;
    height: 100%;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5607_19306 .stroke-wrapper-5566_5797 {
    width: 36px;
    height: 24px;
    flex-shrink: 0;
}
.Pixso-instance-5607_19306 .stroke-5566_5797 {
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5607_19306 .Pixso-vector-5566_5798 {
    width: 25.6494140625px;
    height: 8.4267578125px;
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translateX(calc(-50% + -0.175477968750001px))
        translateY(calc(-50% + 0.21337890625px));
}
.Pixso-instance-5607_19313 .Pixso-symbol-5579_153182 .Pixso-symbol-5578_150578 {
    width: 20px;
    height: 20px;
    position: absolute;
    left: 44px;
    top: 2px;
    background-color: transparent;
}
.Pixso-instance-5607_19313 .Pixso-vector-5579_153183 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5607_19313 .Pixso-symbol-5579_153182 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5976_52069 .Pixso-symbol-5566_5797 {
    width: 100%;
    height: 100%;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5976_52069 .stroke-wrapper-5566_5797 {
    width: 36px;
    height: 24px;
    flex-shrink: 0;
}
.Pixso-instance-5976_52069 .stroke-5566_5797 {
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5976_52069 .Pixso-vector-5566_5798 {
    width: 25.6494140625px;
    height: 8.4267578125px;
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translateX(calc(-50% + -0.175477968750001px))
        translateY(calc(-50% + 0.21337890625px));
}
.Pixso-instance-5976_52070 .Pixso-symbol-5579_153182 .Pixso-symbol-5578_150578 {
    width: 20px;
    height: 20px;
    position: absolute;
    left: 44px;
    top: 2px;
    background-color: transparent;
}
.Pixso-instance-5976_52070 .Pixso-vector-5579_153183 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5976_52070 .Pixso-symbol-5579_153182 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
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
.Pixso-instance-5607_19387 .Pixso-symbol-5579_153182 .Pixso-symbol-5578_150578 {
    width: 20px;
    height: 20px;
    position: absolute;
    left: 204px;
    top: 13px;
    background-color: transparent;
}
.Pixso-instance-5607_19387 .Pixso-vector-5579_153183 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5607_19387 .Pixso-symbol-5579_153182 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5976_52079 .Pixso-symbol-5579_153182 .Pixso-symbol-5578_150578 {
    width: 20px;
    height: 20px;
    position: absolute;
    left: 204px;
    top: 9px;
    background-color: transparent;
}
.Pixso-instance-5976_52079 .Pixso-vector-5579_153183 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5976_52079 .Pixso-symbol-5579_153182 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
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
.Pixso-instance-5607_19419 .Pixso-symbol-5578_149157 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5607_19419 .Pixso-vector-5578_149158 {
    width: 96.89%;
    height: 78.13%;
    position: absolute;
    left: 1.55%;
    right: 1.56%;
    top: 10.9%;
    bottom: 10.97%;
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
.Pixso-instance-5976_52084 .Pixso-symbol-5578_149157 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5976_52084 .Pixso-vector-5578_149158 {
    width: 96.89%;
    height: 78.13%;
    position: absolute;
    left: 1.55%;
    right: 1.56%;
    top: 10.9%;
    bottom: 10.97%;
}
.Pixso-instance-5607_19455 .Pixso-symbol-5461_35733 {
    width: 20px;
    height: 20px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5607_19455 .Pixso-vector-5461_35734 {
    width: 100%;
    height: 100%;
    position: absolute;
    left: 0%;
    right: 0%;
    top: 0%;
    bottom: 0%;
}
.Pixso-instance-5607_19455 .Pixso-group-5461_35735 {
    width: 96.56%;
    height: 96.56%;
    position: absolute;
    left: 1.72%;
    right: 1.72%;
    top: 1.72%;
    bottom: 1.72%;
}
.Pixso-instance-5607_19455 .Pixso-vector-5461_35736 {
    width: 26.94%;
    height: 18.02%;
    position: absolute;
    left: 0%;
    right: 73.06%;
    top: 18.47%;
    bottom: 63.51%;
}
.Pixso-instance-5607_19455 .Pixso-vector-5461_35737 {
    width: 26.94%;
    height: 18.02%;
    position: absolute;
    left: 73.06%;
    right: 0%;
    top: 18.47%;
    bottom: 63.51%;
}
.Pixso-instance-5607_19455 .Pixso-vector-5461_35738 {
    width: 26.94%;
    height: 18.02%;
    position: absolute;
    left: 0%;
    right: 73.06%;
    top: 63.51%;
    bottom: 18.47%;
}
.Pixso-instance-5607_19455 .Pixso-vector-5461_35739 {
    width: 18.02%;
    height: 26.94%;
    position: absolute;
    left: 63.51%;
    right: 18.47%;
    top: 0%;
    bottom: 73.06%;
}
.Pixso-instance-5607_19455 .Pixso-vector-5461_35740 {
    width: 18.02%;
    height: 26.94%;
    position: absolute;
    left: 18.47%;
    right: 63.51%;
    top: 73.06%;
    bottom: 0%;
}
.Pixso-instance-5607_19455 .Pixso-vector-5461_35741 {
    width: 18.02%;
    height: 26.94%;
    position: absolute;
    left: 18.47%;
    right: 63.51%;
    top: 0%;
    bottom: 73.06%;
}
.Pixso-instance-5607_19455 .Pixso-vector-5461_35742 {
    width: 18.02%;
    height: 26.94%;
    position: absolute;
    left: 63.51%;
    right: 18.47%;
    top: 73.06%;
    bottom: 0%;
}
.Pixso-instance-5607_19455 .Pixso-vector-5461_35743 {
    width: 26.94%;
    height: 18.02%;
    position: absolute;
    left: 73.06%;
    right: 0%;
    top: 63.51%;
    bottom: 18.47%;
}
.Pixso-instance-5607_19455 .Pixso-group-5461_35744 {
    width: 100%;
    height: 100%;
    position: absolute;
    left: 0%;
    right: 0%;
    top: 0%;
    bottom: 0%;
}
.Pixso-instance-5607_19455 .Pixso-vector-5461_35745 {
    width: 100%;
    height: 100%;
    position: absolute;
    left: 0%;
    right: 0%;
    top: 0%;
    bottom: 0%;
}
.Pixso-instance-5607_19455 .Pixso-vector-5461_35746 {
    width: 25.25%;
    height: 22.32%;
    position: absolute;
    left: 63.04%;
    right: 11.71%;
    top: 63.04%;
    bottom: 14.64%;
}
.Pixso-instance-5607_19455 .Pixso-vector-5461_35747 {
    width: 22.31%;
    height: 25.25%;
    position: absolute;
    left: 14.65%;
    right: 63.04%;
    top: 63.04%;
    bottom: 11.71%;
}
.Pixso-instance-5607_19455 .Pixso-vector-5461_35748 {
    width: 25.25%;
    height: 22.32%;
    position: absolute;
    left: 11.71%;
    right: 63.04%;
    top: 14.64%;
    bottom: 63.04%;
}
.Pixso-instance-5607_19455 .Pixso-vector-5461_35749 {
    width: 22.32%;
    height: 25.25%;
    position: absolute;
    left: 63.04%;
    right: 14.64%;
    top: 11.71%;
    bottom: 63.04%;
}
.Pixso-instance-5607_19449 .Pixso-symbol-5577_144008 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5607_19449 .Pixso-vector-5577_144009 {
    width: 71.9%;
    height: 40.64%;
    position: absolute;
    left: 14.05%;
    right: 14.05%;
    top: 32.8%;
    bottom: 26.56%;
}
.Pixso-instance-5607_19475 .Pixso-symbol-5579_153182 .Pixso-symbol-5578_150578 {
    width: 20px;
    height: 20px;
    position: absolute;
    left: 218px;
    top: 13px;
    background-color: transparent;
}
.Pixso-instance-5607_19475 .Pixso-vector-5579_153183 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5607_19475 .Pixso-symbol-5579_153182 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5976_52087 .Pixso-symbol-5461_35733 {
    width: 20px;
    height: 20px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5976_52087 .Pixso-vector-5461_35734 {
    width: 100%;
    height: 100%;
    position: absolute;
    left: 0%;
    right: 0%;
    top: 0%;
    bottom: 0%;
}
.Pixso-instance-5976_52087 .Pixso-group-5461_35735 {
    width: 96.56%;
    height: 96.56%;
    position: absolute;
    left: 1.72%;
    right: 1.72%;
    top: 1.72%;
    bottom: 1.72%;
}
.Pixso-instance-5976_52087 .Pixso-vector-5461_35736 {
    width: 26.94%;
    height: 18.02%;
    position: absolute;
    left: 0%;
    right: 73.06%;
    top: 18.47%;
    bottom: 63.51%;
}
.Pixso-instance-5976_52087 .Pixso-vector-5461_35737 {
    width: 26.94%;
    height: 18.02%;
    position: absolute;
    left: 73.06%;
    right: 0%;
    top: 18.47%;
    bottom: 63.51%;
}
.Pixso-instance-5976_52087 .Pixso-vector-5461_35738 {
    width: 26.94%;
    height: 18.02%;
    position: absolute;
    left: 0%;
    right: 73.06%;
    top: 63.51%;
    bottom: 18.47%;
}
.Pixso-instance-5976_52087 .Pixso-vector-5461_35739 {
    width: 18.02%;
    height: 26.94%;
    position: absolute;
    left: 63.51%;
    right: 18.47%;
    top: 0%;
    bottom: 73.06%;
}
.Pixso-instance-5976_52087 .Pixso-vector-5461_35740 {
    width: 18.02%;
    height: 26.94%;
    position: absolute;
    left: 18.47%;
    right: 63.51%;
    top: 73.06%;
    bottom: 0%;
}
.Pixso-instance-5976_52087 .Pixso-vector-5461_35741 {
    width: 18.02%;
    height: 26.94%;
    position: absolute;
    left: 18.47%;
    right: 63.51%;
    top: 0%;
    bottom: 73.06%;
}
.Pixso-instance-5976_52087 .Pixso-vector-5461_35742 {
    width: 18.02%;
    height: 26.94%;
    position: absolute;
    left: 63.51%;
    right: 18.47%;
    top: 73.06%;
    bottom: 0%;
}
.Pixso-instance-5976_52087 .Pixso-vector-5461_35743 {
    width: 26.94%;
    height: 18.02%;
    position: absolute;
    left: 73.06%;
    right: 0%;
    top: 63.51%;
    bottom: 18.47%;
}
.Pixso-instance-5976_52087 .Pixso-group-5461_35744 {
    width: 100%;
    height: 100%;
    position: absolute;
    left: 0%;
    right: 0%;
    top: 0%;
    bottom: 0%;
}
.Pixso-instance-5976_52087 .Pixso-vector-5461_35745 {
    width: 100%;
    height: 100%;
    position: absolute;
    left: 0%;
    right: 0%;
    top: 0%;
    bottom: 0%;
}
.Pixso-instance-5976_52087 .Pixso-vector-5461_35746 {
    width: 25.25%;
    height: 22.32%;
    position: absolute;
    left: 63.04%;
    right: 11.71%;
    top: 63.04%;
    bottom: 14.64%;
}
.Pixso-instance-5976_52087 .Pixso-vector-5461_35747 {
    width: 22.31%;
    height: 25.25%;
    position: absolute;
    left: 14.65%;
    right: 63.04%;
    top: 63.04%;
    bottom: 11.71%;
}
.Pixso-instance-5976_52087 .Pixso-vector-5461_35748 {
    width: 25.25%;
    height: 22.32%;
    position: absolute;
    left: 11.71%;
    right: 63.04%;
    top: 14.64%;
    bottom: 63.04%;
}
.Pixso-instance-5976_52087 .Pixso-vector-5461_35749 {
    width: 22.32%;
    height: 25.25%;
    position: absolute;
    left: 63.04%;
    right: 14.64%;
    top: 11.71%;
    bottom: 63.04%;
}
.Pixso-instance-5976_52088 .Pixso-symbol-5577_144008 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5976_52088 .Pixso-vector-5577_144009 {
    width: 71.9%;
    height: 40.64%;
    position: absolute;
    left: 14.05%;
    right: 14.05%;
    top: 32.8%;
    bottom: 26.56%;
}
.Pixso-instance-5976_52092 .Pixso-symbol-5579_153182 .Pixso-symbol-5578_150578 {
    width: 20px;
    height: 20px;
    position: absolute;
    left: 218px;
    top: 9px;
    background-color: transparent;
}
.Pixso-instance-5976_52092 .Pixso-vector-5579_153183 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5976_52092 .Pixso-symbol-5579_153182 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5609_21325 .Pixso-symbol-5579_152455 .Pixso-symbol-5578_150578 {
    width: 20px;
    height: 20px;
    position: absolute;
    left: 0px;
    top: 1px;
    background-color: transparent;
}
.Pixso-instance-5609_21325 .Pixso-vector-5579_152456 {
    width: 84.37%;
    height: 81.39%;
    position: absolute;
    left: 7.74%;
    right: 7.89%;
    top: 7.8%;
    bottom: 10.81%;
}
.Pixso-instance-5609_21325 .Pixso-symbol-5579_152455 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5609_21330 .Pixso-symbol-5577_144142 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5609_21330 .Pixso-vector-5577_144143 {
    width: 43.76%;
    height: 81.26%;
    position: absolute;
    left: 28.12%;
    right: 28.12%;
    top: 9.37%;
    bottom: 9.37%;
}
.Pixso-instance-5976_52095 .Pixso-symbol-5579_152455 .Pixso-symbol-5578_150578 {
    width: 20px;
    height: 20px;
    position: absolute;
    left: 0px;
    top: 1px;
    background-color: transparent;
}
.Pixso-instance-5976_52095 .Pixso-vector-5579_152456 {
    width: 84.37%;
    height: 81.39%;
    position: absolute;
    left: 7.74%;
    right: 7.89%;
    top: 7.8%;
    bottom: 10.81%;
}
.Pixso-instance-5976_52095 .Pixso-symbol-5579_152455 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5976_52097 .Pixso-symbol-5577_144142 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5976_52097 .Pixso-vector-5577_144143 {
    width: 43.76%;
    height: 81.26%;
    position: absolute;
    left: 28.12%;
    right: 28.12%;
    top: 9.37%;
    bottom: 9.37%;
}
</style>
