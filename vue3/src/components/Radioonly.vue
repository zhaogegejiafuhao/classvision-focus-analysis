<template>
    <div class="component-1267_11567">
        <div id="1267_11567" class="Pixso-symbol-1267_11567">
            <div
                id="1267_11568"
                class="stroke-wrapper-1267_11568"
                v-if="
                    Size === 'sm' &&
                    State === 'Default' &&
                    IsChecked === 'False'
                "
            >
                <div
                    class="Pixso-symbol-1267_11568 fill-gray0-white-67_3285"
                ></div>
                <div class="stroke-1267_11568 stroke-gray30-35_1481"></div>
            </div>
            <div
                id="1267_11569"
                class="stroke-wrapper-1267_11569"
                v-if="
                    Size === 'sm' && State === 'Default' && IsChecked === 'True'
                "
            >
                <div class="Pixso-symbol-1267_11569 fill-brand5-1257_33460">
                    <slot name="slot_5549_10524">
                        <div
                            id="5549_10524"
                            class="Pixso-vector-5549_10524"
                        ></div>
                    </slot>
                </div>
                <div class="stroke-1267_11569 stroke-brand60-1257_33467"></div>
            </div>
            <div
                id="5550_11210"
                class="stroke-wrapper-5550_11210"
                v-if="
                    Size === 'md' &&
                    State === 'Default' &&
                    IsChecked === 'False'
                "
            >
                <div
                    class="Pixso-symbol-5550_11210 fill-gray0-white-67_3285"
                ></div>
                <div class="stroke-5550_11210 stroke-gray30-35_1481"></div>
            </div>
            <div
                id="5550_11211"
                class="stroke-wrapper-5550_11211"
                v-if="
                    Size === 'md' && State === 'Default' && IsChecked === 'True'
                "
            >
                <div class="Pixso-symbol-5550_11211 fill-brand5-1257_33460">
                    <slot name="slot_5550_11212">
                        <div
                            id="5550_11212"
                            class="Pixso-vector-5550_11212"
                        ></div>
                    </slot>
                </div>
                <div class="stroke-5550_11211 stroke-brand60-1257_33467"></div>
            </div>
            <div
                id="5550_11238"
                class="stroke-wrapper-5550_11238"
                v-if="
                    Size === 'lg' &&
                    State === 'Default' &&
                    IsChecked === 'False'
                "
            >
                <div
                    class="Pixso-symbol-5550_11238 fill-gray0-white-67_3285"
                ></div>
                <div class="stroke-5550_11238 stroke-gray30-35_1481"></div>
            </div>
            <div
                id="5550_11239"
                class="stroke-wrapper-5550_11239"
                v-if="
                    Size === 'lg' && State === 'Default' && IsChecked === 'True'
                "
            >
                <div class="Pixso-symbol-5550_11239 fill-brand5-1257_33460">
                    <slot name="slot_5550_11240">
                        <div
                            id="5550_11240"
                            class="Pixso-vector-5550_11240"
                        ></div>
                    </slot>
                </div>
                <div class="stroke-5550_11239 stroke-brand60-1257_33467"></div>
            </div>
            <div
                id="1267_11577"
                class="stroke-wrapper-1267_11577"
                v-if="
                    Size === 'sm' && State === 'Hover' && IsChecked === 'False'
                "
            >
                <div
                    class="Pixso-symbol-1267_11577 fill-brand5-1257_33460"
                ></div>
                <div class="stroke-1267_11577 stroke-brand60-1257_33467"></div>
            </div>
            <div
                id="1267_11578"
                class="stroke-wrapper-1267_11578"
                v-if="
                    Size === 'sm' && State === 'Hover' && IsChecked === 'True'
                "
            >
                <div class="Pixso-symbol-1267_11578 fill-brand5-1257_33460">
                    <slot name="slot_5549_10526">
                        <div
                            id="5549_10526"
                            class="Pixso-vector-5549_10526"
                        ></div>
                    </slot>
                </div>
                <div class="stroke-1267_11578 stroke-brand60-1257_33467"></div>
            </div>
            <div
                id="5550_11213"
                class="stroke-wrapper-5550_11213"
                v-if="
                    Size === 'md' && State === 'Hover' && IsChecked === 'False'
                "
            >
                <div
                    class="Pixso-symbol-5550_11213 fill-brand5-1257_33460"
                ></div>
                <div class="stroke-5550_11213 stroke-brand60-1257_33467"></div>
            </div>
            <div
                id="5550_11214"
                class="stroke-wrapper-5550_11214"
                v-if="
                    Size === 'md' && State === 'Hover' && IsChecked === 'True'
                "
            >
                <div class="Pixso-symbol-5550_11214 fill-brand5-1257_33460">
                    <slot name="slot_5550_11215">
                        <div
                            id="5550_11215"
                            class="Pixso-vector-5550_11215"
                        ></div>
                    </slot>
                </div>
                <div class="stroke-5550_11214 stroke-brand60-1257_33467"></div>
            </div>
            <div
                id="5550_11241"
                class="stroke-wrapper-5550_11241"
                v-if="
                    Size === 'lg' && State === 'Hover' && IsChecked === 'False'
                "
            >
                <div
                    class="Pixso-symbol-5550_11241 fill-brand5-1257_33460"
                ></div>
                <div class="stroke-5550_11241 stroke-brand60-1257_33467"></div>
            </div>
            <div
                id="5550_11242"
                class="stroke-wrapper-5550_11242"
                v-if="
                    Size === 'lg' && State === 'Hover' && IsChecked === 'True'
                "
            >
                <div class="Pixso-symbol-5550_11242 fill-brand5-1257_33460">
                    <slot name="slot_5550_11243">
                        <div
                            id="5550_11243"
                            class="Pixso-vector-5550_11243"
                        ></div>
                    </slot>
                </div>
                <div class="stroke-5550_11242 stroke-brand60-1257_33467"></div>
            </div>
            <div
                id="1267_11586"
                class="stroke-wrapper-1267_11586"
                v-if="
                    Size === 'sm' &&
                    State === 'Focused' &&
                    IsChecked === 'False'
                "
            >
                <div
                    class="Pixso-symbol-1267_11586 fill-gray0-white-67_3285 effect-focusring-brand-5459_24463"
                ></div>
                <div class="stroke-1267_11586 stroke-brand60-1257_33467"></div>
            </div>
            <div
                id="1267_11587"
                class="stroke-wrapper-1267_11587"
                v-if="
                    Size === 'sm' && State === 'Focused' && IsChecked === 'True'
                "
            >
                <div
                    class="Pixso-symbol-1267_11587 fill-brand5-1257_33460 effect-focusring-brand-5459_24463"
                >
                    <slot name="slot_5549_10528">
                        <div
                            id="5549_10528"
                            class="Pixso-vector-5549_10528"
                        ></div>
                    </slot>
                </div>
                <div class="stroke-1267_11587 stroke-brand60-1257_33467"></div>
            </div>
            <div
                id="5550_11216"
                class="stroke-wrapper-5550_11216"
                v-if="
                    Size === 'md' &&
                    State === 'Focused' &&
                    IsChecked === 'False'
                "
            >
                <div
                    class="Pixso-symbol-5550_11216 fill-gray0-white-67_3285 effect-focusring-brand-5459_24463"
                ></div>
                <div class="stroke-5550_11216 stroke-brand60-1257_33467"></div>
            </div>
            <div
                id="5550_11218"
                class="stroke-wrapper-5550_11218"
                v-if="
                    Size === 'md' && State === 'Focused' && IsChecked === 'True'
                "
            >
                <div
                    class="Pixso-symbol-5550_11218 fill-brand5-1257_33460 effect-focusring-brand-5459_24463"
                >
                    <slot name="slot_5550_11219">
                        <div
                            id="5550_11219"
                            class="Pixso-vector-5550_11219"
                        ></div>
                    </slot>
                </div>
                <div class="stroke-5550_11218 stroke-brand60-1257_33467"></div>
            </div>
            <div
                id="5550_11244"
                class="stroke-wrapper-5550_11244"
                v-if="
                    Size === 'lg' &&
                    State === 'Focused' &&
                    IsChecked === 'False'
                "
            >
                <div
                    class="Pixso-symbol-5550_11244 fill-gray0-white-67_3285 effect-focusring-brand-5459_24463"
                ></div>
                <div class="stroke-5550_11244 stroke-brand60-1257_33467"></div>
            </div>
            <div
                id="5550_11246"
                class="stroke-wrapper-5550_11246"
                v-if="
                    Size === 'lg' && State === 'Focused' && IsChecked === 'True'
                "
            >
                <div
                    class="Pixso-symbol-5550_11246 fill-brand5-1257_33460 effect-focusring-brand-5459_24463"
                >
                    <slot name="slot_5550_11247">
                        <div
                            id="5550_11247"
                            class="Pixso-vector-5550_11247"
                        ></div>
                    </slot>
                </div>
                <div class="stroke-5550_11246 stroke-brand60-1257_33467"></div>
            </div>
            <div
                id="5549_11195"
                class="stroke-wrapper-5549_11195"
                v-if="
                    Size === 'sm' &&
                    State === 'Disabled' &&
                    IsChecked === 'False'
                "
            >
                <div class="Pixso-symbol-5549_11195 fill-gray5-32_4120"></div>
                <div class="stroke-5549_11195 stroke-gray30-35_1481"></div>
            </div>
            <div
                id="5549_11196"
                class="stroke-wrapper-5549_11196"
                v-if="
                    Size === 'sm' &&
                    State === 'Disabled' &&
                    IsChecked === 'True'
                "
            >
                <div class="Pixso-symbol-5549_11196 fill-gray5-32_4120">
                    <slot name="slot_5549_11197">
                        <div
                            id="5549_11197"
                            class="Pixso-vector-5549_11197"
                        ></div>
                    </slot>
                </div>
                <div class="stroke-5549_11196 stroke-gray30-35_1481"></div>
            </div>
            <div
                id="5550_11217"
                class="stroke-wrapper-5550_11217"
                v-if="
                    Size === 'md' &&
                    State === 'Disabled' &&
                    IsChecked === 'False'
                "
            >
                <div class="Pixso-symbol-5550_11217 fill-gray5-32_4120"></div>
                <div class="stroke-5550_11217 stroke-gray30-35_1481"></div>
            </div>
            <div
                id="5550_11220"
                class="stroke-wrapper-5550_11220"
                v-if="
                    Size === 'md' &&
                    State === 'Disabled' &&
                    IsChecked === 'True'
                "
            >
                <div class="Pixso-symbol-5550_11220 fill-gray5-32_4120">
                    <slot name="slot_5550_11221">
                        <div
                            id="5550_11221"
                            class="Pixso-vector-5550_11221"
                        ></div>
                    </slot>
                </div>
                <div class="stroke-5550_11220 stroke-gray30-35_1481"></div>
            </div>
            <div
                id="5550_11245"
                class="stroke-wrapper-5550_11245"
                v-if="
                    Size === 'lg' &&
                    State === 'Disabled' &&
                    IsChecked === 'False'
                "
            >
                <div class="Pixso-symbol-5550_11245 fill-gray5-32_4120"></div>
                <div class="stroke-5550_11245 stroke-gray30-35_1481"></div>
            </div>
            <div
                id="5550_11248"
                class="stroke-wrapper-5550_11248"
                v-if="
                    Size === 'lg' &&
                    State === 'Disabled' &&
                    IsChecked === 'True'
                "
            >
                <div class="Pixso-symbol-5550_11248 fill-gray5-32_4120">
                    <slot name="slot_5550_11249">
                        <div
                            id="5550_11249"
                            class="Pixso-vector-5550_11249"
                        ></div>
                    </slot>
                </div>
                <div class="stroke-5550_11248 stroke-gray30-35_1481"></div>
            </div>
        </div>
    </div>
</template>
<script lang="ts" setup>
const props = defineProps({
    Size: { type: String },
    State: { type: String },
    IsChecked: { type: String }
});
</script>
<style>
.Pixso-symbol-1267_11567 {
}
.Pixso-symbol-1267_11568 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    border-radius: 123px 123px 123px 123px;
}
.stroke-wrapper-1267_11568 {
    position: relative;
    width: 16px;
    height: 16px;
}
.stroke-1267_11568 {
    position: absolute;
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-symbol-1267_11569 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    border-radius: 123px 123px 123px 123px;
}
.stroke-wrapper-1267_11569 {
    position: relative;
    width: 16px;
    height: 16px;
}
.stroke-1267_11569 {
    position: absolute;
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-vector-5549_10524 {
    width: 6px;
    height: 6px;
    background-image: url(@/assets/images/Ellipse38.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translateX(calc(-50% + 0px)) translateY(calc(-50% + 0px));
}
.Pixso-symbol-5550_11210 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    border-radius: 123px 123px 123px 123px;
}
.stroke-wrapper-5550_11210 {
    position: relative;
    width: 20px;
    height: 20px;
}
.stroke-5550_11210 {
    position: absolute;
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-symbol-5550_11211 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    border-radius: 123px 123px 123px 123px;
}
.stroke-wrapper-5550_11211 {
    position: relative;
    width: 20px;
    height: 20px;
}
.stroke-5550_11211 {
    position: absolute;
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-vector-5550_11212 {
    width: 8px;
    height: 8px;
    background-image: url(@/assets/images/Ellipse37.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translateX(calc(-50% + 0px)) translateY(calc(-50% + 0px));
}
.Pixso-symbol-5550_11238 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    border-radius: 123px 123px 123px 123px;
}
.stroke-wrapper-5550_11238 {
    position: relative;
    width: 24px;
    height: 24px;
}
.stroke-5550_11238 {
    position: absolute;
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-symbol-5550_11239 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    border-radius: 123px 123px 123px 123px;
}
.stroke-wrapper-5550_11239 {
    position: relative;
    width: 24px;
    height: 24px;
}
.stroke-5550_11239 {
    position: absolute;
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-vector-5550_11240 {
    width: 10px;
    height: 10px;
    background-image: url(@/assets/images/Ellipse36.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translateX(calc(-50% + 0px)) translateY(calc(-50% + 0px));
}
.Pixso-symbol-1267_11577 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    border-radius: 123px 123px 123px 123px;
}
.stroke-wrapper-1267_11577 {
    position: relative;
    width: 16px;
    height: 16px;
}
.stroke-1267_11577 {
    position: absolute;
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-symbol-1267_11578 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    border-radius: 123px 123px 123px 123px;
}
.stroke-wrapper-1267_11578 {
    position: relative;
    width: 16px;
    height: 16px;
}
.stroke-1267_11578 {
    position: absolute;
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-vector-5549_10526 {
    width: 6px;
    height: 6px;
    background-image: url(@/assets/images/Ellipse35.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translateX(calc(-50% + 0px)) translateY(calc(-50% + 0px));
}
.Pixso-symbol-5550_11213 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    border-radius: 123px 123px 123px 123px;
}
.stroke-wrapper-5550_11213 {
    position: relative;
    width: 20px;
    height: 20px;
}
.stroke-5550_11213 {
    position: absolute;
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-symbol-5550_11214 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    border-radius: 123px 123px 123px 123px;
}
.stroke-wrapper-5550_11214 {
    position: relative;
    width: 20px;
    height: 20px;
}
.stroke-5550_11214 {
    position: absolute;
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-vector-5550_11215 {
    width: 8px;
    height: 8px;
    background-image: url(@/assets/images/Ellipse34.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translateX(calc(-50% + 0px)) translateY(calc(-50% + 0px));
}
.Pixso-symbol-5550_11241 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    border-radius: 123px 123px 123px 123px;
}
.stroke-wrapper-5550_11241 {
    position: relative;
    width: 24px;
    height: 24px;
}
.stroke-5550_11241 {
    position: absolute;
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-symbol-5550_11242 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    border-radius: 123px 123px 123px 123px;
}
.stroke-wrapper-5550_11242 {
    position: relative;
    width: 24px;
    height: 24px;
}
.stroke-5550_11242 {
    position: absolute;
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-vector-5550_11243 {
    width: 10px;
    height: 10px;
    background-image: url(@/assets/images/Ellipse33.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translateX(calc(-50% + 0px)) translateY(calc(-50% + 0px));
}
.Pixso-symbol-1267_11586 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    border-radius: 123px 123px 123px 123px;
}
.stroke-wrapper-1267_11586 {
    position: relative;
    width: 16px;
    height: 16px;
}
.stroke-1267_11586 {
    position: absolute;
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-symbol-1267_11587 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    border-radius: 123px 123px 123px 123px;
}
.stroke-wrapper-1267_11587 {
    position: relative;
    width: 16px;
    height: 16px;
}
.stroke-1267_11587 {
    position: absolute;
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-vector-5549_10528 {
    width: 6px;
    height: 6px;
    background-image: url(@/assets/images/Ellipse32.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translateX(calc(-50% + 0px)) translateY(calc(-50% + 0px));
}
.Pixso-symbol-5550_11216 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    border-radius: 123px 123px 123px 123px;
}
.stroke-wrapper-5550_11216 {
    position: relative;
    width: 20px;
    height: 20px;
}
.stroke-5550_11216 {
    position: absolute;
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-symbol-5550_11218 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    border-radius: 123px 123px 123px 123px;
}
.stroke-wrapper-5550_11218 {
    position: relative;
    width: 20px;
    height: 20px;
}
.stroke-5550_11218 {
    position: absolute;
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-vector-5550_11219 {
    width: 8px;
    height: 8px;
    background-image: url(@/assets/images/Ellipse31.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translateX(calc(-50% + 0px)) translateY(calc(-50% + 0px));
}
.Pixso-symbol-5550_11244 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    border-radius: 123px 123px 123px 123px;
}
.stroke-wrapper-5550_11244 {
    position: relative;
    width: 24px;
    height: 24px;
}
.stroke-5550_11244 {
    position: absolute;
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-symbol-5550_11246 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    border-radius: 123px 123px 123px 123px;
}
.stroke-wrapper-5550_11246 {
    position: relative;
    width: 24px;
    height: 24px;
}
.stroke-5550_11246 {
    position: absolute;
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-vector-5550_11247 {
    width: 10px;
    height: 10px;
    background-image: url(@/assets/images/Ellipse30.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translateX(calc(-50% + 0px)) translateY(calc(-50% + 0px));
}
.Pixso-symbol-5549_11195 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    border-radius: 123px 123px 123px 123px;
}
.stroke-wrapper-5549_11195 {
    position: relative;
    width: 16px;
    height: 16px;
}
.stroke-5549_11195 {
    position: absolute;
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-symbol-5549_11196 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    border-radius: 123px 123px 123px 123px;
}
.stroke-wrapper-5549_11196 {
    position: relative;
    width: 16px;
    height: 16px;
}
.stroke-5549_11196 {
    position: absolute;
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-vector-5549_11197 {
    width: 6px;
    height: 6px;
    background-image: url(@/assets/images/Ellipse3.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translateX(calc(-50% + 0px)) translateY(calc(-50% + 0px));
}
.Pixso-symbol-5550_11217 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    border-radius: 123px 123px 123px 123px;
}
.stroke-wrapper-5550_11217 {
    position: relative;
    width: 20px;
    height: 20px;
}
.stroke-5550_11217 {
    position: absolute;
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-symbol-5550_11220 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    border-radius: 123px 123px 123px 123px;
}
.stroke-wrapper-5550_11220 {
    position: relative;
    width: 20px;
    height: 20px;
}
.stroke-5550_11220 {
    position: absolute;
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-vector-5550_11221 {
    width: 8px;
    height: 8px;
    background-image: url(@/assets/images/Ellipse310.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translateX(calc(-50% + 0px)) translateY(calc(-50% + 0px));
}
.Pixso-symbol-5550_11245 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    border-radius: 123px 123px 123px 123px;
}
.stroke-wrapper-5550_11245 {
    position: relative;
    width: 24px;
    height: 24px;
}
.stroke-5550_11245 {
    position: absolute;
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-symbol-5550_11248 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    border-radius: 123px 123px 123px 123px;
}
.stroke-wrapper-5550_11248 {
    position: relative;
    width: 24px;
    height: 24px;
}
.stroke-5550_11248 {
    position: absolute;
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-vector-5550_11249 {
    width: 10px;
    height: 10px;
    background-image: url(@/assets/images/Ellipse39.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translateX(calc(-50% + 0px)) translateY(calc(-50% + 0px));
}
</style>
