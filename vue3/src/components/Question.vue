<template>
    <div class="component-5579_153175">
        <div id="5579_153175" class="Pixso-symbol-5579_153175">
            <div
                id="5579_153176"
                class="Pixso-symbol-5579_153176"
                v-if="Format === 'Outline' && Weight === 'Regular'"
            >
                <slot name="slot_5579_153177">
                    <div
                        id="5579_153177"
                        class="Pixso-vector-5579_153177"
                    ></div>
                </slot>
            </div>
            <div
                id="5579_153182"
                class="Pixso-symbol-5579_153182"
                v-if="Format === 'Outline' && Weight === 'Bold'"
            >
                <slot name="slot_5579_153183">
                    <div
                        id="5579_153183"
                        class="Pixso-vector-5579_153183"
                    ></div>
                </slot>
            </div>
            <div
                id="5579_153184"
                class="Pixso-symbol-5579_153184"
                v-if="Format === 'Outline' && Weight === 'Fill'"
            >
                <slot name="slot_5579_153185">
                    <div
                        id="5579_153185"
                        class="Pixso-vector-5579_153185"
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
.Pixso-symbol-5579_153175 {
}
.Pixso-symbol-5579_153176 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5579_153177 {
    width: 81.24%;
    height: 81.24%;
    background-image: url(@/assets/images/Vector74.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 9.38%;
    right: 9.38%;
    top: 9.38%;
    bottom: 9.38%;
}
.Pixso-symbol-5579_153182 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5579_153183 {
    width: 84.38%;
    height: 84.38%;
    background-image: url(@/assets/images/Vector72.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-symbol-5579_153184 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5579_153185 {
    width: 81.24%;
    height: 81.24%;
    background-image: url(@/assets/images/Vector73.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 9.38%;
    right: 9.38%;
    top: 9.38%;
    bottom: 9.38%;
}
</style>
