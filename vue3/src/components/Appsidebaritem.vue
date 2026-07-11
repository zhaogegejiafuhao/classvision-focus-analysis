<template>
    <div class="component-5982_54531">
        <div id="5982_54531" class="Pixso-symbol-5982_54531">
            <div
                id="5980_54125"
                class="Pixso-symbol-5980_54125 fill-gray0-white-67_3285"
                v-if="Theme === 'White' && State === 'Default'"
            >
                <div id="5980_54290" class="Pixso-frame-5980_54290">
                    <div class="frame-content-5980_54290">
                        <slot name="slot_5980_54108" v-if="visible_5982_36">
                            <Dot
                                id="5980_54108"
                                class="Pixso-instance-5980_54108"
                                Size="sm"
                            />
                        </slot>
                        <slot name="slot_5980_54116" v-if="visible_5982_38">
                            <HouseSimple
                                id="5980_54116"
                                class="Pixso-instance-5980_54116"
                                Format="Outline"
                                Weight="Bold"
                            />
                        </slot>
                        <slot name="slot_5979_34883">
                            <p
                                id="5979_34883"
                                class="Pixso-paragraph-5979_34883 fill-gray80-32_4123-paragraph text-text-mdbold-423_3205"
                            >
                                {{ text_5982_39 ?? "Menu Text" }}
                            </p>
                        </slot>
                    </div>
                </div>
                <slot name="slot_5979_34885" v-if="visible_5982_37">
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
                </slot>
                <slot name="slot_5979_34908" v-if="visible_5982_41">
                    <CaretDown
                        id="5979_34908"
                        class="Pixso-instance-5979_34908"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
            </div>
            <div
                id="6360_52180"
                class="Pixso-symbol-6360_52180 fill-gray5-32_4120"
                v-if="Theme === 'Light Gray' && State === 'Default'"
            >
                <div id="6360_52181" class="Pixso-frame-6360_52181">
                    <div class="frame-content-6360_52181">
                        <slot name="slot_6360_52182" v-if="visible_5982_36">
                            <Dot
                                id="6360_52182"
                                class="Pixso-instance-6360_52182"
                                Size="sm"
                            />
                        </slot>
                        <slot name="slot_6360_52183" v-if="visible_5982_38">
                            <HouseSimple
                                id="6360_52183"
                                class="Pixso-instance-6360_52183"
                                Format="Outline"
                                Weight="Bold"
                            />
                        </slot>
                        <slot name="slot_6360_52184">
                            <p
                                id="6360_52184"
                                class="Pixso-paragraph-6360_52184 fill-gray80-32_4123-paragraph text-text-mdbold-423_3205"
                            >
                                {{ text_5982_39 ?? "Menu Text" }}
                            </p>
                        </slot>
                    </div>
                </div>
                <slot name="slot_6360_52185" v-if="visible_5982_37">
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
                </slot>
                <slot name="slot_6360_52186" v-if="visible_5982_41">
                    <CaretDown
                        id="6360_52186"
                        class="Pixso-instance-6360_52186"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
            </div>
            <div
                id="5982_54523"
                class="Pixso-symbol-5982_54523 fill-gray5-32_4120"
                v-if="Theme === 'White' && State === 'Hover'"
            >
                <div id="5982_54491" class="Pixso-frame-5982_54491">
                    <div class="frame-content-5982_54491">
                        <slot name="slot_5982_54492" v-if="visible_5982_36">
                            <Dot
                                id="5982_54492"
                                class="Pixso-instance-5982_54492"
                                Size="sm"
                            />
                        </slot>
                        <slot name="slot_5982_54493" v-if="visible_5982_38">
                            <HouseSimple
                                id="5982_54493"
                                class="Pixso-instance-5982_54493"
                                Format="Outline"
                                Weight="Bold"
                            />
                        </slot>
                        <slot name="slot_5982_54494">
                            <p
                                id="5982_54494"
                                class="Pixso-paragraph-5982_54494 fill-gray80-32_4123-paragraph text-text-mdbold-423_3205"
                            >
                                {{ text_5982_39 ?? "Menu Text" }}
                            </p>
                        </slot>
                    </div>
                </div>
                <slot name="slot_5982_54495" v-if="visible_5982_37">
                    <BadgeText
                        id="5982_54495"
                        class="Pixso-instance-5982_54495"
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
                </slot>
                <slot name="slot_5982_54496" v-if="visible_5982_41">
                    <CaretDown
                        id="5982_54496"
                        class="Pixso-instance-5982_54496"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
            </div>
            <div
                id="6360_52187"
                class="Pixso-symbol-6360_52187 fill-gray0-white-67_3285"
                v-if="Theme === 'Light Gray' && State === 'Hover'"
            >
                <div id="6360_52188" class="Pixso-frame-6360_52188">
                    <div class="frame-content-6360_52188">
                        <slot name="slot_6360_52189" v-if="visible_5982_36">
                            <Dot
                                id="6360_52189"
                                class="Pixso-instance-6360_52189"
                                Size="sm"
                            />
                        </slot>
                        <slot name="slot_6360_52190" v-if="visible_5982_38">
                            <HouseSimple
                                id="6360_52190"
                                class="Pixso-instance-6360_52190"
                                Format="Outline"
                                Weight="Bold"
                            />
                        </slot>
                        <slot name="slot_6360_52191">
                            <p
                                id="6360_52191"
                                class="Pixso-paragraph-6360_52191 fill-gray80-32_4123-paragraph text-text-mdbold-423_3205"
                            >
                                {{ text_5982_39 ?? "Menu Text" }}
                            </p>
                        </slot>
                    </div>
                </div>
                <slot name="slot_6360_52192" v-if="visible_5982_37">
                    <BadgeText
                        id="6360_52192"
                        class="Pixso-instance-6360_52192"
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
                </slot>
                <slot name="slot_6360_52193" v-if="visible_5982_41">
                    <CaretDown
                        id="6360_52193"
                        class="Pixso-instance-6360_52193"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
            </div>
            <div
                id="5982_54524"
                class="Pixso-symbol-5982_54524 fill-gray0-white-67_3285 effect-focusring-gray-1273_16760"
                v-if="Theme === 'White' && State === 'Focused'"
            >
                <div id="5982_54509" class="Pixso-frame-5982_54509">
                    <div class="frame-content-5982_54509">
                        <slot name="slot_5982_54510" v-if="visible_5982_36">
                            <Dot
                                id="5982_54510"
                                class="Pixso-instance-5982_54510"
                                Size="sm"
                            />
                        </slot>
                        <slot name="slot_5982_54511" v-if="visible_5982_38">
                            <HouseSimple
                                id="5982_54511"
                                class="Pixso-instance-5982_54511"
                                Format="Outline"
                                Weight="Bold"
                            />
                        </slot>
                        <slot name="slot_5982_54512">
                            <p
                                id="5982_54512"
                                class="Pixso-paragraph-5982_54512 fill-gray80-32_4123-paragraph text-text-mdbold-423_3205"
                            >
                                {{ text_5982_39 ?? "Menu Text" }}
                            </p>
                        </slot>
                    </div>
                </div>
                <slot name="slot_5982_54513" v-if="visible_5982_37">
                    <BadgeText
                        id="5982_54513"
                        class="Pixso-instance-5982_54513"
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
                </slot>
                <slot name="slot_5982_54514" v-if="visible_5982_41">
                    <CaretDown
                        id="5982_54514"
                        class="Pixso-instance-5982_54514"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
            </div>
            <div
                id="6360_52194"
                class="Pixso-symbol-6360_52194 fill-gray5-32_4120 effect-focusring-gray-1273_16760"
                v-if="Theme === 'Light Gray' && State === 'Focused'"
            >
                <div id="6360_52195" class="Pixso-frame-6360_52195">
                    <div class="frame-content-6360_52195">
                        <slot name="slot_6360_52196" v-if="visible_5982_36">
                            <Dot
                                id="6360_52196"
                                class="Pixso-instance-6360_52196"
                                Size="sm"
                            />
                        </slot>
                        <slot name="slot_6360_52197" v-if="visible_5982_38">
                            <HouseSimple
                                id="6360_52197"
                                class="Pixso-instance-6360_52197"
                                Format="Outline"
                                Weight="Bold"
                            />
                        </slot>
                        <slot name="slot_6360_52198">
                            <p
                                id="6360_52198"
                                class="Pixso-paragraph-6360_52198 fill-gray80-32_4123-paragraph text-text-mdbold-423_3205"
                            >
                                {{ text_5982_39 ?? "Menu Text" }}
                            </p>
                        </slot>
                    </div>
                </div>
                <slot name="slot_6360_52199" v-if="visible_5982_37">
                    <BadgeText
                        id="6360_52199"
                        class="Pixso-instance-6360_52199"
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
                </slot>
                <slot name="slot_6360_52200" v-if="visible_5982_41">
                    <CaretDown
                        id="6360_52200"
                        class="Pixso-instance-6360_52200"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
            </div>
            <div
                id="5982_54577"
                class="Pixso-symbol-5982_54577 fill-brand60-1257_33467"
                v-if="Theme === 'Brand' && State === 'Default'"
            >
                <div id="5982_54578" class="Pixso-frame-5982_54578">
                    <div class="frame-content-5982_54578">
                        <slot name="slot_5982_54579" v-if="visible_5982_36">
                            <Dot
                                id="5982_54579"
                                class="Pixso-instance-5982_54579"
                                Size="sm"
                            />
                        </slot>
                        <slot name="slot_5982_54580" v-if="visible_5982_38">
                            <HouseSimple
                                id="5982_54580"
                                class="Pixso-instance-5982_54580"
                                Format="Outline"
                                Weight="Bold"
                            />
                        </slot>
                        <slot name="slot_5982_54581">
                            <p
                                id="5982_54581"
                                class="Pixso-paragraph-5982_54581 fill-gray0-white-67_3285-paragraph text-text-mdbold-423_3205"
                            >
                                {{ text_5982_39 ?? "Menu Text" }}
                            </p>
                        </slot>
                    </div>
                </div>
                <slot name="slot_5982_54582" v-if="visible_5982_37">
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
                                class="Pixso-paragraph-5588_11527 fill-gray0-white-67_3285-paragraph text-text-smsemibold-423_3209 fill-gray80-32_4123-paragraph"
                            >
                                {{ "10" }}
                            </p>
                        </template>
                    </BadgeText>
                </slot>
                <slot name="slot_5982_54583" v-if="visible_5982_41">
                    <CaretDown
                        id="5982_54583"
                        class="Pixso-instance-5982_54583"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
            </div>
            <div
                id="6360_52667"
                class="Pixso-symbol-6360_52667 fill-gray80-32_4123"
                v-if="Theme === 'Dark' && State === 'Default'"
            >
                <div id="6360_52668" class="Pixso-frame-6360_52668">
                    <div class="frame-content-6360_52668">
                        <slot name="slot_6360_52669" v-if="visible_5982_36">
                            <Dot
                                id="6360_52669"
                                class="Pixso-instance-6360_52669"
                                Size="sm"
                            />
                        </slot>
                        <slot name="slot_6360_52670" v-if="visible_5982_38">
                            <HouseSimple
                                id="6360_52670"
                                class="Pixso-instance-6360_52670"
                                Format="Outline"
                                Weight="Bold"
                            />
                        </slot>
                        <slot name="slot_6360_52671">
                            <p
                                id="6360_52671"
                                class="Pixso-paragraph-6360_52671 fill-gray0-white-67_3285-paragraph text-text-mdbold-423_3205"
                            >
                                {{ text_5982_39 ?? "Menu Text" }}
                            </p>
                        </slot>
                    </div>
                </div>
                <slot name="slot_6360_52672" v-if="visible_5982_37">
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
                </slot>
                <slot name="slot_6360_52673" v-if="visible_5982_41">
                    <CaretDown
                        id="6360_52673"
                        class="Pixso-instance-6360_52673"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
            </div>
            <div
                id="5982_54591"
                class="Pixso-symbol-5982_54591 fill-brand50-1257_33466"
                v-if="Theme === 'Brand' && State === 'Hover'"
            >
                <div id="5982_54592" class="Pixso-frame-5982_54592">
                    <div class="frame-content-5982_54592">
                        <slot name="slot_5982_54593" v-if="visible_5982_36">
                            <Dot
                                id="5982_54593"
                                class="Pixso-instance-5982_54593"
                                Size="sm"
                            />
                        </slot>
                        <slot name="slot_5982_54594" v-if="visible_5982_38">
                            <HouseSimple
                                id="5982_54594"
                                class="Pixso-instance-5982_54594"
                                Format="Outline"
                                Weight="Bold"
                            />
                        </slot>
                        <slot name="slot_5982_54595">
                            <p
                                id="5982_54595"
                                class="Pixso-paragraph-5982_54595 fill-gray0-white-67_3285-paragraph text-text-mdbold-423_3205"
                            >
                                {{ text_5982_39 ?? "Menu Text" }}
                            </p>
                        </slot>
                    </div>
                </div>
                <slot name="slot_5982_54596" v-if="visible_5982_37">
                    <BadgeText
                        id="5982_54596"
                        class="Pixso-instance-5982_54596"
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
                </slot>
                <slot name="slot_5982_54597" v-if="visible_5982_41">
                    <CaretDown
                        id="5982_54597"
                        class="Pixso-instance-5982_54597"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
            </div>
            <div
                id="6360_52674"
                class="Pixso-symbol-6360_52674 fill-gray70-32_4121"
                v-if="Theme === 'Dark' && State === 'Hover'"
            >
                <div id="6360_52675" class="Pixso-frame-6360_52675">
                    <div class="frame-content-6360_52675">
                        <slot name="slot_6360_52676" v-if="visible_5982_36">
                            <Dot
                                id="6360_52676"
                                class="Pixso-instance-6360_52676"
                                Size="sm"
                            />
                        </slot>
                        <slot name="slot_6360_52677" v-if="visible_5982_38">
                            <HouseSimple
                                id="6360_52677"
                                class="Pixso-instance-6360_52677"
                                Format="Outline"
                                Weight="Bold"
                            />
                        </slot>
                        <slot name="slot_6360_52678">
                            <p
                                id="6360_52678"
                                class="Pixso-paragraph-6360_52678 fill-gray0-white-67_3285-paragraph text-text-mdbold-423_3205"
                            >
                                {{ text_5982_39 ?? "Menu Text" }}
                            </p>
                        </slot>
                    </div>
                </div>
                <slot name="slot_6360_52679" v-if="visible_5982_37">
                    <BadgeText
                        id="6360_52679"
                        class="Pixso-instance-6360_52679"
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
                </slot>
                <slot name="slot_6360_52680" v-if="visible_5982_41">
                    <CaretDown
                        id="6360_52680"
                        class="Pixso-instance-6360_52680"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
            </div>
            <div
                id="5982_54584"
                class="Pixso-symbol-5982_54584 fill-brand60-1257_33467 effect-focusring-brand-5459_24463"
                v-if="Theme === 'Brand' && State === 'Focused'"
            >
                <div id="5982_54585" class="Pixso-frame-5982_54585">
                    <div class="frame-content-5982_54585">
                        <slot name="slot_5982_54586" v-if="visible_5982_36">
                            <Dot
                                id="5982_54586"
                                class="Pixso-instance-5982_54586"
                                Size="sm"
                            />
                        </slot>
                        <slot name="slot_5982_54587" v-if="visible_5982_38">
                            <HouseSimple
                                id="5982_54587"
                                class="Pixso-instance-5982_54587"
                                Format="Outline"
                                Weight="Bold"
                            />
                        </slot>
                        <slot name="slot_5982_54588">
                            <p
                                id="5982_54588"
                                class="Pixso-paragraph-5982_54588 fill-gray0-white-67_3285-paragraph text-text-mdbold-423_3205"
                            >
                                {{ text_5982_39 ?? "Menu Text" }}
                            </p>
                        </slot>
                    </div>
                </div>
                <slot name="slot_5982_54589" v-if="visible_5982_37">
                    <BadgeText
                        id="5982_54589"
                        class="Pixso-instance-5982_54589"
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
                </slot>
                <slot name="slot_5982_54590" v-if="visible_5982_41">
                    <CaretDown
                        id="5982_54590"
                        class="Pixso-instance-5982_54590"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
            </div>
            <div
                id="6360_52681"
                class="Pixso-symbol-6360_52681 fill-gray80-32_4123 effect-focusring-gray-1273_16760"
                v-if="Theme === 'Dark' && State === 'Focused'"
            >
                <div id="6360_52682" class="Pixso-frame-6360_52682">
                    <div class="frame-content-6360_52682">
                        <slot name="slot_6360_52683" v-if="visible_5982_36">
                            <Dot
                                id="6360_52683"
                                class="Pixso-instance-6360_52683"
                                Size="sm"
                            />
                        </slot>
                        <slot name="slot_6360_52684" v-if="visible_5982_38">
                            <HouseSimple
                                id="6360_52684"
                                class="Pixso-instance-6360_52684"
                                Format="Outline"
                                Weight="Bold"
                            />
                        </slot>
                        <slot name="slot_6360_52685">
                            <p
                                id="6360_52685"
                                class="Pixso-paragraph-6360_52685 fill-gray0-white-67_3285-paragraph text-text-mdbold-423_3205"
                            >
                                {{ text_5982_39 ?? "Menu Text" }}
                            </p>
                        </slot>
                    </div>
                </div>
                <slot name="slot_6360_52686" v-if="visible_5982_37">
                    <BadgeText
                        id="6360_52686"
                        class="Pixso-instance-6360_52686"
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
                </slot>
                <slot name="slot_6360_52687" v-if="visible_5982_41">
                    <CaretDown
                        id="6360_52687"
                        class="Pixso-instance-6360_52687"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
            </div>
        </div>
    </div>
</template>
<script lang="ts" setup>
import Dot from "@/components/Dot.vue";
import HouseSimple from "@/components/Housesimple.vue";
import BadgeText from "@/components/Badgetext.vue";
import CaretDown from "@/components/Caretdown.vue";
const props = defineProps({
    visible_5982_36: { type: Boolean, default: false },
    visible_5982_37: { type: Boolean, default: true },
    visible_5982_38: { type: Boolean, default: true },
    text_5982_39: { type: String, default: "Menu Text" },
    instance_5982_40: { type: String, default: "Component_5577_144008" },
    visible_5982_41: { type: Boolean, default: true },
    instance_5982_42: { type: String, default: "Component_6041_60589" },
    Theme: { type: String },
    State: { type: String }
});
</script>
<style>
.Pixso-symbol-5982_54531 {
}
.Pixso-symbol-5980_54125 {
    width: 320px;
    height: auto;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
    padding: 10px 12px 10px 12px;
    min-height: 48px;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-frame-5980_54290 {
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
.frame-content-5980_54290 {
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
    width: 100%;
    position: relative;
}
.Pixso-instance-5980_54108 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5980_54116 {
    width: 24px;
    height: 24px;
}
.Pixso-paragraph-5979_34883 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
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
.Pixso-instance-5979_34908 {
    width: 24px;
    height: 24px;
}
.Pixso-symbol-6360_52180 {
    width: 320px;
    height: auto;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
    padding: 10px 12px 10px 12px;
    min-height: 48px;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-frame-6360_52181 {
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
.frame-content-6360_52181 {
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
    width: 100%;
    position: relative;
}
.Pixso-instance-6360_52182 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-6360_52183 {
    width: 24px;
    height: 24px;
}
.Pixso-paragraph-6360_52184 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-6360_52185 {
    width: 36px;
    height: 28px;
}
.Pixso-instance-6360_52186 {
    width: 24px;
    height: 24px;
}
.Pixso-symbol-5982_54523 {
    width: 320px;
    height: auto;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
    padding: 10px 12px 10px 12px;
    min-height: 48px;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-frame-5982_54491 {
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
.frame-content-5982_54491 {
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
    width: 100%;
    position: relative;
}
.Pixso-instance-5982_54492 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5982_54493 {
    width: 24px;
    height: 24px;
}
.Pixso-paragraph-5982_54494 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5982_54495 {
    width: 36px;
    height: 28px;
}
.Pixso-instance-5982_54496 {
    width: 24px;
    height: 24px;
}
.Pixso-symbol-6360_52187 {
    width: 320px;
    height: auto;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
    padding: 10px 12px 10px 12px;
    min-height: 48px;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-frame-6360_52188 {
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
.frame-content-6360_52188 {
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
    width: 100%;
    position: relative;
}
.Pixso-instance-6360_52189 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-6360_52190 {
    width: 24px;
    height: 24px;
}
.Pixso-paragraph-6360_52191 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-6360_52192 {
    width: 36px;
    height: 28px;
}
.Pixso-instance-6360_52193 {
    width: 24px;
    height: 24px;
}
.Pixso-symbol-5982_54524 {
    width: 320px;
    height: auto;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
    padding: 10px 12px 10px 12px;
    min-height: 48px;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-frame-5982_54509 {
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
.frame-content-5982_54509 {
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
    width: 100%;
    position: relative;
}
.Pixso-instance-5982_54510 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5982_54511 {
    width: 24px;
    height: 24px;
}
.Pixso-paragraph-5982_54512 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5982_54513 {
    width: 36px;
    height: 28px;
}
.Pixso-instance-5982_54514 {
    width: 24px;
    height: 24px;
}
.Pixso-symbol-6360_52194 {
    width: 320px;
    height: auto;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
    padding: 10px 12px 10px 12px;
    min-height: 48px;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-frame-6360_52195 {
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
.frame-content-6360_52195 {
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
    width: 100%;
    position: relative;
}
.Pixso-instance-6360_52196 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-6360_52197 {
    width: 24px;
    height: 24px;
}
.Pixso-paragraph-6360_52198 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-6360_52199 {
    width: 36px;
    height: 28px;
}
.Pixso-instance-6360_52200 {
    width: 24px;
    height: 24px;
}
.Pixso-symbol-5982_54577 {
    width: 320px;
    height: auto;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
    padding: 10px 12px 10px 12px;
    min-height: 48px;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-frame-5982_54578 {
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
.frame-content-5982_54578 {
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
    width: 100%;
    position: relative;
}
.Pixso-instance-5982_54579 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5982_54580 {
    width: 24px;
    height: 24px;
}
.Pixso-paragraph-5982_54581 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5982_54582 {
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
.Pixso-instance-5982_54583 {
    width: 24px;
    height: 24px;
}
.Pixso-symbol-6360_52667 {
    width: 320px;
    height: auto;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
    padding: 10px 12px 10px 12px;
    min-height: 48px;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-frame-6360_52668 {
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
.frame-content-6360_52668 {
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
    width: 100%;
    position: relative;
}
.Pixso-instance-6360_52669 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-6360_52670 {
    width: 24px;
    height: 24px;
}
.Pixso-paragraph-6360_52671 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-6360_52672 {
    width: 36px;
    height: 28px;
}
.Pixso-instance-6360_52673 {
    width: 24px;
    height: 24px;
}
.Pixso-symbol-5982_54591 {
    width: 320px;
    height: auto;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
    padding: 10px 12px 10px 12px;
    min-height: 48px;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-frame-5982_54592 {
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
.frame-content-5982_54592 {
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
    width: 100%;
    position: relative;
}
.Pixso-instance-5982_54593 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5982_54594 {
    width: 24px;
    height: 24px;
}
.Pixso-paragraph-5982_54595 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5982_54596 {
    width: 36px;
    height: 28px;
}
.Pixso-instance-5982_54597 {
    width: 24px;
    height: 24px;
}
.Pixso-symbol-6360_52674 {
    width: 320px;
    height: auto;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
    padding: 10px 12px 10px 12px;
    min-height: 48px;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-frame-6360_52675 {
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
.frame-content-6360_52675 {
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
    width: 100%;
    position: relative;
}
.Pixso-instance-6360_52676 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-6360_52677 {
    width: 24px;
    height: 24px;
}
.Pixso-paragraph-6360_52678 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-6360_52679 {
    width: 36px;
    height: 28px;
}
.Pixso-instance-6360_52680 {
    width: 24px;
    height: 24px;
}
.Pixso-symbol-5982_54584 {
    width: 320px;
    height: auto;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
    padding: 10px 12px 10px 12px;
    min-height: 48px;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-frame-5982_54585 {
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
.frame-content-5982_54585 {
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
    width: 100%;
    position: relative;
}
.Pixso-instance-5982_54586 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5982_54587 {
    width: 24px;
    height: 24px;
}
.Pixso-paragraph-5982_54588 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-5982_54589 {
    width: 36px;
    height: 28px;
}
.Pixso-instance-5982_54590 {
    width: 24px;
    height: 24px;
}
.Pixso-symbol-6360_52681 {
    width: 320px;
    height: auto;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
    padding: 10px 12px 10px 12px;
    min-height: 48px;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-frame-6360_52682 {
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
.frame-content-6360_52682 {
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
    width: 100%;
    position: relative;
}
.Pixso-instance-6360_52683 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-6360_52684 {
    width: 24px;
    height: 24px;
}
.Pixso-paragraph-6360_52685 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 1;
    flex-grow: 1;
    flex-basis: 0;
}
.Pixso-instance-6360_52686 {
    width: 36px;
    height: 28px;
}
.Pixso-instance-6360_52687 {
    width: 24px;
    height: 24px;
}

.Pixso-instance-5980_54116 .Pixso-symbol-6041_60589 .Pixso-symbol-5578_149025 {
    width: 24px;
    height: 24px;
    position: absolute;
    left: 0px;
    top: 0px;
    background-color: transparent;
}
.Pixso-instance-5980_54116 .Pixso-symbol-6041_60589 .Pixso-symbol-5579_152493 {
    width: 24px;
    height: 24px;
    position: absolute;
    left: 0px;
    top: 0px;
    background-color: transparent;
}
.Pixso-instance-5980_54116 .Pixso-symbol-6041_60589 .Pixso-symbol-5578_150332 {
    width: 24px;
    height: 24px;
    position: absolute;
    left: 0px;
    top: 0px;
    background-color: transparent;
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
    width: 16px;
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
.Pixso-instance-5979_34908 .Pixso-symbol-5577_144008 {
    width: 24px;
    height: 24px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-6360_52183 .Pixso-symbol-6041_60589 .Pixso-symbol-5578_149025 {
    width: 24px;
    height: 24px;
    position: absolute;
    left: 0px;
    top: 0px;
    background-color: transparent;
}
.Pixso-instance-6360_52183 .Pixso-symbol-6041_60589 .Pixso-symbol-5579_152493 {
    width: 24px;
    height: 24px;
    position: absolute;
    left: 0px;
    top: 0px;
    background-color: transparent;
}
.Pixso-instance-6360_52183 .Pixso-symbol-6041_60589 .Pixso-symbol-5578_150332 {
    width: 24px;
    height: 24px;
    position: absolute;
    left: 0px;
    top: 0px;
    background-color: transparent;
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
    width: 16px;
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
.Pixso-instance-6360_52186 .Pixso-symbol-5577_144008 {
    width: 24px;
    height: 24px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5982_54495 .Pixso-symbol-5588_11352 {
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
.Pixso-instance-5982_54495 .stroke-wrapper-5588_11352 {
    width: 36px;
    height: 28px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5982_54495 .stroke-5588_11352 {
    inset: 0px;
    border-radius: 1234px 1234px 1234px 1234px;
    pointer-events: none;
    border-width: 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5982_54495 .Pixso-instance-5588_11353 {
    width: 16px;
    height: 16px;
}
.Pixso-instance-5982_54495 .Pixso-frame-5588_11354 {
    width: 16px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 5px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5982_54495 .Pixso-instance-5588_11355 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5982_54495 .Pixso-paragraph-5588_11356 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5982_54495 .Pixso-instance-5588_11357 {
    width: 16px;
    height: 16px;
}
.Pixso-instance-5982_54496 .Pixso-symbol-5577_144008 {
    width: 24px;
    height: 24px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-6360_52192 .Pixso-symbol-5588_11352 {
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
.Pixso-instance-6360_52192 .stroke-wrapper-5588_11352 {
    width: 36px;
    height: 28px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-6360_52192 .stroke-5588_11352 {
    inset: 0px;
    border-radius: 1234px 1234px 1234px 1234px;
    pointer-events: none;
    border-width: 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-6360_52192 .Pixso-instance-5588_11353 {
    width: 16px;
    height: 16px;
}
.Pixso-instance-6360_52192 .Pixso-frame-5588_11354 {
    width: 16px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 5px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-6360_52192 .Pixso-instance-5588_11355 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-6360_52192 .Pixso-paragraph-5588_11356 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-6360_52192 .Pixso-instance-5588_11357 {
    width: 16px;
    height: 16px;
}
.Pixso-instance-6360_52193 .Pixso-symbol-5577_144008 {
    width: 24px;
    height: 24px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5982_54513 .Pixso-symbol-5588_11352 {
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
.Pixso-instance-5982_54513 .stroke-wrapper-5588_11352 {
    width: 36px;
    height: 28px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5982_54513 .stroke-5588_11352 {
    inset: 0px;
    border-radius: 1234px 1234px 1234px 1234px;
    pointer-events: none;
    border-width: 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5982_54513 .Pixso-instance-5588_11353 {
    width: 16px;
    height: 16px;
}
.Pixso-instance-5982_54513 .Pixso-frame-5588_11354 {
    width: 16px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 5px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5982_54513 .Pixso-instance-5588_11355 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5982_54513 .Pixso-paragraph-5588_11356 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5982_54513 .Pixso-instance-5588_11357 {
    width: 16px;
    height: 16px;
}
.Pixso-instance-5982_54514 .Pixso-symbol-5577_144008 {
    width: 24px;
    height: 24px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-6360_52199 .Pixso-symbol-5588_11352 {
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
.Pixso-instance-6360_52199 .stroke-wrapper-5588_11352 {
    width: 36px;
    height: 28px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-6360_52199 .stroke-5588_11352 {
    inset: 0px;
    border-radius: 1234px 1234px 1234px 1234px;
    pointer-events: none;
    border-width: 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-6360_52199 .Pixso-instance-5588_11353 {
    width: 16px;
    height: 16px;
}
.Pixso-instance-6360_52199 .Pixso-frame-5588_11354 {
    width: 16px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 5px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-6360_52199 .Pixso-instance-5588_11355 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-6360_52199 .Pixso-paragraph-5588_11356 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-6360_52199 .Pixso-instance-5588_11357 {
    width: 16px;
    height: 16px;
}
.Pixso-instance-6360_52200 .Pixso-symbol-5577_144008 {
    width: 24px;
    height: 24px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5982_54580 .Pixso-symbol-6041_60589 .Pixso-symbol-5578_149025 {
    width: 24px;
    height: 24px;
    position: absolute;
    left: 0px;
    top: 0px;
    background-color: transparent;
}
.Pixso-instance-5982_54580 .Pixso-symbol-6041_60589 .Pixso-symbol-5579_152493 {
    width: 24px;
    height: 24px;
    position: absolute;
    left: 0px;
    top: 0px;
    background-color: transparent;
}
.Pixso-instance-5982_54580 .Pixso-symbol-6041_60589 .Pixso-symbol-5578_150332 {
    width: 24px;
    height: 24px;
    position: absolute;
    left: 0px;
    top: 0px;
    background-color: transparent;
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
    width: 16px;
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
.Pixso-instance-5982_54583 .Pixso-symbol-5577_144008 {
    width: 24px;
    height: 24px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5982_54583 .Pixso-vector-5577_144009 {
    width: 71.9%;
    height: 40.64%;
    position: absolute;
    left: 14.05%;
    right: 14.05%;
    top: 32.8%;
    bottom: 26.56%;
}
.Pixso-instance-6360_52670 .Pixso-symbol-6041_60589 .Pixso-symbol-5578_149025 {
    width: 24px;
    height: 24px;
    position: absolute;
    left: 0px;
    top: 0px;
    background-color: transparent;
}
.Pixso-instance-6360_52670 .Pixso-symbol-6041_60589 .Pixso-symbol-5579_152493 {
    width: 24px;
    height: 24px;
    position: absolute;
    left: 0px;
    top: 0px;
    background-color: transparent;
}
.Pixso-instance-6360_52670 .Pixso-symbol-6041_60589 .Pixso-symbol-5578_150332 {
    width: 24px;
    height: 24px;
    position: absolute;
    left: 0px;
    top: 0px;
    background-color: transparent;
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
    width: 16px;
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
.Pixso-instance-6360_52673 .Pixso-symbol-5577_144008 {
    width: 24px;
    height: 24px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-6360_52673 .Pixso-vector-5577_144009 {
    width: 71.9%;
    height: 40.64%;
    position: absolute;
    left: 14.05%;
    right: 14.05%;
    top: 32.8%;
    bottom: 26.56%;
}
.Pixso-instance-5982_54596 .Pixso-symbol-5588_11523 {
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
.Pixso-instance-5982_54596 .Pixso-instance-5588_11524 {
    width: 16px;
    height: 16px;
}
.Pixso-instance-5982_54596 .Pixso-frame-5588_11525 {
    width: 16px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 5px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5982_54596 .Pixso-instance-5588_11526 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5982_54596 .Pixso-paragraph-5588_11527 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5982_54596 .Pixso-instance-5588_11528 {
    width: 16px;
    height: 16px;
}
.Pixso-instance-5982_54597 .Pixso-symbol-5577_144008 {
    width: 24px;
    height: 24px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5982_54597 .Pixso-vector-5577_144009 {
    width: 71.9%;
    height: 40.64%;
    position: absolute;
    left: 14.05%;
    right: 14.05%;
    top: 32.8%;
    bottom: 26.56%;
}
.Pixso-instance-6360_52679 .Pixso-symbol-5588_11523 {
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
.Pixso-instance-6360_52679 .Pixso-instance-5588_11524 {
    width: 16px;
    height: 16px;
}
.Pixso-instance-6360_52679 .Pixso-frame-5588_11525 {
    width: 16px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 5px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-6360_52679 .Pixso-instance-5588_11526 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-6360_52679 .Pixso-paragraph-5588_11527 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-6360_52679 .Pixso-instance-5588_11528 {
    width: 16px;
    height: 16px;
}
.Pixso-instance-6360_52680 .Pixso-symbol-5577_144008 {
    width: 24px;
    height: 24px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-6360_52680 .Pixso-vector-5577_144009 {
    width: 71.9%;
    height: 40.64%;
    position: absolute;
    left: 14.05%;
    right: 14.05%;
    top: 32.8%;
    bottom: 26.56%;
}
.Pixso-instance-5982_54589 .Pixso-symbol-5588_11523 {
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
.Pixso-instance-5982_54589 .Pixso-instance-5588_11524 {
    width: 16px;
    height: 16px;
}
.Pixso-instance-5982_54589 .Pixso-frame-5588_11525 {
    width: 16px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 5px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-5982_54589 .Pixso-instance-5588_11526 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5982_54589 .Pixso-paragraph-5588_11527 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5982_54589 .Pixso-instance-5588_11528 {
    width: 16px;
    height: 16px;
}
.Pixso-instance-5982_54590 .Pixso-symbol-5577_144008 {
    width: 24px;
    height: 24px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5982_54590 .Pixso-vector-5577_144009 {
    width: 71.9%;
    height: 40.64%;
    position: absolute;
    left: 14.05%;
    right: 14.05%;
    top: 32.8%;
    bottom: 26.56%;
}
.Pixso-instance-6360_52686 .Pixso-symbol-5588_11523 {
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
.Pixso-instance-6360_52686 .Pixso-instance-5588_11524 {
    width: 16px;
    height: 16px;
}
.Pixso-instance-6360_52686 .Pixso-frame-5588_11525 {
    width: 16px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 5px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-6360_52686 .Pixso-instance-5588_11526 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-6360_52686 .Pixso-paragraph-5588_11527 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-6360_52686 .Pixso-instance-5588_11528 {
    width: 16px;
    height: 16px;
}
.Pixso-instance-6360_52687 .Pixso-symbol-5577_144008 {
    width: 24px;
    height: 24px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-6360_52687 .Pixso-vector-5577_144009 {
    width: 71.9%;
    height: 40.64%;
    position: absolute;
    left: 14.05%;
    right: 14.05%;
    top: 32.8%;
    bottom: 26.56%;
}
.Pixso-instance-5980_54116 .Pixso-symbol-6041_60589 .Pixso-symbol-5577_146643 {
    width: 24px;
    height: 24px;
    position: absolute;
    left: 0px;
    top: 0px;
    background-color: transparent;
}
.Pixso-instance-6360_52183 .Pixso-symbol-6041_60589 .Pixso-symbol-5577_146643 {
    width: 24px;
    height: 24px;
    position: absolute;
    left: 0px;
    top: 0px;
    background-color: transparent;
}
.Pixso-instance-5982_54580 .Pixso-symbol-6041_60589 .Pixso-symbol-5577_146643 {
    width: 24px;
    height: 24px;
    position: absolute;
    left: 0px;
    top: 0px;
    background-color: transparent;
}
.Pixso-instance-6360_52670 .Pixso-symbol-6041_60589 .Pixso-symbol-5577_146643 {
    width: 24px;
    height: 24px;
    position: absolute;
    left: 0px;
    top: 0px;
    background-color: transparent;
}
.Pixso-instance-5980_54116 .Pixso-symbol-6041_60589 {
    width: 24px;
    height: 24px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-6360_52183 .Pixso-symbol-6041_60589 {
    width: 24px;
    height: 24px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5982_54493 .Pixso-symbol-6041_60589 {
    width: 24px;
    height: 24px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-6360_52190 .Pixso-symbol-6041_60589 {
    width: 24px;
    height: 24px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5982_54511 .Pixso-symbol-6041_60589 {
    width: 24px;
    height: 24px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-6360_52197 .Pixso-symbol-6041_60589 {
    width: 24px;
    height: 24px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5982_54580 .Pixso-symbol-6041_60589 {
    width: 24px;
    height: 24px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-6360_52670 .Pixso-symbol-6041_60589 {
    width: 24px;
    height: 24px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5982_54594 .Pixso-symbol-6041_60589 {
    width: 24px;
    height: 24px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-6360_52677 .Pixso-symbol-6041_60589 {
    width: 24px;
    height: 24px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5982_54587 .Pixso-symbol-6041_60589 {
    width: 24px;
    height: 24px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-6360_52684 .Pixso-symbol-6041_60589 {
    width: 24px;
    height: 24px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5980_54116 .Pixso-vector-6041_60590 {
    width: 78.12%;
    height: 81.25%;
    position: absolute;
    left: 10.94%;
    right: 10.94%;
    top: 7.81%;
    bottom: 10.94%;
}
.Pixso-instance-6360_52183 .Pixso-vector-6041_60590 {
    width: 78.12%;
    height: 81.25%;
    position: absolute;
    left: 10.94%;
    right: 10.94%;
    top: 7.81%;
    bottom: 10.94%;
}
.Pixso-instance-5982_54493 .Pixso-vector-6041_60590 {
    width: 78.12%;
    height: 81.25%;
    position: absolute;
    left: 10.94%;
    right: 10.94%;
    top: 7.81%;
    bottom: 10.94%;
}
.Pixso-instance-6360_52190 .Pixso-vector-6041_60590 {
    width: 78.12%;
    height: 81.25%;
    position: absolute;
    left: 10.94%;
    right: 10.94%;
    top: 7.81%;
    bottom: 10.94%;
}
.Pixso-instance-5982_54511 .Pixso-vector-6041_60590 {
    width: 78.12%;
    height: 81.25%;
    position: absolute;
    left: 10.94%;
    right: 10.94%;
    top: 7.81%;
    bottom: 10.94%;
}
.Pixso-instance-6360_52197 .Pixso-vector-6041_60590 {
    width: 78.12%;
    height: 81.25%;
    position: absolute;
    left: 10.94%;
    right: 10.94%;
    top: 7.81%;
    bottom: 10.94%;
}
.Pixso-instance-5982_54580 .Pixso-vector-6041_60590 {
    width: 78.12%;
    height: 81.25%;
    position: absolute;
    left: 10.94%;
    right: 10.94%;
    top: 7.81%;
    bottom: 10.94%;
}
.Pixso-instance-6360_52670 .Pixso-vector-6041_60590 {
    width: 78.12%;
    height: 81.25%;
    position: absolute;
    left: 10.94%;
    right: 10.94%;
    top: 7.81%;
    bottom: 10.94%;
}
.Pixso-instance-5982_54594 .Pixso-vector-6041_60590 {
    width: 78.12%;
    height: 81.25%;
    position: absolute;
    left: 10.94%;
    right: 10.94%;
    top: 7.81%;
    bottom: 10.94%;
}
.Pixso-instance-6360_52677 .Pixso-vector-6041_60590 {
    width: 78.12%;
    height: 81.25%;
    position: absolute;
    left: 10.94%;
    right: 10.94%;
    top: 7.81%;
    bottom: 10.94%;
}
.Pixso-instance-5982_54587 .Pixso-vector-6041_60590 {
    width: 78.12%;
    height: 81.25%;
    position: absolute;
    left: 10.94%;
    right: 10.94%;
    top: 7.81%;
    bottom: 10.94%;
}
.Pixso-instance-6360_52684 .Pixso-vector-6041_60590 {
    width: 78.12%;
    height: 81.25%;
    position: absolute;
    left: 10.94%;
    right: 10.94%;
    top: 7.81%;
    bottom: 10.94%;
}
.Pixso-instance-5980_54116 .Pixso-symbol-6041_60589 .Pixso-symbol-5579_152031 {
    width: 24px;
    height: 24px;
    position: absolute;
    left: 0px;
    top: 0px;
    background-color: transparent;
}
.Pixso-instance-6360_52183 .Pixso-symbol-6041_60589 .Pixso-symbol-5579_152031 {
    width: 24px;
    height: 24px;
    position: absolute;
    left: 0px;
    top: 0px;
    background-color: transparent;
}
.Pixso-instance-5982_54580 .Pixso-symbol-6041_60589 .Pixso-symbol-5579_152031 {
    width: 24px;
    height: 24px;
    position: absolute;
    left: 0px;
    top: 0px;
    background-color: transparent;
}
.Pixso-instance-6360_52670 .Pixso-symbol-6041_60589 .Pixso-symbol-5579_152031 {
    width: 24px;
    height: 24px;
    position: absolute;
    left: 0px;
    top: 0px;
    background-color: transparent;
}
.Pixso-instance-5980_54108 .Pixso-symbol-5489_8978 {
    width: 8px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-6360_52182 .Pixso-symbol-5489_8978 {
    width: 8px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5982_54492 .Pixso-symbol-5489_8978 {
    width: 8px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-6360_52189 .Pixso-symbol-5489_8978 {
    width: 8px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5982_54510 .Pixso-symbol-5489_8978 {
    width: 8px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-6360_52196 .Pixso-symbol-5489_8978 {
    width: 8px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5982_54579 .Pixso-symbol-5489_8978 {
    width: 8px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-6360_52669 .Pixso-symbol-5489_8978 {
    width: 8px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5982_54593 .Pixso-symbol-5489_8978 {
    width: 8px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-6360_52676 .Pixso-symbol-5489_8978 {
    width: 8px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5982_54586 .Pixso-symbol-5489_8978 {
    width: 8px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-6360_52683 .Pixso-symbol-5489_8978 {
    width: 8px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5980_54116 .Pixso-symbol-6041_60589 .Pixso-symbol-5579_151770 {
    width: 24px;
    height: 24px;
    position: absolute;
    left: 0px;
    top: 0px;
    background-color: transparent;
}
.Pixso-instance-6360_52183 .Pixso-symbol-6041_60589 .Pixso-symbol-5579_151770 {
    width: 24px;
    height: 24px;
    position: absolute;
    left: 0px;
    top: 0px;
    background-color: transparent;
}
.Pixso-instance-5982_54580 .Pixso-symbol-6041_60589 .Pixso-symbol-5579_151770 {
    width: 24px;
    height: 24px;
    position: absolute;
    left: 0px;
    top: 0px;
    background-color: transparent;
}
.Pixso-instance-6360_52670 .Pixso-symbol-6041_60589 .Pixso-symbol-5579_151770 {
    width: 24px;
    height: 24px;
    position: absolute;
    left: 0px;
    top: 0px;
    background-color: transparent;
}
</style>
