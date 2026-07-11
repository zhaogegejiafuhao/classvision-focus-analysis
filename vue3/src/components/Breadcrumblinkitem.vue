<template>
    <div class="component-5523_33776">
        <div id="5523_33776" class="Pixso-symbol-5523_33776">
            <div
                id="5522_33763"
                class="Pixso-symbol-5522_33763"
                v-if="State === 'Default' && Fill === 'None'"
            >
                <slot name="slot_5522_33739" v-if="visible_5594_0">
                    <Circle
                        id="5522_33739"
                        class="Pixso-instance-5522_33739"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <slot name="slot_5522_33761" v-if="visible_5594_11">
                    <p
                        id="5522_33761"
                        class="Pixso-paragraph-5522_33761 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                    >
                        {{ text_5594_7 ?? "Link Item" }}
                    </p>
                </slot>
            </div>
            <div
                id="5594_6674"
                class="Pixso-symbol-5594_6674 fill-gray5-32_4120"
                v-if="State === 'Default' && Fill === 'Subtle'"
            >
                <slot name="slot_5594_6675" v-if="visible_5594_0">
                    <Circle
                        id="5594_6675"
                        class="Pixso-instance-5594_6675"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <slot name="slot_5594_6676" v-if="visible_5594_11">
                    <p
                        id="5594_6676"
                        class="Pixso-paragraph-5594_6676 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                    >
                        {{ text_5594_7 ?? "Link Item" }}
                    </p>
                </slot>
            </div>
            <div
                id="5594_6682"
                class="stroke-wrapper-5594_6682"
                v-if="State === 'Default' && Fill === 'Outlined'"
            >
                <div class="Pixso-symbol-5594_6682">
                    <slot name="slot_5594_6683" v-if="visible_5594_0">
                        <Circle
                            id="5594_6683"
                            class="Pixso-instance-5594_6683"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                    <slot name="slot_5594_6684" v-if="visible_5594_11">
                        <p
                            id="5594_6684"
                            class="Pixso-paragraph-5594_6684 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                        >
                            {{ text_5594_7 ?? "Link Item" }}
                        </p>
                    </slot>
                </div>
                <div class="stroke-5594_6682 stroke-gray30-35_1481"></div>
            </div>
            <div
                id="5594_6695"
                class="Pixso-symbol-5594_6695"
                v-if="State === 'Hover' && Fill === 'None'"
            >
                <slot name="slot_5594_6696" v-if="visible_5594_0">
                    <Circle
                        id="5594_6696"
                        class="Pixso-instance-5594_6696"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <slot name="slot_5594_6697" v-if="visible_5594_11">
                    <p
                        id="5594_6697"
                        class="Pixso-paragraph-5594_6697 fill-brand40-1257_33464-paragraph text-text-smbold-423_3208"
                    >
                        {{ text_5594_7 ?? "Link Item" }}
                    </p>
                </slot>
            </div>
            <div
                id="5594_6724"
                class="Pixso-symbol-5594_6724 fill-brand5-1257_33460"
                v-if="State === 'Hover' && Fill === 'Subtle'"
            >
                <slot name="slot_5594_6725" v-if="visible_5594_0">
                    <Circle
                        id="5594_6725"
                        class="Pixso-instance-5594_6725"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <slot name="slot_5594_6726" v-if="visible_5594_11">
                    <p
                        id="5594_6726"
                        class="Pixso-paragraph-5594_6726 fill-brand40-1257_33464-paragraph text-text-smbold-423_3208"
                    >
                        {{ text_5594_7 ?? "Link Item" }}
                    </p>
                </slot>
            </div>
            <div
                id="5594_6748"
                class="stroke-wrapper-5594_6748"
                v-if="State === 'Hover' && Fill === 'Outlined'"
            >
                <div class="Pixso-symbol-5594_6748">
                    <slot name="slot_5594_6749" v-if="visible_5594_0">
                        <Circle
                            id="5594_6749"
                            class="Pixso-instance-5594_6749"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                    <slot name="slot_5594_6750" v-if="visible_5594_11">
                        <p
                            id="5594_6750"
                            class="Pixso-paragraph-5594_6750 fill-brand40-1257_33464-paragraph text-text-smbold-423_3208"
                        >
                            {{ text_5594_7 ?? "Link Item" }}
                        </p>
                    </slot>
                </div>
                <div class="stroke-5594_6748 stroke-brand30-1257_33463"></div>
            </div>
            <div
                id="5594_6708"
                class="Pixso-symbol-5594_6708"
                v-if="State === 'Active' && Fill === 'None'"
            >
                <slot name="slot_5594_6709" v-if="visible_5594_0">
                    <Circle
                        id="5594_6709"
                        class="Pixso-instance-5594_6709"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <slot name="slot_5594_6710" v-if="visible_5594_11">
                    <p
                        id="5594_6710"
                        class="Pixso-paragraph-5594_6710 fill-brand60-1257_33467-paragraph text-text-smbold-423_3208"
                    >
                        {{ text_5594_7 ?? "Link Item" }}
                    </p>
                </slot>
            </div>
            <div
                id="5594_6732"
                class="Pixso-symbol-5594_6732 fill-brand10-1257_33461"
                v-if="State === 'Active' && Fill === 'Subtle'"
            >
                <slot name="slot_5594_6733" v-if="visible_5594_0">
                    <Circle
                        id="5594_6733"
                        class="Pixso-instance-5594_6733"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <slot name="slot_5594_6734" v-if="visible_5594_11">
                    <p
                        id="5594_6734"
                        class="Pixso-paragraph-5594_6734 fill-brand60-1257_33467-paragraph text-text-smbold-423_3208"
                    >
                        {{ text_5594_7 ?? "Link Item" }}
                    </p>
                </slot>
            </div>
            <div
                id="5594_6756"
                class="stroke-wrapper-5594_6756"
                v-if="State === 'Active' && Fill === 'Outlined'"
            >
                <div class="Pixso-symbol-5594_6756">
                    <slot name="slot_5594_6757" v-if="visible_5594_0">
                        <Circle
                            id="5594_6757"
                            class="Pixso-instance-5594_6757"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                    <slot name="slot_5594_6758" v-if="visible_5594_11">
                        <p
                            id="5594_6758"
                            class="Pixso-paragraph-5594_6758 fill-brand60-1257_33467-paragraph text-text-smbold-423_3208"
                        >
                            {{ text_5594_7 ?? "Link Item" }}
                        </p>
                    </slot>
                </div>
                <div class="stroke-5594_6756 stroke-brand60-1257_33467"></div>
            </div>
            <div
                id="5594_6716"
                class="Pixso-symbol-5594_6716"
                v-if="State === 'Disabled' && Fill === 'None'"
            >
                <slot name="slot_5594_6717" v-if="visible_5594_0">
                    <Circle
                        id="5594_6717"
                        class="Pixso-instance-5594_6717"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <slot name="slot_5594_6718" v-if="visible_5594_11">
                    <p
                        id="5594_6718"
                        class="Pixso-paragraph-5594_6718 fill-gray30-35_1481-paragraph text-text-smbold-423_3208"
                    >
                        {{ text_5594_7 ?? "Link Item" }}
                    </p>
                </slot>
            </div>
            <div
                id="5594_6740"
                class="Pixso-symbol-5594_6740 fill-gray5-32_4120"
                v-if="State === 'Disabled' && Fill === 'Subtle'"
            >
                <slot name="slot_5594_6741" v-if="visible_5594_0">
                    <Circle
                        id="5594_6741"
                        class="Pixso-instance-5594_6741"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
                <slot name="slot_5594_6742" v-if="visible_5594_11">
                    <p
                        id="5594_6742"
                        class="Pixso-paragraph-5594_6742 fill-gray30-35_1481-paragraph text-text-smbold-423_3208"
                    >
                        {{ text_5594_7 ?? "Link Item" }}
                    </p>
                </slot>
            </div>
            <div
                id="5594_6764"
                class="stroke-wrapper-5594_6764"
                v-if="State === 'Disabled' && Fill === 'Outlined'"
            >
                <div class="Pixso-symbol-5594_6764">
                    <slot name="slot_5594_6765" v-if="visible_5594_0">
                        <Circle
                            id="5594_6765"
                            class="Pixso-instance-5594_6765"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                    <slot name="slot_5594_6766" v-if="visible_5594_11">
                        <p
                            id="5594_6766"
                            class="Pixso-paragraph-5594_6766 fill-brand30-1257_33463-paragraph text-text-smbold-423_3208"
                        >
                            {{ text_5594_7 ?? "Link Item" }}
                        </p>
                    </slot>
                </div>
                <div class="stroke-5594_6764 stroke-brand30-1257_33463"></div>
            </div>
        </div>
    </div>
</template>
<script lang="ts" setup>
import Circle from "@/components/Circle.vue";
const props = defineProps({
    visible_5594_0: { type: Boolean, default: true },
    instance_5594_5: { type: String, default: "Component_5578_148941" },
    text_5594_7: { type: String, default: "Link Item" },
    visible_5594_11: { type: Boolean, default: true },
    State: { type: String },
    Fill: { type: String }
});
</script>
<style>
.Pixso-symbol-5523_33776 {
}
.Pixso-symbol-5522_33763 {
    width: auto;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 4px;
    align-items: center;
}
.Pixso-instance-5522_33739 {
    width: 20px;
    height: 20px;
}
.Pixso-paragraph-5522_33761 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-symbol-5594_6674 {
    width: auto;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 4px;
    align-items: center;
    padding: 6px 8px 6px 8px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5594_6675 {
    width: 20px;
    height: 20px;
}
.Pixso-paragraph-5594_6676 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-symbol-5594_6682 {
    width: 100%;
    height: 100%;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 4px;
    align-items: center;
    padding: 6px 8px 6px 8px;
    border-radius: 123px 123px 123px 123px;
}
.stroke-wrapper-5594_6682 {
    position: relative;
    width: auto;
    height: auto;
    display: flex;
}
.stroke-5594_6682 {
    position: absolute;
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5594_6683 {
    width: 20px;
    height: 20px;
}
.Pixso-paragraph-5594_6684 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-symbol-5594_6695 {
    width: auto;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 4px;
    align-items: center;
}
.Pixso-instance-5594_6696 {
    width: 20px;
    height: 20px;
}
.Pixso-paragraph-5594_6697 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-symbol-5594_6724 {
    width: auto;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 4px;
    align-items: center;
    padding: 6px 8px 6px 8px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5594_6725 {
    width: 20px;
    height: 20px;
}
.Pixso-paragraph-5594_6726 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-symbol-5594_6748 {
    width: 100%;
    height: 100%;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 4px;
    align-items: center;
    padding: 6px 8px 6px 8px;
    border-radius: 123px 123px 123px 123px;
}
.stroke-wrapper-5594_6748 {
    position: relative;
    width: auto;
    height: auto;
    display: flex;
}
.stroke-5594_6748 {
    position: absolute;
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5594_6749 {
    width: 20px;
    height: 20px;
}
.Pixso-paragraph-5594_6750 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-symbol-5594_6708 {
    width: auto;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 4px;
    align-items: center;
}
.Pixso-instance-5594_6709 {
    width: 20px;
    height: 20px;
}
.Pixso-paragraph-5594_6710 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-symbol-5594_6732 {
    width: auto;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 4px;
    align-items: center;
    padding: 6px 8px 6px 8px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5594_6733 {
    width: 20px;
    height: 20px;
}
.Pixso-paragraph-5594_6734 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-symbol-5594_6756 {
    width: 100%;
    height: 100%;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 4px;
    align-items: center;
    padding: 6px 8px 6px 8px;
    border-radius: 123px 123px 123px 123px;
}
.stroke-wrapper-5594_6756 {
    position: relative;
    width: auto;
    height: auto;
    display: flex;
}
.stroke-5594_6756 {
    position: absolute;
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5594_6757 {
    width: 20px;
    height: 20px;
}
.Pixso-paragraph-5594_6758 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-symbol-5594_6716 {
    width: auto;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 4px;
    align-items: center;
}
.Pixso-instance-5594_6717 {
    width: 20px;
    height: 20px;
}
.Pixso-paragraph-5594_6718 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-symbol-5594_6740 {
    width: auto;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 4px;
    align-items: center;
    padding: 6px 8px 6px 8px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5594_6741 {
    width: 20px;
    height: 20px;
}
.Pixso-paragraph-5594_6742 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-symbol-5594_6764 {
    width: 100%;
    height: 100%;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 4px;
    align-items: center;
    padding: 6px 8px 6px 8px;
    border-radius: 123px 123px 123px 123px;
}
.stroke-wrapper-5594_6764 {
    position: relative;
    width: auto;
    height: auto;
    display: flex;
}
.stroke-5594_6764 {
    position: absolute;
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5594_6765 {
    width: 20px;
    height: 20px;
}
.Pixso-paragraph-5594_6766 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}

.Pixso-instance-5522_33739 .Pixso-symbol-5578_148941 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5522_33739 .Pixso-vector-5578_148942 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5594_6675 .Pixso-symbol-5578_148941 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5594_6675 .Pixso-vector-5578_148942 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5594_6683 .Pixso-symbol-5578_148941 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5594_6683 .Pixso-vector-5578_148942 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5594_6696 .Pixso-symbol-5578_148941 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5594_6696 .Pixso-vector-5578_148942 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5594_6725 .Pixso-symbol-5578_148941 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5594_6725 .Pixso-vector-5578_148942 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5594_6749 .Pixso-symbol-5578_148941 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5594_6749 .Pixso-vector-5578_148942 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5594_6709 .Pixso-symbol-5578_148941 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5594_6709 .Pixso-vector-5578_148942 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5594_6733 .Pixso-symbol-5578_148941 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5594_6733 .Pixso-vector-5578_148942 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5594_6757 .Pixso-symbol-5578_148941 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5594_6757 .Pixso-vector-5578_148942 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5594_6717 .Pixso-symbol-5578_148941 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5594_6717 .Pixso-vector-5578_148942 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5594_6741 .Pixso-symbol-5578_148941 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5594_6741 .Pixso-vector-5578_148942 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-5594_6765 .Pixso-symbol-5578_148941 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5594_6765 .Pixso-vector-5578_148942 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
</style>
