<template>
    <div class="component-5579_151879">
        <div id="5579_151879" class="Pixso-symbol-5579_151879">
            <div
                id="5579_151880"
                class="Pixso-symbol-5579_151880"
                v-if="Format === 'Outline' && Weight === 'Regular'"
            >
                <slot name="slot_5579_151881">
                    <div
                        id="5579_151881"
                        class="Pixso-vector-5579_151881"
                    ></div>
                </slot>
            </div>
            <div
                id="5579_151886"
                class="Pixso-symbol-5579_151886"
                v-if="Format === 'Outline' && Weight === 'Bold'"
            >
                <slot name="slot_5579_151887">
                    <div
                        id="5579_151887"
                        class="Pixso-vector-5579_151887"
                    ></div>
                </slot>
            </div>
            <div
                id="5579_151888"
                class="Pixso-symbol-5579_151888"
                v-if="Format === 'Outline' && Weight === 'Fill'"
            >
                <slot name="slot_5579_151889">
                    <div
                        id="5579_151889"
                        class="Pixso-vector-5579_151889"
                    ></div>
                </slot>
            </div>
        </div>
    </div>
</template>
<script lang="ts" setup>
const props = defineProps({
    Format: { type: String },
    Weight: { type: String }
});
</script>
<style>
.Pixso-symbol-5579_151879 {
}
.Pixso-symbol-5579_151880 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5579_151881 {
    width: 75%;
    height: 75%;
    background-image: url(@/assets/images/Vector2027.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 12.5%;
    bottom: 12.5%;
}
.Pixso-symbol-5579_151886 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5579_151887 {
    width: 78.12%;
    height: 78.12%;
    background-image: url(@/assets/images/Vector2025.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 10.94%;
    right: 10.94%;
    top: 10.94%;
    bottom: 10.94%;
}
.Pixso-symbol-5579_151888 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5579_151889 {
    width: 75%;
    height: 75%;
    background-image: url(@/assets/images/Vector2026.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 12.5%;
    bottom: 12.5%;
}
</style>
