<template>
    <div class="component-5476_6579">
        <div id="5476_6579" class="Pixso-symbol-5476_6579">
            <div
                id="5476_6566"
                class="stroke-wrapper-5476_6566"
                v-if="Size === 'md'"
            >
                <div class="Pixso-symbol-5476_6566">
                    <slot name="slot_5476_6564">
                        <Plus
                            id="5476_6564"
                            class="Pixso-instance-5476_6564"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div class="stroke-5476_6566 stroke-gray30-35_1481"></div>
            </div>
            <div
                id="5476_6578"
                class="stroke-wrapper-5476_6578"
                v-if="Size === 'sm'"
            >
                <div class="Pixso-symbol-5476_6578">
                    <slot name="slot_5476_6571">
                        <Plus
                            id="5476_6571"
                            class="Pixso-instance-5476_6571"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div class="stroke-5476_6578 stroke-gray30-35_1481"></div>
            </div>
            <div
                id="5476_6577"
                class="stroke-wrapper-5476_6577"
                v-if="Size === 'xs'"
            >
                <div class="Pixso-symbol-5476_6577">
                    <slot name="slot_5476_6574">
                        <Plus
                            id="5476_6574"
                            class="Pixso-instance-5476_6574"
                            Format="Outline"
                            Weight="Bold"
                        />
                    </slot>
                </div>
                <div class="stroke-5476_6577 stroke-gray30-35_1481"></div>
            </div>
        </div>
    </div>
</template>
<script lang="ts" setup>
import Plus from "@/components/Plus.vue";
const props = defineProps({
    Size: { type: String }
});
</script>
<style>
.Pixso-symbol-5476_6579 {
}
.Pixso-symbol-5476_6566 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    border-radius: 20px 20px 20px 20px;
}
.stroke-wrapper-5476_6566 {
    position: relative;
    width: 40px;
    height: 40px;
}
.stroke-5476_6566 {
    position: absolute;
    inset: -0.5px -0.5px -0.5px -0.5px;
    border-radius: 20px 20px 20px 20px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: dashed;
    box-sizing: border-box;
}
.Pixso-instance-5476_6564 {
    width: 20px;
    height: 20px;
}
.Pixso-symbol-5476_6578 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    border-radius: 20px 20px 20px 20px;
}
.stroke-wrapper-5476_6578 {
    position: relative;
    width: 32px;
    height: 32px;
}
.stroke-5476_6578 {
    position: absolute;
    inset: -0.5px -0.5px -0.5px -0.5px;
    border-radius: 20px 20px 20px 20px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: dashed;
    box-sizing: border-box;
}
.Pixso-instance-5476_6571 {
    width: 16px;
    height: 16px;
}
.Pixso-symbol-5476_6577 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    border-radius: 20px 20px 20px 20px;
}
.stroke-wrapper-5476_6577 {
    position: relative;
    width: 24px;
    height: 24px;
}
.stroke-5476_6577 {
    position: absolute;
    inset: -0.5px -0.5px -0.5px -0.5px;
    border-radius: 20px 20px 20px 20px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: dashed;
    box-sizing: border-box;
}
.Pixso-instance-5476_6574 {
    width: 12px;
    height: 12px;
}

.Pixso-instance-5476_6564 .Pixso-symbol-5579_150999 {
    width: 20px;
    height: 20px;
    position: absolute;
    left: 10px;
    top: 10px;
    background-color: transparent;
}
.Pixso-instance-5476_6564 .Pixso-vector-5579_151000 {
    width: 78.12%;
    height: 78.12%;
    position: absolute;
    left: 10.94%;
    right: 10.94%;
    top: 10.94%;
    bottom: 10.94%;
}
.Pixso-instance-5476_6571 .Pixso-symbol-5579_150999 {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 8px;
    top: 8px;
    background-color: transparent;
}
.Pixso-instance-5476_6571 .Pixso-vector-5579_151000 {
    width: 78.12%;
    height: 78.12%;
    position: absolute;
    left: 10.94%;
    right: 10.94%;
    top: 10.94%;
    bottom: 10.94%;
}
.Pixso-instance-5476_6574 .Pixso-symbol-5579_150999 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 6px;
    top: 6px;
    background-color: transparent;
}
.Pixso-instance-5476_6574 .Pixso-vector-5579_151000 {
    width: 78.12%;
    height: 78.12%;
    position: absolute;
    left: 10.94%;
    right: 10.94%;
    top: 10.94%;
    bottom: 10.94%;
}
</style>
