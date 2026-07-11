<template>
    <div class="component-1267_11519">
        <div id="1267_11519" class="Pixso-symbol-1267_11519">
            <div
                id="1267_11520"
                class="stroke-wrapper-1267_11520"
                v-if="
                    Size === 'sm' &&
                    State === 'Defaut' &&
                    IsIndeterminate === 'False' &&
                    IsChecked === 'False'
                "
            >
                <div
                    class="Pixso-symbol-1267_11520 fill-gray0-white-67_3285"
                ></div>
                <div class="stroke-1267_11520 stroke-gray30-35_1481"></div>
            </div>
            <div
                id="1267_11521"
                class="Pixso-symbol-1267_11521 fill-brand60-1257_33467"
                v-if="
                    Size === 'sm' &&
                    State === 'Defaut' &&
                    IsIndeterminate === 'False' &&
                    IsChecked === 'True'
                "
            >
                <slot name="slot_5546_8584">
                    <FormControlCheck
                        id="5546_8584"
                        class="Pixso-instance-5546_8584"
                    />
                </slot>
            </div>
            <div
                id="1267_11523"
                class="Pixso-symbol-1267_11523 fill-brand60-1257_33467"
                v-if="
                    Size === 'sm' &&
                    State === 'Defaut' &&
                    IsIndeterminate === 'True' &&
                    IsChecked === 'False'
                "
            >
                <slot name="slot_5546_8596">
                    <FormControlMinus
                        id="5546_8596"
                        class="Pixso-instance-5546_8596"
                    />
                </slot>
            </div>
            <div
                id="5547_8762"
                class="stroke-wrapper-5547_8762"
                v-if="
                    Size === 'md' &&
                    State === 'Defaut' &&
                    IsIndeterminate === 'False' &&
                    IsChecked === 'False'
                "
            >
                <div
                    class="Pixso-symbol-5547_8762 fill-gray0-white-67_3285"
                ></div>
                <div class="stroke-5547_8762 stroke-gray30-35_1481"></div>
            </div>
            <div
                id="5547_8763"
                class="Pixso-symbol-5547_8763 fill-brand60-1257_33467"
                v-if="
                    Size === 'md' &&
                    State === 'Defaut' &&
                    IsIndeterminate === 'False' &&
                    IsChecked === 'True'
                "
            >
                <slot name="slot_5547_8764">
                    <FormControlCheck
                        id="5547_8764"
                        class="Pixso-instance-5547_8764"
                    />
                </slot>
            </div>
            <div
                id="5547_8765"
                class="Pixso-symbol-5547_8765 fill-brand60-1257_33467"
                v-if="
                    Size === 'md' &&
                    State === 'Defaut' &&
                    IsIndeterminate === 'True' &&
                    IsChecked === 'False'
                "
            >
                <slot name="slot_5547_8766">
                    <FormControlMinus
                        id="5547_8766"
                        class="Pixso-instance-5547_8766"
                    />
                </slot>
            </div>
            <div
                id="5547_8834"
                class="stroke-wrapper-5547_8834"
                v-if="
                    Size === 'lg' &&
                    State === 'Defaut' &&
                    IsIndeterminate === 'False' &&
                    IsChecked === 'False'
                "
            >
                <div
                    class="Pixso-symbol-5547_8834 fill-gray0-white-67_3285"
                ></div>
                <div class="stroke-5547_8834 stroke-gray30-35_1481"></div>
            </div>
            <div
                id="5547_8835"
                class="Pixso-symbol-5547_8835 fill-brand60-1257_33467"
                v-if="
                    Size === 'lg' &&
                    State === 'Defaut' &&
                    IsIndeterminate === 'False' &&
                    IsChecked === 'True'
                "
            >
                <slot name="slot_5547_8836">
                    <FormControlCheck
                        id="5547_8836"
                        class="Pixso-instance-5547_8836"
                    />
                </slot>
            </div>
            <div
                id="5547_8837"
                class="Pixso-symbol-5547_8837 fill-brand60-1257_33467"
                v-if="
                    Size === 'lg' &&
                    State === 'Defaut' &&
                    IsIndeterminate === 'True' &&
                    IsChecked === 'False'
                "
            >
                <slot name="slot_5547_8838">
                    <FormControlMinus
                        id="5547_8838"
                        class="Pixso-instance-5547_8838"
                    />
                </slot>
            </div>
            <div
                id="1267_11535"
                class="stroke-wrapper-1267_11535"
                v-if="
                    Size === 'sm' &&
                    State === 'Hover' &&
                    IsIndeterminate === 'False' &&
                    IsChecked === 'False'
                "
            >
                <div
                    class="Pixso-symbol-1267_11535 fill-brand5-1257_33460"
                ></div>
                <div class="stroke-1267_11535 stroke-brand60-1257_33467"></div>
            </div>
            <div
                id="1267_11536"
                class="Pixso-symbol-1267_11536 fill-brand60-1257_33467"
                v-if="
                    Size === 'sm' &&
                    State === 'Hover' &&
                    IsIndeterminate === 'False' &&
                    IsChecked === 'True'
                "
            >
                <slot name="slot_5546_8590">
                    <FormControlCheck
                        id="5546_8590"
                        class="Pixso-instance-5546_8590"
                    />
                </slot>
            </div>
            <div
                id="1267_11538"
                class="Pixso-symbol-1267_11538 fill-brand60-1257_33467"
                v-if="
                    Size === 'sm' &&
                    State === 'Hover' &&
                    IsIndeterminate === 'True' &&
                    IsChecked === 'False'
                "
            >
                <slot name="slot_5546_8611">
                    <FormControlMinus
                        id="5546_8611"
                        class="Pixso-instance-5546_8611"
                    />
                </slot>
            </div>
            <div
                id="5547_8767"
                class="stroke-wrapper-5547_8767"
                v-if="
                    Size === 'md' &&
                    State === 'Hover' &&
                    IsIndeterminate === 'False' &&
                    IsChecked === 'False'
                "
            >
                <div
                    class="Pixso-symbol-5547_8767 fill-brand5-1257_33460"
                ></div>
                <div class="stroke-5547_8767 stroke-brand60-1257_33467"></div>
            </div>
            <div
                id="5547_8768"
                class="Pixso-symbol-5547_8768 fill-brand60-1257_33467"
                v-if="
                    Size === 'md' &&
                    State === 'Hover' &&
                    IsIndeterminate === 'False' &&
                    IsChecked === 'True'
                "
            >
                <slot name="slot_5547_8769">
                    <FormControlCheck
                        id="5547_8769"
                        class="Pixso-instance-5547_8769"
                    />
                </slot>
            </div>
            <div
                id="5547_8770"
                class="Pixso-symbol-5547_8770 fill-brand60-1257_33467"
                v-if="
                    Size === 'md' &&
                    State === 'Hover' &&
                    IsIndeterminate === 'True' &&
                    IsChecked === 'False'
                "
            >
                <slot name="slot_5547_8771">
                    <FormControlMinus
                        id="5547_8771"
                        class="Pixso-instance-5547_8771"
                    />
                </slot>
            </div>
            <div
                id="5547_8839"
                class="stroke-wrapper-5547_8839"
                v-if="
                    Size === 'lg' &&
                    State === 'Hover' &&
                    IsIndeterminate === 'False' &&
                    IsChecked === 'False'
                "
            >
                <div
                    class="Pixso-symbol-5547_8839 fill-brand5-1257_33460"
                ></div>
                <div class="stroke-5547_8839 stroke-brand60-1257_33467"></div>
            </div>
            <div
                id="5547_8840"
                class="Pixso-symbol-5547_8840 fill-brand60-1257_33467"
                v-if="
                    Size === 'lg' &&
                    State === 'Hover' &&
                    IsIndeterminate === 'False' &&
                    IsChecked === 'True'
                "
            >
                <slot name="slot_5547_8841">
                    <FormControlCheck
                        id="5547_8841"
                        class="Pixso-instance-5547_8841"
                    />
                </slot>
            </div>
            <div
                id="5547_8842"
                class="Pixso-symbol-5547_8842 fill-brand60-1257_33467"
                v-if="
                    Size === 'lg' &&
                    State === 'Hover' &&
                    IsIndeterminate === 'True' &&
                    IsChecked === 'False'
                "
            >
                <slot name="slot_5547_8843">
                    <FormControlMinus
                        id="5547_8843"
                        class="Pixso-instance-5547_8843"
                    />
                </slot>
            </div>
            <div
                id="5546_8638"
                class="stroke-wrapper-5546_8638"
                v-if="
                    Size === 'sm' &&
                    State === 'Focused' &&
                    IsIndeterminate === 'False' &&
                    IsChecked === 'False'
                "
            >
                <div
                    class="Pixso-symbol-5546_8638 fill-brand5-1257_33460 effect-focusring-brand-5459_24463"
                ></div>
                <div class="stroke-5546_8638 stroke-brand60-1257_33467"></div>
            </div>
            <div
                id="5546_8639"
                class="Pixso-symbol-5546_8639 fill-brand60-1257_33467 effect-focusring-brand-5459_24463"
                v-if="
                    Size === 'sm' &&
                    State === 'Focused' &&
                    IsIndeterminate === 'False' &&
                    IsChecked === 'True'
                "
            >
                <slot name="slot_5546_8640">
                    <FormControlCheck
                        id="5546_8640"
                        class="Pixso-instance-5546_8640"
                    />
                </slot>
            </div>
            <div
                id="5546_8641"
                class="Pixso-symbol-5546_8641 fill-brand60-1257_33467 effect-focusring-brand-5459_24463"
                v-if="
                    Size === 'sm' &&
                    State === 'Focused' &&
                    IsIndeterminate === 'True' &&
                    IsChecked === 'False'
                "
            >
                <slot name="slot_5546_8642">
                    <FormControlMinus
                        id="5546_8642"
                        class="Pixso-instance-5546_8642"
                    />
                </slot>
            </div>
            <div
                id="5547_8772"
                class="stroke-wrapper-5547_8772"
                v-if="
                    Size === 'md' &&
                    State === 'Focused' &&
                    IsIndeterminate === 'False' &&
                    IsChecked === 'False'
                "
            >
                <div
                    class="Pixso-symbol-5547_8772 fill-brand5-1257_33460 effect-focusring-brand-5459_24463"
                ></div>
                <div class="stroke-5547_8772 stroke-brand60-1257_33467"></div>
            </div>
            <div
                id="5547_8773"
                class="Pixso-symbol-5547_8773 fill-brand60-1257_33467 effect-focusring-brand-5459_24463"
                v-if="
                    Size === 'md' &&
                    State === 'Focused' &&
                    IsIndeterminate === 'False' &&
                    IsChecked === 'True'
                "
            >
                <slot name="slot_5547_8774">
                    <FormControlCheck
                        id="5547_8774"
                        class="Pixso-instance-5547_8774"
                    />
                </slot>
            </div>
            <div
                id="5547_8775"
                class="Pixso-symbol-5547_8775 fill-brand60-1257_33467 effect-focusring-brand-5459_24463"
                v-if="
                    Size === 'md' &&
                    State === 'Focused' &&
                    IsIndeterminate === 'True' &&
                    IsChecked === 'False'
                "
            >
                <slot name="slot_5547_8776">
                    <FormControlMinus
                        id="5547_8776"
                        class="Pixso-instance-5547_8776"
                    />
                </slot>
            </div>
            <div
                id="5547_8844"
                class="stroke-wrapper-5547_8844"
                v-if="
                    Size === 'lg' &&
                    State === 'Focused' &&
                    IsIndeterminate === 'False' &&
                    IsChecked === 'False'
                "
            >
                <div
                    class="Pixso-symbol-5547_8844 fill-brand5-1257_33460 effect-focusring-brand-5459_24463"
                ></div>
                <div class="stroke-5547_8844 stroke-brand60-1257_33467"></div>
            </div>
            <div
                id="5547_8845"
                class="Pixso-symbol-5547_8845 fill-brand60-1257_33467 effect-focusring-brand-5459_24463"
                v-if="
                    Size === 'lg' &&
                    State === 'Focused' &&
                    IsIndeterminate === 'False' &&
                    IsChecked === 'True'
                "
            >
                <slot name="slot_5547_8846">
                    <FormControlCheck
                        id="5547_8846"
                        class="Pixso-instance-5547_8846"
                    />
                </slot>
            </div>
            <div
                id="5547_8847"
                class="Pixso-symbol-5547_8847 fill-brand60-1257_33467 effect-focusring-brand-5459_24463"
                v-if="
                    Size === 'lg' &&
                    State === 'Focused' &&
                    IsIndeterminate === 'True' &&
                    IsChecked === 'False'
                "
            >
                <slot name="slot_5547_8848">
                    <FormControlMinus
                        id="5547_8848"
                        class="Pixso-instance-5547_8848"
                    />
                </slot>
            </div>
            <div
                id="1267_11550"
                class="stroke-wrapper-1267_11550"
                v-if="
                    Size === 'sm' &&
                    State === 'Disabled' &&
                    IsIndeterminate === 'False' &&
                    IsChecked === 'False'
                "
            >
                <div class="Pixso-symbol-1267_11550 fill-gray5-32_4120"></div>
                <div class="stroke-1267_11550 stroke-gray30-35_1481"></div>
            </div>
            <div
                id="1267_11551"
                class="Pixso-symbol-1267_11551 fill-gray5-32_4120"
                v-if="
                    Size === 'sm' &&
                    State === 'Disabled' &&
                    IsIndeterminate === 'False' &&
                    IsChecked === 'True'
                "
            >
                <slot name="slot_5546_8623">
                    <FormControlCheck
                        id="5546_8623"
                        class="Pixso-instance-5546_8623"
                    />
                </slot>
            </div>
            <div
                id="1267_11553"
                class="Pixso-symbol-1267_11553 fill-gray5-32_4120"
                v-if="
                    Size === 'sm' &&
                    State === 'Disabled' &&
                    IsIndeterminate === 'True' &&
                    IsChecked === 'False'
                "
            >
                <slot name="slot_5546_8617">
                    <FormControlMinus
                        id="5546_8617"
                        class="Pixso-instance-5546_8617"
                    />
                </slot>
            </div>
            <div
                id="5547_8777"
                class="stroke-wrapper-5547_8777"
                v-if="
                    Size === 'md' &&
                    State === 'Disabled' &&
                    IsIndeterminate === 'False' &&
                    IsChecked === 'False'
                "
            >
                <div class="Pixso-symbol-5547_8777 fill-gray5-32_4120"></div>
                <div class="stroke-5547_8777 stroke-gray30-35_1481"></div>
            </div>
            <div
                id="5547_8778"
                class="Pixso-symbol-5547_8778 fill-gray5-32_4120"
                v-if="
                    Size === 'md' &&
                    State === 'Disabled' &&
                    IsIndeterminate === 'False' &&
                    IsChecked === 'True'
                "
            >
                <slot name="slot_5547_8779">
                    <FormControlCheck
                        id="5547_8779"
                        class="Pixso-instance-5547_8779"
                    />
                </slot>
            </div>
            <div
                id="5547_8780"
                class="Pixso-symbol-5547_8780 fill-gray5-32_4120"
                v-if="
                    Size === 'md' &&
                    State === 'Disabled' &&
                    IsIndeterminate === 'True' &&
                    IsChecked === 'False'
                "
            >
                <slot name="slot_5547_8781">
                    <FormControlMinus
                        id="5547_8781"
                        class="Pixso-instance-5547_8781"
                    />
                </slot>
            </div>
            <div
                id="5547_8849"
                class="stroke-wrapper-5547_8849"
                v-if="
                    Size === 'lg' &&
                    State === 'Disabled' &&
                    IsIndeterminate === 'False' &&
                    IsChecked === 'False'
                "
            >
                <div class="Pixso-symbol-5547_8849 fill-gray5-32_4120"></div>
                <div class="stroke-5547_8849 stroke-gray30-35_1481"></div>
            </div>
            <div
                id="5547_8850"
                class="Pixso-symbol-5547_8850 fill-gray5-32_4120"
                v-if="
                    Size === 'lg' &&
                    State === 'Disabled' &&
                    IsIndeterminate === 'False' &&
                    IsChecked === 'True'
                "
            >
                <slot name="slot_5547_8851">
                    <FormControlCheck
                        id="5547_8851"
                        class="Pixso-instance-5547_8851"
                    />
                </slot>
            </div>
            <div
                id="5547_8852"
                class="Pixso-symbol-5547_8852 fill-gray5-32_4120"
                v-if="
                    Size === 'lg' &&
                    State === 'Disabled' &&
                    IsIndeterminate === 'True' &&
                    IsChecked === 'False'
                "
            >
                <slot name="slot_5547_8853">
                    <FormControlMinus
                        id="5547_8853"
                        class="Pixso-instance-5547_8853"
                    />
                </slot>
            </div>
        </div>
    </div>
</template>
<script lang="ts" setup>
import FormControlCheck from "@/components/Formcontrolcheck.vue";
import FormControlMinus from "@/components/Formcontrolminus.vue";
const props = defineProps({
    Size: { type: String },
    State: { type: String },
    IsIndeterminate: { type: String },
    IsChecked: { type: String }
});
</script>
<style>
.Pixso-symbol-1267_11519 {
}
.Pixso-symbol-1267_11520 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    border-radius: 6px 6px 6px 6px;
}
.stroke-wrapper-1267_11520 {
    position: relative;
    width: 16px;
    height: 16px;
}
.stroke-1267_11520 {
    position: absolute;
    inset: 0px;
    border-radius: 6px 6px 6px 6px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-symbol-1267_11521 {
    width: 16px;
    height: 16px;
    overflow: hidden;
    position: relative;
    border-radius: 6px 6px 6px 6px;
}
.Pixso-instance-5546_8584 {
    width: 10px;
    height: 10px;
}
.Pixso-symbol-1267_11523 {
    width: 16px;
    height: 16px;
    overflow: hidden;
    position: relative;
    border-radius: 6px 6px 6px 6px;
}
.Pixso-instance-5546_8596 {
    width: 10px;
    height: 10px;
}
.Pixso-symbol-5547_8762 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    border-radius: 8px 8px 8px 8px;
}
.stroke-wrapper-5547_8762 {
    position: relative;
    width: 20px;
    height: 20px;
}
.stroke-5547_8762 {
    position: absolute;
    inset: 0px;
    border-radius: 8px 8px 8px 8px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-symbol-5547_8763 {
    width: 20px;
    height: 20px;
    overflow: hidden;
    position: relative;
    border-radius: 8px 8px 8px 8px;
}
.Pixso-instance-5547_8764 {
    width: 12px;
    height: 12px;
}
.Pixso-symbol-5547_8765 {
    width: 20px;
    height: 20px;
    overflow: hidden;
    position: relative;
    border-radius: 8px 8px 8px 8px;
}
.Pixso-instance-5547_8766 {
    width: 12px;
    height: 12px;
}
.Pixso-symbol-5547_8834 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    border-radius: 10px 10px 10px 10px;
}
.stroke-wrapper-5547_8834 {
    position: relative;
    width: 24px;
    height: 24px;
}
.stroke-5547_8834 {
    position: absolute;
    inset: 0px;
    border-radius: 10px 10px 10px 10px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-symbol-5547_8835 {
    width: 24px;
    height: 24px;
    overflow: hidden;
    position: relative;
    border-radius: 10px 10px 10px 10px;
}
.Pixso-instance-5547_8836 {
    width: 16px;
    height: 16px;
}
.Pixso-symbol-5547_8837 {
    width: 24px;
    height: 24px;
    overflow: hidden;
    position: relative;
    border-radius: 10px 10px 10px 10px;
}
.Pixso-instance-5547_8838 {
    width: 16px;
    height: 16px;
}
.Pixso-symbol-1267_11535 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    border-radius: 6px 6px 6px 6px;
}
.stroke-wrapper-1267_11535 {
    position: relative;
    width: 16px;
    height: 16px;
}
.stroke-1267_11535 {
    position: absolute;
    inset: 0px;
    border-radius: 6px 6px 6px 6px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-symbol-1267_11536 {
    width: 16px;
    height: 16px;
    overflow: hidden;
    position: relative;
    border-radius: 6px 6px 6px 6px;
}
.Pixso-instance-5546_8590 {
    width: 10px;
    height: 10px;
}
.Pixso-symbol-1267_11538 {
    width: 16px;
    height: 16px;
    overflow: hidden;
    position: relative;
    border-radius: 6px 6px 6px 6px;
}
.Pixso-instance-5546_8611 {
    width: 10px;
    height: 10px;
}
.Pixso-symbol-5547_8767 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    border-radius: 8px 8px 8px 8px;
}
.stroke-wrapper-5547_8767 {
    position: relative;
    width: 20px;
    height: 20px;
}
.stroke-5547_8767 {
    position: absolute;
    inset: 0px;
    border-radius: 8px 8px 8px 8px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-symbol-5547_8768 {
    width: 20px;
    height: 20px;
    overflow: hidden;
    position: relative;
    border-radius: 8px 8px 8px 8px;
}
.Pixso-instance-5547_8769 {
    width: 12px;
    height: 12px;
}
.Pixso-symbol-5547_8770 {
    width: 20px;
    height: 20px;
    overflow: hidden;
    position: relative;
    border-radius: 8px 8px 8px 8px;
}
.Pixso-instance-5547_8771 {
    width: 12px;
    height: 12px;
}
.Pixso-symbol-5547_8839 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    border-radius: 10px 10px 10px 10px;
}
.stroke-wrapper-5547_8839 {
    position: relative;
    width: 24px;
    height: 24px;
}
.stroke-5547_8839 {
    position: absolute;
    inset: 0px;
    border-radius: 10px 10px 10px 10px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-symbol-5547_8840 {
    width: 24px;
    height: 24px;
    overflow: hidden;
    position: relative;
    border-radius: 10px 10px 10px 10px;
}
.Pixso-instance-5547_8841 {
    width: 16px;
    height: 16px;
}
.Pixso-symbol-5547_8842 {
    width: 24px;
    height: 24px;
    overflow: hidden;
    position: relative;
    border-radius: 10px 10px 10px 10px;
}
.Pixso-instance-5547_8843 {
    width: 16px;
    height: 16px;
}
.Pixso-symbol-5546_8638 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    border-radius: 6px 6px 6px 6px;
}
.stroke-wrapper-5546_8638 {
    position: relative;
    width: 16px;
    height: 16px;
}
.stroke-5546_8638 {
    position: absolute;
    inset: 0px;
    border-radius: 6px 6px 6px 6px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-symbol-5546_8639 {
    width: 16px;
    height: 16px;
    overflow: hidden;
    position: relative;
    border-radius: 6px 6px 6px 6px;
}
.Pixso-instance-5546_8640 {
    width: 10px;
    height: 10px;
}
.Pixso-symbol-5546_8641 {
    width: 16px;
    height: 16px;
    overflow: hidden;
    position: relative;
    border-radius: 6px 6px 6px 6px;
}
.Pixso-instance-5546_8642 {
    width: 10px;
    height: 10px;
}
.Pixso-symbol-5547_8772 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    border-radius: 8px 8px 8px 8px;
}
.stroke-wrapper-5547_8772 {
    position: relative;
    width: 20px;
    height: 20px;
}
.stroke-5547_8772 {
    position: absolute;
    inset: 0px;
    border-radius: 8px 8px 8px 8px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-symbol-5547_8773 {
    width: 20px;
    height: 20px;
    overflow: hidden;
    position: relative;
    border-radius: 8px 8px 8px 8px;
}
.Pixso-instance-5547_8774 {
    width: 12px;
    height: 12px;
}
.Pixso-symbol-5547_8775 {
    width: 20px;
    height: 20px;
    overflow: hidden;
    position: relative;
    border-radius: 8px 8px 8px 8px;
}
.Pixso-instance-5547_8776 {
    width: 12px;
    height: 12px;
}
.Pixso-symbol-5547_8844 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    border-radius: 10px 10px 10px 10px;
}
.stroke-wrapper-5547_8844 {
    position: relative;
    width: 24px;
    height: 24px;
}
.stroke-5547_8844 {
    position: absolute;
    inset: 0px;
    border-radius: 10px 10px 10px 10px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-symbol-5547_8845 {
    width: 24px;
    height: 24px;
    overflow: hidden;
    position: relative;
    border-radius: 10px 10px 10px 10px;
}
.Pixso-instance-5547_8846 {
    width: 16px;
    height: 16px;
}
.Pixso-symbol-5547_8847 {
    width: 24px;
    height: 24px;
    overflow: hidden;
    position: relative;
    border-radius: 10px 10px 10px 10px;
}
.Pixso-instance-5547_8848 {
    width: 16px;
    height: 16px;
}
.Pixso-symbol-1267_11550 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    border-radius: 6px 6px 6px 6px;
}
.stroke-wrapper-1267_11550 {
    position: relative;
    width: 16px;
    height: 16px;
}
.stroke-1267_11550 {
    position: absolute;
    inset: 0px;
    border-radius: 6px 6px 6px 6px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-symbol-1267_11551 {
    width: 16px;
    height: 16px;
    overflow: hidden;
    position: relative;
    border-radius: 6px 6px 6px 6px;
}
.Pixso-instance-5546_8623 {
    width: 10px;
    height: 10px;
}
.Pixso-symbol-1267_11553 {
    width: 16px;
    height: 16px;
    overflow: hidden;
    position: relative;
    border-radius: 6px 6px 6px 6px;
}
.Pixso-instance-5546_8617 {
    width: 10px;
    height: 10px;
}
.Pixso-symbol-5547_8777 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    border-radius: 8px 8px 8px 8px;
}
.stroke-wrapper-5547_8777 {
    position: relative;
    width: 20px;
    height: 20px;
}
.stroke-5547_8777 {
    position: absolute;
    inset: 0px;
    border-radius: 8px 8px 8px 8px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-symbol-5547_8778 {
    width: 20px;
    height: 20px;
    overflow: hidden;
    position: relative;
    border-radius: 8px 8px 8px 8px;
}
.Pixso-instance-5547_8779 {
    width: 12px;
    height: 12px;
}
.Pixso-symbol-5547_8780 {
    width: 20px;
    height: 20px;
    overflow: hidden;
    position: relative;
    border-radius: 8px 8px 8px 8px;
}
.Pixso-instance-5547_8781 {
    width: 12px;
    height: 12px;
}
.Pixso-symbol-5547_8849 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    border-radius: 10px 10px 10px 10px;
}
.stroke-wrapper-5547_8849 {
    position: relative;
    width: 24px;
    height: 24px;
}
.stroke-5547_8849 {
    position: absolute;
    inset: 0px;
    border-radius: 10px 10px 10px 10px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-symbol-5547_8850 {
    width: 24px;
    height: 24px;
    overflow: hidden;
    position: relative;
    border-radius: 10px 10px 10px 10px;
}
.Pixso-instance-5547_8851 {
    width: 16px;
    height: 16px;
}
.Pixso-symbol-5547_8852 {
    width: 24px;
    height: 24px;
    overflow: hidden;
    position: relative;
    border-radius: 10px 10px 10px 10px;
}
.Pixso-instance-5547_8853 {
    width: 16px;
    height: 16px;
}

.Pixso-instance-5546_8584 .Pixso-vector-5546_8579 {
    width: 71.87%;
    height: 49.99%;
    position: absolute;
    left: 15.63%;
    right: 12.5%;
    top: 28.13%;
    bottom: 21.88%;
}
.Pixso-instance-5546_8584 .Pixso-vector-5546_8578 {
    width: 100%;
    height: 100%;
    position: absolute;
    left: 0%;
    right: 0%;
    top: 0%;
    bottom: 0%;
}
.Pixso-instance-5546_8584 .Pixso-symbol-5546_8580 {
    width: 10px;
    height: 10px;
    overflow: hidden;
    position: absolute;
    left: 3px;
    top: 3px;
    background-color: transparent;
}
.Pixso-instance-5546_8596 .Pixso-vector-5546_8570 {
    width: 68.74%;
    height: 0%;
    position: absolute;
    left: 15.63%;
    right: 15.63%;
    top: 50%;
    bottom: 50%;
}
.Pixso-instance-5546_8596 .Pixso-vector-5546_8569 {
    width: 100%;
    height: 100%;
    position: absolute;
    left: 0%;
    right: 0%;
    top: 0%;
    bottom: 0%;
}
.Pixso-instance-5546_8596 .Pixso-symbol-5546_8576 {
    width: 10px;
    height: 10px;
    overflow: hidden;
    position: absolute;
    left: 3px;
    top: 3px;
    background-color: transparent;
}
.Pixso-instance-5547_8764 .Pixso-vector-5546_8578 {
    width: 100%;
    height: 100%;
    position: absolute;
    left: 0%;
    right: 0%;
    top: 0%;
    bottom: 0%;
}
.Pixso-instance-5547_8764 .Pixso-vector-5546_8579 {
    width: 71.87%;
    height: 50%;
    position: absolute;
    left: 15.63%;
    right: 12.5%;
    top: 28.12%;
    bottom: 21.88%;
}
.Pixso-instance-5547_8764 .Pixso-symbol-5546_8580 {
    width: 12px;
    height: 12px;
    overflow: hidden;
    position: absolute;
    left: 4px;
    top: 4px;
    background-color: transparent;
}
.Pixso-instance-5547_8766 .Pixso-vector-5546_8569 {
    width: 100%;
    height: 100%;
    position: absolute;
    left: 0%;
    right: 0%;
    top: 0%;
    bottom: 0%;
}
.Pixso-instance-5547_8766 .Pixso-vector-5546_8570 {
    width: 68.74%;
    height: 0%;
    position: absolute;
    left: 15.63%;
    right: 15.63%;
    top: 50%;
    bottom: 50%;
}
.Pixso-instance-5547_8766 .Pixso-symbol-5546_8576 {
    width: 12px;
    height: 12px;
    overflow: hidden;
    position: absolute;
    left: 4px;
    top: 4px;
    background-color: transparent;
}
.Pixso-instance-5547_8836 .Pixso-vector-5546_8578 {
    width: 100%;
    height: 100%;
    position: absolute;
    left: 0%;
    right: 0%;
    top: 0%;
    bottom: 0%;
}
.Pixso-instance-5547_8836 .Pixso-vector-5546_8579 {
    width: 71.87%;
    height: 50%;
    position: absolute;
    left: 15.63%;
    right: 12.5%;
    top: 28.13%;
    bottom: 21.87%;
}
.Pixso-instance-5547_8836 .Pixso-symbol-5546_8580 {
    width: 16px;
    height: 16px;
    overflow: hidden;
    position: absolute;
    left: 4px;
    top: 4px;
    background-color: transparent;
}
.Pixso-instance-5547_8838 .Pixso-vector-5546_8569 {
    width: 100%;
    height: 100%;
    position: absolute;
    left: 0%;
    right: 0%;
    top: 0%;
    bottom: 0%;
}
.Pixso-instance-5547_8838 .Pixso-vector-5546_8570 {
    width: 68.74%;
    height: 0%;
    position: absolute;
    left: 15.63%;
    right: 15.63%;
    top: 50%;
    bottom: 50%;
}
.Pixso-instance-5547_8838 .Pixso-symbol-5546_8576 {
    width: 16px;
    height: 16px;
    overflow: hidden;
    position: absolute;
    left: 4px;
    top: 4px;
    background-color: transparent;
}
.Pixso-instance-5546_8590 .Pixso-vector-5546_8579 {
    width: 71.87%;
    height: 49.99%;
    position: absolute;
    left: 15.63%;
    right: 12.5%;
    top: 28.13%;
    bottom: 21.88%;
}
.Pixso-instance-5546_8590 .Pixso-vector-5546_8578 {
    width: 100%;
    height: 100%;
    position: absolute;
    left: 0%;
    right: 0%;
    top: 0%;
    bottom: 0%;
}
.Pixso-instance-5546_8590 .Pixso-symbol-5546_8580 {
    width: 10px;
    height: 10px;
    overflow: hidden;
    position: absolute;
    left: 3px;
    top: 3px;
    background-color: transparent;
}
.Pixso-instance-5546_8611 .Pixso-vector-5546_8570 {
    width: 68.74%;
    height: 0%;
    position: absolute;
    left: 15.63%;
    right: 15.63%;
    top: 50%;
    bottom: 50%;
}
.Pixso-instance-5546_8611 .Pixso-vector-5546_8569 {
    width: 100%;
    height: 100%;
    position: absolute;
    left: 0%;
    right: 0%;
    top: 0%;
    bottom: 0%;
}
.Pixso-instance-5546_8611 .Pixso-symbol-5546_8576 {
    width: 10px;
    height: 10px;
    overflow: hidden;
    position: absolute;
    left: 3px;
    top: 3px;
    background-color: transparent;
}
.Pixso-instance-5547_8769 .Pixso-vector-5546_8578 {
    width: 100%;
    height: 100%;
    position: absolute;
    left: 0%;
    right: 0%;
    top: 0%;
    bottom: 0%;
}
.Pixso-instance-5547_8769 .Pixso-vector-5546_8579 {
    width: 71.87%;
    height: 50%;
    position: absolute;
    left: 15.63%;
    right: 12.5%;
    top: 28.12%;
    bottom: 21.88%;
}
.Pixso-instance-5547_8769 .Pixso-symbol-5546_8580 {
    width: 12px;
    height: 12px;
    overflow: hidden;
    position: absolute;
    left: 4px;
    top: 4px;
    background-color: transparent;
}
.Pixso-instance-5547_8771 .Pixso-vector-5546_8569 {
    width: 100%;
    height: 100%;
    position: absolute;
    left: 0%;
    right: 0%;
    top: 0%;
    bottom: 0%;
}
.Pixso-instance-5547_8771 .Pixso-vector-5546_8570 {
    width: 68.74%;
    height: 0%;
    position: absolute;
    left: 15.63%;
    right: 15.63%;
    top: 50%;
    bottom: 50%;
}
.Pixso-instance-5547_8771 .Pixso-symbol-5546_8576 {
    width: 12px;
    height: 12px;
    overflow: hidden;
    position: absolute;
    left: 4px;
    top: 4px;
    background-color: transparent;
}
.Pixso-instance-5547_8841 .Pixso-vector-5546_8578 {
    width: 100%;
    height: 100%;
    position: absolute;
    left: 0%;
    right: 0%;
    top: 0%;
    bottom: 0%;
}
.Pixso-instance-5547_8841 .Pixso-vector-5546_8579 {
    width: 71.87%;
    height: 50%;
    position: absolute;
    left: 15.63%;
    right: 12.5%;
    top: 28.13%;
    bottom: 21.87%;
}
.Pixso-instance-5547_8841 .Pixso-symbol-5546_8580 {
    width: 16px;
    height: 16px;
    overflow: hidden;
    position: absolute;
    left: 4px;
    top: 4px;
    background-color: transparent;
}
.Pixso-instance-5547_8843 .Pixso-vector-5546_8569 {
    width: 100%;
    height: 100%;
    position: absolute;
    left: 0%;
    right: 0%;
    top: 0%;
    bottom: 0%;
}
.Pixso-instance-5547_8843 .Pixso-vector-5546_8570 {
    width: 68.74%;
    height: 0%;
    position: absolute;
    left: 15.63%;
    right: 15.63%;
    top: 50%;
    bottom: 50%;
}
.Pixso-instance-5547_8843 .Pixso-symbol-5546_8576 {
    width: 16px;
    height: 16px;
    overflow: hidden;
    position: absolute;
    left: 4px;
    top: 4px;
    background-color: transparent;
}
.Pixso-instance-5546_8640 .Pixso-vector-5546_8579 {
    width: 71.87%;
    height: 49.99%;
    position: absolute;
    left: 15.63%;
    right: 12.5%;
    top: 28.13%;
    bottom: 21.88%;
}
.Pixso-instance-5546_8640 .Pixso-vector-5546_8578 {
    width: 100%;
    height: 100%;
    position: absolute;
    left: 0%;
    right: 0%;
    top: 0%;
    bottom: 0%;
}
.Pixso-instance-5546_8640 .Pixso-symbol-5546_8580 {
    width: 10px;
    height: 10px;
    overflow: hidden;
    position: absolute;
    left: 3px;
    top: 3px;
    background-color: transparent;
}
.Pixso-instance-5546_8642 .Pixso-vector-5546_8570 {
    width: 68.74%;
    height: 0%;
    position: absolute;
    left: 15.63%;
    right: 15.63%;
    top: 50%;
    bottom: 50%;
}
.Pixso-instance-5546_8642 .Pixso-vector-5546_8569 {
    width: 100%;
    height: 100%;
    position: absolute;
    left: 0%;
    right: 0%;
    top: 0%;
    bottom: 0%;
}
.Pixso-instance-5546_8642 .Pixso-symbol-5546_8576 {
    width: 10px;
    height: 10px;
    overflow: hidden;
    position: absolute;
    left: 3px;
    top: 3px;
    background-color: transparent;
}
.Pixso-instance-5547_8774 .Pixso-vector-5546_8578 {
    width: 100%;
    height: 100%;
    position: absolute;
    left: 0%;
    right: 0%;
    top: 0%;
    bottom: 0%;
}
.Pixso-instance-5547_8774 .Pixso-vector-5546_8579 {
    width: 71.87%;
    height: 50%;
    position: absolute;
    left: 15.63%;
    right: 12.5%;
    top: 28.12%;
    bottom: 21.88%;
}
.Pixso-instance-5547_8774 .Pixso-symbol-5546_8580 {
    width: 12px;
    height: 12px;
    overflow: hidden;
    position: absolute;
    left: 4px;
    top: 4px;
    background-color: transparent;
}
.Pixso-instance-5547_8776 .Pixso-vector-5546_8569 {
    width: 100%;
    height: 100%;
    position: absolute;
    left: 0%;
    right: 0%;
    top: 0%;
    bottom: 0%;
}
.Pixso-instance-5547_8776 .Pixso-vector-5546_8570 {
    width: 68.74%;
    height: 0%;
    position: absolute;
    left: 15.63%;
    right: 15.63%;
    top: 50%;
    bottom: 50%;
}
.Pixso-instance-5547_8776 .Pixso-symbol-5546_8576 {
    width: 12px;
    height: 12px;
    overflow: hidden;
    position: absolute;
    left: 4px;
    top: 4px;
    background-color: transparent;
}
.Pixso-instance-5547_8846 .Pixso-vector-5546_8578 {
    width: 100%;
    height: 100%;
    position: absolute;
    left: 0%;
    right: 0%;
    top: 0%;
    bottom: 0%;
}
.Pixso-instance-5547_8846 .Pixso-vector-5546_8579 {
    width: 71.87%;
    height: 50%;
    position: absolute;
    left: 15.63%;
    right: 12.5%;
    top: 28.13%;
    bottom: 21.87%;
}
.Pixso-instance-5547_8846 .Pixso-symbol-5546_8580 {
    width: 16px;
    height: 16px;
    overflow: hidden;
    position: absolute;
    left: 4px;
    top: 4px;
    background-color: transparent;
}
.Pixso-instance-5547_8848 .Pixso-vector-5546_8569 {
    width: 100%;
    height: 100%;
    position: absolute;
    left: 0%;
    right: 0%;
    top: 0%;
    bottom: 0%;
}
.Pixso-instance-5547_8848 .Pixso-vector-5546_8570 {
    width: 68.74%;
    height: 0%;
    position: absolute;
    left: 15.63%;
    right: 15.63%;
    top: 50%;
    bottom: 50%;
}
.Pixso-instance-5547_8848 .Pixso-symbol-5546_8576 {
    width: 16px;
    height: 16px;
    overflow: hidden;
    position: absolute;
    left: 4px;
    top: 4px;
    background-color: transparent;
}
.Pixso-instance-5546_8623 .Pixso-vector-5546_8579 {
    width: 71.87%;
    height: 49.99%;
    position: absolute;
    left: 15.63%;
    right: 12.5%;
    top: 28.13%;
    bottom: 21.88%;
}
.Pixso-instance-5546_8623 .Pixso-vector-5546_8578 {
    width: 100%;
    height: 100%;
    position: absolute;
    left: 0%;
    right: 0%;
    top: 0%;
    bottom: 0%;
}
.Pixso-instance-5546_8623 .Pixso-symbol-5546_8580 {
    width: 10px;
    height: 10px;
    overflow: hidden;
    position: absolute;
    left: 3px;
    top: 3px;
    background-color: transparent;
}
.Pixso-instance-5546_8617 .Pixso-vector-5546_8570 {
    width: 68.74%;
    height: 0%;
    position: absolute;
    left: 15.63%;
    right: 15.63%;
    top: 50%;
    bottom: 50%;
}
.Pixso-instance-5546_8617 .Pixso-vector-5546_8569 {
    width: 100%;
    height: 100%;
    position: absolute;
    left: 0%;
    right: 0%;
    top: 0%;
    bottom: 0%;
}
.Pixso-instance-5546_8617 .Pixso-symbol-5546_8576 {
    width: 10px;
    height: 10px;
    overflow: hidden;
    position: absolute;
    left: 3px;
    top: 3px;
    background-color: transparent;
}
.Pixso-instance-5547_8779 .Pixso-vector-5546_8578 {
    width: 100%;
    height: 100%;
    position: absolute;
    left: 0%;
    right: 0%;
    top: 0%;
    bottom: 0%;
}
.Pixso-instance-5547_8779 .Pixso-vector-5546_8579 {
    width: 71.87%;
    height: 50%;
    position: absolute;
    left: 15.63%;
    right: 12.5%;
    top: 28.12%;
    bottom: 21.88%;
}
.Pixso-instance-5547_8779 .Pixso-symbol-5546_8580 {
    width: 12px;
    height: 12px;
    overflow: hidden;
    position: absolute;
    left: 4px;
    top: 4px;
    background-color: transparent;
}
.Pixso-instance-5547_8781 .Pixso-vector-5546_8569 {
    width: 100%;
    height: 100%;
    position: absolute;
    left: 0%;
    right: 0%;
    top: 0%;
    bottom: 0%;
}
.Pixso-instance-5547_8781 .Pixso-vector-5546_8570 {
    width: 68.74%;
    height: 0%;
    position: absolute;
    left: 15.63%;
    right: 15.63%;
    top: 50%;
    bottom: 50%;
}
.Pixso-instance-5547_8781 .Pixso-symbol-5546_8576 {
    width: 12px;
    height: 12px;
    overflow: hidden;
    position: absolute;
    left: 4px;
    top: 4px;
    background-color: transparent;
}
.Pixso-instance-5547_8851 .Pixso-vector-5546_8578 {
    width: 100%;
    height: 100%;
    position: absolute;
    left: 0%;
    right: 0%;
    top: 0%;
    bottom: 0%;
}
.Pixso-instance-5547_8851 .Pixso-vector-5546_8579 {
    width: 71.87%;
    height: 50%;
    position: absolute;
    left: 15.63%;
    right: 12.5%;
    top: 28.13%;
    bottom: 21.87%;
}
.Pixso-instance-5547_8851 .Pixso-symbol-5546_8580 {
    width: 16px;
    height: 16px;
    overflow: hidden;
    position: absolute;
    left: 4px;
    top: 4px;
    background-color: transparent;
}
.Pixso-instance-5547_8853 .Pixso-vector-5546_8569 {
    width: 100%;
    height: 100%;
    position: absolute;
    left: 0%;
    right: 0%;
    top: 0%;
    bottom: 0%;
}
.Pixso-instance-5547_8853 .Pixso-vector-5546_8570 {
    width: 68.74%;
    height: 0%;
    position: absolute;
    left: 15.63%;
    right: 15.63%;
    top: 50%;
    bottom: 50%;
}
.Pixso-instance-5547_8853 .Pixso-symbol-5546_8576 {
    width: 16px;
    height: 16px;
    overflow: hidden;
    position: absolute;
    left: 4px;
    top: 4px;
    background-color: transparent;
}
</style>
