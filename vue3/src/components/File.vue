<template>
    <div class="component-5579_151365">
        <div id="5579_151365" class="Pixso-symbol-5579_151365">
            <div
                id="5579_151366"
                class="Pixso-symbol-5579_151366"
                v-if="Format === 'Outline' && Weight === 'Regular'"
            >
                <slot name="slot_5579_151367">
                    <div
                        id="5579_151367"
                        class="Pixso-vector-5579_151367"
                    ></div>
                </slot>
            </div>
            <div
                id="5579_151372"
                class="Pixso-symbol-5579_151372"
                v-if="Format === 'Outline' && Weight === 'Bold'"
            >
                <slot name="slot_5579_151373">
                    <div
                        id="5579_151373"
                        class="Pixso-vector-5579_151373"
                    ></div>
                </slot>
            </div>
            <div
                id="5579_151374"
                class="Pixso-symbol-5579_151374"
                v-if="Format === 'Outline' && Weight === 'Fill'"
            >
                <slot name="slot_5579_151375">
                    <div
                        id="5579_151375"
                        class="Pixso-vector-5579_151375"
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
.Pixso-symbol-5579_151365 {
}
.Pixso-symbol-5579_151366 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5579_151367 {
    width: 68.74%;
    height: 81.24%;
    background-image: url(@/assets/images/Vector316.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 15.63%;
    right: 15.63%;
    top: 9.38%;
    bottom: 9.38%;
}
.Pixso-symbol-5579_151372 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5579_151373 {
    width: 71.88%;
    height: 84.38%;
    background-image: url(@/assets/images/Vector314.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 14.06%;
    right: 14.06%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-symbol-5579_151374 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5579_151375 {
    width: 68.74%;
    height: 81.24%;
    background-image: url(@/assets/images/Vector315.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 15.63%;
    right: 15.63%;
    top: 9.38%;
    bottom: 9.38%;
}
</style>
